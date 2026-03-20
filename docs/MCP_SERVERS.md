# Source-specific MCP servers

Agent4Target uses a hybrid MCP setup:

- Internal source MCP servers (stdio):

- `python3 -m mcp_server.depmap_mcp`
- `python3 -m mcp_server.literature_mcp`

- External MCP servers:
- Open Targets official MCP (stdio): `external_mcps/open-targets-platform-mcp/.venv/bin/otp-mcp --transport stdio`
- PHAROS community MCP (SSE): `cd external_mcps/pharos-mcp-server && HOME=. npx wrangler dev --ip 127.0.0.1 --port 8787`

## Tool names

- DepMap: `depmap_collect_target_evidence`
- PHAROS (external): `pharos_graphql_query` (via community MCP SSE server)
- Open Targets (external): `search_entities`, `query_open_targets_graphql` (official MCP)
- Literature: `literature_collect_target_evidence`

## Notes

- By default, connectors use live APIs (`A4T_OFFLINE_MODE=0`).
- Set `A4T_OFFLINE_MODE=1` for deterministic local output.
- Set `response_format=json` for machine-readable output.
- LangGraph agent orchestration calls internal stdio MCPs and external MCPs via `/Users/apple/Projects/Agent4agent/agent/mcp_runtime.py`.
