from __future__ import annotations

from agents.episodic_memory import get_episodic_memory_by_run_id, persist_episodic_memory, query_episodic_memory
from agents.schema import (
    CollectionPlan,
    CollectorRequest,
    EvidenceDossier,
    EvidenceGraphSnapshot,
    Phase2HandoffPayload,
    VerificationReport,
)


def _dossier(run_id: str, gene_symbol: str, disease_id: str | None = None) -> EvidenceDossier:
    request = CollectorRequest(gene_symbol=gene_symbol, disease_id=disease_id, sources=[], run_id=run_id)
    return EvidenceDossier(
        run_id=run_id,
        query=request,
        run_metadata={},
        source_status=[],
        errors=[],
        plan=CollectionPlan(run_id=run_id, selected_sources=[], query_intent="collect", query_variants=[], retry_policy={}, expected_outputs={}),
        verified_evidence=[],
        verification_report=VerificationReport(),
        conflicts=[],
        graph_snapshot=EvidenceGraphSnapshot(),
        review_decision=None,
        summary_markdown="# Summary",
        artifact_path=f"/tmp/{run_id}.json",
        artifacts={},
        handoff_payload=Phase2HandoffPayload(run_id=run_id),
    )


def test_episodic_memory_persists_and_queries_runs(tmp_path) -> None:
    persist_episodic_memory(_dossier("run-1", "EGFR", "EFO_1"), tmp_path)
    persist_episodic_memory(_dossier("run-2", "KRAS", "EFO_2"), tmp_path)

    assert get_episodic_memory_by_run_id("run-1", tmp_path)["gene_symbol"] == "EGFR"
    assert len(query_episodic_memory(gene_symbol="KRAS", root=tmp_path)) == 1
    assert len(query_episodic_memory(disease_id="EFO_1", root=tmp_path)) == 1

    # New runs include a stable creation timestamp for deterministic "latest run" selection.
    all_runs = query_episodic_memory(root=tmp_path)
    assert all(isinstance(entry.get("created_at_ms"), int) for entry in all_runs)
    created = [int(entry.get("created_at_ms") or 0) for entry in all_runs]
    assert created == sorted(created)
