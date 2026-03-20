from __future__ import annotations

import pytest
from pydantic import ValidationError

from agents.schema import PHASE2_HANDOFF_VERSION, Phase2HandoffPayload


def test_phase2_handoff_payload_accepts_versioned_payload() -> None:
    payload = Phase2HandoffPayload(
        run_id="run-handoff",
        ready=False,
        review_required=True,
        blocking_issues=["schema_validity"],
        warning_issues=["citation_presence"],
        conflict_count=1,
        evidence_count=4,
        requested_source_count=4,
        successful_source_count=3,
        dossier_artifact_path="/tmp/dossier.json",
        graph_artifact_path="/tmp/graph.json",
        reason="awaiting_human_review",
    )

    assert payload.handoff_version == PHASE2_HANDOFF_VERSION
    assert payload.phase == "phase2"


def test_phase2_handoff_payload_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        Phase2HandoffPayload(
            run_id="run-handoff",
            unknown=True,
        )
