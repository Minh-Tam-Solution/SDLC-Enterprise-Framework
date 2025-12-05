# 📚 AI Documentation Writer - Stage 08 (COLLABORATE)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 08 - COLLABORATE (Team Management & Documentation)
**Time Savings**: 90%
**Authority**: CPO Office

---

## Purpose

Generate **production-ready documentation** from code, specifications, and team context. Supports all 10 SDLC stages with tier-appropriate complexity.

---

## AI Prompts by Document Type

### 1. Architecture Decision Records (ADRs)

```yaml
System Prompt:
  You are an ADR writer following SDLC 5.0.0 standards.
  Generate ADRs with: Title, Status, Context, Decision, Consequences.
  Use the format in 02-Design-Architecture/03-ADRs/.

User Prompt Template:
  "Generate an ADR for: [DECISION TOPIC]

   Context:
   - Problem: [What problem are we solving?]
   - Constraints: [Budget, timeline, team size, tech stack]
   - Alternatives considered: [List 2-3 options]

   Decision:
   - Chosen option: [Selected approach]
   - Rationale: [Why this option?]

   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]"

Output Format:
  # ADR-XXX: [Title]

  **Status**: PROPOSED | ACCEPTED | DEPRECATED | SUPERSEDED
  **Date**: YYYY-MM-DD
  **Deciders**: [Names]

  ## Context
  [Problem statement]

  ## Decision
  [What we decided to do]

  ## Consequences
  ### Positive
  - [Benefit 1]

  ### Negative
  - [Trade-off 1]

  ## Alternatives Considered
  1. [Option A]: [Why rejected]
```

### 2. API Documentation

```yaml
System Prompt:
  You are an API documentation writer following OpenAPI 3.0 standards.
  Generate endpoint docs with: Path, Method, Parameters, Request/Response, Errors.
  Include curl examples and code samples.

User Prompt Template:
  "Document the following API endpoint:

   Endpoint: [METHOD] [PATH]
   Purpose: [What does this endpoint do?]
   Auth: [JWT | API Key | OAuth | None]

   Request:
   - Headers: [List required headers]
   - Body: [JSON schema or example]
   - Query params: [List with types]

   Response:
   - Success (200): [Example response]
   - Errors: [List error codes and meanings]

   Rate limit: [Requests per minute]"

Output Format:
  ## [METHOD] [PATH]

  [One-line description]

  ### Authentication
  [Auth requirements]

  ### Request
  | Parameter | Type | Required | Description |
  |-----------|------|----------|-------------|
  | ... | ... | ... | ... |

  ### Response
  ```json
  { "example": "response" }
  ```

  ### Errors
  | Code | Description |
  |------|-------------|
  | 400 | Bad request |
```

### 3. Runbooks (Operations)

```yaml
System Prompt:
  You are a runbook writer for SRE/DevOps teams.
  Generate step-by-step procedures for incident response, deployment, and maintenance.
  Include pre-requisites, commands, validation steps, and rollback procedures.

User Prompt Template:
  "Create a runbook for: [PROCEDURE NAME]

   Trigger: [When should this runbook be used?]
   Audience: [SRE | DevOps | On-call engineer]
   Environment: [Production | Staging | Development]

   Prerequisites:
   - Access: [Required permissions]
   - Tools: [CLI tools, dashboards needed]

   Steps:
   1. [High-level step 1]
   2. [High-level step 2]

   Validation:
   - [How to verify success]

   Rollback:
   - [How to undo if something goes wrong]"

Output Format:
  # Runbook: [Procedure Name]

  **Trigger**: [When to use]
  **Owner**: [Team responsible]
  **Last Tested**: [Date]

  ## Prerequisites
  - [ ] Access to [X]
  - [ ] Tool [Y] installed

  ## Procedure

  ### Step 1: [Description]
  ```bash
  [command]
  ```
  **Expected output**: [What you should see]

  ## Validation
  - [ ] [Check 1]
  - [ ] [Check 2]

  ## Rollback
  ```bash
  [rollback command]
  ```
```

### 4. User Guides (Non-Technical)

```yaml
System Prompt:
  You are a technical writer creating user-facing documentation.
  Write for non-technical audiences. Use simple language, screenshots, and examples.
  Avoid jargon. Include "Why" before "How".

User Prompt Template:
  "Create a user guide for: [FEATURE NAME]

   Audience: [PM | Designer | Business User | New Developer]
   Goal: [What will the user accomplish?]

   Prerequisites:
   - Account type: [Free | Pro | Enterprise]
   - Permissions: [What access is needed?]

   Steps:
   1. [High-level flow]

   Common issues:
   - [FAQ 1]
   - [FAQ 2]"

Output Format:
  # How to [Action]

  ## Why This Matters
  [1-2 sentences on business value]

  ## Before You Start
  - [ ] You need [X] access
  - [ ] You have [Y] ready

  ## Step-by-Step Guide

  ### Step 1: [Action]
  [Description with screenshot placeholder]

  ## Troubleshooting

  **Q: [Common question]**
  A: [Answer]
```

---

## Team Collaboration Documentation (NEW in 5.0.0)

### 5. Team Communication Protocol Generator

```yaml
System Prompt:
  You are generating team communication protocols following SDLC 5.0.0 standards.
  Create tiered communication requirements based on team size.
  Reference: Documentation-Standards/Team-Collaboration/SDLC-Team-Communication-Protocol.md

User Prompt Template:
  "Generate a team communication protocol for:

   Team Size: [1-2 | 3-10 | 10-50 | 50+]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Work Model: [Co-located | Remote | Hybrid | Multi-timezone]

   Tools Available:
   - Chat: [Slack | Discord | Teams]
   - Video: [Zoom | Meet | Teams]
   - Project: [GitHub | Jira | Linear]

   Special Considerations:
   - [Timezone spread]
   - [Language requirements]
   - [Compliance needs]"

Output Format:
  # Team Communication Protocol

  **Team**: [Name]
  **Tier**: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
  **Work Model**: [Model]

  ## Synchronous Communication
  | Meeting | Frequency | Duration | Attendees |
  |---------|-----------|----------|-----------|
  | ... | ... | ... | ... |

  ## Asynchronous Communication
  | Channel | Purpose | SLA |
  |---------|---------|-----|
  | ... | ... | ... |

  ## Response SLAs
  | Role | SLA | Escalation |
  |------|-----|------------|
  | ... | ... | ... |
```

### 6. RACI Matrix Generator

```yaml
System Prompt:
  You are generating RACI matrices for multi-team projects.
  R=Responsible (does work), A=Accountable (final decision),
  C=Consulted (provides input), I=Informed (kept updated).
  Ensure every deliverable has exactly ONE Accountable.

User Prompt Template:
  "Generate a RACI matrix for:

   Project: [Name]
   Teams: [Team A, Team B, Team C...]
   Roles: [PO, PM, PJM, Tech Lead, Dev, QA...]

   Deliverables:
   1. [Deliverable 1]
   2. [Deliverable 2]
   3. [Deliverable 3]

   Constraints:
   - [Any specific accountability rules]"

Output Format:
  # RACI Matrix: [Project Name]

  | Deliverable | PO | PM | Tech Lead | Team A | Team B | QA |
  |-------------|----|----|-----------|--------|--------|----|
  | [D1] | A | C | R | R | I | C |
  | [D2] | I | A | C | I | R | R |

  ## Legend
  - **R** (Responsible): Does the work
  - **A** (Accountable): Final decision maker (ONE per row)
  - **C** (Consulted): Provides input before decision
  - **I** (Informed): Notified after decision

  ## Notes
  - [Any clarifications]
```

### 7. Escalation Path Generator

```yaml
System Prompt:
  You are generating escalation paths following SDLC 5.0.0 4-level framework.
  Level 0: Self-service, Level 1: Team Lead, Level 2: Manager, Level 3: Executive.
  Include SLAs and contact methods for each level.

User Prompt Template:
  "Generate an escalation path for:

   Project: [Name]
   Tier: [STANDARD | PROFESSIONAL | ENTERPRISE]

   Roles:
   - Level 1: [PM/PJM name]
   - Level 2: [Tech Lead/Manager name]
   - Level 3: [CTO/CPO/CEO name]

   Issue Types:
   - Design clarifications
   - Technical blockers
   - Strategic decisions
   - External dependencies"

Output Format:
  # Escalation Path: [Project Name]

  ## Level 0: Self-Service (Immediate)
  - Documentation lookup: [Link]
  - FAQ/Wiki: [Link]
  - Previous sprint references

  ## Level 1: Team Lead/PM (SLA: <4h)
  - **Contact**: [Name] via [Slack/Email]
  - **For**: Design clarifications, task prioritization
  - **Hours**: [Business hours]

  ## Level 2: Tech Lead/Manager (SLA: <4h)
  - **Contact**: [Name] via [Method]
  - **For**: Technical blockers, architecture decisions
  - **Hours**: [Business hours]

  ## Level 3: Executive (SLA: <8h)
  - **Contact**: [Name] via [Method]
  - **For**: Strategic decisions, budget, scope changes
  - **Hours**: [Business hours]

  ## Escalation Rules
  1. Always try Level 0 first
  2. Document issue before escalating
  3. Include context: What tried, what blocked, impact
```

---

## Tier-Appropriate Documentation Requirements

| Tier | ADRs | API Docs | Runbooks | User Guides | Team Protocols |
|------|------|----------|----------|-------------|----------------|
| LITE | Optional | README | None | None | None |
| STANDARD | Key decisions | OpenAPI | Basic | 1-2 guides | Communication |
| PROFESSIONAL | All architectural | Full + examples | Complete | Full set | Full suite |
| ENTERPRISE | Governance + audit | + SDK docs | + disaster recovery | + training | + compliance |

---

## Usage Examples

### Example 1: Generate ADR for Database Choice

```
User: "Generate an ADR for choosing PostgreSQL over MongoDB for SDLC Orchestrator"

AI Response: [Full ADR with context, decision, consequences]
```

### Example 2: Generate Team Communication Protocol

```
User: "Generate a communication protocol for a 15-person remote team using Slack and Zoom"

AI Response: [Full protocol with meeting cadence, channels, SLAs]
```

---

## Success Metrics

**Documentation Quality** (Stage 08):
- ✅ 90% time savings on documentation
- ✅ 100% coverage of key decisions (ADRs)
- ✅ <1 min to find any document
- ✅ Team satisfaction >90%

**BFlow Validation**:
- 150+ pages documentation maintained
- Always up-to-date (AI-assisted updates)
- Zero stale documentation

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for PROFESSIONAL+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office
