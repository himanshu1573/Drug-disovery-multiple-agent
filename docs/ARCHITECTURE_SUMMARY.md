# Architecture Summary (Phase-1)

Phase-1 is a multi-agent Evidence Collector for gene-disease research.

## What It Does

- Takes gene/disease query input
- Runs planned multi-source evidence collection in parallel
- Normalizes and verifies evidence
- Detects cross-source conflicts
- Builds evidence graph snapshot
- Produces explanation and human-reviewable dossier
- Emits machine-readable handoff payload for Phase-2

## Canonical Flow

```text
validate_input -> plan_collection -> collect_sources_parallel -> normalize_evidence -> verify_evidence -> analyze_conflicts -> build_evidence_graph -> generate_explanation -> human_review_gate -> emit_dossier
```

## Core Components

- Orchestrator (LangGraph)
- Planning Agent
- 4 Evidence Collectors (DepMap/OpenTargets/PHAROS/Literature)
- Normalization Agent
- Verification Agent
- Conflict Analyzer
- Evidence Graph Builder
- Explanation Agent
- Human Review Gateway
- Memory subsystems (episodic/semantic/procedural/working)

## Output

Primary output: `EvidenceDossier` containing verified evidence, conflicts, provenance, graph snapshot, review decision, and downstream handoff payload.

## Scope Guardrails

- Use only approved Phase-1 sources.
- Do not output unsupported claims.
- Do not bypass verification/review stages.
- Do not treat Phase-2 capabilities as done in Phase-1.

## Related Docs

- [WHAT_WE_ARE_BUILDING.md](/Users/apple/Desktop/Drugagent/docs/WHAT_WE_ARE_BUILDING.md)
- [COMPLETE_FLOW_AND_RESPONSIBILITIES.md](/Users/apple/Desktop/Drugagent/docs/COMPLETE_FLOW_AND_RESPONSIBILITIES.md)
- [PRD_PHASE1_EVIDENCE_COLLECTOR.md](/Users/apple/Desktop/Drugagent/docs/PRD_PHASE1_EVIDENCE_COLLECTOR.md)
- [TRACEABILITY_MATRIX_PRD_FLOW_TASKS.md](/Users/apple/Desktop/Drugagent/docs/TRACEABILITY_MATRIX_PRD_FLOW_TASKS.md)
