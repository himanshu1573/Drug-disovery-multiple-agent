from __future__ import annotations

from typing import Any

import pytest
from fastapi.testclient import TestClient

from agents import llm_policy
from agents.llm_credentials import LLMCredentials, current_llm_credentials
from agents.provider_select import ProviderSelection

SECRET = "sk-user-secret"
SESSION_HEADERS = {"X-LLM-Provider": "openai", "X-LLM-API-Key": SECRET}


async def _no_server_provider() -> ProviderSelection:
    return ProviderSelection(provider="none", locked=True, llm_calls_enabled=False, error="no server keys")


@pytest.fixture
def app_module(monkeypatch: pytest.MonkeyPatch, tmp_path):
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path / "artifacts"))
    from ui_api import app as module  # import after env set

    # Simulate a public demo server with no LLM key of its own; avoids live provider probes.
    monkeypatch.setattr(module, "select_provider_once", _no_server_provider)
    return module


def _drain_events(module: Any, run_id: str) -> list[Any]:
    queue = module.BUS.subscribe(run_id)
    events = []
    while not queue.empty():
        events.append(queue.get_nowait())
    return events


def test_session_key_reaches_background_run_but_not_persisted_request(app_module, monkeypatch) -> None:
    seen: dict[str, Any] = {}

    async def _fake_run(request, progress_cb=None):
        seen["creds"] = current_llm_credentials()
        seen["openai_key"] = llm_policy.openai_api_key()
        seen["request_json"] = request.model_dump_json()
        return {"status": "ok"}

    monkeypatch.setattr(app_module, "run_collection_graph", _fake_run)
    resp = TestClient(app_module.app).post("/api/runs", json={"gene_symbol": "KRAS"}, headers=SESSION_HEADERS)

    assert resp.status_code == 200
    assert seen["creds"] == LLMCredentials(provider="openai", api_key=SECRET)
    assert seen["openai_key"] == SECRET
    # CollectorRequest is persisted to dossiers/run state; the key must never be part of it.
    assert SECRET not in seen["request_json"]


def test_run_without_any_key_fails_fast(app_module, monkeypatch) -> None:
    started = False

    async def _fake_run(request, progress_cb=None):
        nonlocal started
        started = True

    monkeypatch.setattr(app_module, "run_collection_graph", _fake_run)
    resp = TestClient(app_module.app).post("/api/runs", json={"gene_symbol": "KRAS"})

    assert resp.status_code == 401
    assert "API key" in resp.json()["detail"]
    assert started is False


@pytest.mark.parametrize(
    "headers",
    [
        {"X-LLM-Provider": "openai"},
        {"X-LLM-API-Key": "sk-x"},
        {"X-LLM-Provider": "anthropic", "X-LLM-API-Key": "sk-x"},
    ],
)
def test_malformed_session_headers_are_rejected(app_module, headers: dict[str, str]) -> None:
    resp = TestClient(app_module.app).post("/api/runs", json={"gene_symbol": "KRAS"}, headers=headers)
    assert resp.status_code == 400


def test_run_failure_error_is_redacted(app_module, monkeypatch) -> None:
    async def _failing_run(request, progress_cb=None):
        raise RuntimeError(f"401 Incorrect API key provided: {llm_policy.openai_api_key()}")

    monkeypatch.setattr(app_module, "run_collection_graph", _failing_run)
    run_id = "run-redact-key"
    resp = TestClient(app_module.app).post(
        "/api/runs", json={"gene_symbol": "KRAS", "run_id": run_id}, headers=SESSION_HEADERS
    )

    assert resp.status_code == 200
    failed = [e for e in _drain_events(app_module, run_id) if e.event == "run_failed"]
    assert failed
    assert SECRET not in failed[0].data["error"]
    assert "[REDACTED]" in failed[0].data["error"]


def test_validate_session_key_reports_invalid_key_without_echoing_it(app_module, monkeypatch) -> None:
    async def _fake_probe_openai(*, model: str, api_key: str | None = None) -> tuple[bool, str | None]:
        return False, f"AuthenticationError: Incorrect API key provided: {api_key}"

    monkeypatch.setattr("agents.provider_select._probe_openai", _fake_probe_openai)
    resp = TestClient(app_module.app).post("/api/session/validate", headers=SESSION_HEADERS)

    assert resp.status_code == 200
    body = resp.json()
    assert body["valid"] is False
    assert body["provider"] == "openai"
    assert SECRET not in body["error"]


def test_validate_session_key_accepts_working_gemini_key(app_module, monkeypatch) -> None:
    probed: dict[str, str | None] = {}

    async def _fake_probe_google(*, model: str, api_key: str | None = None) -> tuple[bool, str | None]:
        probed["api_key"] = api_key
        return True, None

    monkeypatch.setattr("agents.provider_select._probe_google", _fake_probe_google)
    headers = {"X-LLM-Provider": "gemini", "X-LLM-API-Key": "user-google"}
    resp = TestClient(app_module.app).post("/api/session/validate", headers=headers)

    assert resp.status_code == 200
    assert resp.json() == {"valid": True, "provider": "google", "error": None}
    assert probed["api_key"] == "user-google"


def test_validate_session_key_requires_headers(app_module) -> None:
    resp = TestClient(app_module.app).post("/api/session/validate")
    assert resp.status_code == 400
