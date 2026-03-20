
import asyncio
import json
from agents.mcp_runtime import collect_source_via_mcp_with_raw
from agents.schema import CollectorRequest, SourceName

async def test_raw_mcp():
    request = CollectorRequest(
        gene_symbol="EGFR",
        disease_id="EFO_0000311",
        sources=[SourceName.DEPMAP, SourceName.OPENTARGETS]
    )
    
    # Just test DEPMAP for now as it's easier to verify
    source = SourceName.DEPMAP
    print(f"Testing source: {source}")
    items, status, errors, raw_payload = await collect_source_via_mcp_with_raw(source, request)
    
    print("\n--- RAW PAYLOAD ---")
    print(json.dumps(raw_payload, indent=2))
    
    print("\n--- STATUS ---")
    print(status)

if __name__ == "__main__":
    asyncio.run(test_raw_mcp())
