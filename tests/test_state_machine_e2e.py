from __future__ import annotations

import json

import pytest

from agents.graph import create_collector_graph
from agents.schema import (
    CollectorRequest,
    EvidenceRecord,
    Provenance,
    ReviewDecision,
    ReviewDecisionStatus,
    SourceName,
)


def _item(**overrides) -> EvidenceRecord:
    data = {
        "source": SourceName.OPENTARGETS,
        "target_id": "ENSG00000146648",
        "target_symbol": "EGFR",
        "disease_id": "EFO_0000311",
        "evidence_type": "disease_association",
        "raw_value": 0.91,
        "normalized_score": 0.91,
        "confidence": 0.88,
        "summary": "Strong disease association",
        "provenance": Provenance(provider="Open Targets", endpoint="/graphql", query={"gene_symbol": "EGFR"}),
    }
    data.update(overrides)
    return EvidenceRecord(**data)


@pytest.mark.asyncio
async def test_state_machine_e2e_approved_path(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-e2e-approved")
    review = ReviewDecision(decision=ReviewDecisionStatus.APPROVED, reviewer_id="r1", reason="Approved by reviewer.")

    result = await app.ainvoke(
        {"query": request, "evidence_items": [_item()], "review_decision": review},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result["final_dossier"].handoff_payload.ready is True
    assert (tmp_path / "dossiers" / "run-e2e-approved.evidence_dossier.json").exists()


@pytest.mark.asyncio
async def test_state_machine_e2e_rejected_terminal_path(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-e2e-rejected")
    review = ReviewDecision(decision=ReviewDecisionStatus.REJECTED, reviewer_id="r1", reason="Rejected by reviewer.")

    result = await app.ainvoke(
        {"query": request, "evidence_items": [_item()], "review_decision": review},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result["final_dossier"].handoff_payload.ready is False
    assert result["final_dossier"].handoff_payload.reason == "rejected_by_reviewer"


@pytest.mark.asyncio
async def test_state_machine_e2e_needs_more_evidence_loop(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-e2e-loop")
    review = ReviewDecision(
        decision=ReviewDecisionStatus.NEEDS_MORE_EVIDENCE,
        reviewer_id="r1",
        reason="Need more evidence.",
    )

    result = await app.ainvoke(
        {"query": request, "evidence_items": [_item(target_symbol="NRAS")], "review_decision": review},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result["review_decision"].decision == ReviewDecisionStatus.NEEDS_MORE_EVIDENCE
    assert result["review_iteration_count"] == 1
    payload = json.loads((tmp_path / "dossiers" / "run-e2e-loop.evidence_dossier.json").read_text(encoding="utf-8"))
    assert payload["handoff_payload"]["reason"] == "needs_more_evidence"
