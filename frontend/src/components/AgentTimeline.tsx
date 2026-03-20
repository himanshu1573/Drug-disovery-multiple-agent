"use client";

import { useMemo } from "react";

type LogItem = { ts: number; event: string; data: Record<string, unknown> };

type StageStatus = "pending" | "running" | "success" | "error";

const STAGE_ORDER = [
  "validate_input",
  "plan_collection",
  "plan_review_gate",
  "collect_sources_parallel",
  "normalize_evidence",
  "verify_evidence",
  "analyze_conflicts",
  "assess_sufficiency",
  "build_evidence_graph",
  "generate_explanation",
  "supervisor_decide",
  "prepare_review_brief",
  "human_review_gate",
  "emit_dossier",
] as const;

function stageLabel(stage: string): string {
  return stage.replaceAll("_", " ");
}

function pillClass(status: StageStatus): string {
  switch (status) {
    case "success":
      return "bg-emerald-100 text-emerald-800 border-emerald-200";
    case "running":
      return "bg-sky-100 text-sky-800 border-sky-200";
    case "error":
      return "bg-red-100 text-red-800 border-red-200";
    default:
      return "bg-slate-100 text-slate-700 border-slate-200";
  }
}

export function AgentTimeline({ items }: { items: LogItem[] }) {
  const derived = useMemo(() => {
    const stageStart: Record<string, number> = {};
    const stageEnd: Record<string, { ts: number; durationMs?: number; update?: unknown }> = {};
    const stageError: Record<string, { ts: number; error?: string }> = {};

    const agentByStage: Record<string, { agent_name?: string; summary?: string; model_used?: string | null; generation_mode?: string | null }> =
      {};
    const decisionByStage: Record<string, { action?: string; rationale?: string; decision_mode?: string; model_used?: string | null }> = {};

    const sourceEvents: { ts: number; source: string; kind: "start" | "end"; data: Record<string, unknown> }[] = [];

    for (const it of items) {
      const d = it.data ?? {};
      if (it.event === "stage_start") {
        const stage = String(d.stage ?? "");
        if (stage) stageStart[stage] = it.ts;
      }
      if (it.event === "stage_end") {
        const stage = String(d.stage ?? "");
        if (stage) stageEnd[stage] = { ts: it.ts, durationMs: Number(d.duration_ms ?? NaN), update: d.update };
      }
      if (it.event === "stage_error") {
        const stage = String(d.stage ?? "");
        if (stage) stageError[stage] = { ts: it.ts, error: typeof d.error === "string" ? d.error : undefined };
      }
      if (it.event === "agent_report") {
        const stage = String(d.stage_name ?? "");
        if (stage) {
          agentByStage[stage] = {
            agent_name: typeof d.agent_name === "string" ? d.agent_name : undefined,
            summary: typeof d.summary === "string" ? d.summary : undefined,
            model_used: typeof d.model_used === "string" ? d.model_used : null,
            generation_mode: typeof d.generation_mode === "string" ? d.generation_mode : null,
          };
        }
      }
      if (it.event === "agent_decision") {
        const stage = String(d.stage_name ?? "");
        if (stage) {
          decisionByStage[stage] = {
            action: typeof d.action === "string" ? d.action : undefined,
            rationale: typeof d.rationale === "string" ? d.rationale : undefined,
            decision_mode: typeof d.decision_mode === "string" ? d.decision_mode : undefined,
            model_used: typeof d.model_used === "string" ? d.model_used : null,
          };
        }
      }
      if (it.event === "source_start" || it.event === "source_end") {
        const source = String(d.source ?? "");
        if (source) {
          sourceEvents.push({
            ts: it.ts,
            source,
            kind: it.event === "source_start" ? "start" : "end",
            data: d,
          });
        }
      }
    }

    const stages = STAGE_ORDER.map((stage) => {
      let status: StageStatus = "pending";
      if (stageError[stage]) status = "error";
      else if (stageEnd[stage]) status = "success";
      else if (stageStart[stage]) status = "running";

      const durationMs = stageEnd[stage]?.durationMs;
      const durationLabel = Number.isFinite(durationMs) ? `${Math.round(durationMs!)}ms` : null;

      return {
        stage,
        status,
        startedAt: stageStart[stage] ?? null,
        endedAt: stageEnd[stage]?.ts ?? null,
        durationLabel,
        update: stageEnd[stage]?.update ?? null,
        error: stageError[stage]?.error ?? null,
        agent: agentByStage[stage] ?? null,
        decision: decisionByStage[stage] ?? null,
      };
    });

    return { stages, sourceEvents };
  }, [items]);

  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="text-sm font-semibold text-slate-900">Agent flow</h2>
        <span className="text-xs text-slate-500">{derived.stages.filter((s) => s.status !== "pending").length}/{STAGE_ORDER.length} stages</span>
      </div>

      <ol className="flex flex-col gap-2">
        {derived.stages.map((s) => (
          <li key={s.stage} className="rounded-md border border-slate-200 bg-white p-3">
            <div className="flex items-start justify-between gap-3">
              <div className="flex flex-col gap-1">
                <div className="flex items-center gap-2">
                  <span className={`rounded-full border px-2 py-0.5 text-xs font-medium ${pillClass(s.status)}`}>
                    {s.status}
                  </span>
                  <span className="text-sm font-semibold text-slate-900">{stageLabel(s.stage)}</span>
                  {s.durationLabel ? <span className="text-xs text-slate-500">{s.durationLabel}</span> : null}
                </div>

                {s.agent ? (
                  <div className="text-xs text-slate-700">
                    <span className="font-mono">{s.agent.agent_name ?? "agent"}</span>
                    {s.agent.generation_mode ? (
                      <span className="text-slate-500"> [{s.agent.generation_mode}{s.agent.model_used ? `:${s.agent.model_used}` : ""}]</span>
                    ) : null}
                    {s.agent.summary ? <div className="mt-1 text-slate-700">{s.agent.summary}</div> : null}
                  </div>
                ) : null}

                {s.decision ? (
                  <div className="text-xs text-slate-700">
                    <span className="font-mono">supervisor_agent</span>
                    {s.decision.decision_mode ? (
                      <span className="text-slate-500"> [{s.decision.decision_mode}{s.decision.model_used ? `:${s.decision.model_used}` : ""}]</span>
                    ) : null}
                    {s.decision.action ? <div className="mt-1"><span className="font-medium">action:</span> {s.decision.action}</div> : null}
                    {s.decision.rationale ? <div className="mt-1 text-slate-700">{s.decision.rationale}</div> : null}
                  </div>
                ) : null}

                {s.stage === "collect_sources_parallel" && derived.sourceEvents.length ? (
                  <div className="mt-2 rounded border border-slate-100 bg-slate-50 p-2 text-xs text-slate-700">
                    <div className="mb-1 text-slate-500">Sources</div>
                    <ul className="flex flex-col gap-1">
                      {derived.sourceEvents.slice(-8).map((ev, idx) => (
                        <li key={`${ev.ts}-${idx}`} className="flex items-center justify-between gap-2">
                          <span className="font-mono">{ev.source}</span>
                          <span className="text-slate-600">
                            {ev.kind === "start" ? "start" : `end (${String(ev.data.status ?? "ok")}, ${String(ev.data.record_count ?? "?")} records)`}
                          </span>
                        </li>
                      ))}
                    </ul>
                  </div>
                ) : null}

                {s.error ? (
                  <div className="mt-2 rounded border border-red-200 bg-red-50 p-2 text-xs text-red-800 whitespace-pre-wrap break-words">
                    {s.error}
                  </div>
                ) : null}
              </div>

              <div className="text-right text-xs text-slate-500">
                {s.startedAt ? <div>start {new Date(s.startedAt).toLocaleTimeString()}</div> : null}
                {s.endedAt ? <div>end {new Date(s.endedAt).toLocaleTimeString()}</div> : null}
              </div>
            </div>
          </li>
        ))}
      </ol>
    </div>
  );
}
