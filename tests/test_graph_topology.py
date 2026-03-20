from __future__ import annotations

import json

import pytest

from agents.graph import COLLECTOR_NODE_SEQUENCE, build_collector_graph, create_collector_graph
from agents.schema import (
    CollectorRequest,
    EvidenceRecord,
    GraphEdgeType,
    Provenance,
    ReviewDecision,
    ReviewDecisionStatus,
    SourceName,
)


def test_collector_graph_declares_full_phase1_node_sequence() -> None:
    graph_builder = build_collector_graph()

    assert list(graph_builder.nodes) == COLLECTOR_NODE_SEQUENCE


@pytest.mark.asyncio
async def test_collector_graph_executes_phase1_flow_without_sources(monkeypatch) -> None:
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", sources=[])

    result_state = await app.ainvoke(
        {"query": request},
        config={"configurable": {"thread_id": request.run_id}},
    )

    assert result_state["plan"].run_id == request.run_id
    assert result_state["verification_report"].pass_count >= 1
    assert result_state["final_result"].run_id == request.run_id
    assert result_state["final_dossier"].run_id == request.run_id


@pytest.mark.asyncio
async def test_collector_graph_builds_evidence_graph_artifact(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    app = create_collector_graph()
    request = CollectorRequest(gene_symbol="EGFR", sources=[], run_id="run-graph-topology")
    item = EvidenceRecord(
        source=SourceName.LITERATURE,
        target_id="ENSG00000146648",
        target_symbol="EGFR",
        disease_id="EFO_0000311",
        evidence_type="literature_article",
        raw_value=0.9,
        normalized_score=0.9,
        confidence=0.8,
        support={"pmid": "12345"},
        provenance=Provenance(provider="Europe PMC", endpoint="/search", query={"gene_symbol": "EGFR"}),
    )

    review = ReviewDecision(
        decision=ReviewDecisionStatus.APPROVED,
        reviewer_id="scientist-1",
        reason="Approved for graph snapshot test.",
    )

    result_state = await app.ainvoke(
        {"query": request, "evidence_items": [item], "review_decision": review},
        config={"configurable": {"thread_id": request.run_id}},
    )

    graph_snapshot = result_state["evidence_graph"]
    artifact_path = tmp_path / "graphs" / f"{request.run_id}.evidence_graph.json"
    payload = json.loads(artifact_path.read_text(encoding="utf-8"))

    assert graph_snapshot.artifact_path == str(artifact_path)
    assert any(edge.edge_type == GraphEdgeType.EVIDENCE_PUBLICATION for edge in graph_snapshot.edges)
    assert payload["artifact_path"] == str(artifact_path)
