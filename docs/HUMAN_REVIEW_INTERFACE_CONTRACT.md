# Human Review Interface Contract

The review interface is transport-agnostic. CLI, API, or notebook callers should submit a structured review payload and receive a structured acceptance response.

## Input

- `run_id`
- `decision`: `approved | rejected | needs_more_evidence`
- `reviewer_id`
- `reason`

## Response

- `run_id`
- `accepted`
- `decision`
- `status`

## Rules

- `reviewer_id` and `reason` are required for every decision.
- `needs_more_evidence` signals a bounded recollection path.
- `rejected` produces a terminal non-ready handoff.
- `approved` is the only decision that sets Phase-2 handoff `ready=true`.
