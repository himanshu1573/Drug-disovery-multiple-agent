from __future__ import annotations

import asyncio
import json

import pytest

from agents.episodic_memory import query_episodic_memory
from agents.graph import collect_sources_in_parallel
from agents.schema import CollectorRequest, ErrorCode, SourceName, StatusName


def test_episodic_memory_corrupt_store_is_quarantined(tmp_path) -> None:
    mem_dir = tmp_path / "episodic_memory"
    mem_dir.mkdir(parents=True, exist_ok=True)
    path = mem_dir / "runs.json"
    path.write_text("{not valid json", encoding="utf-8")

    runs = query_episodic_memory(gene_symbol="KRAS", root=tmp_path)
    assert runs == []

    # Store should be reset to valid JSON.
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload == []

    # A corrupt backup should exist.
    backups = list(mem_dir.glob("runs.json.corrupt.*"))
    assert backups


def test_collector_request_normalizes_inputs_and_sources_default() -> None:
    req = CollectorRequest(
        gene_symbol=" kras ",
        disease_id="EFO:0000311",
        sources=[],
        run_id="  run-xyz  ",
    )
    assert req.gene_symbol == "KRAS"
    assert req.disease_id == "EFO_0000311"
    assert req.run_id == "run-xyz"
    # Explicit empty sources should remain empty (offline/test runs may seed evidence directly).
    assert req.sources == []


@pytest.mark.asyncio
async def test_collect_sources_times_out_hung_collector(monkeypatch) -> None:
    monkeypatch.setenv("A4T_SOURCE_TIMEOUT_S", "0.1")

    async def hung_collector(_source: SourceName, _request: CollectorRequest):
        await asyncio.sleep(10)
        raise AssertionError("should have timed out")

    req = CollectorRequest(gene_symbol="KRAS", sources=[SourceName.DEPMAP], run_id="run-timeout-test")
    result = await collect_sources_in_parallel(req, collector=hung_collector)

    assert result["source_status"]
    status = result["source_status"][0]
    assert status.source == SourceName.DEPMAP
    assert status.status == StatusName.FAILED
    assert status.error_code == ErrorCode.TIMEOUT
    assert result["errors"]
    assert result["errors"][0].error_code == ErrorCode.TIMEOUT
