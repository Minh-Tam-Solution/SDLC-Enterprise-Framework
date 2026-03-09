# SOUL Role Templates

**Version**: 1.0.0 | **Framework**: SDLC 6.1.2 | **Ring**: 2 (Governance — Templates & Tools)

---

## What are SOULs?

SOUL (Standard Operating Unit Layout) templates define **role-specific personas** for AI agents in the SASE (Software Agent Software Engineering) model. Each SOUL specifies:

- **Identity** — Role description, capabilities, constraints
- **SDLC Stage Coverage** — Which stages the role operates in
- **Gate Responsibilities** — Which quality gates the role participates in
- **Communication Patterns** — How the role interacts with other roles
- **Tier Availability** — Which SDLC tiers include this role

SOULs are the persona layer that sits above AGENTS.md (workspace context). While AGENTS.md defines *project-specific* context, SOULs define *role-specific* behavior that is reusable across projects.

---

## SASE 12-Role Classification

### SE4A — Software Engineering for Agents (8 Executor Roles)

| # | SOUL | File | Purpose | SDLC Stages |
|---|------|------|---------|-------------|
| 1 | **coder** | `SOUL-coder.md` | Developer — writes code, runs tests, creates commits | 04 (Build) |
| 2 | **tester** | `SOUL-tester.md` | QA Engineer — test planning, execution, automation | 04-05 (Build-Test) |
| 3 | **architect** | `SOUL-architect.md` | Architect — system design, ADRs, technical decisions | 02-03 (Design-Integrate) |
| 4 | **pm** | `SOUL-pm.md` | Product Manager — requirements, user stories, prioritization | 00-01 (Discover-Plan) |
| 5 | **pjm** | `SOUL-pjm.md` | Project Manager — sprint planning, resource allocation, tracking | 01-04 (Plan-Build) |
| 6 | **devops** | `SOUL-devops.md` | DevOps — CI/CD, infrastructure, deployment, monitoring | 05-08 (Deploy-Operate) |
| 7 | **fullstack** | `SOUL-fullstack.md` | Full-Stack Developer — frontend + backend implementation | 04 (Build) |
| 8 | **reviewer** | `SOUL-reviewer.md` | Code Reviewer — PR review, quality checks, best practices | 04-05 (Build-Test) |

### SE4H — Software Engineering for Humans (3 Advisor Roles)

| # | SOUL | File | Purpose | SDLC Stages |
|---|------|------|---------|-------------|
| 9 | **ceo** | `SOUL-ceo.md` | CEO Advisor — business strategy, market positioning | 00-09 (All) |
| 10 | **cto** | `SOUL-cto.md` | CTO Advisor — technical strategy, architecture governance | 00-09 (All) |
| 11 | **cpo** | `SOUL-cpo.md` | CPO Advisor — product strategy, user experience | 00-09 (All) |

### Router (1 Role)

| # | SOUL | File | Purpose | SDLC Stages |
|---|------|------|---------|-------------|
| 12 | **assistant** | `SOUL-assistant.md` | Router — routes requests to appropriate specialist roles | 00-09 (All) |

### Support Roles (1 SE4A + 3 Non-SDLC)

| # | SOUL | File | Purpose | Classification |
|---|------|------|---------|----------------|
| 13 | **researcher** | `SOUL-researcher.md` | Research — literature review, competitive analysis | SE4A (SDLC) |
| 14 | **writer** | `SOUL-writer.md` | Documentation specialist | Nice-to-have |
| 15 | **sales** | `SOUL-sales.md` | Sales engineer | Nice-to-have (non-SDLC) |
| 16 | **cs** | `SOUL-cs.md` | Customer service | Nice-to-have (non-SDLC) |
| 17 | **itadmin** | `SOUL-itadmin.md` | IT administrator | Nice-to-have (non-SDLC) |

---

## Tier Availability Matrix

| Tier | Available SOULs | Count |
|------|----------------|-------|
| **LITE** | assistant, coder, tester | 3 |
| **STANDARD** | + pm, architect, reviewer | 6 |
| **PROFESSIONAL** | + devops, fullstack, pjm, researcher | 10 |
| **ENTERPRISE** | + ceo, cto, cpo | 13 |
| **OPTIONAL** | + writer, sales, cs, itadmin | 17 |

> **Note**: OPTIONAL roles (writer, sales, cs, itadmin) are non-SDLC support roles. Include them when your team needs business operations support beyond software engineering.

---

## Usage Guide

### 1. Selecting SOULs for Your Project

Choose SOULs based on your SDLC tier and team composition:

```yaml
# Example: STANDARD tier project
souls:
  - assistant    # Router (always included)
  - coder        # Primary developer
  - tester       # QA engineer
  - pm           # Product manager
  - architect    # System architect
  - reviewer     # Code reviewer
```

### 2. SOUL Template Structure

Each SOUL file follows this structure:

```markdown
---
role: <role_name>
category: executor | advisor | router
sdlc_framework: "6.1.2"
version: 1.0.0
sdlc_stages: ["04"]           # Which SDLC stages
sdlc_gates: ["G-Sprint"]      # Which gates
created: 2026-XX-XX
---

# SOUL — <Role Name>

## Identity          # Who this role is
## Capabilities      # What it can do
## Constraints       # What it must/must not do
## Communication     # How it interacts with others
## Gate Responsibilities  # Gate-specific behavior
```

### 3. Relationship to Other SASE Artifacts

| Artifact | Purpose | Location |
|----------|---------|----------|
| **SOUL** | Role persona (WHO) | `04-SASE-Artifacts/souls/` |
| **TEAM** | Team composition (WHO works together) | `04-SASE-Artifacts/teams/` |
| **AGENTS.md** | Workspace context (WHERE) | `03-Agent-Templates/` |
| **CRP** | Change Request Process (HOW changes flow) | `04-SASE-Artifacts/01-CRP-Template.md` |
| **MRP** | Merge Request Process (HOW code merges) | `04-SASE-Artifacts/02-MRP-Template.md` |
| **VCR** | Version Control Rules (HOW versions work) | `04-SASE-Artifacts/03-VCR-Template.md` |

---

## TEAM Charters

Team charters define how SOULs collaborate in groups. See `../teams/` for 10 team templates:

**SDLC Function Teams** (7):
- `TEAM-dev.md` — Development team
- `TEAM-qa.md` — Quality Assurance team
- `TEAM-design.md` — Design team
- `TEAM-executive.md` — Executive team
- `TEAM-fullstack.md` — Full-Stack team
- `TEAM-ops.md` — Operations team
- `TEAM-planning.md` — Planning team

**Organizational Teams** (3):
- `TEAM-advisory.md` — Advisory Board (governance oversight)
- `TEAM-business.md` — Business Operations (sales, CS, support)
- `TEAM-engineering.md` — SDLC Engineering (stages 00-08)

---

*Added in SDLC 6.1.2 — Ring 2 (Governance: Templates & Tools)*
