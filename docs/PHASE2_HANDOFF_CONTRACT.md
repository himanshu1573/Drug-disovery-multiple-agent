# Phase-2 Handoff Contract

`EvidenceDossier.handoff_payload` is the machine interface from Phase-1 Evidence Collector to downstream Phase-2 agents.

## Version

- `handoff_version`: `phase2.v1`

## Fields

- `handoff_version`: version pin for compatibility checks
- `phase`: fixed target stage name, currently `phase2`
- `run_id`: originating Phase-1 run
- `ready`: `true` only when verification is not blocked and review is not pending
- `review_required`: whether human review is still required
- `blocking_issues`: blocking verification rule names
- `warning_issues`: non-blocking verification rule names
- `conflict_count`: number of emitted `ConflictRecord` items
- `evidence_count`: verified evidence record count
- `requested_source_count`: number of requested sources for the run
- `successful_source_count`: number of successful sources
- `dossier_artifact_path`: persisted dossier artifact path
- `graph_artifact_path`: persisted graph artifact path
- `reason`: machine-readable readiness rationale

## Semantics

- If `ready=false` and `reason=verification_blocked`, downstream agents must not treat the dossier as promotion-ready.
- If `ready=false` and `review_required=true`, downstream agents may inspect artifacts but must not auto-advance workflow state.
- `blocking_issues` and `warning_issues` are rule names from the verification contract, not free-form prose.

## Stability

- Additive changes are allowed in minor contract updates.
- Removing or renaming fields requires a version bump.
- Consumers should pin on `handoff_version`.
