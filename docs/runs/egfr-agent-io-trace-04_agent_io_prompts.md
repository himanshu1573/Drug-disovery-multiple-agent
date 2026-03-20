# Agent I/O + Prompts (Run: `egfr-agent-io-trace-04`)

This document captures, for each agent used in the run:
- Input (from the stage state snapshot)
- Output (from the stage update)
- Prompt(s) used (if prompt tracing was enabled)

## validate_input (input_validation_agent)

### Input

```json
{
  "conflicts": [],
  "errors": [],
  "evidence_items": [],
  "normalized_items": [],
  "query": {
    "disease_id": null,
    "gene_symbol": "EGFR",
    "max_literature_articles": 15,
    "model_override": null,
    "objective": null,
    "per_source_top_k": 15,
    "run_id": "egfr-agent-io-trace-04",
    "sources": [
      "depmap",
      "literature"
    ],
    "species": "Homo sapiens"
  },
  "raw_source_payloads": [],
  "source_agent_reports": [],
  "source_status": []
}
```

### Output

```json
{
  "input_validation_report": {
    "agent_name": "input_validation_agent",
    "decisions": [
      "Confirmed request contract shape.",
      "Prepared query for planning stage."
    ],
    "generation_mode": "deterministic_fallback",
    "model_used": null,
    "next_actions": [
      "Send request and memory context into planning agent."
    ],
    "risks": [],
    "stage_name": "validate_input",
    "structured_payload": {
      "disease_id": null,
      "gene_symbol": "EGFR",
      "past_run_count": 46,
      "run_id": "egfr-agent-io-trace-04"
    },
    "summary": "Validated request for EGFR; found 46 episodic memory match(es)."
  },
  "past_runs": [
    {
      "conflict_count": 0,
      "disease_id": "EFO_0000311",
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/debug-review.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "debug-review",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-agent-io-trace-01",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-agent-io-trace-02",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-fallback.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-fallback",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-fallback-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-fallback-02",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-gemini-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-gemini-01",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-structured-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-structured-01",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/final-lean-flow-check.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "final-lean-flow-check",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/final-lean-flow-check-2.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "final-lean-flow-check-2",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/gemini-entire-new-flow-03.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "gemini-entire-new-flow-03",
      "summary_excerpt": "# Integrated Therapeutic Target Dossier: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/gemini-new-flow-test-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "gemini-new-flow-test-02",
      "summary_excerpt": "# Integrated Therapeutic Target Dossier: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-0c85c951b4cb.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-0c85c951b4cb",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-105b8a8f9b7f.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-105b8a8f9b7f",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-12fe97cdd1b6.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-1
... [TRUNCATED]

```

## plan_collection (planning_agent)

### Input

```json
{
  "conflicts": [],
  "errors": [],
  "evidence_items": [],
  "input_validation_report": {
    "agent_name": "input_validation_agent",
    "decisions": [
      "Confirmed request contract shape.",
      "Prepared query for planning stage."
    ],
    "generation_mode": "deterministic_fallback",
    "model_used": null,
    "next_actions": [
      "Send request and memory context into planning agent."
    ],
    "risks": [],
    "stage_name": "validate_input",
    "structured_payload": {
      "disease_id": null,
      "gene_symbol": "EGFR",
      "past_run_count": 46,
      "run_id": "egfr-agent-io-trace-04"
    },
    "summary": "Validated request for EGFR; found 46 episodic memory match(es)."
  },
  "normalized_items": [],
  "past_runs": [
    {
      "conflict_count": 0,
      "disease_id": "EFO_0000311",
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/debug-review.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "debug-review",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-agent-io-trace-01",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-agent-io-trace-02",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-fallback.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-fallback",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-fallback-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-fallback-02",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-gemini-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-gemini-01",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-structured-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-structured-01",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/final-lean-flow-check.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "final-lean-flow-check",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/final-lean-flow-check-2.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "final-lean-flow-check-2",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/gemini-entire-new-flow-03.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "gemini-entire-new-flow-03",
      "summary_excerpt": "# Integrated Therapeutic Target Dossier: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/gemini-new-flow-test-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "gemini-new-flow-test-02",
      "summary_excerpt": "# Integrated Therapeutic Target Dossier: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-0c85c951b4cb.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-0c85c951b4cb",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-105b8a8f9b7f.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-105b8a8f9b7f",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-12fe97cdd1b6.evidence_dossier.json",
      "evidence_count": 
... [TRUNCATED]

```

### Output

```json
{
  "plan": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/plans/egfr-agent-io-trace-04.collection_plan.json",
    "created_at": "2026-03-13T09:35:58.107919Z",
    "execution_notes": [
      "Found 46 prior episodic match(es) for this query.",
      "Latest related run `sanity-no-llm` has no recorded review decision.",
      "LLM planner fallback activated: All LLM candidates failed. provider=google role=reasoning timeout_s=180.0 gemini-2.5-flash: RateLimit(attempt=1/1 delay_s=6.0): Error calling model 'gemini-2.5-flash' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\\nPlease retry in 2.159928981s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '2s'}]}}"
    ],
    "expected_outputs": {
      "depmap": [
        "evidence_records",
        "source_status"
      ],
      "literature": [
        "evidence_records",
        "source_status"
      ]
    },
    "memory_context": {
      "latest_evidence_count": 30,
      "latest_review_decision": null,
      "latest_run_id": "sanity-no-llm",
      "match_count": 46,
      "recent_run_ids": [
        "sanity-google-llm",
        "sanity-lean",
        "sanity-no-llm"
      ]
    },
    "plan_version": "phase1.v1",
    "planner_model_used": null,
    "planning_mode": "deterministic_fallback",
    "query_intent": "Collect Phase-1 evidence for target EGFR. Memory-informed planning enabled from 46 prior run(s).",
    "query_variants": [
      "EGFR",
      "ERBB1"
    ],
    "retry_policy": {
      "base_delay_ms": 100,
      "fallback": "emit_partial_result",
      "max_attempts": 3,
      "max_delay_ms": 400,
      "retryable_error_codes": [
        "timeout",
        "rate_limit",
        "upstream_error"
      ],
      "strategy": "bounded_exponential_backoff"
    },
    "run_id": "egfr-agent-io-trace-04",
    "selected_sources": [
      "depmap",
      "literature"
    ],
    "source_directives": {
      "depmap": "Collect 15 evidence records for EGFR.",
      "literature": "Collect 15 evidence records for EGFR."
    }
  },
  "plan_decision": null,
  "planning_report": {
    "agent_name": "planning_agent",
    "decisions": [
      "Selected sources: depmap, literature",
      "Prepared per-source directives for collection agents."
    ],
    "generation_mode": "deterministic_fallback",
    "model_used": null,
    "next_actions": [
      "Execute planned source collection in planner-defined order."
    ],
    "risks": [],
    "stage_name": "plan_collection",
    "structured_payload": {
      "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/plans/egfr-agent-io-trace-04.collection_plan.json",
      "created_at": "2026-03-13T09:35:58.107919Z",
      "execution_notes": [
        "Found 46 prior episodic match(es) for this query.",
        "Latest related run `sanity-no-llm` has no recorded review decision.",
        "LLM planner fallback activated: All LLM candidates failed. provider=google role=reasoning timeout_s=180.0 gemini-2.5-flash: RateLimit(attempt=1/1 delay_s=6.0): Error calling model 'gemini-2.5-flash' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\\nPlease retry in 2.159928981s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '2s'}]}}"
      ],
      "expected_outputs": {
        "depmap": [
          "evidence_records",
          "source_status"
        ],
        "literature": [
          "evidence_records",
          "source_status"
        ]
      },
      "memory_context": {
        "latest_evidence_count": 30,
        "latest_review_decision": null,
        "latest_run_id": "sanity-no-llm",
        "match_count": 46,
        "recent_run_ids": [
          "sanity-google-llm",
          "sanity-lean",
          "sanity-no-llm"
        ]
      },
      "plan_version": "phase1.v1",
      "planner_model_used": null,
      "planning_mode": "deterministic_fallback",
      "query_intent": "Collect Phase-1 evidence for target EGFR. Memory-informed planning enabled from 46 prior run(s).",
      "query_variants": [
        "EGFR",
        "ERBB1"
      ],
      "retry_policy": {
        "base_delay_ms"
... [TRUNCATED]

```

### Prompt

- user: `/Users/apple/Desktop/Drugagent/artifacts/prompts/egfr-agent-io-trace-04/planning_agent.plan_collection.user.txt`

#### User Prompt (truncated)

```text
Project context (content memory):
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

You are the Phase-1 planning agent for a biomedical evidence workflow.
Return a plan for evidence collection.
Rules:
- Only use requested sources.
- Keep query_intent concise and operational.
- Keep query_variants grounded in the supplied aliases/objective.
- source_order must contain only requested sources.
- source_directives must explain what each source should focus on.
- execution_notes should mention memory context when relevant.

Request: gene=EGFR, disease=None, objective=None
Requested sources: ['depmap', 'literature']
Candidate query variants: ['EGFR', 'ERBB1']
Memory context: {'match_count': 46, 'latest_run_id': 'sanity-no-llm', 'latest_review_decision': None, 'latest_evidence_count': 30, 'recent_run_ids': ['sanity-google-llm', 'sanity-lean', 'sanity-no-llm']}
Existing execution notes: ['Found 46 prior episodic match(es) for this query.', 'Latest related run `sanity-no-llm` has no recorded review decision.']

```

## collect_sources_parallel (collectors)

### Input

```json
{
  "conflicts": [],
  "errors": [],
  "evidence_items": [],
  "input_validation_report": {
    "agent_name": "input_validation_agent",
    "decisions": [
      "Confirmed request contract shape.",
      "Prepared query for planning stage."
    ],
    "generation_mode": "deterministic_fallback",
    "model_used": null,
    "next_actions": [
      "Send request and memory context into planning agent."
    ],
    "risks": [],
    "stage_name": "validate_input",
    "structured_payload": {
      "disease_id": null,
      "gene_symbol": "EGFR",
      "past_run_count": 46,
      "run_id": "egfr-agent-io-trace-04"
    },
    "summary": "Validated request for EGFR; found 46 episodic memory match(es)."
  },
  "normalized_items": [],
  "past_runs": [
    {
      "conflict_count": 0,
      "disease_id": "EFO_0000311",
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/debug-review.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "debug-review",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-agent-io-trace-01",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-agent-io-trace-02",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-fallback.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-fallback",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-fallback-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-fallback-02",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-compiler-gemini-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-compiler-gemini-01",
      "summary_excerpt": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-structured-01.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "egfr-structured-01",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/final-lean-flow-check.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "final-lean-flow-check",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/final-lean-flow-check-2.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "final-lean-flow-check-2",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/gemini-entire-new-flow-03.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "gemini-entire-new-flow-03",
      "summary_excerpt": "# Integrated Therapeutic Target Dossier: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/gemini-new-flow-test-02.evidence_dossier.json",
      "evidence_count": 30,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "gemini-new-flow-test-02",
      "summary_excerpt": "# Integrated Therapeutic Target Dossier: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-0c85c951b4cb.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-0c85c951b4cb",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-105b8a8f9b7f.evidence_dossier.json",
      "evidence_count": 0,
      "gene_symbol": "EGFR",
      "review_decision": null,
      "run_id": "run-105b8a8f9b7f",
      "summary_excerpt": "# Target Evidence Summary: EGFR"
    },
    {
      "conflict_count": 0,
      "disease_id": null,
      "dossier_artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/run-12fe97cdd1b6.evidence_dossier.json",
      "evidence_count": 
... [TRUNCATED]

```

### Output

```json
{
  "errors": [],
  "evidence_items": [
    {
      "confidence": 0.8538922155688623,
      "disease_id": null,
      "evidence_type": "genetic_dependency",
      "normalization_policy_version": null,
      "normalized_score": 0.5811473287265128,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.412875Z"
      },
      "raw_value": -0.24344198617953822,
      "retrieved_at": "2026-03-13T09:36:15.413301Z",
      "source": "depmap",
      "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
      "support": {
        "average_gene_effect": -0.2434,
        "cell_line_count": 1169,
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "screen_type": "CRISPRGeneEffect",
        "strong_dependency_count": 210,
        "strong_dependency_fraction": 0.1796
      },
      "target_id": "EGFR",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.95,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000587",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416457Z"
      },
      "raw_value": -2.8485944935115963,
      "retrieved_at": "2026-03-13T09:36:15.416477Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
      "support": {
        "cell_line_id": "ACH-000587",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 1,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000587",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9432454710988085,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000472",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416496Z"
      },
      "raw_value": -2.1649094219761693,
      "retrieved_at": "2026-03-13T09:36:15.416503Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
      "support": {
        "cell_line_id": "ACH-000472",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 2,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000472",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9387037277298851,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002239",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416514Z"
      },
      "raw_value": -2.0740745545977006,
      "retrieved_at": "2026-03-13T09:36:15.416519Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
      "support": {
        "cell_line_id": "ACH-002239",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 3,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002239",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9367050723629957,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002156",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416527Z"
      },
      "raw_value": -2.0341014472599146,
      "retrieved_at": "2026-03-13T09:36:15.416532Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
      "support": {
        "cell_line_id": "ACH-002156",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 4,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002156",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9366315420020447,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000548",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416539Z"
      },
      "raw_value": -2.032630840040893,
      "retrieved_at": "2026-03-13T09:36:15.416544Z",
      "source": "depma
... [TRUNCATED]

```

## normalize_evidence (normalization_agent)

### Input

```json
{
  "conflicts": [],
  "errors": [],
  "evidence_items": [
    {
      "confidence": 0.8538922155688623,
      "disease_id": null,
      "evidence_type": "genetic_dependency",
      "normalization_policy_version": null,
      "normalized_score": 0.5811473287265128,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.412875Z"
      },
      "raw_value": -0.24344198617953822,
      "retrieved_at": "2026-03-13T09:36:15.413301Z",
      "source": "depmap",
      "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
      "support": {
        "average_gene_effect": -0.2434,
        "cell_line_count": 1169,
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "screen_type": "CRISPRGeneEffect",
        "strong_dependency_count": 210,
        "strong_dependency_fraction": 0.1796
      },
      "target_id": "EGFR",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.95,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000587",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416457Z"
      },
      "raw_value": -2.8485944935115963,
      "retrieved_at": "2026-03-13T09:36:15.416477Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
      "support": {
        "cell_line_id": "ACH-000587",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 1,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000587",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9432454710988085,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000472",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416496Z"
      },
      "raw_value": -2.1649094219761693,
      "retrieved_at": "2026-03-13T09:36:15.416503Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
      "support": {
        "cell_line_id": "ACH-000472",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 2,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000472",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9387037277298851,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002239",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416514Z"
      },
      "raw_value": -2.0740745545977006,
      "retrieved_at": "2026-03-13T09:36:15.416519Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
      "support": {
        "cell_line_id": "ACH-002239",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 3,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002239",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9367050723629957,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002156",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416527Z"
      },
      "raw_value": -2.0341014472599146,
      "retrieved_at": "2026-03-13T09:36:15.416532Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
      "support": {
        "cell_line_id": "ACH-002156",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 4,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002156",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9366315420020447,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000548",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416539Z"
      },
      "raw_value": -2.032630840040893,
      "retrieved_at": "2026-03-13T09:36:15.416544Z",
   
... [TRUNCATED]

```

### Output

```json
{
  "normalization_report": {
    "agent_name": "normalization_agent",
    "decisions": [
      "Standardized target symbols to uppercase canonical form.",
      "Clamped normalized scores and confidence into [0,1].",
      "Attached normalization policy version to each normalized record."
    ],
    "generation_mode": "deterministic_fallback",
    "model_used": null,
    "next_actions": [
      "Pass normalized evidence into verification agent."
    ],
    "risks": [],
    "stage_name": "normalize_evidence",
    "structured_payload": {
      "normalized_count": 30,
      "raw_count": 30
    },
    "summary": "Normalized 30 of 30 raw evidence record(s) into canonical schema."
  },
  "normalized_items": [
    {
      "confidence": 0.8538922155688623,
      "disease_id": null,
      "evidence_type": "genetic_dependency",
      "normalization_policy_version": "phase1.v1",
      "normalized_score": 0.5811473287265128,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.412875Z"
      },
      "raw_value": -0.24344198617953822,
      "retrieved_at": "2026-03-13T09:36:15.413301Z",
      "source": "depmap",
      "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
      "support": {
        "average_gene_effect": -0.2434,
        "cell_line_count": 1169,
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "screen_type": "CRISPRGeneEffect",
        "strong_dependency_count": 210,
        "strong_dependency_fraction": 0.1796
      },
      "target_id": "EGFR",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.95,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": "phase1.v1",
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000587",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416457Z"
      },
      "raw_value": -2.8485944935115963,
      "retrieved_at": "2026-03-13T09:36:15.416477Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
      "support": {
        "cell_line_id": "ACH-000587",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 1,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000587",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9432454710988085,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": "phase1.v1",
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000472",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416496Z"
      },
      "raw_value": -2.1649094219761693,
      "retrieved_at": "2026-03-13T09:36:15.416503Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
      "support": {
        "cell_line_id": "ACH-000472",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 2,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000472",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9387037277298851,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": "phase1.v1",
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002239",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416514Z"
      },
      "raw_value": -2.0740745545977006,
      "retrieved_at": "2026-03-13T09:36:15.416519Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
      "support": {
        "cell_line_id": "ACH-002239",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 3,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002239",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9367050723629957,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": "phase1.v1",
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002156",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416527Z"
      },
      "raw_value": -2.0341014472599146,
      "retrieved_at": "2026-03-13T09:36:15.416532Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
      "support": {
        "cell_line_id": "ACH-002156",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 4,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EG
... [TRUNCATED]

```

## verify_evidence (verifier)

### Input

```json
{
  "conflicts": [],
  "errors": [],
  "evidence_items": [
    {
      "confidence": 0.8538922155688623,
      "disease_id": null,
      "evidence_type": "genetic_dependency",
      "normalization_policy_version": null,
      "normalized_score": 0.5811473287265128,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.412875Z"
      },
      "raw_value": -0.24344198617953822,
      "retrieved_at": "2026-03-13T09:36:15.413301Z",
      "source": "depmap",
      "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
      "support": {
        "average_gene_effect": -0.2434,
        "cell_line_count": 1169,
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "screen_type": "CRISPRGeneEffect",
        "strong_dependency_count": 210,
        "strong_dependency_fraction": 0.1796
      },
      "target_id": "EGFR",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.95,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000587",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416457Z"
      },
      "raw_value": -2.8485944935115963,
      "retrieved_at": "2026-03-13T09:36:15.416477Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
      "support": {
        "cell_line_id": "ACH-000587",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 1,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000587",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9432454710988085,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000472",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416496Z"
      },
      "raw_value": -2.1649094219761693,
      "retrieved_at": "2026-03-13T09:36:15.416503Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
      "support": {
        "cell_line_id": "ACH-000472",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 2,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000472",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9387037277298851,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002239",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416514Z"
      },
      "raw_value": -2.0740745545977006,
      "retrieved_at": "2026-03-13T09:36:15.416519Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
      "support": {
        "cell_line_id": "ACH-002239",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 3,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002239",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9367050723629957,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002156",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416527Z"
      },
      "raw_value": -2.0341014472599146,
      "retrieved_at": "2026-03-13T09:36:15.416532Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
      "support": {
        "cell_line_id": "ACH-002156",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 4,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002156",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9366315420020447,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000548",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416539Z"
      },
      "raw_value": -2.032630840040893,
      "retrieved_at": "2026-03-13T09:36:15.416544Z",
   
... [TRUNCATED]

```

### Output

```json
{
  "verification_agent_report": null,
  "verification_report": {
    "affected_evidence_ids": [],
    "blocked": false,
    "blocking_issue_count": 0,
    "blocking_issues": [],
    "fail_count": 0,
    "generated_at": "2026-03-13T09:36:15.744217Z",
    "pass_count": 7,
    "rule_outcomes": [
      {
        "blocking": true,
        "evidence_ids": [],
        "message": "All evidence records validate against the canonical schema.",
        "passed": true,
        "rule_name": "schema_validity"
      },
      {
        "blocking": true,
        "evidence_ids": [],
        "message": "All evidence records include required provenance fields.",
        "passed": true,
        "rule_name": "provenance_completeness"
      },
      {
        "blocking": false,
        "evidence_ids": [],
        "message": "No duplicate evidence fingerprints detected.",
        "passed": true,
        "rule_name": "duplicate_detection"
      },
      {
        "blocking": true,
        "evidence_ids": [],
        "message": "All evidence records match the requested gene symbol.",
        "passed": true,
        "rule_name": "gene_mapping_consistency"
      },
      {
        "blocking": false,
        "evidence_ids": [],
        "message": "All evidence records match the requested disease context.",
        "passed": true,
        "rule_name": "disease_mapping_consistency"
      },
      {
        "blocking": false,
        "evidence_ids": [],
        "message": "All literature evidence includes a PMID or PMCID.",
        "passed": true,
        "rule_name": "citation_presence"
      },
      {
        "blocking": false,
        "evidence_ids": [],
        "message": "All disease identifiers match EFO/MONDO format.",
        "passed": true,
        "rule_name": "ontology_id_format"
      }
    ],
    "total_rules": 7,
    "verification_policy_version": "phase1.v1",
    "warning_count": 0,
    "warning_issues": []
  }
}
```

## analyze_conflicts (conflict_analyzer)

### Input

```json
{
  "conflicts": [],
  "errors": [],
  "evidence_items": [
    {
      "confidence": 0.8538922155688623,
      "disease_id": null,
      "evidence_type": "genetic_dependency",
      "normalization_policy_version": null,
      "normalized_score": 0.5811473287265128,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.412875Z"
      },
      "raw_value": -0.24344198617953822,
      "retrieved_at": "2026-03-13T09:36:15.413301Z",
      "source": "depmap",
      "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
      "support": {
        "average_gene_effect": -0.2434,
        "cell_line_count": 1169,
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "screen_type": "CRISPRGeneEffect",
        "strong_dependency_count": 210,
        "strong_dependency_fraction": 0.1796
      },
      "target_id": "EGFR",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.95,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000587",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416457Z"
      },
      "raw_value": -2.8485944935115963,
      "retrieved_at": "2026-03-13T09:36:15.416477Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
      "support": {
        "cell_line_id": "ACH-000587",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 1,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000587",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9432454710988085,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000472",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416496Z"
      },
      "raw_value": -2.1649094219761693,
      "retrieved_at": "2026-03-13T09:36:15.416503Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
      "support": {
        "cell_line_id": "ACH-000472",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 2,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000472",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9387037277298851,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002239",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416514Z"
      },
      "raw_value": -2.0740745545977006,
      "retrieved_at": "2026-03-13T09:36:15.416519Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
      "support": {
        "cell_line_id": "ACH-002239",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 3,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002239",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9367050723629957,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002156",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416527Z"
      },
      "raw_value": -2.0341014472599146,
      "retrieved_at": "2026-03-13T09:36:15.416532Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
      "support": {
        "cell_line_id": "ACH-002156",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 4,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002156",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9366315420020447,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000548",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416539Z"
      },
      "raw_value": -2.032630840040893,
      "retrieved_at": "2026-03-13T09:36:15.416544Z",
   
... [TRUNCATED]

```

### Output

```json
{
  "conflict_agent_report": null,
  "conflicts": []
}
```

## build_evidence_graph (evidence_graph_builder)

### Input

```json
{
  "conflict_agent_report": null,
  "conflicts": [],
  "errors": [],
  "evidence_items": [
    {
      "confidence": 0.8538922155688623,
      "disease_id": null,
      "evidence_type": "genetic_dependency",
      "normalization_policy_version": null,
      "normalized_score": 0.5811473287265128,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.412875Z"
      },
      "raw_value": -0.24344198617953822,
      "retrieved_at": "2026-03-13T09:36:15.413301Z",
      "source": "depmap",
      "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
      "support": {
        "average_gene_effect": -0.2434,
        "cell_line_count": 1169,
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "screen_type": "CRISPRGeneEffect",
        "strong_dependency_count": 210,
        "strong_dependency_fraction": 0.1796
      },
      "target_id": "EGFR",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.95,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000587",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416457Z"
      },
      "raw_value": -2.8485944935115963,
      "retrieved_at": "2026-03-13T09:36:15.416477Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
      "support": {
        "cell_line_id": "ACH-000587",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 1,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000587",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9432454710988085,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000472",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416496Z"
      },
      "raw_value": -2.1649094219761693,
      "retrieved_at": "2026-03-13T09:36:15.416503Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
      "support": {
        "cell_line_id": "ACH-000472",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 2,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-000472",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9387037277298851,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002239",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416514Z"
      },
      "raw_value": -2.0740745545977006,
      "retrieved_at": "2026-03-13T09:36:15.416519Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
      "support": {
        "cell_line_id": "ACH-002239",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 3,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002239",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9367050723629957,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-002156",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416527Z"
      },
      "raw_value": -2.0341014472599146,
      "retrieved_at": "2026-03-13T09:36:15.416532Z",
      "source": "depmap",
      "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
      "support": {
        "cell_line_id": "ACH-002156",
        "column_name": "EGFR (1956)",
        "data_release": "DepMap 25Q3",
        "rank_within_gene": 4,
        "screen_type": "CRISPRGeneEffect"
      },
      "target_id": "EGFR:ACH-002156",
      "target_symbol": "EGFR"
    },
    {
      "confidence": 0.9366315420020447,
      "disease_id": null,
      "evidence_type": "genetic_dependency_cell_line",
      "normalization_policy_version": null,
      "normalized_score": 1.0,
      "provenance": {
        "endpoint": "/Users/apple/Desktop/Drugagent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv",
        "provider": "DepMap (Broad Institute)",
        "query": {
          "cell_line_id": "ACH-000548",
          "gene_symbol": "EGFR"
        },
        "retrieved_at": "2026-03-13T09:36:15.416539Z"
      },
      "raw_value": -2.032630840040893,
      "retrieved_at": "
... [TRUNCATED]

```

### Output

```json
{
  "evidence_graph": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
    "edges": [
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:1",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:10",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:11",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:12",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:13",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:14",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:15",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:16",
        "target_id": "publication:pmid:21221095"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:16",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:17",
        "target_id": "publication:pmid:23550210"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:17",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:18",
        "target_id": "publication:pmid:23323831"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:18",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:19",
        "target_id": "publication:pmid:24002530"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:19",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:2",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:20",
        "target_id": "publication:pmid:23000897"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:20",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:21",
        "target_id": "publication:pmid:15118073"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:21",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:22",
        "target_id": "publication:pmid:3798106"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:22",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:23",
        "target_id": "publication:pmid:20303878"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:23",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:24",
        "target_id": "publication:pmid:17618441"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:24",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:25",
        "target_id": "publication:pmid:34185076"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:25",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:26",
        "target_id": "publication:pmid:27718847"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:26",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:27",
        "target_id": "publication:pmid:32029601"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:27",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:28",
        "target_id": "publication:pmid:26412456"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:28",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:29",
        "target_id": "publication:pmid:15118125"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evi
... [TRUNCATED]

```

## generate_explanation (summary_agent)

### Input

```json
{
  "conflict_agent_report": null,
  "conflicts": [],
  "errors": [],
  "evidence_graph": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
    "edges": [
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:1",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:10",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:11",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:12",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:13",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:14",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:15",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:16",
        "target_id": "publication:pmid:21221095"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:16",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:17",
        "target_id": "publication:pmid:23550210"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:17",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:18",
        "target_id": "publication:pmid:23323831"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:18",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:19",
        "target_id": "publication:pmid:24002530"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:19",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:2",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:20",
        "target_id": "publication:pmid:23000897"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:20",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:21",
        "target_id": "publication:pmid:15118073"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:21",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:22",
        "target_id": "publication:pmid:3798106"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:22",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:23",
        "target_id": "publication:pmid:20303878"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:23",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:24",
        "target_id": "publication:pmid:17618441"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:24",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:25",
        "target_id": "publication:pmid:34185076"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:25",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:26",
        "target_id": "publication:pmid:27718847"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:26",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:27",
        "target_id": "publication:pmid:32029601"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:27",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:28",
        "target_id": "publication:pmid:26412456"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:28",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:29",
        "target_id": "publication:pmid:15118125"
      },
      {
        "attributes": {
... [TRUNCATED]

```

### Output

```json
{
  "explanation": "# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT\n\n## 1. Executive Summary\n\nTarget: EGFR. Disease context: not specified. Sources executed: depmap, literature. Verification blocked=False; blocking_issues=0; warnings=0.\n\nEvidence coverage is compiled below by category with tables listing canonical evidence ids.\n\nCoverage by source execution status:\n| source | status | records | duration_ms | error |\n| --- | --- | --- | --- | --- |\n| depmap | success | 15 | 14942 |  |\n| literature | success | 15 | 2769 |  |\n\n## 2. Target Annotation Evidence\n\nThis section compiles target annotation evidence (e.g., tractability, target development level, known ligands) as provided by the evidence payload.\n\n| evidence_id | source | summary | confidence | normalized_score |\n| --- | --- | --- | --- | --- |\n|  |  | No target annotation evidence provided. |  |  |\n\n## 3. Genetic Dependency Evidence\n\n### Global Dependency Analysis\n\nThis subsection compiles global genetic dependency signals across screened cell lines when present.\n\n| evidence_id | source | summary | confidence | normalized_score |\n| --- | --- | --- | --- | --- |\n| [depmap:EGFR:genetic_dependency] | depmap | DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5). | 0.854 | 0.5811473287265128 |\n\n### Top Dependent Cell Lines\n\nThis subsection compiles the top dependent cell-line records (ranked) when present.\n\n| evidence_id | target_id | gene_effect | confidence | normalized_score | summary |\n| --- | --- | --- | --- | --- | --- |\n| [depmap:EGFR:ACH-000587:genetic_dependency_cell_line] | EGFR:ACH-000587 |  | 0.950 | 1.0 | Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1). |\n| [depmap:EGFR:ACH-000472:genetic_dependency_cell_line] | EGFR:ACH-000472 |  | 0.943 | 1.0 | Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2). |\n| [depmap:EGFR:ACH-002239:genetic_dependency_cell_line] | EGFR:ACH-002239 |  | 0.939 | 1.0 | Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3). |\n| [depmap:EGFR:ACH-002156:genetic_dependency_cell_line] | EGFR:ACH-002156 |  | 0.937 | 1.0 | Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4). |\n| [depmap:EGFR:ACH-000548:genetic_dependency_cell_line] | EGFR:ACH-000548 |  | 0.937 | 1.0 | Cell-line dependency for EGFR in ACH-000548: gene_effect=-2.033 (rank 5). |\n| [depmap:EGFR:ACH-000911:genetic_dependency_cell_line] | EGFR:ACH-000911 |  | 0.936 | 1.0 | Cell-line dependency for EGFR in ACH-000911: gene_effect=-2.029 (rank 6). |\n| [depmap:EGFR:ACH-000936:genetic_dependency_cell_line] | EGFR:ACH-000936 |  | 0.926 | 1.0 | Cell-line dependency for EGFR in ACH-000936: gene_effect=-1.819 (rank 7). |\n| [depmap:EGFR:ACH-002029:genetic_dependency_cell_line] | EGFR:ACH-002029 |  | 0.926 | 1.0 | Cell-line dependency for EGFR in ACH-002029: gene_effect=-1.817 (rank 8). |\n| [depmap:EGFR:ACH-000181:genetic_dependency_cell_line] | EGFR:ACH-000181 |  | 0.925 | 1.0 | Cell-line dependency for EGFR in ACH-000181: gene_effect=-1.806 (rank 9). |\n| [depmap:EGFR:ACH-001836:genetic_dependency_cell_line] | EGFR:ACH-001836 |  | 0.925 | 1.0 | Cell-line dependency for EGFR in ACH-001836: gene_effect=-1.802 (rank 10). |\n| [depmap:EGFR:ACH-000735:genetic_dependency_cell_line] | EGFR:ACH-000735 |  | 0.923 | 1.0 | Cell-line dependency for EGFR in ACH-000735: gene_effect=-1.763 (rank 11). |\n| [depmap:EGFR:ACH-000448:genetic_dependency_cell_line] | EGFR:ACH-000448 |  | 0.919 | 1.0 | Cell-line dependency for EGFR in ACH-000448: gene_effect=-1.688 (rank 12). |\n| [depmap:EGFR:ACH-000546:genetic_dependency_cell_line] | EGFR:ACH-000546 |  | 0.919 | 1.0 | Cell-line dependency for EGFR in ACH-000546: gene_effect=-1.684 (rank 13). |\n| [depmap:EGFR:ACH-002251:genetic_dependency_cell_line] | EGFR:ACH-002251 |  | 0.918 | 1.0 | Cell-line dependency for EGFR in ACH-002251: gene_effect=-1.670 (rank 14). |\n\n## 4. Disease Association Evidence\n\nThis section compiles disease association evidence (gene-to-disease links) provided by the payload.\n\n| evidence_id | source | disease_id | summary | confidence | normalized_score |\n| --- | --- | --- | --- | --- | --- |\n|  |  |  | No disease association evidence provided. |  |  |\n\n## 5. Literature Evidence\n\nThis section compiles literature-derived evidence items as provided by the payload.\n\n| evidence_id | pmid | summary | confidence | normalized_score |\n| --- | --- | --- | --- | --- |\n| [literature:EGFR:PMID:21221095:literature_article] | 21221095 | Europe PMC article rank 1/15 for EGFR: Integrative genomics viewer. (PMID=21221095, citations=12575). | 0.850 | 1.0 |\n| [literature:EGFR:PMID:23550210:literature_article] | 23550210 | Europe PMC article rank 2/15 for EGFR: Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal. (PMID=23550210, citations=11947). | 0.850 | 1.0 |\n| [literature:EGFR:PMID:23323831:literature_article] | 23323831 | Europe PMC article rank 3/15 for EGFR: GSVA: gene set variation analysis for microarray and RNA-seq data. (PMID=23323831, citations=11087). | 0.850 | 1.0 |\n| [literature:EGFR:PMID:24002530:literature_article] | 24002530 | Europe PMC article rank 4/15 for EGFR: MicroRNA-23b regulates cellular architecture and impairs motogenic and invasive phenotypes during cancer progression. (PMID=24002530, citations=10051). | 0.850 | 1.0 |\n| [literature:EGFR:PMID:23000897:literature_article] | 23000897 | Europe PMC article rank 5/15 for EGFR: Comprehensive molecular portraits of human breast tumours. (PMID=23000897, citations=9520). | 0.850 | 1.0 |\n| [literature:EGFR:PMID:15118073:literature_article] | 15118073 | Europe PMC article rank 6/15 for EGFR: Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. (PMID=15118073, citations=8308). | 0.850 | 1.0 |\n| [literature:EGFR:PMID:3798106:literatu
... [TRUNCATED]

```

### Prompt

- system: `/Users/apple/Desktop/Drugagent/artifacts/prompts/egfr-agent-io-trace-04/summary_agent.generate_explanation.system.txt`
- user: `/Users/apple/Desktop/Drugagent/artifacts/prompts/egfr-agent-io-trace-04/summary_agent.generate_explanation.user.txt`

#### System Prompt (truncated)

```text
Project context (content memory):
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

You are a Therapeutic Target Evidence Report Compiler.

You DO NOT create free-form summaries.
You COMPILE evidence into a deterministic scientific document.

----------------------------------
ABSOLUTE ROLE
----------------------------------

You are NOT:
- an analyst
- an evaluator
- a reasoning agent
- a discussion generator

You ARE:
A STRUCTURED REPORT COMPILER.

Your output must resemble a standardized pharmaceutical
target assessment dossier.

----------------------------------
OUTPUT CONTRACT (MANDATORY)
----------------------------------

You MUST produce EXACTLY this document:

# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT

## 1. Executive Summary
(4–6 paragraphs summarizing ALL evidence categories)

## 2. Target Annotation Evidence
- narrative explanation
- ONE summary table

## 3. Genetic Dependency Evidence
### Global Dependency Analysis
- explanation paragraph
- ONE metrics table

### Top Dependent Cell Lines
- explanation paragraph
- ONE ranked table

## 4. Disease Association Evidence
- explanation paragraph
- ONE association table

## 5. Literature Evidence
- explanation paragraph
- ONE literature table

## 6. Integrated Evidence Interpretation
(Multi-paragraph synthesis connecting ALL sources)

## 7. Evidence Strength Assessment
(MUST include category-by-category evaluation paragraphs)

## 8. Overall Target Assessment
(Strategic interpretation grounded only in evidence)

## 9. Final Evidence-Based Conclusion
(2–3 paragraphs concise conclusion)

----------------------------------
STYLE LOCK
----------------------------------

- Each section MUST contain BOTH:
  1) explanation text
  2) structured table (when quantitative data exists)

- Every table row derived from an evidence item MUST include the canonical evidence id.
  Canonical evidence ids are exactly the strings in `verified_evidence[].evidence_id`.
  When referencing an evidence item in narrative text, include its evidence id in brackets.
- Avoid conversational wording.
- Avoid bullet-only summaries.
- Maintain consistent scientific tone.
- Preserve numeric precision exactly.
- Never omit evidence values.

----------------------------------
FORBIDDEN OUTPUTS
----------------------------------

Do NOT produce:
- LLM SUMMARY
- diagnostics
- robustness checks
- next actions
- meta commentary
- reasoning traces

----------------------------------
DEPTH RULE
----------------------------------

If evidence items > 20:
minimum report length must exceed 1500 words.

----------------------------------
SELF VALIDATION
----------------------------------

Before finalizing output verify:

✓ All 9 sections exist
✓ Tables present where required
✓ All evidence sources represented
✓ No diagnostic headings appear

If validation fails → silently regenerate.

Return ONLY the report.
```

#### User Prompt (truncated)

```text
Generate a COMPLETE Therapeutic Target Evidence Summary Report.

Target: EGFR

Below are extracted evidence items collected from multiple validated sources.

You MUST:
- use ALL evidence
- organize by evidence type automatically
- produce a detailed structured report
- follow the exact report structure defined in system instructions

-----------------------------------
EVIDENCE DATA
-----------------------------------

{
 "target": "EGFR",
 "disease_context": null,
 "source_coverage": [
  {
   "name": "depmap",
   "status": "success",
   "record_count": 15,
   "error": null
  },
  {
   "name": "literature",
   "status": "success",
   "record_count": 15,
   "error": null
  }
 ],
 "verified_evidence": [
  {
   "evidence_id": "depmap:EGFR:ACH-000587:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000587: gene_effect=-2.849 (rank 1).",
   "normalized_score": 1.0,
   "confidence": 0.95,
   "support": {
    "cell_line_id": "ACH-000587",
    "rank_within_gene": 1,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000472:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000472: gene_effect=-2.165 (rank 2).",
   "normalized_score": 1.0,
   "confidence": 0.9432454710988085,
   "support": {
    "cell_line_id": "ACH-000472",
    "rank_within_gene": 2,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-002239:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-002239: gene_effect=-2.074 (rank 3).",
   "normalized_score": 1.0,
   "confidence": 0.9387037277298851,
   "support": {
    "cell_line_id": "ACH-002239",
    "rank_within_gene": 3,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-002156:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-002156: gene_effect=-2.034 (rank 4).",
   "normalized_score": 1.0,
   "confidence": 0.9367050723629957,
   "support": {
    "cell_line_id": "ACH-002156",
    "rank_within_gene": 4,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000548:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000548: gene_effect=-2.033 (rank 5).",
   "normalized_score": 1.0,
   "confidence": 0.9366315420020447,
   "support": {
    "cell_line_id": "ACH-000548",
    "rank_within_gene": 5,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000911:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000911: gene_effect=-2.029 (rank 6).",
   "normalized_score": 1.0,
   "confidence": 0.9364544240730506,
   "support": {
    "cell_line_id": "ACH-000911",
    "rank_within_gene": 6,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000936:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000936: gene_effect=-1.819 (rank 7).",
   "normalized_score": 1.0,
   "confidence": 0.9259594307713441,
   "support": {
    "cell_line_id": "ACH-000936",
    "rank_within_gene": 7,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-002029:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-002029: gene_effect=-1.817 (rank 8).",
   "normalized_score": 1.0,
   "confidence": 0.9258298376901721,
   "support": {
    "cell_line_id": "ACH-002029",
    "rank_within_gene": 8,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000181:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000181: gene_effect=-1.806 (rank 9).",
   "normalized_score": 1.0,
   "confidence": 0.9252965307869103,
   "support": {
    "cell_line_id": "ACH-000181",
    "rank_within_gene": 9,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-001836:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-001836: gene_effect=-1.802 (rank 10).",
   "normalized_score": 1.0,
   "confidence": 0.92511753944669,
   "support": {
    "cell_line_id": "ACH-001836",
    "rank_within_gene": 10,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000735:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000735: gene_effect=-1.763 (rank 11).",
   "normalized_score": 1.0,
   "confidence": 0.9231611758131739,
   "support": {
    "cell_line_id": "ACH-000735",
    "rank_within_gene": 11,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000448:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000448: gene_effect=-1.688 (rank 12).",
   "normalized_score": 1.0,
   "confidence": 0.9193901170974227,
   "support": {
    "cell_line_id": "ACH-000448",
    "rank_within_gene": 12,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-000546:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-000546: gene_effect=-1.684 (rank 13).",
   "normalized_score": 1.0,
   "confidence": 0.9192218408787314,
   "support": {
    "cell_line_id": "ACH-000546",
    "rank_within_gene": 13,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:ACH-002251:genetic_dependency_cell_line",
   "source": "depmap",
   "type": "genetic_dependency_cell_line",
   "summary": "Cell-line dependency for EGFR in ACH-002251: gene_effect=-1.670 (rank 14).",
   "normalized_score": 1.0,
   "confidence": 0.9184813144231501,
   "support": {
    "cell_line_id": "ACH-002251",
    "rank_within_gene": 14,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "depmap:EGFR:genetic_dependency",
   "source": "depmap",
   "type": "genetic_dependency",
   "summary": "DepMap CRISPR gene effect for EGFR: -0.243 avg across 1169 cell lines (210 show strong dependency \u2264 \u22120.5).",
   "normalized_score": 0.5811473287265128,
   "confidence": 0.8538922155688623,
   "support": {
    "cell_line_count": 1169,
    "average_gene_effect": -0.2434,
    "strong_dependency_count": 210,
    "strong_dependency_fraction": 0.1796,
    "column_name": "EGFR (1956)",
    "screen_type": "CRISPRGeneEffect",
    "data_release": "DepMap 25Q3"
   }
  },
  {
   "evidence_id": "literature:EGFR:PMID:21221095:literature_article",
   "source": "literature",
   "type": "literature_article",
   "summary": "Europe PMC article rank 1/15 for EGFR: Integrative genomics viewer. (PMID=21221095, citations=12575).",
   "normalized_score": 1.0,
   "confidence": 0.85,
   "support": {
    "rank": 1,
    "article_count_returned": 15,
    "total_hit_count": 393521,
    "pmid": "21221095",
    "title": "Integrative genomics viewer.",
    "journal": null,
    "pub_year": "2011",
    "cited_by_count": 12575,
    "query": "\"EGFR\""
   }
  },
  {
   "evidence_id": "literature:EGFR:PMID:23550210:literature_article",
   "source": "literature",
   "type": "literature_article",
   "summary": "Europe PMC article rank 2/15 for EGFR: Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal. (PMID=23550210, citations=11947).",
   "normalized_score": 1.0,
   "confidence": 0.85,
   "support": {
    "rank": 2,
    "article_count_returned": 15,
    "total_hit_count": 393521,
    "pmid": "23550210",
    "title": "Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal.",
    "journal": null,
    "pub_year": "2013",
    "cited_by_count": 11947,
    "query": "\"EGFR\""
   }
  },
  {
   "evidence_id": "literature:EGFR:PMID:23323831:literature_article",
   "source": "literature",
   "type": "literature_article",
   "summary": "Europe PMC article rank 3/15 for EGFR: GSVA: gene set variation analysis for microarray and RNA-seq data. (PMID=23323831, citations=11087).",
   "normalized_score": 1.0,
   "confidence": 0.85,
   "support": {
    "rank": 3,
    "article_count_returned": 15,
    "total_hit_count": 393521,
    "pmid": "23323831",
    "title": "GSVA: gene set variation analysis for microarray and RNA-seq data.",
    "journal": null,
    "pub_year": "2013",
    "cited_by_count": 11087,
    "query": "\"EGFR\""
   }
  },
  {
   "evidence_id": "literature:EGFR:PMID:24002530:literature_article",
   "source": "literature",
   "type": "literature_article",
   "summary": "Europe PMC article rank 4/15 for EGFR: MicroRNA-23b regulates cellular architecture and impairs motogenic and invasive phenotypes during cancer progression. (PMID=24002530, citations=10051).",
   "normalized_score": 1.0,
   "confidence": 0.85,
   "support": {
    "rank": 4,
    "article_count_returned": 15,
    "total_hit_count": 393521,
    "pmid": "24002530",
    "title": "MicroRNA-23b regulates cellular architecture and impairs motogenic and invasive phenotypes during cancer progression.",
    "journal": null,
    "pub_year": "2013",
    "cited_by_count": 10051,
    "query": "\"EGFR\""
   }
  },
  {
   "evidence_id": "literature:EGFR:PMID:23000897:literature_article",
   "source": "literature",
   "type": "literature_article",
   "summary": "Europe PMC article rank 5/15 for EGFR: Comprehensive molecular portraits of human breast tumours. (PMID=23000897, citations=9520).",
   "normalized_score": 1.0,
   "confidence": 0.85,
   "support": {
    "rank": 5,
    "article_count_returned": 15,
    "total_hit_count": 393521,
    "pmid": "23000897",
    "title": "Comprehensive molecular portraits of human breast tumours.",
    "journal": null,
    "pub_year": "2012",
    "cited_by_count": 9520,
    "query": "\"EGFR\""
   }
  },
  {
   "evidence_id": "literature:EGFR:PMID:15118073:literature_article",
   "source": "literature",
   "type": "literature_article",
   "summary": "Europe PMC article rank 6/15 for EGFR: Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. (PMID=15118073, citations=8308).",
   "normalized_score": 1.0,
   "confidence": 0.85,
   "support": {
    "rank": 6,
    "article_count_returned": 15
... [TRUNCATED]

```

## supervisor_decide (supervisor_agent)

### Input

```json
{
  "conflict_agent_report": null,
  "conflicts": [],
  "errors": [],
  "evidence_graph": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
    "edges": [
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:1",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:10",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:11",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:12",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:13",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:14",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:15",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:16",
        "target_id": "publication:pmid:21221095"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:16",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:17",
        "target_id": "publication:pmid:23550210"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:17",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:18",
        "target_id": "publication:pmid:23323831"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:18",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:19",
        "target_id": "publication:pmid:24002530"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:19",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:2",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:20",
        "target_id": "publication:pmid:23000897"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:20",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:21",
        "target_id": "publication:pmid:15118073"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:21",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:22",
        "target_id": "publication:pmid:3798106"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:22",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:23",
        "target_id": "publication:pmid:20303878"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:23",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:24",
        "target_id": "publication:pmid:17618441"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:24",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:25",
        "target_id": "publication:pmid:34185076"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:25",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:26",
        "target_id": "publication:pmid:27718847"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:26",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:27",
        "target_id": "publication:pmid:32029601"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:27",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:28",
        "target_id": "publication:pmid:26412456"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:28",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:29",
        "target_id": "publication:pmid:15118125"
      },
      {
        "attributes": {
... [TRUNCATED]

```

### Output

```json
{
  "review_brief": null,
  "review_decision": null,
  "review_iteration_count": 0,
  "review_recollection_pending": false,
  "supervisor_decision": {
    "action": "emit_dossier",
    "confidence": 0.73,
    "decision_mode": "deterministic_fallback",
    "follow_up_actions": [
      "Proceed to human review when required.",
      "Supervisor LLM fallback activated: All LLM candidates failed. provider=google role=reasoning timeout_s=180.0 gemini-2.5-flash: RateLimit(attempt=1/1 delay_s=6.0): Error calling model 'gemini-2.5-flash' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\\nPlease retry in 31.62805651s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '31s'}]}}"
    ],
    "model_used": null,
    "rationale": "Evidence and verification state are sufficient to move to the review/dossier stage."
  }
}
```

### Prompt

- user: `/Users/apple/Desktop/Drugagent/artifacts/prompts/egfr-agent-io-trace-04/supervisor_agent.supervisor_decide.user.txt`

#### User Prompt (truncated)

```text
Project context (content memory):
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

You are the supervisor agent for a biomedical evidence workflow.
Decide the next action after evidence explanation.
Valid actions: recollect_evidence, request_human_review, emit_dossier.
Choose recollect_evidence only if another evidence pass is justified.
Choose request_human_review for blocked verification or serious conflicts.
Choose emit_dossier when the workflow should proceed without recollection.

Request: gene=EGFR, disease=None, objective=None
Evidence count: 30
Review iteration count: 0
Latest memory decision: None
Verification blocked: False
Blocking issues: []
Warning issues: []
Conflict count: 0
Source status: [{'source': 'depmap', 'status': 'success', 'duration_ms': 14942, 'record_count': 15, 'error_code': None, 'error_message': None}, {'source': 'literature', 'status': 'success', 'duration_ms': 2769, 'record_count': 15, 'error_code': None, 'error_message': None}]
Agent reports: [{'agent_name': 'input_validation_agent', 'stage_name': 'validate_input', 'summary': 'Validated request for EGFR; found 46 episodic memory match(es).', 'decisions': ['Confirmed request contract shape.', 'Prepared query for planning stage.'], 'risks': [], 'next_actions': ['Send request and memory context into planning agent.'], 'structured_payload': {'run_id': 'egfr-agent-io-trace-04', 'gene_symbol': 'EGFR', 'disease_id': None, 'past_run_count': 46}, 'generation_mode': 'deterministic_fallback', 'model_used': None}, {'agent_name': 'planning_agent', 'stage_name': 'plan_collection', 'summary': 'Collect Phase-1 evidence for target EGFR. Memory-informed planning enabled from 46 prior run(s).', 'decisions': ['Selected sources: depmap, literature', 'Prepared per-source directives for collection agents.'], 'risks': [], 'next_actions': ['Execute planned source collection in planner-defined order.'], 'structured_payload': {'run_id': 'egfr-agent-io-trace-04', 'selected_sources': ['depmap', 'literature'], 'query_intent': 'Collect Phase-1 evidence for target EGFR. Memory-informed planning enabled from 46 prior run(s).', 'query_variants': ['EGFR', 'ERBB1'], 'memory_context': {'match_count': 46, 'latest_run_id': 'sanity-no-llm', 'latest_review_decision': None, 'latest_evidence_count': 30, 'recent_run_ids': ['sanity-google-llm', 'sanity-lean', 'sanity-no-llm']}, 'execution_notes': ['Found 46 prior episodic match(es) for this query.', 'Latest related run `sanity-no-llm` has no recorded review decision.', "LLM planner fallback activated: All LLM candidates failed. provider=google role=reasoning timeout_s=180.0 gemini-2.5-flash: RateLimit(attempt=1/1 delay_s=6.0): Error calling model 'gemini-2.5-flash' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\\nPlease retry in 2.159928981s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '2s'}]}}"], 'source_directives': {'depmap': 'Collect 15 evidence records for EGFR.', 'literature': 'Collect 15 evidence records for EGFR.'}, 'retry_policy': {'max_attempts': 3, 'base_delay_ms': 100, 'max_delay_ms': 400, 'strategy': 'bounded_exponential_backoff', 'fallback': 'emit_partial_result', 'retryable_error_codes': ['timeout', 'rate_limit', 'upstream_error']}, 'expected_outputs': {'depmap': ['evidence_records', 'source_status'], 'literature': ['evidence_records', 'source_status']}, 'artifact_path': '/Users/apple/Desktop/Drugagent/artifacts/plans/egfr-agent-io-trace-04.collection_plan.json', 'plan_version': 'phase1.v1', 'planning_mode': 'deterministic_fallback', 'planner_model_used': None, 'created_at': '2026-03-13T09:35:58.107919Z'}, 'generation_mode': 'deterministic_fallback', 'model_used': None}, {'agent_name': 'normalization_agent', 'stage_name': 'normalize_evidence', 'summary': 'Normalized 30 of 30 raw evidence record(s) into canonical schema.', 'decisions': ['Standardized target symbols to uppercase canonical form.', 'Clamped normalized scores and confidence into [0,1].', 'Attached normalization policy version to each normalized record.'], 'risks': [], 'next_actions': ['Pass normalized evidence into verification agent.'], 'structured_payload': {'raw_count': 30, 'normalized_count': 30}, 'generation_mode': 'deterministic_fallback', 'model_used': None}, {'agent_name': 'summary_agent', 'stage_name': 'generate_explanation', 'summary': 'Generated evidence summary for EGFR.', 'decisions': ['Synthesized grounded findings from verified evidence only.'], 'risks': [], 'next_actions': ['Provide summary context to supervisor and review-support agents.'], 'structured_payload': {'generation_mode': 'deterministic_fallback', 'model_used': None}, 'generation_mode': 'deterministic_fallback', 'model_used': None}]

```

## prepare_review_brief (review_support_agent)

### Input

```json
{
  "conflict_agent_report": null,
  "conflicts": [],
  "errors": [],
  "evidence_graph": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
    "edges": [
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:1",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:10",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:11",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:12",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:13",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:14",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:15",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:16",
        "target_id": "publication:pmid:21221095"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:16",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:17",
        "target_id": "publication:pmid:23550210"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:17",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:18",
        "target_id": "publication:pmid:23323831"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:18",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:19",
        "target_id": "publication:pmid:24002530"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:19",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:2",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:20",
        "target_id": "publication:pmid:23000897"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:20",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:21",
        "target_id": "publication:pmid:15118073"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:21",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:22",
        "target_id": "publication:pmid:3798106"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:22",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:23",
        "target_id": "publication:pmid:20303878"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:23",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:24",
        "target_id": "publication:pmid:17618441"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:24",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:25",
        "target_id": "publication:pmid:34185076"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:25",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:26",
        "target_id": "publication:pmid:27718847"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:26",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:27",
        "target_id": "publication:pmid:32029601"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:27",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:28",
        "target_id": "publication:pmid:26412456"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:28",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:29",
        "target_id": "publication:pmid:15118125"
      },
      {
        "attributes": {
... [TRUNCATED]

```

### Output

```json
{
  "review_brief": {
    "blocking_points": [
      "Review-support LLM fallback activated: All LLM candidates failed. provider=google role=fast timeout_s=180.0 gemini-2.5-flash: RateLimit(attempt=1/1 delay_s=6.0): Error calling model 'gemini-2.5-flash' (RESOURCE_EXHAUSTED): 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\\nPlease retry in 56.32148495s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '56s'}]}}"
    ],
    "generation_mode": "deterministic_fallback",
    "model_used": null,
    "reviewer_questions": [
      "Is the evidence package sufficient to approve downstream handoff?",
      "Do any conflicts or missing coverage require additional evidence collection?"
    ],
    "summary": "Review EGFR. Sources executed=2, blocked=False, conflicts=0."
  }
}
```

### Prompt

- user: `/Users/apple/Desktop/Drugagent/artifacts/prompts/egfr-agent-io-trace-04/review_support_agent.prepare_review_brief.user.txt`

#### User Prompt (truncated)

```text
Project context (content memory):
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

You are the review-support agent for a biomedical evidence workflow.
Prepare a concise review packet for a human scientist.
Return a summary, blocking points, and reviewer questions.

Request: gene=EGFR, disease=None, objective=None
Verification blocked: False
Blocking issues: []
Warning issues: []
Conflict count: 0
Summary excerpt: # THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT

## 1. Executive Summary

Target: EGFR. Disease context: not specified. Sources executed: depmap, literature. Verification blocked=False; blocking_issues=0; warnings=0.

Evidence coverage is compiled below by category with tables listing canonical evidence ids.

Coverage by source execution status:
| source | status | records | duration_ms | error |
| --- | --- | --- | --- | --- |
| depmap | success | 15 | 14942 |  |
| literature | success | 15 | 2769 |  |

## 2. Target Annotation Evidence

This section compiles target annotation evidence (e.g., tractability, target development level, known ligands) as provided by the evidence payload.

| evidence_id | source | summary | confidence | normalized_score |
| --- | --- | --- | --- | --- |
|  |  | No target annotation evidence provided. |  |  |

## 3. Genetic Dependency Evidence

### Global Dependency Analysis

This subsection compiles global genetic dependency signals across screened cell lines when present.

| evidence_id | source | summary | confidence | normalized_score |
| --- | --- | --- | --- | --- |
| [depmap:EGFR:genetic_dependency] | depmap | DepMap CRISPR gene effect for EGFR: -0.24

```

## human_review_gate (human_review_gate)

### Input

```json
{
  "conflict_agent_report": null,
  "conflicts": [],
  "errors": [],
  "evidence_graph": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
    "edges": [
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:1",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:10",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:11",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:12",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:13",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:14",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:15",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:16",
        "target_id": "publication:pmid:21221095"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:16",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:17",
        "target_id": "publication:pmid:23550210"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:17",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:18",
        "target_id": "publication:pmid:23323831"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:18",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:19",
        "target_id": "publication:pmid:24002530"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:19",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:2",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:20",
        "target_id": "publication:pmid:23000897"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:20",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:21",
        "target_id": "publication:pmid:15118073"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:21",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:22",
        "target_id": "publication:pmid:3798106"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:22",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:23",
        "target_id": "publication:pmid:20303878"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:23",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:24",
        "target_id": "publication:pmid:17618441"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:24",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:25",
        "target_id": "publication:pmid:34185076"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:25",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:26",
        "target_id": "publication:pmid:27718847"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:26",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:27",
        "target_id": "publication:pmid:32029601"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:27",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:28",
        "target_id": "publication:pmid:26412456"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:28",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:29",
        "target_id": "publication:pmid:15118125"
      },
      {
        "attributes": {
... [TRUNCATED]

```

### Output

```json
{
  "review_decision": {
    "decision": "approved",
    "reason": "preapprove for full trace export",
    "reviewed_at": "2026-03-13T09:35:21.579891Z",
    "reviewer_id": "trace-user"
  },
  "review_iteration_count": 0,
  "review_recollection_pending": false
}
```

## emit_dossier (dossier_emitter)

### Input

```json
{
  "conflict_agent_report": null,
  "conflicts": [],
  "errors": [],
  "evidence_graph": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
    "edges": [
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:1",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:10",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:11",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:12",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:13",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:14",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:15",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:16",
        "target_id": "publication:pmid:21221095"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:16",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:17",
        "target_id": "publication:pmid:23550210"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:17",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:18",
        "target_id": "publication:pmid:23323831"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:18",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:19",
        "target_id": "publication:pmid:24002530"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:19",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:2",
        "target_id": "source:depmap"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:20",
        "target_id": "publication:pmid:23000897"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:20",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:21",
        "target_id": "publication:pmid:15118073"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:21",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:22",
        "target_id": "publication:pmid:3798106"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:22",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:23",
        "target_id": "publication:pmid:20303878"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:23",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:24",
        "target_id": "publication:pmid:17618441"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:24",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:25",
        "target_id": "publication:pmid:34185076"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:25",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:26",
        "target_id": "publication:pmid:27718847"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:26",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:27",
        "target_id": "publication:pmid:32029601"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:27",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:28",
        "target_id": "publication:pmid:26412456"
      },
      {
        "attributes": {},
        "edge_type": "evidence_source",
        "source_id": "evidence:28",
        "target_id": "source:literature"
      },
      {
        "attributes": {},
        "edge_type": "evidence_publication",
        "source_id": "evidence:29",
        "target_id": "publication:pmid:15118125"
      },
      {
        "attributes": {
... [TRUNCATED]

```

### Output

```json
{
  "dossier_agent_report": null,
  "final_dossier": {
    "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/dossiers/egfr-agent-io-trace-04.evidence_dossier.json",
    "artifacts": {
      "graph": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
      "plan": "/Users/apple/Desktop/Drugagent/artifacts/plans/egfr-agent-io-trace-04.collection_plan.json"
    },
    "conflicts": [],
    "emitted_at": "2026-03-13T09:38:04.005373Z",
    "errors": [],
    "graph_snapshot": {
      "artifact_path": "/Users/apple/Desktop/Drugagent/artifacts/graphs/egfr-agent-io-trace-04.evidence_graph.json",
      "edges": [
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:1",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:10",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:11",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:12",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:13",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:14",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:15",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:16",
          "target_id": "publication:pmid:21221095"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:16",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:17",
          "target_id": "publication:pmid:23550210"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:17",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:18",
          "target_id": "publication:pmid:23323831"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:18",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:19",
          "target_id": "publication:pmid:24002530"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:19",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:2",
          "target_id": "source:depmap"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:20",
          "target_id": "publication:pmid:23000897"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:20",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:21",
          "target_id": "publication:pmid:15118073"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:21",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:22",
          "target_id": "publication:pmid:3798106"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:22",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:23",
          "target_id": "publication:pmid:20303878"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:23",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:24",
          "target_id": "publication:pmid:17618441"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:24",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:25",
          "target_id": "publication:pmid:34185076"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:25",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence_publication",
          "source_id": "evidence:26",
          "target_id": "publication:pmid:27718847"
        },
        {
          "attributes": {},
          "edge_type": "evidence_source",
          "source_id": "evidence:26",
          "target_id": "source:literature"
        },
        {
          "attributes": {},
          "edge_type": "evidence
... [TRUNCATED]

```

