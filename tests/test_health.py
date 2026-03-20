from __future__ import annotations

import os

import pytest

from agents.health import run_source_health_checks, validate_source_health
from agents.request_builders import build_collector_request
from agents.schema import SourceName


def test_source_health_checks_report_requested_sources(monkeypatch, tmp_path) -> None:
    depmap_cache = tmp_path / "CRISPRGeneEffect.csv"
    depmap_cache.write_text("gene\nKRAS\n", encoding="utf-8")
    monkeypatch.setenv("DEPMAP_CACHE_FILE", str(depmap_cache))
    request = build_collector_request(
        gene_symbol="KRAS",
        sources=[SourceName.DEPMAP, SourceName.PHAROS, SourceName.OPENTARGETS],
    )

    results = run_source_health_checks(request)

    assert [result.source for result in results] == ["depmap", "pharos", "opentargets"]
    assert any(result.source == "depmap" and result.healthy for result in results)


def test_validate_source_health_fails_fast_when_pharos_launcher_missing(monkeypatch) -> None:
    request = build_collector_request(gene_symbol="KRAS", sources=[SourceName.EXT_PHAROS])
    original_exists = os.path.exists

    def fake_exists(path: str) -> bool:
        if path.endswith("external_mcps/run_pharos_mcp.sh"):
            return False
        return original_exists(path)

    monkeypatch.setattr(os.path, "exists", fake_exists)

    with pytest.raises(RuntimeError, match="Pharos launcher missing"):
        validate_source_health(request)
