import asyncio
import argparse

from agents.mcp_runtime import collect_source_via_mcp
from agents.schema import CollectorRequest, SourceName

# ANSI Colors
C_HEADER = "\033[95m"
C_OK = "\033[92m"
C_INFO = "\033[94m"
C_END = "\033[0m"
C_BOLD = "\033[1m"


async def run_test(source, gene, disease):
    print(f"\n{C_BOLD}{C_INFO}🔬 TESTING SOURCE: {source.upper()} | TARGET: {gene}{C_END}")
    
    request = CollectorRequest(
        gene_symbol=gene,
        disease_id=disease,
        sources=[SourceName(source)],
        max_literature_articles=3,
    )

    try:
        items, status, errors = await collect_source_via_mcp(SourceName(source), request)
        result = {
            "items": [item.model_dump(mode="json") for item in items],
            "source_status": status.model_dump(mode="json"),
            "errors": [err.model_dump(mode="json") for err in errors],
        }
        print(f"{C_OK}--- RESULT ---{C_END}\n{result}\n")
    except Exception as e:
        print(f"\033[91m❌ ERROR: {str(e)}\033[0m")


async def main():
    parser = argparse.ArgumentParser(description="MCP Tool Tester")
    parser.add_argument("--source", required=True, choices=["literature", "opentargets", "pharos", "depmap"])
    parser.add_argument("--gene", default="EGFR")
    parser.add_argument("--disease", default=None)
    
    args = parser.parse_args()
    await run_test(args.source, args.gene, args.disease)


if __name__ == "__main__":
    asyncio.run(main())
