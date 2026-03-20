import json
import asyncio
import httpx

# ANSI Colors for a beautiful terminal report
C_HEADER = "\033[95m"
C_OK = "\033[92m"
C_INFO = "\033[94m"
C_DATA = "\033[90m"
C_WARNING = "\033[93m"
C_FAIL = "\033[91m"
C_END = "\033[0m"
C_BOLD = "\033[1m"

async def test_europe_pmc(gene):
    print(f"{C_HEADER}Testing Europe PMC (Literature)...{C_END}")
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    params = {"query": gene, "format": "json", "pageSize": 1}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        if resp.status_code == 200:
            data = resp.json()
            hit_count = data.get('hitCount')
            paper = data.get('resultList', {}).get('result', [{}])[0]
            print(f"{C_OK}✅ SUCCESS: Found {hit_count} papers.{C_END}")
            print(f"{C_DATA}   Sample Result: \"{paper.get('title')[:60]}...\"{C_END}")
        else:
            print(f"{C_FAIL}❌ FAILED: Status {resp.status_code}{C_END}")

async def test_open_targets(gene):
    print(f"{C_HEADER}Testing Open Targets (GraphQL)...{C_END}")
    url = "https://api.platform.opentargets.org/api/v4/graphql"
    query = """
    query search($queryString: String!) {
      search(queryString: $queryString, entityNames: ["target"]) {
        hits {
          id
          name
        }
      }
    }
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json={"query": query, "variables": {"queryString": gene}})
        if resp.status_code == 200:
            data = resp.json()
            hits = data.get("data", {}).get("search", {}).get("hits", [])
            print(f"{C_OK}✅ SUCCESS: Found {len(hits)} matching targets.{C_END}")
            if hits:
                print(f"{C_DATA}   Sample Result: ID={hits[0]['id']}, Name={hits[0]['name']}{C_END}")
        else:
            print(f"{C_FAIL}❌ FAILED: Status {resp.status_code}{C_END}")

async def test_pharos(gene):
    print(f"{C_HEADER}Testing PHAROS (GraphQL)...{C_END}")
    url = "https://pharos-api.ncats.io/graphql"
    query = """
    query targetDetails($term: String!) {
      target(q: {sym: $term}) {
        name
        tdl
      }
    }
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json={"query": query, "variables": {"term": gene}})
        if resp.status_code == 200:
            data = resp.json()
            target = data.get("data", {}).get("target", {})
            print(f"{C_OK}✅ SUCCESS: PHAROS API is responsive.{C_END}")
            print(f"{C_DATA}   Sample Result: {target.get('name')} (TDL: {target.get('tdl')}){C_END}")
        else:
            print(f"{C_FAIL}❌ FAILED: Status {resp.status_code}{C_END}")

async def test_depmap(gene):
    print(f"{C_HEADER}Testing DepMap (REST)...{C_END}")
    # Using a common search endpoint with a User-Agent to avoid the 404/Block
    url = f"https://depmap.org/portal/api/gene/{gene}"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    async with httpx.AsyncClient(headers=headers) as client:
        resp = await client.get(url)
        if resp.status_code == 200:
            try:
                data = resp.json()
                print(f"{C_OK}✅ SUCCESS: DepMap API returned details.{C_END}")
                # Show the internal ID or a small snippet
                print(f"{C_DATA}   Sample Result: Gene ID={data.get('id', 'N/A')}{C_END}")
            except:
                print(f"{C_WARNING}⚠️  NOTICE: Connected but could not parse JSON.{C_END}")
        else:
            print(f"{C_FAIL}❌ FAILED: Status {resp.status_code} (Likely needs specific headers){C_END}")

async def main():
    gene = "EGFR"
    print(f"\n{C_BOLD}{C_INFO}🔬 STARTING MULTI-SOURCE API VERIFICATION FOR: {gene}{C_END}\n")
    
    await test_europe_pmc(gene)
    print("-" * 50)
    await test_open_targets(gene)
    print("-" * 50)
    await test_pharos(gene)
    print("-" * 50)
    await test_depmap(gene)
    
    print(f"\n{C_BOLD}{C_INFO}🏁 ALL TESTS COMPLETED{C_END}\n")

if __name__ == "__main__":
    asyncio.run(main())
