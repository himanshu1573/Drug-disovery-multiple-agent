from __future__ import annotations

from agents.request_builders import build_collector_request
from agents.schema import SourceName
from cli.main import _parse_sources
from mcps.server import BundleCollectInput, _build_request


def test_request_builder_normalizes_entrypoint_defaults() -> None:
    request = build_collector_request(gene_symbol=" egfr ")

    assert request.gene_symbol == "EGFR"
    assert request.per_source_top_k == 5
    assert request.max_literature_articles == 5
    assert request.sources == [
        SourceName.DEPMAP,
        SourceName.PHAROS,
        SourceName.OPENTARGETS,
        SourceName.LITERATURE,
    ]


def test_cli_and_mcp_entrypoints_build_equivalent_requests() -> None:
    sources = _parse_sources("depmap,pharos")
    cli_request = build_collector_request(
        gene_symbol="kras",
        disease_id="EFO_0001071",
        sources=sources,
        per_source_top_k=7,
        max_literature_articles=7,
        model_override="gpt-5-mini",
        run_id="run-entrypoint-parity",
    )

    mcp_request = _build_request(
        BundleCollectInput(
            gene_symbol="kras",
            disease_id="EFO_0001071",
            sources=[SourceName.DEPMAP, SourceName.PHAROS],
            per_source_top_k=7,
            max_literature_articles=7,
            model_override="gpt-5-mini",
            run_id="run-entrypoint-parity",
        )
    )

    assert cli_request == mcp_request
