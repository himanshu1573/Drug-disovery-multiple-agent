from __future__ import annotations

import json
from pathlib import Path

import pytest

from agents.normalizer import normalize_evidence_items
from agents.schema import EvidenceRecord, NORMALIZATION_POLICY_VERSION, Provenance, SourceName


def _record(source: SourceName, **overrides) -> EvidenceRecord:
    base = EvidenceRecord(
        source=source,
        target_id="ENSG00000133703",
        target_symbol=" kras ",
        disease_id="EFO_0001071",
        evidence_type="association",
        raw_value=1.0,
        normalized_score=None,
        confidence=1.0,
        summary="  source summary  ",
        provenance=Provenance(provider=source.value, endpoint="/test", query={"gene_symbol": "KRAS"}),
    )
    return base.model_copy(update=overrides)


def test_normalizer_applies_canonical_policy_across_sources() -> None:
    items = normalize_evidence_items(
        [
            _record(SourceName.DEPMAP),
            _record(SourceName.OPENTARGETS, confidence=-0.3, raw_value=0.4),
            _record(SourceName.PHAROS, normalized_score=0.8),
            _record(SourceName.LITERATURE, disease_id="", raw_value="not-numeric", confidence=0.6),
        ]
    )

    assert [item.source for item in items] == [
        SourceName.DEPMAP,
        SourceName.OPENTARGETS,
        SourceName.PHAROS,
        SourceName.LITERATURE,
    ]
    assert all(item.target_symbol == "KRAS" for item in items)
    assert all(item.normalization_policy_version == NORMALIZATION_POLICY_VERSION for item in items)
    assert items[0].normalized_score == 1.0
    assert items[1].normalized_score == 0.4
    assert items[2].normalized_score == 0.8
    assert items[3].normalized_score is None
    assert items[0].confidence == 1.0
    assert items[1].confidence == 0.0
    assert items[3].disease_id is None
    assert items[0].summary == "source summary"


@pytest.mark.parametrize("fixture_name", ["kras", "egfr", "tp53"])
def test_normalizer_matches_documented_fixtures(fixture_name: str) -> None:
    fixture_dir = Path(__file__).parent / "fixtures" / "normalization"
    input_payload = json.loads((fixture_dir / f"{fixture_name}_input.json").read_text(encoding="utf-8"))
    expected_payload = json.loads((fixture_dir / f"{fixture_name}_expected.json").read_text(encoding="utf-8"))

    items = normalize_evidence_items(
        [
            EvidenceRecord.model_construct(
                **{
                    **item,
                    "provenance": Provenance.model_validate(item["provenance"]),
                }
            )
            for item in input_payload
        ]
    )
    actual_payload = [
        {
            "source": item.source,
            "target_id": item.target_id,
            "target_symbol": item.target_symbol,
            "disease_id": item.disease_id,
            "evidence_type": item.evidence_type,
            "raw_value": item.raw_value,
            "normalized_score": item.normalized_score,
            "confidence": item.confidence,
            "summary": item.summary,
            "normalization_policy_version": item.normalization_policy_version,
        }
        for item in items
    ]

    assert actual_payload == expected_payload
