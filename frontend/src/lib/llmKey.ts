export type LlmProvider = "openai" | "google";
export type SessionLlmKey = { provider: LlmProvider; apiKey: string };

export const PROVIDER_LABEL: Record<LlmProvider, string> = { openai: "OpenAI", google: "Google Gemini" };

// sessionStorage, never localStorage: the key is scoped to this tab and cleared when it closes.
// Mirrored in memory so the app still works if storage is blocked (e.g. some private modes).
const SS_LLM_KEY = "drugagent.llm_key.v1";

let current: SessionLlmKey | null = null;
let loaded = false;

export function getSessionLlmKey(): SessionLlmKey | null {
  if (loaded) return current;
  loaded = true;
  try {
    const parsed = JSON.parse(sessionStorage.getItem(SS_LLM_KEY) ?? "null") as Partial<SessionLlmKey> | null;
    if ((parsed?.provider === "openai" || parsed?.provider === "google") && typeof parsed.apiKey === "string" && parsed.apiKey) {
      current = { provider: parsed.provider, apiKey: parsed.apiKey };
    }
  } catch {
    // ignore
  }
  return current;
}

export function setSessionLlmKey(key: SessionLlmKey | null): void {
  current = key;
  loaded = true;
  try {
    if (key) sessionStorage.setItem(SS_LLM_KEY, JSON.stringify(key));
    else sessionStorage.removeItem(SS_LLM_KEY);
  } catch {
    // ignore
  }
}

export function maskKey(apiKey: string): string {
  return `••••${apiKey.length > 8 ? apiKey.slice(-4) : ""}`;
}
