from __future__ import annotations

import pytest

from agents.schema import CollectorRequest, SourceName, StatusName
from mcps.connectors.depmap import DepMapConnector
from mcps.connectors.literature import LiteratureConnector
from mcps.connectors.opentargets import OpenTargetsConnector
from mcps.connectors.pharos import PharosConnector


@pytest.mark.asyncio
async def test_opentargets_connector_returns_contract_with_mocked_graphql(monkeypatch) -> None:
    connector = OpenTargetsConnector()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311")

    async def fake_resolve(_symbol: str):
        return "ENSG00000146648", "EGFR"

    async def fake_graphql(_query: str, _variables: dict):
        return {
            "target": {
                "id": "ENSG00000146648",
                "approvedSymbol": "EGFR",
                "associatedDiseases": {
                    "count": 1,
                    "rows": [{"score": 0.91, "disease": {"id": "EFO_0000311", "name": "NSCLC"}}],
                },
            }
        }

    monkeypatch.setattr(connector, "_resolve_target", fake_resolve)
    monkeypatch.setattr(connector, "_graphql", fake_graphql)

    items, status, errors = await connector.collect(request)

    assert len(items) == 1
    assert status.status == StatusName.SUCCESS
    assert errors == []


@pytest.mark.asyncio
async def test_pharos_connector_returns_annotation_with_mocked_graphql(monkeypatch) -> None:
    connector = PharosConnector()
    request = CollectorRequest(gene_symbol="EGFR")

    async def fake_graphql(_query: str, _variables: dict):
        return {"target": {"sym": "EGFR", "name": "EGFR", "tdl": "Tclin", "fam": "Kinase", "novelty": 0.2, "ligandCounts": [{"value": 12}]}}

    monkeypatch.setattr(connector, "_graphql", fake_graphql)
    items, status, errors = await connector.collect(request)

    assert len(items) == 1
    assert items[0].evidence_type == "target_annotation"
    assert status.status == StatusName.SUCCESS
    assert errors == []


@pytest.mark.asyncio
async def test_literature_connector_returns_articles_with_mocked_http(monkeypatch) -> None:
    connector = LiteratureConnector()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", per_source_top_k=2)

    async def fake_get_json(*_args, **_kwargs):
        return {
            "hitCount": 2,
            "resultList": {
                "result": [
                    {"pmid": "1", "title": "Paper 1", "journalTitle": "J1", "pubYear": "2024", "citedByCount": 10},
                    {"pmid": "2", "title": "Paper 2", "journalTitle": "J2", "pubYear": "2023", "citedByCount": 4},
                ]
            },
        }

    monkeypatch.setattr(connector.http, "get_json", fake_get_json)
    items, status, errors = await connector.collect(request)

    assert len(items) == 2
    assert all(item.source == SourceName.LITERATURE for item in items)
    assert status.status == StatusName.SUCCESS
    assert errors == []


@pytest.mark.asyncio
async def test_literature_connector_caps_by_max_literature_articles(monkeypatch) -> None:
    connector = LiteratureConnector()
    request = CollectorRequest(gene_symbol="EGFR", disease_id="EFO_0000311", per_source_top_k=10, max_literature_articles=2)

    async def fake_get_json(*_args, **_kwargs):
        return {
            "hitCount": 5,
            "resultList": {
                "result": [
                    {"pmid": "1", "title": "EGFR Paper 1", "journalTitle": "J1", "pubYear": "2024", "citedByCount": 10},
                    {"pmid": "2", "title": "EGFR Paper 2", "journalTitle": "J2", "pubYear": "2023", "citedByCount": 9},
                    {"pmid": "3", "title": "EGFR Paper 3", "journalTitle": "J3", "pubYear": "2022", "citedByCount": 8},
                    {"pmid": "4", "title": "EGFR Paper 4", "journalTitle": "J4", "pubYear": "2021", "citedByCount": 7},
                    {"pmid": "5", "title": "EGFR Paper 5", "journalTitle": "J5", "pubYear": "2020", "citedByCount": 6},
                ]
            },
        }

    monkeypatch.setattr(connector.http, "get_json", fake_get_json)
    items, status, errors = await connector.collect(request)

    assert len(items) == 2
    assert status.status == StatusName.SUCCESS
    assert errors == []


@pytest.mark.asyncio
async def test_depmap_connector_uses_loaded_dataframe_without_disk_reload(monkeypatch) -> None:
    import pandas as pd
    import mcps.connectors.depmap as depmap_module

    connector = DepMapConnector()
    request = CollectorRequest(gene_symbol="EGFR", per_source_top_k=2)

    monkeypatch.setattr(depmap_module.os.path, "exists", lambda _path: True)
    depmap_module._df = pd.DataFrame({"EGFR (1956)": [-1.2, -0.7]}, index=["CL1", "CL2"])
    depmap_module._col_map = {"EGFR": "EGFR (1956)"}

    items, status, errors = await connector.collect(request)

    assert len(items) == 2
    assert items[0].evidence_type == "genetic_dependency"
    assert status.status == StatusName.SUCCESS
    assert errors == []
