from __future__ import annotations

import json
from pathlib import Path

from agents.schema import (
    CollectionPlan,
    CollectorRequest,
    EvidenceDossier,
    EvidenceGraphSnapshot,
    Phase2HandoffPayload,
    VerificationReport,
)


def test_dossier_and_handoff_contract_regression_snapshot() -> None:
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", sources=[], run_id="run-contract")
    dossier = EvidenceDossier(
        run_id=request.run_id,
        query=request,
        run_metadata={"collector_node_sequence": ["emit_dossier"]},
        source_status=[],
        errors=[],
        plan=CollectionPlan(run_id=request.run_id, selected_sources=[], query_intent="collect", query_variants=[], retry_policy={}, expected_outputs={}),
        verified_evidence=[],
        verification_report=VerificationReport(),
        conflicts=[],
        graph_snapshot=EvidenceGraphSnapshot(),
        review_decision=None,
        summary_markdown="## Source Coverage\n## Confidence Profile\n## Conflict Notes\n## Grounded Findings",
        artifact_path="/tmp/dossier.json",
        artifacts={"graph": "/tmp/graph.json", "plan": "/tmp/plan.json"},
        handoff_payload=Phase2HandoffPayload(
            run_id=request.run_id,
            dossier_artifact_path="/tmp/dossier.json",
            graph_artifact_path="/tmp/graph.json",
        ),
    )

    actual = dossier.model_dump(mode="json")
    expected_path = Path(__file__).parent / "fixtures" / "contracts" / "evidence_dossier_snapshot.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert set(actual.keys()) == set(expected.keys())
    assert set(actual["handoff_payload"].keys()) == set(expected["handoff_payload"].keys())
