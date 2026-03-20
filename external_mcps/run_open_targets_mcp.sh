#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/apple/Projects/Agent4agent/external_mcps/open-targets-platform-mcp"
export HOME="$ROOT"

exec "$ROOT/.venv/bin/otp-mcp" --transport stdio "$@"
