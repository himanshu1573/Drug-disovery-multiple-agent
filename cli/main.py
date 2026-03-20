from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time

from dotenv import load_dotenv

from agents.graph import CollectionPaused, get_collection_state, resume_collection_graph, run_collection_graph
from agents.request_builders import build_collector_request
from agents.review_interface import apply_review_decision
from agents.schema import CollectorRequest, ReviewDecisionInput, ReviewDecisionStatus, SourceName
from cli.formatters import bold, blue, cyan, dim, green, red, yellow, print_table_result

load_dotenv()

ASCII_LOGO = r"""
     ___                        _     _  _                         _   
    / _ \                      | |   | || |                       | |  
   / /_\ \ __ _  ___ _ __  _   | |_  | || |_    __ _  __ _  ___ _ __ | |_ 
   |  _  |/ _` |/ _ \ '_ \| |_ | __| |__   _|  / _` |/ _` |/ _ \ '_ \| __|
   | | | | (_| |  __/ | | |  _|| |_     | |   | (_| | (_| |  __/ | | | |_ 
   \_| |_/\__, |\___|_| |_|_|   \__|    |_|    \__,_|\__, |\___|_| |_|\__|
           __/ |                                      __/ |               
          |___/                                      |___/                
"""

def print_header():
    # Print the logo in a gradient of colors
    lines = ASCII_LOGO.strip("\n").split("\n")
    colors = [cyan, cyan, blue, blue, blue, cyan, cyan]
    for i, line in enumerate(lines):
        print(colors[i % len(colors)](line))
    
    print("\n" + "=" * 100)
    print(f"  {bold(yellow('AGENT 4 AGENT'))} | {bold('Evidence Collector Ecosystem')}")
    print("=" * 100)
    
    print(f"\n{bold('Initialized 4 Separate MCP Systems:')}")
    print(f"  {green('✔')} {bold('Open Targets')}  {dim('— Global drug/disease associations via external MCP')}")
    print(f"  {green('✔')} {bold('Pharos')}        {dim('— Target development levels via community MCP')}")
    print(f"  {green('✔')} {bold('Internal Lit')}   {dim('— AI-powered semantic literature search')}")
    print(f"  {green('✔')} {bold('DepMap')}         {dim('— Cancer dependency/perturbation genetic scores')}")
    print("-" * 100)

VALID_SOURCES = ["opentargets", "pharos", "literature", "depmap"]

SOURCE_DESCRIPTIONS = {
    "opentargets":     "Disease associations via official Open Targets external MCP (stdio)",
    "pharos":          "Target development level via community PHAROS external MCP (SSE:8787)",
    "literature":      "Published research papers via internal MCP",
    "depmap":          "CRISPR genetic dependency scores via internal MCP",
}


def _display_stage_name(stage_name: str) -> str:
    return stage_name.replace("_", " ").title()


def _print_failure_context(exc: Exception) -> None:
    stage = getattr(exc, "__drugagent_stage__", None)
    state = getattr(exc, "__drugagent_input__", None)
    if stage is None:
        return
    print(red(f"\n[Failure] Stage `{stage}` failed."))
    if state is not None:
        print(dim("Input snapshot:"))
        print(json.dumps(state, indent=2, default=str))


def _print_pause_context(exc: CollectionPaused) -> None:
    print(yellow(f"\n[Paused] Run `{exc.run_id}` is waiting at {', '.join(exc.next_stages) or 'unknown stage'}."))
    plan = exc.state_values.get("plan")
    if plan is not None and hasattr(plan, "model_dump"):
        print(dim("Planner output:"))
        print(json.dumps(plan.model_dump(mode="json"), indent=2))
    supervisor_decision = exc.state_values.get("supervisor_decision")
    if supervisor_decision is not None and hasattr(supervisor_decision, "model_dump"):
        print(dim("Supervisor decision:"))
        print(json.dumps(supervisor_decision.model_dump(mode="json"), indent=2))
    review_brief = exc.state_values.get("review_brief")
    if review_brief is not None and hasattr(review_brief, "model_dump"):
        print(dim("Review brief:"))
        print(json.dumps(review_brief.model_dump(mode="json"), indent=2))
    print(dim("Submit a review decision for this run id, then resume the workflow."))

def _parse_sources(raw_sources: str | None) -> list[SourceName]:
    if raw_sources is None or not raw_sources.strip():
        return [
            SourceName.DEPMAP,
            SourceName.PHAROS,
            SourceName.OPENTARGETS,
            SourceName.LITERATURE,
        ]

    parsed: list[SourceName] = []
    for value in raw_sources.split(","):
        token = value.strip().lower()
        if not token:
            continue
        try:
            parsed.append(SourceName(token))
        except ValueError:
            print(red(f"Error: Unknown source '{token}'. Valid: {', '.join(VALID_SOURCES)}"))
            sys.exit(1)
    return parsed


def _parse_review_decision(raw_decision: str) -> ReviewDecisionStatus:
    token = raw_decision.strip().lower()
    try:
        return ReviewDecisionStatus(token)
    except ValueError:
        options = ", ".join([status.value for status in ReviewDecisionStatus])
        print(red(f"Error: Unknown decision '{token}'. Valid: {options}"))
        sys.exit(1)

async def run_query(
    gene: str,
    disease: str | None,
    sources: list[SourceName],
    output: str = "table",
    save: str | None = None,
    top_k: int = 5,
    model: str | None = None,
    objective: str | None = None,
    run_id: str | None = None,
    save_markdown: bool = False,
) -> None:
    await _execute_query(
        request=build_collector_request(
            gene_symbol=gene,
            disease_id=disease,
            objective=objective,
            sources=sources,
            per_source_top_k=top_k,
            max_literature_articles=max(top_k, 1),
            model_override=model,
            run_id=run_id,
        ),
        output=output,
        save=save,
        gene=gene,
        sources=sources,
        disease=disease,
        runner=run_collection_graph,
        save_markdown=save_markdown,
    )


async def resume_query(
    run_id: str,
    output: str = "table",
    save: str | None = None,
) -> None:
    snapshot = await get_collection_state(run_id)
    state_values = snapshot.values
    request = state_values.get("query")
    if request is None:
        raise ValueError(f"No stored query found for run `{run_id}`.")
    if isinstance(request, dict):
        request = CollectorRequest.model_validate(request)
    await _execute_query(
        request=request,
        output=output,
        save=save,
        gene=request.gene_symbol,
        sources=request.sources,
        disease=request.disease_id,
        runner=resume_collection_graph,
        save_markdown=False,
    )


async def _execute_query(
    *,
    request,
    output: str,
    save: str | None,
    gene: str,
    sources: list[SourceName],
    disease: str | None,
    runner,
    save_markdown: bool,
) -> None:
    if output in ("table", "minimal"):
        source_names = [s.value for s in sources]
        print_header()
        print(f"\n{blue('🔬 Querying')} {bold(gene.upper())} across {bold(str(len(source_names)))} source(s)...")
        src_list = ", ".join(f"{cyan(s)}" for s in source_names)
        print(f"   Sources: {src_list}")
        if disease:
            print(f"   Disease: {disease}")
        print(dim("   Connecting to live APIs..."))

    def on_progress(event_type: str, payload: dict):
        if output not in ("table", "minimal"):
            return

        if event_type == "stage_start":
            stage = payload["stage"]
            print(f"   {cyan('•')} Entering {bold(cyan(_display_stage_name(stage)))}")
            return

        if event_type == "stage_end":
            stage = payload["stage"]
            update = payload.get("update", {})
            context = ""
            if stage == "validate_input":
                past_runs = update.get("past_runs", {})
                count = past_runs.get("count", 0) if isinstance(past_runs, dict) else 0
                context = f"validated inputs; prior runs={count}"
            elif stage == "plan_collection":
                plan = update.get("plan", {})
                selected_sources = plan.get("selected_sources", []) if isinstance(plan, dict) else []
                memory_context = plan.get("memory_context", {}) if isinstance(plan, dict) else {}
                memory_hits = memory_context.get("match_count", 0) if isinstance(memory_context, dict) else 0
                latest_decision = memory_context.get("latest_review_decision") if isinstance(memory_context, dict) else None
                planning_mode = plan.get("planning_mode", "unknown")
                planner_model = plan.get("planner_model_used")
                context = (
                    f"planned {len(selected_sources)} source(s), mode={planning_mode}, memory_hits={memory_hits}"
                    + (f", latest_decision={latest_decision}" if latest_decision else "")
                    + (f", model={planner_model}" if planner_model else "")
                )
                print(f"      {dim('query_intent:')} {plan.get('query_intent', '')}")
                if selected_sources:
                    print(f"      {dim('selected_sources:')} {', '.join(selected_sources)}")
                variants = plan.get('query_variants', [])
                if variants:
                    print(f"      {dim('query_variants:')} {', '.join(variants)}")
                expected_outputs = plan.get("expected_outputs", {})
                if expected_outputs:
                    print(f"      {dim('expected_outputs:')} {json.dumps(expected_outputs)}")
                retry_policy = plan.get("retry_policy", {})
                if retry_policy:
                    print(f"      {dim('retry_policy:')} {json.dumps(retry_policy)}")
                source_directives = plan.get("source_directives", {})
                for source_name, directive in source_directives.items():
                    print(f"      {dim(f'directive[{source_name}]:')} {directive}")
                notes = plan.get("execution_notes", [])
                for note in notes:
                    print(f"      {dim('plan_note:')} {note}")
            elif stage == "collect_sources_parallel":
                items = update.get("evidence_items", {})
                statuses = update.get("source_status", {})
                item_count = items.get("count", 0) if isinstance(items, dict) else 0
                status_count = statuses.get("count", 0) if isinstance(statuses, dict) else 0
                context = f"fetched {item_count} raw item(s) across {status_count} source run(s)"
            elif stage == "normalize_evidence":
                items = update.get("normalized_items", {})
                context = f"normalized {items.get('count', 0) if isinstance(items, dict) else 0} item(s)"
            elif stage == "verify_evidence":
                report = update.get("verification_report", {})
                context = (
                    f"blocked={report.get('blocked', False)} "
                    f"warnings={report.get('warning_count', 0)}"
                    if isinstance(report, dict)
                    else ""
                )
            elif stage == "analyze_conflicts":
                conflicts = update.get("conflicts", {})
                context = f"conflicts={conflicts.get('count', 0) if isinstance(conflicts, dict) else 0}"
            elif stage == "build_evidence_graph":
                graph = update.get("evidence_graph", {})
                if isinstance(graph, dict):
                    context = (
                        f"nodes={len(graph.get('nodes', []))} "
                        f"edges={len(graph.get('edges', []))}"
                    )
            elif stage == "generate_explanation":
                context = "summary generated"
            elif stage == "supervisor_decide":
                decision = update.get("supervisor_decision", {})
                if isinstance(decision, dict):
                    context = (
                        f"action={decision.get('action', 'unknown')}, "
                        f"mode={decision.get('decision_mode', 'unknown')}"
                    )
            elif stage == "prepare_review_brief":
                brief = update.get("review_brief", {})
                if isinstance(brief, dict):
                    question_count = len(brief.get("reviewer_questions", []))
                    blocking_count = len(brief.get("blocking_points", []))
                    context = f"questions={question_count} blocking_points={blocking_count}"
            elif stage == "human_review_gate":
                decision = update.get("review_decision", {})
                if isinstance(decision, dict):
                    context = f"decision={decision.get('decision', 'pending')}"
                elif decision is None:
                    context = "decision=pending_manual_review"
            elif stage == "emit_dossier":
                context = "final dossier emitted"

            suffix = f" {dim(f'({context})')}" if context else ""
            print(f"   {green('✓')} {_display_stage_name(stage)} complete{suffix}")
            return

        if event_type == "edge":
            source = payload["from_stage"]
            target = payload["to_stage"]
            reason = payload.get("reason", "")
            reason_text = f" [{reason}]" if reason else ""
            print(f"   {yellow('↳')} {_display_stage_name(source)} -> {_display_stage_name(target)}{dim(reason_text)}")
            return

        if event_type == "source_start":
            print(f"      {blue('·')} Source collector start: {payload['source']}")
            return

        if event_type == "source_end":
            error = payload.get("error", "")
            suffix = f", error={error}" if error else ""
            print(
                f"      {blue('·')} Source collector end: {payload['source']} "
                f"status={payload.get('status')} records={payload.get('record_count', 0)}{suffix}"
            )
            return

        if event_type == "agent_decision":
            decision_mode = payload.get("decision_mode", "unknown")
            print(
                f"      {yellow('·')} Agent decision: {payload['agent_name']} -> {payload['action']} "
                f"{dim(f'[{decision_mode}]')}"
            )
            print(f"        {payload.get('rationale', '')}")
            return

        if event_type == "agent_report":
            generation_mode = payload.get("generation_mode", "unknown")
            print(
                f"      {yellow('·')} Agent report: {payload['agent_name']} "
                f"{dim(f'[{generation_mode}]')}"
            )
            print(f"        {payload.get('summary', '')}")
            return

        if event_type == "stage_error":
            print(red(f"   [X] {_display_stage_name(payload['stage'])} failed: {payload.get('error', 'unknown error')}"))
            return

        if event_type == "workflow_paused":
            next_stages = payload.get("next_stages", ())
            reason = payload.get("reason", "workflow_paused")
            print(f"   {yellow('∥')} Workflow paused at {', '.join(next_stages) or 'unknown'} {dim(f'[{reason}]')}")

    t0 = time.perf_counter()
    result = await runner(request, progress_cb=on_progress)
    elapsed = time.perf_counter() - t0

    result_dict = result.model_dump(mode="json")

    if output == "json":
        print(json.dumps(result_dict, indent=2))
    elif output == "table":
        print_table_result(result_dict)
        print(dim(f"  [Completed in {elapsed:.2f}s]"))
    elif output == "minimal":
        print(green(f"\n✅ Flow completed successfully in {elapsed:.2f}s!"))

    if save:
        os.makedirs(os.path.dirname(save) if os.path.dirname(save) else ".", exist_ok=True)
        with open(save, "w") as f:
            json.dump(result_dict, f, indent=2)
        print(green(f"✅ Full JSON saved to: {save}"))

    # Optional: save markdown summary (disabled by default to avoid repo noise).
    auto_enabled = os.getenv("A4T_AUTO_SAVE_RESULTS", "0").strip().lower() in {"1", "true", "yes"}
    if (save_markdown or auto_enabled) and result.llm_summary and result.llm_summary.markdown_report:
        md_dir = "results"
        os.makedirs(md_dir, exist_ok=True)
        md_path = os.path.join(md_dir, f"{gene.upper()}_summary.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(result.llm_summary.markdown_report)
        print(green(f"📄 Markdown report saved to: {md_path}"))

async def repl_loop() -> None:
    print_header()
    print(bold("Interactive REPL Mode"))
    print("Enter target + disease, then source MCP servers are orchestrated via LangGraph.")
    print("Type 'quit' or 'exit' to stop.")
    print("=" * 100)

    while True:
        gene_symbol = input("\nTarget gene symbol (example: EGFR): ").strip()
        if gene_symbol.lower() in {"quit", "exit"}:
            break
        if not gene_symbol:
            continue

        disease_id = input("Disease id (optional, example: EFO_0000311): ").strip() or None
        raw_sources = input("Sources (comma list or empty for all): ").strip() or None

        try:
            sources = _parse_sources(raw_sources)
            await run_query(gene_symbol, disease_id, sources)
        except ValueError as exc:
            print(red(f"Input error: {exc}"))
        except Exception as exc:  # noqa: BLE001
            _print_failure_context(exc)
            print(red(f"Execution error: {exc}"))
    print("Goodbye")


def submit_review(
    run_id: str,
    decision: str,
    reviewer_id: str,
    reason: str,
) -> None:
    parsed_decision = _parse_review_decision(decision)
    payload = ReviewDecisionInput(
        run_id=run_id,
        decision=parsed_decision,
        reviewer_id=reviewer_id,
        reason=reason,
    )
    response = apply_review_decision(payload)
    print(json.dumps(response.model_dump(mode="json"), indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli",
        description=bold("Evidence Collector — Aggregate genetic evidence from scientific databases via MCP"),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run a single query")
    run_parser.add_argument(
        "--gene", "-g",
        required=True,
        metavar="SYMBOL",
        help="Target gene symbol (example: EGFR, BRAF, KRAS)",
    )
    run_parser.add_argument(
        "--disease", "-d",
        default=None,
        metavar="DISEASE_ID",
        help="Disease EFO/MONDO ID to filter evidence (example: EFO_0000311)",
    )
    run_parser.add_argument(
        "--sources", "-s",
        default=",".join(VALID_SOURCES),
        metavar="SOURCE[,SOURCE]",
        help=f"Comma-separated sources to query. Default: all. Options: {', '.join(VALID_SOURCES)}",
    )
    run_parser.add_argument(
        "--output", "-o",
        choices=["table", "json", "minimal"],
        default="table",
        help="Output format: 'table', 'json', or 'minimal'. Default: table",
    )
    run_parser.add_argument(
        "--save",
        metavar="FILE",
        default=None,
        help="Save JSON result to a file (example: --save results/EGFR.json)",
    )
    run_parser.add_argument(
        "--save-markdown",
        action="store_true",
        help="Save the generated markdown report to results/<GENE>_summary.md (default: off).",
    )
    run_parser.add_argument(
        "--top-k",
        type=int,
        default=15,
        metavar="N",
        help="Target number of evidence records per source (default: 15).",
    )
    run_parser.add_argument(
        "--model",
        metavar="MODEL",
        default=None,
        help="Override the LLM model (default: env variable A4T_SUMMARY_MODEL)",
    )
    run_parser.add_argument(
        "--objective",
        metavar="TEXT",
        default=None,
        help="Optional research objective or intent.",
    )
    run_parser.add_argument(
        "--run-id",
        metavar="RUN_ID",
        default=None,
        help="Optional explicit run id. Use this when resuming or pairing with manual review.",
    )
    
    # REPL command
    subparsers.add_parser("repl", help="Start interactive REPL loop")

    # Review command
    review_parser = subparsers.add_parser("review", help="Record a human review decision")
    review_parser.add_argument(
        "--run-id",
        required=True,
        metavar="RUN_ID",
        help="Run id to attach the review decision to.",
    )
    review_parser.add_argument(
        "--decision",
        required=True,
        metavar="DECISION",
        help="Decision: approved | rejected | needs_more_evidence",
    )
    review_parser.add_argument(
        "--reviewer-id",
        required=True,
        metavar="REVIEWER",
        help="Reviewer identifier (required).",
    )
    review_parser.add_argument(
        "--reason",
        required=True,
        metavar="TEXT",
        help="Reason for the decision (required).",
    )

    resume_parser = subparsers.add_parser("resume", help="Resume a paused run from checkpoint")
    resume_parser.add_argument(
        "--output", "-o",
        choices=["table", "json", "minimal"],
        default="table",
        help="Output format: 'table', 'json', or 'minimal'. Default: table",
    )
    resume_parser.add_argument(
        "--save",
        metavar="FILE",
        default=None,
        help="Save JSON result to a file.",
    )
    resume_parser.add_argument(
        "--run-id",
        required=True,
        metavar="RUN_ID",
        help="Paused run id to resume.",
    )
    
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "repl":
        try:
            asyncio.run(repl_loop())
        except KeyboardInterrupt:
            print(f"\n{yellow('Interrupted.')}")
            sys.exit(0)
            
    elif args.command == "run":
        sources = _parse_sources(args.sources)
        try:
            asyncio.run(run_query(
                gene=args.gene,
                disease=args.disease,
                sources=sources,
                output=args.output,
                save=args.save,
                top_k=args.top_k,
                model=args.model,
                objective=args.objective,
                run_id=args.run_id,
                save_markdown=args.save_markdown,
            ))
        except KeyboardInterrupt:
            print(f"\n{yellow('Interrupted.')}")
            sys.exit(0)
        except CollectionPaused as exc:
            _print_pause_context(exc)
            sys.exit(2)
        except Exception as exc:
            _print_failure_context(exc)
            print(red(f"\n[Error] {exc}"))
            sys.exit(1)

    elif args.command == "review":
        try:
            submit_review(
                run_id=args.run_id,
                decision=args.decision,
                reviewer_id=args.reviewer_id,
                reason=args.reason,
            )
        except Exception as exc:
            _print_failure_context(exc)
            print(red(f"\n[Error] {exc}"))
            sys.exit(1)

    elif args.command == "resume":
        try:
            asyncio.run(resume_query(
                run_id=args.run_id,
                output=args.output,
                save=args.save,
            ))
        except KeyboardInterrupt:
            print(f"\n{yellow('Interrupted.')}")
            sys.exit(0)
        except CollectionPaused as exc:
            _print_pause_context(exc)
            sys.exit(2)
        except Exception as exc:
            _print_failure_context(exc)
            print(red(f"\n[Error] {exc}"))
            sys.exit(1)


if __name__ == "__main__":
    main()
