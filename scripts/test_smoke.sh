#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="python3"
if [[ -x "venv/bin/python" ]] && venv/bin/python -m pytest --version >/dev/null 2>&1; then
  PYTHON_BIN="venv/bin/python"
fi

echo "[smoke] collecting root test suite"
"$PYTHON_BIN" -m pytest --collect-only tests -q

echo "[smoke] running root tests only"
"$PYTHON_BIN" -m pytest tests -q
