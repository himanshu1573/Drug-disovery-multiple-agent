from __future__ import annotations

import pytest

from agents.config_profiles import get_config_profile, validate_config_profiles


def test_config_profiles_validate_required_fields() -> None:
    validate_config_profiles()


def test_get_config_profile_supports_all_declared_profiles() -> None:
    assert get_config_profile("dev")["observability_level"] == "debug"
    assert get_config_profile("test")["offline_mode"] is True
    assert get_config_profile("staging")["summary_model"] == "gpt-5-mini"
    assert get_config_profile("prod")["retry_max_attempts"] == 3


def test_get_config_profile_rejects_unknown_profile() -> None:
    with pytest.raises(ValueError, match="Unknown config profile"):
        get_config_profile("unknown")
