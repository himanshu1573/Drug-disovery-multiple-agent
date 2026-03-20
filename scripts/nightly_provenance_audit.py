from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def _artifact_root(root: str | Path | None = None) -> Path:
    return Path(
        root
        or os.getenv("A4T_ARTIFACT_DIR")
        or Path(__file__).resolve().parent.parent / "artifacts"
    )


def build_provenance_audit_report(root: str | Path | None = None) -> dict[str, Any]:
    base = _artifact_root(root)
    dossier_dir = base / "dossiers"
    dossiers = sorted(dossier_dir.glob("*.evidence_dossier.json")) if dossier_dir.exists() else []
    total_records = 0
    complete_records = 0
    verification_fail_count = 0
    source_status_drift: dict[str, int] = {}

    for path in dossiers:
        payload = json.loads(path.read_text(encoding="utf-8"))
        verification_fail_count += int(payload.get("verification_report", {}).get("fail_count", 0))
        for status in payload.get("source_status", []):
            source = status.get("source", "unknown")
            state = status.get("status", "unknown")
            if state != "success":
                source_status_drift[source] = source_status_drift.get(source, 0) + 1
        for item in payload.get("verified_evidence", []):
            total_records += 1
            provenance = item.get("provenance", {})
            if provenance.get("provider") and provenance.get("endpoint"):
                complete_records += 1

    completeness_ratio = (complete_records / total_records) if total_records else 1.0
    return {
        "dossier_count": len(dossiers),
        "total_evidence_records": total_records,
        "provenance_complete_records": complete_records,
        "provenance_completeness_ratio": completeness_ratio,
        "verification_fail_count": verification_fail_count,
        "source_status_drift": source_status_drift,
        "pass": completeness_ratio >= 0.95 and verification_fail_count == 0,
    }


def persist_provenance_audit_report(root: str | Path | None = None) -> str:
    base = _artifact_root(root)
    audit_dir = base / "audits"
    audit_dir.mkdir(parents=True, exist_ok=True)
    path = audit_dir / "nightly_provenance_audit.json"
    path.write_text(json.dumps(build_provenance_audit_report(root), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return str(path)


if __name__ == "__main__":
    print(persist_provenance_audit_report())
