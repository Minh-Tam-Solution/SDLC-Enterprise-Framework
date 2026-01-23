# Situation-Specific Guides

**Version**: 5.1.3
**Date**: January 2025
**Stage**: 02 - Core Methodology (Documentation Standards)
**Pillar**: Cross-Pillar Reference Guides
**Status**: ACTIVE - Production Standard
**Authority**: CTO Office

---

## Purpose

Situation-Specific Guides provide **step-by-step instructions** for common SDLC situations. Unlike reference documents, these guides are:
- **Action-oriented**: Tell you what to do, step-by-step
- **Context-aware**: Specific to a particular situation
- **Checklist-based**: Verifiable completion criteria

**Philosophy**: "When you're in this situation, follow these steps."

---

## Available Guides

### Sprint Planning Guides (Pillar 2)

| Guide | Situation | Key Actions |
|-------|-----------|-------------|
| [When-Planning-Sprint.md](./When-Planning-Sprint.md) | Starting a new sprint | Pre-sprint checklist, Planning Hierarchy alignment, G-Sprint gate passage |

### Upcoming Guides (Planned)

| Guide | Situation | Status |
|-------|-----------|--------|
| When-Scope-Changes-Mid-Sprint.md | Scope change request during sprint | Planned |
| When-Sprint-Fails-Goals.md | Sprint didn't meet objectives | Planned |
| When-Carryover-Items-Pile-Up.md | Multiple sprints with carryover | Planned |
| When-Switching-Phase.md | Transitioning between Roadmap phases | Planned |
| When-Onboarding-New-Team-Member.md | New member joins mid-sprint | Planned |
| When-Technical-Debt-Blocks-Sprint.md | Tech debt impacts sprint capacity | Planned |

---

## Guide Structure Standard

All Situation-Specific Guides follow this structure:

```markdown
# When [Situation]

## Overview
- When to use this guide
- Prerequisites

## Pre-[Action] Checklist
- [ ] Verification steps
- [ ] Required approvals

## Step-by-Step Process
### Step 1: [Action]
### Step 2: [Action]
...

## Post-[Action] Verification
- [ ] Completion criteria
- [ ] Documentation requirements

## Common Pitfalls
- What to avoid

## Related Documents
- Cross-references
```

---

## Pillar Integration

| Pillar | Related Guides |
|--------|---------------|
| **Pillar 0: Design Thinking** | When-Problem-Definition-Changes.md (planned) |
| **Pillar 1: 10-Stage Lifecycle** | When-Switching-Phase.md (planned) |
| **Pillar 2: Sprint Planning Governance** | ✅ When-Planning-Sprint.md |
| **Pillar 3: 4-Tier Classification** | When-Upgrading-Project-Tier.md (planned) |
| **Pillar 4: Quality Gates** | When-Gate-Fails.md (planned) |
| **Pillar 5: SASE Integration** | When-Security-Audit-Required.md (planned) |
| **Pillar 6: Documentation Permanence** | When-SSOT-Conflict-Detected.md (planned) |

---

## Quick Reference: Sprint Planning

When planning a sprint, follow [When-Planning-Sprint.md](./When-Planning-Sprint.md):

```yaml
Step 1: Verify Previous Sprint Closed
  - G-Sprint-Close gate passed
  - SPRINT-INDEX.md updated
  - Retro documented

Step 2: Review Roadmap Alignment
  - Check current Phase
  - Verify sprint number
  - Run SSOT validation

Step 3: Gather Sprint Inputs
  - Previous sprint carryover
  - Backlog priorities
  - Dependency status

Step 4: Execute Planning
  - Set Sprint Goal
  - Define Scope (boundaries!)
  - Calculate capacity
  - Assign stories

Step 5: Pass G-Sprint Gate
  - Sprint Plan complete
  - Scope explicitly defined
  - Acceptance criteria set
  - Dependencies declared
```

---

## Related Documents

- [SDLC-Sprint-Planning-Governance.md](../../Governance-Compliance/SDLC-Sprint-Planning-Governance.md) - Full governance framework
- [SDLC-Core-Methodology.md](../../SDLC-Core-Methodology.md) - 7-Pillar Architecture
- [SPRINT-TEMPLATE.md](../../../05-Templates-Tools/5-Project-Templates/PLANNING-HIERARCHY-TEMPLATE/SPRINT-TEMPLATE.md) - Sprint template

---

**Document Status**: ACTIVE
**Compliance**: Reference Guide
**Last Updated**: January 2025
**Owner**: CTO Office
