#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${SCRIPT_DIR}/pharos-mcp-server"
cd "$ROOT"
export HOME="$ROOT"

exec wrangler dev --ip 127.0.0.1 --port 8787 "$@"
