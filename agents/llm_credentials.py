"""Per-session LLM credentials (bring-your-own-key).

A key supplied by a UI session is scoped to the current asyncio context via a ContextVar, so it:
- never touches `os.environ` (shared by every request and inherited by MCP subprocesses), and
- never enters `CollectorRequest` (persisted to dossiers, run state, and working memory).

`llm_policy` consults `current_llm_credentials()` before falling back to server env keys.
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import Literal

LLMProvider = Literal["openai", "google"]


@dataclass(frozen=True)
class LLMCredentials:
    provider: LLMProvider
    api_key: str = field(repr=False)

    def redact(self, text: str) -> str:
        """Remove this key from text that may be shown to users or persisted."""
        return text.replace(self.api_key, "[REDACTED]") if self.api_key else text


_CURRENT: ContextVar[LLMCredentials | None] = ContextVar("a4t_llm_credentials", default=None)


def current_llm_credentials() -> LLMCredentials | None:
    return _CURRENT.get()


@contextmanager
def use_llm_credentials(creds: LLMCredentials | None) -> Iterator[None]:
    token = _CURRENT.set(creds)
    try:
        yield
    finally:
        _CURRENT.reset(token)
