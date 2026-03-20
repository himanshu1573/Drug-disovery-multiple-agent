from __future__ import annotations

import pytest

from agents.graph import get_collection_state, get_collection_state_history, resume_collection_graph, run_collection_graph
from agents.schema import CollectorRequest
from agents.summary_agent import SummaryAgent


@pytest.mark.asyncio
async def test_collection_graph_resumes_from_checkpoint_after_failure(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("A4T_ARTIFACT_DIR", str(tmp_path))
    monkeypatch.setenv("A4T_REQUIRE_REVIEW", "0")
    monkeypatch.setenv("OPENAI_API_KEY", "")

    request = CollectorRequest(gene_symbol="EGFR", sources=[], run_id="run-checkpoint-resume")
    original_run = SummaryAgent.run
    attempts = {"count": 0}

    async def flaky_run(self, *args, **kwargs):
        if attempts["count"] == 0:
            attempts["count"] += 1
            raise RuntimeError("forced explanation failure")
        return await original_run(self, *args, **kwargs)

    monkeypatch.setattr(SummaryAgent, "run", flaky_run)

    with pytest.raises(RuntimeError, match="forced explanation failure"):
        await run_collection_graph(request)

    state_after_failure = await get_collection_state(request.run_id)
    assert state_after_failure.values["plan"].run_id == request.run_id
    assert "evidence_graph" in state_after_failure.values

    result = await resume_collection_graph(request)
    assert result.run_id == request.run_id

    resumed_state = await get_collection_state(request.run_id)
    assert resumed_state.values["final_dossier"].run_id == request.run_id
    assert resumed_state.values["final_dossier"].plan.artifact_path is not None

    history = await get_collection_state_history(request.run_id)
    assert len(history) >= 3
