# Drugagent Phase-1 Evidence Collector (Content Memory)

This repository implements a Phase-1 "Evidence Collector" multi-agent workflow for biomedical target evidence (gene-centric).

Primary user goal:
- Provide a reproducible, inspectable evidence dossier for a target (e.g. EGFR) by collecting and normalizing evidence from configured sources, running verification/conflict checks, and generating a long-form therapeutic dossier.

Core workflow stages (LangGraph):
- validate_input: validate request inputs and load episodic memory for similar past runs.
- plan_collection: select sources, generate query variants, and create per-source directives; persist a plan artifact.
- collect_sources_parallel: fetch evidence from requested sources (DepMap, literature, Open Targets, Pharos, plus optional external MCP servers).
- normalize_evidence: normalize raw items into a consistent EvidenceRecord shape and scoring space.
- verify_evidence: run deterministic verification rules and produce a VerificationReport.
- analyze_conflicts: detect cross-source conflicts (severity/rationale).
- build_evidence_graph: build a deterministic evidence graph snapshot (nodes/edges) for explainability and UI.
- generate_explanation: generate a long-form 9-section "Integrated Therapeutic Target Dossier" grounded strictly in the payload.
- supervisor_decide: choose whether to recollect, request human review, or emit dossier based on verification/conflicts/coverage and memory context.
- prepare_review_brief: create a concise review packet for a human reviewer.
- human_review_gate: enforce human-in-the-loop if configured (interrupts the run until a decision is supplied).
- emit_dossier: persist final dossier artifact and write episodic memory for future runs.

Memory layers:
- Episodic memory: stores per-run summaries/decisions and is queried early to inform planning/supervision.
- Semantic memory: maintains gene/disease aliases for query variants and consistency checks.
- Procedural memory: stores the stage sequence used in a run (for auditability).
- Working memory: stores per-stage snapshots of state+updates for debugging and UI traces.

Human-in-the-loop (HITL):
- The workflow can require manual approval/rejection (or request more evidence) before final emission.
- HITL behavior is configurable via environment variables so the CLI and future frontend can pause/resume runs.

Output contract:
- Persist plan/graph/dossier artifacts under `artifacts/` (and human-readable reports under `results/`).
- The long report must remain detailed prose (not overly truncated "strict noise removal").

Frontend/deployment direction:
- Expose run events (stage start/end, edges, agent reports/decisions) so a UI can render a Perplexity-style timeline of "which agent ran next and why".
- Provide API endpoints to start runs, stream events (SSE/WebSocket), submit review decisions, and fetch artifacts.

