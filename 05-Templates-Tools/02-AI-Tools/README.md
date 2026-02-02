# 🤖 AI Tools for SDLC 6.0.2
## Stage-Aligned AI Automation for Complete Lifecycle + SASE Integration

**Framework Version**: 6.0.2
**Date**: February 2, 2026
**Status**: ACTIVE - Production Standards + SASE/SE 3.0 + E2E API Testing
**Pillar**: 5 - SASE Integration (AI Tools)
**Scope**: AI tools mapped to all 10 SDLC stages (00-09) + 4-Tier Classification + Agentic Maturity
**Structure**: SDLC 6.0.2 (2-level maximum, files prefixed by category)
**Foundation**: Proven across 3 platforms (BFlow, NQH-Bot, MTEP)
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) principles

> **Versioning Note**: Individual prompt files have their own version numbers (e.g., v5.2.0) indicating when the prompt content was last refined. All prompts are compatible with SDLC Framework 6.0.2.

---

## 🆕 What's New in SDLC 6.0.2 (February 2026)

### E2E API Testing Enhancement (RFC-SDLC-602)

**SDLC 6.0.2** adds **standardized E2E API testing workflows** with OWASP security integration:

| Template | Purpose | File |
|----------|---------|------|
| **E2E API Testing Workflow** | 6-phase standardized testing process | `testing_e2e-api-testing-workflow.md` |
| **Security Testing Checklist** | OWASP API Top 10 (2023) coverage | `testing_security-testing-checklist.md` |

**Key Features**:
- **6-Phase Workflow**: Discovery → Configuration → Execution → Security → Reporting → CI/CD Integration
- **OWASP API Top 10**: Complete security checklist (2023 edition)
- **Stage Cross-Reference**: Bidirectional Stage 03 ↔ 05 traceability
- **SSOT Principle**: Single openapi.json source in Stage 03

**→ [Quick Start Guide: 07-Implementation-Guides/E2E-TESTING-QUICKSTART.md](../../07-Implementation-Guides/E2E-TESTING-QUICKSTART.md)**

**Validation Metrics (SOP Generator Pilot)**:
- 58 endpoints tested
- 84.5% pass rate
- 83% time savings (3h → 30min)
- CTO Approval: 9.2/10

---

## 🆕 What's New in SDLC 6.0.2 (January 2026)

### AI Governance Principles Integration

**SDLC 6.0.2** adds **timeless AI Governance Principles** that apply to ALL AI tools:

| Principle | Summary | Reference |
|-----------|---------|-----------|
| AI-Human Collaboration | Human guides, AI executes, Human verifies | [01-AI-Human-Collaboration.md](../../03-AI-GOVERNANCE/01-AI-Human-Collaboration.md) |
| Planning Mode | Risk-based trigger (>15 LOC, API changes, auth) | [03-Planning-Mode-Principle.md](../../03-AI-GOVERNANCE/03-Planning-Mode-Principle.md) |
| Verification-First | TDD with AI, evidence before merge | [04-Verification-Principle.md](../../03-AI-GOVERNANCE/04-Verification-Principle.md) |
| Context Management | AGENTS.md <60 lines | [05-Context-Management.md](../../03-AI-GOVERNANCE/05-Context-Management.md) |
| Anti-Patterns | Avoid blind acceptance, context stuffing | [07-Anti-Patterns.md](../../03-AI-GOVERNANCE/07-Anti-Patterns.md) |

**→ [Full principles: 03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/)**

> **Best Practices Note**: For AI agent best practices (planning mode, model selection, sub-agents), see [04-AI-TOOLS-LANDSCAPE/best-practices-2026/](../../04-AI-TOOLS-LANDSCAPE/best-practices-2026/).
>
> This folder focuses on **stage-aligned prompts** (WHAT to generate at each stage).

---

### 7-Pillar Architecture (SDLC 6.0.2+)

**SDLC 6.0.2+** features the **7-Pillar Architecture** with Sprint Planning Governance as Pillar 2:

```yaml
7-Pillar Framework:
  - Pillar 0: Design Thinking Foundation
  - Pillar 1: 10-Stage Lifecycle  
  - Pillar 2: Sprint Planning Governance (NEW)
  - Pillar 3: 4-Tier Classification
  - Pillar 4: Quality Gates (Dual-Track)
  - Pillar 5: SASE Integration
  - Pillar 6: Documentation Permanence
```

### SASE Integration for AI Tools

**SDLC 6.0.2** integrates **SE 3.0 SASE principles** into AI tool usage:

```yaml
SE4H (Human) Role with AI Tools:
  - Create BriefingScript before delegating to AI
  - Review AI outputs with MRP evidence
  - Approve changes with VCR

SE4A (AI Agent) Role:
  - Execute tasks based on BriefingScript
  - Generate code following MentorScript standards
  - Provide MRP evidence for review
```

### Agentic Maturity × AI Tools

| Level | How to Use AI Tools |
|-------|---------------------|
| **L0** Tool-Assisted | Use AI Tools directly (ad-hoc prompts) |
| **L1** Agent-Assisted | Create BRS → Use AI Tools → Generate MRP |
| **L2** Structured Agentic | Full SASE workflow with all 6 artifacts |
| **L3** Lifecycle Agentic | AI proactively suggests improvements |

**→ See also: [../04-SASE-Artifacts/](../04-SASE-Artifacts/) for templates**

---

## 🎯 10-Stage Lifecycle Coverage

### 10-Stage Lifecycle Coverage (SDLC 6.0.2)

SDLC 6.0.2 has **10 stages (00-09)**. AI tools now cover the complete lifecycle:

| Stage | Name | Files Prefix | Key Automation |
|-------|------|--------------|----------------|
| 00 | FOUNDATION (WHY?) | `design_thinking_*` | User research, problem definition |
| 01 | PLANNING (WHAT?) | `design_thinking_*` | Ideation, requirements synthesis |
| 02 | DESIGN (HOW?) | `design_to_code_*` | Architecture, component design |
| 03 | INTEGRATE | `integration_*` | API contracts, integration tests |
| 04 | BUILD | `code_review_*` | Code generation, review automation |
| 05 | TEST | `testing_*` | Test cases, UAT, **E2E API testing**, security |
| 06 | DEPLOY | `deployment_*` | Checklists, rollback plans, release notes |
| 07 | OPERATE | `operations_*` | Monitoring, incident response, post-mortems |
| 08 | COLLABORATE | `collaboration_*` | Protocols, RACI, documentation |
| 09 | GOVERN | `governance_*` | Compliance checks, audit reports |

> **SDLC 6.0.2**: Files are now prefixed by category (e.g., `design_thinking_empathy-synthesis.md`) instead of being in subfolders. This maintains 2-level maximum folder structure.

### 4-Tier Classification

AI tools scale with your team size:

| Tier | Team Size | Required Tools | Optional Tools |
|------|-----------|----------------|----------------|
| **LITE** | 1-2 | Basic code-review | All others |
| **STANDARD** | 3-10 | + testing, deployment, collaboration | governance |
| **PROFESSIONAL** | 10-50 | + integration, governance | Advanced features |
| **ENTERPRISE** | 50+ | Full suite with audit trails | Custom extensions |

### Industry Standards Integration

| Standard | How Applied | Tools Using |
|----------|-------------|-------------|
| **OWASP ASVS** | Security compliance (L1-L3) | governance/compliance-checker |
| **NIST SSDF** | Secure development | code-review/, testing/ |
| **CMMI v3.0** | Maturity mapping (L1-L5) | governance/audit-report |
| **DORA Metrics** | Performance measurement | operations/, governance/ |
| **Team Topologies** | Team structure | collaboration/ |
| **SAFe 6.0** | Agile at scale | collaboration/, governance/ |
| **ISO 12207** | Process standards | All tools |

---

## 📂 Folder Structure (10-Stage Aligned - SDLC 6.0.2)

```
1-AI-Tools/
├── README.md                    # This file
│
├── design-thinking/             # Stage 00-01 (FOUNDATION → PLANNING)
│   ├── empathy-synthesis.md     # User research synthesis
│   ├── problem-statement.md     # Problem definition generator
│   ├── ideation-facilitator.md  # Solution brainstorming
│   ├── prototype-validator.md   # Rapid prototype validation
│   └── user-testing-analyzer.md # User testing analysis
│
├── design-to-code/              # Stage 02 (DESIGN)
│   └── universal-prompts.md     # Design-to-code automation
│
├── integration/                 # Stage 03 (INTEGRATE)
│   ├── api-contract-designer.md # OpenAPI, GraphQL specs
│   └── integration-test-generator.md # Contract testing
│
├── code-review/                 # Stage 04 (BUILD)
│   ├── tier-1-manual-prompts.md # Manual + AI assistance
│   ├── tier-2-ai-powered.md     # Full AI review
│   └── tier-3-automation.md     # Automated review setup
│
├── testing/                     # Stage 05 (TEST)
│   ├── test-case-generator.md   # Functional/integration tests
│   ├── uat-script-creator.md    # User acceptance testing
│   └── performance-test-analyzer.md # Load/stress testing
│
├── deployment/                  # Stage 06 (DEPLOY)
│   ├── deployment-checklist-generator.md # Pre/post deploy checks
│   ├── rollback-plan-creator.md # Rollback procedures
│   └── release-notes-writer.md  # Release documentation
│
├── operations/                  # Stage 07 (OPERATE)
│   ├── monitoring-setup-helper.md # Dashboards, alerts, SLOs
│   ├── incident-response-guide.md # Incident handling
│   └── post-mortem-analyzer.md  # Blameless post-mortems
│
├── collaboration/               # Stage 08 (COLLABORATE)
│   ├── README.md                # Collaboration tools overview
│   ├── documentation-writer.md  # ADRs, runbooks, guides
│   ├── meeting-summarizer.md    # Standup, planning, retro
│   ├── team-protocol-generator.md # Multi-team protocols
│   └── raci-matrix-generator.md # RACI with validation
│
├── governance/                  # Stage 09 (GOVERN)
│   ├── README.md                # Governance tools overview
│   ├── compliance-checker.md    # SDLC, security, regulatory
│   └── audit-report-generator.md # Compliance audit reports
│
└── platform-examples/           # Real implementations
    ├── bflow-ai-patterns.md     # BFlow Platform patterns
    └── nqh-bot-ai-patterns.md   # NQH-Bot patterns
```

---

## 🚀 Quick Start by Tier

### LITE Tier (1-2 People)

**Required**: Basic code quality
```yaml
Minimum Setup:
  - code-review/tier-1-manual-prompts.md  # AI-assisted review
  - design-to-code/universal-prompts.md   # Design to code

Time Investment: 2 hours
ROI: 10x productivity increase
```

### STANDARD Tier (3-10 People)

**Required**: Core automation
```yaml
Setup:
  Stage 00-01: design-thinking/ (problem validation)
  Stage 03: code-review/tier-2-ai-powered.md
  Stage 04: testing/test-case-generator.md
  Stage 05: deployment/deployment-checklist-generator.md
  Stage 08: collaboration/meeting-summarizer.md

Time Investment: 1 day
ROI: 20x productivity increase
```

### PROFESSIONAL Tier (10-50 People)

**Required**: Full automation + governance
```yaml
Setup:
  All STANDARD tools PLUS:
  Stage 04: testing/uat-script-creator.md, performance-test-analyzer.md
  Stage 06: operations/ (all tools)
  Stage 07: integration/ (all tools)
  Stage 08: collaboration/ (all tools including RACI)
  Stage 09: governance/compliance-checker.md

Time Investment: 1 week
ROI: 30x productivity increase
```

### ENTERPRISE Tier (50+ People)

**Required**: Complete suite with audit trails
```yaml
Setup:
  All PROFESSIONAL tools PLUS:
  Stage 09: governance/audit-report-generator.md
  Custom automation pipelines
  Integration with enterprise tools

Time Investment: 2 weeks
ROI: 50x productivity increase
```

---

## 📊 Time Savings by Stage

| Stage | Tool | Traditional | With AI | Savings |
|-------|------|-------------|---------|---------|
| 00-01 | Design Thinking | 26 hours | 1 hour | **96%** |
| 02 | Design-to-Code | 2-4 hours | 5-10 min | **95%** |
| 03 | Code Review | 30 min/PR | 10 min/PR | **67%** |
| 04 | Test Cases | 8 hours | 45 min | **90%** |
| 04 | UAT Scripts | 4 hours | 36 min | **85%** |
| 04 | Performance Analysis | 6 hours | 1.2 hours | **80%** |
| **05** | **E2E API Testing** | **3 hours** | **30 min** | **83%** ⭐ NEW |
| **05** | **OWASP Security Check** | **4 hours** | **45 min** | **81%** ⭐ NEW |
| 05 | Deployment Checklist | 4 hours | 36 min | **85%** |
| 06 | Monitoring Setup | 8 hours | 1.2 hours | **85%** |
| 06 | Post-Mortem | 4 hours | 24 min | **90%** |
| 07 | API Contracts | 6 hours | 54 min | **85%** |
| 08 | Documentation | 4 hours | 24 min | **90%** |
| 08 | Meeting Summaries | 30 min | 2 min | **95%** |
| 09 | Compliance Check | 8 hours | 24 min | **95%** |
| 09 | Audit Reports | 2 days | 2 hours | **85%** |

**Total Annual Savings**: $199,000 - $206,000 per team

---

## 🎯 Stage-by-Stage AI Patterns

### Stage 00-01: Design Thinking (WHY? → WHAT?)

**Purpose**: Validate problems before building solutions

```
AI Prompt Pattern:
"Synthesize user research for [feature]:
- Interviews: [count] users
- Pain points: [list]
- Desired outcomes: [list]

Generate:
✅ Empathy map
✅ Problem statement
✅ 15+ solution ideas (ranked)
✅ Validation criteria

Target: 75-90% user adoption (vs 30% without DT)"
```

**Tools**: `design-thinking/*.md`
**BFlow Result**: 96% time savings, 75%+ feature adoption

---

### Stage 02: Architecture (HOW?)

**Purpose**: Convert designs to production code

```
AI Prompt Pattern:
"Convert [design tool] design to [framework]:
- Design: [URL/screenshot]
- Component: [name]
- Requirements:
  ✅ Zero Mock Policy (real implementations)
  ✅ Tests included (80%+ coverage)
  ✅ Performance (<50ms)
  ✅ Accessibility (WCAG 2.1 AA)"
```

**Tools**: `design-to-code/*.md`
**BFlow Result**: 95% time savings, consistent quality

---

### Stage 04: Development (BUILD)

**Purpose**: Ensure code quality before merge

```
AI Prompt Pattern:
"Review code for SDLC 6.0.2:
[paste code]

Check:
✅ 6 Pillars compliance
✅ Security (OWASP Top 10)
✅ Performance (<50ms target)
✅ Test coverage (80%+)
✅ Documentation

Score: X/100 with specific fixes"
```

**Tools**: `code-review/*.md`
**BFlow Result**: 67-93% review time savings

---

### Stage 05: Quality (TEST)

**Purpose**: Comprehensive testing automation

```
AI Prompt Pattern:
"Generate test cases for [feature]:
- Functional (happy paths, edge cases)
- Integration (API contracts)
- Performance (load targets)

Zero Mock Policy: Real data only
Coverage Target: 95%+
Output: pytest/jest format"
```

**Tools**: `testing_*.md`
**BFlow Result**: 150+ tests in 45 min, 98% pass rate

#### NEW in 6.0.2: E2E API Testing Workflow

```
AI Prompt Pattern (e2e-api-testing skill):
"/e2e-api-testing --openapi docs/03-Integration-APIs/openapi.json

6-Phase Workflow:
✅ Phase 1: API Discovery (parse OpenAPI)
✅ Phase 2: Test Configuration (env, auth)
✅ Phase 3: Test Execution (all endpoints)
✅ Phase 4: Security Testing (OWASP Top 10)
✅ Phase 5: Report Generation (markdown)
✅ Phase 6: CI/CD Integration

Target: 80%+ pass rate, <30 min setup"
```

**Tools**: `testing_e2e-api-testing-workflow.md`, `testing_security-testing-checklist.md`
**SOP Generator Result**: 58 endpoints, 84.5% pass rate, 83% time savings

---

### Stage 05: Release (DEPLOY)

**Purpose**: Zero-downtime deployments

```
AI Prompt Pattern:
"Generate deployment checklist:
- Environment: [staging/production]
- Strategy: [blue-green/canary]
- Rollback: <5 min target

Include:
✅ Pre-deployment checks
✅ Deployment steps
✅ Post-deployment validation
✅ Rollback procedure"
```

**Tools**: `deployment/*.md`
**BFlow Result**: Zero downtime, 10+ successful deploys

---

### Stage 06: Production (OPERATE)

**Purpose**: Reliable operations with fast recovery

```
AI Prompt Pattern:
"Generate monitoring setup:
- SLOs: 99.9% uptime, <50ms API, <0.1% errors
- Dashboards: CEO/CTO visibility
- Alerts: PagerDuty/Slack
- On-call rotation"
```

**Tools**: `operations/*.md`
**BFlow Result**: 99.95% uptime, proactive alerting

---

### Stage 03: Integration (INTEGRATE)

**Purpose**: Seamless system connections

```
AI Prompt Pattern:
"Generate API contract (OpenAPI 3.0):
- Endpoints: [list]
- Auth: OAuth2/JWT
- Rate limits: [X req/min]
- Contract tests included"
```

**Tools**: `integration/*.md`
**BFlow Result**: 120+ contract tests, 98% pass rate

---

### Stage 08: Teams (COLLABORATE)

**Purpose**: Effective multi-team coordination

```
AI Prompt Pattern:
"Generate team protocol:
- Teams: [list with sizes]
- Work model: [remote/hybrid]
- Include:
  ✅ Communication channels + SLAs
  ✅ RACI matrix (single-A validated)
  ✅ Escalation paths (4 levels)
  ✅ Handoff procedures"
```

**Tools**: `collaboration/*.md`
**BFlow Result**: 50% fewer "who decides?" questions

---

### Stage 09: Compliance (GOVERN)

**Purpose**: Automated compliance assurance

```
AI Prompt Pattern:
"Check compliance for [project]:
- Tier: [LITE/STANDARD/PROFESSIONAL/ENTERPRISE]
- Standards: SDLC 6.0.2, OWASP ASVS L[1-3]

Check:
✅ 10-stage structure
✅ Documentation standards
✅ Security baseline
✅ Team collaboration protocols

Output: Score + violations + auto-fix commands"
```

**Tools**: `governance/*.md`
**BFlow Result**: Zero compliance surprises, <5 min detection

---

## 🏆 Proven Results

### BFlow Platform
- **Design Thinking**: 96% time savings (26h → 1h)
- **Test Generation**: 150+ cases in 45 min
- **Compliance**: 100% Vietnamese regulations
- **Operations**: 99.95% uptime

### NQH-Bot
- **Feature Adoption**: 30% → 75%+ with DT
- **Code Quality**: Zero critical bugs
- **Team Coordination**: 50% fewer conflicts

### MTEP
- **Onboarding**: <30 min time to value
- **Documentation**: 150+ pages maintained
- **Compliance**: SOC 2 ready

---

## 📚 Documentation

### Core References
- [SDLC-Core-Methodology.md](../../02-Core-Methodology/SDLC-Core-Methodology.md) - 10-stage lifecycle
- [Team-Collaboration Standards](../../02-Core-Methodology/Documentation-Standards/Team-Collaboration/) - Collaboration protocols
- [sdlc_validator.py](../07-Scripts/compliance/sdlc_validator.py) - Compliance automation

### Stage-Specific Guides
- **Stage 00-01**: [design-thinking/](./design-thinking/)
- **Stage 02**: [design-to-code/](./design-to-code/)
- **Stage 03**: [code-review/](./code-review/)
- **Stage 04**: [testing/](./testing/)
- **Stage 05**: [deployment/](./deployment/)
- **Stage 06**: [operations/](./operations/)
- **Stage 07**: [integration/](./integration/)
- **Stage 08**: [collaboration/](./collaboration/)
- **Stage 09**: [governance/](./governance/)

---

## ✅ Success Metrics

| Metric | Target | Achieved |
|--------|--------|----------|
| Time savings (average) | 80%+ | **90%** |
| Test coverage | 80%+ | **87%** |
| Feature adoption | 70%+ | **75%+** |
| Compliance score | 95%+ | **100%** |
| Zero downtime deploys | 100% | **100%** |
| Audit readiness | Always | **Validated** |

---

**Folder Status**: ACTIVE - SDLC 6.0.2 Complete
**Last Updated**: February 2, 2026
**Owner**: CPO Office

***"AI automation for every stage of the lifecycle."*** 🚀

**AI Governance**: All tools align with [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) principles.

**E2E Testing**: See [E2E-TESTING-QUICKSTART.md](../../07-Implementation-Guides/E2E-TESTING-QUICKSTART.md) for quick start guide.

**Legacy/Archive Policy**: Content in 99-legacy and 10-archive folders is never validated or upgraded.
