from __future__ import annotations

import pytest

from agents.schema import CollectorRequest, EvidenceRecord, Provenance, SourceName, SourceStatus, StatusName
from agents.normalizer import normalize_evidence_items
from agents.summary_agent import SummaryAgent


@pytest.mark.asyncio
async def test_compiler_report_requires_llm_configuration(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("A4T_REPORT_FORMAT", "compiler")
    monkeypatch.setenv("A4T_LLM_CALLS_ENABLED", "1")
    monkeypatch.setenv("A4T_REQUIRE_LLM_AGENTS", "1")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    req = CollectorRequest(gene_symbol="EGFR")
    items = normalize_evidence_items(
        [
            EvidenceRecord(
                source=SourceName.PHAROS,
                target_id="EGFR",
                target_symbol="EGFR",
                disease_id=None,
                evidence_type="target_annotation",
                raw_value={"tdl": "Tclin"},
                normalized_score=1.0,
                confidence=0.8,
                support={},
                summary="PHAROS annotations for EGFR.",
                provenance=Provenance(provider="PHAROS", endpoint="/graphql", query={"gene_symbol": "EGFR"}),
            )
        ]
    )
    statuses = [SourceStatus(source=SourceName.PHAROS, status=StatusName.SUCCESS, record_count=1, duration_ms=1)]

    agent = SummaryAgent()
    with pytest.raises(RuntimeError) as exc:
        await agent.run(request=req, items=items, source_status=statuses)

    assert "Compiler report requires" in str(exc.value)
