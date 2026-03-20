# Add a New Evidence Collector

1. Add a new `SourceName` enum value in `agent/schema.py`.
2. Implement connector class in `mcp_server/connectors/<source>.py` extending `CollectorConnector`.
3. Return `tuple[list[EvidenceRecord], SourceStatus, list[ErrorRecord]]` from `collect()`.
4. Register connector in `mcp_server/connectors/__init__.py`.
5. Add MCP tool entry + routing in `mcp_server/server.py`.
6. Add a LangGraph node in `agent/graph.py` and connect it before `merge`.
7. Add tests for schema, connector behavior, and graph integration.
