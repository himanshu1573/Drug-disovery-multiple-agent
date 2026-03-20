from __future__ import annotations

import pytest

from agents.graph import collect_sources_in_parallel
from agents.schema import (
    CollectorRequest,
    ErrorCode,
    ErrorRecord,
    Provenance,
    EvidenceRecord,
    SourceName,
    SourceStatus,
    StatusName,
)


def _success_record(source: SourceName) -> EvidenceRecord:
    return EvidenceRecord(
        source=source,
        target_id="ENSG00000133703",
        target_symbol="KRAS",
        disease_id="EFO_0001071",
        evidence_type="test_evidence",
        confidence=0.8,
        provenance=Provenance(provider=source.value, endpoint="/test", query={"gene_symbol": "KRAS"}),
    )


@pytest.mark.asyncio
async def test_collect_sources_in_parallel_preserves_status_integrity(monkeypatch) -> None:
    request = CollectorRequest(
        gene_symbol="KRAS",
        run_id="run-parallel-integrity",
        sources=[
            SourceName.LITERATURE,
            SourceName.PHAROS,
            SourceName.OPENTARGETS,
            SourceName.DEPMAP,
        ],
    )

    async def fake_collector(source: SourceName, req: CollectorRequest):
        if source == SourceName.DEPMAP:
            item = _success_record(source)
            status = SourceStatus(source=source, status=StatusName.SUCCESS, duration_ms=11, record_count=1)
            return [item], status, [], {"source": source.value, "items": [item.model_dump(mode="json")]}
        if source == SourceName.PHAROS:
            status = SourceStatus(source=source, status=StatusName.SKIPPED, duration_ms=8, record_count=0, error_message="No match")
            return [], status, [], {"source": source.value, "items": []}
        if source == SourceName.OPENTARGETS:
            status = SourceStatus(
                source=source,
                status=StatusName.FAILED,
                duration_ms=15,
                record_count=0,
                error_code=ErrorCode.RATE_LIMIT,
                error_message="rate limited",
            )
            errors = [ErrorRecord(source=source, error_code=ErrorCode.RATE_LIMIT, message="rate limited", retryable=True)]
            return [], status, errors, {"source": source.value, "items": []}
        raise RuntimeError("unexpected collector crash")

    result = await collect_sources_in_parallel(request, collector=fake_collector)

    assert [status.source for status in result["source_status"]] == [
        SourceName.DEPMAP,
        SourceName.PHAROS,
        SourceName.OPENTARGETS,
        SourceName.LITERATURE,
    ]
    assert [status.status for status in result["source_status"]] == [
        StatusName.SUCCESS,
        StatusName.SKIPPED,
        StatusName.FAILED,
        StatusName.FAILED,
    ]
    assert len(result["evidence_items"]) == 1
    assert len(result["raw_source_payloads"]) == 4
    assert any(error.error_code == ErrorCode.RATE_LIMIT for error in result["errors"])
    assert any(error.error_code == ErrorCode.INTERNAL_ERROR for error in result["errors"])
    assert all(status.duration_ms >= 0 for status in result["source_status"])
