"use client";

export function EventLog({
  items,
}: {
  items: { ts: number; event: string; data: Record<string, unknown> }[];
}) {
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4">
      <div className="mb-3 flex items-center justify-between">
        <h2 className="text-sm font-semibold text-slate-900">Run events</h2>
        <span className="text-xs text-slate-500">{items.length} events</span>
      </div>
      <div className="max-h-[60vh] overflow-auto rounded-md border border-slate-100 bg-slate-50 p-3 text-xs">
        {items.length === 0 ? (
          <div className="text-slate-500">No events yet.</div>
        ) : (
          <ol className="flex flex-col gap-2">
            {items
              .slice()
              .reverse()
              .map((it, idx) => (
                <li key={`${it.ts}-${idx}`} className="rounded border border-slate-200 bg-white p-2">
                  <div className="flex items-center justify-between gap-3">
                    <span className="font-mono text-slate-900">{it.event}</span>
                    <span className="text-slate-500">{new Date(it.ts).toLocaleTimeString()}</span>
                  </div>
                  <pre className="mt-2 whitespace-pre-wrap break-words text-slate-700">
                    {JSON.stringify(it.data, null, 2)}
                  </pre>
                </li>
              ))}
          </ol>
        )}
      </div>
    </div>
  );
}

