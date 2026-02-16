---
sdlc_version: "6.0.6"
document_type: "Framework Standard"
stage: "03 - AI GOVERNANCE"
status: "APPROVED"
owner: "CTO"
last_updated: "2026-02-17"
context_zone: "Core"
update_frequency: "Per sprint (or when new tier requirements emerge)"
priority: "P0"
source: "Industry best practices (Q1 2026) — AI assistant context documentation"
sprint: "174"
---

# CLAUDE.md Standard for AI-Assisted Development

**Framework Version**: SDLC 6.0.6
**Pillar**: 03 — AI Governance
**Classification**: ORANGE (Methodology Standard — affects all adopters)
**Effective Date**: February 17, 2026

---

## 1. Purpose

CLAUDE.md is the canonical context document for AI coding assistants (Claude Code, Cursor, Copilot, and other LLM-based development tools). It serves as the single source of truth that enables:

- **Zero-to-productive onboarding** (<10 minutes for AI assistants, <2 hours for new developers)
- **Consistent AI guidance** across all team members using the same codebase
- **Progressive disclosure** (4 layers: Quickstart → Patterns → Architecture → Deep Dive)
- **Reduced knowledge silos** (replaces tribal knowledge with structured documentation)

### 1.1 Why CLAUDE.md Matters

Traditional codebases rely on README.md for human onboarding. In the Software 3.0 era, AI assistants are the primary code navigators. CLAUDE.md bridges the gap between human-readable documentation and AI-actionable context.

### 1.2 Industry Adoption Context

As of Q1 2026, CLAUDE.md and AGENTS.md are emerging as industry standards across 60K+ repositories. Leading AI-native teams use CLAUDE.md as a **living data catalog** — not just documentation, but a navigation system for complex codebases. However, most implementations are **static** — updated manually and rarely maintained. SDLC 6.0.6 formalizes CLAUDE.md as a **living artifact** with tier-specific requirements and validation criteria.

---

## 2. Three-Tier Structure

CLAUDE.md requirements scale with team and project complexity. Choose the tier that matches your organization.

### 2.1 TIER 1: LITE

**Target**: Startups, small teams (<10 members), MVPs, open-source projects
**File**: `CLAUDE.md` (500-1,000 lines)

#### Required Sections

| Section | Content | Purpose |
|---------|---------|---------|
| **Project Overview** | 5-10 sentence description of what the project does, who it serves, and the core value proposition | Orients AI assistant to project context |
| **Tech Stack** | Languages, frameworks, databases, key dependencies with versions | Prevents version-mismatched code generation |
| **Quick Start** | 3-5 commands to clone, install, and run the development server | Enables immediate productivity |
| **Architecture Summary** | High-level diagram (text/ASCII) showing 2-4 major components and their relationships | Prevents cross-boundary violations |
| **Top 5 Decisions** | Brief description of 5 most important architecture decisions (or link to ADRs) | Prevents AI from suggesting alternatives to settled decisions |
| **Top 10 Tasks** | 10 most common development tasks with file paths and commands | Covers 80% of daily developer needs |
| **Constraints** | Hard constraints (legal, security, performance) that must never be violated | Safety guardrails for AI generation |
| **Emergency Contacts** | On-call rotation, escalation paths, critical service URLs | For incident response context |

#### Validation Criteria

An AI assistant reading only the LITE CLAUDE.md should be able to:

1. Run the development server within 5 minutes
2. Locate 3 key files for a given task
3. Identify 2 constraints that apply to any code generation request
4. Understand the high-level architecture without reading source code

#### LITE Template

```markdown
# CLAUDE AI PROJECT CONTEXT — [PROJECT NAME]

**Version**: [X.Y.Z]
**Status**: [Active | Maintenance | Archived]
**Last Updated**: [YYYY-MM-DD]

---

## Project Overview
[5-10 sentences: what, who, why]

## Tech Stack
- **Language**: [e.g., Python 3.11+]
- **Framework**: [e.g., FastAPI 0.104+]
- **Database**: [e.g., PostgreSQL 15.5]
- **Cache**: [e.g., Redis 7.2]
- **Frontend**: [e.g., React 18 + TypeScript 5.0]

## Quick Start
\```bash
git clone [repo-url]
cd [project-name]
[install-command]
[run-command]
\```

## Architecture
\```
[ASCII diagram showing 2-4 major components]
\```

## Key Decisions
1. [Decision 1 — why, not what]
2. [Decision 2]
3. [Decision 3]
4. [Decision 4]
5. [Decision 5]

## Common Tasks
1. **[Task Name]**: `[command]` — affects `[file-path]`
2. ...

## Constraints
- [Constraint 1: e.g., "Never import AGPL libraries directly"]
- [Constraint 2: e.g., "API latency must be <100ms p95"]

## Emergency
- **On-call**: [contact]
- **Status page**: [URL]
```

---

### 2.2 TIER 2: PRO

**Target**: SMBs, growing teams (10-100 members), multi-module projects
**File**: `CLAUDE.md` (1,500-3,000 lines)

#### Required Sections

All LITE sections, plus:

| Section | Content | Purpose |
|---------|---------|---------|
| **Module Zones** | 6-10 module-specific sections with key files, state machines, debugging patterns, and test commands | Enables focused navigation within large codebases |
| **Debugging Patterns** | Top 10 most common bugs/issues and their resolution steps | Prevents repeated debugging cycles |
| **Test Commands** | Per-module test execution commands with expected output | Enables AI-assisted testing |
| **Onboarding Checklist** | 5-7 sequential tasks for new team members (with AI assistance) | Structured ramp-up path |
| **Integration Map** | Which module calls which, with API contracts and data flow | Prevents integration regressions |

#### Module Zone Structure

Each module zone follows a consistent structure:

```markdown
## Module: [Module Name]

**Purpose**: [1-2 sentences]

**Key Files**:
- `path/to/entry_point.py` — [description]
- `path/to/service.py` — [description]
- `path/to/model.py` — [description]

**State Machine** (if applicable):
\```
STATE_A ──action──> STATE_B ──action──> STATE_C
\```

**Common Tasks**:
1. [Task]: `[command]`
2. [Task]: `[command]`

**Debugging**:
- **Issue**: [common issue description]
  - **Root Cause**: [explanation]
  - **Fix**: [resolution steps]

**Tests**:
\```bash
[test command with environment variables]
\```

**Dependencies**:
- Upstream: [services this module depends on]
- Downstream: [services that depend on this module]
```

#### Validation Criteria

An AI assistant reading only the PRO CLAUDE.md should be able to:

1. Implement a small feature (<50 LOC) within a single module in <15 minutes
2. Diagnose a known bug using the debugging patterns section
3. Run tests for a specific module without needing to read CI/CD configs
4. Understand data flow between 2 connected modules

---

### 2.3 TIER 3: ENTERPRISE

**Target**: Large enterprises (100+ members), regulated industries, multi-repo systems
**Files**: `CLAUDE.md` (2,000 lines) + `docs/CLAUDE/*.md` (10+ supplementary files)

#### Required Sections

All PRO sections, plus:

| Section | Content | Purpose |
|---------|---------|---------|
| **System Decomposition** | Separate CLAUDE docs per major system (Gateway, Auth, Payment, Reporting) | Manages context window limitations for large codebases |
| **Cross-System Dependencies** | Explicit dependency graph with API versions, SLAs, and circuit breaker configs | Prevents cascading failures from AI-generated changes |
| **Compliance Checklists** | SOC2, HIPAA, GDPR, PCI-DSS requirements mapped to code sections | Ensures AI never generates non-compliant code |
| **Runbook Library** | 20+ operational runbooks with decision trees | Enables AI-assisted incident response |
| **Change Impact Matrix** | For each system, list other systems that would be affected by changes | Prevents unintended side effects |
| **Security Boundary Map** | Network boundaries, trust zones, data classification per service | Prevents data leaks across trust boundaries |

#### File Organization

```
project-root/
├── CLAUDE.md                          # Master index (2,000 lines)
├── docs/
│   └── CLAUDE/
│       ├── gateway-system.md          # Gateway service deep dive
│       ├── auth-system.md             # Authentication & authorization
│       ├── payment-system.md          # Payment processing (PCI-DSS)
│       ├── reporting-system.md        # Analytics & dashboards
│       ├── compliance-checklist.md    # Regulatory requirements
│       ├── runbooks/
│       │   ├── incident-response.md
│       │   ├── deployment-rollback.md
│       │   └── data-recovery.md
│       └── integration-contracts/
│           ├── gateway-auth.md
│           └── auth-payment.md
```

#### Validation Criteria

An AI assistant reading the ENTERPRISE CLAUDE.md ecosystem should be able to:

1. Navigate a 500K+ LOC codebase and locate the root cause of a production incident in <20 minutes
2. Determine compliance implications of any code change
3. Identify all downstream systems affected by a proposed change
4. Generate code that respects security boundaries and data classification

---

## 3. Content Principles

### 3.1 Living Documentation

CLAUDE.md must be updated every sprint. Stale CLAUDE.md is worse than no CLAUDE.md because it generates incorrect AI guidance.

**Update Triggers**:
- New module added or removed
- Architecture decision changed (new ADR)
- Common debugging pattern discovered
- Test commands changed
- Dependency versions updated

**Sprint Ceremony**: Include "CLAUDE.md review" in sprint retrospective checklist.

### 3.2 Progressive Disclosure

CLAUDE.md uses a 4-layer progressive disclosure model:

| Layer | Content | Audience |
|-------|---------|----------|
| **L1: Quickstart** | Project overview, tech stack, quick start commands | New AI assistant, first 5 minutes |
| **L2: Patterns** | Common tasks, debugging patterns, test commands | AI assistant working on a known task |
| **L3: Architecture** | Module zones, state machines, integration maps | AI assistant implementing a new feature |
| **L4: Deep Dive** | Cross-system dependencies, compliance, runbooks | AI assistant debugging production issues |

**Rule**: Each layer should be self-contained. An AI assistant at Layer 2 should not need to read Layer 4 content to complete a routine task.

### 3.3 Action-Oriented Content

Every section must contain **file paths** and **commands**, not abstract descriptions.

```markdown
# BAD (abstract)
The gate engine uses OPA for policy evaluation. Policies are stored
in the policy-packs directory.

# GOOD (action-oriented)
## Gate Engine → OPA Integration
- **Policy files**: `backend/policy-packs/rego/*.rego`
- **OPA service**: `backend/app/services/opa_service.py:evaluate_policy()`
- **Test OPA locally**:
  \```bash
  curl -X POST http://localhost:8185/v1/data/sdlc/gates/g1 \
    -d '{"input": {"gate_type": "G1", "evidence_count": 3}}'
  \```
```

### 3.4 Constraint-First

Hard constraints (legal, security, performance) must appear early in the document and be clearly marked. AI assistants scan from top to bottom — constraints buried at line 3,000 are effectively invisible.

**Constraint Format**:
```markdown
## CRITICAL CONSTRAINTS (AI MUST FOLLOW)
1. **AGPL Containment**: NEVER import AGPL libraries (MinIO SDK, Grafana SDK). Use network-only HTTP API calls.
2. **Performance Budget**: API latency MUST be <100ms p95. No N+1 queries.
3. **Zero Mock Policy**: No `// TODO`, no `pass # placeholder`, no `return { mock: true }`.
```

---

## 4. Tier Selection Guide

### Decision Tree

```
Is your team >100 members OR in a regulated industry?
  ├── YES → ENTERPRISE tier
  └── NO
       Is your project multi-module (>3 modules) OR team >10 members?
         ├── YES → PRO tier
         └── NO → LITE tier
```

### Tier Mapping to SDLC 6.0.6 Project Classification

| SDLC Tier | CLAUDE.md Tier | Rationale |
|-----------|---------------|-----------|
| **LITE** | LITE | Small projects, minimal governance |
| **STANDARD** | LITE or PRO | Growing projects, evaluate complexity |
| **PROFESSIONAL** | PRO | Multi-module, established teams |
| **ENTERPRISE** | ENTERPRISE | Large-scale, regulated environments |

---

## 5. Platform Automation Opportunities

Any platform implementing SDLC 6.0.6 can automate CLAUDE.md management:

### 5.1 Template Generation

Platforms should provide scaffolding that generates CLAUDE.md templates matching the project's tier (LITE/PRO/ENTERPRISE) with pre-filled sections.

### 5.2 Quality Gate Validation

Gate G1 (Consultation) should validate CLAUDE.md structure:
- Presence of required sections for the project's tier
- File paths reference actual existing files
- Commands are executable (syntax validation)
- Constraints section exists and is non-empty

### 5.3 Dynamic Updates

Platforms may auto-update CLAUDE.md sections based on lifecycle events:
- Gate pass/fail → Update "Project Status" section
- New ADR approved → Update "Key Decisions" section
- Module added → Scaffold new Module Zone
- Bug resolved → Add to "Debugging Patterns"

---

## 6. Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| **Onboarding time reduction** | 50% (4h → 2h average) | Survey new hires after 1 week |
| **AI assistant accuracy** | >90% on "find file for task X" | Automated test suite against CLAUDE.md |
| **Developer satisfaction** | >80% report "CLAUDE.md is my first reference" | Quarterly developer survey |
| **Stale content rate** | <10% of sections outdated | Automated freshness check (last_updated) |
| **Constraint violation rate** | 0% for CRITICAL constraints | Pre-commit hook + CI/CD validation |

---

## 7. Anti-Patterns

### 7.1 Information Dump

**Problem**: CLAUDE.md with 10,000+ lines of every piece of documentation concatenated together.
**Why it fails**: Exceeds AI context window, dilutes important context, causes AI to hallucinate from irrelevant information.
**Fix**: Use progressive disclosure. Each tier has a line limit. Use supplementary files for ENTERPRISE.

### 7.2 Stale Documentation

**Problem**: CLAUDE.md created once and never updated.
**Why it fails**: AI generates code based on outdated architecture, wrong file paths, deprecated patterns.
**Fix**: Include in sprint retrospective checklist. Automated freshness warnings.

### 7.3 Abstract Philosophy

**Problem**: CLAUDE.md filled with design philosophy and principles without file paths or commands.
**Why it fails**: AI cannot translate abstract principles into concrete code. "We value clean code" is not actionable.
**Fix**: Every section must include file paths and executable commands.

### 7.4 Copy-Paste README

**Problem**: CLAUDE.md is a copy of README.md with minor formatting changes.
**Why it fails**: README.md is for humans (marketing, badges, contributing guide). CLAUDE.md is for AI assistants (file navigation, debugging, constraints).
**Fix**: CLAUDE.md and README.md serve different audiences. Write each for its target reader.

---

## 8. Adoption Roadmap

### Phase 1: Framework Standard — This Document

- Define 3-tier structure with validation criteria
- Provide templates for each tier
- Document anti-patterns and success metrics

### Phase 2: Reference Implementations

- Create PRO-tier and LITE-tier reference CLAUDE.md files for real projects
- Validate templates against the validation criteria in this document
- Collect adoption feedback from early adopters

### Phase 3: Platform Automation

- Platform CLI generates CLAUDE.md templates per tier
- Quality Gate G1 validates CLAUDE.md structure
- Dynamic updates from lifecycle events

---

## 9. References

- **SDLC 6.0.6**: Section 8 (Specification Standard)
- **Industry Context**: 60K+ repositories with CLAUDE.md/AGENTS.md as of Q1 2026
- **AI-Native Team Practices**: Multiple AI-first organizations use CLAUDE.md as living data catalogs (Q1 2026)

---

**Document Status**: APPROVED
**Approved By**: CTO
**Ring**: Core (timeless methodology, tool-agnostic)
**Next Review**: After reference implementations are validated
