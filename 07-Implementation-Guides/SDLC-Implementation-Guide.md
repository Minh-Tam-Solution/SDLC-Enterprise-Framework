# SDLC 6.1.0 Implementation Guide - From Zero to Production

**Version**: 6.1.0
**Date**: January 29, 2026
**Status**: ACTIVE - PRODUCTION READY
**Target**: Any team, any size, any experience level
**Promise**: Working SDLC in 1 day (LITE) to 4 weeks (ENTERPRISE)
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles

---

## 🎯 30-Second Overview

**What is SDLC 6.1.0?**
- A **10-stage lifecycle** framework (WHY → GOVERN)
- With **7-Pillar Architecture** + **Section 7 Quality Assurance System**
- With **SASE** for human-AI collaboration (AGENTS.md + 3 artifacts)
- And **4-tier scaling** (LITE → ENTERPRISE)

**Why use it?**
- **14,822% ROI** validated across 4 production systems
- **60-70% → <30%** feature waste reduction
- **10-50x** productivity improvement

**How to start?** (Depends on your situation)
1. Pick your implementation path (see below)
2. Pick your tier
3. Follow the Quick Start for your scenario

---

## 🛤️ Pick Your Implementation Path (CRITICAL)

**Your situation determines your path.** Don't skip this section.

| Situation | Path | Time | Start Here |
|-----------|------|------|------------|
| **New project** (Greenfield) | Full Setup | 1 day - 4 weeks | Continue below → [Pick Your Tier](#-pick-your-tier-1-minute) |
| **Existing project** (Brownfield) | Incremental Adoption | 1 week - 2 months | → [Brownfield Implementation](#-brownfield-implementation-existing-projects) |
| **Upgrading from 5.x** | Framework Migration | 2-5 days | → [Version Migration](#-version-migration-5x--60) |

### Decision Tree

```
Is this a NEW project?
├── YES → Greenfield Path (this guide's main content)
│         └── Pick Tier → Follow Quick Start → Done
│
└── NO → Already have code/docs?
          ├── YES, using SDLC 5.x/6.x → Version Migration Path
          │         └── Run compatibility check → Fix gaps → Done
          │
          └── YES, but NO SDLC yet → Brownfield Path
                    └── Phase 1-4 incremental → Don't disrupt existing work
```

### SDLC Orchestrator CLI Support

```bash
# Greenfield (new project)
sdlcctl init /path/to/project --tier STANDARD

# Brownfield (existing project)
sdlcctl scan /path/to/project          # Assess current state
sdlcctl fix /path/to/project           # Auto-fix compliance gaps
sdlcctl report /path/to/project        # Generate compliance report

# Version migration (5.x → 6.0)
sdlcctl migrate /path/to/project --from 5.3 --to 6.0
```

---

## 📊 Pick Your Tier (1 Minute)

| Question | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|----------|------|----------|--------------|------------|
| Team size? | 1-2 | 3-10 | 10-50 | 50+ |
| Budget? | <$50K | $50-200K | $200K-1M | $1M+ |
| AI agents? | Optional | Helpful | Recommended | Required |
| Setup time? | **1 day** | **1 week** | **2 weeks** | **4 weeks** |

**Not sure?** → Start with LITE, upgrade later.

---

## 🚀 Quick Start: LITE Tier (1 Day)

### Morning (4 hours): Setup

**Step 1: Design Thinking (30 min)**
```markdown
Answer these 3 questions:
1. WHO is your user? (Name them, describe them)
2. WHAT problem do they have? (Be specific)
3. WHY does it matter? (Business value)

Done? You've completed Stage 00-01.
```

**Step 2: Quality Gates (30 min)**
```bash
# Install pre-commit hooks (copy-paste this)
pip install pre-commit  # or npm install husky
# Add to your repo - see SDLC-PRE-COMMIT-HOOKS.md
```

**Step 3: Code Review Setup (30 min)**
- Solo developer? → Self-review checklist
- 2 people? → Cross-review PRs
- See: `SDLC-Code-Review-Guide.md`

### Afternoon (4 hours): First Feature

**Step 4: Build with SDLC**
```yaml
Before coding:
  - [ ] Design Thinking done (3 questions answered)
  - [ ] Pre-commit hooks installed

While coding:
  - [ ] Write tests (aim for 80% coverage)
  - [ ] Run pre-commit before each commit

Before merge:
  - [ ] Self-review with checklist
  - [ ] All tests pass
```

**Step 5: Deploy**
- Push to production
- Monitor for 24 hours
- Celebrate your first SDLC-compliant feature! 🎉

### LITE Success Checklist
- [ ] Design Thinking completed (30 min)
- [ ] Pre-commit hooks installed
- [ ] First feature deployed
- [ ] Self-review process working

**Time**: 1 day | **Cost**: $0 | **ROI**: 10x productivity

---

## 🚀 Quick Start: STANDARD Tier (1 Week)

### Day 1: Foundation

**Morning: Team Workshop (2 hours)**
```markdown
With your team (3-10 people), answer:
1. WHO are our users? (Create 2-3 personas)
2. WHAT are their top 3 pain points?
3. WHY should we solve this now?

Output: 1-page problem statement
```

**Afternoon: Setup**
- All developers install pre-commit hooks
- Choose code review approach:
  - Free: Manual review with checklists
  - AI-powered: Cursor/Claude/ChatGPT (if you have subscription)
- Create PR template

### Day 2-3: Pilot Feature

**Select 1 feature** to build with full SDLC:
```yaml
Day 2:
  - Design session (1 hour)
  - Architecture discussion (1 hour)
  - Start development

Day 3:
  - Complete development
  - Code reviews (all PRs)
  - Integration testing
```

### Day 4: Deploy & Test

```yaml
Morning:
  - Deploy to staging
  - UAT with real users (3-5 people)
  - Fix critical issues

Afternoon:
  - Deploy to production
  - Monitor performance
  - Document learnings
```

### Day 5: Process Lock-In

```yaml
Morning:
  - Team retrospective
  - Document what worked
  - Document what didn't

Afternoon:
  - Create team playbook (1-2 pages)
  - Train remaining team members
  - Declare SDLC operational!
```

### STANDARD Success Checklist
- [ ] All devs have pre-commit hooks
- [ ] Design Thinking workshop done
- [ ] Code review process chosen
- [ ] Pilot feature deployed
- [ ] Team playbook created
- [ ] All team members trained

**Time**: 1 week | **Cost**: $0-200 | **ROI**: 20x team productivity

---

## 🚀 Quick Start: PROFESSIONAL Tier (2 Weeks)

### Week 1: Foundation & Pilot

| Day | Morning | Afternoon |
|-----|---------|-----------|
| **1** | Leadership alignment (CEO/CTO/CPO) | Define tier-specific requirements |
| **2** | Design Thinking training (all staff) | Setup development environment |
| **3** | Pilot team selection (10 devs) | Start pilot feature |
| **4** | Pilot development | Code reviews + testing |
| **5** | Pilot deployment | Retrospective + learnings |

### Week 2: Rollout & Operations

| Day | Morning | Afternoon |
|-----|---------|-----------|
| **6** | Train Phase 1 teams (50%) | Setup monitoring (Stage 06) |
| **7** | Phase 1 starts full SDLC | Integration setup (Stage 07) |
| **8** | Train Phase 2 teams (50%) | Collaboration protocols (Stage 08) |
| **9** | Full organization active | Governance setup (Stage 09) |
| **10** | Organization-wide launch | Celebration + metrics review |

### PROFESSIONAL Additions

**SASE Integration** (for AI-assisted teams):
```yaml
SE4H (Human - Agent Coach):
  Creates: AGENTS.md (context), VCR (approvals)
  Role: Define what to build, approve results

SE4A (Agent - AI Executor):
  Creates: CRP (questions), MRP (evidence)
  Role: Build what human defines, provide evidence

Workflow: AGENTS.md → [work] → CRP (if stuck) → MRP → VCR
```

**Quality Gates**:
- G0.1: Problem Definition (Stage 00)
- G2: Design Ready (Stage 02)
- G3: Ship Ready (before production)

### PROFESSIONAL Success Checklist
- [ ] Leadership aligned
- [ ] All teams trained
- [ ] SASE workflow understood (if using AI)
- [ ] Quality gates active
- [ ] Monitoring live
- [ ] Organization-wide launch complete

**Time**: 2 weeks | **Cost**: $5-20K | **ROI**: 30x organizational efficiency

---

## 🚀 Quick Start: ENTERPRISE Tier (4 Weeks)

### Week 1: Strategy & Governance

```yaml
Focus: Leadership alignment + Compliance framework
- Executive briefing (CEO/CTO/CPO/CISO)
- Compliance requirements (SOC 2? ISO? CMMI level?)
- Select 2-3 pilot teams (diverse domains)
- Define success metrics
```

### Week 2: Pilot Implementation

```yaml
Focus: Full 10-stage deployment for pilots
- Complete SDLC lifecycle for pilot teams
- Industry standards integration (OWASP, DORA, CMMI)
- SASE workflow with Level 2 (Structured Agentic)
- Establish baseline metrics
```

### Week 3: Phase 1 Rollout (50%)

```yaml
Focus: Half the organization
- Train and onboard Phase 1 teams
- Cross-team collaboration protocols
- Integration with enterprise tools (Jira, ServiceNow)
- Early metrics validation
```

### Week 4: Full Operation

```yaml
Focus: Complete rollout
- Phase 2 teams (remaining 50%)
- Governance dashboards live
- Compliance reporting automated
- Organization-wide launch
```

### ENTERPRISE Additions

**Full 10-Stage Implementation**:
```
Stage 00: WHY? - Problem validation, business case
Stage 01: WHAT? - Requirements, roadmap, planning
Stage 02: HOW? - Architecture, ADRs, design
Stage 04: BUILD - Development, code review
Stage 05: TEST - QA, UAT, security testing
Stage 06: DEPLOY - Release, zero-downtime
Stage 07: OPERATE - Monitoring, incidents, SLOs
Stage 03: INTEGRATE - APIs, external services
Stage 08: COLLABORATE - Teams, communication
Stage 09: GOVERN - Compliance, audits, governance
```

**Agentic Maturity Target**: Level 2 (Structured Agentic)
- All 6 SASE artifacts in use
- ACE (Agent Command Environment) for humans
- AEE (Agent Execution Environment) for agents

### ENTERPRISE Success Checklist
- [ ] All 10 stages operational
- [ ] Governance dashboards live
- [ ] Compliance reporting automated
- [ ] CMMI L3+ achieved (if target)
- [ ] 50x efficiency demonstrated
- [ ] Audit readiness validated

**Time**: 4 weeks | **Cost**: $50-200K | **ROI**: 50x enterprise-wide efficiency

---

## 📋 The 10 Stages (Reference)

### Foundation Stages (WHY → WHAT)
```
00 WHY?    - Is this worth building? (Design Thinking)
01 WHAT?   - What exactly should we build? (Requirements)
```

### Build Stages (HOW → DEPLOY)
```
02 HOW?    - How should we build it? (Architecture)
03 BUILD   - Building the solution (Development)
04 TEST    - Does it work correctly? (Quality)
05 DEPLOY  - Get it to users (Release)
```

### Run Stages (OPERATE → GOVERN)
```
06 OPERATE   - Keep it running (Production)
07 INTEGRATE - Connect with systems (APIs)
08 COLLABORATE - Work together (Teams)
09 GOVERN    - Stay compliant (Governance)
```

**Which stages for your tier?**
- LITE: 00, 02, 03 (minimum viable)
- STANDARD: 00-05 (build pipeline)
- PROFESSIONAL: 00-07 (operations)
- ENTERPRISE: 00-09 (full governance)

---

## 📁 Project Folder Structure (MANDATORY)

### Standard `/docs` Structure (10-Stage Aligned)

Every SDLC 6.1.0 compliant project **MUST** have this documentation structure using **shortened folder names**:

```
your-project/
├── docs/                              # 📚 SDLC Documentation Root
│   ├── 00-foundation/                 # Stage 00: WHY?
│   │   ├── problem-statement.md       # Design Thinking output
│   │   ├── business-case.md           # ROI justification
│   │   └── user-research/             # Empathy maps, personas
│   │
│   ├── 01-planning/                   # Stage 01: WHAT?
│   │   ├── requirements.md            # Functional requirements
│   │   ├── user-stories.md            # User stories/epics
│   │   └── roadmap.md                 # Product roadmap
│   │
│   ├── 02-design/                     # Stage 02: HOW?
│   │   ├── 01-ADRs/                   # Architecture Decision Records (SPEC-XXXX-ADR-XXX)
│   │   ├── 02-System-Architecture/    # System architecture docs
│   │   ├── 14-Technical-Specs/        # Technical Specifications (SPEC-XXXX)
│   │   └── 15-API-Specs/              # API Specifications (optional)
│   │
│   ├── 03-integrate/                  # Stage 03: INTEGRATE
│   │   ├── api-contracts/             # External API docs
│   │   ├── integration-guides/        # How to integrate
│   │   └── third-party/               # Vendor integrations
│   │
│   ├── 04-build/                      # Stage 04: BUILD
│   │   ├── coding-standards.md        # Team conventions
│   │   ├── setup-guide.md             # Dev environment setup
│   │   └── sprint-logs/               # Sprint documentation
│   │
│   ├── 05-test/                       # Stage 05: TEST
│   │   ├── test-strategy.md           # Testing approach
│   │   ├── test-cases/                # Test case documentation
│   │   └── qa-reports/                # QA findings
│   │
│   ├── 06-deploy/                     # Stage 06: DEPLOY
│   │   ├── deployment-guide.md        # How to deploy
│   │   ├── release-notes/             # Version release notes
│   │   └── rollback-procedures.md     # Rollback steps
│   │
│   ├── 07-operate/                    # Stage 07: OPERATE
│   │   ├── runbooks/                  # Operational procedures
│   │   ├── monitoring.md              # Monitoring setup
│   │   └── incident-reports/          # Post-mortems
│   │
│   ├── 08-collaborate/                # Stage 08: COLLABORATE
│   │   ├── 01-SDLC-Compliance/        # ⭐ Project SDLC context (CLAUDE.md, AGENTS.md)
│   │   ├── 02-Team-Protocols/         # Team agreements
│   │   ├── 03-Meeting-Notes/          # Meeting records
│   │   └── 04-Onboarding/             # New member guide
│   │
│   ├── 09-govern/                     # Stage 09: GOVERN
│   │   ├── compliance/                # Compliance evidence
│   │   ├── metrics/                   # KPI dashboards
│   │   └── audit-logs/                # Audit trail
│   │
│   └── 10-archive/                    # 📦 Project Archive (Optional)
│       ├── deprecated-features/       # Old features removed from codebase
│       ├── old-integrations/          # Deprecated integrations
│       └── historical-docs/           # Documents not belonging to any stage
│
├── src/                               # 💻 Source Code
├── tests/                             # 🧪 Test Files
├── .sdlc/                             # ⚙️ SDLC Configuration
│   ├── config.json                    # Project tier & settings
│   └── checklists/                    # Review checklists
├── CLAUDE.md                          # 🤖 AI Agent Context (STANDARD+)
└── README.md                          # 📖 Project Overview
```

### Folder Naming Convention

**SDLC 6.1.0 uses shortened folder names** (not long descriptive names):

| Stage | Folder Name | NOT |
|-------|-------------|-----|
| 00 WHY | `00-foundation` | ~~00-Project-Foundation~~ |
| 01 WHAT | `01-planning` | ~~01-Planning-Analysis~~ |
| 02 HOW | `02-design` | ~~02-Architecture-Design~~ |
| 03 INTEGRATE | `03-integrate` | ~~03-Integration~~ |
| 04 BUILD | `04-build` | ~~04-Development~~ |
| 05 TEST | `05-test` | ~~05-Quality-Assurance~~ |
| 06 DEPLOY | `06-deploy` | ~~06-Deployment~~ |
| 07 OPERATE | `07-operate` | ~~07-Operations~~ |
| 08 COLLABORATE | `08-collaborate` | ~~08-Team-Management~~ |
| 09 GOVERN | `09-govern` | ~~09-Executive-Reports~~ |
| 10 ARCHIVE | `10-archive` | Project-level archive (optional) |

### Archive Strategy (Important!)

**Two types of archives exist:**

| Archive Type | Location | Purpose |
|--------------|----------|---------|
| **Project Archive** | `docs/10-archive/` | Old documents that don't belong to any stage (deprecated features, historical docs) |
| **Stage-Level Legacy** | `docs/XX-stage/99-legacy/` | Old documents **within a specific stage** (e.g., old design decisions in `02-design/99-legacy/`) |

**Example:**
```
docs/
├── 02-design/
│   ├── current-architecture.md      # Active document
│   └── 99-legacy/                    # OLD design docs
│       └── v1-architecture.md        # Previous version
├── 09-govern/
│   └── 99-legacy/                    # OLD governance docs
│       └── old-compliance-report.md
└── 10-archive/                       # Project-level archive
    ├── deprecated-feature-x/         # Feature removed from codebase
    └── old-vendor-integration/       # Vendor no longer used
```

**Rule of thumb:**
- If the old doc relates to a specific stage → `XX-stage/99-legacy/`
- If the old doc doesn't fit any stage → `docs/10-archive/`

### Minimum Structure by Tier

| Tier | Required Folders | Optional |
|------|-----------------|----------|
| **LITE** | `docs/00-foundation/`, `README.md` | All others |
| **STANDARD** | `docs/00-05/`, `CLAUDE.md`, `.sdlc/` | `docs/06-09/` |
| **PROFESSIONAL** | `docs/00-07/`, full `.sdlc/` | `docs/08-09/` |
| **ENTERPRISE** | **ALL folders** (00-09) | None - all required |

### Quick Setup Commands

**LITE (1 command):**
```bash
mkdir -p docs/00-foundation && echo "# Problem Statement" > docs/00-foundation/problem-statement.md
```

**STANDARD (copy-paste):**
```bash
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy}
mkdir -p docs/02-design/ADRs
mkdir -p .sdlc/checklists
```

**PROFESSIONAL (copy-paste):**
```bash
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy,07-operate}
mkdir -p docs/02-design/ADRs
mkdir -p docs/03-integrate/{api-contracts,third-party}
mkdir -p docs/07-operate/runbooks
mkdir -p .sdlc/checklists
```

**ENTERPRISE (copy-paste):**
```bash
mkdir -p docs/{00-foundation,01-planning,02-design,03-integrate,04-build,05-test,06-deploy,07-operate,08-collaborate,09-govern}
mkdir -p docs/00-foundation/user-research
mkdir -p docs/02-design/ADRs
mkdir -p docs/03-integrate/{api-contracts,third-party}
mkdir -p docs/04-build/sprint-logs
mkdir -p docs/05-test/{test-cases,qa-reports}
mkdir -p docs/06-deploy/release-notes
mkdir -p docs/07-operate/{runbooks,incident-reports}
mkdir -p docs/08-collaborate/meeting-notes
mkdir -p docs/09-govern/{compliance,metrics,audit-logs}
mkdir -p .sdlc/checklists
```

### File Naming Standards

| Language | Convention | Max Length | Example |
|----------|------------|------------|---------|
| **Python** | `snake_case` | 50 chars | `user_service.py` |
| **TypeScript** | `camelCase` | 50 chars | `userService.ts` |
| **React** | `PascalCase` | 50 chars | `UserDashboard.tsx` |
| **Markdown** | `kebab-case` | 60 chars | `deployment-guide.md` |
| **Folders** | `kebab-case` | 30 chars | `sprint-logs/` |

---

## 📋 Specifications Location (MANDATORY)

### Where to Put Specs?

**All specifications MUST be in `02-design/` with proper numbering:**

```
docs/02-design/
├── 01-ADRs/                          # Architecture Decision Records
│   ├── SPEC-0001-ADR-001-Database-Choice.md
│   ├── SPEC-0002-ADR-002-Auth-Strategy.md
│   └── ...
│
├── 14-Technical-Specs/               # Technical Specifications
│   ├── SPEC-0010-Auth-Service.md
│   ├── SPEC-0011-API-Gateway.md
│   ├── SPEC-0012-Event-Bus.md
│   └── ...
│
└── 15-API-Specs/                     # API Specifications (optional subfolder)
    ├── SPEC-0050-REST-API-v1.md
    ├── SPEC-0051-WebSocket-API.md
    └── ...
```

### Specification Numbering Convention

```
SPEC-XXXX[-Type]-Name.md

Format:
  SPEC-    : Prefix (mandatory)
  XXXX     : 4-digit sequential number (0001-9999)
  Type     : Optional type (ADR, API, etc.)
  Name     : Descriptive name (kebab-case)

Examples:
  SPEC-0001-ADR-001-Database-Choice.md    # ADR type
  SPEC-0010-Auth-Service.md               # Technical spec
  SPEC-0050-API-User-Management.md        # API spec
```

### Numbering Ranges (Recommended)

| Range | Type | Example |
|-------|------|---------|
| `0001-0099` | ADRs (Architecture Decisions) | `SPEC-0001-ADR-001-...` |
| `0100-0499` | Technical Specs (Services) | `SPEC-0100-Auth-Service.md` |
| `0500-0799` | API Specs | `SPEC-0500-REST-API-v1.md` |
| `0800-0999` | Integration Specs | `SPEC-0800-GitHub-Integration.md` |

### ❌ Anti-Pattern: Specs Outside 02-design

```
# ❌ WRONG - Don't do this
docs/specs/                    # Non-compliant folder
docs/specifications/           # Non-compliant folder
docs/04-build/specs/           # Wrong stage

# ✅ CORRECT - Always in 02-design
docs/02-design/14-Technical-Specs/SPEC-0001-*.md
```

---

## 🏢 SDLC Compliance Folder (Project Context)

### Purpose

Every project implementing SDLC 6.1.0 should have an **SDLC Compliance folder** containing:
- Project-specific summary of the Framework
- AI context files (CLAUDE.md, AGENTS.md)
- Quick reference for team members (human + AI)

**This folder helps new team members quickly understand the project without reading the entire Framework.**

### Standard Location: `08-collaborate/01-SDLC-Compliance/`

```
docs/08-collaborate/
└── 01-SDLC-Compliance/               # SDLC Context for this project
    ├── CLAUDE.md                     # AI assistant context (project-specific)
    ├── AGENTS.md                     # Agent guidelines & boundaries
    ├── PROJECT-CONTEXT.md            # Human-readable quick reference
    ├── COMPLIANCE-CHECKLIST.md       # Progress tracking
    └── FRAMEWORK-SUMMARY.md          # SDLC 6.1.0 summary (optional)
```

### Why 08-collaborate (Not 09-govern)?

| Aspect | 08-collaborate | 09-govern |
|--------|----------------|-----------|
| **Primary audience** | Team members (AI + Human) | Leadership, Auditors |
| **Content type** | Context, onboarding, quick ref | Audit trails, reports |
| **Update frequency** | Per sprint/feature | Monthly/Quarterly |
| **SDLC Compliance fits** | ✅ **Yes** - Team context | ❌ No - Not audit material |

### Root-Level Symlinks (Recommended)

For convenience, create symlinks at project root:

```bash
# Create symlinks for quick access
ln -s docs/08-collaborate/01-SDLC-Compliance/CLAUDE.md ./CLAUDE.md
ln -s docs/08-collaborate/01-SDLC-Compliance/AGENTS.md ./AGENTS.md
```

**Result:**
```
your-project/
├── CLAUDE.md → docs/08-collaborate/01-SDLC-Compliance/CLAUDE.md
├── AGENTS.md → docs/08-collaborate/01-SDLC-Compliance/AGENTS.md
├── docs/
│   └── 08-collaborate/
│       └── 01-SDLC-Compliance/
│           ├── CLAUDE.md           # Source of truth
│           ├── AGENTS.md           # Source of truth
│           └── ...
└── src/
```

### SDLC Compliance Contents

| File | Purpose | Required |
|------|---------|----------|
| `CLAUDE.md` | AI context: project overview, tech stack, conventions | STANDARD+ |
| `AGENTS.md` | Agent boundaries, tools, permissions | PROFESSIONAL+ |
| `PROJECT-CONTEXT.md` | Human-readable summary (non-technical) | LITE+ |
| `COMPLIANCE-CHECKLIST.md` | SDLC stage completion tracking | STANDARD+ |
| `FRAMEWORK-SUMMARY.md` | SDLC 6.1.0 quick reference | Optional |

### Migration for Existing Projects

If your project uses old location:
```bash
# Old locations (migrate from)
docs/08-Team-Management/01-SDLC-Compliance/    # Old naming
docs/09-govern/SDLC-Compliance/                # Wrong stage

# New standard location (migrate to)
docs/08-collaborate/01-SDLC-Compliance/        # Correct
```

### Validation

Run this to check your structure:
```bash
python3 path/to/sdlc_validator.py /your/project
```

---

## 🤖 SASE Quick Reference (AI Teams)

### SDLC 6.1.0 Simplified Artifacts

| # | Artifact | Created By | Purpose |
|---|----------|------------|---------|
| 1 | **AGENTS.md** | Human | AI context file (industry standard, 60K+ repos) |
| 2 | **CRP** (Consultation Request) | Agent | When uncertain, request human guidance |
| 3 | **MRP** (Merge-Readiness Pack) | Agent | 5-point evidence before merge |
| 4 | **VCR** (Version Controlled Resolution) | Human | Approval/rejection record |

> **⚠️ Deprecated in 6.0.0**: BRS, LPS, MTS → All merged into AGENTS.md

### Minimum Workflow (Level 1)
```
Human: AGENTS.md → Agent: [work] → Agent: MRP → Human: VCR
```

### Full Workflow (Level 2)
```
Human: AGENTS.md (context) → Agent: [work] →
Agent: CRP (if stuck) → Human: Answer →
Agent: MRP → Human: VCR
```

### Maturity Levels

| Level | Name | Who Uses |
|-------|------|----------|
| L0 | Tool-Assisted | ChatGPT/Copilot users (ad-hoc) |
| L1 | Agent-Assisted | Teams starting with SASE |
| L2 | Structured Agentic | Established PROFESSIONAL teams |
| L3 | Lifecycle Agentic | Future state (agents proactive) |

---

## 📊 Success Metrics by Tier

### LITE
- Setup: <1 day
- First feature: <1 week
- Bug rate: <5 bugs/feature
- Productivity: 10x baseline

### STANDARD
- Feature adoption: >60%
- Code review time: <30 min
- Test coverage: 80%+
- Deployment: Weekly

### PROFESSIONAL
- Feature adoption: >75%
- Change failure rate: <15%
- MTTR: <1 hour
- API latency (p95): <100ms

### ENTERPRISE
- Feature adoption: >80%
- CMMI level: L3+
- Compliance: 100%
- Time to market: 50% faster

---

## 🚨 Common Mistakes (Avoid These)

### Mistake 1: Skipping Design Thinking
```
❌ "We know what to build, let's just code"
✅ 30 minutes of Design Thinking saves weeks of rework
```

### Mistake 2: No Pre-commit Hooks
```
❌ "We'll fix issues in code review"
✅ Catch 80% of issues automatically before commit
```

### Mistake 3: Wrong Tier
```
❌ "We're a startup but let's do ENTERPRISE level"
✅ Start simple, upgrade when pain points appear
```

### Mistake 4: Skipping SASE Artifacts (AI Teams)
```
❌ "Just tell the AI what to build"
✅ AGENTS.md = clear context = better output
```

### Mistake 5: All Stages at Once
```
❌ "We need all 10 stages from day 1"
✅ Start with your tier's minimum, add stages as needed
```

---

## 🔄 Brownfield Implementation (Existing Projects)

**For teams with existing codebases that want to adopt SDLC 6.1.0 incrementally.**

### Philosophy: Don't Disrupt, Enhance

```yaml
Brownfield Principles:
  1. Never stop current work (ship features while adopting)
  2. Start with highest-ROI improvements (pre-commit hooks)
  3. Add structure gradually (don't reorganize everything day 1)
  4. Measure before/after (prove value to skeptics)
```

### 4-Phase Brownfield Adoption

| Phase | Focus | Time | Immediate Value |
|-------|-------|------|-----------------|
| **Phase 1** | Quality Gates | 1-2 days | Catch bugs before commit |
| **Phase 2** | Documentation Structure | 1 week | Find docs easily, onboard faster |
| **Phase 3** | AI Collaboration (SASE) | 2 weeks | 2-5x dev productivity with AI |
| **Phase 4** | Full Governance | 4 weeks | Compliance, metrics, audit trail |

### Phase 1: Quality Gates (Start Here)

```bash
# Day 1: Install pre-commit hooks
pip install pre-commit
# Copy .pre-commit-config.yaml from SDLC-PRE-COMMIT-HOOKS.md

# Day 2: Establish code review
# Choose tier from SDLC-Universal-Code-Review-Framework.md
```

**Guides:**
- [SDLC-PRE-COMMIT-HOOKS.md](SDLC-PRE-COMMIT-HOOKS.md) - Pre-commit setup
- [SDLC-Universal-Code-Review-Framework.md](SDLC-Universal-Code-Review-Framework.md) - Review tier selection

### Phase 2: Documentation Structure

```bash
# Scan existing structure
sdlcctl scan /your/project

# Auto-create missing folders (non-destructive)
sdlcctl fix /your/project --dry-run  # Preview changes
sdlcctl fix /your/project            # Apply changes

# Move existing docs to correct locations (MANUAL - be careful)
# Don't delete old locations until team is trained
```

**Key Rule:** Keep `99-legacy/` folders for old docs that don't fit new structure.

### Phase 3: AI Collaboration (SASE)

```yaml
Start Simple:
  1. Create AGENTS.md in project root (industry standard)
  2. Try CRP (Consultation Request) when AI is stuck
  3. Use MRP (Merge-Readiness Pack) for AI-generated code
  4. VCR (Version Controlled Resolution) for approvals

Don't:
  - Force all 4 artifacts immediately
  - Disrupt existing dev workflow
  - Expect perfect AI output on day 1
```

**Guides:**
- [ACE-AEE-Reference-Architecture.md](ACE-AEE-Reference-Architecture.md) - SASE architecture
- [../05-Templates-Tools/04-SASE-Artifacts/](../05-Templates-Tools/04-SASE-Artifacts/) - Templates

### Phase 4: Full Governance

```yaml
Only After Phases 1-3 Stable:
  - Quality Gates: Live for 2+ sprints
  - Documentation: 80%+ compliance
  - Team: Comfortable with workflow

Phase 4 Adds:
  - Stage 09 (GOVERN) - Compliance tracking
  - Metrics dashboards - DORA metrics, quality trends
  - Audit trail - Evidence Vault integration
```

**Guide:** [SDLC-Compliance-Enforcement-Guide.md](SDLC-Compliance-Enforcement-Guide.md)

### Brownfield by Tier

| Tier | Recommended Phases | Skip/Defer |
|------|-------------------|------------|
| LITE | Phase 1 only | Phases 2-4 (add when painful) |
| STANDARD | Phases 1-2 | Phases 3-4 (add in 1-2 months) |
| PROFESSIONAL | Phases 1-3 | Phase 4 (add in 2-3 months) |
| ENTERPRISE | All 4 Phases | None - all required |

---

## ⬆️ Version Migration (5.x → 6.1.0)

**For teams already using SDLC 5.x who want to upgrade to 6.1.0.**

### What Changed in 6.0.0?

| Component | 5.x | 6.0.0 | Migration Impact |
|-----------|-----|-------|------------------|
| **Pillars** | 7-Pillar | 7-Pillar + Section 7 (QA System) | LOW - additive |
| **SASE Artifacts** | 6 artifacts (BRS, LPS, MTS, CRP, MRP, VCR) | 4 artifacts (AGENTS.md, CRP, MRP, VCR) | MEDIUM - deprecations |
| **Folder Structure** | 10-stage + 99-legacy | Same + 10-archive clarification | LOW - compatible |
| **Quality System** | Pillar 4 only | Section 7 (Anti-Vibecoding, Progressive Routing) | NEW - additive |
| **AI Governance** | Principles scattered | 7 AI Governance Principles centralized | LOW - documentation |

### Migration Checklist

```yaml
Step 1: Update Version References (30 min)
  - [ ] Update CLAUDE.md header to 6.0.0
  - [ ] Update any framework version references
  - [ ] Update footer in documentation files

Step 2: SASE Artifact Migration (1-2 hours)
  - [ ] Create AGENTS.md if not exists (replaces BRS+MTS+LPS)
  - [ ] Keep CRP, MRP, VCR (unchanged)
  - [ ] Archive old BRS/LPS/MTS to 99-legacy (optional)
  - [ ] Update any SASE workflow documentation

Step 3: Section 7 Adoption (optional, 1-2 days)
  - [ ] Review Anti-Vibecoding specification
  - [ ] Configure Vibecoding Index thresholds
  - [ ] Set up Progressive Routing (if PROFESSIONAL+)
  - [ ] Enable Kill Switch criteria (if ENTERPRISE)

Step 4: Validation (30 min)
  - [ ] Run sdlcctl scan for 6.0.0 compliance
  - [ ] Fix any reported issues
  - [ ] Generate compliance report
```

### SASE Artifact Migration Detail

```yaml
Deprecated in 6.0.0:
  ❌ BRS (BriefingScript) → Merged into AGENTS.md
  ❌ LPS (LoopScript) → Merged into AGENTS.md
  ❌ MTS (MentorScript) → Merged into AGENTS.md

Still Active in 6.0.0:
  ✅ AGENTS.md (NEW - industry standard, 60K+ repos)
  ✅ CRP (Consultation Request) - Agent requests human help
  ✅ MRP (Merge-Readiness Pack) - 5-point evidence before merge
  ✅ VCR (Version Controlled Resolution) - Human approval record

Migration Path:
  1. Create AGENTS.md from existing BRS+MTS content
  2. Keep CRP/MRP/VCR workflows unchanged
  3. Move old BRS/LPS/MTS to 99-legacy folder
```

### CLI Migration Command

```bash
# Check 5.x → 6.0 compatibility
sdlcctl migrate /path/to/project --from 5.3 --to 6.0 --dry-run

# View migration plan
sdlcctl migrate /path/to/project --from 5.3 --to 6.0 --plan

# Execute migration (with backup)
sdlcctl migrate /path/to/project --from 5.3 --to 6.0 --backup

# Validate post-migration
sdlcctl scan /path/to/project --version 6.0
```

### Migration by Tier

| Tier | Migration Effort | Key Changes |
|------|------------------|-------------|
| LITE | **Minimal** (30 min) | Update version refs, create AGENTS.md |
| STANDARD | **Low** (1-2 hours) | + SASE artifact migration |
| PROFESSIONAL | **Medium** (1 day) | + Section 7 QA configuration |
| ENTERPRISE | **Full** (2-3 days) | + Kill Switch, Progressive Routing, Audit |

---

## 📚 Real-World Migration Case Studies

### Case Study 1: NQH-Bot Platform (Large-Scale Migration)

**Context**: Vietnamese F&B Workforce Management Platform with 65+ specifications

| Metric | Value |
|--------|-------|
| **Project Size** | Vietnamese F&B WFM Platform |
| **Total Specs** | 65 specifications |
| **Migration Timeline** | 8 weeks (Sprint 41-44) |
| **Total Effort** | 129 SP (~258 hours) |
| **Investment** | ₫338M |
| **ROI** | 74% first year, 7-month payback |
| **Final Compliance Score** | 87/100 |

**Key Success Factors:**

1. **ROI-Driven Planning**
   - Calculate investment vs expected value before starting
   - Present to CEO/CTO for formal approval
   - Track against milestones

2. **Phased Approach (P0 → P1 → P2 → P3)**
   ```yaml
   Phase P0: ADRs + API Specs (22 files) - Sprint 42
   Phase P1: Technical Designs (50 files) - Sprint 42-43
   Phase P2: UI/UX + Sprint Plans (40 files) - Sprint 43-44
   Phase P3: Archive + Cleanup (100+ files) - Ongoing
   ```

3. **Domain Complexity Factor**
   - Vietnamese F&B compliance specs required +40h extra effort
   - BHXH, OT Calculation, Labor Law specs need CTO/Legal review
   - Add complexity multiplier to estimates

4. **Centralized Specs with Stage-Based Numbering**
   ```
   docs/specs/
   ├── SPEC-01xx (Stage 01 - Planning)
   ├── SPEC-02xx (Stage 02 - Design)
   ├── ...
   └── SPEC-10xx (Stage 10 - Operations)
   ```

**Pitfalls Encountered:**

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Duplicate stage folders (04/05/06 collision) | High confusion | Check existing folders before creating |
| Version reference inconsistency | Confusing docs | Update ALL headers, not just main files |
| 23% specs missed 6.0.0 format | Validation failures | Use validation scripts early and often |

**Lessons Learned:**
- Large platforms (>100 files) benefit from centralized `docs/specs/`
- SPEC-XXYY numbering (stage-based) provides clear organization
- Pre-commit validation catches format issues before they accumulate

---

### Case Study 2: BFlow Platform (Stealth Pilot Approach)

**Context**: Multi-tenant SaaS platform with careful, risk-averse migration strategy

| Metric | Value |
|--------|-------|
| **Preparation Phase** | Sprint 122-126 (CTO-only, 10 weeks) |
| **Execution Phase** | Sprint 127-130 (Team rollout) |
| **Stealth Pilots** | 2 specs (CTO converts first) |
| **Training** | 8-hour workshop before team migration |
| **Gate Checkpoints** | G-Phase-0, G-Phase-1, G-Phase-2 |

**Stealth Pilot Methodology:**

```yaml
Philosophy: "Validate before rollout"

Week 1-4 (Sprint 122-123):
  - CTO creates all templates
  - CTO sets up validation tooling
  - Team allocation: 0% SDLC 6.1.0 work

Week 5-8 (Sprint 124-125):
  - CTO converts 2 specs as "stealth pilots"
  - Validates templates work in practice
  - Measures actual conversion velocity
  - Team allocation: Still 0% SDLC 6.1.0 work

Week 9-10 (Sprint 126):
  - Training materials finalized
  - Tech Lead dry-run review
  - Gate G-Phase-1 approval
  - Team ready for Sprint 127 kickoff
```

**Key Success Factors:**

1. **CTO Prepares Everything First**
   - Templates, validation tools, training materials
   - Team doesn't see incomplete work

2. **Stealth Pilots Validate Templates**
   - Real specs converted, not just theory
   - Velocity data informs Sprint 127 planning

3. **Clear Gate Checkpoints**
   - G-Phase-0: Initial setup (AGENTS.md, version refs)
   - G-Phase-1: Go-Live + CTO prep complete
   - G-Phase-2: Team pilot success metrics

4. **Team Communication Strategy**
   - Set expectations early (Feb 3): "Sprint 127 conditional on Go-Live"
   - Update regularly (Mar 28): "Still on track"
   - Final confirmation (Apr 12): "Sprint 127 starts Apr 15"

**Recommendation:**
For teams new to SDLC 6.1.0, the BFlow "stealth pilot" approach reduces risk by validating templates before team-wide rollout. Consider this approach if:
- Team has never migrated SDLC versions before
- High-stakes production system (can't afford migration failures)
- CTO/Tech Lead capacity available for preparation work

---

### Choosing Your Approach

| Scenario | Recommended Approach | Example |
|----------|---------------------|---------|
| **Small team, fast pace** | Direct migration | LITE/STANDARD tiers |
| **Large codebase, many specs** | Phased (P0→P3) | NQH-Bot approach |
| **Risk-averse, new to SDLC** | Stealth pilot | BFlow approach |
| **Enterprise, compliance-heavy** | Full governance + stealth | Combine both approaches |

---

## 📚 Related Documents

### Core Reading (Start Here)
- `SDLC-PRE-COMMIT-HOOKS.md` - Setup quality gates
- `SDLC-Code-Review-Guide.md` - Code review (all tiers)
- `../05-Templates-Tools/SASE-Artifacts/` - SASE templates

### By Need
- **Code Review**: `SDLC-Universal-Code-Review-Framework.md`
- **Deployment**: `SDLC-Deployment-Guide.md`
- **Crisis**: `SDLC-Crisis-Response-Guide.md`
- **Compliance**: `SDLC-Compliance-Enforcement-Guide.md`
- **Self-Contained Setup**: `SDLC-Self-Contained-Deployment-Guide.md`

### Reference
- `../02-Core-Methodology/SDLC-Core-Methodology.md` - Full 10-stage theory
- `../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` - SASE details
- `../03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md` - L0→L3 progression

---

## ✅ Final Checklist

### Before Starting
- [ ] I know my tier (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
- [ ] I have read this Quick Start section for my tier
- [ ] My team is ready (or it's just me for LITE)

### After 1 Week
- [ ] Pre-commit hooks installed on all machines
- [ ] Design Thinking completed for at least 1 feature
- [ ] First SDLC-compliant feature deployed
- [ ] Code review process working

### After 1 Month
- [ ] Team is comfortable with SDLC workflow
- [ ] Metrics show improvement (bugs, velocity, quality)
- [ ] Ready to upgrade tier if needed
- [ ] Contributing learnings back to process

---

## 🎯 One Page Summary

```
SDLC 6.1.0 = 10 Stages + 7 Pillars + Section 7 (QA) + 4 Tiers

Pick Your Path:
  Greenfield (new project)   → This guide's Quick Starts
  Brownfield (existing)      → Phase 1-4 incremental
  Migration (5.x → 6.0)      → Version migration section

Pick Your Tier:
  LITE (1-2 people)       → 1 day setup
  STANDARD (3-10)         → 1 week setup
  PROFESSIONAL (10-50)    → 2 weeks setup
  ENTERPRISE (50+)        → 4 weeks setup

Essential Steps:
  1. Design Thinking (30 min minimum)
  2. Pre-commit hooks (30 min setup)
  3. Code review process (choose your style)
  4. Deploy first feature (celebrate!)

SASE for AI Teams (6.0.0 Simplified):
  Human: AGENTS.md → Agent: [work] → MRP → Human: VCR

Success = Validated features with less waste
ROI = 10-50x improvement (tier dependent)
```

---

**Document Version**: 6.1.0
**Last Updated**: February 14, 2026
**Owner**: CPO Office
**Next Review**: March 2026
**Framework**: SDLC 6.1.0

---

***"Start simple. Deploy fast. Iterate always."***

***"The best process is the one you actually use."***

***"From zero to production in 1 day (LITE) to 4 weeks (ENTERPRISE)."***
