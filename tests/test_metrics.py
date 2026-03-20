from __future__ import annotations

import json

from agents.metrics import build_run_metrics, persist_run_metrics
from agents.schema import ConflictRecord, ConflictSeverity, SourceName, SourceStatus, StatusName, VerificationReport


def test_run_metrics_capture_source_latency_and_conflict_rates(tmp_path) -> None:
    metrics = build_run_metrics(
        run_id="run-metrics",
        source_status=[
            SourceStatus(source=SourceName.OPENTARGETS, status=StatusName.SUCCESS, duration_ms=21, record_count=2),
            SourceStatus(source=SourceName.PHAROS, status=StatusName.FAILED, duration_ms=15, record_count=0),
        ],
        verification_report=VerificationReport(
            total_rules=7,
            pass_count=6,
            fail_count=1,
            warning_count=0,
            blocked=True,
            blocking_issue_count=1,
            blocking_issues=["gene_mapping_consistency"],
            warning_issues=[],
            affected_evidence_ids=["e1"],
            rule_outcomes=[],
        ),
        conflicts=[
            ConflictRecord(
                severity=ConflictSeverity.HIGH,
                rationale="Contradiction detected.",
                sources=[SourceName.OPENTARGETS, SourceName.PHAROS],
                evidence_ids=["e1"],
            )
        ],
    )

    path = persist_run_metrics(metrics, tmp_path)
    payload = json.loads(open(path, encoding="utf-8").read())

    assert payload["success_ratio"] == 0.5
    assert payload["source_latency_ms"]["opentargets"] == 21
    assert payload["verification_fail_count"] == 1
    assert payload["conflict_count"] == 1
