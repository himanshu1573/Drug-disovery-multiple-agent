from __future__ import annotations

import json
from pathlib import Path

from agents.graph import COLLECTOR_NODE_SEQUENCE
from agents.procedural_memory import persist_procedural_memory, procedural_memory_payload


def test_procedural_memory_payload_tracks_versions_and_prompt_signature() -> None:
    payload = procedural_memory_payload("run-proc", COLLECTOR_NODE_SEQUENCE)

    assert payload["run_id"] == "run-proc"
    assert payload["collector_node_sequence"] == COLLECTOR_NODE_SEQUENCE
    assert len(payload["summary_prompt_hash"]) == 12


def test_procedural_memory_persists_json_artifact(tmp_path) -> None:
    path = Path(persist_procedural_memory("run-proc", COLLECTOR_NODE_SEQUENCE, tmp_path))
    payload = json.loads(path.read_text(encoding="utf-8"))

    assert path.name == "run-proc.procedural_memory.json"
    assert payload["collector_node_sequence"] == COLLECTOR_NODE_SEQUENCE
