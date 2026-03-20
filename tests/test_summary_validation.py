from __future__ import annotations

from agents.evidence_id import compute_evidence_id
from agents.schema import EvidenceRecord, Provenance, SourceName
from agents.summary_validation import validate_summary_markdown


def _item() -> EvidenceRecord:
    source = SourceName.OPENTARGETS
    target_id = "ENSG00000146648"
    disease_id = "EFO_0000311"
    evidence_type = "disease_association"
    support = {}
    evidence_id = compute_evidence_id(
        source=source.value,
        target_id=target_id,
        disease_id=disease_id,
        evidence_type=evidence_type,
        raw_value=0.9,
        support=support,
    )
    return EvidenceRecord(
        evidence_id=evidence_id,
        source=source,
        target_id=target_id,
        target_symbol="EGFR",
        disease_id=disease_id,
        evidence_type=evidence_type,
        normalized_score=0.9,
        confidence=0.8,
        summary="Strong disease association",
        provenance=Provenance(provider="Open Targets", endpoint="/graphql", query={"gene_symbol": "EGFR"}),
        support=support,
    )


def test_summary_validation_accepts_grounded_summary() -> None:
    item = _item()
    ref = item.evidence_id
    markdown = "\n".join(
        [
            "## 1. Executive Summary",
            "This is the executive summary paragraph with sufficient detail.",
            "## 2. Target Biology & Mechanism of Action",
            "EGFR is a receptor tyrosine kinase involved in cancer cell proliferation.",
            "## 3. Genetic Dependency & Functional Evidence",
            "CRISPR screens show moderate dependency in EGFR-amplified cell lines.",
            "## 4. Disease Associations & Clinical Relevance",
            "EGFR is associated with multiple cancer types including NSCLC.",
            "## 5. Druggability & Therapeutic Tractability",
            "EGFR is a well-established drug target with approved kinase inhibitors.",
            "## 6. Cross-Source Evidence Synthesis",
            "Evidence from Open Targets and literature are consistent.",
            "## 7. Conflict Analysis & Evidence Gaps",
            "No conflicts detected. Literature coverage is limited.",
            "## 8. Grounded Evidence Citations",
            f"- [{ref}] {item.summary} (confidence=0.8, score=0.9)",
            "## 9. Conclusions & Recommended Next Steps",
            "Recommend expanding to additional disease contexts.",
        ]
    )

    valid, reason = validate_summary_markdown(markdown, [item])
    assert valid is True
    assert reason is None


def test_summary_validation_rejects_unsupported_claims() -> None:
    item = _item()
    markdown = "\n".join(
        [
            "## 1. Executive Summary",
            "This is the executive summary.",
            "## 2. Target Biology & Mechanism of Action",
            "I think EGFR is definitely the best target.",
            "## 3. Genetic Dependency & Functional Evidence",
            "Some dependency data.",
            "## 4. Disease Associations & Clinical Relevance",
            "Disease info.",
            "## 8. Grounded Evidence Citations",
            "- [phantom:BAD:ref] unsupported claim",
            "## 9. Conclusions & Recommended Next Steps",
            "Further work needed.",
        ]
    )

    valid, reason = validate_summary_markdown(markdown, [item])
    assert valid is False
    assert reason is not None
