from __future__ import annotations

import asyncio

import pytest
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from agents import llm_policy
from agents.llm_credentials import (
    LLMCredentials,
    current_llm_credentials,
    use_llm_credentials,
)

USER_OPENAI = LLMCredentials(provider="openai", api_key="sk-user")
USER_GOOGLE = LLMCredentials(provider="google", api_key="user-google")


@pytest.fixture(autouse=True)
def _server_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "sk-server")
    monkeypatch.setenv("GOOGLE_API_KEY", "server-google")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("A4T_LLM_PROVIDER", raising=False)


def test_session_key_replaces_server_keys_only_inside_context() -> None:
    with use_llm_credentials(USER_OPENAI):
        assert llm_policy.openai_api_key() == "sk-user"
        # The server's key for the other provider must not be spent on a session run.
        assert llm_policy.google_api_key() is None
        assert llm_policy.preferred_provider() == "openai"
    assert current_llm_credentials() is None
    assert llm_policy.openai_api_key() == "sk-server"


def test_get_llm_uses_session_key_not_server_env_key() -> None:
    with use_llm_credentials(USER_OPENAI):
        llm = llm_policy.get_llm("gpt-4o-mini")
    assert isinstance(llm, ChatOpenAI)
    assert llm.openai_api_key is not None
    assert llm.openai_api_key.get_secret_value() == "sk-user"


def test_gemini_session_remaps_openai_default_models() -> None:
    # Agent defaults are OpenAI names (e.g. the `gpt-5` profile default).
    with use_llm_credentials(USER_GOOGLE):
        llm = llm_policy.get_llm("gpt-5")
    assert isinstance(llm, ChatGoogleGenerativeAI)
    assert llm.google_api_key is not None
    assert llm.google_api_key.get_secret_value() == "user-google"


def test_gemini_only_server_remaps_openai_default_models(monkeypatch: pytest.MonkeyPatch) -> None:
    # Previously raised `OpenAIError: Missing credentials` before any Gemini fallback was tried.
    monkeypatch.delenv("OPENAI_API_KEY")
    assert isinstance(llm_policy.get_llm("gpt-5"), ChatGoogleGenerativeAI)


async def test_fallback_candidates_resolve_to_session_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    attempts: list[tuple[str, str]] = []

    async def _fake_guarded(runnable, prompt, *, provider):
        attempts.append((provider, runnable.model))
        raise ValueError("boom")

    monkeypatch.setattr(llm_policy, "_ainvoke_guarded", _fake_guarded)
    with use_llm_credentials(USER_GOOGLE), pytest.raises(RuntimeError, match="All LLM candidates failed"):
        await llm_policy.ainvoke_with_fallbacks(prompt="hi", primary_model="gpt-5", role="reasoning")

    # `gpt-5` and the Gemini fallback resolve to the same model, so it is attempted once.
    assert attempts == [("google", "gemini-2.5-flash")]


def test_session_key_enables_llm_calls_disabled_by_server_probe(monkeypatch: pytest.MonkeyPatch) -> None:
    # provider_select sets this process-wide when the server itself has no working key.
    monkeypatch.setenv("A4T_LLM_CALLS_ENABLED", "0")
    assert llm_policy.llm_calls_enabled() is False
    with use_llm_credentials(USER_GOOGLE):
        assert llm_policy.llm_calls_enabled() is True


async def test_concurrent_sessions_do_not_see_each_others_keys() -> None:
    async def _read_key(creds: LLMCredentials) -> str | None:
        with use_llm_credentials(creds):
            await asyncio.sleep(0)  # let the other session run in between
            return llm_policy.openai_api_key()

    keys = await asyncio.gather(
        _read_key(LLMCredentials(provider="openai", api_key="sk-a")),
        _read_key(LLMCredentials(provider="openai", api_key="sk-b")),
    )
    assert keys == ["sk-a", "sk-b"]


def test_rate_limit_gate_is_per_session_key() -> None:
    assert llm_policy._gate_key("openai") == "openai"
    with use_llm_credentials(LLMCredentials(provider="openai", api_key="sk-a")):
        gate_a = llm_policy._gate_key("openai")
    with use_llm_credentials(LLMCredentials(provider="openai", api_key="sk-b")):
        gate_b = llm_policy._gate_key("openai")
    assert gate_a != gate_b
    assert "sk-a" not in gate_a


def test_credentials_never_render_the_key() -> None:
    creds = LLMCredentials(provider="openai", api_key="sk-secret-123")
    assert "sk-secret-123" not in repr(creds)
    assert creds.redact("Incorrect API key provided: sk-secret-123") == "Incorrect API key provided: [REDACTED]"
