# 🤝 AI Team Protocol Generator - Stage 08 (COLLABORATE)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 08 - COLLABORATE (Team Management & Documentation)
**Time Savings**: 80%
**Authority**: CPO Office

---

## Purpose

Generate **comprehensive team protocols** for multi-team coordination following SDLC 5.0.0 standards. Covers governance structure, team roles, handoff procedures, and escalation paths.

---

## AI Prompts by Protocol Type

### 1. Multi-Team Collaboration Protocol

```yaml
System Prompt:
  You are generating multi-team collaboration protocols following SDLC 5.0.0 standards.
  Create governance structure, team definitions, RACI matrices, and handoff procedures.
  Reference: Documentation-Standards/Team-Collaboration/SDLC-Team-Collaboration-Protocol.md

User Prompt Template:
  "Generate a multi-team collaboration protocol for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]

   Teams:
   - Team A: [Name], [Size], [Primary Role]
   - Team B: [Name], [Size], [Primary Role]
   - Team C: [Name], [Size], [Primary Role]

   Governance:
   - Project Owner: [Name]
   - Project Manager: [Name]
   - Technical Lead: [Name]

   Work Model: [Co-located | Remote | Hybrid | Multi-timezone]

   Key Deliverables:
   1. [Deliverable 1]
   2. [Deliverable 2]
   3. [Deliverable 3]"

Output Format:
  # Multi-Team Collaboration Protocol: [Project Name]

  **Version**: 1.0.0
  **Date**: [YYYY-MM-DD]
  **Tier**: [Tier]
  **Status**: ACTIVE

  ---

  ## Project Governance

  | Role | Name | Authority | Escalation To |
  |------|------|-----------|---------------|
  | Project Owner | [Name] | Strategic, Budget | Sponsor |
  | Project Manager | [Name] | Cross-team, Stakeholders | PO |
  | Technical Lead | [Name] | Architecture, Code Quality | PM |

  ---

  ## Team Structure

  ### Team A: [Name]
  - **Role**: [Primary function]
  - **Members**: [Count] ([Key roles])
  - **Deliverables**: [What they produce]
  - **Dependencies**:
    - Upstream: [Teams providing input]
    - Downstream: [Teams receiving output]
  - **Sync Cadence**: [Daily/Weekly with whom]

  ### Team B: [Name]
  [Same structure]

  ---

  ## RACI Matrix

  | Deliverable | PO | PM | Tech Lead | Team A | Team B | Team C |
  |-------------|----|----|-----------|--------|--------|--------|
  | [D1] | A | C | R | R | I | C |
  | [D2] | I | A | C | I | R | R |
  | [D3] | A | C | C | C | I | R |

  ### Legend
  - **R**: Responsible (does the work)
  - **A**: Accountable (final decision - ONE per row)
  - **C**: Consulted (provides input)
  - **I**: Informed (notified after)

  ---

  ## Handoff Protocol

  ### [Team A] → [Team B]: [Handoff Name]
  1. **Trigger**: [When handoff occurs]
  2. **Criteria**: [Definition of Done for handoff]
  3. **Process**:
     - Team A posts in #handoff channel
     - Team B has [X] hours to review
     - Q&A session if needed
     - Team B accepts or requests changes
  4. **Acceptance**: Team B Lead signs off

  ---

  ## Communication Standards

  ### Channels
  | Channel | Purpose | Participants |
  |---------|---------|--------------|
  | #team-a | Team A internal | Team A |
  | #handoff | Cross-team handoffs | All teams |
  | #escalation | Blocked items | PM, Leads |

  ### Response SLAs
  | Role | SLA | Escalation |
  |------|-----|------------|
  | Team Member | <4h | Team Lead |
  | Team Lead | <4h | PM |
  | PM | <4h | PO |

  ---

  ## Escalation Path
  [4-level escalation following SDLC 5.0.0 standards]
```

### 2. Remote/Hybrid Work Protocol

```yaml
System Prompt:
  You are generating remote/hybrid work protocols for distributed teams.
  Address timezone management, async communication, and work-life balance.
  Follow Team Topologies principles for distributed team structure.

User Prompt Template:
  "Generate a remote/hybrid work protocol for:

   Project: [Name]
   Team Size: [Number]

   Locations:
   - [Location 1]: [Number] people, [Timezone]
   - [Location 2]: [Number] people, [Timezone]
   - [Location 3]: [Number] people, [Timezone]

   Tools:
   - Communication: [Slack/Teams/Discord]
   - Video: [Zoom/Meet/Teams]
   - Project Management: [GitHub/Jira/Linear]
   - Documentation: [Notion/Confluence/Wiki]

   Constraints:
   - Overlap hours required: [X] hours minimum
   - Languages: [English, Vietnamese, etc.]
   - Compliance: [Any regulatory requirements]"

Output Format:
  # Remote/Hybrid Work Protocol: [Project Name]

  **Version**: 1.0.0
  **Date**: [YYYY-MM-DD]
  **Status**: ACTIVE

  ---

  ## Team Distribution

  | Location | Team Members | Timezone | Core Hours (Local) |
  |----------|--------------|----------|-------------------|
  | [Loc 1] | [X] | [TZ] | 9:00-18:00 |
  | [Loc 2] | [Y] | [TZ] | 9:00-18:00 |

  ---

  ## Overlap Hours

  **Golden Hours**: [X:00] - [Y:00] UTC ([Z] hours overlap)

  | Activity | When | Who |
  |----------|------|-----|
  | Daily Sync | [Time] UTC | All team |
  | Planning | [Time] UTC | Leads + PM |
  | Ad-hoc meetings | Golden hours | As needed |

  ---

  ## Async-First Communication

  ### Writing Guidelines
  - ✅ Context first: "Regarding [topic]..."
  - ✅ Specific ask: "I need X by Y"
  - ✅ Deadline stated: "Please respond by EOD Friday"
  - ✅ Visual aids: Screenshots, diagrams

  ### Responding Guidelines
  - ✅ Acknowledge receipt: "Saw this, will respond by..."
  - ✅ Use threads: Keep discussions organized
  - ✅ Summarize decisions: "Decision: We'll use X because Y"
  - ✅ Update status: "Done ✅" or "Blocked, see thread"

  ---

  ## Tool Usage Matrix

  | Tool | Purpose | Response SLA | Best For |
  |------|---------|--------------|----------|
  | Slack | Real-time chat | <4h | Quick questions |
  | Email | External + formal | <24h | Stakeholder comms |
  | GitHub | Code discussions | 24h | PRs, issues |
  | [Doc tool] | Documentation | N/A | Long-form content |

  ---

  ## Work-Life Balance Guidelines

  - **Respect quiet hours**: No @mentions after [Time] local time
  - **Flexible start**: Core hours + flexible surrounding
  - **Meeting-free days**: [Day] reserved for deep work
  - **PTO coverage**: Always have backup assigned
```

### 3. Design-First Handoff Protocol

```yaml
System Prompt:
  You are generating design-first handoff protocols for teams where
  design/architecture must be approved before implementation begins.
  This pattern is common in regulated industries or quality-critical projects.

User Prompt Template:
  "Generate a design-first handoff protocol for:

   Project: [Name]
   Design Team: [Name/Size]
   Implementation Team: [Name/Size]

   Design Artifacts:
   - [Artifact 1]: [e.g., Figma mockups]
   - [Artifact 2]: [e.g., API specifications]
   - [Artifact 3]: [e.g., Architecture diagrams]

   Approval Authority: [Who approves design changes?]

   Sprint Rhythm:
   - Design phase: Days [X-Y]
   - Implementation phase: Days [Y-Z]
   - Review/Integration: Days [Z-End]"

Output Format:
  # Design-First Handoff Protocol: [Project Name]

  **Version**: 1.0.0
  **Pattern**: Design-First Development
  **Status**: ACTIVE

  ---

  ## Workflow Overview

  ```
  Design Team                    Implementation Team
  ┌────────────┐                ┌────────────────────┐
  │ Day 1-3:   │                │ Day 4-8:           │
  │ - Research │──→ Handoff ──→ │ - Implement        │
  │ - Design   │   (Day 3-4)    │ - Test             │
  │ - Document │                │ - Integrate        │
  └────────────┘                └────────────────────┘
           │                              │
           └───── Review (Day 9-10) ──────┘
  ```

  ---

  ## Design Phase (Days 1-3)

  ### Deliverables
  | Artifact | Owner | Format | Location |
  |----------|-------|--------|----------|
  | UI Mockups | Designer | Figma | /design/mockups |
  | API Spec | Architect | OpenAPI | /docs/api |
  | Data Model | Architect | ERD | /docs/data |

  ### Definition of Done (Design)
  - [ ] All screens designed in Figma
  - [ ] API endpoints documented
  - [ ] [Approval Authority] sign-off obtained
  - [ ] Handoff document prepared

  ---

  ## Handoff Protocol (Day 3-4)

  ### Pre-Handoff Checklist
  - [ ] All design artifacts in designated locations
  - [ ] SSOT links documented
  - [ ] Known constraints listed
  - [ ] Open questions documented

  ### Handoff Meeting (30 min)
  1. **Design walkthrough** (10 min): Design Team presents
  2. **Q&A** (10 min): Implementation Team asks questions
  3. **Acceptance** (10 min): Implementation Lead confirms understanding

  ### Post-Handoff
  - Design Team available for clarifications via #sprint-questions
  - Changes to design require [Approval Authority] approval
  - Implementation Team owns execution from this point

  ---

  ## Implementation Phase (Days 4-8)

  ### Rules
  1. **Follow design specs exactly** - no creative interpretation
  2. **Ask before you guess** - clarify with Design Team if unclear
  3. **Request changes formally** - design change = new approval cycle
  4. **Daily progress updates** - post in #sprint-progress

  ---

  ## Design Change Request Process

  | Step | Who | Action | SLA |
  |------|-----|--------|-----|
  | 1 | Impl Team | Submit change request | - |
  | 2 | Design Team | Assess impact | 2h |
  | 3 | [Authority] | Approve/Reject | 4h |
  | 4 | Design Team | Update specs | 4h |
  | 5 | Impl Team | Continue with new spec | - |

  **Total SLA for design change**: <12 hours
```

### 4. On-Call and Incident Response Protocol

```yaml
System Prompt:
  You are generating on-call and incident response protocols following SRE best practices.
  Define rotation schedules, escalation procedures, and postmortem requirements.
  Reference DORA metrics and Google SRE handbook patterns.

User Prompt Template:
  "Generate an on-call protocol for:

   Project: [Name]
   Team Size: [Number]

   Services Covered:
   - [Service 1]: [Criticality]
   - [Service 2]: [Criticality]

   SLOs:
   - Availability: [X]%
   - Response Time (P0): [X] minutes
   - Response Time (P1): [X] minutes

   Tools:
   - Alerting: [PagerDuty/OpsGenie/Custom]
   - Monitoring: [Prometheus/Datadog/Custom]
   - Communication: [Slack channel]"

Output Format:
  # On-Call Protocol: [Project Name]

  **Version**: 1.0.0
  **Status**: ACTIVE
  **SLO**: [X]% availability

  ---

  ## On-Call Rotation

  | Week | Primary | Secondary | Escalation |
  |------|---------|-----------|------------|
  | 1 | Alice | Bob | Tech Lead |
  | 2 | Bob | Charlie | Tech Lead |
  | 3 | Charlie | Alice | Tech Lead |

  **Rotation**: Weekly, handoff at [Day] [Time] UTC
  **Compensation**: [Per company policy]

  ---

  ## Severity Definitions

  | Severity | Definition | Response SLA | Examples |
  |----------|------------|--------------|----------|
  | P0 | Service down | 15 min | Complete outage |
  | P1 | Major degradation | 1 hour | 50%+ errors |
  | P2 | Minor degradation | 4 hours | Single feature |
  | P3 | Non-urgent | Next business day | UI glitch |

  ---

  ## Incident Response Procedure

  ### P0 Procedure
  1. **Acknowledge** alert within 15 minutes
  2. **Assess** scope and impact
  3. **Communicate** in #incidents channel
  4. **Mitigate** (prioritize fixing over root cause)
  5. **Escalate** if not resolved in 30 minutes
  6. **Resolve** and verify
  7. **Document** in incident log
  8. **Postmortem** within 48 hours

  ### Communication Template
  ```
  🚨 **Incident: [Title]**
  **Severity**: P[X]
  **Status**: Investigating | Mitigating | Resolved
  **Impact**: [What's affected]
  **ETA**: [When we expect resolution]
  **Lead**: @[Name]
  ```

  ---

  ## Postmortem Requirements

  | Severity | Postmortem Required | Timeline | Attendees |
  |----------|---------------------|----------|-----------|
  | P0 | Yes (mandatory) | 48 hours | All + Mgmt |
  | P1 | Yes (mandatory) | 1 week | Team + Lead |
  | P2 | Optional | 2 weeks | Team |
  | P3 | No | - | - |
```

---

## Tier-Appropriate Protocol Requirements

| Tier | Multi-Team | Remote/Hybrid | Design-First | On-Call |
|------|------------|---------------|--------------|---------|
| LITE | N/A | Informal | N/A | N/A |
| STANDARD | Basic | Documented | Optional | Basic |
| PROFESSIONAL | Full RACI | Full protocol | If applicable | Full rotation |
| ENTERPRISE | Full + audit | Full + compliance | Mandatory | Full + SRE |

---

## Usage Examples

### Example 1: Generate Multi-Team Protocol

```
User: "Generate a collaboration protocol for 3 teams (Backend, Frontend, QA)
       working on SDLC Orchestrator with PM as coordinator"

AI Response: [Full protocol with RACI, handoffs, escalation]
```

### Example 2: Generate Remote Work Protocol

```
User: "Generate remote work protocol for team split between
       Vietnam (UTC+7) and US West Coast (UTC-8)"

AI Response: [Full protocol with overlap hours, async guidelines, tools]
```

---

## Success Metrics

**Protocol Effectiveness** (Stage 08):
- ✅ 80% time savings on protocol creation
- ✅ 90%+ team clarity on roles (RACI)
- ✅ 50% reduction in handoff delays
- ✅ 70% reduction in escalations

**Industry Alignment**:
- Team Topologies patterns applied
- SAFe 6.0 coordination principles
- DORA metrics integration
- Google SRE best practices

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for PROFESSIONAL+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office
