"use client";

import { useEffect, useMemo, useState, type ReactNode } from "react";

import { AssistantToolUI, type SourceStep as UISourceStep } from "@/components/AssistantToolUI";
import { ChatComposer } from "@/components/ChatComposer";
import { MarkdownReport } from "@/components/MarkdownReport";
import { SourcesGrid } from "@/components/SourcesGrid";
import { PlanApprovalPanel } from "@/components/PlanApprovalPanel";
import { ReviewDecisionPanel } from "@/components/ReviewDecisionPanel";
import { useRunEvents } from "@/hooks/useRunEvents";
import { createRun, createRunFromText, postFollowup } from "@/lib/api";
import type { SourceName } from "@/lib/types";
import { Github } from "lucide-react";

const ALL_SOURCES: { key: SourceName; label: string }[] = [
  { key: "depmap", label: "DepMap" },
  { key: "pharos", label: "Pharos" },
  { key: "opentargets", label: "Open Targets" },
  { key: "literature", label: "Literature" },
];

const LS_HISTORY_KEY = "drugagent.history.v1";
const LS_LAST_RUN_KEY = "drugagent.last_run_id.v1";
const LS_FOLLOWUPS_PREFIX = "drugagent.followups.v1.";

function safeJsonParse<T>(raw: string | null): T | null {
  if (!raw) return null;
  try {
    return JSON.parse(raw) as T;
  } catch {
    return null;
  }
}

function getRunIdFromUrl(): string | null {
  try {
    const params = new URLSearchParams(window.location.search);
    const run = params.get("run");
    return run && run.trim() ? run.trim() : null;
  } catch {
    return null;
  }
}

function setRunIdInUrl(runId: string | null) {
  try {
    const url = new URL(window.location.href);
    if (runId) url.searchParams.set("run", runId);
    else url.searchParams.delete("run");
    window.history.replaceState({}, "", url.toString());
  } catch {
    // ignore
  }
}

function stageLabel(stage: string): string {
  switch (stage) {
    case "validate_input":
      return "Validating input";
    case "plan_collection":
      return "Planning collection";
    case "plan_review_gate":
      return "Waiting for plan approval";
    case "collect_sources_parallel":
      return "Searching sources";
    case "normalize_evidence":
      return "Normalizing evidence";
    case "verify_evidence":
      return "Verifying evidence";
    case "analyze_conflicts":
      return "Analyzing conflicts";
    case "build_evidence_graph":
      return "Building evidence graph";
    case "generate_explanation":
      return "Writing answer";
    case "human_review_gate":
      return "Waiting for final review";
    case "emit_dossier":
      return "Finalizing dossier";
    default:
      return stage.replaceAll("_", " ");
  }
}

type RunState = "idle" | "running" | "paused" | "completed" | "failed";

function deriveSourceSteps(log: Array<{ event: string; data: Record<string, unknown> }>, snapshot: any): UISourceStep[] {
  const steps: UISourceStep[] = [];
  const idx = new Map<string, number>();

  for (const it of log) {
    if (it.event !== "source_start" && it.event !== "source_end") continue;
    const source = String(it.data?.source ?? "");
    if (!source) continue;

    const currentIndex = idx.get(source);
    if (currentIndex === undefined) {
      idx.set(source, steps.length);
      steps.push({ source, status: "pending" });
    }
    const i = idx.get(source)!;

    if (it.event === "source_start") {
      steps[i] = { ...steps[i], status: "running" };
    } else {
      const rawStatus = String(it.data?.status ?? "success").toLowerCase();
      const mapped: UISourceStep["status"] =
        rawStatus === "success"
          ? "success"
          : rawStatus === "partial"
            ? "partial"
            : rawStatus === "skipped"
              ? "skipped"
              : "failed";
      const rc = typeof it.data?.record_count === "number" ? it.data.record_count : Number(it.data?.record_count ?? NaN);
      steps[i] = { ...steps[i], status: mapped, recordCount: Number.isFinite(rc) ? rc : undefined };
    }
  }

  if (steps.length) return steps;

  const fromSnapshot: any[] = Array.isArray(snapshot?.values?.source_status) ? snapshot.values.source_status : [];
  for (const s of fromSnapshot) {
    const source = typeof s?.source === "string" ? s.source : null;
    const rawStatus = typeof s?.status === "string" ? s.status.toLowerCase() : null;
    if (!source || !rawStatus) continue;
    const mapped: UISourceStep["status"] =
      rawStatus === "success"
        ? "success"
        : rawStatus === "partial"
          ? "partial"
          : rawStatus === "skipped"
            ? "skipped"
            : "failed";
    steps.push({
      source,
      status: mapped,
      recordCount: typeof s?.record_count === "number" ? s.record_count : undefined,
    });
  }
  return steps;
}

function deriveCurrentStage(log: Array<{ event: string; data: Record<string, unknown> }>): string | null {
  let current: string | null = null;
  for (const it of log) {
    if (it.event === "stage_start") current = String(it.data?.stage ?? "") || current;
    if (it.event === "stage_end" && current && String(it.data?.stage ?? "") === current) current = null;
    if (it.event === "stage_error") return String(it.data?.stage ?? "") || current;
  }
  return current;
}

function readString(value: unknown): string | null {
  return typeof value === "string" && value.trim().length > 0 ? value : null;
}

function answerFromSnapshot(snapshot: any): string | null {
  const explanation = readString(snapshot?.values?.explanation);
  const dossierSummary = readString(snapshot?.values?.final_dossier?.summary_markdown);
  return dossierSummary ?? explanation;
}

function queryTitleFromSnapshot(snapshot: any, runId: string | null, history: any[]): { title: string; gene: string | null } {
  const q = snapshot?.values?.query ?? null;
  const gene = typeof q?.gene_symbol === "string" && q.gene_symbol.trim() ? q.gene_symbol.trim() : null;
  const objective = typeof q?.objective === "string" && q.objective.trim() ? q.objective.trim() : null;
  if (objective) return { title: objective, gene };
  if (gene) return { title: `Research: ${gene}${q?.disease_id ? ` / ${q.disease_id}` : ""}`, gene };

  if (runId) {
    const h = history.find((it) => it.runId === runId);
    if (h) return { title: h.title, gene: h.gene || null };
  }

  return { title: "New thread", gene };
}

function tabButton(active: boolean): string {
  return active
    ? "text-neutral-100 border-b border-neutral-200"
    : "text-neutral-400 hover:text-neutral-200 border-b border-transparent";
}

export default function Page() {
  const [runId, setRunId] = useState<string | null>(null);
  const [reviewerId, setReviewerId] = useState<string>("user@example.com");
  const [history, setHistory] = useState<Array<{ runId: string; startedAt: number; title: string; gene: string }>>([]);
  const [activeTab, setActiveTab] = useState<"answer" | "links" | "images">("answer");

  const { log, paused, failed, completed, snapshot } = useRunEvents(runId);

  // Restore state on load:
  // - prefer URL `?run=<id>` (shareable)
  // - else restore last selected run id from localStorage
  // - restore sidebar history from localStorage
  useEffect(() => {
    const restoredHistory =
      safeJsonParse<Array<{ runId: string; startedAt: number; title: string; gene: string }>>(localStorage.getItem(LS_HISTORY_KEY)) ?? [];
    if (Array.isArray(restoredHistory)) setHistory(restoredHistory.slice(0, 50));

    const urlRun = getRunIdFromUrl();
    const lastRun = (localStorage.getItem(LS_LAST_RUN_KEY) ?? "").trim() || null;
    const initial = urlRun ?? lastRun;
    if (initial) setRunId(initial);
  }, []);

  // Persist history for thread continuity across refresh.
  useEffect(() => {
    try {
      localStorage.setItem(LS_HISTORY_KEY, JSON.stringify(history.slice(0, 50)));
    } catch {
      // ignore
    }
  }, [history]);

  // Persist current run selection in URL + localStorage to prevent accidental "new threads".
  useEffect(() => {
    setRunIdInUrl(runId);
    try {
      if (runId) localStorage.setItem(LS_LAST_RUN_KEY, runId);
      else localStorage.removeItem(LS_LAST_RUN_KEY);
    } catch {
      // ignore
    }
  }, [runId]);

  const { title: queryTitle, gene: activeGene } = useMemo(() => queryTitleFromSnapshot(snapshot, runId, history), [snapshot, runId, history]);
  const currentStage = useMemo(() => deriveCurrentStage(log), [log]);
  const sourceSteps = useMemo(() => deriveSourceSteps(log, snapshot), [log, snapshot]);
  const runState: RunState = failed ? "failed" : completed ? "completed" : paused ? "paused" : runId ? "running" : "idle";

  const rerunFromSnapshot = async (overrides: {
    objective?: string;
    sources?: SourceName[];
    per_source_top_k?: number;
    max_literature_articles?: number;
  }) => {
    const q = (snapshot?.values?.query as any) ?? {};
    const gene = activeGene ?? history.find((h) => h.runId === runId)?.gene ?? (typeof q.gene_symbol === "string" ? q.gene_symbol : "KRAS");
    const objective =
      overrides.objective ??
      (typeof q.objective === "string" && q.objective.trim() ? q.objective.trim() : queryTitle || `Research: ${gene}`);
    const sources =
      overrides.sources ??
      (Array.isArray(q.sources) ? (q.sources as SourceName[]) : ALL_SOURCES.map((s) => s.key));

    const baseTopK = Number.isFinite(Number(q.per_source_top_k)) ? Number(q.per_source_top_k) : 5;
    const baseLit = Number.isFinite(Number(q.max_literature_articles)) ? Number(q.max_literature_articles) : 5;

    await startRun({
      gene_symbol: gene,
      objective,
      disease_id: typeof q.disease_id === "string" ? q.disease_id : undefined,
      sources,
      per_source_top_k: overrides.per_source_top_k ?? baseTopK,
      max_literature_articles: overrides.max_literature_articles ?? baseLit,
    });
  };

  const onMoreEvidence = async () => {
    const q = (snapshot?.values?.query as any) ?? {};
    const baseTopK = Number.isFinite(Number(q.per_source_top_k)) ? Number(q.per_source_top_k) : 5;
    const baseLit = Number.isFinite(Number(q.max_literature_articles)) ? Number(q.max_literature_articles) : 5;
    await rerunFromSnapshot({
      per_source_top_k: Math.min(20, baseTopK + 5),
      max_literature_articles: Math.min(20, baseLit + 5),
    });
  };

  const onAllSources = async () => {
    await rerunFromSnapshot({ sources: ALL_SOURCES.map((s) => s.key) });
  };

  const onTightenObjective = async () => {
    const q = (snapshot?.values?.query as any) ?? {};
    const gene = activeGene ?? history.find((h) => h.runId === runId)?.gene ?? (typeof q.gene_symbol === "string" ? q.gene_symbol : "this target");
    await rerunFromSnapshot({
      objective: `Therapeutic target assessment for ${gene}: tractability, dependency, and disease relevance`,
    });
  };

  const startNewThread = () => {
    setRunId(null);
    setActiveTab("answer");
  };

  const startRun = async (input: {
    gene_symbol: string;
    objective?: string;
    disease_id?: string;
    sources: SourceName[];
    per_source_top_k?: number;
    max_literature_articles?: number;
  }) => {
    const resp = await createRun({
      gene_symbol: input.gene_symbol.trim(),
      objective: input.objective?.trim() || undefined,
      disease_id: input.disease_id?.trim() || undefined,
      sources: input.sources,
      per_source_top_k: input.per_source_top_k,
      max_literature_articles: input.max_literature_articles,
    });
    setRunId(resp.run_id);
    setHistory((prev) => [{ runId: resp.run_id, startedAt: Date.now(), title: input.objective?.trim() || `Research: ${input.gene_symbol.trim()}`, gene: input.gene_symbol.trim() }, ...prev].slice(0, 50));
  };

  const startRunFromText = async (input: {
    message: string;
    sources: SourceName[];
    per_source_top_k?: number;
    max_literature_articles?: number;
  }) => {
    const resp = await createRunFromText({
      message: input.message.trim(),
      sources: input.sources,
      per_source_top_k: input.per_source_top_k,
      max_literature_articles: input.max_literature_articles,
    });
    setRunId(resp.run_id);
    setHistory((prev) => [{ runId: resp.run_id, startedAt: Date.now(), title: input.message.trim(), gene: "" }, ...prev].slice(0, 50));
  };

  const gatePanel = useMemo(() => {
    if (!runId) return null;
    if (paused?.reason === "plan_approval_required") {
      return <PlanApprovalPanel runId={runId} snapshot={snapshot} reviewerId={reviewerId} />;
    }
    if (paused?.reason === "human_review_required") {
      return <ReviewDecisionPanel runId={runId} snapshot={snapshot} reviewerId={reviewerId} />;
    }
    return null;
  }, [paused?.reason, reviewerId, runId, snapshot]);

  const showGate = Boolean(gatePanel);

  return (
    <div className="flex h-screen bg-neutral-950 text-neutral-100">
      <aside className="hidden w-72 flex-col border-r border-white/10 bg-neutral-950/60 p-3 md:flex">
        <div className="flex items-center gap-2 px-2 py-2">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-white/10 text-xs font-semibold text-white">
            DA
          </div>
          <div className="flex flex-col leading-tight">
            <div className="text-sm font-semibold text-neutral-100">Drugagent</div>
            <div className="text-xs text-neutral-500">Search</div>
          </div>
        </div>


        <button onClick={startNewThread} className="mt-3 w-full rounded-xl bg-white px-4 py-2 text-sm font-medium text-neutral-900">
          + New Thread
        </button>

        <div className="mt-4 px-2 text-xs font-semibold text-neutral-500">Threads</div>
        <div className="mt-2 flex-1 overflow-auto px-1">
          <ul className="flex flex-col gap-1">
            {history.length ? (
              history.map((h) => (
                <li key={h.runId}>
                  <button
                    className={`w-full rounded-xl px-3 py-2 text-left text-sm ${
                      h.runId === runId ? "bg-white/10 text-neutral-100" : "text-neutral-300 hover:bg-white/5"
                    }`}
                    onClick={() => setRunId(h.runId)}
                  >
                    <div className="truncate">{h.title}</div>
                    <div className="mt-0.5 text-[11px] text-neutral-500">{new Date(h.startedAt).toLocaleString()}</div>
                  </button>
                </li>
              ))
            ) : (
              <li className="px-3 py-2 text-sm text-neutral-500">No threads yet</li>
            )}
          </ul>
        </div>

        <div className="mt-auto border-t border-white/10 px-2 pt-3 pb-3">
          <a
            href="https://github.com/himanshu1573"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-2 text-[11px] font-medium text-neutral-400 hover:text-neutral-200"
          >
            <span>
              Simple built by <span className="font-semibold text-neutral-200">Himanshu Prajapati</span>
              <span className="ml-1 text-neutral-300" aria-label="love">
                ♥
              </span>
            </span>
          </a>
        </div>

        <div className="border-t border-white/10 px-2 pt-3">
          <div className="text-[11px] text-neutral-600">Run mode: {runState} • Sources: one-by-one</div>
        </div>
      </aside>

      <main className="flex min-w-0 flex-1 flex-col">
        {!runId ? (
          <HomeView
            onStart={startRun}
            onStartFromText={startRunFromText}
            initialGene="KRAS"
            initialSources={ALL_SOURCES.map((s) => s.key)}
          />
        ) : (
          <RunView
            runId={runId}
            activeTab={activeTab}
            onTab={setActiveTab}
            queryTitle={queryTitle}
            runState={runState}
            currentStage={currentStage}
            sourceSteps={sourceSteps}
            log={log}
            failed={failed}
            snapshot={snapshot}
            showGate={showGate}
            gatePanel={gatePanel}
            onMoreEvidence={() => void onMoreEvidence()}
            onAllSources={() => void onAllSources()}
            onTightenObjective={() => void onTightenObjective()}
            onFollowup={async (message) => {
              const resp = await postFollowup(runId, { message });
              return resp.answer_markdown;
            }}
          />
        )}
      </main>
    </div>
  );
}

function HomeView({
  onStart,
  onStartFromText,
  initialGene,
  initialSources,
}: {
  onStart: (input: { gene_symbol: string; objective?: string; disease_id?: string; sources: SourceName[]; per_source_top_k?: number; max_literature_articles?: number }) => Promise<void>;
  onStartFromText: (input: { message: string; sources: SourceName[]; per_source_top_k?: number; max_literature_articles?: number }) => Promise<void>;
  initialGene: string;
  initialSources: SourceName[];
}) {
  const [gene, setGene] = useState(initialGene);
  const [objective, setObjective] = useState("");
  const [sources, setSources] = useState<Set<SourceName>>(new Set(initialSources));
  const [advancedOpen, setAdvancedOpen] = useState(false);
  const [perSourceTopK, setPerSourceTopK] = useState(5);
  const [maxLiterature, setMaxLiterature] = useState(5);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const toggle = (key: SourceName) => {
    setSources((prev) => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const submit = async () => {
    setBusy(true);
    setError(null);
    try {
      const trimmedGene = gene.trim();
      const trimmedObjective = objective.trim();

      if (trimmedGene && trimmedObjective) {
        await onStart({
          gene_symbol: trimmedGene,
          objective: trimmedObjective,
          sources: Array.from(sources),
          per_source_top_k: perSourceTopK,
          max_literature_articles: maxLiterature,
        });
      } else if (trimmedGene) {
        await onStart({
          gene_symbol: trimmedGene,
          sources: Array.from(sources),
          per_source_top_k: perSourceTopK,
          max_literature_articles: maxLiterature,
        });
      } else if (trimmedObjective) {
        await onStartFromText({
          message: trimmedObjective,
          sources: Array.from(sources),
          per_source_top_k: perSourceTopK,
          max_literature_articles: maxLiterature,
        });
      }
      setObjective("");
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to start run");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="flex h-full flex-col items-center justify-center px-6">
      <div className="text-center">
        <div className="text-5xl font-semibold tracking-tight text-neutral-100">Drugagent</div>
        <div className="mt-2 text-sm text-neutral-400">Clean research UI • sequential agents • evidence-first answers</div>
      </div>

      <div className="mt-10 w-full max-w-3xl">
        <div className="mt-8 rounded-3xl border border-white/10 bg-white/5 p-6 shadow-2xl">
          <div className="flex flex-col gap-6 md:flex-row items-end">
            <div className="flex-1 w-full">
              <div className="text-[11px] font-bold text-neutral-500 uppercase tracking-widest mb-2 ml-1">Gene Symbol</div>
              <input
                value={gene}
                onChange={(e) => setGene(e.target.value)}
                className="w-full rounded-2xl border border-white/10 bg-neutral-900/50 px-4 py-3 text-sm text-neutral-100 placeholder:text-neutral-500 focus:border-white/20 focus:bg-neutral-900/80 outline-none transition-all"
                placeholder="Enter gene (e.g. KRAS)"
              />
            </div>

            <div className="hidden md:block pb-3 px-2 text-[10px] font-black text-neutral-600">OR</div>

            <div className="flex-[2] w-full">
              <div className="text-[11px] font-bold text-neutral-500 uppercase tracking-widest mb-2 ml-1">Research Objective / Query</div>
              <input
                value={objective}
                onChange={(e) => setObjective(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault();
                    if (!busy) submit();
                  }
                }}
                className="w-full rounded-2xl border border-white/10 bg-neutral-900/50 px-4 py-3 text-sm text-neutral-100 placeholder:text-neutral-500 focus:border-white/20 focus:bg-neutral-900/80 outline-none transition-all"
                placeholder="Enter search query or detailed objective"
              />
            </div>

            <button
              onClick={submit}
              disabled={busy || (gene.trim().length === 0 && objective.trim().length === 0)}
              className="h-[46px] w-full md:w-auto rounded-2xl bg-white px-8 text-sm font-bold text-neutral-900 hover:bg-neutral-200 transition-colors disabled:opacity-30 disabled:cursor-not-allowed"
            >
              {busy ? "..." : "Search"}
            </button>
          </div>

        <div className="mt-4 flex flex-wrap gap-2">
          {ALL_SOURCES.map((s) => (
            <button
              key={s.key}
              type="button"
              onClick={() => toggle(s.key)}
              className={`rounded-full border px-3 py-1 text-xs ${
                sources.has(s.key) ? "border-white/20 bg-white/10 text-neutral-100" : "border-white/10 bg-transparent text-neutral-400 hover:bg-white/5"
              }`}
            >
              {s.label}
            </button>
          ))}
        </div>

        <div className="mt-4">
          <button
            type="button"
            onClick={() => setAdvancedOpen((v) => !v)}
            className="text-xs font-medium text-neutral-400 hover:text-neutral-200"
          >
            {advancedOpen ? "Hide advanced" : "Show advanced"}
          </button>
          {advancedOpen ? (
            <div className="mt-3 grid grid-cols-1 gap-3 sm:grid-cols-2">
              <label className="flex flex-col gap-1">
                <span className="text-[11px] font-semibold text-neutral-500">Per-source top K</span>
                <input
                  type="number"
                  min={1}
                  max={20}
                  value={perSourceTopK}
                  onChange={(e) => setPerSourceTopK(Number(e.target.value))}
                  className="mt-1 w-full rounded-xl border border-white/10 bg-neutral-950/40 px-3 py-2 text-sm text-neutral-100"
                />
              </label>
              <label className="flex flex-col gap-1">
                <span className="text-[11px] font-semibold text-neutral-500">Max literature articles</span>
                <input
                  type="number"
                  min={1}
                  max={20}
                  value={maxLiterature}
                  onChange={(e) => setMaxLiterature(Number(e.target.value))}
                  className="mt-1 w-full rounded-xl border border-white/10 bg-neutral-950/40 px-3 py-2 text-sm text-neutral-100"
                />
              </label>
            </div>
          ) : null}
        </div>

        {error ? <div className="mt-3 text-sm text-red-300">{error}</div> : null}
      </div>

        <div className="mt-6 flex flex-wrap justify-center gap-2">
          {[
            "Mutation impact",
            "Drug resistance",
            "Target tractability",
            "Biomarkers",
            "Mechanism of action",
          ].map((chip) => (
            <button
              key={chip}
              type="button"
              className="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-neutral-300 hover:bg-white/10"
              onClick={() => setObjective(chip)}
            >
              {chip}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

function RunView({
  runId,
  activeTab,
  onTab,
  queryTitle,
  runState,
  currentStage,
  sourceSteps,
  log,
  failed,
  snapshot,
  showGate,
  gatePanel,
  onFollowup,
  onMoreEvidence,
  onAllSources,
  onTightenObjective,
}: {
  runId: string;
  activeTab: "answer" | "links" | "images";
  onTab: (t: "answer" | "links" | "images") => void;
  queryTitle: string;
  runState: RunState;
  currentStage: string | null;
  sourceSteps: UISourceStep[];
  log: Array<{ ts: number; event: string; data: Record<string, unknown> }>;
  failed: string | null;
  snapshot: any;
  showGate: boolean;
  gatePanel: ReactNode;
  onFollowup: (message: string) => Promise<string>;
  onMoreEvidence: () => void;
  onAllSources: () => void;
  onTightenObjective: () => void;
}) {
  const [followupBusy, setFollowupBusy] = useState(false);
  const [followups, setFollowups] = useState<Array<{ q: string; a: string }>>([]);
  const answer = useMemo(() => answerFromSnapshot(snapshot), [snapshot]);
  const followupEnabled = Boolean(answer && answer.trim().length > 0);

  // Restore and persist follow-ups per run.
  useEffect(() => {
    try {
      const restored = safeJsonParse<Array<{ q: string; a: string }>>(localStorage.getItem(`${LS_FOLLOWUPS_PREFIX}${runId}`));
      setFollowups(Array.isArray(restored) ? restored : []);
    } catch {
      setFollowups([]);
    }
  }, [runId]);

  useEffect(() => {
    try {
      localStorage.setItem(`${LS_FOLLOWUPS_PREFIX}${runId}`, JSON.stringify(followups.slice(-50)));
    } catch {
      // ignore
    }
  }, [followups, runId]);

  return (
    <div className="relative flex h-full flex-col">
      <div className="flex items-center justify-between border-b border-white/10 px-6 py-4">
        <div className="flex items-center gap-6 text-sm">
          <button className={tabButton(activeTab === "answer")} onClick={() => onTab("answer")}>
            Answer
          </button>
          <button className={tabButton(activeTab === "links")} onClick={() => onTab("links")}>
            Links
          </button>
          <button className={tabButton(activeTab === "images")} onClick={() => onTab("images")}>
            Images
          </button>
          <span className="ml-2 rounded-full border border-white/10 bg-white/5 px-2 py-0.5 text-[11px] text-neutral-300">
            {runState}
          </span>
        </div>

        <div className="flex items-center gap-4">
          <a
            href="https://github.com/himanshu1573/Drug-disovery-multiple-agent.git"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-xl border border-white/10 bg-white/5 p-2 text-neutral-200 hover:bg-white/10"
            title="View Source Code"
          >
            <Github className="h-5 w-5" />
          </a>
        </div>
      </div>

      <div className="flex-1 overflow-auto px-6 py-6 pb-32">
        <div className="flex w-full flex-col gap-6">
          {queryTitle && queryTitle !== "New thread" ? (
            <div className="ml-auto w-full rounded-2xl bg-white/5 px-4 py-3 text-sm text-neutral-100">
              {queryTitle}
            </div>
          ) : null}

          {failed ? (
            <div className="rounded-2xl border border-red-500/30 bg-red-500/10 p-4 text-sm text-red-200">
              <div className="font-semibold">Run failed</div>
              <pre className="mt-2 whitespace-pre-wrap break-words text-xs">{failed}</pre>
            </div>
          ) : null}

          {activeTab === "answer" ? (
            <>
              <AssistantToolUI
                runState={runState}
                currentStage={currentStage}
                log={log}
                snapshot={snapshot}
                sourceSteps={sourceSteps}
                answer={answer}
                sourcesUI={<SourcesGrid snapshot={snapshot} variant="strip" hideWhenEmpty />}
                onMoreEvidence={onMoreEvidence}
                onAllSources={onAllSources}
                onTightenObjective={onTightenObjective}
              />

              {followups.length ? (
                <div className="rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-neutral-100">
                  <div className="text-xs font-semibold text-neutral-300">Follow-ups</div>
                  <div className="mt-3 flex flex-col gap-6">
                    {followups.map((f, i) => (
                      <div
                        key={`${i}-${f.q.slice(0, 12)}`}
                        className="rounded-2xl border border-white/10 bg-neutral-950/20 p-4"
                      >
                        <div className="text-xs font-semibold text-neutral-300">Question</div>
                        <div className="mt-2 text-sm text-neutral-100/90">{f.q}</div>
                        <div className="mt-4 text-xs font-semibold text-neutral-300">Answer</div>
                        <MarkdownReport markdown={f.a} defaultMode="rendered" />
                      </div>
                    ))}
                  </div>
                </div>
              ) : null}
            </>
          ) : null}

          {activeTab === "links" ? <SourcesGrid snapshot={snapshot} variant="grid" /> : null}

          {activeTab === "images" ? (
            <div className="rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-neutral-400">
              Images view is not available yet.
            </div>
          ) : null}

        </div>
      </div>

      <div className="absolute bottom-6 left-1/2 w-[min(52rem,calc(100%-3rem))] -translate-x-1/2 px-1">
        <ChatComposer
          disabled={followupBusy || !followupEnabled}
          placeholder={followupEnabled ? "Ask a follow-up" : "Follow-up is available after the report is generated"}
          onSend={async (message) => {
            setFollowupBusy(true);
            try {
              const answer = await onFollowup(message);
              setFollowups((prev) => [...prev, { q: message, a: answer }]);
            } finally {
              setFollowupBusy(false);
            }
          }}
        />
      </div>

      {showGate ? (
        <div className="absolute inset-0 flex items-center justify-center bg-neutral-950/80 p-6 backdrop-blur-sm">
          <div className="w-full max-w-3xl">{gatePanel}</div>
        </div>
      ) : null}
    </div>
  );
}
