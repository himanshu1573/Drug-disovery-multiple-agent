from __future__ import annotations

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


def _valid_item(**overrides) -> EvidenceRecord:
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
async def test_review_gate_does_not_auto_decide_when_review_is_disabled(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-review-approved")

    result_state = await app.ainvoke(
        {"query": request, "evidence_items": [_valid_item()]},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result_state["review_decision"] is None
    assert result_state["final_dossier"].handoff_payload.ready is False
    assert result_state["final_dossier"].handoff_payload.reason == "awaiting_human_review"


@pytest.mark.asyncio
async def test_review_gate_preserves_manual_rejection(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-review-rejected")
    manual_rejection = ReviewDecision(
        decision=ReviewDecisionStatus.REJECTED,
        reviewer_id="scientist-1",
        reason="Conflict pattern not acceptable.",
    )

    result_state = await app.ainvoke(
        {"query": request, "evidence_items": [_valid_item()], "review_decision": manual_rejection},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result_state["review_decision"].decision == ReviewDecisionStatus.REJECTED
    assert result_state["final_dossier"].handoff_payload.ready is False
    assert result_state["final_dossier"].handoff_payload.reason == "rejected_by_reviewer"


@pytest.mark.asyncio
async def test_review_gate_loops_once_for_explicit_needs_more_evidence(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-review-loop")
    needs_more = ReviewDecision(
        decision=ReviewDecisionStatus.NEEDS_MORE_EVIDENCE,
        reviewer_id="scientist-1",
        reason="Need more evidence before approval.",
    )

    result_state = await app.ainvoke(
        {"query": request, "evidence_items": [_valid_item(target_symbol="NRAS")], "review_decision": needs_more},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result_state["review_decision"].decision == ReviewDecisionStatus.NEEDS_MORE_EVIDENCE
    assert result_state["review_iteration_count"] == 1
    assert result_state["final_dossier"].run_metadata["review_iteration_count"] == 1
    assert result_state["final_dossier"].handoff_payload.reason == "needs_more_evidence"
