#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Cleaning generated runtime artifacts..."

if [ -d "${ROOT}/artifacts" ]; then
  find "${ROOT}/artifacts" -mindepth 1 -maxdepth 2 \
    ! -path "${ROOT}/artifacts/.gitkeep" \
    ! -path "${ROOT}/artifacts/episodic_memory" \
    ! -path "${ROOT}/artifacts/episodic_memory/*" \
    -exec rm -rf {} +
fi

rm -f "${ROOT}/pharos_server.log" 2>/dev/null || true

echo "Done."

