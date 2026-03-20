from __future__ import annotations

import asyncio
import time

import pytest

from agents.graph import collect_sources_in_parallel
from agents.schema import CollectorRequest, SourceName, SourceStatus, StatusName


@pytest.mark.asyncio
async def test_parallel_collection_synthetic_p95_latency_meets_budget() -> None:
    request = CollectorRequest(
        gene_symbol="EGFR",
        sources=[SourceName.DEPMAP, SourceName.PHAROS, SourceName.OPENTARGETS, SourceName.LITERATURE],
    )
    latencies: list[float] = []

    async def fake_collector(source, _request):
        await asyncio.sleep(0.01)
        status = SourceStatus(source=source, status=StatusName.SUCCESS, duration_ms=10, record_count=0)
        return [], status, [], {"source": source.value, "items": []}

    for _ in range(15):
        started = time.perf_counter()
        await collect_sources_in_parallel(request, collector=fake_collector)
        latencies.append(time.perf_counter() - started)

    p95 = sorted(latencies)[int(len(latencies) * 0.95) - 1]
    assert p95 < 0.2


@pytest.mark.asyncio
async def test_parallel_collection_handles_concurrent_runs_under_budget() -> None:
    request = CollectorRequest(
        gene_symbol="EGFR",
        sources=[SourceName.DEPMAP, SourceName.PHAROS, SourceName.OPENTARGETS, SourceName.LITERATURE],
    )

    async def fake_collector(source, _request):
        await asyncio.sleep(0.01)
        status = SourceStatus(source=source, status=StatusName.SUCCESS, duration_ms=10, record_count=0)
        return [], status, [], {"source": source.value, "items": []}

    started = time.perf_counter()
    results = await asyncio.gather(*[collect_sources_in_parallel(request, collector=fake_collector) for _ in range(10)])
    elapsed = time.perf_counter() - started

    assert len(results) == 10
    assert elapsed < 0.5
