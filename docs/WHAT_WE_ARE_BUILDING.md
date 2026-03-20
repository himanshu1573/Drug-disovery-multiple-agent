# What We Are Building
## Canonical Product Intent for Phase-1

**Version:** 1.0  
**Date:** March 9, 2026  
**Status:** Canonical alignment document for humans and agents

---

## 1. Build Statement

We are building a **production-ready multi-agent system for drug discovery**, starting with **Phase-1: Evidence Collector**.

Phase-1 exists to automatically **gather, verify, and organize scientific evidence** for a **gene-disease relationship** using multiple biomedical sources.

This is not a single tool-calling bot. It is a **structured team of specialized agents** coordinated by an orchestrator.

The Phase-1 output is a **structured Evidence Dossier** that downstream agents can consume for:
- target prioritization
- pathway analysis
- drug design planning

---

## 2. High-Level Goal

### Input
A query such as:
- `gene = KRAS`
- `disease = Lung Cancer`
- `goal = collect evidence`

### Output
A structured evidence package containing:
- gene-disease associations
- experimental and computational evidence
- literature references
- confidence indicators
- conflict flags
- full provenance

This output is the foundation for later drug discovery phases.

---

## 3. Core Product Idea

Scientists normally do this manually:
- search multiple databases
- read and compare studies
- resolve contradictions
- summarize evidence

This system automates that workflow using specialized agents with explicit responsibilities.

---

## 4. Architecture We Are Implementing

### 4.1 User Input Layer
Collect research request fields:
- gene
- disease
- objective

### 4.2 Orchestration Layer
The orchestrator is the workflow controller. It must:
- execute agent graph deterministically
- maintain state and checkpoints
- handle retries and failures
- coordinate inter-agent handoffs

### 4.3 Planning Agent
Generates collection strategy per request, for example:
1. OpenTargets association query
2. DepMap dependency query
3. PHAROS druggability query
4. Literature evidence query

### 4.4 Evidence Collectors (Parallel)
- DepMap Collector
- OpenTargets Collector
- PHAROS Collector
- Literature Collector

Each returns:
- raw source payloads
- parsed evidence
- source metadata/provenance
- source execution status

### 4.5 Data Processing Layer
Contains three core agents:

#### Normalization Agent
Converts heterogeneous source outputs to canonical schema.

#### Verification Agent
Performs validation and integrity checks:
- schema checks
- duplicate detection
- identifier consistency
- citation completeness

#### Conflict Analyzer
Detects cross-source contradictions and flags severity.

### 4.6 Knowledge Construction
Builds evidence graph relations, e.g.:
- Gene -> Disease -> Evidence -> Publication

### 4.7 Explanation Agent
Generates human-readable evidence summary grounded in verified evidence only.

### 4.8 Human Review Gateway
Allows scientists to:
- approve/reject evidence
- request additional collection
- add trusted references
- adjust confidence with traceable rationale

### 4.9 Evidence Dossier (Phase-1 Output)
Final report contains:
- normalized and verified evidence
- source provenance
- conflicts
- explanation summary
- review decision

### 4.10 Memory System
- Episodic memory: prior runs and outcomes
- Semantic memory: biomedical mappings/facts
- Procedural memory: agent workflows and rules
- Working memory: current run artifacts/state

### 4.11 Retry and Recovery
Orchestrator must support:
- retry on transient failures
- fallback behavior for degraded sources
- escalation to human review for unresolved issues

### 4.12 Future Integration
Evidence dossier is input to later agents such as:
- target prioritization
- pathway reasoning
- drug candidate generation
- experiment planning

---

## 5. Responsibilities of This System

This system is responsible for:
- collecting multi-source biomedical evidence
- validating and structuring evidence
- exposing uncertainty and conflicts
- enabling human scientific oversight
- producing a reliable handoff package for Phase-2

This system is not responsible for:
- final portfolio decision-making
- molecule generation execution
- replacing expert scientific judgment

---

## 6. Anti-Hallucination Build Guardrails (Must Follow)

All implementation agents and contributors must follow these rules:

1. **Do not add new product scope** that is not in this document, PRD, or approved change requests.
2. **Do not invent data sources** beyond the defined Phase-1 collectors unless explicitly approved.
3. **Do not invent output fields** outside versioned contracts.
4. **Do not bypass verification and provenance requirements** when generating summaries.
5. **Do not treat unverified evidence as facts** in dossier conclusions.
6. **Do not skip human review gates** for conflict-heavy or low-coverage runs.
7. **Do not claim Phase-2 functionality** as part of Phase-1 completion.
8. **When uncertain, fail closed**: flag as unknown/needs review instead of fabricating.

---

## 7. Source of Truth Hierarchy

When documents differ, resolve in this order:
1. `docs/WHAT_WE_ARE_BUILDING.md` (this document)
2. `docs/PRD_PHASE1_EVIDENCE_COLLECTOR.md`
3. `docs/COMPLETE_FLOW_AND_RESPONSIBILITIES.md`
4. implementation docs in `docs/ARCHITECTURE*.md`

---

## 8. One-Line Summary

We are building a **multi-agent, verifiable evidence collection platform** for gene-disease research where **Phase-1 outputs a trusted Evidence Dossier** for downstream drug discovery agents.

