from __future__ import annotations

from agents.request_builders import build_collector_request
from agents.schema import SourceName
from cli.main import _parse_sources
from mcps.server import BundleCollectInput, _build_request


def test_force_source_overrides_requested_sources_for_mcp_tools() -> None:
    request = _build_request(
        BundleCollectInput(
            gene_symbol="EGFR",
            sources=[SourceName.DEPMAP, SourceName.LITERATURE],
        ),
        force_source=SourceName.OPENTARGETS,
    )

    assert request.sources == [SourceName.OPENTARGETS]


def test_cli_source_parser_matches_shared_request_builder_contract() -> None:
    parsed_sources = _parse_sources("literature,depmap")
    request = build_collector_request(gene_symbol="TP53", sources=parsed_sources)

    assert request.sources == [SourceName.LITERATURE, SourceName.DEPMAP]
    assert request.gene_symbol == "TP53"
