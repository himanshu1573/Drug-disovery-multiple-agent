# Configuration Policy

This project uses environment-based runtime configuration for secrets and provider credentials.

## Rules

- Do not hardcode API keys, tokens, or secrets in source files.
- Load provider credentials from environment variables only.
- Supported LLM providers:
  - OpenAI: `OPENAI_API_KEY`
  - Google Gemini: `GOOGLE_API_KEY` (preferred) or `GEMINI_API_KEY` (supported alias)
- `A4T_LLM_PROVIDER=auto|openai|google` selects the active provider (default: `auto`).
- `A4T_LLM_CALLS_ENABLED=1|0` enables/disables outbound LLM calls (default: enabled; under pytest: disabled unless explicitly enabled).
- `A4T_LLM_CROSS_PROVIDER_FALLBACK=1|0` controls whether the runtime will try the other provider when the preferred one fails (default: enabled for auto; disabled when provider is explicitly forced).
- `A4T_LLM_RETRY_ATTEMPTS` and `A4T_LLM_RETRY_BASE_DELAY_S` control retry behavior for timeouts (defaults: 3 attempts, base delay 1s).
- `A4T_LLM_CONCURRENCY`, `A4T_LLM_MIN_INTERVAL_S`, and optional `A4T_LLM_RPM` implement a global rate limiter (recommended for free tier).
- `A4T_LLM_429_BASE_DELAY_S` and `A4T_LLM_429_MAX_DELAY_S` control backoff when a provider rate-limits (429/resource exhausted).
- Missing provider credentials can degrade to deterministic behavior only when `A4T_REQUIRE_LLM_AGENTS=0`.
- Runtime logging must redact secret-like values before emission.
- Artifact files may contain run metadata, but must not contain raw secrets.
- Note: the default runtime flow is now "lean" and does not execute optional commentary agents.

## Operational guardrails

- Use `.env` only for local development and keep it uncommitted.
- Use `.env.example` as the non-secret template.
- Prefer source-specific environment variables over embedding credentials in request payloads.
- When adding new providers, extend secret redaction patterns and add regression tests.

## Model Defaults (Configurable)
- Reasoning defaults:
  - Google: `A4T_GOOGLE_REASONING_MODEL` (default: `gemini-2.5-flash`)
  - OpenAI: `A4T_OPENAI_REASONING_MODEL` (default: `gpt-5`)
- Fast defaults:
  - Google: `A4T_GOOGLE_FAST_MODEL` (default: `gemini-2.5-flash`)
  - OpenAI: `A4T_OPENAI_FAST_MODEL` (default: `gpt-5-mini`)

## Automatic Fallbacks (Optional)
Structured-output agent calls can fall back to alternate models/providers when enabled:
- Toggle: `A4T_LLM_FALLBACK_ENABLED=1|0` (default: 1)
- Google fallback list: `A4T_GOOGLE_FALLBACK_MODELS` (comma-separated)
- OpenAI fallback list: `A4T_OPENAI_FALLBACK_MODELS` (comma-separated)

## Optional Commentary Agents (Currently Disabled)
The following LLM commentary agents are not executed in the default flow and their implementations live under
`agents/optional_agents/`:
- per-source collector review agent (`SourceCollectionAgent`)
- verification interpretation agent (`VerificationAgent` LLM assessor)
- conflict interpretation agent (`ConflictResolutionAgent` LLM assessor)
- graph commentary agent (`EvidenceGraphAgent` LLM assessor)
- dossier commentary agent (`DossierAgent` LLM assessor)

Re-enabling them requires explicitly wiring them back into the LangGraph runtime.

## Content Memory (Optional)
To provide consistent project context to every LLM agent prompt:
- `A4T_CONTENT_MEMORY_ENABLED=1|0` (default: 1)
- `A4T_CONTENT_MEMORY_PATH` (default: `docs/CONTENT_MEMORY.md`, fallback: `docs/WHAT_WE_ARE_BUILDING.md`)
- `A4T_CONTENT_MEMORY_MAX_CHARS` (default: 6000)

## Report Format (Optional)
The SummaryAgent supports two output formats:
- `A4T_REPORT_FORMAT=structured` (default): 9-section "THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT" compiler format (tables + evidence ids).
- `A4T_REPORT_FORMAT=dossier`: legacy 9-section "Integrated Therapeutic Target Dossier" narrative report.

## Follow-up + User URL Fetching (Optional)
For in-run follow-up Q&A, the UI API can optionally fetch **user-provided URLs** and pass extracted snippets to the follow-up agent.

- `A4T_FOLLOWUP_MAX_URLS` (default: 5): maximum number of user URLs to fetch per follow-up request.
- `A4T_URL_FETCH_TIMEOUT_S` (default: 15): per-request timeout for fetching a URL.
- `A4T_URL_FETCH_MAX_BYTES` (default: 2000000): maximum bytes downloaded per URL.
- `A4T_URL_FETCH_DNS_CHECK=1|0` (default: 1): whether to DNS-resolve hostnames and block those resolving to private/localhost IPs (SSRF mitigation).

## Current enforcement

- Secret redaction is implemented in [agents/telemetry.py](/Users/apple/Desktop/Drugagent/agents/telemetry.py).
- Summary generation reads credentials from environment variables in [agents/summary_agent.py](/Users/apple/Desktop/Drugagent/agents/summary_agent.py).
- Regression coverage exists in [tests/test_telemetry.py](/Users/apple/Desktop/Drugagent/tests/test_telemetry.py).
