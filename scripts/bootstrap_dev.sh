#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-venv}"

echo "[bootstrap] creating virtualenv at $VENV_DIR"
"$PYTHON_BIN" -m venv "$VENV_DIR"

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

echo "[bootstrap] upgrading pip"
pip install --upgrade pip

echo "[bootstrap] installing root dependencies"
pip install -r requirements.txt

echo "[bootstrap] installing test tooling"
pip install pytest pytest-asyncio

echo "[bootstrap] installing local MCP packages (editable)"
pip install -e deepmap-mcp
pip install -e literature-mcp
pip install -e external_mcps/open-targets-platform-mcp

echo "[bootstrap] downloading DepMap dataset (optional, ~300MB)"
# Run the download script; if it fails (e.g. no internet), we just warn but continue.
python3 scripts/download_depmap.py || echo "[bootstrap] WARNING: DepMap download failed. You may need to run it manually later."

echo "[bootstrap] done"
echo "Next: source $VENV_DIR/bin/activate && ./scripts/test_smoke.sh"
