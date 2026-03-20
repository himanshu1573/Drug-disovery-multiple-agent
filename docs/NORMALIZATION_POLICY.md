# Normalization Policy

Phase-1 normalization converts source-specific payloads into the canonical `EvidenceRecord` contract before verification, conflict analysis, and dossier emission.

## Current rules

- `target_symbol` is trimmed and uppercased.
- `disease_id` is trimmed; empty values become `null`.
- `normalized_score` is preserved when already present.
- If `normalized_score` is missing and `raw_value` is numeric, the numeric value is clamped to `[0.0, 1.0]`.
- If `raw_value` is non-numeric and `normalized_score` is missing, `normalized_score` stays `null`.
- `confidence` is clamped to `[0.0, 1.0]`.
- `summary` is trimmed.
- `normalization_policy_version` is stamped on every record.

## Fixture coverage

The reproducible fixture set lives under [tests/fixtures/normalization](/Users/apple/Desktop/Drugagent/tests/fixtures/normalization) and covers:

- `KRAS`: canonical dependency-style numeric mapping.
- `EGFR`: empty disease normalization plus score/confidence clamping.
- `TP53`: literature-style non-numeric payload preservation.

These fixtures are used by tests to assert deterministic source-to-schema behavior.
