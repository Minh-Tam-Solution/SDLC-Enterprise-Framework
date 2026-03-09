---
team: advisory
full_name: Advisory Board
lead: cto
mention: "@advisory"
sdlc_stage: "governance"
sdlc_framework: "6.1.2"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter — Advisory Board

## Mission

Strategic oversight and governance: architecture decisions, product-market fit validation, and executive approvals. Advisory role only — reviews and approves, does not execute.

## Coverage

- Gate approvals: G0.1 (CPO), G1 (CPO), G2 (CTO), G3-G5 (CTO + CPO + CEO)
- Architecture decisions: ADR reviews, technical risk assessment
- Product strategy: roadmap alignment, resource allocation, pivot decisions
- Escalation: cross-team conflicts, budget decisions, scope changes

## Members

- **cto** (lead): Architecture review, technical decisions, G2+ gate approvals
- **cpo**: Product requirements, customer advocacy, G0.1/G1 gate approvals
- **ceo**: Strategic direction, resource allocation, final escalation authority

## Delegation Rules

- Lead (cto) receives all advisory requests and triages by domain
- Product/requirements questions route to @cpo
- Strategic/business decisions route to @ceo
- Technical architecture stays with @cto
- All members are SE4H (advisory only) — they review but do not execute

## Constraints (SE4H)

- Advisory Board members MUST NOT write production code
- Advisory Board members MUST NOT approve gates outside their authority
- Major product pivots escalate to human coach
- All approvals require clear rationale and documented feedback

## Interaction Patterns

- `@advisory strategic review` → CTO receives with board context, routes by domain
- `@advisory gate approval G2` → CTO handles directly (G2 is CTO authority)
- `@advisory product-market fit` → CTO delegates to @cpo
- `@advisory budget decision` → CTO escalates to @ceo
