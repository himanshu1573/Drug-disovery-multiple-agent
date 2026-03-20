from __future__ import annotations

import pytest

from agents.query_interpretation_agent import QueryInterpretationAgent, QueryInterpretationContext


@pytest.mark.asyncio
async def test_query_interpretation_heuristic_extracts_single_gene() -> None:
    agent = QueryInterpretationAgent()
    out = await agent.interpret(
        message="KRAS dependency in lung cancer",
        context=QueryInterpretationContext(mode="new_run"),
    )
    assert out.in_scope is True
    assert out.gene_symbol == "KRAS"


@pytest.mark.asyncio
async def test_query_interpretation_out_of_scope_without_gene_or_keywords() -> None:
    agent = QueryInterpretationAgent()
    out = await agent.interpret(
        message="What is the weather today?",
        context=QueryInterpretationContext(mode="new_run"),
    )
    assert out.in_scope is False
    assert out.gene_symbol is None


@pytest.mark.asyncio
async def test_query_interpretation_followup_inherits_active_gene() -> None:
    agent = QueryInterpretationAgent()
    out = await agent.interpret(
        message="What about G12C specifically?",
        context=QueryInterpretationContext(mode="followup", active_gene="KRAS", active_disease="EFO_0003060"),
    )
    assert out.in_scope is True
    assert out.gene_symbol == "KRAS"
    assert out.disease_id == "EFO_0003060"


@pytest.mark.asyncio
async def test_query_interpretation_requires_llm_when_ambiguous_and_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    agent = QueryInterpretationAgent()
    monkeypatch.setenv("A4T_REQUIRE_LLM_AGENTS", "1")
    monkeypatch.setenv("A4T_LLM_CALLS_ENABLED", "0")
    with pytest.raises(RuntimeError):
        await agent.interpret(
            message="KRAS and EGFR in lung cancer",
            context=QueryInterpretationContext(mode="new_run"),
        )
