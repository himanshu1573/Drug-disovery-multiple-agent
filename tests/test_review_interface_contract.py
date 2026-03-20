from __future__ import annotations

import pytest
from pydantic import ValidationError

from agents.schema import ReviewDecisionInput, ReviewDecisionResponse, ReviewDecisionStatus


def test_review_interface_models_accept_valid_payloads() -> None:
    payload = ReviewDecisionInput(
        run_id="run-1",
        decision=ReviewDecisionStatus.APPROVED,
        reviewer_id="scientist-1",
        reason="Looks good.",
    )
    response = ReviewDecisionResponse(
        run_id="run-1",
        accepted=True,
        decision=ReviewDecisionStatus.APPROVED,
        status="recorded",
    )

    assert payload.run_id == response.run_id
    assert response.accepted is True


def test_review_interface_requires_reviewer_fields() -> None:
    with pytest.raises(ValidationError):
        ReviewDecisionInput(
            run_id="run-1",
            decision=ReviewDecisionStatus.REJECTED,
            reviewer_id="",
            reason="",
        )
