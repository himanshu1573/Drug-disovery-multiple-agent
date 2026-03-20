# Operational Runbook

## Daily checks

- Review latest files under `artifacts/health_reports/` for source availability.
- Review latest files under `artifacts/metrics/` for source latency, success ratio, verification failures, and conflict counts.
- Confirm checkpoint continuity by inspecting `artifacts/working_memory/<run_id>/` for the most recent failed or resumed run.

## Incident triage

### Source unhealthy before run

- `pharos` launcher missing: restore `external_mcps/run_pharos_mcp.sh` or disable `pharos` from the request.
- `depmap` cache missing: restore `mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv` or refresh local cache.

### Source fails during run

- Timeout or `429`: rely on bounded retry policy, then inspect `retry_telemetry` in raw payload artifacts.
- Partial outage: confirm final dossier still emitted and verify degraded source coverage in summary and metrics.
- Malformed payload: inspect raw payload and connector parsing path before retrying.

### Recovery

- Use the same `run_id` to inspect checkpoints and working-memory snapshots.
- Resume from the last stable node using the existing checkpoint path.
- Compare `procedural_memory`, `plans`, `graphs`, and `metrics` artifacts for reproducibility gaps.

## Review checklist

- Source coverage section explains which sources succeeded or degraded.
- Conflict notes match the emitted `ConflictRecord` entries.
- Metrics and health artifacts exist for the run.
- Graph artifact exists when the run reaches `build_evidence_graph`.

## Escalation

- Escalate to human review when conflicts are high severity, verification is blocked, or source coverage is materially degraded.
