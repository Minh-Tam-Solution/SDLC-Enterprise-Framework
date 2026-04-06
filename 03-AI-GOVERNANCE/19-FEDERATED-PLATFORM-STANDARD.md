---
title: "Federated Platform Standard — BRAIN/VOICE/HANDS/ADVISOR"
version: "6.3.0"
ring: 1
sdlc_version: "6.3.0"
last_updated: "2026-04-06"
status: "ACTIVE"
pillar: "NEW — Federated Platform"
source: "CEO Federated AI OS Workflow v3 + ADR-083 + V2 Independence Principle"
---

# Federated Platform Standard — BRAIN/VOICE/HANDS/ADVISOR

> NEW in Framework 6.3.0. Defines how multiple AI platforms collaborate without creating circular dependencies.

## 4-Tool Ecosystem

| Tool | Role | Mandate | Purpose |
|------|------|---------|---------|
| **Claude Code** | HANDS | Mandatory | Developer writes code in IDE |
| **SDLC Orchestrator** | BRAIN | Mandatory | Quality gates verify + governance |
| **MTClaw** | VOICE | Mandatory | Team AI agents execute |
| **EndiorBot** | ADVISOR | Optional (OSS) | Personal AI assistant |

## Boundaries (Non-Negotiable)

```
BRAIN (Orchestrator):
  CAN:    evaluate gates, collect evidence, track sprints, approve/reject
  CANNOT: execute code, run agents for coding tasks, write to repos

VOICE (MTClaw):
  CAN:    execute agents, run tools, produce evidence, coordinate team
  CANNOT: approve gates, set policy, bypass governance

HANDS (Claude Code):
  CAN:    write code, run tests, debug, refactor
  CANNOT: approve gates, skip review, self-merge

ADVISOR (EndiorBot):
  CAN:    brainstorm, consult, research, personal productivity
  CANNOT: produce company deliverables, bypass governance
```

## Integration Principles

### V2 Independence Principle
> V2 works standalone without MTClaw. MTClaw integration is additive, not dependency.

- Evidence ingestion accepts from ANY source (MTClaw, manual, API, CI/CD)
- All evidence sources treated equally — no preference for MTClaw-produced evidence
- Gate evaluation works with zero MTClaw evidence

### One-Way Data Flow
```
MTClaw → Evidence → Orchestrator → Gate Decision
  (producer)   (push)    (consumer)     (authority)
```
No reverse dependency. Orchestrator never pulls from MTClaw.

### Open Edge — Closed Core
- **Open Edge**: EndiorBot (OSS) — drives adoption, brand, community
- **Closed Core**: Orchestrator + MTClaw — enterprise governance + execution (SaaS revenue)
- **Foundation**: SDLC Framework (open methodology, Apache-2.0) — competitive moat from expertise

## Shared Infrastructure

Shared services that all platforms consume (NOT owned by any single platform):

| Service | Example | Owner |
|---|---|---|
| AI-Platform | LLM inference, RAG, code-review-graph | IT Admin |
| Ollama | Local models | IT Admin |
| MinIO | Object storage | IT Admin |
| PostgreSQL | Databases (per-platform) | IT Admin |

## Policy: Company Deliverables

```
Company deliverables MUST flow through MTClaw + Orchestrator (evidence trail).
EndiorBot output = advisory only, NOT executable artifact.
Gates CANNOT be bypassed — Orchestrator is the only authority.
```
