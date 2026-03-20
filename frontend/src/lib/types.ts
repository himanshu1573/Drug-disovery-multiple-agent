export type SourceName = "depmap" | "pharos" | "opentargets" | "literature";

export type RunEvent =
  | { event: "connected"; data: { run_id: string } }
  | { event: "ping"; data: { run_id: string } }
  | { event: "run_status"; data: { run_id: string; status: string } }
  | { event: "run_completed"; data: { run_id: string; status: "completed"; result: unknown } }
  | { event: "run_failed"; data: { run_id: string; status: "failed"; error: string } }
  | { event: "run_paused"; data: { run_id: string; reason: string; next_stages: string[] } }
  | { event: string; data: Record<string, unknown> };

export type Snapshot = {
  run_id: string;
  next: string[];
  values: Record<string, unknown>;
  _runtime?: {
    provider: "openai" | "google" | "none";
    locked: boolean;
    llm_calls_enabled: boolean;
    error?: string | null;
    selected_at_ms?: number;
    system_pref?: string;
  };
  _persisted?: {
    status: string;
    last_stage?: string | null;
    updated_at_ms?: number;
    error?: string | null;
  } | null;
};

export type PlanDecisionStatus = "approved" | "rejected" | "needs_changes";

export type ReviewDecisionStatus = "approved" | "rejected" | "needs_more_evidence";
