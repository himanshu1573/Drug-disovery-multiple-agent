from __future__ import annotations

import json

import pytest

from agents.graph import COLLECTOR_NODE_SEQUENCE, CollectionPaused, run_collection_graph
from agents.request_builders import build_collector_request
from agents.episodic_memory import persist_episodic_memory
from agents.schema import (
    CollectionPlan,
    EvidenceDossier,
    EvidenceGraphSnapshot,
    Phase2HandoffPayload,
    SupervisorAction,
    SupervisorDecision,
    VerificationReport,
)


@pytest.mark.asyncio
async def test_graph_persists_working_memory_and_stage_logs(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    events: list[dict] = []
    monkeypatch.setattr("agents.graph.log_event", lambda event, **fields: events.append({"event": event, **fields}))
    
    async def emit_directly(self, **_kwargs):
        return SupervisorDecision(
            action=SupervisorAction.EMIT_DOSSIER,
            rationale="Test override to keep a single pass.",
        )

    monkeypatch.setattr("agents.supervisor_agent.SupervisorAgent.decide", emit_directly)
    request = build_collector_request(gene_symbol="KRAS", sources=[], run_id="run-observability")

    await run_collection_graph(request)

    working_dir = tmp_path / "working_memory" / request.run_id
    assert working_dir.exists()
    for stage in COLLECTOR_NODE_SEQUENCE:
        assert (working_dir / f"{stage}.json").exists()

    start_events = [event for event in events if event.get("event") == "stage_start"]
    end_events = [event for event in events if event.get("event") == "stage_end"]

    assert [event["stage"] for event in start_events] == COLLECTOR_NODE_SEQUENCE
    assert [event["stage"] for event in end_events] == COLLECTOR_NODE_SEQUENCE
    assert all(event["run_id"] == request.run_id for event in end_events)


@pytest.mark.asyncio
async def test_graph_persists_procedural_memory_on_plan_stage(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    
    async def emit_directly(self, **_kwargs):
        return SupervisorDecision(
            action=SupervisorAction.EMIT_DOSSIER,
            rationale="Test override to keep a single pass.",
        )

    monkeypatch.setattr("agents.supervisor_agent.SupervisorAgent.decide", emit_directly)
    request = build_collector_request(gene_symbol="EGFR", sources=[], run_id="run-procedural")

    await run_collection_graph(request)

    procedural_path = tmp_path / "procedural_memory" / f"{request.run_id}.procedural_memory.json"
    payload = json.loads(procedural_path.read_text(encoding="utf-8"))

    assert payload["run_id"] == request.run_id
    assert payload["collector_node_sequence"] == COLLECTOR_NODE_SEQUENCE


@pytest.mark.asyncio
async def test_graph_emits_progress_events_for_stages_edges_and_sources(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    request = build_collector_request(gene_symbol="KRAS", sources=[], run_id="run-progress-events")
    events: list[tuple[str, dict]] = []

    await run_collection_graph(request, progress_cb=lambda event, payload: events.append((event, payload)))

    event_names = [event for event, _payload in events]
    assert "stage_start" in event_names
    assert "stage_end" in event_names
    assert "edge" in event_names

    edge_payloads = [payload for event, payload in events if event == "edge"]
    assert any(
        payload["from_stage"] == "validate_input" and payload["to_stage"] == "plan_collection"
        for payload in edge_payloads
    )


@pytest.mark.asyncio
async def test_plan_stage_uses_episodic_memory_context(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    seed_request = build_collector_request(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-seed")
    persist_episodic_memory(
        EvidenceDossier(
            run_id=seed_request.run_id,
            query=seed_request,
            run_metadata={},
            source_status=[],
            errors=[],
            plan=CollectionPlan(run_id=seed_request.run_id, selected_sources=[], query_intent="collect", query_variants=[], retry_policy={}, expected_outputs={}),
            verified_evidence=[],
            verification_report=VerificationReport(),
            conflicts=[],
            graph_snapshot=EvidenceGraphSnapshot(),
            review_decision=None,
            summary_markdown="# Summary",
            artifact_path=str(tmp_path / "dossiers" / "run-seed.evidence_dossier.json"),
            artifacts={},
            handoff_payload=Phase2HandoffPayload(run_id=seed_request.run_id),
        ),
        tmp_path,
    )

    request = build_collector_request(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-memory-aware")
    events: list[tuple[str, dict]] = []

    await run_collection_graph(request, progress_cb=lambda event, payload: events.append((event, payload)))

    plan_events = [payload for event, payload in events if event == "stage_end" and payload["stage"] == "plan_collection"]
    assert plan_events
    plan = plan_events[-1]["update"]["plan"]
    assert plan["memory_context"]["match_count"] == 1
    assert plan["memory_context"]["latest_run_id"] == "run-seed"


@pytest.mark.asyncio
async def test_run_collection_graph_raises_pause_when_review_required(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.delenv("A4T_REQUIRE_REVIEW", raising=False)
    monkeypatch.setenv("OPENAI_API_KEY", "")
    request = build_collector_request(gene_symbol="EGFR", sources=[], run_id="run-paused")

    with pytest.raises(CollectionPaused) as exc_info:
        await run_collection_graph(request)

    assert exc_info.value.run_id == "run-paused"
    assert "human_review_gate" in exc_info.value.next_stages
    assert "plan" in exc_info.value.state_values
    assert "final_dossier" not in exc_info.value.state_values
