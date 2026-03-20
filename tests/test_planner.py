from __future__ import annotations

import asyncio
import json

from agents.planner import build_collection_plan, persist_collection_plan
from agents.schema import CollectorRequest, SourceName


def test_build_collection_plan_is_deterministic() -> None:
    request = CollectorRequest(
        gene_symbol="EGFR",
        disease_id="EFO_0000311",
        sources=[SourceName.LITERATURE, SourceName.OPENTARGETS, SourceName.DEPMAP],
        run_id="run-fixed",
    )

    plan_a = asyncio.run(build_collection_plan(request))
    plan_b = asyncio.run(build_collection_plan(request))

    assert plan_a.run_id == plan_b.run_id
    assert plan_a.selected_sources == [
        SourceName.DEPMAP,
        SourceName.OPENTARGETS,
        SourceName.LITERATURE,
    ]
    assert plan_a.selected_sources == plan_b.selected_sources
    assert plan_a.query_intent == plan_b.query_intent
    assert plan_a.query_variants == ["EGFR", "ERBB1", "EGFR:EFO_0000311"]
    assert plan_a.query_variants == plan_b.query_variants
    assert plan_a.memory_context["match_count"] == 0
    assert plan_a.execution_notes[0] == "No episodic memory match found; using default Phase-1 plan."
    assert plan_a.planning_mode == "deterministic_fallback"
    assert plan_a.source_directives["depmap"].startswith("Collect")
    assert plan_a.retry_policy["fallback"] == "emit_partial_result"
    assert plan_a.expected_outputs == plan_b.expected_outputs


def test_persist_collection_plan_writes_artifact(tmp_path) -> None:
    request = CollectorRequest(
        gene_symbol="KRAS",
        sources=[SourceName.PHAROS],
        run_id="run-plan-artifact",
    )

    plan = persist_collection_plan(asyncio.run(build_collection_plan(request)), artifacts_root=tmp_path)

    assert plan.artifact_path is not None

    artifact_path = tmp_path / "plans" / "run-plan-artifact.collection_plan.json"
    assert artifact_path.exists()

    payload = json.loads(artifact_path.read_text(encoding="utf-8"))
    assert payload["run_id"] == "run-plan-artifact"
    assert payload["artifact_path"] == str(artifact_path)
    assert payload["selected_sources"] == ["pharos"]


def test_collection_plan_includes_semantic_query_variants() -> None:
    request = CollectorRequest(
        gene_symbol="KRAS",
        disease_id="EFO_0001071",
        sources=[SourceName.OPENTARGETS],
    )

    plan = asyncio.run(build_collection_plan(request))

    assert plan.query_variants == ["KRAS", "K-RAS", "KRAS:EFO_0001071"]


def test_collection_plan_uses_episodic_memory_context() -> None:
    request = CollectorRequest(
        gene_symbol="EGFR",
        disease_id="EFO_0000311",
        sources=[SourceName.OPENTARGETS, SourceName.LITERATURE],
        run_id="run-memory-aware",
    )

    plan = asyncio.run(
        build_collection_plan(
            request,
            past_runs=[
                {
                    "run_id": "run-old",
                    "gene_symbol": "EGFR",
                    "disease_id": "EFO_0000311",
                    "review_decision": {"decision": "approved"},
                    "evidence_count": 7,
                }
            ],
        )
    )

    assert plan.memory_context["match_count"] == 1
    assert plan.memory_context["latest_run_id"] == "run-old"
    assert plan.memory_context["latest_review_decision"] == "approved"
    assert "Memory-informed planning enabled from 1 prior run(s)." in plan.query_intent
    assert any("Prior approved dossier exists" in note for note in plan.execution_notes)


def test_cached_planner_refreshes_memory_aware_fields(tmp_path, monkeypatch) -> None:
    # Planner cache is disabled by default under pytest; enable it explicitly and point
    # artifacts to a temp dir so cache files are isolated.
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_PLANNER_CACHE_ENABLED", "1")
    monkeypatch.setenv("A4T_PLANNER_CACHE_TTL_S", "99999")

    request = CollectorRequest(
        gene_symbol="EGFR",
        disease_id="EFO_0000311",
        sources=[SourceName.OPENTARGETS, SourceName.LITERATURE],
        run_id="run-cache-seed",
    )

    # First run: no episodic memory context, but cache is populated.
    seeded = asyncio.run(build_collection_plan(request, past_runs=[]))
    assert seeded.memory_context["match_count"] == 0
    assert seeded.planning_mode in {"deterministic_fallback", "llm_planner", "cached_planner"}

    # Second run: same query inputs (cache hit), but now with episodic memory.
    cached_memory_aware = asyncio.run(
        build_collection_plan(
            request.model_copy(update={"run_id": "run-cache-hit"}),
            past_runs=[
                {
                    "run_id": "run-old",
                    "gene_symbol": "EGFR",
                    "disease_id": "EFO_0000311",
                    "review_decision": {"decision": "needs_more_evidence"},
                    "evidence_count": 11,
                }
            ],
        )
    )

    assert cached_memory_aware.planning_mode == "cached_planner"
    assert cached_memory_aware.memory_context["match_count"] == 1
    assert "Memory-informed planning enabled from 1 prior run(s)." in cached_memory_aware.query_intent
    assert any("Found 1 prior episodic match" in note for note in cached_memory_aware.execution_notes)


def test_collection_plan_uses_llm_response_when_available(monkeypatch) -> None:
    class FakePlanningAgent:
        async def plan(self, **_kwargs):
            from agents.planning_agent import PlanningResponse, SourceDirective

            return (
                PlanningResponse(
                    query_intent="LLM-generated planning intent.",
                    query_variants=["EGFR", "ERBB1", "EGFR NSCLC"],
                    source_order=["literature", "depmap"],
                    source_directives=[
                        SourceDirective(source="literature", directive="Prioritize mechanism and disease papers."),
                        SourceDirective(source="depmap", directive="Prioritize dependency strength and context."),
                    ],
                    execution_notes=["LLM reviewed prior runs before planning."],
                ),
                "llm_planner",
                "gpt-5",
            )

    monkeypatch.setattr("agents.planner.PlanningAgent", lambda: FakePlanningAgent())
    request = CollectorRequest(
        gene_symbol="EGFR",
        sources=[SourceName.DEPMAP, SourceName.LITERATURE],
        run_id="run-llm-plan",
    )

    plan = asyncio.run(build_collection_plan(request))

    assert plan.selected_sources == [SourceName.LITERATURE, SourceName.DEPMAP]
    assert plan.query_intent == "LLM-generated planning intent."
    assert plan.planning_mode == "llm_planner"
    assert plan.planner_model_used == "gpt-5"
    assert plan.source_directives["literature"] == "Prioritize mechanism and disease papers."


def test_planner_falls_back_even_when_llm_agents_required(monkeypatch) -> None:
    # Under the UI, we often run with A4T_REQUIRE_LLM_AGENTS=1 to enforce an LLM-compiled
    # final report, but planning should still be resilient and fall back deterministically
    # on transient LLM issues (timeouts, upstream errors).
    monkeypatch.setenv("A4T_LLM_CALLS_ENABLED", "1")
    monkeypatch.setenv("A4T_REQUIRE_LLM_AGENTS", "1")
    monkeypatch.setenv("A4T_REQUIRE_LLM_PLANNER", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    async def boom(**_kwargs):
        raise TimeoutError("synthetic timeout")

    monkeypatch.setattr("agents.planning_agent.structured_ainvoke_with_fallbacks", boom)

    request = CollectorRequest(
        gene_symbol="KRAS",
        sources=[SourceName.PHAROS, SourceName.LITERATURE],
        run_id="run-llm-plan-timeout",
    )

    plan = asyncio.run(build_collection_plan(request))

    assert plan.planning_mode == "deterministic_fallback"
    assert plan.selected_sources == [SourceName.PHAROS, SourceName.LITERATURE]
    assert plan.query_variants[0] == "KRAS"
