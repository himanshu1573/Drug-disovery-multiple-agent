from __future__ import annotations

import json

from scripts.nightly_provenance_audit import build_provenance_audit_report, persist_provenance_audit_report


def test_nightly_provenance_audit_reports_completeness_and_drift(tmp_path) -> None:
    dossier_dir = tmp_path / "dossiers"
    dossier_dir.mkdir(parents=True)
    dossier_dir.joinpath("run-1.evidence_dossier.json").write_text(
        json.dumps(
            {
                "source_status": [{"source": "opentargets", "status": "failed"}],
                "verification_report": {"fail_count": 1},
                "verified_evidence": [{"provenance": {"provider": "Open Targets", "endpoint": "/graphql"}}],
            }
        ),
        encoding="utf-8",
    )

    report = build_provenance_audit_report(tmp_path)
    path = persist_provenance_audit_report(tmp_path)

    assert report["dossier_count"] == 1
    assert report["provenance_completeness_ratio"] == 1.0
    assert report["verification_fail_count"] == 1
    assert report["source_status_drift"]["opentargets"] == 1
    assert path.endswith("audits/nightly_provenance_audit.json")
