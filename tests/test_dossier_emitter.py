from __future__ import annotations

import json

import pytest

from agents.graph import create_collector_graph
from agents.graph import get_collector_checkpointer
from agents.schema import CollectorRequest, EvidenceRecord, Provenance, SourceName


@pytest.mark.asyncio
async def test_emit_dossier_persists_complete_phase1_output(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    # Ensure a clean checkpoint thread for this fixed run_id to avoid cross-test contamination.
    get_collector_checkpointer().delete_thread("run-dossier")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-dossier")
    item = EvidenceRecord(
        source=SourceName.OPENTARGETS,
        target_id="ENSG00000146648",
        target_symbol="EGFR",
        disease_id="EFO_0000311",
        evidence_type="disease_association",
        raw_value=0.91,
        normalized_score=0.91,
        confidence=0.88,
        summary="Strong disease association",
        provenance=Provenance(provider="Open Targets", endpoint="/graphql", query={"gene_symbol": "EGFR"}),
    )

    result_state = await app.ainvoke(
        {"query": request, "evidence_items": [item]},
        config={"configurable": {"thread_id": request.run_id}},
    )

    dossier = result_state["final_dossier"]
    payload = json.loads((tmp_path / "dossiers" / "run-dossier.evidence_dossier.json").read_text(encoding="utf-8"))

    assert dossier.artifact_path == str(tmp_path / "dossiers" / "run-dossier.evidence_dossier.json")
    assert payload["run_metadata"]["collector_node_sequence"][-1] == "emit_dossier"
    assert payload["source_status"] == []
    assert payload["errors"] == []
    assert payload["artifacts"]["plan"].endswith(".collection_plan.json")
    assert payload["artifacts"]["graph"].endswith(".evidence_graph.json")
    assert payload["handoff_payload"]["run_id"] == request.run_id
    assert payload["handoff_payload"]["handoff_version"] == "phase2.v1"
    assert payload["handoff_payload"]["dossier_artifact_path"] == str(tmp_path / "dossiers" / "run-dossier.evidence_dossier.json")
    assert "blocking_issues" in payload["handoff_payload"]
