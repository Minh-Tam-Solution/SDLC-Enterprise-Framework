# SDLC 6.3.0 Implementation Guides

**Version**: 6.3.1 | **Status**: PRODUCTION READY | **Date**: March 18, 2026

Practical how-to guides for implementing SDLC 6.3.0 framework: **9 Mental Models**, **Lean Ring 1**, **Long-Running Agent Protocol**, **Citizen Developer Pathway**, **13 Multi-Agent Patterns**, and the full **7-Pillar + Section 7 + Section 8** architecture.

**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles
**Ring**: 3 (Outer) — implementation guides, not methodology

---

## What's New in 6.3.0

**Agentic SDLC — 9 Mental Models + Lean Ring 1 + Long-Running Agents + Citizen Developer**

| Feature | Guide | Description |
|---------|-------|-------------|
| **Multi-Agent Patterns** | [MULTI-AGENT-PATTERNS.md](MULTI-AGENT-PATTERNS.md) | 13 patterns (moved from Ring 1). Lane queues, failover, snapshots, long-running sessions, cross-team coordination |
| **Citizen Developer** | [Citizen-Developer-Guide.md](Citizen-Developer-Guide.md) | 30-min onboarding for non-technical users. Template-only, assist_only autonomy, 3 mandatory boundaries |
| **Conversation-First** | [CONVERSATION-FIRST-GOVERNANCE.md](CONVERSATION-FIRST-GOVERNANCE.md) | OTT/CLI-first governance patterns for chat-driven SDLC workflows |
| **Autonomous Codegen** | [AUTONOMOUS-CODEGEN-PATTERNS.md](AUTONOMOUS-CODEGEN-PATTERNS.md) | Two-agent pattern + 4-Gate Quality Pipeline for code generation |
| **MCP Integration** | [MCP-Integration-Guide.md](MCP-Integration-Guide.md) | Model Context Protocol server setup for AI tool integration |
| **Lean Ring 1** | — | Ring 1 consolidated: 41→30 files, -21% size. These guides updated to reference merged docs |

**What changed for implementation**:
- Stage Lifecycle is now ONE doc (was 3 separate: Dependencies + Exit Criteria + Tier Requirements)
- Quality Gates Assurance is now ONE doc (was 2 separate: QA System + Security Gates)
- Multi-Agent Patterns moved HERE from Ring 1 (implementation patterns, not timeless principles)
- All guides reference 9 Mental Models (was 6) — added Agent Continuity (#7) + Everyone Builds (#8)

---

## Getting Started - Pick Your Path

### New Project (Greenfield)
Start fresh with SDLC 6.3.0 from day one.

| Team Size | Time | Start Here |
|-----------|------|------------|
| 1-2 people (LITE) | 1 day | [Quick Start Guide](../08-Training-Materials/SDLC-Quick-Start-Guide.md) |
| 3-10 people (STANDARD) | 1 week | [Implementation Guide](SDLC-Implementation-Guide.md) |
| 10-50 people (PROFESSIONAL) | 2 weeks | [Implementation Guide](SDLC-Implementation-Guide.md) + [Deployment Guide](SDLC-Deployment-Guide.md) |
| 50+ people (ENTERPRISE) | 4 weeks | [Full Implementation](SDLC-Implementation-Guide.md) + [Self-Contained Deployment](SDLC-Self-Contained-Deployment-Guide.md) |

### Existing Project (Brownfield)
Adopt SDLC 6.3.0 incrementally into running projects.

| Phase | Focus | Time | Guide |
|-------|-------|------|-------|
| **Phase 1** | Pre-commit hooks + Code review | 1-2 days | [Pre-Commit Hooks](SDLC-PRE-COMMIT-HOOKS.md) + [Code Review](SDLC-Code-Review-Guide.md) |
| **Phase 2** | Folder structure + Documentation | 1 week | [Compliance Enforcement](SDLC-Compliance-Enforcement-Guide.md) |
| **Phase 3** | AI agents + SASE artifacts | 2 weeks | [ACE-AEE Architecture](ACE-AEE-Reference-Architecture.md) + [Multi-Agent Patterns](MULTI-AGENT-PATTERNS.md) |
| **Phase 4** | Full governance + Quality gates | 4 weeks | [Platform Patterns](SDLC-Platform-Patterns.md) |

> Start with Phase 1 only. Each phase adds value independently.

### Non-Technical Users (Citizen Developer)
Domain experts (PM, Legal, Finance, Ops) who need workflow automation.

| Step | Time | Guide |
|------|------|-------|
| **Onboarding** | 30 min | [Citizen Developer Guide](Citizen-Developer-Guide.md) |
| **First workflow** | 1 hour | Template-based, assist_only autonomy, ZeroClaw auto-scan |

---

## Quick Navigation

| I want to... | Go to |
|--------------|-------|
| Start SDLC from scratch (new project) | [SDLC-Implementation-Guide.md](SDLC-Implementation-Guide.md) |
| Add SDLC to existing project | Start with [Pre-Commit Hooks](SDLC-PRE-COMMIT-HOOKS.md) |
| Validate stage consistency | [SDLC-Stage-Consistency-Validation-Guide.md](SDLC-Stage-Consistency-Validation-Guide.md) |
| Choose code review tier | [SDLC-Code-Review-Guide.md](SDLC-Code-Review-Guide.md) |
| Setup pre-commit hooks | [SDLC-PRE-COMMIT-HOOKS.md](SDLC-PRE-COMMIT-HOOKS.md) |
| Handle production crisis | [SDLC-Crisis-Response-Guide.md](SDLC-Crisis-Response-Guide.md) |
| Work with AI agents (SASE) | [ACE-AEE Architecture](ACE-AEE-Reference-Architecture.md) + [SASE Artifacts](../05-Templates-Tools/04-SASE-Artifacts/) |
| Use multi-agent patterns | [MULTI-AGENT-PATTERNS.md](MULTI-AGENT-PATTERNS.md) |
| Setup conversation-first governance | [CONVERSATION-FIRST-GOVERNANCE.md](CONVERSATION-FIRST-GOVERNANCE.md) |
| Onboard non-technical users | [Citizen-Developer-Guide.md](Citizen-Developer-Guide.md) |
| Setup autonomous code generation | [AUTONOMOUS-CODEGEN-PATTERNS.md](AUTONOMOUS-CODEGEN-PATTERNS.md) |
| Integrate MCP servers | [MCP-Integration-Guide.md](MCP-Integration-Guide.md) |
| Learn the framework basics | [Quick Start Guide](../08-Training-Materials/SDLC-Quick-Start-Guide.md) (2 days) |

---

## All Guides in This Folder

### Core Implementation

| Guide | Purpose | Use When |
|-------|---------|----------|
| **SDLC-Implementation-Guide.md** | Complete SDLC 6.3.0 deployment | Starting from scratch (greenfield) |
| **SDLC-Stage-Consistency-Validation-Guide.md** | 4-stage consistency validation | Preventing spec drift |
| **SDLC-Self-Contained-Deployment-Guide.md** | Team folder deployment | Deploying to specific team |
| **SDLC-Compliance-Enforcement-Guide.md** | Adopt SDLC in existing project | Brownfield migration |

### AI Agents & Multi-Agent

| Guide | Purpose | Use When |
|-------|---------|----------|
| **MULTI-AGENT-PATTERNS.md** | 13 collaboration patterns (lane queues, failover, snapshots) | Building multi-agent systems |
| **ACE-AEE-Reference-Architecture.md** | Agent Command/Execution Environment setup | Implementing SASE dual-workbench |
| **AUTONOMOUS-CODEGEN-PATTERNS.md** | Two-agent pattern + 4-Gate Quality Pipeline | Automated code generation |
| **MCP-Integration-Guide.md** | Model Context Protocol server integration | Connecting AI tools to project context |
| **CONVERSATION-FIRST-GOVERNANCE.md** | OTT/CLI-first governance workflows | Chat-driven SDLC for distributed teams |
| **Citizen-Developer-Guide.md** | 30-min onboarding for non-technical users | Enabling domain experts to build |

### Code Review Framework

| Guide | Tier | Team Size |
|-------|------|-----------|
| **SDLC-Code-Review-Guide.md** | All Tiers | All |
| **SDLC-CodeRabbit-Integration-Guide.md** | Tier 3 (AI) | 15-100+ |

### Quality & Operations

| Guide | Stage | Purpose |
|-------|-------|---------|
| **SDLC-PRE-COMMIT-HOOKS.md** | 04 BUILD | Pre-commit quality gates |
| **SDLC-Compliance-Enforcement-Guide.md** | 09 GOVERN | Compliance automation |
| **SDLC-Crisis-Response-Guide.md** | 07 OPERATE | Crisis response procedures |
| **SDLC-Deployment-Guide.md** | 06 DEPLOY | Production deployment |
| **SDLC-Platform-Patterns.md** | All | Battle-tested platform patterns |
| **E2E-TESTING-QUICKSTART.md** | 05 TEST | E2E API testing quick start |
| **SDLC-E2E-API-Testing-Methodology.md** | 05 TEST | Full E2E testing methodology |

---

## Required Folder Structure

```bash
# LITE (1-2 people)
mkdir -p docs/00-foundation

# STANDARD (3-10 people)
mkdir -p docs/{00-foundation,01-planning,02-design,04-build,05-test,06-deploy}

# PROFESSIONAL (10-50 people)
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy,07-operate}

# ENTERPRISE (50+ people)
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy,07-operate,08-collaborate,09-govern}
mkdir -p docs/10-archive  # Project-level archive (NOT a stage)
```

### Legacy/Archive Structure (RFC-001)

```yaml
Rules (RFC-001):
  - 10-archive: Centralized archive at docs root with stage-aligned subfolders
    - Format: 10-archive/{NN}-Legacy/ (e.g., 10-archive/02-Legacy/)
  - 99-legacy: ELIMINATED from active stages (00-09) per RFC-001
    - Only permitted in non-stage folders (backend/, frontend/, tools/)
  - Content in archive folders is never validated or upgraded
```

### CLI Automation

```bash
# New project (greenfield) - init command
sdlcctl init /path/to/project --tier STANDARD

# Existing project (brownfield) - scan + fix commands
sdlcctl scan /path/to/project          # Scan current state
sdlcctl fix /path/to/project           # Auto-fix compliance gaps
sdlcctl report /path/to/project        # Generate compliance report
```

---

## Templates & Tools Reference

### SASE Artifacts

Location: [05-Templates-Tools/04-SASE-Artifacts/](../05-Templates-Tools/04-SASE-Artifacts/)

| Artifact | Created By | Purpose |
|----------|------------|---------|
| **AGENTS.md** | Human (SE4H) | AI agent context (industry standard, 60K+ repos) |
| **CRP** (Consultation Request) | Agent (SE4A) | When uncertain, request human guidance |
| **MRP** (Merge-Readiness Pack) | Agent (SE4A) | 5-point evidence before merge |
| **VCR** (Version Controlled Resolution) | Human (SE4H) | Approval/rejection record |
| **18 SOUL templates** | Framework | Role-specific personas (coder, tester, architect, cso, etc.) |
| **10 TEAM charters** | Framework | Team composition templates |

### Automation Scripts

Location: [05-Templates-Tools/07-Scripts/](../05-Templates-Tools/07-Scripts/)

| Script | Purpose |
|--------|---------|
| `compliance_sdlc_validator.py` | Validate SDLC 6.3.0 folder structure |
| `compliance_sdlc_scanner.py` | Scan project for compliance |
| `quickstart_solo_setup.py` | Setup for solo developer |

---

## Training → Implementation Pathway

> Completed the [11-module training program](../08-Training-Materials/SDLC-Training-Materials.md)? Here's how training modules map to implementation guides:

| Training Module | Implementation Guide |
|-----------------|---------------------|
| Module 01 (SDLC Overview) | [Implementation Guide](SDLC-Implementation-Guide.md) — full lifecycle setup |
| Module 02 (Six Pillars) | [Compliance Enforcement](SDLC-Compliance-Enforcement-Guide.md) — enforce all pillars |
| Module 03 (Zero Mock) | [Pre-Commit Hooks](SDLC-PRE-COMMIT-HOOKS.md) — automated mock detection |
| Module 04 (Code Quality) | [Code Review Guide](SDLC-Code-Review-Guide.md) — 3-tier review framework |
| Module 05 (Dev Workflow) | [Pre-Commit Hooks](SDLC-PRE-COMMIT-HOOKS.md) + [Deployment Guide](SDLC-Deployment-Guide.md) |
| Module 06 (AI Tools) | [MCP Integration](MCP-Integration-Guide.md) + [Autonomous Codegen](AUTONOMOUS-CODEGEN-PATTERNS.md) |
| Module 07 (SASE Agentic) | [ACE-AEE Architecture](ACE-AEE-Reference-Architecture.md) + [Multi-Agent Patterns](MULTI-AGENT-PATTERNS.md) |
| Module 08 (Authority) | [Stage Consistency Validation](SDLC-Stage-Consistency-Validation-Guide.md) — gate enforcement |
| Module 09 (Gate Workshop) | [Implementation Guide](SDLC-Implementation-Guide.md) — gate setup section |
| Module 10 (ADR & Sprint) | [Implementation Guide](SDLC-Implementation-Guide.md) — planning section |
| Module 11 (Remote Teams) | [Conversation-First Governance](CONVERSATION-FIRST-GOVERNANCE.md) — async workflows |

---

## Related Documentation

| Folder | Purpose |
|--------|---------|
| [01-Overview/](../01-Overview/) | Executive Summary |
| [02-Core-Methodology/](../02-Core-Methodology/) | 10-stage lifecycle, 9 Mental Models, System Thinking |
| [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) | AI governance principles, Long-Running Agent Protocol |
| [04-AI-TOOLS-LANDSCAPE/](../04-AI-TOOLS-LANDSCAPE/) | AI tool profiles, best practices 2026 |
| [05-Templates-Tools/](../05-Templates-Tools/) | SASE artifacts, SOUL templates, ROI Calculator |
| [06-Case-Studies/](../06-Case-Studies/) | Battle-tested platform examples |
| [08-Training-Materials/](../08-Training-Materials/) | 11-module training program (39h) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 6.3.0 | Mar 2026 | Agentic SDLC: +5 new guides (Multi-Agent, Citizen Dev, Conversation-First, Autonomous Codegen, MCP), Lean Ring 1 cross-ref updates, tool-agnostic sanitization |
| 6.0.6 | Feb 2026 | Anthropic Best Practices, CLAUDE.md Standard, MRP Template |
| 6.0.4 | Feb 2026 | TDD Workflow Integration, 3-Phase Sprint Lifecycle |
| 6.0.1 | Feb 2026 | SPEC-0021 Stage Consistency Validation |

---

**Last Updated**: March 18, 2026
**Authority**: CTO + CPO Office
**Framework Version**: 6.3.0
