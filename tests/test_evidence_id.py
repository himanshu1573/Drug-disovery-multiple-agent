from __future__ import annotations

from agents.evidence_id import compute_evidence_id


def test_compute_evidence_id_is_deterministic_and_sensitive_to_support() -> None:
    base = dict(
        source="opentargets",
        target_id="ENSG00000146648",
        disease_id="EFO_0000311",
        evidence_type="disease_association",
        raw_value=0.9,
    )
    a = compute_evidence_id(**base, support={"evidence_count": 10})
    b = compute_evidence_id(**base, support={"evidence_count": 10})
    c = compute_evidence_id(**base, support={"evidence_count": 11})

    assert a == b
    assert a != c

