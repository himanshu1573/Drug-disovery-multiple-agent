from __future__ import annotations

import pytest
from pydantic import ValidationError

from agents.schema import (
    CollectionPlan,
    CollectorRequest,
    ConflictRecord,
    ConflictSeverity,
    EvidenceDossier,
    EvidenceGraphEdge,
    EvidenceGraphNode,
    EvidenceGraphSnapshot,
    EvidenceRecord,
    Phase2HandoffPayload,
    GraphEdgeType,
    Provenance,
    ReviewDecision,
    ReviewDecisionStatus,
    SourceName,
    VerificationReport,
    VerificationRuleOutcome,
)


def _request() -> CollectorRequest:
    return CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311")


def _evidence() -> EvidenceRecord:
    return EvidenceRecord(
        source=SourceName.OPENTARGETS,
        target_id="ENSG00000146648",
        target_symbol="EGFR",
        disease_id="EFO_0000311",
        evidence_type="disease_association",
        normalized_score=0.91,
        confidence=0.85,
        provenance=Provenance(
            provider="Open Targets",
            endpoint="/api/v4/graphql",
            query={"gene": "EGFR", "disease_id": "EFO_0000311"},
        ),
    )


def _plan(run_id: str) -> CollectionPlan:
    return CollectionPlan(
        run_id=run_id,
        selected_sources=[SourceName.OPENTARGETS, SourceName.LITERATURE],
        query_intent="Collect target-disease evidence for EGFR in NSCLC.",
        query_variants=["EGFR", "Epidermal Growth Factor Receptor"],
        retry_policy={"max_attempts": 3, "backoff": "exponential"},
        expected_outputs={
            "opentargets": ["disease_association", "tractability"],
            "literature": ["article_hits"],
        },
    )


def _verification_report() -> VerificationReport:
    return VerificationReport(
        total_rules=3,
        pass_count=2,
        fail_count=0,
        warning_count=1,
        blocked=False,
        blocking_issue_count=0,
        blocking_issues=[],
        warning_issues=["ontology_format"],
        affected_evidence_ids=[],
        rule_outcomes=[
            VerificationRuleOutcome(rule_name="schema_validity", passed=True),
            VerificationRuleOutcome(rule_name="citation_presence", passed=True),
            VerificationRuleOutcome(
                rule_name="ontology_format",
                passed=True,
                blocking=False,
                message="Disease identifier matches expected EFO pattern.",
            ),
        ],
    )


def _graph() -> EvidenceGraphSnapshot:
    return EvidenceGraphSnapshot(
        nodes=[
            EvidenceGraphNode(id="target:EGFR", node_type="target", label="EGFR"),
            EvidenceGraphNode(id="disease:EFO_0000311", node_type="disease", label="Non-small cell lung carcinoma"),
            EvidenceGraphNode(id="evidence:1", node_type="evidence", label="Open Targets association"),
        ],
        edges=[
            EvidenceGraphEdge(
                source_id="target:EGFR",
                target_id="disease:EFO_0000311",
                edge_type=GraphEdgeType.TARGET_DISEASE,
            ),
            EvidenceGraphEdge(
                source_id="target:EGFR",
                target_id="evidence:1",
                edge_type=GraphEdgeType.TARGET_EVIDENCE,
            ),
        ],
        artifact_path="/tmp/run-graph.evidence_graph.json",
    )


def test_phase1_models_accept_valid_payloads() -> None:
    request = _request()
    evidence = _evidence()
    plan = _plan(request.run_id)
    verification_report = _verification_report()
    conflict = ConflictRecord(
        severity=ConflictSeverity.LOW,
        rationale="Minor score variance across sources.",
        sources=[SourceName.OPENTARGETS, SourceName.LITERATURE],
        evidence_ids=["evidence:1", "evidence:2"],
    )
    review = ReviewDecision(
        decision=ReviewDecisionStatus.APPROVED,
        reviewer_id="scientist-1",
        reason="Evidence is coherent and sufficiently sourced.",
    )

    dossier = EvidenceDossier(
        run_id=request.run_id,
        query=request,
        run_metadata={"collector_node_sequence": ["emit_dossier"]},
        source_status=[],
        errors=[],
        plan=plan,
        verified_evidence=[evidence],
        verification_report=verification_report,
        conflicts=[conflict],
        graph_snapshot=_graph(),
        review_decision=review,
        summary_markdown="EGFR is supported by verified evidence.",
        artifact_path="/tmp/run-dossier.evidence_dossier.json",
        artifacts={"plan": "/tmp/run-plan.json", "graph": "/tmp/run-graph.json"},
        handoff_payload=Phase2HandoffPayload(
            run_id=request.run_id,
            ready=False,
            review_required=True,
            blocking_issues=[],
            warning_issues=[],
            conflict_count=1,
            evidence_count=1,
            requested_source_count=2,
            successful_source_count=2,
            dossier_artifact_path="/tmp/run-dossier.evidence_dossier.json",
            graph_artifact_path="/tmp/run-graph.json",
            reason="awaiting_human_review",
        ),
    )

    assert plan.plan_version == "phase1.v1"
    assert verification_report.rule_outcomes[0].rule_name == "schema_validity"
    assert dossier.verified_evidence[0].target_symbol == "EGFR"
    assert dossier.graph_snapshot.edges[0].edge_type == GraphEdgeType.TARGET_DISEASE
    assert dossier.graph_snapshot.artifact_path == "/tmp/run-graph.evidence_graph.json"
    assert dossier.artifact_path == "/tmp/run-dossier.evidence_dossier.json"
    assert dossier.review_decision is not None


def test_collection_plan_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        CollectionPlan(
            run_id="run-test",
            selected_sources=[SourceName.OPENTARGETS],
            query_intent="Collect evidence.",
            unexpected_field=True,
        )


def test_conflict_record_requires_rationale() -> None:
    with pytest.raises(ValidationError):
        ConflictRecord(
            severity=ConflictSeverity.HIGH,
            rationale="",
            sources=[SourceName.OPENTARGETS],
        )


def test_review_decision_requires_reviewer_id() -> None:
    with pytest.raises(ValidationError):
        ReviewDecision(
            decision=ReviewDecisionStatus.REJECTED,
            reviewer_id="",
            reason="Insufficient provenance.",
        )


def test_evidence_dossier_requires_nested_contracts() -> None:
    request = _request()
    with pytest.raises(ValidationError):
        EvidenceDossier(
            run_id=request.run_id,
            query=request,
            plan=_plan(request.run_id),
            verified_evidence=[],
            verification_report=_verification_report(),
            conflicts=[],
            graph_snapshot={"nodes": [], "edges": []},
            review_decision=None,
            summary_markdown="",
            handoff_payload={},
            extra_field="not allowed",
        )
