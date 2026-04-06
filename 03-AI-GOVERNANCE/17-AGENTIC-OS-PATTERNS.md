---
title: "Agentic OS Patterns — Production-Verified Architecture Standards"
version: "6.3.0"
ring: 2
sdlc_version: "6.3.0"
last_updated: "2026-04-06"
status: "ACTIVE"
pillar: "NEW — Agentic OS Patterns"
source: "Giải phẫu Agentic OS (Lâm Nguyễn, 18 patterns from 513K LOC Claude Code) + SDLC Orchestrator v2 production validation"
---

# Agentic OS Patterns — Production-Verified Architecture Standards

> NEW in Framework 6.3.0. 12 of 18 patterns validated in production by SDLC Orchestrator v2 (Sprint 9-16, 352 tests).

## Context

"Giải phẫu một Agentic Operating System" (Lâm Nguyễn, April 2026) extracted 18 architectural patterns from 513,000 lines of Claude Code production source code. These patterns are universal — applicable to any agentic system, not just coding tools.

SDLC Orchestrator v2 implemented 12 of these patterns across 7 sprints, validating them in a governance platform context. This document codifies the validated patterns as formal SDLC Framework methodology.

## 12 Validated Patterns

### Pipeline 2: Query Loop (Heart)

| # | Pattern | V2 Implementation | Sprint | Tests |
|---|---------|-------------------|--------|-------|
| **#1** | Async Generator Control Flow | 8-state agent loop (`agent_loop.py`) | S8 | 25 |
| **#2** | Derived Stop Signals | `needsFollowUp` from content, not API `stop_reason` (`tool_parser.py`) | S9b | 12 |
| **#3** | Escalating Recovery | 3-level: retry ×3 → escalate tokens/turns → surface error (`recovery.py`) | S9b | 15 |

### Pipeline 3: Tool Orchestration (Hands)

| # | Pattern | V2 Implementation | Sprint | Tests |
|---|---------|-------------------|--------|-------|
| **#4** | Concurrency-safe Partitioning | `CONCURRENT_SAFE_TOOLS` frozenset, asyncio.gather for read-only (`tool_executor.py`) | S11 | 14 |
| **#11** | Dangerous Pattern Detection | 5-category bash classifier: read_only/network/file_mutate/package/destructive (`bash_classifier.py`) | S12 | 13 |
| **#12** | Shell Rule Matching | 18 default rules + project override, first-match-wins (`shell_rules.py`) | S12 | 5 |
| **#13** | Cost Tracking | Token usage per session + daily budget alerts (`cost_tracker.py`) | S12 | 3 |

### Pipeline 4: Multi-Agent Coordination (Swarm)

| # | Pattern | V2 Implementation | Sprint | Tests |
|---|---------|-------------------|--------|-------|
| **#7** | Coordinator Restriction | PM/Architect CANNOT use execution tools — 7-step permission pipeline (`permissions.py`) | S9a | 20 |
| **#8** | Fork Isolation | Git worktree per agent + merge back + conflict detection (`fork_manager.py`) | S15 | 5 |
| **#10** | Permission Classification | 7-step pipeline: deny→prefix→coordinator→readonly→destructive→write→read (`permissions.py`) | S9a | 20 |

### Pipeline 5: Context Management (Memory)

| # | Pattern | V2 Implementation | Sprint | Tests |
|---|---------|-------------------|--------|-------|
| **#9** | Context Defense (5-layer) | L1 truncation → L2 microcompact → L3 auto-compact → L4 reactive → L5 collapse (`context_defense.py`) | S9c, S13 | 18 |
| **#14** | Memory System | Per-agent cross-session memory: extract/recall/attach (`agent_memory.py`) | S14 | 15 |

## Implementation Guidelines

### For New Agentic Systems

1. **Start with Pattern #1** (Agent Loop) — the async generator state machine is the foundation
2. **Add Pattern #10** (Permission Pipeline) immediately — security before features
3. **Add Pattern #3** (Escalating Recovery) early — graceful failure handling
4. **Add Pattern #9** (Context Defense) when sessions > 10 iterations
5. **Add Pattern #4** (Concurrency) when tool count > 5

### For Existing Systems

1. **Audit** against pattern checklist — which patterns are missing?
2. **Prioritize** by risk: #10 (permissions) > #3 (recovery) > #9 (context) > #4 (concurrency)
3. **Validate** each pattern with tests before claiming implementation

## Remaining Patterns (Phase 3-4)

| # | Pattern | Status | Target |
|---|---------|--------|--------|
| #5 | Streaming Tool Execution | Deferred — CLI subprocess handles internally | Phase 4 |
| #6 | Context Modifier Chain | Interface defined (ToolResult.context_mods), injection in Phase 4 | Phase 4 |
| #15 | MCP Integration | CRG tools via AI-Platform MCP | Phase 3 (Sprint 18) |
| #16 | Dynamic Discovery | MCP tool discovery endpoint operational | Phase 3 (Sprint 18) |
| #17 | Native Replacement | N/A — web-first platform, not terminal | — |
| #18 | Terminal-as-Browser | N/A — web-first platform | — |
