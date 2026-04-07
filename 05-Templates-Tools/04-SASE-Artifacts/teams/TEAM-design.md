---
team: design
archetype: design
sdlc_framework: "6.3.0"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter - Design Team

## Mission

Own the **HOW** of the system. Transform requirements into architecture, technical specifications, and integration contracts. Every line of code must have a design document backing it.

## Coverage

| SDLC Stage | Responsibility |
|------------|---------------|
| 02-Design | Architecture decisions (ADRs), technical specs, API contracts |
| 03-Integrate | Integration specifications, contract definitions |

## Leader

**@architect** — Owns all architecture decisions. Final say on technical approach, patterns, and technology choices.

## Members

| Role | Responsibility | When Active |
|------|---------------|-------------|
| @architect | ADRs, technical specs, system design | Stage 02-03 |
| @pm | Requirements clarification, acceptance criteria validation | Stage 02 (advisory) |
| @coder | Implementation feasibility input, effort estimation | Stage 02 (advisory) |
| @cso | Security architecture review, threat model, AGPL containment | Stage 02 (advisory, PRO+ tier) |

## Gates

| Gate | Stage | Team Role | Criteria |
|------|-------|-----------|----------|
| G2 | 02 | Proposer | Design approved, ADRs documented, API contracts defined |

## Workflow

```
1. @architect receives requirements from Planning team (post-G1)
   └── Input: docs/01-planning/requirements.md

2. @architect creates architecture decision records
   └── Deliverable: docs/02-design/01-ADRs/ADR-XXX.md

3. @architect writes technical specifications
   └── Deliverable: docs/02-design/TS-XXX.md (API contracts, data models)

4. @pm clarifies requirements if architect has questions
   └── Format: [@pm: Acceptance criteria unclear for <feature> — X or Y?]

5. @coder provides effort estimation and feasibility input
   └── Format: [@coder: Can you estimate effort for <approach>?]

6. @cso reviews security posture (PRO+ tier)
   └── Verify: threat model, auth design, AGPL containment, API security

7. Submit for G2 gate review
```

## Delegation Rules

The **@architect** (leader) coordinates all design work:

- `[@pm: Need clarification on requirements for <feature>]`
- `[@coder: Estimate implementation effort for <technical approach>]`

Only delegate clarification and estimation tasks. Do not delegate implementation.

## Policies

### Design Document Completeness
Every feature entering Stage 04 (Build) MUST have:
- ADR for non-trivial decisions (Status: Accepted)
- Technical spec with API contracts and data models
- Integration spec if touching external systems

### No Design-by-Implementation
Design documents come FIRST. Implementation follows design, not the other way around. If a coder discovers the design is incomplete mid-implementation, they must STOP and escalate back to the design team.

### Handoff to Dev
When G2 passes, design hands off to the Development team:
```
[@dev: Design complete for <feature>. G2 passed.
Key docs:
- ADR: docs/02-design/01-ADRs/ADR-XXX.md
- Spec: docs/02-design/TS-XXX.md
Ready for implementation.]
```

## Tier Availability

| Tier | Available |
|------|-----------|
| LITE | No (use @fullstack) |
| STANDARD | No (architect in @planning advisory) |
| PROFESSIONAL | Yes |
| ENTERPRISE | Yes |
