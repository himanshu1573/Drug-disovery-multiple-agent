from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from .schema import PlanDecision


def _artifact_root(root: str | Path | None = None) -> Path:
    return Path(
        root
        or os.getenv("A4T_ARTIFACT_DIR")
        or Path(__file__).resolve().parent.parent / "artifacts"
    )


def persist_plan_audit(run_id: str, plan_decision: PlanDecision, root: str | Path | None = None) -> str:
    audit_dir = _artifact_root(root) / "plan_audit" / run_id
    audit_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = audit_dir / f"{timestamp}_{plan_decision.reviewer_id}.plan.json"
    payload = {"run_id": run_id, **plan_decision.model_dump(mode="json")}
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return str(path)

