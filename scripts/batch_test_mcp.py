import asyncio
import time
import json
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from agents.mcp_runtime import collect_source_via_mcp
from agents.schema import CollectorRequest, SourceName

# ANSI Colors
C_HEADER = "\033[95m"
C_OK = "\033[92m"
C_INFO = "\033[94m"
C_DATA = "\033[90m"
C_END = "\033[0m"
C_BOLD = "\033[1m"

GENE_LIST = [
    "EGFR", "KRAS", "BRAF", "TP53", "BRCA1", 
    "BRCA2", "MYC", "ERBB2", "ALK", "MET", "PIK3CA"
]

RESULTS_DIR = ROOT_DIR / "artifacts" / "batch_results"

async def test_gene(gene):
    print(f"{C_INFO}▶ Processing {gene}...{C_END}")
    
    request = CollectorRequest(
        gene_symbol=gene,
        max_literature_articles=1,
    )

    gene_data = {
        "gene": gene,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "sources": {}
    }
    
    # helper to check success
    def is_success(res):
        return bool(res.get("items"))

    async def collect(source: SourceName):
        items, status, errors = await collect_source_via_mcp(source, request)
        return {
            "items": [item.model_dump(mode="json") for item in items],
            "source_status": [status.model_dump(mode="json")],
            "errors": [err.model_dump(mode="json") for err in errors],
        }

    # 1. Open Targets
    try:
        res = await collect(SourceName.OPENTARGETS)
        gene_data["sources"]["opentargets"] = res
    except Exception as e:
        gene_data["sources"]["opentargets"] = {"error": str(e)}

    # 2. PHAROS
    try:
        res = await collect(SourceName.PHAROS)
        gene_data["sources"]["pharos"] = res
    except Exception as e:
        gene_data["sources"]["pharos"] = {"error": str(e)}

    # 3. Literature
    try:
        res = await collect(SourceName.LITERATURE)
        gene_data["sources"]["literature"] = res
    except Exception as e:
        gene_data["sources"]["literature"] = {"error": str(e)}

    # 4. DepMap
    try:
        res = await collect(SourceName.DEPMAP)
        gene_data["sources"]["depmap"] = res
    except Exception as e:
        gene_data["sources"]["depmap"] = {"error": str(e)}

    # Save individual gene file
    file_path = RESULTS_DIR / f"{gene}.json"
    with open(file_path, "w") as f:
        json.dump(gene_data, f, indent=2)
    
    # Return status indicators for the terminal table
    return {
        "OT": "✅" if is_success(gene_data["sources"]["opentargets"]) else "⏹️",
        "PH": "✅" if is_success(gene_data["sources"]["pharos"]) else "⏹️",
        "LIT": "✅" if is_success(gene_data["sources"]["literature"]) else "⏹️",
        "DM": "✅" if is_success(gene_data["sources"]["depmap"]) else "🔒"
    }

async def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    print(f"\n{C_BOLD}{C_HEADER}🚀 BATCH TESTING & ARCHIVING: {len(GENE_LIST)} TARGETS{C_END}")
    print(f"{C_DATA}Saving results to: {RESULTS_DIR}/{C_END}\n")
    
    table = []
    for gene in GENE_LIST:
        status_row = await test_gene(gene)
        table.append((gene, status_row))
        await asyncio.sleep(0.3)

    # Generate Summary Markdown
    summary_path = RESULTS_DIR / "summary_report.md"
    with open(summary_path, "w") as f:
        f.write(f"# Batch Evidence Collection Summary\n\n")
        f.write(f"Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"| GENE | Open Targets | PHAROS | Literature | DepMap |\n")
        f.write(f"| :--- | :---: | :---: | :---: | :---: |\n")
        for gene, res in table:
            f.write(f"| **{gene}** | {res['OT']} | {res['PH']} | {res['LIT']} | {res['DM']} |\n")
        f.write(f"\nLegend: ✅=Data Found, ⏹️=Target Not in DB, 🔒=Security Blocked\n")

    print(f"\n{C_BOLD}📊 BATCH COMPLETE{C_END}")
    print(f"Summary saved to: {summary_path}")
    print(f"Individual data saved in: {RESULTS_DIR}\n")

if __name__ == "__main__":
    asyncio.run(main())
