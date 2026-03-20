from __future__ import annotations

import json
from pathlib import Path

from agents.working_memory import persist_working_memory_snapshot
from agents.schema import CollectorRequest


def test_working_memory_persists_jsonable_state(tmp_path) -> None:
    request = CollectorRequest(gene_symbol="KRAS", run_id="run-working-memory", sources=[])
    path = Path(
        persist_working_memory_snapshot(
            request.run_id,
            "validate_input",
            {"state": {"query": request}, "update": {"query": request}},
            tmp_path,
        )
    )

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert path.name == "validate_input.json"
    assert payload["state"]["query"]["run_id"] == request.run_id
    assert payload["update"]["query"]["gene_symbol"] == "KRAS"
