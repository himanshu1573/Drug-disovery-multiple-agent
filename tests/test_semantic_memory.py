from __future__ import annotations

from agents.semantic_memory import disease_aliases, gene_aliases, load_semantic_memory


def test_semantic_memory_bootstraps_default_knowledge(tmp_path) -> None:
    knowledge = load_semantic_memory(tmp_path)

    assert "gene_aliases" in knowledge
    assert knowledge["gene_aliases"]["EGFR"] == ["ERBB1"]


def test_gene_aliases_include_canonical_symbol_and_known_alias(tmp_path) -> None:
    aliases = gene_aliases("egfr", tmp_path)

    assert aliases == {"EGFR", "ERBB1"}


def test_disease_aliases_include_colon_and_underscore_variants(tmp_path) -> None:
    aliases = disease_aliases("EFO_0001071", tmp_path)

    assert aliases == {"EFO_0001071", "EFO:0001071"}
