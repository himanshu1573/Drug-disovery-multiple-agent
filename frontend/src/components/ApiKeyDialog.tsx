"use client";

import { useState, type FormEvent } from "react";
import { Eye, EyeOff, KeyRound, Lock } from "lucide-react";

import { validateLlmKey } from "@/lib/api";
import { PROVIDER_LABEL, type LlmProvider, type SessionLlmKey } from "@/lib/llmKey";

const KEY_HELP: Record<LlmProvider, { url: string; label: string; placeholder: string }> = {
  openai: { url: "https://platform.openai.com/api-keys", label: "platform.openai.com", placeholder: "sk-..." },
  google: { url: "https://aistudio.google.com/apikey", label: "aistudio.google.com (free tier)", placeholder: "AIza..." },
};

export function ApiKeyDialog({
  required,
  serverKeyAvailable,
  current,
  onSave,
  onClose,
}: {
  required: boolean;
  serverKeyAvailable: boolean;
  current: SessionLlmKey | null;
  onSave: (key: SessionLlmKey) => void;
  onClose: () => void;
}) {
  const [provider, setProvider] = useState<LlmProvider>(current?.provider ?? "google");
  const [apiKey, setApiKey] = useState("");
  const [showKey, setShowKey] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submit = async (e: FormEvent) => {
    e.preventDefault();
    const trimmed = apiKey.trim();
    if (!trimmed || busy) return;
    setBusy(true);
    setError(null);
    try {
      const result = await validateLlmKey(provider, trimmed);
      if (result.valid) onSave({ provider, apiKey: trimmed });
      else setError(result.error ?? "The provider rejected this key.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not validate the key.");
    } finally {
      setBusy(false);
    }
  };

  const help = KEY_HELP[provider];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-neutral-950/80 p-4 backdrop-blur-sm">
      <form
        onSubmit={submit}
        role="dialog"
        aria-modal="true"
        aria-labelledby="api-key-dialog-title"
        className="w-full max-w-md rounded-3xl border border-white/10 bg-neutral-900 p-6 shadow-2xl"
      >
        <div className="flex items-center gap-2">
          <KeyRound className="h-5 w-5 text-neutral-300" />
          <h2 id="api-key-dialog-title" className="text-lg font-semibold text-neutral-100">
            Bring your own API key
          </h2>
        </div>
        <p className="mt-2 text-sm text-neutral-400">
          The agents use an LLM to plan evidence collection, write the report, and answer follow-ups. Add an OpenAI or
          Google Gemini key to try the app.
        </p>

        <div className="mt-5 flex gap-2">
          {(Object.keys(PROVIDER_LABEL) as LlmProvider[]).map((p) => (
            <button
              key={p}
              type="button"
              onClick={() => {
                setProvider(p);
                setError(null);
              }}
              className={`rounded-full border px-3 py-1 text-xs ${
                provider === p ? "border-white/20 bg-white/10 text-neutral-100" : "border-white/10 text-neutral-400 hover:bg-white/5"
              }`}
            >
              {PROVIDER_LABEL[p]}
            </button>
          ))}
        </div>

        <label className="mt-4 block">
          <span className="text-[11px] font-bold uppercase tracking-widest text-neutral-500">{PROVIDER_LABEL[provider]} API key</span>
          <div className="mt-2 flex items-center rounded-2xl border border-white/10 bg-neutral-950/50 focus-within:border-white/20">
            <input
              type={showKey ? "text" : "password"}
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder={help.placeholder}
              autoComplete="off"
              spellCheck={false}
              autoFocus
              className="min-w-0 flex-1 bg-transparent px-4 py-3 text-sm text-neutral-100 outline-none placeholder:text-neutral-600"
            />
            <button
              type="button"
              onClick={() => setShowKey((v) => !v)}
              className="px-3 text-neutral-500 hover:text-neutral-200"
              aria-label={showKey ? "Hide key" : "Show key"}
            >
              {showKey ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
            </button>
          </div>
        </label>
        <div className="mt-2 text-xs text-neutral-500">
          Get a key at{" "}
          <a href={help.url} target="_blank" rel="noopener noreferrer" className="text-neutral-300 underline hover:text-neutral-100">
            {help.label}
          </a>
        </div>

        <div className="mt-4 flex gap-2 rounded-2xl border border-white/10 bg-white/5 p-3 text-xs text-neutral-400">
          <Lock className="mt-0.5 h-3.5 w-3.5 shrink-0" />
          <span>
            Stored only in this browser tab and cleared when you close it. Sent with your requests, used in memory for your
            runs, and never saved on the server.
          </span>
        </div>

        {error ? <div className="mt-3 break-words text-sm text-red-300">{error}</div> : null}

        <div className="mt-5 flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
          {!required ? (
            <button
              type="button"
              onClick={onClose}
              className="rounded-2xl border border-white/10 px-4 py-2 text-sm text-neutral-300 hover:bg-white/5"
            >
              {serverKeyAvailable && !current ? "Skip, use server key" : "Cancel"}
            </button>
          ) : null}
          <button
            type="submit"
            disabled={busy || !apiKey.trim()}
            className="rounded-2xl bg-white px-4 py-2 text-sm font-bold text-neutral-900 hover:bg-neutral-200 disabled:cursor-not-allowed disabled:opacity-30"
          >
            {busy ? "Validating..." : "Validate & continue"}
          </button>
        </div>
      </form>
    </div>
  );
}
