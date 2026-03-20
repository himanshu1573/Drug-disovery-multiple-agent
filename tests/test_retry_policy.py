from __future__ import annotations

import pytest

from agents import mcp_runtime
from agents.schema import CollectorRequest, ErrorCode, ErrorRecord, SourceName, SourceStatus, StatusName


def _failed_attempt(code: ErrorCode, message: str):
    status = SourceStatus(
        source=SourceName.OPENTARGETS,
        status=StatusName.FAILED,
        duration_ms=10,
        record_count=0,
        error_code=code,
        error_message=message,
    )
    errors = [
        ErrorRecord(
            source=SourceName.OPENTARGETS,
            error_code=code,
            message=message,
            retryable=code in {ErrorCode.TIMEOUT, ErrorCode.RATE_LIMIT, ErrorCode.UPSTREAM_ERROR},
        )
    ]
    payload = {
        "items": [],
        "source_status": [status.model_dump(mode="json")],
        "errors": [error.model_dump(mode="json") for error in errors],
    }
    return [], status, errors, payload


@pytest.mark.asyncio
async def test_retry_policy_retries_transient_failure_then_succeeds(monkeypatch) -> None:
    request = CollectorRequest(gene_symbol="EGFR", sources=[SourceName.OPENTARGETS], run_id="run-retry-success")
    sleep_calls: list[float] = []
    attempts = {"count": 0}

    async def fake_sleep(delay: float) -> None:
        sleep_calls.append(delay)

    async def fake_once(source, req):
        attempts["count"] += 1
        if attempts["count"] == 1:
            return _failed_attempt(ErrorCode.TIMEOUT, "temporary timeout")
        status = SourceStatus(
            source=source,
            status=StatusName.SUCCESS,
            duration_ms=12,
            record_count=0,
        )
        return [], status, [], {"items": [], "source_status": [status.model_dump(mode="json")], "errors": []}

    monkeypatch.setattr(mcp_runtime, "_execute_mcp_call_once", fake_once)
    monkeypatch.setattr(mcp_runtime.asyncio, "sleep", fake_sleep)

    _, status, _, raw_payload = await mcp_runtime.collect_source_via_mcp_with_raw(SourceName.OPENTARGETS, request)

    assert attempts["count"] == 2
    assert sleep_calls == [0.1]
    assert status.status == StatusName.SUCCESS
    assert raw_payload["retry_attempts"] == 2
    assert len(raw_payload["retry_telemetry"]) == 1
    assert raw_payload["retry_telemetry"][0]["error_code"] == "timeout"


@pytest.mark.asyncio
async def test_retry_policy_stops_after_max_attempts(monkeypatch) -> None:
    request = CollectorRequest(gene_symbol="EGFR", sources=[SourceName.OPENTARGETS], run_id="run-retry-fail")
    sleep_calls: list[float] = []
    attempts = {"count": 0}

    async def fake_sleep(delay: float) -> None:
        sleep_calls.append(delay)

    async def fake_once(source, req):
        attempts["count"] += 1
        return _failed_attempt(ErrorCode.RATE_LIMIT, "rate limited")

    monkeypatch.setattr(mcp_runtime, "_execute_mcp_call_once", fake_once)
    monkeypatch.setattr(mcp_runtime.asyncio, "sleep", fake_sleep)

    _, status, errors, raw_payload = await mcp_runtime.collect_source_via_mcp_with_raw(SourceName.OPENTARGETS, request)

    assert attempts["count"] == mcp_runtime.MAX_RETRY_ATTEMPTS
    assert sleep_calls == [0.1, 0.2]
    assert status.status == StatusName.FAILED
    assert status.error_code == ErrorCode.RATE_LIMIT
    assert errors[0].retryable is True
    assert raw_payload["retry_attempts"] == mcp_runtime.MAX_RETRY_ATTEMPTS
    assert len(raw_payload["retry_telemetry"]) == mcp_runtime.MAX_RETRY_ATTEMPTS - 1
