# Artifact Storage Policy

## Layout

Artifacts are stored under `artifacts/` with deterministic names keyed by `run_id`.

- `plans/<run_id>.collection_plan.json`
- `graphs/<run_id>.evidence_graph.json`
- `dossiers/<run_id>.evidence_dossier.json`
- `metrics/<run_id>.metrics.json`
- `health_reports/<run_id>.health.json`
- `review_audit/<run_id>/<timestamp>_<reviewer_id>.review.json`
- `review_decisions/<run_id>.review_decision.json`
- `procedural_memory/<run_id>.procedural_memory.json`
- `working_memory/<run_id>/`
- `episodic_memory/runs.json`
- `audits/nightly_provenance_audit.json`

## Retention

- Keep explicitly retained `run_id` artifacts.
- Remove non-retained run-scoped artifacts using the retention utility.
- Keep `episodic_memory/runs.json` as the long-lived index.

## Runtime helper

- Layout and retention helpers live in [agents/artifact_store.py](/Users/apple/Desktop/Drugagent/agents/artifact_store.py).
