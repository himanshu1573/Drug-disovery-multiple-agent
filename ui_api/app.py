from __future__ import annotations

import asyncio
import json
import os
from typing import Any, AsyncGenerator

from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

from agents.artifact_store import artifact_layout, artifact_root
from agents.graph import CollectionPaused, get_collection_state, resume_collection_graph, run_collection_graph
from agents.plan_interface import apply_plan_decision
from agents.provider_select import current_provider_selection, select_provider_once
from agents.run_state_store import RunStateStore
from agents.review_interface import apply_review_decision
from agents.schema import CollectorRequest, EvidenceDossier, EvidenceRecord, SourceName
from agents.query_interpretation_agent import QueryInterpretationAgent, QueryInterpretationContext
from agents.followup_agent import FollowupAgent, FollowupContext
from agents.url_resource_fetcher import UrlResourceFetcher, extract_urls as extract_urls_from_text
from ui_api.event_bus import BUS
from ui_api.models import (
    CreateRunInput,
    CreateRunResponse,
    CreateRunFromTextInput,
    FollowupInput,
    FollowupResponse,
    PlanDecisionBody,
    ResumeRunResponse,
    ReviewDecisionBody,
)


def _bool_env(name: str, default: str = "0") -> bool:
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes"}


app = FastAPI(title="Drugagent UI Gateway", version="0.1.0")

# Load repo-local .env so UI runs match CLI behavior (keys + runtime toggles).
try:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # If Docker Compose injects empty env vars (e.g., OPENAI_API_KEY=""), treat them as unset so
    # repo-local `.env` can populate values for local/dev runs.
    for key in ("OPENAI_API_KEY", "GOOGLE_API_KEY", "GEMINI_API_KEY"):
        if os.getenv(key, None) == "":
            os.environ.pop(key, None)
    load_dotenv(os.path.join(repo_root, ".env"), override=False)
except Exception:
    pass

# UI default provider behavior:
# - Many developers set both GOOGLE_API_KEY and OPENAI_API_KEY locally.
# - The library "auto" preference may pick Google first; if quota/timeouts occur and
#   cross-provider fallback is disabled, the UI will silently degrade to deterministic output.
# Prefer OpenAI by default when a key is present, unless the user explicitly set A4T_LLM_PROVIDER.
if not os.getenv("A4T_LLM_PROVIDER"):
    if os.getenv("OPENAI_API_KEY", "").strip():
        os.environ.setdefault("A4T_LLM_PROVIDER", "openai")
    elif os.getenv("GOOGLE_API_KEY", "").strip() or os.getenv("GEMINI_API_KEY", "").strip():
        os.environ.setdefault("A4T_LLM_PROVIDER", "google")

# UI default: strict mode. Do not silently fall back to deterministic summaries.
# If LLM calls fail (missing keys, quota, invalid output), runs should fail and surface the error to the UI.
os.environ.setdefault("A4T_REQUIRE_LLM_AGENTS", "1")
os.environ.setdefault("A4T_LLM_CALLS_ENABLED", "1")
os.environ.setdefault("A4T_LLM_FALLBACK_ENABLED", "1")
os.environ.setdefault("A4T_LLM_CROSS_PROVIDER_FALLBACK", "1")

# UI default report: compiler (LLM-generated 9-section scientific report).
# If the user explicitly overrides A4T_REPORT_FORMAT, honor it.
if not os.getenv("A4T_REPORT_FORMAT"):
    os.environ.setdefault("A4T_REPORT_FORMAT", "compiler")

# Configuration harmonization:
# If the user explicitly disabled LLM calls (A4T_LLM_CALLS_ENABLED=0), do not require LLM agents.
# This prevents hard-failures like: "LLM calls are disabled ... but A4T_REQUIRE_LLM_AGENTS=1".
if not _bool_env("A4T_LLM_CALLS_ENABLED", "1"):
    os.environ["A4T_REQUIRE_LLM_AGENTS"] = "0"
    os.environ.setdefault("A4T_LLM_FALLBACK_ENABLED", "1")
    os.environ.setdefault("A4T_REPORT_FORMAT", "structured")

# UI default: remove human-in-the-loop gates (no pause modals).
os.environ.setdefault("A4T_REQUIRE_REVIEW", "0")
os.environ.setdefault("A4T_REQUIRE_PLAN_APPROVAL", "0")

# Reasonable defaults for free-tier Gemini: minimize burstiness to reduce 429s.
os.environ.setdefault("A4T_LLM_CONCURRENCY", "1")
os.environ.setdefault("A4T_LLM_MIN_INTERVAL_S", "3.0")
os.environ.setdefault("A4T_LLM_RETRY_ATTEMPTS", "2")
# Planner/summarizer calls can legitimately take >60s (especially compiler reports with large payloads).
os.environ.setdefault("A4T_LLM_TIMEOUT_S", "180")
os.environ.setdefault("A4T_LLM_429_BASE_DELAY_S", "2.0")
os.environ.setdefault("A4T_LLM_429_MAX_DELAY_S", "8.0")
os.environ.setdefault("A4T_LLM_RPM", "10")
os.environ.setdefault("A4T_SOURCE_DISPATCH_MODE", "sequential")

if _bool_env("A4T_UI_CORS_ENABLED", "1"):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin.strip() for origin in os.getenv("A4T_UI_CORS_ORIGINS", "http://localhost:3000").split(",")],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def _select_llm_provider_on_startup() -> None:
    # Choose a single provider for this process (OpenAI-first by default) so runs are consistent.
    try:
        await select_provider_once()
    except Exception:
        # Never block UI startup; agents will fall back deterministically if LLM calls are disabled.
        pass


@app.get("/api/health")
async def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "provider": (current_provider_selection() or (await select_provider_once())).as_dict(),
        "report_format": os.getenv("A4T_REPORT_FORMAT", ""),
        "llm_calls_enabled": os.getenv("A4T_LLM_CALLS_ENABLED", ""),
        "require_llm_agents": os.getenv("A4T_REQUIRE_LLM_AGENTS", ""),
        "llm_timeout_s": os.getenv("A4T_LLM_TIMEOUT_S", ""),
        "require_llm_planner": os.getenv("A4T_REQUIRE_LLM_PLANNER", "0"),
        "has_openai_key": bool(os.getenv("OPENAI_API_KEY", "").strip()),
    }


async def _run_in_background(request, *, is_resume: bool = False) -> None:
    run_id = request.run_id
    BUS.ensure_run(run_id)

    def on_progress(event_type: str, payload: dict[str, Any]) -> None:
        BUS.publish(run_id, event_type, payload)

    try:
        if is_resume:
            BUS.publish(run_id, "run_status", {"run_id": run_id, "status": "resuming"})
            result = await resume_collection_graph(request, progress_cb=on_progress)
        else:
            BUS.publish(run_id, "run_status", {"run_id": run_id, "status": "running"})
            result = await run_collection_graph(request, progress_cb=on_progress)

        BUS.publish(run_id, "run_completed", {"run_id": run_id, "status": "completed", "result": result.model_dump(mode="json") if hasattr(result, "model_dump") else result})
    except CollectionPaused as exc:
        BUS.publish(
            run_id,
            "run_paused",
            {
                "run_id": run_id,
                "reason": exc.reason,
                "next_stages": list(exc.next_stages),
            },
        )
    except Exception as exc:  # noqa: BLE001
        BUS.publish(run_id, "run_failed", {"run_id": run_id, "status": "failed", "error": str(exc)})


@app.post("/api/runs", response_model=CreateRunResponse)
async def create_run(body: CreateRunInput, background: BackgroundTasks) -> CreateRunResponse:
    await select_provider_once()
    request = body.to_request()
    run_id = request.run_id
    BUS.ensure_run(run_id)
    background.add_task(_run_in_background, request, is_resume=False)
    return CreateRunResponse(run_id=run_id, status="started")


@app.post("/api/runs/from-text", response_model=CreateRunResponse)
async def create_run_from_text(body: CreateRunFromTextInput, background: BackgroundTasks) -> CreateRunResponse:
    await select_provider_once()
    interp = QueryInterpretationAgent(model=body.model_override)
    parsed = await interp.interpret(message=body.message, context=QueryInterpretationContext(mode="new_run"))
    if not parsed.in_scope:
        raise HTTPException(status_code=400, detail=parsed.user_message_to_show_if_out_of_scope)
    if not parsed.gene_symbol:
        raise HTTPException(status_code=400, detail="Could not extract a target gene symbol from the message.")

    run_id = body.run_id or f"run-{__import__('uuid').uuid4().hex[:12]}"
    request = CollectorRequest(
        gene_symbol=parsed.gene_symbol,
        disease_id=parsed.disease_id,
        objective=parsed.objective,
        sources=body.sources
        or [
            SourceName.DEPMAP,
            SourceName.PHAROS,
            SourceName.OPENTARGETS,
            SourceName.LITERATURE,
        ],
        per_source_top_k=body.per_source_top_k,
        max_literature_articles=body.max_literature_articles,
        model_override=body.model_override,
        run_id=run_id,
    )
    BUS.ensure_run(run_id)
    background.add_task(_run_in_background, request, is_resume=False)
    return CreateRunResponse(run_id=run_id, status="started")


@app.post("/api/runs/{run_id}/resume", response_model=ResumeRunResponse)
async def resume_run(run_id: str, background: BackgroundTasks) -> ResumeRunResponse:
    await select_provider_once()
    snapshot = await get_collection_state(run_id)
    request = snapshot.values.get("query")
    if request is None:
        raise HTTPException(status_code=404, detail=f"Unknown run_id `{run_id}`")
    if isinstance(request, dict):
        request = CollectorRequest.model_validate(request)
    background.add_task(_run_in_background, request, is_resume=True)
    return ResumeRunResponse(run_id=run_id, status="resumed")


@app.get("/api/runs/{run_id}/state")
async def get_state(run_id: str) -> dict[str, Any]:
    snapshot = await get_collection_state(run_id)
    persisted = RunStateStore.load_latest(run_id)
    return {
        "run_id": run_id,
        "next": list(snapshot.next),
        "values": jsonable_encoder(snapshot.values),
        "_runtime": (current_provider_selection() or (await select_provider_once())).as_dict(),
        "_persisted": (
            {
                "status": persisted.status,
                "last_stage": persisted.last_stage,
                "updated_at_ms": persisted.updated_at_ms,
                "error": persisted.error,
            }
            if persisted is not None
            else None
        ),
    }


def _sse_encode(event: str, data: dict[str, Any]) -> str:
    return f"event: {event}\ndata: {json.dumps(data, default=str)}\n\n"


@app.get("/api/runs/{run_id}/events")
async def stream_events(run_id: str) -> StreamingResponse:
    queue = BUS.subscribe(run_id)

    async def gen() -> AsyncGenerator[bytes, None]:
        yield _sse_encode("connected", {"run_id": run_id}).encode("utf-8")
        try:
            while True:
                try:
                    item = await asyncio.wait_for(queue.get(), timeout=15.0)
                    yield _sse_encode(item.event, {**item.data, "_ts_ms": item.created_at_ms}).encode("utf-8")
                except asyncio.TimeoutError:
                    yield _sse_encode("ping", {"run_id": run_id}).encode("utf-8")
        finally:
            BUS.unsubscribe(run_id, queue)

    return StreamingResponse(gen(), media_type="text/event-stream")


def _artifact_meta_for_run(run_id: str) -> dict[str, Any]:
    layout = artifact_layout(run_id)
    root = artifact_root().resolve()

    artifacts: dict[str, Any] = {}
    for key, raw_path in layout.items():
        try:
            path = (root / os.path.relpath(raw_path, str(root))).resolve()
        except Exception:
            # If relpath fails for any reason, treat as missing.
            artifacts[key] = {"path": raw_path, "exists": False, "kind": "unknown"}
            continue

        # Safety: only report artifacts inside the configured artifact root.
        if root not in path.parents and path != root:
            artifacts[key] = {"path": raw_path, "exists": False, "kind": "outside_root"}
            continue

        artifacts[key] = {
            "path": str(path),
            "exists": path.exists(),
            "kind": "dir" if path.exists() and path.is_dir() else "file",
        }

    # Episodic memory is shared; always include it for UI visibility.
    epi = (root / "episodic_memory" / "runs.json")
    artifacts["episodic_memory_runs"] = {"path": str(epi), "exists": epi.exists(), "kind": "file"}
    return artifacts


@app.get("/api/runs/{run_id}/artifacts")
async def get_artifacts(run_id: str) -> dict[str, Any]:
    return {"run_id": run_id, "artifacts": _artifact_meta_for_run(run_id)}


def _evidence_index_from_dossier(dossier: EvidenceDossier, *, max_items: int = 60) -> list[dict[str, Any]]:
    items = list(dossier.verified_evidence or [])
    items.sort(key=lambda it: float(it.confidence or 0.0), reverse=True)
    out: list[dict[str, Any]] = []
    for it in items[:max_items]:
        # Prefer canonical evidence ids. Fall back only for legacy artifacts.
        ev_id = it.evidence_id or f"{it.source}:{it.target_id}:{it.evidence_type}"
        support = it.support if isinstance(it.support, dict) else {}
        compact_support = {}
        for key in ("rank", "pmid", "title", "pub_year", "cited_by_count", "cell_line_id", "gene_effect", "tdl", "family", "ligand_total", "tractability", "association_count"):
            if key in support:
                compact_support[key] = support.get(key)
        out.append(
            {
                "evidence_id": ev_id,
                "source": it.source,
                "type": it.evidence_type,
                "summary": it.summary,
                "confidence": it.confidence,
                "normalized_score": it.normalized_score,
                "raw_value": it.raw_value,
                "support": compact_support,
            }
        )
    return out


def _evidence_index_from_records(records: list[EvidenceRecord], *, max_items: int = 60) -> list[dict[str, Any]]:
    items = list(records or [])
    items.sort(key=lambda it: float(it.confidence or 0.0), reverse=True)
    out: list[dict[str, Any]] = []
    for it in items[:max_items]:
        ev_id = it.evidence_id or f"{it.source}:{it.target_id}:{it.evidence_type}"
        support = it.support if isinstance(it.support, dict) else {}
        compact_support = {}
        for key in ("rank", "pmid", "title", "pub_year", "cited_by_count", "cell_line_id", "gene_effect", "tdl", "family", "ligand_total", "tractability", "association_count"):
            if key in support:
                compact_support[key] = support.get(key)
        out.append(
            {
                "evidence_id": ev_id,
                "source": it.source,
                "type": it.evidence_type,
                "summary": it.summary,
                "confidence": it.confidence,
                "normalized_score": it.normalized_score,
                "raw_value": it.raw_value,
                "support": compact_support,
            }
        )
    return out


@app.post("/api/runs/{run_id}/followup", response_model=FollowupResponse)
async def followup(run_id: str, body: FollowupInput) -> FollowupResponse:
    BUS.ensure_run(run_id)
    layout = artifact_layout(run_id)
    dossier_path = layout["dossier"]
    dossier: EvidenceDossier | None = None
    fallback_snapshot = None
    try:
        with open(dossier_path, "r") as f:
            dossier = EvidenceDossier.model_validate(json.load(f))
    except FileNotFoundError:
        # Allow follow-ups once the report has been generated, even if the run hasn't emitted the final dossier yet.
        fallback_snapshot = RunStateStore.load_latest(run_id)
        if fallback_snapshot is None:
            raise HTTPException(status_code=404, detail=f"Run dossier not found for run_id `{run_id}`")
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Failed to load dossier for run_id `{run_id}`: {exc}")

    if dossier is not None:
        gene = dossier.query.gene_symbol
        disease = dossier.query.disease_id
        objective = dossier.query.objective
        model_override = dossier.query.model_override
        dossier_summary_markdown = dossier.summary_markdown or ""
        evidence_index = _evidence_index_from_dossier(dossier)
    else:
        values = (fallback_snapshot.values if fallback_snapshot is not None else {}) or {}
        query = values.get("query") if isinstance(values.get("query"), dict) else {}
        gene = str(query.get("gene_symbol") or "").strip() or "UNKNOWN"
        disease = str(query.get("disease_id") or "").strip() or None
        objective = str(query.get("objective") or "").strip() or None
        model_override = query.get("model_override") if isinstance(query.get("model_override"), str) else None
        dossier_summary_markdown = str(values.get("explanation") or "").strip()
        records_raw = (
            values.get("normalized_items")
            if isinstance(values.get("normalized_items"), list)
            else values.get("verified_evidence")
            if isinstance(values.get("verified_evidence"), list)
            else []
        )
        try:
            records = [EvidenceRecord.model_validate(item) for item in records_raw]
        except Exception:
            records = []
        evidence_index = _evidence_index_from_records(records)
        if not dossier_summary_markdown or not evidence_index:
            raise HTTPException(
                status_code=409,
                detail="Follow-up is available after the report is generated (stage: generate_explanation). Please wait for the run to finish writing the report.",
            )

    interp = QueryInterpretationAgent(model=model_override)
    parsed = await interp.interpret(
        message=body.message,
        context=QueryInterpretationContext(mode="followup", active_gene=gene, active_disease=disease),
    )
    if not parsed.in_scope:
        return FollowupResponse(
            run_id=run_id,
            answer_markdown=parsed.user_message_to_show_if_out_of_scope,
            target_switch_detected=False,
            extracted_gene_symbol=None,
            used_urls=[],
        )
    if parsed.target_switch_detected and parsed.gene_symbol:
        return FollowupResponse(
            run_id=run_id,
            answer_markdown=(
                f"This run is for target **{gene}**. Your message looks like it switches targets to **{parsed.gene_symbol}**. "
                "Start a new thread/run for the new target to collect evidence consistently."
            ),
            target_switch_detected=True,
            extracted_gene_symbol=parsed.gene_symbol,
            used_urls=[],
        )

    urls = []
    urls.extend(parsed.detected_urls or [])
    urls.extend(body.urls or [])
    urls.extend(extract_urls_from_text(body.message))
    # Dedupe + cap in fetcher.
    urls = list(dict.fromkeys([u.strip() for u in urls if isinstance(u, str) and u.strip()]))

    BUS.publish(run_id, "followup_started", {"run_id": run_id})
    try:
        fetcher = UrlResourceFetcher()
        resources = await fetcher.fetch(urls)
        used_urls = [r.url for r in resources]
        context = FollowupContext(
            run_id=run_id,
            gene_symbol=gene,
            disease_id=disease,
            original_objective=objective,
            dossier_summary_markdown=dossier_summary_markdown,
            evidence_index=evidence_index,
            url_resources=[
                {"url": r.url, "content_type": r.content_type, "title": r.title, "text": r.text, "bytes_fetched": r.bytes_fetched}
                for r in resources
            ],
        )
        agent = FollowupAgent(model=model_override)
        answer = await agent.answer(question=body.message, context=context)
        BUS.publish(run_id, "followup_completed", {"run_id": run_id, "used_urls": used_urls})
        return FollowupResponse(
            run_id=run_id,
            answer_markdown=answer.answer_markdown,
            target_switch_detected=False,
            extracted_gene_symbol=gene,
            used_urls=used_urls,
        )
    except Exception as exc:  # noqa: BLE001
        BUS.publish(run_id, "followup_failed", {"run_id": run_id, "error": str(exc)})
        raise HTTPException(status_code=500, detail=f"Follow-up failed: {exc}")


@app.post("/api/runs/{run_id}/plan-decision")
async def post_plan_decision(run_id: str, body: PlanDecisionBody) -> dict[str, Any]:
    if body.run_id != run_id:
        raise HTTPException(status_code=400, detail="run_id mismatch")
    resp = apply_plan_decision(body)
    BUS.publish(run_id, "plan_decision_recorded", resp.model_dump(mode="json"))
    return resp.model_dump(mode="json")


@app.post("/api/runs/{run_id}/review-decision")
async def post_review_decision(run_id: str, body: ReviewDecisionBody) -> dict[str, Any]:
    if body.run_id != run_id:
        raise HTTPException(status_code=400, detail="run_id mismatch")
    resp = apply_review_decision(body)
    BUS.publish(run_id, "review_decision_recorded", resp.model_dump(mode="json"))
    return resp.model_dump(mode="json")
