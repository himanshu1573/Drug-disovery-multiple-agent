from __future__ import annotations

import pytest

from agents.graph import collect_sources_in_parallel
from agents.mcp_runtime import _parse_payload_models
from agents.schema import CollectorRequest, ErrorCode, SourceName, SourceStatus, StatusName


def test_mcp_payload_parser_tolerates_malformed_items() -> None:
    items, status, errors = _parse_payload_models(
        SourceName.OPENTARGETS,
        {
            "items": [{"bad": "payload"}],
            "source_status": [{"source": "opentargets", "status": "success", "duration_ms": 1, "record_count": 0}],
            "errors": [],
        },
    )

    assert items == []
    assert status.status == StatusName.SUCCESS
    assert errors == []


@pytest.mark.asyncio
async def test_parallel_collection_degrades_safely_under_partial_source_outage() -> None:
    request = CollectorRequest(
        gene_symbol="EGFR",
        sources=[SourceName.OPENTARGETS, SourceName.PHAROS],
        run_id="run-resilience-partial",
    )

    async def fake_collector(source, _request):
        if source == SourceName.OPENTARGETS:
            status = SourceStatus(source=source, status=StatusName.SUCCESS, duration_ms=3, record_count=0)
            return [], status, [], {"source": source.value, "items": []}
        raise RuntimeError("pharos offline")

    result = await collect_sources_in_parallel(request, collector=fake_collector)

    assert len(result["source_status"]) == 2
    assert any(status.status == StatusName.SUCCESS for status in result["source_status"])
    assert any(status.status == StatusName.FAILED for status in result["source_status"])
    assert any(error.error_code == ErrorCode.INTERNAL_ERROR for error in result["errors"])
