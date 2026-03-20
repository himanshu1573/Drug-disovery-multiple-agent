"use client";

import { useEffect, useMemo, useRef, useState } from "react";

import { eventsUrl, getState } from "@/lib/api";
import type { Snapshot } from "@/lib/types";

type LogItem = { ts: number; event: string; data: Record<string, unknown> };

export function useRunEvents(runId: string | null) {
  const [log, setLog] = useState<LogItem[]>([]);
  const [paused, setPaused] = useState<{ reason: string; nextStages: string[] } | null>(null);
  const [failed, setFailed] = useState<string | null>(null);
  const [completed, setCompleted] = useState<boolean>(false);
  const [snapshot, setSnapshot] = useState<Snapshot | null>(null);
  const esRef = useRef<EventSource | null>(null);

  const url = useMemo(() => (runId ? eventsUrl(runId) : null), [runId]);

  useEffect(() => {
    setLog([]);
    setPaused(null);
    setFailed(null);
    setCompleted(false);
    setSnapshot(null);

    if (!url || !runId) return;

    const es = new EventSource(url);
    esRef.current = es;

    const onAny = (eventName: string) => (evt: MessageEvent) => {
      let data: Record<string, unknown> = {};
      try {
        data = JSON.parse(evt.data ?? "{}");
      } catch {
        data = { raw: evt.data };
      }
      const ts = typeof data._ts_ms === "number" ? data._ts_ms : Date.now();
      setLog((prev) => [...prev.slice(-499), { ts, event: eventName, data }]);
    };

    es.addEventListener("connected", onAny("connected"));
    es.addEventListener("run_status", (evt) => {
      try {
        const data = JSON.parse(evt.data ?? "{}") as { status?: string };
        const status = String(data.status ?? "").toLowerCase();
        if (status && status !== "paused") setPaused(null);
      } catch {
        // ignore
      }
      onAny("run_status")(evt);
    });
    es.addEventListener("stage_start", (evt) => {
      // Clear any pause overlay as soon as the workflow resumes.
      setPaused(null);
      onAny("stage_start")(evt);
    });
    es.addEventListener("stage_end", onAny("stage_end"));
    es.addEventListener("stage_error", onAny("stage_error"));
    es.addEventListener("agent_report", onAny("agent_report"));
    es.addEventListener("agent_decision", onAny("agent_decision"));
    es.addEventListener("source_start", onAny("source_start"));
    es.addEventListener("source_end", onAny("source_end"));
    es.addEventListener("edge", onAny("edge"));
    es.addEventListener("workflow_paused", onAny("workflow_paused"));
    es.addEventListener("plan_decision_recorded", onAny("plan_decision_recorded"));
    es.addEventListener("review_decision_recorded", onAny("review_decision_recorded"));
    es.addEventListener("run_paused", async (evt) => {
      const data = JSON.parse(evt.data ?? "{}") as { reason?: string; next_stages?: string[] };
      setPaused({ reason: data.reason ?? "paused", nextStages: data.next_stages ?? [] });
      try {
        const snap = await getState(runId);
        setSnapshot(snap);
      } catch {
        // ignore
      }
      onAny("run_paused")(evt);
    });
    es.addEventListener("run_completed", async (evt) => {
      setCompleted(true);
      setPaused(null);
      try {
        const snap = await getState(runId);
        setSnapshot(snap);
      } catch {
        // ignore
      }
      onAny("run_completed")(evt);
    });
    es.addEventListener("run_failed", (evt) => {
      setPaused(null);
      try {
        const data = JSON.parse(evt.data ?? "{}") as { error?: string };
        setFailed(data.error ?? "Unknown error");
      } catch {
        setFailed("Unknown error");
      }
      onAny("run_failed")(evt);
    });

    es.onerror = () => {
      // Browser will auto-reconnect; we keep last state.
    };

    return () => {
      es.close();
      esRef.current = null;
    };
  }, [url, runId]);

  return { log, paused, failed, completed, snapshot };
}
