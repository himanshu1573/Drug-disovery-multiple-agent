from __future__ import annotations

import os
from typing import Literal


ProfileName = Literal["dev", "test", "staging", "prod"]


CONFIG_PROFILES: dict[str, dict[str, object]] = {
    "dev": {
        "summary_model": "gpt-5",
        "retry_max_attempts": 3,
        "pharos_start_timeout_s": 30,
        "observability_level": "debug",
        "offline_mode": False,
    },
    "test": {
        "summary_model": "deterministic_fallback",
        "retry_max_attempts": 3,
        "pharos_start_timeout_s": 5,
        "observability_level": "test",
        "offline_mode": True,
    },
    "staging": {
        "summary_model": "gpt-5-mini",
        "retry_max_attempts": 3,
        "pharos_start_timeout_s": 20,
        "observability_level": "info",
        "offline_mode": False,
    },
    "prod": {
        "summary_model": "gpt-5",
        "retry_max_attempts": 3,
        "pharos_start_timeout_s": 20,
        "observability_level": "info",
        "offline_mode": False,
    },
}


def get_config_profile(name: str | None = None) -> dict[str, object]:
    raw = name if name is not None else (os.getenv("A4T_ENV_PROFILE") or "dev")
    profile_name = raw.strip().lower()
    if profile_name not in CONFIG_PROFILES:
        raise ValueError(f"Unknown config profile: {profile_name}")
    return dict(CONFIG_PROFILES[profile_name])


def validate_config_profiles() -> None:
    required_fields = {
        "summary_model",
        "retry_max_attempts",
        "pharos_start_timeout_s",
        "observability_level",
        "offline_mode",
    }
    for name, profile in CONFIG_PROFILES.items():
        missing = required_fields.difference(profile)
        if missing:
            raise ValueError(f"Profile '{name}' missing fields: {sorted(missing)}")
