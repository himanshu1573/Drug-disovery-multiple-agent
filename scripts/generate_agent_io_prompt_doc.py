#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


def _artifact_root() -> Path:
    return Path(os.getenv("A4T_ARTIFACT_DIR") or Path(__file__).resolve().parent.parent / "artifacts")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _compact(value: Any, max_chars: int = 6000) -> str:
    text = json.dumps(value, indent=2, ensure_ascii=True, default=str)
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n... [TRUNCATED]\n"


def _read_text(path: Path, max_chars: int = 12000) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n... [TRUNCATED]\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate per-agent input/output/prompt doc for a run_id.")
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--out", default="", help="Output markdown path (default: docs/runs/<run_id>_agent_io_prompts.md)")
    args = ap.parse_args()

    run_id = args.run_id
    root = _artifact_root()
    workdir = root / "working_memory" / run_id
    promptdir = root / "prompts" / run_id

    if not workdir.exists():
        raise SystemExit(f"Missing working_memory for run_id={run_id}: {workdir}")

    out_path = Path(args.out) if args.out else (Path(__file__).resolve().parent.parent / "docs" / "runs" / f"{run_id}_agent_io_prompts.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    def section(title: str) -> list[str]:
        return [f"## {title}", ""]

    lines: list[str] = []
    lines.append(f"# Agent I/O + Prompts (Run: `{run_id}`)")
    lines.append("")
    lines.append("This document captures, for each agent used in the run:")
    lines.append("- Input (from the stage state snapshot)")
    lines.append("- Output (from the stage update)")
    lines.append("- Prompt(s) used (if prompt tracing was enabled)")
    lines.append("")

    # Stage files are stored as <stage>.json
    stages = [
        ("validate_input", "input_validation_agent"),
        ("plan_collection", "planning_agent"),
        ("collect_sources_parallel", "collectors"),
        ("normalize_evidence", "normalization_agent"),
        ("verify_evidence", "verifier"),
        ("analyze_conflicts", "conflict_analyzer"),
        ("build_evidence_graph", "evidence_graph_builder"),
        ("generate_explanation", "summary_agent"),
        ("supervisor_decide", "supervisor_agent"),
        ("prepare_review_brief", "review_support_agent"),
        ("human_review_gate", "human_review_gate"),
        ("emit_dossier", "dossier_emitter"),
    ]

    for stage, agent in stages:
        stage_path = workdir / f"{stage}.json"
        if not stage_path.exists():
            continue
        payload = _read_json(stage_path)
        state = payload.get("state", {})
        update = payload.get("update", {})

        lines.extend(section(f"{stage} ({agent})"))
        lines.append("### Input")
        lines.append("")
        lines.append("```json")
        lines.append(_compact(state))
        lines.append("```")
        lines.append("")
        lines.append("### Output")
        lines.append("")
        lines.append("```json")
        lines.append(_compact(update))
        lines.append("```")
        lines.append("")

        # Prompt traces are separate working memory snapshots + text files.
        if promptdir.exists():
            # Search promptdir for files matching "<agent>.<stage>.*.txt"
            prefix = f"{agent}.{stage}"
            sys_path = promptdir / f"{prefix}.system.txt"
            user_path = promptdir / f"{prefix}.user.txt"
            if sys_path.exists() or user_path.exists():
                lines.append("### Prompt")
                lines.append("")
                if sys_path.exists():
                    lines.append(f"- system: `{sys_path}`")
                if user_path.exists():
                    lines.append(f"- user: `{user_path}`")
                lines.append("")
                if sys_path.exists():
                    lines.append("#### System Prompt (truncated)")
                    lines.append("")
                    lines.append("```text")
                    lines.append(_read_text(sys_path))
                    lines.append("```")
                    lines.append("")
                if user_path.exists():
                    lines.append("#### User Prompt (truncated)")
                    lines.append("")
                    lines.append("```text")
                    lines.append(_read_text(user_path))
                    lines.append("```")
                    lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

