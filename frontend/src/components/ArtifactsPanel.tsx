"use client";

import { useEffect, useState } from "react";

import { getArtifacts } from "@/lib/api";

type ArtifactMeta = { path: string; exists: boolean; kind: string };

function badge(exists: boolean) {
  return exists
    ? "bg-emerald-100 text-emerald-800 border-emerald-200"
    : "bg-slate-100 text-slate-700 border-slate-200";
}

export function ArtifactsPanel({ runId }: { runId: string }) {
  const [artifacts, setArtifacts] = useState<Record<string, ArtifactMeta> | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let alive = true;
    setArtifacts(null);
    setError(null);

    const refresh = () => {
      getArtifacts(runId)
        .then((resp) => {
          if (!alive) return;
          setArtifacts(resp.artifacts);
          setError(null);
        })
        .catch((e) => {
          if (!alive) return;
          setError(e instanceof Error ? e.message : "Failed to load artifacts");
        });
    };

    refresh();
    const t = setInterval(refresh, 2500);
    return () => {
      alive = false;
      clearInterval(t);
    };
  }, [runId]);

  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4">
      <div className="mb-2 flex items-center justify-between">
        <h2 className="text-sm font-semibold text-slate-900">Artifacts / Memory</h2>
        <span className="text-xs text-slate-500 font-mono">{runId}</span>
      </div>
      {error ? <div className="text-sm text-red-600">{error}</div> : null}
      {!artifacts && !error ? <div className="text-sm text-slate-600">Loading…</div> : null}
      {artifacts ? (
        <ul className="mt-2 flex flex-col gap-2 text-xs">
          {[
            ["plan", "Plan (collection_plan)"],
            ["procedural_memory", "Procedural memory"],
            ["working_memory", "Working memory snapshots"],
            ["dossier", "Final dossier"],
            ["graph", "Evidence graph snapshot"],
            ["episodic_memory_runs", "Episodic memory (runs.json)"],
          ].map(([key, label]) => {
            const meta = artifacts[key] ?? null;
            return (
              <li key={key} className="flex items-start justify-between gap-3 rounded border border-slate-100 bg-slate-50 p-2">
                <div className="flex flex-col gap-1">
                  <div className="text-slate-900">{label}</div>
                  {meta ? <div className="font-mono text-slate-500 break-all">{meta.path}</div> : <div className="text-slate-500">Missing</div>}
                </div>
                <span className={`h-fit rounded-full border px-2 py-0.5 text-[11px] ${badge(Boolean(meta?.exists))}`}>
                  {meta?.exists ? "exists" : "missing"}
                </span>
              </li>
            );
          })}
        </ul>
      ) : null}
    </div>
  );
}
