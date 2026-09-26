---
title: "Citizen Developer Guide"
version: "6.3.1"
ring: 3
iceberg_layer: "Events"
dt_phase: "Empathize + Prototype"
sdlc_version: "6.3.1"
last_updated: "2026-03-18"
status: "ACTIVE"
---

# Citizen Developer Guide

> **Ring 3 (Outer)** — Implementation guide for non-technical users building with AI agents.
> Implements Mental Model #8: "More People Build, Under Guardrails."

## 1. Who Is This For?

This guide is for **domain experts** — PMs, legal staff, finance teams, operations managers — who want to automate workflows using AI agents without writing code.

**Important**: This is an EMERGING practice. Start with internal tools only, under supervision.

## 2. Three Mandatory Boundaries

### Boundary 1: Use-Case Limits
- ✅ **ALLOWED**: Internal workflow automation, data reports, notification bots, template generation
- ❌ **NOT ALLOWED**: Customer-facing applications, payment processing, PII handling, security-sensitive tools

### Boundary 2: Escalation Rules
Any agent action touching these domains **automatically escalates to technical staff**:
- Authentication/authorization changes
- Payment or financial transactions
- Personal Identifiable Information (PII)
- Database schema modifications
- External API integrations
- Security configurations

### Boundary 3: Template-Only Rule
Citizens build **FROM templates**, not from scratch.
- All templates are pre-validated by automated security scanning (SAST)
- Custom code blocks are scanned before deployment
- No direct database access — only through approved API endpoints

## 3. Getting Started (30-Minute Pathway)

### Step 1: Choose Your Template (5 min)

| Template | Use Case | Complexity |
|----------|----------|------------|
| **Notification Bot** | Send alerts when conditions met | Simple |
| **Report Generator** | Aggregate data into formatted report | Simple |
| **Approval Workflow** | Route requests through approval chain | Medium |
| **Data Sync** | Keep two systems in sync | Medium |
| **Dashboard Widget** | Visual display of key metrics | Medium |

### Step 2: Configure via Conversation (10 min)

Use chat to configure your tool:
```
You: Create a notification bot
Agent: I'll help. What should trigger the notification?
You: When a new gate evaluation fails
Agent: Who should receive the notification?
You: The project PM and the gate reviewer
Agent: Created! Here's your bot configuration:
  Trigger: gate evaluation failed
  Recipients: project PM, gate reviewer
  Channel: chat notification
  Shall I activate it?
```

### Step 3: Test in Sandbox (10 min)
- All citizen-built tools run in sandbox first
- Sandbox has read-only access to production data
- Test with sample data before going live

### Step 4: Request Activation (5 min)
- Submit activation request (auto-creates evidence trail)
- Technical staff reviews (automated security scan + human review)
- Activation or feedback within 24 hours

## 4. Autonomy Level

Citizen developers operate at **LITE tier** with **assist_only** autonomy:
- Agent **suggests** actions, human **approves** every execution
- No autonomous code generation
- No direct system modifications
- All outputs reviewed before deployment

## 5. Quality Gates for Citizen-Built Tools

Simplified gate process (not full SDLC):

| Gate | Requirement | Who Reviews |
|------|------------|-------------|
| G0 | Problem statement defined | Self |
| G1 | Template selected, configuration complete | Auto-validated |
| G2 | Security scan passes | Automated |
| G3 | Technical staff approval | Human (technical) |

## 6. Examples: Before/After

### Example 1: Monthly Report
**Before**: PM manually exports data from 3 systems, formats in spreadsheet, emails to stakeholders. Takes 4 hours/month.
**After**: Chat command → Agent queries API, formats report, sends to stakeholders. Takes 2 minutes.

### Example 2: Approval Routing
**Before**: Gate approval requests sent via email, often lost. Average response time: 3 days.
**After**: Chat command → Agent creates evidence bundle, notifies reviewer with approval link, tracks response. Average response time: 4 hours.

## 7. Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent won't execute my request | Check if request crosses Boundary 1 (use-case limits) |
| "Escalated to technical staff" message | Your request touches a restricted domain (Boundary 2) |
| Template doesn't fit my need | Request a custom template via technical team — do NOT modify existing ones |
| Tool stopped working after update | Check if underlying API changed — report via your support channel |

## 8. Graduating to Developer Tools

If you need capabilities beyond citizen developer boundaries:
1. Complete the "SDLC Fundamentals" training (08-Training-Materials/)
2. Request STANDARD tier access from your team admin
3. You'll gain access to higher autonomy — agents execute code, but you approve gates

---

## Further Reading

> This guide is self-contained. References below are for deeper study.

**Framework References**:
- Mental Model #8: "More People Build, Under Guardrails" (02-Core-Methodology/SDLC-System-Thinking-Foundation.md)
- LITE Tier Requirements (02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md)

**Industry**:
- Anthropic: "2026 Agentic Coding Trends Report" — Trend 7: Non-technical use cases
- Singapore MGF Dimension 4: End-User Responsibility

---

**Document Status**: ACTIVE
**Framework Version**: SDLC 6.3.1
**Last Updated**: March 18, 2026
