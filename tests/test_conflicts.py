from __future__ import annotations

from agents.conflicts import analyze_conflicts
from agents.normalizer import normalize_evidence_items
from agents.schema import ConflictSeverity, EvidenceRecord, Provenance, SourceName


def _record(source: SourceName, score: float, **overrides) -> EvidenceRecord:
    data = {
        "source": source,
        "target_id": "ENSG00000133703",
        "target_symbol": "KRAS",
        "disease_id": "EFO_0001071",
        "evidence_type": "association",
        "raw_value": score,
        "normalized_score": score,
        "confidence": 0.8,
        "summary": f"{source.value} score {score}",
        "provenance": Provenance(provider=source.value, endpoint="/test", query={"gene_symbol": "KRAS"}),
    }
    data.update(overrides)
    return EvidenceRecord(**data)


def test_conflict_analyzer_assigns_high_severity_for_extreme_score_divergence() -> None:
    conflicts = analyze_conflicts(
        normalize_evidence_items([
            _record(SourceName.DEPMAP, 0.1),
            _record(SourceName.OPENTARGETS, 0.9),
        ])
    )

    assert len(conflicts) == 1
    assert conflicts[0].severity == ConflictSeverity.HIGH
    assert len(conflicts[0].evidence_ids) == 2
    assert all(eid for eid in conflicts[0].evidence_ids)


def test_conflict_analyzer_assigns_medium_and_low_severity_thresholds() -> None:
    medium = analyze_conflicts(
        normalize_evidence_items([
            _record(SourceName.DEPMAP, 0.2),
            _record(SourceName.OPENTARGETS, 0.6),
        ])
    )
    low = analyze_conflicts(
        normalize_evidence_items([
            _record(SourceName.DEPMAP, 0.3),
            _record(SourceName.OPENTARGETS, 0.52),
        ])
    )

    assert medium[0].severity == ConflictSeverity.MEDIUM
    assert low[0].severity == ConflictSeverity.LOW


def test_conflict_analyzer_ignores_single_source_and_small_spread_groups() -> None:
    conflicts = analyze_conflicts(
        normalize_evidence_items([
            _record(SourceName.DEPMAP, 0.4),
            _record(SourceName.DEPMAP, 0.4, target_id="ENSG-alt"),
            _record(SourceName.OPENTARGETS, 0.45, target_id="ENSG-alt"),
        ])
    )

    assert conflicts == []
