from __future__ import annotations

from pathlib import Path


def test_ci_quality_gate_script_enforces_required_commands() -> None:
    text = Path("scripts/ci_quality_gates.sh").read_text(encoding="utf-8")

    assert "ruff check" in text
    assert "mypy agents cli mcps" in text
    assert "coverage report --fail-under=80" in text


def test_github_workflows_reference_quality_gates_and_nightly_audit() -> None:
    ci = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")
    nightly = Path(".github/workflows/nightly-provenance-audit.yml").read_text(encoding="utf-8")

    assert "scripts/ci_quality_gates.sh" in ci
    assert "schedule:" in nightly
    assert "scripts/nightly_provenance_audit.py" in nightly
