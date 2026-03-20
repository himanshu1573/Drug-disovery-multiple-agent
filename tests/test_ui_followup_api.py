from __future__ import annotations

import json

import pytest
from fastapi.testclient import TestClient

from agents.schema import (
    CollectionPlan,
    CollectorRequest,
    EvidenceDossier,
    EvidenceRecord,
    EvidenceGraphSnapshot,
    Phase2HandoffPayload,
    Provenance,
    VerificationReport,
)

def _write_latest_snapshot(
    tmp_artifacts: str,
    *,
    run_id: str,
    explanation: str | None = None,
    normalized_items: list[dict] | None = None,  # noqa: ANN401 - JSON-like payload
) -> None:
    workdir = f"{tmp_artifacts}/working_memory/{run_id}"
    import os

    os.makedirs(workdir, exist_ok=True)
    payload = {
        "run_id": run_id,
        "status": "running",
        "last_stage": "generate_explanation" if explanation else "collect_sources_parallel",
        "next": [],
        "values": {
            "query": {
                "gene_symbol": "KRAS",
                "disease_id": "EFO_0003060",
                "objective": "baseline",
                "sources": [],
                "per_source_top_k": 5,
                "max_literature_articles": 5,
                "run_id": run_id,
            },
            "explanation": explanation or "",
            "normalized_items": normalized_items or [],
        },
        "updated_at_ms": 1700000000000,
        "error": None,
    }
    with open(f"{workdir}/latest.json", "w") as f:
        json.dump(payload, f)


def _write_dossier(tmp_artifacts: str, run_id: str) -> None:
    request = CollectorRequest(gene_symbol="KRAS", disease_id="EFO_0003060", sources=[], run_id=run_id, objective="baseline")
    dossier = EvidenceDossier(
        run_id=request.run_id,
        query=request,
        run_metadata={"collector_node_sequence": ["emit_dossier"]},
        source_status=[],
        errors=[],
        plan=CollectionPlan(
            run_id=request.run_id,
            selected_sources=[],
            query_intent="collect",
            query_variants=[],
            retry_policy={},
            expected_outputs={},
        ),
        verified_evidence=[],
        verification_report=VerificationReport(),
        conflicts=[],
        graph_snapshot=EvidenceGraphSnapshot(),
        review_decision=None,
        summary_markdown="# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT\n\n## 1. Executive Summary\n\nStub.\n\n## References\n\n### Evidence IDs\n- [depmap:KRAS:genetic_dependency]\n",
        artifact_path=f"{tmp_artifacts}/dossiers/{run_id}.evidence_dossier.json",
        artifacts={},
        handoff_payload=Phase2HandoffPayload(
            run_id=request.run_id,
            dossier_artifact_path=f"{tmp_artifacts}/dossiers/{run_id}.evidence_dossier.json",
            graph_artifact_path=f"{tmp_artifacts}/graphs/{run_id}.evidence_graph.json",
        ),
    )

    dossier_path = f"{tmp_artifacts}/dossiers/{run_id}.evidence_dossier.json"
    with open(dossier_path, "w") as f:
        json.dump(dossier.model_dump(mode="json"), f)


def test_followup_missing_dossier_returns_404(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    tmp_artifacts = tmp_path / "artifacts"
    tmp_artifacts.mkdir()
    for d in ["dossiers", "graphs", "plans", "metrics", "health_reports", "review_audit", "review_decisions", "episodic_memory", "procedural_memory", "working_memory"]:
        (tmp_artifacts / d).mkdir(exist_ok=True)

    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_artifacts))

    from ui_api.app import app  # import after env set

    client = TestClient(app)
    resp = client.post("/api/runs/run-missing/followup", json={"message": "What does the dossier say?"})
    assert resp.status_code == 404


def test_followup_returns_answer(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    tmp_artifacts = tmp_path / "artifacts"
    tmp_artifacts.mkdir()
    for d in ["dossiers", "graphs", "plans", "metrics", "health_reports", "review_audit", "review_decisions", "episodic_memory", "procedural_memory", "working_memory"]:
        (tmp_artifacts / d).mkdir(exist_ok=True)

    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_artifacts))
    run_id = "run-followup"
    _write_dossier(str(tmp_artifacts), run_id)

    # Patch FollowupAgent to avoid live LLM calls.
    async def _fake_answer(self, *, question, context):  # noqa: ANN001
        return type("X", (), {"answer_markdown": f"Answer for: {question}\n\n## References\n\n### Evidence IDs\n- [depmap:KRAS:genetic_dependency]\n\n### User URLs\n"})()

    monkeypatch.setenv("A4T_URL_FETCH_DNS_CHECK", "0")
    monkeypatch.setattr("agents.followup_agent.FollowupAgent.answer", _fake_answer, raising=True)

    from ui_api.app import app  # import after env set

    client = TestClient(app)
    resp = client.post(f"/api/runs/{run_id}/followup", json={"message": "Summarize KRAS dependency."})
    assert resp.status_code == 200
    data = resp.json()
    assert data["run_id"] == run_id
    assert "## References" in data["answer_markdown"]


def test_followup_before_report_returns_409(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    tmp_artifacts = tmp_path / "artifacts"
    tmp_artifacts.mkdir()
    for d in ["dossiers", "graphs", "plans", "metrics", "health_reports", "review_audit", "review_decisions", "episodic_memory", "procedural_memory", "working_memory"]:
        (tmp_artifacts / d).mkdir(exist_ok=True)
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_artifacts))

    run_id = "run-followup-early"
    _write_latest_snapshot(str(tmp_artifacts), run_id=run_id, explanation="", normalized_items=[])

    from ui_api.app import app  # import after env set

    client = TestClient(app)
    resp = client.post(f"/api/runs/{run_id}/followup", json={"message": "What do we know so far?"})
    assert resp.status_code == 409


def test_followup_uses_snapshot_when_dossier_missing(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    tmp_artifacts = tmp_path / "artifacts"
    tmp_artifacts.mkdir()
    for d in ["dossiers", "graphs", "plans", "metrics", "health_reports", "review_audit", "review_decisions", "episodic_memory", "procedural_memory", "working_memory"]:
        (tmp_artifacts / d).mkdir(exist_ok=True)

    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_artifacts))
    run_id = "run-followup-snapshot"

    record = EvidenceRecord(
        evidence_id="depmap:KRAS:NA:genetic_dependency:abcdef1234",
        source="depmap",
        target_id="KRAS",
        target_symbol="KRAS",
        disease_id=None,
        evidence_type="genetic_dependency",
        raw_value=-0.25,
        normalized_score=0.6,
        confidence=0.8,
        support={"gene_effect": -0.25},
        summary="KRAS dependency example.",
        provenance=Provenance(provider="test", endpoint="snapshot", query={}),
    )
    _write_latest_snapshot(
        str(tmp_artifacts),
        run_id=run_id,
        explanation="# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT\n\n## 1. Executive Summary\n\nStub.\n",
        normalized_items=[record.model_dump(mode="json")],
    )

    async def _fake_answer(self, *, question, context):  # noqa: ANN001
        ev_id = context.evidence_index[0]["evidence_id"] if context.evidence_index else "missing"
        return type("X", (), {"answer_markdown": f"Used evidence: [{ev_id}]\n\n## References\n\n### Evidence IDs\n- [{ev_id}]\n\n### User URLs\n"})()

    monkeypatch.setenv("A4T_URL_FETCH_DNS_CHECK", "0")
    monkeypatch.setattr("agents.followup_agent.FollowupAgent.answer", _fake_answer, raising=True)

    from ui_api.app import app  # import after env set

    client = TestClient(app)
    resp = client.post(f"/api/runs/{run_id}/followup", json={"message": "Summarize KRAS dependency."})
    assert resp.status_code == 200
    data = resp.json()
    assert "depmap:KRAS:NA:genetic_dependency" in data["answer_markdown"]


def test_from_text_out_of_scope_returns_400(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    tmp_artifacts = tmp_path / "artifacts"
    tmp_artifacts.mkdir()
    for d in ["dossiers", "graphs", "plans", "metrics", "health_reports", "review_audit", "review_decisions", "episodic_memory", "procedural_memory", "working_memory"]:
        (tmp_artifacts / d).mkdir(exist_ok=True)

    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_artifacts))
    from ui_api.app import app

    client = TestClient(app)
    resp = client.post("/api/runs/from-text", json={"message": "Tell me a joke"})
    assert resp.status_code == 400
