# Product Requirements Document (PRD)
## Phase-1 Drug Discovery Evidence Collector (Multi-Agent + MCP)

**Version:** 1.0  
**Date:** March 9, 2026  
**Status:** Draft for implementation alignment  
**Owners:** Platform Engineering, Applied AI, Bioinformatics  

---

## Canonical Intent Reference

Before implementing any feature, align with:
- [WHAT_WE_ARE_BUILDING.md](/Users/apple/Desktop/Drugagent/docs/WHAT_WE_ARE_BUILDING.md)

This prevents scope drift and implementation hallucination.

---

## 1. Product Overview

Build a production-ready **Phase-1 Evidence Collector** that accepts a target gene and optional disease context, collects evidence from multiple biomedical sources in parallel, verifies and normalizes the evidence, detects conflicts, generates a structured evidence dossier, and supports human-in-the-loop review before handoff to downstream Phase-2 agents (target ranking, pathway reasoning, drug design).

This PRD aligns to the architecture vision and current codebase status, and defines:
- Exact requirements (functional + non-functional)
- Delivery phases and engineering plan
- Test strategy and acceptance criteria
- Risks, mitigations, and operational readiness requirements

---

## 2. Problem Statement

Current capabilities already collect evidence from DepMap, Open Targets, PHAROS, and Literature via MCP-driven orchestration, but the end-to-end Phase-1 architecture is only partially implemented.

Key gaps to close:
- No explicit planning-agent stage with dynamic task plans
- Limited verification (schema-level checks exist, but not comprehensive integrity checks)
- No first-class conflict analyzer output model
- No explicit evidence graph persistence/query layer
- Human review flow is not yet represented as an operational gate
- Memory architecture is conceptual, not implemented as a persistent subsystem
- Testing is not organized into a production-grade quality gate matrix

---

## 3. Goals and Non-Goals

### 3.1 Goals
- Deliver a reliable multi-agent Phase-1 pipeline with deterministic orchestration and robust failure handling.
- Standardize all evidence into a canonical, provenance-rich schema.
- Add validation and contradiction detection before dossier generation.
- Introduce review gating for scientific oversight.
- Provide a machine-usable output package for Phase-2 agents.
- Establish a complete production test strategy (unit, integration, E2E, reliability, performance).

### 3.2 Non-Goals (Phase-1)
- No target ranking model training (belongs to Phase-2).
- No medicinal chemistry generation or docking workflows.
- No automated clinical recommendation engine.
- No full ontology curation platform.

---

## 4. Users and Stakeholders

### 4.1 Primary Users
- Computational biologists
- Translational scientists
- AI/ML research engineers

### 4.2 Secondary Users
- Platform SRE/DevOps
- QA automation engineers
- Product/program managers

### 4.3 Stakeholders
- Drug discovery leadership
- Applied AI platform team
- Compliance and scientific review group

---

## 5. User Stories

1. As a scientist, I submit `gene=KRAS`, `disease=Lung Cancer` and receive a transparent, source-backed evidence dossier.
2. As a reviewer, I can approve/reject flagged evidence conflicts before downstream use.
3. As an engineer, I can trace every evidence claim to source, endpoint, query, and retrieval time.
4. As an orchestration service, I can retry failed source calls and still produce partial but valid outputs.
5. As a Phase-2 agent, I can consume a stable, versioned evidence package contract.

---

## 6. Current-State Assessment (Codebase Snapshot)

### 6.1 Already Implemented
- LangGraph orchestration with nodes for validation, parallel MCP collection, and merge/summary.
- MCP runtime for DepMap, Open Targets, PHAROS, Literature.
- Canonical Pydantic contracts for request/evidence/status/result.
- CLI flow for single-run and REPL execution.
- Deterministic fallback summary when no LLM key exists.
- External PHAROS server lifecycle helper.

### 6.2 Partial / Missing vs Target Architecture
- Planning Agent: not explicit as a dedicated node with plan artifact.
- Normalization Agent: partial; no dedicated normalization stage node with confidence harmonization rules as a separately versioned component.
- Verification Agent: limited to parsing/validation, missing deeper checks (duplicate semantics, citation completeness, gene mapping confidence, ontology validation).
- Conflict Analyzer: no separate persisted conflict entity and severity classification output.
- Evidence Graph Builder: conceptual only, no graph storage contract or query API.
- Human Review Gateway: no formal approval state machine and decision audit trail.
- Memory System: no episodic/semantic/procedural/working memory persistence layer.

### 6.3 Technical Debt to Resolve in Phase-1 Hardening
- Schema/implementation consistency checks across agent layers must be enforced in CI.
- MCP server and collector interfaces need versioned compatibility tests.
- Test tooling bootstrap is incomplete in the current local environment.

---

## 7. Scope (Phase-1 Deliverables)

### 7.1 In Scope
- Multi-agent execution flow:
  - Orchestrator
  - Planner
  - Parallel collectors
  - Normalization
  - Verification
  - Conflict analyzer
  - Evidence graph build
  - Explanation
  - Human review gate
  - Final dossier + handoff package
- Memory integration for Phase-1 requirements (minimal viable implementation for all 4 memory classes).
- Observability, provenance, and quality gates.

### 7.2 Out of Scope
- Phase-2 ranking and design execution.
- Full UI suite beyond review gateway MVP.

---

## 8. Functional Requirements

### FR-1 Input Contract
- Accept required `gene_symbol` and optional `disease_id`, with defaults for species and source list.
- Validate against schema and reject malformed requests with typed errors.

### FR-2 Orchestration and State Machine
- Implement deterministic LangGraph state transitions:
  1. `validate_input`
  2. `plan_collection`
  3. `collect_sources_parallel`
  4. `normalize_evidence`
  5. `verify_evidence`
  6. `analyze_conflicts`
  7. `build_evidence_graph`
  8. `generate_explanation`
  9. `human_review_gate`
  10. `emit_dossier`
- Persist checkpoint state per run for resumability.

### FR-3 Planning Agent
- Produce explicit plan artifact per run with:
  - Selected sources
  - Query variants
  - Priority and retry policy
  - Expected outputs per source
- Store plan in working memory + run artifacts.

### FR-4 Evidence Collection Agents
- Run DepMap/OpenTargets/PHAROS/Literature in parallel.
- Capture source-level status: success/partial/failed/skipped.
- Capture timing and error taxonomy (timeout, rate limit, upstream error, parse, validation).

### FR-5 Normalization Agent
- Convert all source payloads into canonical `EvidenceRecord` schema.
- Enforce normalized fields:
  - `target_symbol`, `target_id`, `disease_id`, `evidence_type`, `confidence`, `provenance`
- Apply normalization policy versioning (`normalization_policy_version`).

### FR-6 Verification Agent
- Required checks:
  - Schema validity
  - Required provenance completeness
  - Duplicate detection
  - Incorrect gene mapping detection
  - Missing citations for literature-backed claims
  - Ontology ID format checks (EFO/MONDO when provided)
- Emit verification report with pass/fail counts and blocking issues.

### FR-7 Conflict Analyzer
- Detect contradictory evidence across sources.
- Classify conflicts (`low`, `medium`, `high`) and rationale.
- Add conflict records to dossier and review queue.

### FR-8 Evidence Graph Builder
- Build typed graph relations:
  - Target -> Disease
  - Target -> Evidence
  - Evidence -> Publication
  - Evidence -> Source
- Emit serializable graph snapshot (JSON-LD or equivalent structured format).

### FR-9 Explanation Agent
- Generate structured evidence summary grounded only in verified evidence.
- Include source coverage, confidence profile, and conflict notes.

### FR-10 Human Review Gateway
- Review outcomes:
  - `approved`
  - `rejected`
  - `needs_more_evidence`
- Require reviewer identity, timestamp, and decision reason.

### FR-11 Memory System
- Episodic memory: store run-level outcomes and decisions.
- Semantic memory: cached biomedical facts/ontology mappings.
- Procedural memory: agent runbook/prompt and tool policy versions.
- Working memory: current run state and intermediate artifacts.

### FR-12 Final Output Contract
- Produce `EvidenceDossier` with:
  - Run metadata
  - Verified evidence list
  - Conflict list
  - Graph snapshot
  - Review decision
  - Handoff payload for Phase-2

---

## 9. Non-Functional Requirements

### NFR-1 Reliability
- P95 successful run completion (with partial tolerance): >= 99% under normal upstream availability.
- Retry with exponential backoff for transient failures.

### NFR-2 Performance
- P95 Phase-1 runtime <= 45s for standard 4-source query (excluding human review wait).
- Per-source timeout budgets configurable.

### NFR-3 Traceability
- 100% of output evidence must include provenance provider, endpoint, query, retrieval timestamp.

### NFR-4 Observability
- Structured logs per node execution.
- Metrics: source latency, success/failure ratios, verification failures, conflict rates.
- Run-level correlation via `run_id`.

### NFR-5 Security
- Secrets via environment manager only.
- No PHI storage in logs/artifacts.
- Audit trail for human review actions.

### NFR-6 Maintainability
- Versioned schemas and backward compatibility policy for output contracts.
- Component-level test coverage gate.

---

## 10. System Architecture Specification

### 10.1 Runtime Topology
- **Control plane:** LangGraph orchestrator state machine
- **Execution plane:** MCP source collectors + processing agents
- **Data plane:** canonical evidence store + graph snapshot artifacts + run metadata
- **Review plane:** approval/rejection gate before final handoff

### 10.2 State Model (Minimum)
- `query`
- `plan`
- `raw_source_payloads`
- `normalized_items`
- `verification_report`
- `conflicts`
- `evidence_graph`
- `explanation`
- `review_decision`
- `final_dossier`

### 10.3 Failure Policy
- Source-level fail does not terminate run if minimum source threshold is still achievable.
- Verification blocking errors prevent dossier finalization until review/override.
- Human rejection loops run back to planning with additional evidence constraints.

---

## 11. Implementation Plan

### Phase A: Core Pipeline Refactor (Week 1-2)
- Add planner, normalization, verification, conflict nodes.
- Expand collector state object and run artifact model.
- Introduce explicit intermediate contracts.

### Phase B: Graph + Review + Memory MVP (Week 3-4)
- Implement evidence graph builder and serialized snapshot.
- Add human review decision model and persistence.
- Implement minimal episodic/working memory storage.

### Phase C: Hardening and Ops (Week 5)
- Add observability instrumentation.
- Enforce CI quality gates and contract tests.
- Run reliability/performance tests and tune timeouts/retries.

### Phase D: Release Readiness (Week 6)
- UAT with scientist workflows.
- Freeze contracts and publish integration docs for Phase-2 agents.

---

## 12. Data Contracts

### 12.1 Canonical EvidenceRecord (Required Fields)
- `source`
- `target_id`
- `target_symbol`
- `disease_id`
- `evidence_type`
- `raw_value`
- `normalized_score`
- `confidence`
- `summary`
- `support`
- `provenance.provider`
- `provenance.endpoint`
- `provenance.query`
- `provenance.retrieved_at`

### 12.2 New Phase-1 Contracts to Add
- `CollectionPlan`
- `VerificationReport`
- `ConflictRecord`
- `EvidenceGraphSnapshot`
- `ReviewDecision`
- `EvidenceDossier`

---

## 13. Test Strategy (Production Quality)

### 13.1 Test Levels
- **Unit tests:** schema validators, mapping functions, conflict rules, retry policy, planner logic.
- **Integration tests:** each MCP source connector with mocked upstream responses.
- **Workflow tests:** full LangGraph state-machine progression with synthetic payloads.
- **E2E tests:** real-source smoke tests for supported genes (KRAS, EGFR, TP53).
- **Resilience tests:** timeout, 429, malformed payload, partial source failures.
- **Performance tests:** latency budgets under concurrent runs.
- **Regression tests:** snapshot tests for dossier shape and key sections.

### 13.2 Requirements-to-Test Matrix
- FR-1 -> input validation tests (valid/invalid gene, bad source enum, malformed disease).
- FR-2 -> state transition tests and checkpoint resume tests.
- FR-3 -> plan artifact generation tests and deterministic ordering tests.
- FR-4 -> parallel collection tests and per-source status correctness tests.
- FR-5 -> normalization mapping tests for each source payload shape.
- FR-6 -> verification rule tests (duplicates, missing provenance, mapping mismatch).
- FR-7 -> contradiction detection tests across curated conflicting fixtures.
- FR-8 -> graph node/edge integrity tests.
- FR-9 -> explanation grounding tests (no claim without evidence id).
- FR-10 -> review decision state transition tests.
- FR-11 -> memory read/write consistency tests.
- FR-12 -> dossier contract and backward compatibility tests.

### 13.3 Test Data and Fixtures
- Gold fixtures for EGFR, KRAS, TP53 across all four sources.
- Corrupted fixtures for parser and verification negative tests.
- Conflict fixture sets (strong-vs-weak evidence contradictions).

### 13.4 CI Quality Gates
- Lint + type + unit suite must pass.
- Contract tests for dossier schema versions.
- Minimum coverage threshold: 80% for `agents/` and `mcps/` critical paths.
- Nightly E2E smoke on real APIs.

### 13.5 Exit Criteria (Go/No-Go)
- All P0/P1 test suites green for 7 consecutive CI runs.
- No unresolved high-severity verification defects.
- Performance and reliability SLOs met in staging.
- Scientist review sign-off on at least 10 representative targets.

---

## 14. Acceptance Criteria

1. A run with all 4 sources produces a verified dossier and graph snapshot.
2. Partial source failure still yields valid output if minimum coverage threshold is met.
3. Conflicts are surfaced with severity and included in review queue.
4. Human approval/rejection changes final run status deterministically.
5. Every claim in final dossier maps to provenance metadata.
6. Phase-2 handoff payload validates against published contract.

---

## 15. Risks and Mitigations

- **Upstream API instability** -> retries, circuit breaker, cached fallbacks.
- **Schema drift across MCPs** -> contract tests + strict version pinning.
- **Low evidence consistency across sources** -> conflict analyzer + review policy.
- **LLM variability in explanation** -> deterministic fallback + grounding checks.
- **Operational complexity with external servers** -> managed lifecycle + health probes.

---

## 16. Operational Runbook Requirements

- Source health checks before run start.
- Run cancellation and resume support.
- Structured incident taxonomy for failed runs.
- Daily summary of source success rates and latency trends.

---

## 17. Open Questions

1. Evidence graph storage target: file artifact vs graph DB (Neo4j/other) for Phase-1?
2. Reviewer UX location: CLI prompts, lightweight web panel, or notebook workflow?
3. Coverage threshold policy: static global vs disease-area specific?
4. Should semantic memory be read-only in Phase-1 or allow curation writes?

---

## 18. Immediate Next Engineering Tasks

1. Add new schema models (`CollectionPlan`, `VerificationReport`, `ConflictRecord`, `EvidenceDossier`).
2. Refactor LangGraph with explicit planner/normalization/verification/conflict nodes.
3. Implement verification rule engine and contradiction detector fixtures.
4. Add dossier contract tests and state-machine integration tests.
5. Implement review decision persistence and run status transitions.
6. Publish Phase-2 handoff interface docs.

---

## Appendix A: Proposed LangGraph State Progression

`validate_input -> plan_collection -> collect_sources_parallel -> normalize_evidence -> verify_evidence -> analyze_conflicts -> build_evidence_graph -> generate_explanation -> human_review_gate -> emit_dossier`

## Appendix B: Minimum Dossier Fields

- `run_id`
- `query`
- `source_status`
- `verified_evidence`
- `verification_report`
- `conflicts`
- `graph_snapshot`
- `summary_markdown`
- `review_decision`
- `handoff_payload_phase2`
