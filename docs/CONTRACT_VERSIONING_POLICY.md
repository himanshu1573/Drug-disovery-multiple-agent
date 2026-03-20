# Contract Versioning Policy

## Scope

This policy governs machine-readable output contracts emitted by the Phase-1 Evidence Collector:

- `CollectorResult`
- `EvidenceDossier`
- embedded contract artifacts such as `CollectionPlan` and `VerificationReport`

It exists to keep Phase-2 handoffs stable while allowing controlled schema evolution.

## Current Contract Versions

- `schema_version`: `0.1.0`
- `CollectionPlan.plan_version`: `phase1.v1`
- `VerificationReport.verification_policy_version`: `phase1.v1`

## Compatibility Rules

### Patch Version

Use a patch bump when:

- fixing docs or examples only
- tightening implementation without changing serialized output
- adding internal validation that does not reject previously valid persisted payloads

Patch releases must remain backward-compatible.

### Minor Version

Use a minor bump when:

- adding new optional fields
- adding new optional enum values that downstream consumers may ignore safely
- extending handoff payload content without changing required existing fields

Minor releases must preserve all existing required fields and field meanings.

### Major Version

Use a major bump when:

- renaming or removing fields
- changing field types or semantics
- making optional fields required
- changing default interpretation of an existing field in a way that affects downstream logic

Any major bump requires:

- migration notes in this document
- updated regression tests
- explicit downstream compatibility review before release

## Stability Guarantees

For `CollectorResult` and `EvidenceDossier`, the following top-level fields are treated as stable for `0.x` compatibility within this Phase-1 project:

- `schema_version`
- `run_id`
- `query`

Additional stable fields:

- `CollectorResult`: `items`, `source_status`, `errors`, `llm_summary`
- `EvidenceDossier`: `plan`, `verified_evidence`, `verification_report`, `conflicts`, `graph_snapshot`, `review_decision`, `summary_markdown`, `handoff_payload`

Do not remove or rename these fields without a documented version bump.

## Migration Notes

### `0.1.0`

- initial versioned contract baseline for Phase-1 collector outputs
- introduces explicit Phase-1 artifacts:
  - `CollectionPlan`
  - `VerificationReport`
  - `ConflictRecord`
  - `EvidenceGraphSnapshot`
  - `ReviewDecision`
  - `EvidenceDossier`

## Testing Policy

Regression tests must fail if:

- `schema_version` changes unexpectedly
- required top-level fields disappear from `CollectorResult` or `EvidenceDossier`
- `CollectionPlan.plan_version` changes without an intentional update
- `VerificationReport.verification_policy_version` changes without an intentional update

These checks live in the test suite and should be updated in the same change set as any intentional contract version bump.
