import asyncio
import json
import time
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from agents.schema import CollectorRequest, SourceName
from mcps.connectors.literature import LiteratureConnector
from mcps.connectors.depmap import DepMapConnector
from mcps.connectors.pharos import PharosConnector

# ANSI Colors for that "Cool" terminal look
C_HEADER = "\033[95m"
C_NAV = "\033[94m"
C_RAW = "\033[93m"
C_FILTER = "\033[92m"
C_FINAL = "\033[96m"
C_END = "\033[0m"
C_BOLD = "\033[1m"

async def trace_literature(gene):
    print(f"\n{C_HEADER}{C_BOLD}--- STEP 1: LITERATURE (LIVE SEARCH) ---{C_END}")
    connector = LiteratureConnector()
    request = CollectorRequest(gene_symbol=gene)
    
    # 1. Navigation
    url = f"{connector.base_url}?query={gene}&format=json"
    print(f"{C_NAV}🚀 NAVIGATING TO LIVE API:{C_END} {url}")
    
    # 2. Get Raw Data
    print(f"{C_RAW}📥 FETCHING RAW DATA...{C_END}")
    start = time.perf_counter()
    # We reach into the connector's internal http client
    payload = await connector.http.get_json(connector.base_url, params={"query": gene, "format": "json", "pageSize": 5})
    duration = time.perf_counter() - start
    
    raw_sample = json.dumps(payload, indent=2)[:500] + "..."
    print(f"{C_RAW}📥 RAW DATA RECEIVED ({duration:.2f}s):{C_END}\n{raw_sample}")
    
    # 3. Filtering
    print(f"\n{C_FILTER}🔍 FILTERING & CLEANING:{C_END}")
    results = payload.get("resultList", {}).get("result", [])
    print(f"   - Found {len(results)} total papers.")
    print(f"   - Action: Extracting PMIDs and Titles for the top 5.")
    print(f"   - Action: Discarding abstracts, author lists, and journal metadata to save space.")
    
    # 4. Final Result
    items, status, errors = await connector.collect(request)
    print(f"\n{C_FINAL}✅ FINAL CLEANED AGENT RECORD:{C_END}")
    print(json.dumps(items[0].model_dump(mode="json"), indent=2))

async def trace_mock_source(name, connector_class, raw_simulation):
    print(f"\n{C_HEADER}{C_BOLD}--- STEP: {name.upper()} (CONCEPTUAL TRACE) ---{C_END}")
    connector = connector_class()
    request = CollectorRequest(gene_symbol="EGFR")
    
    # 1. Navigation
    print(f"{C_NAV}🚀 TARGET ENDPOINT:{C_END} {connector.source.value.upper()} API")
    
    # 2. Raw Simulation
    print(f"{C_RAW}📥 TYPICAL RAW API RESPONSE:{C_END}\n{raw_simulation}")
    
    # 3. Filtering
    print(f"\n{C_FILTER}🔍 AGENT LOGIC (THE 'FILTER'):{C_END}")
    print(f"   - Ignoring: lineage graphs, mutation maps, and protein structures.")
    print(f"   - Extracting: The specific dependency 'Chronos' score.")
    
    # 4. Final Result
    items, status, errors = await connector.collect(request)
    print(f"\n{C_FINAL}✅ RESULT AFTER AGENT CLEANING:{C_END}")
    print(json.dumps(items[0].model_dump(mode="json"), indent=2))

async def main():
    print(f"{C_HEADER}{C_BOLD}==========================================")
    print("DEEP TRACE: HOW THE AGENT CLEANS YOUR DATA")
    print(f"=========================================={C_END}")
    
    gene = "EGFR"
    
    # Trace Live Literature
    await trace_literature(gene)
    
    # Trace DepMap (Simulated Raw for explanation)
    depmap_raw = """{
  "gene": "EGFR",
  "dependency": {
     "chronos_score": -0.82,
     "p_value": 0.0001,
     "confidence_interval": [-0.85, -0.79]
  },
  "lineage_data": { "stomach": [...], "lung": [...], "100+ more rows": "..." },
  "mutations": [ { "id": "L858R", "freq": 0.12 }, "..." ]
}"""
    await trace_mock_source("DepMap", DepMapConnector, depmap_raw)

    print(f"\n{C_HEADER}{C_BOLD}=========================================={C_END}")
    print(f"{C_BOLD}SUMMARY: The agent turned ~1MB of raw noise into ~1KB of high-value insights.{C_END}")

if __name__ == "__main__":
    asyncio.run(main())
