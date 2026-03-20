from __future__ import annotations

from agents.schema import CollectorRequest, EvidenceRecord, Provenance, SourceName
from agents.normalizer import normalize_evidence_items
from agents.verifier import run_verification


def _record(**overrides) -> EvidenceRecord:
    data = {
        "source": SourceName.OPENTARGETS,
        "target_id": "ENSG00000133703",
        "target_symbol": "KRAS",
        "disease_id": "EFO_0001071",
        "evidence_type": "association",
        "raw_value": 0.8,
        "normalized_score": 0.8,
        "confidence": 0.8,
        "summary": "Canonical evidence",
        "provenance": Provenance(provider="Open Targets", endpoint="/graphql", query={"gene_symbol": "KRAS"}),
        "support": {},
    }
    data.update(overrides)
    return EvidenceRecord(**data)


def _outcome(report, name: str):
    for outcome in report.rule_outcomes:
        if outcome.rule_name == name:
            return outcome
    raise AssertionError(f"Missing outcome for {name}")


def test_verifier_accepts_valid_evidence_bundle() -> None:
    request = CollectorRequest(gene_symbol="KRAS", disease_id="EFO_0001071")
    literature = _record(
        source=SourceName.LITERATURE,
        target_id="KRAS:PMID:123",
        evidence_type="literature_article",
        support={"pmid": "123"},
        provenance=Provenance(provider="Europe PMC", endpoint="/search", query={"gene_symbol": "KRAS"}),
    )

    report = run_verification(request, normalize_evidence_items([_record(), literature]))

    assert report.total_rules == len(report.rule_outcomes)
    assert report.fail_count == 0
    assert report.warning_count == 0
    assert report.blocked is False
    assert report.blocking_issue_count == 0
    assert report.blocking_issues == []
    assert report.warning_issues == []
    assert report.affected_evidence_ids == []


def test_verifier_flags_duplicates() -> None:
    request = CollectorRequest(gene_symbol="KRAS")
    item = _record()

    report = run_verification(request, normalize_evidence_items([item, item.model_copy()]))

    duplicate = _outcome(report, "duplicate_detection")
    assert duplicate.passed is False
    assert len(duplicate.evidence_ids) == 2
    assert "duplicate_detection" in report.warning_issues
    assert len(report.affected_evidence_ids) == 1


def test_verifier_flags_gene_mapping_mismatch() -> None:
    request = CollectorRequest(gene_symbol="KRAS")
    report = run_verification(request, normalize_evidence_items([_record(target_symbol="NRAS")]))

    gene_mapping = _outcome(report, "gene_mapping_consistency")
    assert gene_mapping.passed is False
    assert gene_mapping.blocking is True
    assert report.blocked is True
    assert report.blocking_issue_count == 1
    assert "gene_mapping_consistency" in report.blocking_issues


def test_verifier_flags_missing_literature_citation() -> None:
    request = CollectorRequest(gene_symbol="KRAS")
    report = run_verification(
        request,
        normalize_evidence_items([
            _record(
                source=SourceName.LITERATURE,
                target_id="KRAS:PMID:none",
                evidence_type="literature_article",
                support={},
                provenance=Provenance(provider="Europe PMC", endpoint="/search", query={"gene_symbol": "KRAS"}),
            )
        ]),
    )

    citation = _outcome(report, "citation_presence")
    assert citation.passed is False
    assert citation.blocking is False
    assert report.warning_count >= 1
    assert "citation_presence" in report.warning_issues


def test_verifier_flags_bad_ontology_format_and_disease_mismatch() -> None:
    request = CollectorRequest(gene_symbol="KRAS", disease_id="EFO_0001071")
    report = run_verification(request, normalize_evidence_items([_record(disease_id="DOID:1234")]))

    ontology = _outcome(report, "ontology_id_format")
    disease = _outcome(report, "disease_mapping_consistency")
    assert ontology.passed is False
    assert disease.passed is False


def test_verifier_flags_missing_provenance_fields() -> None:
    request = CollectorRequest(gene_symbol="KRAS")
    broken = _record().model_copy(
        update={
            "provenance": Provenance(provider="", endpoint="", query={}),
        }
    )

    report = run_verification(request, normalize_evidence_items([broken]))

    provenance = _outcome(report, "provenance_completeness")
    assert provenance.passed is False
    assert provenance.blocking is True


def test_verifier_accepts_semantic_memory_aliases_for_gene_and_disease() -> None:
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0001071")
    report = run_verification(
        request,
        normalize_evidence_items([
            _record(
                target_symbol="ERBB1",
                disease_id="EFO:0001071",
                target_id="ENSG00000146648",
            )
        ]),
    )

    assert _outcome(report, "gene_mapping_consistency").passed is True
    assert _outcome(report, "disease_mapping_consistency").passed is True
