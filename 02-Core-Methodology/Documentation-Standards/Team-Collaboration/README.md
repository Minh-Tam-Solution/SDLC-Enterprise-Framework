# Team Collaboration Standards

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Documentation Standards)
**Status**: ACTIVE - Production Standard
**Authority**: CPO Office

---

## Purpose

Define **team collaboration standards** for multi-team coordination across distributed, hybrid, and co-located teams. These standards are **methodology-agnostic** - they work regardless of team location or structure.

**Key Insight**: "Remote Team" vs "Local Team" is a false dichotomy. All teams (Team A, Team B, Team C...) need the same coordination patterns - the location is secondary to the **structure, roles, and handoff protocols**.

---

## Documents in This Section

| Document | Purpose | Tier Required |
|----------|---------|---------------|
| [SDLC-Team-Communication-Protocol.md](./SDLC-Team-Communication-Protocol.md) | Tiered communication requirements (LITE → ENTERPRISE) | ALL tiers |
| [SDLC-Team-Collaboration-Protocol.md](./SDLC-Team-Collaboration-Protocol.md) | Multi-team coordination (N teams) | STANDARD+ |
| [SDLC-Escalation-Path-Standards.md](./SDLC-Escalation-Path-Standards.md) | 4-level escalation framework | STANDARD+ |

---

## Quick Start by Tier

### LITE Tier (1-2 people)
```yaml
Required:
  - Basic communication (async Slack/Discord)
  - No formal protocol needed

Recommended:
  - Weekly sync meeting (optional)
```

### STANDARD Tier (3-10 people)
```yaml
Required:
  - SDLC-Team-Communication-Protocol.md (daily async updates)
  - Basic escalation path (PM → Lead)

Recommended:
  - Weekly planning meeting
  - Sprint retrospectives
```

### PROFESSIONAL Tier (10-50 people)
```yaml
Required:
  - Full SDLC-Team-Collaboration-Protocol.md (multi-team)
  - SDLC-Escalation-Path-Standards.md (4-level)
  - RACI matrix per deliverable
  - Handoff protocols documented

Recommended:
  - Team Topologies applied
  - Cross-team sync cadence
```

### ENTERPRISE Tier (50+ people)
```yaml
Required:
  - Everything in PROFESSIONAL
  - Formal CAB process
  - SLA requirements (<4h PM, <8h CEO)
  - Multiple team types (Stream-aligned, Platform, Enabling)

Mandatory Documentation:
  - Team charters
  - Dependency maps
  - Escalation matrices
```

---

## Core Principles

### Principle 1: Teams, Not Locations

```yaml
Old Thinking (Wrong):
  - "Remote Team" vs "Local Team"
  - Location-based protocols
  - Timezone as primary concern

New Thinking (Correct):
  - Team A, Team B, Team C...
  - Function-based protocols
  - Deliverables as primary concern
  - Location = implementation detail
```

### Principle 2: Explicit Handoffs

```yaml
Every team-to-team interaction needs:
  1. Clear trigger (when does handoff happen?)
  2. Acceptance criteria (DoD for handoff)
  3. Documentation requirements
  4. Feedback loop (how to request changes?)
```

### Principle 3: Escalation Before Assumption

```yaml
Rule: "Ask Before You Guess"
  - When unclear → Ask immediately
  - Never self-assume business logic
  - Follow escalation path (Level 0 → Level 3)
  - Document decisions made
```

### Principle 4: RACI Clarity

```yaml
For every deliverable:
  R - Responsible: Who does the work?
  A - Accountable: Who approves?
  C - Consulted: Who provides input?
  I - Informed: Who needs updates?
```

---

## Multi-Team Coordination Framework

### Team Structure Template

```yaml
Team [X]:
  Name: [Team Name]
  Role: [Primary responsibility]
  Members: [Number + key roles]
  Deliverables: [What this team produces]
  Dependencies:
    Upstream: [Teams providing input]
    Downstream: [Teams receiving output]
  Sync Cadence: [Daily/Weekly with whom]
```

### Example: 3-Team Setup

```yaml
Team A - Design:
  Role: Architecture, UI/UX, API contracts
  Members: 3 (Architect, 2 Designers)
  Deliverables: ADRs, Figma designs, OpenAPI specs
  Dependencies:
    Upstream: None (starting point)
    Downstream: Team B (receives designs)
  Sync: Daily standup 9AM, Wed 3PM with Team B

Team B - Implementation:
  Role: Backend + Frontend development
  Members: 5 (2 Backend, 2 Frontend, 1 DevOps)
  Deliverables: Working code, tests, docs
  Dependencies:
    Upstream: Team A (receives designs)
    Downstream: Team C (provides code)
  Sync: Daily standup 10AM, Wed 3PM with A, Fri 2PM with C

Team C - QA & Operations:
  Role: Testing, deployment, monitoring
  Members: 2 (QA Lead, SRE)
  Deliverables: Test reports, runbooks, alerts
  Dependencies:
    Upstream: Team B (receives code)
    Downstream: Production
  Sync: Daily standup 11AM, Fri 2PM with Team B
```

---

## Industry Standards Alignment

| Standard | Integration Point |
|----------|------------------|
| **Team Topologies** | 4 team types (Stream-aligned, Platform, Enabling, Complicated-Subsystem) |
| **SAFe 6.0** | Lean governance, PI Planning concepts |
| **DORA Metrics** | Team performance measurement |
| **ITIL 4** | Escalation and incident management |

---

## Related Documents

- [02-Core-Methodology/SDLC-Core-Methodology.md](../../SDLC-Core-Methodology.md) - 10-stage framework
- [02-Core-Methodology/Governance-Compliance/](../Governance-Compliance/) - Quality & Security gates
- [03-Templates-Tools/5-Project-Templates/](../../../03-Templates-Tools/5-Project-Templates/) - Project templates

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office

