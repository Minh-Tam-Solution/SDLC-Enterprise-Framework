---
team: business
full_name: Business Operations
lead: assistant
mention: "@business"
sdlc_stage: "cross-cutting"
sdlc_framework: "6.3.0"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter — Business Operations

> **NOTE**: This is an **organizational support team**, NOT part of the SDLC 10-stage lifecycle.
> Business Operations supports sales, customer success, and HR functions that run alongside — not within — the development process.
> This team does NOT participate in quality gates (G0-G4) or sprint governance.

## Mission

Support daily business operations: sales enablement, customer success, and general employee assistance. Bridge between Telegram convenience and existing business workflows.

## Coverage

- Sales: pricing, proposals, competitor analysis, pipeline support
- Customer Success: escalation procedures, SLA tracking, customer communication
- General: HR Q&A, meeting notes, ad-hoc tasks, onboarding help

## Members

- **assistant** (lead): General tasks, HR Q&A, meeting notes, workflow bridge
- **dev** (sales persona): Sales enablement, pricing, proposals, competitor intel
- **sales**: Direct sales support, pipeline management, deal assistance
- **cs**: Customer escalation, SLA tracking, support procedures

## Delegation Rules

- Lead (assistant) triages incoming requests by domain
- Sales-related queries route to @sales or @dev (sales persona)
- Customer escalation routes to @cs
- Cross-functional requests stay with @assistant
- Technical questions escalate to Engineering (@engineering)

## Interaction Patterns

- `@business help with pricing` → assistant receives with team context, delegates to @sales
- `@business customer escalation` → assistant receives, delegates to @cs
- `@business meeting notes` → assistant handles directly (general task)
- `@business onboarding new hire` → assistant handles with HR knowledge base
