# Summary Guardrails

The explanation stage must remain grounded in verified evidence only.

## Enforced checks

- Required sections:
  - `Source Coverage`
  - `Confidence Profile`
  - `Conflict Notes`
  - `Grounded Findings`
- Grounded findings must reference canonical evidence IDs.
- Forbidden speculative language includes phrases such as `I think`, `we believe`, and `probably`.

## Runtime behavior

- If an LLM-generated summary fails validation, the runtime falls back to the deterministic grounded summary path.
