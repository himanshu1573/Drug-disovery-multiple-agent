# Drug Discovery Agent Architecture

This document contains a detailed architecture diagram of the implemented system, completely based on the actual source code. It traces the flow of a target query from the CLI down to multiple evidence sources via the Model Context Protocol (MCP) using a LangGraph-based state machine, then through analysis and summary generation.

<div align="center">
  <img src="../public/Agent4target.svg" alt="Drug Discovery Agent Workflow" width="800" />
</div>

```mermaid
flowchart TD
    %% Define Styling
    classDef cli fill:#f9d0c4,stroke:#333,stroke-width:2px;
    classDef graph fill:#d4e6f1,stroke:#333,stroke-width:2px;
    classDef mcp fill:#d5f5e3,stroke:#333,stroke-width:2px;
    classDef ext_mcp fill:#fcba03,stroke:#333,stroke-width:2px;
    classDef summary fill:#e8daef,stroke:#333,stroke-width:2px;
    classDef artifacts fill:#fcf3cf,stroke:#333,stroke-width:2px;

    %% CLI Entrypoint
    subgraph Client [CLI Application]
        CLI[cli/main.py]:::cli
        RunCMD(run --gene --disease)
        ReplCMD(repl loop)
        CLI --> RunCMD
        CLI --> ReplCMD
    end

    %% Agent State Graph
    subgraph AgentGraph [LangGraph Collector Ecosystem (agents/graph.py)]
        RunCMD --> |build_collector_request| initGraph((START))
        ReplCMD --> |build_collector_request| initGraph
        
        initGraph --> N1_validate_input[validate_input]:::graph
        N1_validate_input --> N2_plan_collection[plan_collection]:::graph
        N2_plan_collection --> N3_plan_review_gate[plan_review_gate]:::graph
        
        N3_plan_review_gate --> N4_collect_sources_parallel[collect_sources_parallel]:::graph
        N4_collect_sources_parallel --> N5_normalize_evidence[normalize_evidence]:::graph
        N5_normalize_evidence --> N6_verify_evidence[verify_evidence]:::graph
        N6_verify_evidence --> N7_analyze_conflicts[analyze_conflicts]:::graph
        N7_analyze_conflicts --> N8_assess_sufficiency[assess_sufficiency]:::graph
        
        %% Sufficiency Loop
        N8_assess_sufficiency -- "NEEDS_RECOLLECTION" --> N4_collect_sources_parallel
        
        N8_assess_sufficiency --> N9_build_evidence_graph[build_evidence_graph]:::graph
        N9_build_evidence_graph --> N10_generate_explanation[generate_explanation]:::graph
        
        N10_generate_explanation --> N11_supervisor_decide[supervisor_decide]:::graph
        N11_supervisor_decide --> N12_prepare_review_brief[prepare_review_brief]:::graph
        N12_prepare_review_brief --> N13_human_review_gate[human_review_gate]:::graph
        
        %% Routing after review
        N13_human_review_gate -- "APPROVED / REJECTED" --> N14_emit_dossier[emit_dossier]:::graph
        N13_human_review_gate -- "NEEDS_MORE_EVIDENCE" --> N4_collect_sources_parallel
        
        N14_emit_dossier --> END_G((END))
    end

    %% Evidence Artifacts Generation
    subgraph Storage [Persistence & Artifacts]
        N14_emit_dossier --> |persist_evidence_dossier| Dossier(EvidenceDossier JSON)
        N14_emit_dossier --> |persist_episodic_memory| EpisodicMem(Episodic Memory)
        N9_build_evidence_graph --> GraphArt(Evidence Graph JSON)
    end

    %% MCP Connectors layer
    subgraph MCP_Runtime [MCP Connectors (agents/mcp_runtime.py)]
        N4_collect_sources_parallel --> |Parallel Dispatch| Dispatch_Internal
        N4_collect_sources_parallel --> |Parallel Dispatch| Dispatch_External
    
        Dispatch_Internal --> DepMap(mcps.depmap_mcp)
        Dispatch_Internal --> LitMCP(mcps.literature_mcp)
        
        Dispatch_External --> WrapOT(mcps.opentargets_mcp)
        Dispatch_External --> WrapPharos(mcps.pharos_mcp)
    end

    %% Actual external MCP processes
    subgraph External_MCP_Processes [External Target Systems]
        WrapOT -- "stdio" --> ExtOT[external_mcps/open-targets-platform-mcp/...\n(JS/TypeScript Process)]:::ext_mcp
        WrapPharos -- "SSE :8787" --> ExtPharos[external_mcps/pharos-mcp-server/...\n(Wrangler Dev/Node)]:::ext_mcp
    end
    
    %% Output
    Dossier -.-> |Writes down| MD_SUM[results/GENE_summary.md]:::artifacts
    Dossier -.-> |Returns to| CLI
```

## System Components

1.  **Command-Line Interface (`cli/main.py`)**: Entry point for execution. Orchestrates `run`, `repl`, `review`, and `resume` commands.
2.  **State Machine / Agent Graph (`agents/graph.py`)**: Built on `langgraph`. Manages the 14-node "Lean Flow" pipeline. It handles state transitions, error recovery, and human-in-the-loop interrupts.
3.  **Core Agents (Lean Flow)**:
    - **Input Validation Agent**: Ensures query quality and checks episodic memory.
    - **Planning Agent**: Strategizes source selection and collection directives.
    - **Normalization Agent**: Standardizes heterogeneous source data.
    - **Sufficiency Agent**: Deterministically decides if more evidence is needed.
    - **Summary Agent**: LLM-powered synthesis of verified claims.
    - **Supervisor Agent**: Orthogonal router deciding the final state of the run.
4.  **Model Context Protocol (MCP) Runtime (`agents/mcp_runtime.py`)**: Communicates with local and external data sources (DepMap, Pharos, Open Targets, Literature) using the MCP standard.
5.  **Output & Storage**: Persists working snapshots, episodic memory, and final markdown dossiers in the `artifacts/` and `results/` directories.
