import httpx
import asyncio
import csv
import io
import os
import pytest

async def test_depmap_csv_access():
    if os.getenv("RUN_NETWORK_TESTS") != "1":
        pytest.skip("Set RUN_NETWORK_TESTS=1 to run DepMap live network test.")

    print("🚀 Starting DepMap CSV Access Test...")
    
    files_api = "https://depmap.org/portal/api/download/files"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        # 1. Fetch file list
        print(f"📡 Requesting file list from: {files_api}")
        response = await client.get(files_api, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to get file list: {response.status_code}")
            return
            
        # Parse CSV file list
        csv_data = response.text
        reader = csv.DictReader(io.StringIO(csv_data))
        
        target_url = None
        for row in reader:
            # We want CRISPRGeneEffect.csv from the latest release
            if row.get('filename') == 'CRISPRGeneEffect.csv':
                target_url = row.get('url')
                break
        
        if not target_url:
            print("❌ Could not find CRISPRGeneEffect.csv in the file list.")
            return
            
        print(f"✅ Found CRISPR URL: {target_url[:60]}...")
        
        # 2. Test Partial Download (Range request)
        print("📡 Testing partial download (first 2KB)...")
        # Note: Some GCS links might not support Range, lets try a simple stream first
        try:
            async with client.stream("GET", target_url, headers=headers) as stream:
                if stream.status_code != 200:
                    print(f"❌ Download stream failed: {stream.status_code}")
                    return
                
                chunk = None
                async for c in stream.aiter_bytes():
                    chunk = c
                    break
                if chunk is None:
                    print("❌ No data received.")
                    return
                print(f"✅ Successfully downloaded {len(chunk)} bytes.")
                header_line = chunk.decode('utf-8').split('\n')[0]
                print(f"📝 Header Snippet: {header_line[:100]}...")
                
                if "gene" in header_line.lower() or "achilles" in header_line.lower():
                    print("📊 Verification SUCCESS: File contains gene/cell-line data.")
                else:
                    print("⚠️ Warning: Header doesn't look like gene effect data.")
        except Exception as e:
            print(f"❌ Error during download test: {e}")

if __name__ == "__main__":
    asyncio.run(test_depmap_csv_access())
