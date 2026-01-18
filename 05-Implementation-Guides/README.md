# SDLC 5.1.3 Implementation Guides

**Version**: 5.1.3 | **Status**: PRODUCTION READY | **Date**: January 2025

Practical how-to guides for implementing SDLC 5.1.3 framework + SASE artifacts.

---

## Quick Navigation

| I want to... | Go to |
|--------------|-------|
| Start SDLC from scratch | [SDLC-Implementation-Guide.md](SDLC-Implementation-Guide.md) |
| Choose code review tier | [SDLC-Universal-Code-Review-Framework.md](SDLC-Universal-Code-Review-Framework.md) |
| Setup pre-commit hooks | [SDLC-PRE-COMMIT-HOOKS.md](SDLC-PRE-COMMIT-HOOKS.md) |
| Handle production crisis | [SDLC-Crisis-Response-Guide.md](SDLC-Crisis-Response-Guide.md) |
| Work with AI agents (SASE) | [SASE Artifacts](../03-Templates-Tools/SASE-Artifacts/) |

---

## Guides in This Folder

### Core Implementation

| Guide | Purpose | Use When |
|-------|---------|----------|
| **SDLC-Implementation-Guide.md** | Complete SDLC 5.1.3 deployment | Starting from scratch |
| **SDLC-Self-Contained-Deployment-Guide.md** | Team folder deployment | Deploying to specific team |

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

### Legacy/Archive Structure (SDLC 5.1.3)

```yaml
Rules:
  - 10-archive: ONLY at docs root (not a stage, holds unsorted legacy docs)
  - 99-legacy: within EACH stage (00-09) AND in backend, frontend, tools
  - Content in legacy/archive folders is never validated or upgraded
```

---

## Templates & Tools Reference

### SASE Artifacts

Location: [03-Templates-Tools/SASE-Artifacts/](../03-Templates-Tools/SASE-Artifacts/)

| Artifact | Created By | Purpose |
|----------|------------|---------|
| **BRS** (BriefingScript) | Human (SE4H) | Task specification |
| **LPS** (LoopScript) | Agent (SE4A) | Execution plan |
| **MTS** (MentorScript) | Human (SE4H) | Coding standards |
| **CRP** (Consultation Request) | Agent (SE4A) | When uncertain |
| **MRP** (Merge-Readiness Pack) | Agent (SE4A) | 5-point evidence |
| **VCR** (Version Controlled Resolution) | Human (SE4H) | Approval record |

### AI Tools & Prompts

Location: [03-Templates-Tools/1-AI-Tools/](../03-Templates-Tools/1-AI-Tools/)

- `design-thinking/` - Problem statement, empathy synthesis, ideation
- `code-review/` - Tier 1/2/3 prompts
- `testing/` - Test case generator, UAT scripts
- `deployment/` - Deployment checklists, rollback plans
- `operations/` - Incident response, monitoring setup
- `governance/` - Compliance checker, audit reports
- `integration/` - API contract designer, integration tests
- `collaboration/` - Meeting summarizer, RACI generator

### Automation Scripts

Location: [03-Templates-Tools/4-Scripts/](../03-Templates-Tools/4-Scripts/)

| Script | Purpose |
|--------|---------|
| `compliance/sdlc_validator.py` | Validate SDLC 5.1 folder structure |
| `compliance/sdlc_scanner.py` | Scan project for compliance |
| `quick-start/solo_setup.py` | Setup for solo developer |

---

## Related Documentation

| Folder | Purpose |
|--------|---------|
| [01-Overview/](../01-Overview/) | Executive Summary |
| [02-Core-Methodology/](../02-Core-Methodology/) | 10-stage lifecycle theory |
| [04-Case-Studies/](../04-Case-Studies/) | BFlow, NQH-Bot, MTEP examples |

---

**Last Updated**: December 11, 2025
**Authority**: CTO + CPO Office
