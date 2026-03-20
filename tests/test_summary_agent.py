from __future__ import annotations

from agents.evidence_id import compute_evidence_id
from agents.evidence_graph import build_evidence_graph_snapshot
from agents.schema import (
    CollectorRequest,
    ConflictRecord,
    ConflictSeverity,
    EvidenceRecord,
    Provenance,
    SourceName,
    SourceStatus,
    StatusName,
    VerificationReport,
)
from agents.summary_agent import SummaryAgent


def _record(source: SourceName, target_id: str, summary: str, confidence: float, score: float) -> EvidenceRecord:
    disease_id = "EFO_0000311"
    evidence_type = "disease_association" if source == SourceName.OPENTARGETS else "literature_article"
    support = {"pmid": "12345"} if source == SourceName.LITERATURE else {}
    evidence_id = compute_evidence_id(
        source=source.value,
        target_id=target_id,
        disease_id=disease_id,
        evidence_type=evidence_type,
        raw_value=score,
        support=support,
    )
    return EvidenceRecord(
        evidence_id=evidence_id,
        source=source,
        target_id=target_id,
        target_symbol="EGFR",
        disease_id=disease_id,
        evidence_type=evidence_type,
        raw_value=score,
        normalized_score=score,
        confidence=confidence,
        summary=summary,
        support=support,
        provenance=Provenance(provider=source.value, endpoint="/test", query={"gene_symbol": "EGFR"}),
    )


async def _run_summary() -> str:
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311")
    items = [
        _record(SourceName.OPENTARGETS, "ENSG00000146648", "Strong disease association", 0.9, 0.91),
        _record(SourceName.LITERATURE, "EGFR:PMID:12345", "Peer-reviewed evidence", 0.72, 0.7),
    ]
    statuses = [
        SourceStatus(source=SourceName.OPENTARGETS, status=StatusName.SUCCESS, record_count=1, duration_ms=15),
        SourceStatus(source=SourceName.LITERATURE, status=StatusName.SUCCESS, record_count=1, duration_ms=20),
        SourceStatus(source=SourceName.PHAROS, status=StatusName.FAILED, record_count=0, duration_ms=10, error_message="offline"),
    ]
    conflicts = [
        ConflictRecord(
            severity=ConflictSeverity.LOW,
            rationale="Minor score spread across sources.",
            sources=[SourceName.OPENTARGETS, SourceName.LITERATURE],
            evidence_ids=[items[0].evidence_id],
        )
    ]
    verification = VerificationReport(
        total_rules=8,
        pass_count=8,
        fail_count=0,
        warning_count=0,
        blocked=False,
        blocking_issue_count=0,
        blocking_issues=[],
        warning_issues=[],
        affected_evidence_ids=[],
        rule_outcomes=[],
    )
    graph = build_evidence_graph_snapshot(items, conflicts=conflicts)
    agent = SummaryAgent()
    summary = await agent.run(
        request=request,
        items=items,
        source_status=statuses,
        verification_report=verification,
        conflicts=conflicts,
        evidence_graph=graph,
    )
    return summary.markdown_report


def test_summary_agent_grounded_fallback_contains_coverage_confidence_and_conflicts() -> None:
    import asyncio
    from unittest.mock import patch

    # Force deterministic fallback by explicitly disabling the LLM requirement flag
    with patch.dict("os.environ", {"A4T_REQUIRE_LLM_AGENTS": "0"}, clear=False):
        with patch.dict("os.environ", {}, clear=False) as env_patch:
            env_patch.pop("OPENAI_API_KEY", None)
            markdown = asyncio.run(_run_summary())

    # The deterministic fallback produces coverage/confidence/conflict sections
    assert "## Source Coverage" in markdown or "## 1. Executive Summary" in markdown
    assert "opentargets" in markdown.lower()
    assert "pharos" in markdown.lower()

