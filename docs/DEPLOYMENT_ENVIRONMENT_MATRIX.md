# Deployment Environment Matrix

## Profiles

| Profile | Summary Model | Retry Attempts | PHAROS Timeout (s) | Observability | Offline Mode |
|---|---|---:|---:|---|---|
| `dev` | `gpt-5` | 3 | 30 | `debug` | `false` |
| `test` | `deterministic_fallback` | 3 | 5 | `test` | `true` |
| `staging` | `gpt-5-mini` | 3 | 20 | `info` | `false` |
| `prod` | `gpt-5` | 3 | 20 | `info` | `false` |

## Settings covered

- API key usage remains environment-based.
- Retry limits stay aligned with bounded backoff policy.
- PHAROS startup timeout is profile-specific.
- Observability verbosity is profile-specific.
- Test profile is explicitly offline-first.

## Source of truth

- Runtime definitions live in [agents/config_profiles.py](/Users/apple/Desktop/Drugagent/agents/config_profiles.py).
- Local profile selection uses `A4T_ENV_PROFILE`.
