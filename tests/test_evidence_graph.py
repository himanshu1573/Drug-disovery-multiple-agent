from __future__ import annotations

import json

from agents.evidence_graph import build_evidence_graph_snapshot, persist_evidence_graph_snapshot
from agents.normalizer import normalize_evidence_items
from agents.schema import (
    ConflictRecord,
    ConflictSeverity,
    EvidenceRecord,
    GraphEdgeType,
    Provenance,
    SourceName,
)


def _record(**overrides) -> EvidenceRecord:
    data = {
        "source": SourceName.LITERATURE,
        "target_id": "ENSG00000146648",
        "target_symbol": "EGFR",
        "disease_id": "EFO_0000311",
        "evidence_type": "literature_article",
        "raw_value": 0.9,
        "normalized_score": 0.9,
        "confidence": 0.8,
        "summary": "EGFR evidence",
        "support": {"pmid": "12345"},
        "provenance": Provenance(provider="Europe PMC", endpoint="/search", query={"gene_symbol": "EGFR"}),
    }
    data.update(overrides)
    return EvidenceRecord(**data)


def test_evidence_graph_builder_emits_expected_relations() -> None:
    item = normalize_evidence_items([_record()])[0]
    evidence_node_id = f"evidence:{item.evidence_id}"
    conflict = ConflictRecord(
        severity=ConflictSeverity.MEDIUM,
        rationale="Score divergence detected.",
        sources=[SourceName.LITERATURE, SourceName.OPENTARGETS],
        evidence_ids=[item.evidence_id],
    )

    snapshot = build_evidence_graph_snapshot([item], conflicts=[conflict])

    node_ids = {node.id for node in snapshot.nodes}
    edge_keys = {(edge.source_id, edge.target_id, edge.edge_type) for edge in snapshot.edges}

    assert "target:EGFR" in node_ids
    assert "disease:EFO_0000311" in node_ids
    assert "source:literature" in node_ids
    assert "publication:pmid:12345" in node_ids
    assert ("target:EGFR", "disease:EFO_0000311", GraphEdgeType.TARGET_DISEASE) in edge_keys
    assert ("target:EGFR", evidence_node_id, GraphEdgeType.TARGET_EVIDENCE) in edge_keys
    assert (evidence_node_id, "source:literature", GraphEdgeType.EVIDENCE_SOURCE) in edge_keys
    assert (evidence_node_id, "publication:pmid:12345", GraphEdgeType.EVIDENCE_PUBLICATION) in edge_keys

    evidence_node = next(node for node in snapshot.nodes if node.id == evidence_node_id)
    assert evidence_node.attributes["conflict_severity"] == "medium"


def test_evidence_graph_snapshot_persists_stable_json_artifact(tmp_path) -> None:
    snapshot = build_evidence_graph_snapshot(normalize_evidence_items([_record()]))

    persisted = persist_evidence_graph_snapshot("run-graph", snapshot, tmp_path)

    assert persisted.artifact_path is not None
    payload = json.loads((tmp_path / "graphs" / "run-graph.evidence_graph.json").read_text(encoding="utf-8"))
    assert payload["artifact_path"] == str(tmp_path / "graphs" / "run-graph.evidence_graph.json")
    assert payload["graph_format"] == "json"
