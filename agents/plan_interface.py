from __future__ import annotations

import json
import os
from pathlib import Path

from .plan_audit import persist_plan_audit
from .schema import PlanDecision, PlanDecisionInput, PlanDecisionResponse


def _artifact_root(root: str | Path | None = None) -> Path:
    return Path(
        root
        or os.getenv("A4T_ARTIFACT_DIR")
        or Path(__file__).resolve().parent.parent / "artifacts"
    )


def persist_plan_decision(run_id: str, plan_decision: PlanDecision, root: str | Path | None = None) -> str:
    decision_dir = _artifact_root(root) / "plan_decisions"
    decision_dir.mkdir(parents=True, exist_ok=True)
    path = decision_dir / f"{run_id}.plan_decision.json"
    payload = {"run_id": run_id, **plan_decision.model_dump(mode="json")}
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return str(path)


def load_plan_decision(run_id: str, root: str | Path | None = None) -> PlanDecision | None:
    path = _artifact_root(root) / "plan_decisions" / f"{run_id}.plan_decision.json"
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload.pop("run_id", None)
    return PlanDecision.model_validate(payload)


def apply_plan_decision(payload: PlanDecisionInput, root: str | Path | None = None) -> PlanDecisionResponse:
    plan_decision = PlanDecision(
        decision=payload.decision,
        reviewer_id=payload.reviewer_id,
        reason=payload.reason,
        updated_plan=payload.updated_plan,
    )
    persist_plan_audit(payload.run_id, plan_decision, root)
    persist_plan_decision(payload.run_id, plan_decision, root)
    return PlanDecisionResponse(
        run_id=payload.run_id,
        accepted=True,
        decision=payload.decision,
        status="recorded",
    )

