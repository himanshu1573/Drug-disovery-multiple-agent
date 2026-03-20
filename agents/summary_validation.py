from __future__ import annotations

import re
import os

from .schema import EvidenceRecord


FORBIDDEN_PATTERNS = [
    re.compile(r"\bI think\b", re.IGNORECASE),
    re.compile(r"\bwe believe\b", re.IGNORECASE),
    re.compile(r"\bprobably\b", re.IGNORECASE),
]


def validate_summary_markdown(markdown: str, items: list[EvidenceRecord]) -> tuple[bool, str | None]:
    # Auto-detect format from headings to avoid coupling validation to env defaults.
    if "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT" in markdown:
        required_sections = [
            "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT",
            "## 1. Executive Summary",
            "## 2. Target Annotation Evidence",
            "## 3. Genetic Dependency Evidence",
            "## 4. Disease Association Evidence",
            "## 5. Literature Evidence",
            "## 6. Integrated Evidence Interpretation",
            "## 7. Evidence Strength Assessment",
            "## 8. Overall Target Assessment",
            "## 9. Final Evidence-Based Conclusion",
        ]
        format_mode = "compiler"
    elif "## 1. Executive Summary" in markdown:
        required_sections = [
            "## 1. Executive Summary",
            "## 2. Target Biology",
            "## 3. Genetic Dependency",
            "## 4. Disease Associations",
            "## 8. Grounded Evidence Citations",
            "## 9. Conclusions",
        ]
        format_mode = "dossier"
    elif "## Executive Answer" in markdown:
        required_sections = [
            "## Executive Answer",
            "## Evidence Summary",
            "## Source Coverage",
            "## Conflicts & Caveats",
            "## Machine Appendix",
        ]
        format_mode = "concise"
    elif "## Executive" in markdown:
        required_sections = [
            "## Executive",
            "## Source Coverage",
            "## Key Findings",
            "## Evidence Citations",
        ]
        format_mode = "structured"
    else:
        report_format = (os.getenv("A4T_REPORT_FORMAT", "structured") or "structured").strip().lower()
        if report_format == "dossier":
            required_sections = [
                "## 1. Executive Summary",
                "## 2. Target Biology",
                "## 3. Genetic Dependency",
                "## 4. Disease Associations",
                "## 8. Grounded Evidence Citations",
                "## 9. Conclusions",
            ]
            format_mode = "dossier"
        else:
            required_sections = [
                "## Executive Answer",
                "## Evidence Summary",
                "## Source Coverage",
                "## Conflicts & Caveats",
                "## Machine Appendix",
            ]
            format_mode = "concise"

    for section in required_sections:
        if section not in markdown:
            return False, f"Missing section: {section}"

    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(markdown):
            return False, f"Forbidden language matched: {pattern.pattern}"

    evidence_refs = {(item.evidence_id or "").strip() for item in items if (item.evidence_id or "").strip()}

    if format_mode in {"dossier", "structured"}:
        grounded_lines = [line.strip("- ").strip() for line in markdown.splitlines() if line.startswith("- [")]
        for line in grounded_lines:
            if evidence_refs and not any(f"[{ref}]" in line for ref in evidence_refs):
                return False, f"Unsupported citation reference: {line}"
    elif format_mode == "compiler":
        missing = [ref for ref in sorted(evidence_refs) if ref and ref not in markdown]
        if missing:
            return False, f"Missing evidence ids in compiled report: {missing[:3]}"
    else:
        # Concise format: require at least one evidence id reference if any items exist.
        if items and evidence_refs and not any(ref in markdown for ref in list(evidence_refs)[:5]):
            return False, "No evidence_id references found in report."

    return True, None
