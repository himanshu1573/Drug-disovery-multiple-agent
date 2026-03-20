"use client";

import { ReactNode, useState } from "react";

export function CollapsibleSection({
  title,
  defaultOpen = true,
  right,
  children,
}: {
  title: string;
  defaultOpen?: boolean;
  right?: ReactNode;
  children: ReactNode;
}) {
  const [open, setOpen] = useState(defaultOpen);

  return (
    <details
      className="rounded-lg border border-slate-200 bg-white shadow-sm open:shadow-sm"
      open={open}
      onToggle={(e) => setOpen((e.currentTarget as HTMLDetailsElement).open)}
    >
      <summary className="flex cursor-pointer list-none items-center justify-between gap-3 px-4 py-3">
        <div className="flex items-center gap-2">
          <span className="text-sm font-semibold text-slate-900">{title}</span>
        </div>
        <div className="flex items-center gap-3">
          {right ? <div className="hidden sm:block">{right}</div> : null}
          <span className="select-none text-xs text-slate-500">{open ? "▾" : "▸"}</span>
        </div>
      </summary>
      <div className="border-t border-slate-100 p-4">{children}</div>
    </details>
  );
}
