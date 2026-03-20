from __future__ import annotations

from datetime import datetime, timezone

from agents.evidence_sufficiency import assess_evidence_sufficiency, maybe_apply_auto_recollect
from agents.schema import EvidenceRecord, Provenance, SourceName


def _prov() -> Provenance:
    return Provenance(provider="test", endpoint="unit", query={}, retrieved_at=datetime.now(timezone.utc))


def _src_for_category(category: str) -> SourceName:
    if category == "annotation":
        return SourceName.PHAROS
    if category == "dependency":
        return SourceName.DEPMAP
    if category == "disease_association":
        return SourceName.OPENTARGETS
    return SourceName.LITERATURE


def _rec(category: str) -> EvidenceRecord:
    return EvidenceRecord(
        source=_src_for_category(category),
        target_id="EGFR",
        target_symbol="EGFR",
        disease_id=None,
        evidence_type=category,
        raw_value=None,
        normalized_score=0.5,
        confidence=0.5,
        support={},
        summary=None,
        provenance=_prov(),
    )


def test_assess_evidence_sufficiency_missing_categories() -> None:
    report = assess_evidence_sufficiency(
        [_rec("literature")],
        min_total=1,
        min_per_category=1,
        required_categories=("annotation", "dependency", "disease_association", "literature"),
    )
    assert report.sufficient is False
    assert "annotation" in report.missing_categories
    assert "dependency" in report.missing_categories
    assert "disease_association" in report.missing_categories
    assert report.total_items == 1


def test_assess_evidence_sufficiency_sufficient() -> None:
    items = [_rec("annotation"), _rec("dependency"), _rec("disease_association"), _rec("literature")]
    report = assess_evidence_sufficiency(items, min_total=4, min_per_category=1)
    assert report.sufficient is True
    assert report.missing_categories == []


def test_assess_evidence_sufficiency_defaults_are_coverage_first() -> None:
    items = [_rec("annotation"), _rec("dependency"), _rec("disease_association"), _rec("literature")]
    report = assess_evidence_sufficiency(items)
    assert report.sufficient is True
    assert report.min_total == 4


def test_auto_recollect_decision_triggers_once() -> None:
    report = assess_evidence_sufficiency([_rec("literature")], min_total=25, min_per_category=1)
    decision = maybe_apply_auto_recollect(
        per_source_top_k=5,
        max_literature_articles=5,
        sufficiency=report,
        blocked=False,
        high_conflict=False,
        auto_recollect_count=0,
        max_passes=1,
        top_k_step=5,
        lit_step=5,
    )
    assert decision["should_recollect"] is True
    assert decision["next_per_source_top_k"] == 10
    assert decision["next_max_literature_articles"] == 5
    assert decision["next_auto_recollect_count"] == 1


def test_auto_recollect_does_not_trigger_when_blocked_or_maxed() -> None:
    report = assess_evidence_sufficiency([_rec("literature")], min_total=25, min_per_category=1)
    blocked = maybe_apply_auto_recollect(
        per_source_top_k=5,
        max_literature_articles=5,
        sufficiency=report,
        blocked=True,
        high_conflict=False,
        auto_recollect_count=0,
        max_passes=1,
        top_k_step=5,
        lit_step=5,
    )
    assert blocked["should_recollect"] is False

    maxed = maybe_apply_auto_recollect(
        per_source_top_k=5,
        max_literature_articles=5,
        sufficiency=report,
        blocked=False,
        high_conflict=False,
        auto_recollect_count=1,
        max_passes=1,
        top_k_step=5,
        lit_step=5,
    )
    assert maxed["should_recollect"] is False
