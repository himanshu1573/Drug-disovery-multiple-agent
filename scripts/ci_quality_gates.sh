#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="python3"
if [[ -x "venv/bin/python" ]]; then
  PYTHON_BIN="venv/bin/python"
fi

"$PYTHON_BIN" -m ruff check agents cli mcps tests
"$PYTHON_BIN" -m mypy agents cli mcps --ignore-missing-imports

"$PYTHON_BIN" -m coverage erase
"$PYTHON_BIN" -m coverage run -m pytest \
  tests/test_phase1_schema.py \
  tests/test_contract_versions.py \
  tests/test_graph_topology.py \
  tests/test_graph_checkpoint_resume.py \
  tests/test_graph_observability.py \
  tests/test_evidence_graph.py \
  tests/test_conflicts.py \
  tests/test_verifier.py \
  tests/test_planner.py \
  tests/test_retry_policy.py \
  tests/test_parallel_collection.py \
  tests/test_normalizer.py \
  tests/test_summary_agent.py \
  tests/test_metrics.py \
  tests/test_connector_integrations.py \
  tests/test_resilience.py \
  tests/test_performance_slo.py \
  tests/test_health.py \
  tests/test_request_builders.py \
  tests/test_server_manager.py \
  tests/test_entrypoint_contracts.py \
  tests/test_dossier_emitter.py \
  tests/test_config_profiles.py \
  tests/test_handoff_contract.py \
  tests/test_review_gate.py \
  tests/test_review_audit.py \
  tests/test_episodic_memory.py \
  tests/test_review_interface_contract.py \
  tests/test_summary_validation.py \
  tests/test_state_machine_e2e.py \
  tests/test_contract_regressions.py
"$PYTHON_BIN" -m coverage report --fail-under=80
