from __future__ import annotations

from agents.artifact_store import apply_retention_policy, artifact_layout


def test_artifact_layout_is_deterministic(tmp_path) -> None:
    layout = artifact_layout("run-123", tmp_path)

    assert layout["plan"].endswith("plans/run-123.collection_plan.json")
    assert layout["graph"].endswith("graphs/run-123.evidence_graph.json")
    assert layout["working_memory"].endswith("working_memory/run-123")


def test_retention_policy_removes_non_retained_artifacts(tmp_path) -> None:
    graph_dir = tmp_path / "graphs"
    graph_dir.mkdir(parents=True)
    kept = graph_dir / "run-keep.evidence_graph.json"
    removed = graph_dir / "run-drop.evidence_graph.json"
    kept.write_text("{}", encoding="utf-8")
    removed.write_text("{}", encoding="utf-8")

    deleted = apply_retention_policy(root=tmp_path, retain_run_ids={"run-keep"})

    assert str(removed) in deleted
    assert kept.exists()
    assert not removed.exists()
