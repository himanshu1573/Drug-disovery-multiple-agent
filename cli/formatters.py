import sys

# ─────────────────────────────────────────────────────────────────────────────
# ANSI Colors (auto-disable if not a tty)
# ─────────────────────────────────────────────────────────────────────────────
_IS_TTY = sys.stdout.isatty()

def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _IS_TTY else text

def bold(t: str)   -> str: return _c("1", t)
def green(t: str)  -> str: return _c("92", t)
def yellow(t: str) -> str: return _c("93", t)
def red(t: str)    -> str: return _c("91", t)
def blue(t: str)   -> str: return _c("94", t)
def dim(t: str)    -> str: return _c("90", t)
def cyan(t: str)   -> str: return _c("96", t)

STATUS_ICONS = {
    "success": green("✅ success"),
    "skipped": yellow("⏩ skipped"),
    "failed":  red("❌ failed"),
}

def _status_icon(status: str) -> str:
    return STATUS_ICONS.get(status, dim(status))

def print_table_result(result: dict) -> None:
    gene = result["query"]["gene_symbol"]
    disease = result["query"].get("disease_id") or dim("none")
    run_id = result.get("run_id", "")

    print()
    print(bold("=" * 100))
    print(bold(f"  EVIDENCE COLLECTION REPORT: {cyan(gene)}"))
    print(f"  Target indication : {disease}")
    print(f"  Run Identifier    : {dim(run_id)}")
    print(bold("=" * 100))

    # Source status table
    print(f"\n{bold('SOURCE STATUS')}")
    print(f"  {'Source':<16} {'Status':<22} {'Records':<10} {'Duration':<12} {'Note'}")
    print(f"  {'-'*16} {'-'*22} {'-'*10} {'-'*12} {'-'*40}")
    for s in result.get("source_status", []):
        src    = s["source"]
        status = _status_icon(s.get("status", ""))
        count  = str(s.get("record_count", 0))
        dur    = f"{s.get('duration_ms', 0)} ms"
        note   = dim(s.get("error_message") or "")
        print(f"  {src:<16} {status:<30} {count:<10} {dur:<12} {note}")

    llm_summary = result.get("llm_summary")
    if llm_summary:
        print(f"\n{bold('BIO-SYNTHESIS DOSSIER')}")
        print(f"  Mode                 : {llm_summary.get('generation_mode', 'unknown')}")
        if llm_summary.get("model_used"):
            print(f"  Model                : {cyan(llm_summary['model_used'])}")
            
        robustness = llm_summary.get("robustness")
        if robustness:
            print(f"  Status               : {green('COMPLETED') if robustness.get('minimum_coverage_met') else yellow('PARTIAL')}")
            print(
                "  Robustness           : "
                f"sources={robustness.get('successful_source_count', 0)}/"
                f"{robustness.get('requested_source_count', 0)} | "
                f"verdict={robustness.get('verdict', '')}"
            )
            
        markdown_report = llm_summary.get("markdown_report")
        if markdown_report:
            print("\n" + bold("-" * 100))
            print(markdown_report)
            print(bold("-" * 100))

    print(f"\n{bold('ERRORS')}" if result.get("errors") else "")
    for err in result.get("errors", []):
        print(f"  [{err['source']}] {err['error_code']}: {err['message']}")

    print(bold("=" * 100))
    print()
