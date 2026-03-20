from __future__ import annotations

from agents.schema import (
    CollectionPlan,
    CollectorResult,
    EvidenceDossier,
    PHASE2_HANDOFF_VERSION,
    PLAN_VERSION,
    SCHEMA_VERSION,
    VERIFICATION_POLICY_VERSION,
    Phase2HandoffPayload,
    VerificationReport,
)


def test_schema_version_constants_match_expected_baseline() -> None:
    assert SCHEMA_VERSION == "0.1.0"
    assert PLAN_VERSION == "phase1.v1"
    assert VERIFICATION_POLICY_VERSION == "phase1.v1"
    assert PHASE2_HANDOFF_VERSION == "phase2.v1"


def test_collector_result_contract_keeps_stable_top_level_fields() -> None:
    fields = set(CollectorResult.model_fields)

    assert fields >= {
        "schema_version",
        "run_id",
        "query",
        "items",
        "source_status",
        "errors",
        "llm_summary",
    }
    assert CollectorResult.model_fields["schema_version"].default == SCHEMA_VERSION


def test_evidence_dossier_contract_keeps_stable_top_level_fields() -> None:
    fields = set(EvidenceDossier.model_fields)

    assert fields >= {
        "schema_version",
        "run_id",
        "query",
        "run_metadata",
        "source_status",
        "errors",
        "plan",
        "verified_evidence",
        "verification_report",
        "conflicts",
        "graph_snapshot",
        "review_decision",
        "summary_markdown",
        "artifact_path",
        "artifacts",
        "handoff_payload",
    }
    assert EvidenceDossier.model_fields["schema_version"].default == SCHEMA_VERSION


def test_embedded_contract_versions_are_pinned() -> None:
    assert CollectionPlan.model_fields["plan_version"].default == PLAN_VERSION
    assert VerificationReport.model_fields["verification_policy_version"].default == VERIFICATION_POLICY_VERSION
    assert Phase2HandoffPayload.model_fields["handoff_version"].default == PHASE2_HANDOFF_VERSION


def test_verification_report_contract_keeps_structured_summary_fields() -> None:
    fields = set(VerificationReport.model_fields)

    assert fields >= {
        "total_rules",
        "pass_count",
        "fail_count",
        "warning_count",
        "blocked",
        "blocking_issue_count",
        "blocking_issues",
        "warning_issues",
        "affected_evidence_ids",
        "rule_outcomes",
    }
