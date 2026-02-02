# SDLC 6.0.3 Implementation Guides

**Version: 6.0.3 | **Status**: PRODUCTION READY | **Date**: February 1, 2026

Practical how-to guides for implementing SDLC 6.0.3 framework + Section 7 Quality Assurance System + **SPEC-0021 Stage Consistency Validation**.

**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles

---

## 🚀 Getting Started - Pick Your Path

### New Project (Greenfield)
Start fresh with SDLC 6.0.3 from day one.

| Team Size | Time | Start Here |
|-----------|------|------------|
| 1-2 people (LITE) | 1 day | [Quick Start Guide](../08-Training-Materials/SDLC-Quick-Start-Guide.md) |
| 3-10 people (STANDARD) | 1 week | [Implementation Guide](SDLC-Implementation-Guide.md) |
| 10-50 people (PROFESSIONAL) | 2 weeks | [Implementation Guide](SDLC-Implementation-Guide.md) + [Deployment Guide](SDLC-Deployment-Guide.md) |
| 50+ people (ENTERPRISE) | 4 weeks | [Full Implementation](SDLC-Implementation-Guide.md) + [Self-Contained Deployment](SDLC-Self-Contained-Deployment-Guide.md) |

### Existing Project (Brownfield)
Adopt SDLC 6.0.3 incrementally into running projects.

| Phase | Focus | Time | Guide |
|-------|-------|------|-------|
| **Phase 1** | Pre-commit hooks + Code review | 1-2 days | [Pre-Commit Hooks](SDLC-PRE-COMMIT-HOOKS.md) + [Code Review](SDLC-Universal-Code-Review-Framework.md) |
| **Phase 2** | Folder structure + Documentation | 1 week | [Compliance Enforcement](SDLC-Compliance-Enforcement-Guide.md) |
| **Phase 3** | AI agents + SASE artifacts | 2 weeks | [ACE-AEE Architecture](ACE-AEE-Reference-Architecture.md) |
| **Phase 4** | Full governance + Quality gates | 4 weeks | [Platform Patterns](SDLC-Platform-Patterns.md) |

> 💡 **Brownfield Tip**: Start with Phase 1 only. Each phase adds value independently. Don't try to do everything at once.

---

## What's New in 6.0.1

**SPEC-0021: Stage Consistency Validation** - Prevents "spec drift" where implementation diverges from design.

| Feature | Description |
|---------|-------------|
| **4-Stage Model** | Stage 01 ↔ 02 ↔ 03 ↔ 04 consistency validation |
| **Implementation Guide** | [SDLC-Stage-Consistency-Validation-Guide.md](SDLC-Stage-Consistency-Validation-Guide.md) ⭐ NEW |

---

## Quick Navigation

| I want to... | Go to |
|--------------|-------|
| Start SDLC from scratch (new project) | [SDLC-Implementation-Guide.md](SDLC-Implementation-Guide.md) |
| Add SDLC to existing project | Start with [Pre-Commit Hooks](SDLC-PRE-COMMIT-HOOKS.md) |
| **Validate stage consistency** | [SDLC-Stage-Consistency-Validation-Guide.md](SDLC-Stage-Consistency-Validation-Guide.md) ⭐ NEW |
| Choose code review tier | [SDLC-Universal-Code-Review-Framework.md](SDLC-Universal-Code-Review-Framework.md) |
| Setup pre-commit hooks | [SDLC-PRE-COMMIT-HOOKS.md](SDLC-PRE-COMMIT-HOOKS.md) |
| Handle production crisis | [SDLC-Crisis-Response-Guide.md](SDLC-Crisis-Response-Guide.md) |
| Work with AI agents (SASE) | [SASE Artifacts](../05-Templates-Tools/04-SASE-Artifacts/) |
| Learn the framework basics | [Quick Start Guide](../08-Training-Materials/SDLC-Quick-Start-Guide.md) (2 days) |
| Train my team | [Training Materials](../08-Training-Materials/SDLC-Training-Materials.md) (8 hours) |

---

## Guides in This Folder

### Core Implementation

| Guide | Purpose | Use When |
|-------|---------|----------|
| **SDLC-Implementation-Guide.md** | Complete SDLC 6.0.3 deployment | Starting from scratch (greenfield) |
| **SDLC-Stage-Consistency-Validation-Guide.md** | 4-stage consistency validation | Preventing spec drift ⭐ NEW |
| **SDLC-Self-Contained-Deployment-Guide.md** | Team folder deployment | Deploying to specific team |
| **SDLC-Compliance-Enforcement-Guide.md** | Adopt SDLC in existing project | Brownfield migration |

### Code Review Framework (3-Tier)

| Guide | Tier | Team Size | Cost |
|-------|------|-----------|------|
| **SDLC-Universal-Code-Review-Framework.md** | Overview | All | - |
| **SDLC-Manual-Code-Review-Playbook.md** | Tier 1 | 1-5 | $0 |
| **SDLC-Subscription-Powered-Code-Review-Guide.md** | Tier 2 | 5-20 | $0* |
| **SDLC-CodeRabbit-Integration-Guide.md** | Tier 3 | 15-100+ | $12-15/seat |

*Uses existing AI subscriptions

### Quality & Operations

| Guide | Stage | Purpose |
|-------|-------|---------|
| **SDLC-PRE-COMMIT-HOOKS.md** | 04 BUILD | Pre-commit quality gates |
| **SDLC-Compliance-Enforcement-Guide.md** | 09 GOVERN | Compliance automation |
| **SDLC-Crisis-Response-Guide.md** | 07 OPERATE | Crisis response procedures |
| **SDLC-Deployment-Guide.md** | 06 DEPLOY | Production deployment |
| **SDLC-Platform-Patterns.md** | All | BFlow/NQH/MTEP patterns |

### SASE Architecture

| Guide | Purpose |
|-------|---------|
| **ACE-AEE-Reference-Architecture.md** | Agent Control/Execution Environment setup |

---

## Required Folder Structure

```bash
# LITE (1-2 people)
mkdir -p docs/00-foundation

# STANDARD (3-10 people)
mkdir -p docs/{00-foundation,01-planning,02-design,04-build,05-test,06-deploy}

# PROFESSIONAL (10-50 people)
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy,07-operate}

# ENTERPRISE (50+ people) - includes 10-archive and 99-legacy structure
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy,07-operate,08-collaborate,09-govern}
mkdir -p docs/10-archive  # Project-level archive (NOT a stage)
# 99-legacy folders created as needed within each stage
```

### Legacy/Archive Structure (SDLC 6.0.3)

```yaml
Rules:
  - 10-archive: ONLY at docs root (not a stage, holds unsorted legacy docs)
  - 99-legacy: within EACH stage (00-09) AND in backend, frontend, tools
  - Content in legacy/archive folders is never validated or upgraded
```

### SDLC Orchestrator CLI Integration

> 💡 The strategies above are automated by SDLC Orchestrator CLI:

```bash
# New project (greenfield) - init command
sdlcctl init /path/to/project --tier STANDARD

# Existing project (brownfield) - scan + fix commands
sdlcctl scan /path/to/project          # Scan current state
sdlcctl fix /path/to/project           # Auto-fix compliance gaps
sdlcctl report /path/to/project        # Generate compliance report
```

See [SDLC Orchestrator](https://github.com/Minh-Tam-Solution/SDLC-Orchestrator) for automation.

---

## Templates & Tools Reference

### SASE Artifacts (6.0.0 Simplified)

Location: [05-Templates-Tools/04-SASE-Artifacts/](../05-Templates-Tools/04-SASE-Artifacts/)

| Artifact | Created By | Purpose |
|----------|------------|---------|
| **AGENTS.md** | Human | AI agent context (industry standard, 60K+ repos) |
| **CRP** (Consultation Request) | Agent (SE4A) | When uncertain, request human guidance |
| **MRP** (Merge-Readiness Pack) | Agent (SE4A) | 5-point evidence before merge |
| **VCR** (Version Controlled Resolution) | Human (SE4H) | Approval/rejection record |

> ⚠️ **Note**: BRS, LPS, MTS deprecated in 6.0.0. Use AGENTS.md instead (see [Deprecation Policy](../DEPRECATION-POLICY.md)).

### AI Tools & Prompts

Location: [05-Templates-Tools/1-AI-Tools/](../05-Templates-Tools/1-AI-Tools/)

- `design-thinking/` - Problem statement, empathy synthesis, ideation
- `code-review/` - Tier 1/2/3 prompts
- `testing/` - Test case generator, UAT scripts
- `deployment/` - Deployment checklists, rollback plans
- `operations/` - Incident response, monitoring setup
- `governance/` - Compliance checker, audit reports
- `integration/` - API contract designer, integration tests
- `collaboration/` - Meeting summarizer, RACI generator

### Automation Scripts

Location: [05-Templates-Tools/07-Scripts/](../05-Templates-Tools/07-Scripts/)

| Script | Purpose |
|--------|---------|
| `compliance_sdlc_validator.py` | Validate SDLC 6.0.3 folder structure (7-Pillar + 2-Section) |
| `compliance_sdlc_scanner.py` | Scan project for compliance |
| `quickstart_solo_setup.py` | Setup for solo developer |

---

## Related Documentation

| Folder | Purpose |
|--------|---------|
| [01-Overview/](../01-Overview/) | Executive Summary |
| [02-Core-Methodology/](../02-Core-Methodology/) | 10-stage lifecycle theory |
| [06-Case-Studies/](../06-Case-Studies/) | BFlow, NQH-Bot, MTEP examples |

---

**Last Updated**: February 1, 2026
**Authority**: CTO + CPO Office
**Framework Version: 6.0.3
