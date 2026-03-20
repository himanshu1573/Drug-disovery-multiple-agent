import type { PlanDecisionStatus, ReviewDecisionStatus, Snapshot, SourceName } from "@/lib/types";

const ENV_API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL;
const API_BASE =
  (typeof ENV_API_BASE === "string" && ENV_API_BASE.trim().length > 0 ? ENV_API_BASE : null)?.replace(/\/+$/, "") ??
  (process.env.NODE_ENV === "development" ? "http://localhost:8000/api" : "/api");

async function readApiError(res: Response): Promise<string> {
  const contentType = res.headers.get("content-type") ?? "";
  let text = "";
  try {
    text = await res.text();
  } catch {
    // ignore
  }

  const looksLikeHtml =
    contentType.toLowerCase().includes("text/html") ||
    /<html[\s>]/i.test(text) ||
    text.includes("This page could not be found") ||
    text.includes("self.__next_f.push");

  if (looksLikeHtml) {
    return [
      `API request failed (${res.status} ${res.statusText || "error"}).`,
      "The frontend likely pointed at itself (e.g. using `/api` without a proxy).",
      "If you're running `docker compose up`, open the UI via `http://localhost` (nginx) instead of `http://localhost:3000`.",
      "If you're running the frontend directly, set `NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api` (and run the API).",
    ].join(" ");
  }

  const trimmed = text.trim();
  if (!trimmed) return `API request failed (${res.status} ${res.statusText || "error"}).`;
  return trimmed.length > 1200 ? `${trimmed.slice(0, 1200)}…` : trimmed;
}

export async function createRun(input: {
  gene_symbol: string;
  disease_id?: string;
  objective?: string;
  sources?: SourceName[];
  per_source_top_k?: number;
  max_literature_articles?: number;
  model_override?: string;
}): Promise<{ run_id: string; status: string }> {
  const res = await fetch(`${API_BASE}/runs`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export async function createRunFromText(input: {
  message: string;
  sources?: SourceName[];
  per_source_top_k?: number;
  max_literature_articles?: number;
  model_override?: string;
  run_id?: string;
}): Promise<{ run_id: string; status: string }> {
  const res = await fetch(`${API_BASE}/runs/from-text`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export async function postFollowup(runId: string, input: { message: string; urls?: string[] }): Promise<{ run_id: string; answer_markdown: string; used_urls: string[] }> {
  const res = await fetch(`${API_BASE}/runs/${encodeURIComponent(runId)}/followup`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export async function getState(runId: string): Promise<Snapshot> {
  const res = await fetch(`${API_BASE}/runs/${encodeURIComponent(runId)}/state`, {
    cache: "no-store",
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export async function postPlanDecision(input: {
  run_id: string;
  decision: PlanDecisionStatus;
  reviewer_id: string;
  reason?: string;
  updated_plan?: Record<string, unknown>;
}): Promise<unknown> {
  const res = await fetch(`${API_BASE}/runs/${encodeURIComponent(input.run_id)}/plan-decision`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export async function postReviewDecision(input: {
  run_id: string;
  decision: ReviewDecisionStatus;
  reviewer_id: string;
  reason?: string;
}): Promise<unknown> {
  const res = await fetch(`${API_BASE}/runs/${encodeURIComponent(input.run_id)}/review-decision`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export async function resumeRun(runId: string): Promise<{ run_id: string; status: string }> {
  const res = await fetch(`${API_BASE}/runs/${encodeURIComponent(runId)}/resume`, {
    method: "POST",
  });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}

export function eventsUrl(runId: string): string {
  return `${API_BASE}/runs/${encodeURIComponent(runId)}/events`;
}

export async function getArtifacts(runId: string): Promise<{ run_id: string; artifacts: Record<string, { path: string; exists: boolean; kind: string }> }> {
  const res = await fetch(`${API_BASE}/runs/${encodeURIComponent(runId)}/artifacts`, { cache: "no-store" });
  if (!res.ok) throw new Error(await readApiError(res));
  return res.json();
}
