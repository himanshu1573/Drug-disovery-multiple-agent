#!/usr/bin/env python3
"""
One-time DepMap dataset downloader.
Downloads CRISPRGeneEffect.csv (~300MB) from the Broad Institute DepMap portal
and saves it to the local cache so the Evidence Collector can use it instantly.

Run once:
    python3 scripts/download_depmap.py

After this, `collect.py --sources depmap` will work instantly from local cache.
"""
import asyncio
import csv
import io
import os
import time
from pathlib import Path

import httpx

ROOT_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT_DIR / "mcps" / "connectors" / ".depmap_cache"
CACHE_FILE = CACHE_DIR / "CRISPRGeneEffect.csv"
FILES_API = "https://depmap.org/portal/api/download/files"


async def main():
    print("=" * 60)
    print("  DepMap One-Time Dataset Downloader")
    print("=" * 60)

    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"\n📡 Fetching file list from DepMap...")
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(FILES_API, headers=headers)
        resp.raise_for_status()
        raw = resp.text

    reader = csv.DictReader(io.StringIO(raw))
    csv_url = None
    release_name = None
    for row in reader:
        if row.get("filename") == "CRISPRGeneEffect.csv":
            csv_url = row.get("url")
            release_name = row.get("release")
            break

    if not csv_url:
        print("❌ Could not find CRISPRGeneEffect.csv in the DepMap file list.")
        return

    print(f"✅ Found dataset: {release_name}")
    print(f"   URL: {csv_url[:60]}...")
    print(f"\n📥 Downloading to: {CACHE_FILE}")
    print("   This is a ~300MB file. Please wait...\n")

    os.makedirs(CACHE_DIR, exist_ok=True)
    t0 = time.perf_counter()
    downloaded = 0

    async with httpx.AsyncClient(timeout=300.0, follow_redirects=True) as client:
        async with client.stream("GET", csv_url, headers=headers) as stream:
            stream.raise_for_status()
            total = int(stream.headers.get("content-length", 0))

            with open(CACHE_FILE, "wb") as f:
                async for chunk in stream.aiter_bytes(chunk_size=65536):
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total:
                        pct = downloaded / total * 100
                        mb = downloaded / 1024 / 1024
                        print(f"\r   {pct:.1f}% ({mb:.1f} MB downloaded)", end="", flush=True)

    elapsed = time.perf_counter() - t0
    size_mb = os.path.getsize(CACHE_FILE) / 1024 / 1024
    print(f"\n\n✅ Download complete!")
    print(f"   File size : {size_mb:.1f} MB")
    print(f"   Time taken: {elapsed:.1f}s")
    print(f"   Saved to  : {CACHE_FILE}")
    print(f"\n🚀 You can now run:")
    print(f"   python3 collect.py --gene EGFR --sources depmap")
    print(f"   python3 collect.py --gene BRAF --sources depmap")
    print()


if __name__ == "__main__":
    asyncio.run(main())
