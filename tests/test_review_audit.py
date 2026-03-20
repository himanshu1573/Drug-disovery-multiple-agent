from __future__ import annotations

import json

from agents.review_audit import persist_review_audit
from agents.schema import ReviewDecision, ReviewDecisionStatus


def test_review_audit_persists_queryable_record(tmp_path) -> None:
    review = ReviewDecision(
        decision=ReviewDecisionStatus.APPROVED,
        reviewer_id="scientist-1",
        reason="Evidence is sufficient.",
    )

    path = persist_review_audit("run-review-audit", review, tmp_path)
    payload = json.loads(open(path, encoding="utf-8").read())

    assert payload["run_id"] == "run-review-audit"
    assert payload["reviewer_id"] == "scientist-1"
    assert payload["decision"] == "approved"
