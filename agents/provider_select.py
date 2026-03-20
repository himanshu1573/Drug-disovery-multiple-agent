from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


def _bool_env(name: str, default: str = "0") -> bool:
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes"}


def _probe_timeout_s() -> float:
    raw = os.getenv("A4T_PROVIDER_PROBE_TIMEOUT_S", "6").strip()
    try:
        return max(1.0, float(raw))
    except ValueError:
        return 6.0


def _system_provider_pref() -> str:
    raw = os.getenv("A4T_SYSTEM_LLM_PROVIDER", "auto").strip().lower()
    return raw if raw in {"auto", "openai", "google"} else "auto"


def _openai_key_present() -> bool:
    return bool(os.getenv("OPENAI_API_KEY", "").strip())


def _google_key_present() -> bool:
    return bool((os.getenv("GOOGLE_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")).strip())


async def _probe_openai(*, model: str) -> tuple[bool, str | None]:
    if not _openai_key_present():
        return False, "OPENAI_API_KEY not set"
    try:
        # Keep the probe lightweight; avoid provider-specific kwargs that can drift across library versions.
        llm = ChatOpenAI(model=model, temperature=0)
        await asyncio.wait_for(llm.ainvoke("ping"), timeout=_probe_timeout_s())
        return True, None
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}: {exc}"


async def _probe_google(*, model: str) -> tuple[bool, str | None]:
    if not _google_key_present():
        return False, "GOOGLE_API_KEY/GEMINI_API_KEY not set"
    try:
        llm = ChatGoogleGenerativeAI(model=model, temperature=0, max_output_tokens=1)
        # Defensive: google client has had cases where `ainvoke()` blocks; use a thread.
        await asyncio.wait_for(asyncio.to_thread(llm.invoke, "ping"), timeout=_probe_timeout_s())
        return True, None
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}: {exc}"


@dataclass(frozen=True)
class ProviderSelection:
    provider: str  # openai|google|none
    locked: bool
    llm_calls_enabled: bool
    error: str | None = None
    selected_at_ms: int = 0

    def as_dict(self) -> dict[str, object]:
        return {
            "provider": self.provider,
            "locked": self.locked,
            "llm_calls_enabled": self.llm_calls_enabled,
            "error": self.error,
            "selected_at_ms": self.selected_at_ms,
            "system_pref": _system_provider_pref(),
        }


_CACHED: ProviderSelection | None = None
_LOCK = asyncio.Lock()


def current_provider_selection() -> ProviderSelection | None:
    return _CACHED


def reset_provider_selection() -> None:
    """Reset the cached selection. Internal/Test use only."""
    global _CACHED  # noqa: PLW0603
    _CACHED = None
    if "A4T_LLM_PROVIDER" in os.environ:
        del os.environ["A4T_LLM_PROVIDER"]
    # Do NOT reset A4T_LLM_CALLS_ENABLED or CROSS_PROVIDER_FALLBACK here as they might be set by .env


async def select_provider_once() -> ProviderSelection:
    """Select and lock the system provider for this process.

    Policy (default):
    - If A4T_SYSTEM_LLM_PROVIDER=auto:
      - probe OpenAI first, then Google
    - If explicitly openai/google:
      - probe that provider, and (by default) do not fall back to the other provider
    - If no provider is reachable:
      - disable live LLM calls for this process (deterministic mode)
    """
    global _CACHED  # noqa: PLW0603
    if _CACHED is not None:
        return _CACHED

    async with _LOCK:
        if _CACHED is not None:
            return _CACHED

        system_pref = _system_provider_pref()
        
        openai_model = os.getenv("A4T_OPENAI_FAST_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"
        google_model = os.getenv("A4T_GOOGLE_FAST_MODEL", "gemini-2.5-flash").strip() or "gemini-2.5-flash"

        # Start probes in parallel to minimize latency
        openai_task = _probe_openai(model=openai_model)
        google_task = _probe_google(model=google_model)
        
        results = await asyncio.gather(openai_task, google_task, return_exceptions=True)
        
        openai_ok, openai_err = results[0] if not isinstance(results[0], Exception) else (False, str(results[0]))
        google_ok, google_err = results[1] if not isinstance(results[1], Exception) else (False, str(results[1]))

        selected: str | None = None
        
        # Selection logic:
        # 1. HONOR SYSTEM PREFERENCE FIRST (if locked and healthy)
        if system_pref == "openai" and openai_ok:
            selected = "openai"
        elif system_pref == "google" and google_ok:
            selected = "google"
        # 2. AUTO-SELECT (Priority: OpenAI > Google)
        elif openai_ok:
            selected = "openai"
        elif google_ok:
            selected = "google"

        selected_at_ms = int(time.time() * 1000)
        if selected is None:
            errors = []
            if openai_err: errors.append(f"openai: {openai_err}")
            if google_err: errors.append(f"google: {google_err}")
            
            os.environ["A4T_LLM_CALLS_ENABLED"] = "0"
            os.environ["A4T_LLM_CROSS_PROVIDER_FALLBACK"] = "0"
            
            # Log failure to a local file for debugging
            try:
                with open("llm_probe_error.log", "w") as f:
                    f.write(f"Selection Result: FAIL\nErrors: {'; '.join(errors) if errors else 'Unknown'}\n")
            except Exception:
                pass

            os.environ.setdefault("A4T_LLM_PROVIDER", system_pref if system_pref != "auto" else "openai")
            _CACHED = ProviderSelection(
                provider="none",
                locked=True,
                llm_calls_enabled=False,
                error="; ".join(errors) if errors else "Probes failed for both providers",
                selected_at_ms=selected_at_ms,
            )
            return _CACHED

        os.environ["A4T_LLM_PROVIDER"] = selected
        os.environ.setdefault("A4T_LLM_CALLS_ENABLED", "1")
        # Ensure fallback is enabled globally to handle transient errors in the locked provider.
        os.environ["A4T_LLM_CROSS_PROVIDER_FALLBACK"] = "1"
        
        _CACHED = ProviderSelection(
            provider=selected,
            locked=True,
            llm_calls_enabled=True,
            error=None,
            selected_at_ms=selected_at_ms,
        )
        return _CACHED
