from __future__ import annotations

from typing import get_type_hints

from agents.state import CollectorState


def test_collector_state_exposes_phase1_pipeline_fields() -> None:
    hints = get_type_hints(CollectorState, include_extras=True)

    assert "query" in hints
    assert "plan" in hints
    assert "evidence_items" in hints
    assert "normalized_items" in hints
    assert "verification_report" in hints
    assert "conflicts" in hints
    assert "evidence_graph" in hints
    assert "explanation" in hints
    assert "review_decision" in hints
    assert "final_result" in hints
    assert "final_dossier" in hints
