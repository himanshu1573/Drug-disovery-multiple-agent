# Local MCP setup (external repos)

This workspace has two cloned MCP repos:

- `/Users/apple/Projects/Agent4agent/external_mcps/open-targets-platform-mcp`
- `/Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server`

## 1) Open Targets MCP (Python)

Installed locally in a project venv:

```bash
cd /Users/apple/Projects/Agent4agent/external_mcps/open-targets-platform-mcp
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -e .
.venv/bin/pip install fastmcp==2.13.3 mcp==1.22.0
```

Why pin these versions:
- The repo lockfile (`uv.lock`) pins FastMCP 2.x and MCP 1.22.x.
- Using FastMCP 3.x broke `--list-tools` in local testing.

Verify:

```bash
.venv/bin/otp-mcp --help
.venv/bin/otp-mcp --list-tools
```

Run (stdio):

```bash
HOME=/Users/apple/Projects/Agent4agent/external_mcps/open-targets-platform-mcp \
  .venv/bin/otp-mcp --transport stdio
```

## 2) Pharos MCP (TypeScript / Cloudflare Workers)

Installed locally:

```bash
cd /Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server
npm ci
npm install -D @cloudflare/workerd-darwin-arm64@1.20250424.0 \
  --fetch-retries=5 --fetch-retry-maxtimeout=120000 --fetch-timeout=300000
```

Verify:

```bash
HOME=/Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server npx wrangler --version
HOME=/Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server npx wrangler dev --help
```

Run local dev server (SSE path `/sse`):

```bash
HOME=/Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server \
  npx wrangler dev --ip 127.0.0.1 --port 8787
```

Notes:
- This Pharos repo is Cloudflare/Workers-oriented (SSE endpoint), not stdio-first.
- If inspector port errors appear, set an explicit inspector port:

```bash
HOME=/Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server \
  npx wrangler dev --ip 127.0.0.1 --port 8787 --inspector-port 9230
```

## Repo status checks

```bash
cd /Users/apple/Projects/Agent4agent/external_mcps/open-targets-platform-mcp && git rev-parse --short HEAD
cd /Users/apple/Projects/Agent4agent/external_mcps/pharos-mcp-server && git rev-parse --short HEAD
```
