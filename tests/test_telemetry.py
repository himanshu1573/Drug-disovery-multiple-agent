from __future__ import annotations

import json
import logging
from io import StringIO

from agents.telemetry import get_logger, log_event, redact_secrets


def test_redact_secrets_masks_secret_like_values() -> None:
    payload = redact_secrets(
        {
            "token": "sk-1234567890abcdef",
            "nested": ["lsv2_1234567890abcdef", "safe"],
            "message": "api_key=supersecretvalue",
        }
    )

    assert payload["token"] == "[REDACTED]"
    assert payload["nested"][0] == "[REDACTED]"
    assert "[REDACTED]" in payload["message"]


def test_log_event_emits_json_without_secret_leakage() -> None:
    logger = get_logger()
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.handlers = [handler]

    log_event("stage_start", run_id="run-1", api_key="sk-1234567890abcdef")

    record = json.loads(stream.getvalue().strip().splitlines()[-1])
    assert record["event"] == "stage_start"
    assert record["api_key"] == "[REDACTED]"
