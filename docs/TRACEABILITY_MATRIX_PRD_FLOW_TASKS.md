# Traceability Matrix: PRD -> Flow -> Task Master

**Date:** March 9, 2026  
**Scope:** Phase-1 Evidence Collector only  
**Sources:**
- [PRD_PHASE1_EVIDENCE_COLLECTOR.md](/Users/apple/Desktop/Drugagent/docs/PRD_PHASE1_EVIDENCE_COLLECTOR.md)
- [COMPLETE_FLOW_AND_RESPONSIBILITIES.md](/Users/apple/Desktop/Drugagent/docs/COMPLETE_FLOW_AND_RESPONSIBILITIES.md)
- [WHAT_WE_ARE_BUILDING.md](/Users/apple/Desktop/Drugagent/docs/WHAT_WE_ARE_BUILDING.md)
- [.taskmaster/tasks/tasks.json](/Users/apple/Desktop/Drugagent/.taskmaster/tasks/tasks.json)

---

## Canonical Runtime Flow

`validate_input -> plan_collection -> collect_sources_parallel -> normalize_evidence -> verify_evidence -> analyze_conflicts -> build_evidence_graph -> generate_explanation -> human_review_gate -> emit_dossier`

---

## FR/NFR -> Flow Stage -> Task IDs

| Requirement | Flow Stage(s) | Task Master IDs |
|---|---|---|
| FR-1 Input Contract | `validate_input` | 6, 10 |
| FR-2 Orchestration + State Machine | all stages | 8, 10, 12, 29, 37 |
| FR-3 Planning Agent | `plan_collection` | 11, 28 |
| FR-4 Evidence Collectors (parallel) | `collect_sources_parallel` | 5, 14, 32 |
| FR-5 Normalization Agent | `normalize_evidence` | 15, 16 |
| FR-6 Verification Agent | `verify_evidence` | 17, 18, 27 |
| FR-7 Conflict Analyzer | `analyze_conflicts` | 19 |
| FR-8 Evidence Graph Builder | `build_evidence_graph` | 20 |
| FR-9 Explanation Agent | `generate_explanation` | 21, 45 |
| FR-10 Human Review Gateway | `human_review_gate` | 24, 25, 43 |
| FR-11 Memory System | cross-stage memory | 26, 27, 28, 29 |
| FR-12 Final Output Contract | `emit_dossier` | 22, 23, 39 |
| NFR-1 Reliability | retries/failure behavior | 13, 30, 32, 38 |
| NFR-2 Performance | collection/execution/runtime | 14, 30, 40 |
| NFR-3 Traceability | provenance + run artifacts | 18, 22, 44, 46 |
| NFR-4 Observability | structured logs + metrics | 30, 31, 46 |
| NFR-5 Security | secret handling/auditability | 25, 33 |
| NFR-6 Maintainability | versioning, tests, CI gates | 9, 35, 39, 41 |

---

## Flow Stage -> Task IDs

| Flow Stage | Primary Task IDs | Supporting Task IDs |
|---|---|---|
| `validate_input` | 6, 10 | 8, 9 |
| `plan_collection` | 11 | 28 |
| `collect_sources_parallel` | 5, 14 | 13, 32, 47 |
| `normalize_evidence` | 15 | 16 |
| `verify_evidence` | 17, 18 | 27, 35 |
| `analyze_conflicts` | 19 | 35 |
| `build_evidence_graph` | 20 | 44 |
| `generate_explanation` | 21 | 45 |
| `human_review_gate` | 24, 43 | 25 |
| `emit_dossier` | 22, 23 | 39, 44 |
| Cross-cutting ops/quality | 30, 31, 34, 40, 41, 42, 46, 48 | 1, 2, 3, 4, 7 |

---

## Coverage Check

- FR covered: `12/12`
- NFR covered: `6/6`
- Flow stages covered: `10/10`
- Unassigned requirements: `0`

---

## Change Rule

When PRD/flow/tasks change, update this matrix in the same PR.  
No PR is complete if it introduces a new requirement or stage without traceability mapping.
