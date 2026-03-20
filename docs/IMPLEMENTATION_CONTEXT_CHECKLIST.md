# Implementation Context Checklist (Phase-1)

Use this checklist before starting implementation and before merging any PR.

## Scope Lock
- [ ] Work is strictly within Phase-1 Evidence Collector scope from [WHAT_WE_ARE_BUILDING.md](/Users/apple/Desktop/Drugagent/docs/WHAT_WE_ARE_BUILDING.md).
- [ ] No Phase-2 features are implemented or implied as complete.
- [ ] No new biomedical sources were added without explicit approval.

## Flow Lock
- [ ] Runtime flow is preserved:
  `validate_input -> plan_collection -> collect_sources_parallel -> normalize_evidence -> verify_evidence -> analyze_conflicts -> build_evidence_graph -> generate_explanation -> human_review_gate -> emit_dossier`
- [ ] Node/edge changes are documented if flow behavior changes.

## Evidence Integrity
- [ ] Output claims are grounded in verified evidence only.
- [ ] Provenance fields are present for evidence records.
- [ ] Contradictions are flagged, not hidden.
- [ ] Human review gate behavior is preserved (`approved`, `rejected`, `needs_more_evidence`).

## Contract Safety
- [ ] Output schema changes are backward-compatible, or version bump/migration is documented.
- [ ] Phase-2 handoff payload contract remains valid.

## Quality Gates
- [ ] Tests for changed behavior are included or updated.
- [ ] Existing tests related to modified components pass.
- [ ] Logging/observability fields (`run_id`, status, durations) are preserved.

## Required References
- Product intent: [WHAT_WE_ARE_BUILDING.md](/Users/apple/Desktop/Drugagent/docs/WHAT_WE_ARE_BUILDING.md)
- Full flow/responsibilities: [COMPLETE_FLOW_AND_RESPONSIBILITIES.md](/Users/apple/Desktop/Drugagent/docs/COMPLETE_FLOW_AND_RESPONSIBILITIES.md)
- Requirements: [PRD_PHASE1_EVIDENCE_COLLECTOR.md](/Users/apple/Desktop/Drugagent/docs/PRD_PHASE1_EVIDENCE_COLLECTOR.md)
