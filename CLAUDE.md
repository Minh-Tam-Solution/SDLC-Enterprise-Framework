# CLAUDE.md - AI Assistant Guidelines for SDLC 6.3.1

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

The **SDLC-Enterprise-Framework** is a universal, battle-tested AI+Human development framework (**v6.3.1**) featuring the **7-Pillar Architecture + Section 7 (Quality Assurance) + Section 8 (Unified Specification Standard)** with complete 10-Stage lifecycle (WHY → GOVERN), **8 Mental Models**, **Lean Ring 1 Consolidation**, **Long-Running Agent Protocol**, SASE/SE 3.0 Integration, Agentic Maturity Model, and 4-Tier Classification system. Built through 10 months of real platform development (June 2025 - April 2026) across BFlow, NQH-Bot, and MTEP platforms, this framework is **tool-agnostic** — any platform can implement it.

**What's New in 6.3.1 (April 17, 2026) — AGENT CONTINUITY RUNTIME GUIDANCE + GOVERNANCE TRAINING EXPANSION**:

*Agent Continuity Runtime Guidance*:
- ✅ **New SASE Artifact** - `05-Templates-Tools/04-SASE-Artifacts/Agent-Continuity-Runtime-Guidance.md`
- ✅ **SHOULD recommendation** for runtime implementors closing the Agent Continuity gap (MM #7)
- ✅ **Origin**: MTClaw field report 2026-04-17; SDLC Orchestrator Sprint 59 adopted the pattern
- ✅ **Implementation-plurality** preserved per CPO Condition 1 — Layer 1.25 injection is ONE valid pattern
- ✅ **AGENTS-MD-Template** now cross-references the new guidance doc

*Governance Training Expansion*:
- ✅ **4 New Training Modules (08-11)** - Total program: 11 modules, 39h instruction (was 7 modules, 32h)
- ✅ **Module 08: Authority & Decision Governance** (2h) - Role boundaries, decision matrix, escalation protocol
- ✅ **Module 09: Quality Gate Workshop** (2h) - Hands-on G0-G4 evaluation on SDLC Orchestrator
- ✅ **Module 10: ADR & Sprint Plan Workflow** (2h) - When to write ADR, sprint enforcement rules
- ✅ **Module 11: Remote Team Governance** (1h) - Async rules, Collaborator vs Fork workflow
- ✅ **80 quiz questions** - 20 per module, multiple choice + scenario-based
- ✅ **Real-world incidents** - Modules derived from actual governance violations (genericized)

**What's New in 6.3.0 (March 29, 2026) - METHODOLOGY UPGRADE + CSO**:
- ✅ **Fix-First Review Protocol** - AUTO-FIX vs ASK classification for every review finding (Section 6.3, Quality Gates doc)
- ✅ **Effort Compression Table** - AI vs human time ratios (100x→6x) for gate evaluation decisions (System Thinking doc)
- ✅ **Scope Drift Detection** - CLEAN/SCOPE_CREEP/MISSING checklist at G3+G-Sprint-Close (new checklist)
- ✅ **Three-Tier Testing** - Static (free) → Integration (CI) → AI Eval ($$$), diff-based selection (Part 13)
- ✅ **Doc Staleness Detection** - Cross-ref diff vs .md files, FRESH/STALE/UNRELATED (Part 14)
- ✅ **Terminal Status Taxonomy** - DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT with required metadata (Section 8, Agentic Principles)
- ✅ **SOUL-cso** - Chief Security Officer role (SE4H advisor, PRO+ tier). OWASP ASVS L2, AGPL containment, threat modeling
- ✅ **18 SOUL templates** - SASE 13-role model (was 12). 4 SE4H advisors (was 3). Tier matrix: PRO(11), ENTERPRISE(14)
- ✅ **4 TEAM charter updates** - @cso integrated into Executive, Design, QA, Ops teams

**What's New in 6.3.0 (March 18, 2026) - AGENTIC SDLC + LEAN RING 1**:
- ✅ **Lean Ring 1** - 41→30 substantive files, 584→463KB (-21%). 5 docs merged into 2, 9 moved to Ring 2
- ✅ **Mental Model #7** - "Agent Continuity" — agents maintain context across sessions
- ✅ **Mental Model #8** - "More People Build, Under Guardrails" — domain experts build within boundaries
- ✅ **Long-Running Agent Protocol** - Checkpoint, memory, handoff, human checkpoints, traceability (Ring 1)
- ✅ **Citizen Developer Guide** - 30-min pathway for non-technical users (Ring 3)
- ✅ **ROI Calculator** - Agent ROI formula, output volume metrics, productivity paradox (Ring 2)
- ✅ **Tool-Agnostic** - 42 product-specific references sanitized. 0 tool-specific language in Ring 1
- ✅ **Evidence base** - Anthropic 2026 Trends, NIST emerging, Singapore MGF, Context Engineering Guide

**What's in 6.1.2 (March 9, 2026) - SOULs + TEAMs TEMPLATES**:
- ✅ **17 SOUL role templates** (now 18 with SOUL-cso in 6.3.0) - SASE 12-role model personas added to Ring 2 (`04-SASE-Artifacts/souls/`)
- ✅ **10 TEAM charters** - 7 SDLC function teams + 3 organizational teams (`04-SASE-Artifacts/teams/`)
- ✅ **Tier Availability Matrix** - LITE(3) → STANDARD(6) → PRO(10) → ENTERPRISE(13) → OPTIONAL(17)
- ✅ **Hybrid sourcing** - EndiorBot (12 SOULs + 7 TEAMs) + MTClaw (5 SOULs + 3 TEAMs), best-of-breed per role
- ✅ **Vendor-neutral templates** - All project-specific references sanitized to `{PROJECT_NAME}`, `{AI_PROVIDER}`

**What's New in 6.1.1 (February 21, 2026) - POST-CLEANUP PATCH**:
- ✅ **"AI Council" → "Senior Review Board"** - Tool-agnostic terminology in 5 active docs
- ✅ **36 FROZEN templates archived** - Sprint 173 AI prompt templates → `10-archive/05-Legacy/`
- ✅ **Conversation-First Governance (#15)** - New methodology doc for OTT/CLI-first governance
- ✅ **Tool profile disclaimers** - All profiles marked REFERENCE PROFILE with independence note
- ✅ **AI Governance README gap fixed** - Docs #12-#15 now listed in table

**What's New in 6.1.0 (February 18, 2026) - CONSOLIDATION RELEASE**:
- ✅ **Ring 1 Monolith Slim** - Design Thinking 2,018→364 lines, Agentic Principles 1,313→293 lines
- ✅ **Agentic Docs → 03-AI-GOVERNANCE** - Moved Agentic Core Principles (#13) + Maturity Model (#14) to correct ring
- ✅ **Multi-Agent Patterns** - New doc #12 with 10 collaboration patterns (lane queues, failover, snapshots)
- ✅ **System Thinking Foundation** - Dedicated doc for core concept (since SDLC 4.0): 4-Layer Iceberg, 6 Mental Models
- ✅ **Crisis-to-Pattern Methodology** - Extracted from Design Thinking as dedicated doc (formalizes Mental Model #5)
- ✅ **Design Thinking Templates** - 9 templates extracted to Documentation-Standards
- ✅ **BRS/MTS/LPS → AGENTS.md** - Terminology cleanup across SASE templates + Maturity Model
- ✅ **Version Alignment** - 636 stale version refs updated to 6.1.0

**What's New in 6.0.6 (February 16, 2026) - MINOR RELEASE**:
- ✅ **CLAUDE.md Standard** - 3-tier structure (LITE/PRO/ENTERPRISE) with validation criteria
- ✅ **Autonomous Codegen Patterns** - Two-agent pattern + 4-Gate Quality Pipeline methodology
- ✅ **MRP Template** - 5-section Merge-Readiness Package for Gate G4
- ✅ **Anthropic Best Practices Integration** - Source: 10 teams, 5 quickstarts analysis

**What's New in 6.0.5 (February 15, 2026) - MINOR RELEASE**:
- ✅ **RFC-001 Legacy Document Organization** - Centralized archive standard
- ✅ **Anti-Vibecoding Alignment** - SPEC-0001 updated with Quality Assurance System

**What's New in 6.0.4 (February 8, 2026) - MINOR RELEASE**:
- ✅ **TDD Workflow Integration** - 3-Phase Sprint Enhancement with Spec Converter (SpecIR)
- ✅ **Tier-Aware TDD Coverage** - Coverage targets per classification tier

**What's New in 6.0.3 (February 2, 2026) - MINOR RELEASE**:
- ✅ **Boris Cherny Best Practices Consolidation** - 3-Circle Architecture (Core → Governance → Outer Ring)
- ✅ **Visual Documentation Standards** - Diagram conventions and tooling

**What's New in 6.0.2 (February 2, 2026) - MINOR RELEASE (RFC-SDLC-602)**:
- ✅ **E2E API Testing Workflow** - 6-phase standardized testing workflow with Stage 03 ↔ 05 cross-reference
- ✅ **OWASP API Top 10 Checklist** - Complete API security testing coverage (2023 edition)
- ✅ **Testing Artifacts Structure** - SDLC-compliant folder layout for test outputs
- ✅ **sdlcctl E2E Commands** - `sdlcctl e2e validate`, `sdlcctl e2e cross-reference`, `sdlcctl e2e generate-report`
- ✅ **OPA Policy Integration** - e2e_testing_compliance, stage_cross_reference policies
- ✅ **4 New Evidence Types** - e2e_test_report, security_test_report, api_coverage_report, cross_reference_validation

**What's New in 6.0.1 (February 1, 2026) - MINOR RELEASE (SPEC-0021)**:
- ✅ **Stage Consistency Validation** - 4-stage consistency validation workflow (PLANNING ↔ DESIGN ↔ INTEGRATE ↔ BUILD)
- ✅ **Pre/Post-Implementation Checklists** - Actionable checklists for stage transitions
- ✅ **Artifact Integrity Hashing** - SHA256 checksums for post-approval modification detection
- ✅ **CLI Validation Commands** - `sdlcctl validate-consistency` for automated checking

**What's New in 6.0.0 (January 28, 2026) - MAJOR RELEASE**:
- ✅ **Unified Specification Standard (Section 8)** - YAML frontmatter required, BDD requirements format
- ✅ **DESIGN_DECISIONS.md Template** - Lightweight ADR alternative for sprint-scoped decisions
- ✅ **SPEC_DELTA.md Template** - Version change tracking with breaking change documentation
- ✅ **Context Authority Methodology** - Dynamic AGENTS.md with 4 zones (Static → Ephemeral)
- ✅ **OpenSpec Alignment** - Industry-standard spec-driven development compatibility
- ✅ **20 Priority Spec Migration** - Structured migration plan for existing specifications
- ✅ **CONVERSION-LAYER-SPECIFICATION** - Technical spec for `sdlcctl spec convert` command

**Breaking Changes in 6.0.0**:
- ⚠️ All new specs MUST use YAML frontmatter (`spec_id`, `tier`, `stage`, `status`)
- ⚠️ Requirements MUST use BDD format (GIVEN-WHEN-THEN)
- ⚠️ Tier declaration REQUIRED for all specifications

**What's in 5.3.0 (January 2026) - ARCHIVED**:
- ✅ **Stage Dependency Matrix** - Explicit stage prerequisites, parallel execution rules, early start triggers
- ✅ **Stage Exit Criteria** - Documentation, evidence, artifact integrity requirements per tier (LITE/PRO/ENTERPRISE)
- ✅ **Sprint-Stage Integration** - Multi-stage sprint handling, G-Sprint gate integration with stage validation
- ✅ **Quality Assurance System (Section 7)** - Anti-Vibecoding governance with Vibecoding Index (0-100)
- ✅ **Progressive Routing** - Auto-approve Green (0-30) → CEO mandatory Red (81-100)
- ✅ **Auto-Generation Layer** - Intent, Ownership, Context, Attestation generators (<5 min compliance)
- ✅ **Kill Switch Criteria** - Auto-rollback on rejection >80%, latency >500ms, false positives >20%
- ✅ **Tier-Specific Stage Requirements** - Decision trees for LITE/PRO/ENTERPRISE stage skipping
- ✅ **Stage Transition Checklists** - Actionable checklists for all 9 stage transitions

**What's in 5.2.0 (January 2026)**:
- ✅ **AI Governance Principles** - 7 timeless principles for AI+Human collaboration
- ✅ **Risk-Based Planning Mode** - Planning triggered by risk factors, not LOC count
- ✅ **Concentric Circles Model** - Core (timeless) → Governance (stable) → Outer Ring (tools)
- ✅ **AI Agent Best Practices 2026** - Complete orchestration guide

**What's in 5.1.3 (January 2026)**:
- ✅ **7-Pillar Architecture** - Complete framework structure with Sprint Planning Governance as Pillar 2
- ✅ **Sprint Planning Governance (Pillar 2)** - G-Sprint/G-Sprint-Close gates, Planning Hierarchy (ROADMAP → PHASE → SPRINT → BACKLOG)
- ✅ **10 Golden Rules** - Sprint governance principles for consistent execution
- ✅ **Dual-Track Quality Gates** - Feature Gate (G0-G4) + Sprint Gate (G-Sprint/G-Sprint-Close)
- ✅ **24h Documentation Enforcement** - Sprint-related docs within 24 hours of completion
- ✅ **Code Review Sprint Integration** - 4-Layer system with Sprint Context Check
- ✅ **AI Agent Best Practices (2026)** - Planning Mode, Model Selection Matrix, Sub-agents Guidelines
- ✅ **Planning Sub-agent Orchestration** - Expert workflow alignment for AI-assisted development

**What's in 5.1.2 (December 24, 2025)**:
- ✅ **Project Structure Standard** - Clear separation between documentation stage mapping and code folder organization
- ✅ **Documentation-Only Stage Mapping** - Only `/docs` folders are mapped to SDLC stages (00-09)
- ✅ **Code Folders Are NOT Stage-Mapped** - `backend/`, `frontend/`, `tools/`, `tests/` are organizational units

**What's in 5.1.1 (December 12, 2025)**:
- ✅ **Legacy/Archive Folder Skip** - Validators skip 99-legacy and 10-archive folders
- ✅ **Stage Consistency** - INTEGRATE is Stage 03, all 10 stages: 00-09
- ✅ **Version Consistency** - Framework-wide 5.1.1 alignment

**What's New in 5.1.0 (December 11, 2025)**:
- ✅ **SASE Framework Integration** - SE 3.0 (arXiv:2509.06216v2), 6 SASE Artifact Templates
- ✅ **SE4H vs SE4A Distinction** - Agent Coach (Human) vs Agent Executor (AI) roles
- ✅ **Agentic Maturity Model** - 4 Levels (L0 Tool-Assisted → L3 Lifecycle Agentic)
- ✅ **7 Agentic Principles** - Brief-First, Evidence-Based MRP, Human Accountability, etc.
- ✅ **ACE/AEE Architecture** - Agent Command Environment + Agent Execution Environment

**What's in 5.0.0 (December 5, 2025)**:
- ✅ **Governance & Compliance Standards** - Quality Gates, Security Gates, Observability, Change Management
- ✅ **4-Tier Classification** - LITE (1-2), STANDARD (3-10), PROFESSIONAL (10-50), ENTERPRISE (50+)
- ✅ **Industry Best Practices** - CMMI v3.0, SAFe 6.0, DORA Metrics, OWASP ASVS, NIST SSDF

**What's in SDLC 4.9.1 (November 29, 2025)**:
- ✅ **Code File Naming Standards** - Python: snake_case, TypeScript: camelCase, React: PascalCase

**What's in SDLC 4.9 (November 13, 2025)**:
- ✅ **Complete 10-Stage Lifecycle** - WHY → WHAT → HOW → BUILD → TEST → DEPLOY → OPERATE → INTEGRATE → COLLABORATE → GOVERN
- ✅ **Perfect /docs Alignment** - 10 SDLC stages → 10 /docs folders (00-09)
- ✅ **BFlow 52-Day Journey** - Flagship validation (ROI metrics deferred to post-GA measurement)

## Key Framework Concepts

### The Complete 10-Stage Lifecycle (Documentation Only - SDLC 5.1.3)

**IMPORTANT**: Stage mapping applies ONLY to `/docs` folders. Code folders (`backend/`, `frontend/`, etc.) are NOT stage-mapped.

```yaml
Business Question → SDLC Stage → /docs Folder (5.1.3)
WHY?        → Stage 00: Foundation    → docs/00-foundation/
WHAT?       → Stage 01: Planning      → docs/01-planning/
HOW?        → Stage 02: Design        → docs/02-design/
INTEGRATE   → Stage 03: Integration   → docs/03-integrate/
BUILD       → Stage 04: Development   → docs/04-build/
TEST        → Stage 05: Quality       → docs/05-test/
DEPLOY      → Stage 06: Deployment    → docs/06-deploy/
OPERATE     → Stage 07: Operations    → docs/07-operate/
COLLABORATE → Stage 08: Team Mgmt     → docs/08-collaborate/
GOVERN      → Stage 09: Governance    → docs/09-govern/
ARCHIVE     → (Not a stage)           → docs/10-archive/  # Project-level archive
```

### Code Folder Organization (NOT Stage-Mapped)

```yaml
Code folders are organizational units, NOT lifecycle stages:
  backend/       # Server-side code (Python, Go, Java, etc.)
  frontend/      # Client-side code (React, Vue, Angular, etc.)
  tools/         # Utility scripts, CLI tools
  tests/         # Test suites (unit, integration, e2e)
  mobile/        # Mobile app code (optional)
  infra/         # Infrastructure as Code (optional)
```

See [SDLC-Project-Structure-Standard.md](02-Core-Methodology/Documentation-Standards/SDLC-Project-Structure-Standard.md) for complete specification.

### Code File Naming Standards (NEW in 4.9.1)

```yaml
Python Files:
  Format: snake_case
  Max Length: 50 characters
  Examples: user_service.py, invoice_repository.py

TypeScript Files:
  Format: camelCase
  Max Length: 50 characters
  Examples: arService.ts, paymentSlice.ts

React Components:
  Format: PascalCase
  Max Length: 50 characters
  Examples: ARDashboard.tsx, InvoiceList.tsx

Documentation Files:
  Format: kebab-case
  No version in filename
  Examples: SDLC-Core-Methodology.md
```

### The 7-Pillar Architecture + Section 7 (SDLC 5.3.0)

**Pillar 0: Design Thinking Foundation**
- Stanford d.school 5-phase methodology (Empathize, Define, Ideate, Prototype, Test)
- System Thinking integration (4-layer Iceberg Model)
- 96% time savings proven (NQH-Bot: 4 weeks vs 6 months)

**Pillar 1: 10-Stage Lifecycle (Enhanced in 5.3.0)**
- Complete lifecycle: WHY → GOVERN (Stages 00-09)
- **Explicit Stage Dependencies** - Prerequisites, parallel rules, early start triggers
- **Stage Exit Criteria** - Documentation, evidence, signoff per tier
- Archive management (10-archive/{NN}-Legacy per RFC-001)

**Pillar 2: Sprint Planning Governance (5.1.3)**
- Sprint Planning Hierarchy: ROADMAP → PHASE → SPRINT → BACKLOG
- G-Sprint/G-Sprint-Close gates
- **Sprint-Stage Integration** (5.3.0) - Multi-stage sprint handling
- 10 Golden Rules for sprint execution
- 24h documentation enforcement

**Pillar 3: 4-Tier Classification (Enhanced in 5.3.0)**
- LITE (1-2), STANDARD (3-10), PROFESSIONAL (10-50), ENTERPRISE (50+)
- **Tier-Specific Stage Requirements** - Decision trees for stage skipping
- Scalable documentation requirements

**Pillar 4: Quality Gates (Dual-Track)**
- Feature Gates: G0 → G1 → G2 → G3 → G4
- Sprint Gates: G-Sprint → G-Sprint-Close
- **Stage Transition Checklists** (5.3.0) - Actionable checklists for 9 transitions
- Zero Mock Policy (679 mocks → 0 in 48 hours)
- 90%+ test coverage with real services

**Pillar 5: SASE Integration**
- SE 3.0 (arXiv:2509.06216v2) principles
- SASE Artifacts: CRP, MRP, VCR, AGENTS.md _(BRS/LPS/MTS deprecated)_
- SE4H vs SE4A roles
- Agentic Maturity Levels (L0-L3)

**Pillar 6: Documentation Permanence**
- 919 files standardized (NQH-Bot)
- Document naming standards (no sprint references)
- Archive management (10-archive/{NN}-Legacy)

**Section 7: Quality Assurance System (NEW in 5.3.0)**
- **Vibecoding Index** (0-100) - 5 weighted signals:
  - Architectural Smell (25%): God class, feature envy, shotgun surgery
  - Abstraction Complexity (15%): Deep inheritance, interface proliferation
  - AI Dependency Ratio (20%): AI lines / total lines
  - Change Surface Area (20%): Files, modules, API contracts touched
  - Drift Velocity (20%): New patterns, naming violations
- **Progressive Routing**:
  - Green (0-30): Auto-approve
  - Yellow (31-60): Tech Lead review
  - Orange (61-80): CEO optional
  - Red (81-100): CEO mandatory
- **Auto-Generation Layer** - 4 generators: Intent, Ownership, Context, Attestation
- **Kill Switch** - Auto-rollback on rejection >80%, latency >500ms, false positives >20%
- **Governance Modes** - OFF/WARNING/SOFT/FULL

## AI Agent Best Practices (2026)

Based on expert AI coding workflow analysis (January 2026), these practices maximize AI-assisted development effectiveness.

### Planning Mode (RISK-BASED - Updated in 5.2.0)

```yaml
When to Use Planning Mode (MANDATORY - Risk-Based):
  - Data schema / API contracts (breaking changes)
  - Authentication / Authorization (security-critical)
  - Cross-service boundaries (coordination complexity)
  - Concurrency / Race conditions (hard to test)
  - Security-sensitive code (vulnerabilities)
  - Public API interfaces (external impact)
  - Payment / Financial logic (money involved)

When to Use Planning Mode (RECOMMENDED):
  - >50 LOC changes (not hard rule, use judgment)
  - >3 files affected
  - Unfamiliar code area
  - Complex business logic

Planning Mode Workflow:
  1. EXPLORE → Search similar implementations (agentic grep > RAG)
  2. SYNTHESIZE → Build implementation plan from extracted patterns
  3. APPROVE → Present to human for validation
  4. EXECUTE → Generate code following approved plan

Key Insight (5.2.0):
  "Planning is RISK-BASED, not LOC-based"
  - Simple rename across 50 files? Maybe skip planning.
  - Touches auth even 5 lines? PLAN.
  - Intent-based, not size-based.
```

### Model Selection Matrix

```yaml
Task-Type Model Routing (2026):

  Large Features (>50 LOC, multi-file):
    Primary: Claude Opus 4.5 (70% of work)
    Reason: Best at complex reasoning, multi-file refactoring

  Small Fixes (<15 LOC, single file):
    Primary: Claude Sonnet 4.5
    Reason: Fast, accurate for targeted changes

  Architecture & Debugging:
    Primary: GPT 5.2 (when stuck)
    Reason: Strong reasoning, different perspective helps

  Design & Creativity:
    Primary: Gemini 3 Pro
    Reason: Large context, creative solutions

  Quick Answers & Micro-edits:
    Primary: Claude Haiku 4.5
    Reason: Fastest response time

Expert Rule:
  "Switch models when stuck - different model = different perspective"
```

### Sub-agents Usage Guidelines

```yaml
When to Use Sub-agents:
  ✅ Research and exploration (isolated context)
  ✅ Pattern extraction before implementation
  ✅ Parallel information gathering
  ✅ ADR and convention review

When to AVOID Sub-agents:
  ❌ Parallel editing in same project (coordination issues)
  ❌ Tightly coupled operations
  ❌ Sequential dependencies

Session Management:
  - Fork sessions to learn without polluting main context
  - Use Explore sub-agents for pattern discovery
  - Keep main session clean for implementation
```

### Developer Role Evolution (Software 3.0)

```yaml
2026 Developer Responsibilities:
  ✅ Design feedback loops (not write code)
  ✅ Monitor agent work quality
  ✅ Identify patterns and update context files
  ✅ Make high-level architecture decisions
  ✅ Update AGENTS.md/CLAUDE.md with learnings
  ✅ Configure tools/skills/MCP servers

Key Shift:
  "Developer role = Design feedback loops, NOT write code"
  - Review AI output for patterns and anti-patterns
  - Update context files to improve future generations
  - Make architectural decisions AI cannot make alone
```

### Specification Generation Workflow

```yaml
Expert Specification Process:
  1. Reference Collection
     - Screenshot/record similar features
     - Gather existing code patterns
     - Review related ADRs

  2. PRD Synthesis (Gemini 3 Pro)
     - Large context for synthesis
     - Input reference materials
     - Output structured PRD draft

  3. Interactive Refinement (Claude)
     - "Interview mode" with ask_user_question
     - Clarify ambiguities iteratively
     - Produce refined specification

  4. Dependency Discovery (ChatGPT + Search)
     - Find recommended packages
     - Check compatibility with tech stack
     - Validate library choices
```

### Feedback Loop Closure

```yaml
Learning from Code Reviews:
  1. Extract patterns from PR review comments
  2. Categorize: pattern_violation | missing_requirement | edge_case | performance
  3. Store learnings for future reference
  4. Monthly: Aggregate → Update decomposition hints
  5. Quarterly: Synthesize → Update CLAUDE.md patterns

Continuous Improvement:
  - Track recurring review comments
  - Update context files with lessons learned
  - Improve future AI generations automatically
```

## Repository Structure

### Core Documentation Structure (SDLC 6.1.0)
```
SDLC-Orchestrator/SDLC-Enterprise-Framework/
├── README.md                      # Main framework documentation
├── CHANGELOG.md                   # Complete version history
├── CLAUDE.md                      # This file - AI assistant guidelines
├── CONTENT-MAP.md                 # Topic → canonical file mapping
├── DEPRECATION-POLICY.md          # Redirect rules
│
├── 01-Overview/                   # Strategic overview
│   └── SDLC-Executive-Summary.md  # Complete 10-stage overview
│
├── 02-Core-Methodology/           # Core principles (Ring 1 — Lean in 6.3.0)
│   ├── SDLC-Core-Methodology.md           # Hub: 7-Pillar + 10-Stage
│   ├── SDLC-Design-Thinking-Principles.md # Pillar 0 (slim, 364 lines)
│   ├── SDLC-System-Thinking-Foundation.md # Pillar 0 (8 Mental Models, 6.3.0)
│   ├── SDLC-Crisis-To-Pattern-Methodology.md # Pillar 0 (MM #5)
│   ├── SDLC-Stage-Lifecycle-Framework.md  # CONSOLIDATED 6.3.0 (Deps+Exit+Tier)
│   ├── SDLC-Context-Authority-Methodology.md # Section 8
│   ├── SDLC-SSOT-Principle.md
│   ├── Documentation-Standards/
│   │   ├── SDLC-Naming-Standards.md
│   │   ├── SDLC-Project-Structure-Standard.md
│   │   ├── SDLC-Sprint-Planning-Guide.md
│   │   └── SDLC-Legacy-Document-Organization.md
│   └── Governance-Compliance/
│       ├── SDLC-Sprint-Governance.md      # Pillar 2
│       └── SDLC-Quality-Gates-Assurance-Framework.md # CONSOLIDATED 6.3.0
│
├── 03-AI-GOVERNANCE/              # AI Governance Principles (Ring 1 — timeless)
│   ├── 01 to 09: Core AI Governance Principles
│   ├── 13-AGENTIC-CORE-PRINCIPLES.md    # SASE SE4H/SE4A
│   ├── 14-AGENTIC-MATURITY-MODEL.md     # L0-L3
│   ├── 16-LONG-RUNNING-AGENT-PROTOCOL.md # NEW 6.3.0
│   └── 10/11/12/15: redirect stubs → Ring 2 (expire Sep 2026)
│
├── 04-AI-TOOLS-LANDSCAPE/        # AI Tools (Ring 2)
│   ├── tool-profiles/             # Claude, Cursor, Copilot
│   ├── best-practices-2026/       # 8 best practice guides
│   └── integration-guides/        # MCP integration
│
├── 05-Templates-Tools/            # Templates (Ring 2)
│   ├── 01-Specification-Standard/ # YAML + BDD specs
│   ├── 02-AI-Tools/               # AI prompts by stage
│   ├── 04-SASE-Artifacts/         # AGENTS.md, CRP, MRP, VCR
│   │   ├── souls/                 # NEW 6.1.2: 17 SOUL role templates
│   │   └── teams/                 # NEW 6.1.2: 10 TEAM charters
│   ├── 05-Checklists/             # Stage transition checklists
│   ├── 06-Manual-Templates/       # Design Thinking + MRP templates
│   └── 08-Project-Templates/      # Planning hierarchy templates
│
├── 06-Case-Studies/               # Case studies (Ring 2)
├── 07-Implementation-Guides/      # Guides (Ring 3)
│   ├── E2E-TESTING-QUICKSTART.md  # MOVED 6.1.0
│   ├── SDLC-E2E-API-Testing-Methodology.md # MOVED 6.1.0
│   └── ... (code review, deployment, etc.)
├── 08-Training-Materials/         # Training (Ring 3)
├── 09-Continuous-Improvement/     # RFCs + improvement (Ring 3)
│
└── 10-archive/                    # Centralized legacy archive
    └── {NN}-Legacy/               # Stage-aligned archives
```

## Development Workflow

### When Working with Framework Documentation
1. **Check current version**: Framework is at **SDLC 6.1.0** (February 2026)
2. **Apply 7-Pillar Architecture**: Design Thinking + 10-Stage + Sprint Governance + 4-Tier + Quality Gates + SASE + Documentation
3. **Stage mapping for docs only**: Only `/docs` folders are stage-mapped
4. **Use English only**: All technical content must be in English
5. **Follow code file naming**: Python snake_case, TypeScript camelCase, React PascalCase
6. **Maintain version consistency**: Update to 6.1.0 across related documents

### When Updating Framework Content
1. **Review CHANGELOG.md**: Check version history
2. **Check 02-Core-Methodology/**: Core principles and 7-Pillar Architecture
3. **Update consistently**: Version 6.1.0, dates February 2026
4. **Preserve legacy**: Use 10-archive/{NN}-Legacy/ for superseded content (RFC-001)
5. **Apply code file naming**: All new files must follow naming standards
6. **Respect documentation vs code separation**: Stage mapping only for `/docs`
7. **Apply Sprint Governance**: Include sprint context in PRs and documentation

### When Creating New Content
1. **Start with Design Thinking**: Apply 5-phase methodology before coding
2. **Choose Code Review tier**: Manual (Tier 1), AI-powered (Tier 2), or CodeRabbit (Tier 3)
3. **Follow 10-stage lifecycle**: Map content to appropriate stage
4. **Apply code file naming**: snake_case/camelCase/PascalCase as appropriate
5. **Measure success**: Track ROI, productivity, and quality metrics

## Framework Compliance Standards

### Required Compliance Metrics (SDLC 6.1.0)
- **10-Stage Lifecycle Applied**: All 10 stages considered
- **Code File Naming**: Python snake_case, TypeScript camelCase, React PascalCase
- **Design Thinking Applied**: 5-phase methodology for all new features
- **Code Review Active**: At least Tier 1 (manual) for all code changes
- **Productivity Gains**: 10x minimum, 50x achievable
- **Mock Instance Detection**: 0 instances (absolute Zero Mock Policy)
- **Test Coverage**: >90% with real services only
- **Performance**: <50ms response time target

### Quality Gates (SDLC 6.1.0)
- **Pre-Design Thinking**: User validation before coding starts
- **Pre-commit hooks**: Block commits with mock instances
- **Code file naming validation**: Enforce naming standards
- **Code Review enforcement**: At least Tier 1 for all changes
- **CI pipeline gates**: Enforce Zero Mock and performance standards

## Framework Evolution Context

```
SDLC 1.0 (June 2025)
  ↓ CEO + Claude Code collaboration begins
SDLC 3.x (July 2025)
  ↓ BFlow Platform teaches System Thinking
SDLC 4.6 (September 24, 2025)
  ↓ 679 mock crisis → Zero Mock Policy born
SDLC 4.7 (September 27, 2025)
  ↓ Battle-tested 5 pillars (HOW to build with excellence)
SDLC 4.8 (November 7, 2025)
  ↓ Design Thinking enhancement (WHAT to build that matters)
SDLC 4.9 (November 13, 2025)
  ↓ 10-Stage Complete Lifecycle (WHY → GOVERN full journey)
SDLC 4.9.1 (November 29, 2025)
  ↓ Code File Naming Standards Restored
SDLC 5.0.0 (December 5, 2025)
  ↓ Governance & Compliance + 4-Tier Classification + Industry Best Practices
SDLC 5.1.0 (December 11, 2025)
  ↓ SASE Integration + SE 3.0 Agentic Principles
SDLC 5.1.2 (December 24, 2025)
  ↓ Project Structure Standard + Quality Gates Enhancement
SDLC 5.1.3 (January 2026)
  ↓ 7-Pillar Architecture + Sprint Planning Governance (Pillar 2)
SDLC 5.2.0 (January 22, 2026)
  ↓ AI Governance Principles + Risk-Based Planning + Concentric Circles
SDLC 5.3.0 (January 2026)
  ↓ Stage Dependencies + Quality Assurance System (Section 7)
SDLC 6.0.0 (January 28, 2026)
  ↓ Unified Specification Standard (Section 8) + YAML Frontmatter
SDLC 6.0.3 (February 2, 2026)
  ↓ Boris Cherny Consolidation + Visual Documentation Standards
SDLC 6.0.4 (February 8, 2026)
  ↓ TDD Workflow Integration + 3-Phase Sprint Enhancement
SDLC 6.0.5 (February 15, 2026)
  ↓ RFC-001 Legacy Organization + Anti-Vibecoding Alignment
SDLC 6.0.6 (February 16, 2026)
  ↓ Anthropic Best Practices: CLAUDE.md Standard + Autonomous Codegen + MRP Template
SDLC 6.1.0 (February 18, 2026)
  ↓ Consolidation: Ring 1 slim, agentic→AI-GOV move, BRS/MTS/LPS→AGENTS.md, Multi-Agent Patterns
SDLC 6.1.1 (February 21, 2026)
  ↓ Post-Cleanup Patch: AI Council→Senior Review Board, 36 frozen templates archived, Conversation-First
SDLC 6.1.2 (March 9, 2026) ← CURRENT
  ↓ SOULs + TEAMs: 17 SASE role templates + 10 team charters added to Ring 2
```

## Proven Production Use

Framework đã được công ty NQH/MTS sử dụng để phát triển các platform trong
**NQH Technology Ecosystem** — 5-layer architecture, 14 platforms.

Reference: `Bflow-Platform/docs/00-foundation/01-vision/nqh-technology-ecosystem-vision.md`

## Quick Reference Links

**Essential Documentation**:
- Main README: [README.md](README.md)
- Core Methodology: [02-Core-Methodology/SDLC-Core-Methodology.md](02-Core-Methodology/SDLC-Core-Methodology.md)
- Implementation Guide: [07-Implementation-Guides/SDLC-Implementation-Guide.md](07-Implementation-Guides/SDLC-Implementation-Guide.md)
- Naming Standards: [02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md](02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md)

**NEW in 6.1.2**:
- SOUL Role Templates: [05-Templates-Tools/04-SASE-Artifacts/souls/README.md](05-Templates-Tools/04-SASE-Artifacts/souls/README.md)
- TEAM Charters: [05-Templates-Tools/04-SASE-Artifacts/teams/](05-Templates-Tools/04-SASE-Artifacts/teams/)

**NEW in 6.1.0**:
- Multi-Agent Patterns: [03-AI-GOVERNANCE/12-MULTI-AGENT-PATTERNS.md](03-AI-GOVERNANCE/12-MULTI-AGENT-PATTERNS.md)
- Agentic Core Principles (moved): [03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md](03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md)
- Agentic Maturity Model (moved): [03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md](03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md)
- System Thinking: [02-Core-Methodology/SDLC-System-Thinking-Foundation.md](02-Core-Methodology/SDLC-System-Thinking-Foundation.md)
- Crisis-to-Pattern: [02-Core-Methodology/SDLC-Crisis-To-Pattern-Methodology.md](02-Core-Methodology/SDLC-Crisis-To-Pattern-Methodology.md)
- Design Thinking Templates: [02-Core-Methodology/Documentation-Standards/SDLC-Design-Thinking-Templates.md](02-Core-Methodology/Documentation-Standards/SDLC-Design-Thinking-Templates.md)

**NEW in 6.0.6**:
- CLAUDE.md Standard: 3-tier (LITE/PRO/ENTERPRISE) with validation criteria
- Autonomous Codegen Patterns: Two-agent + 4-Gate Quality Pipeline methodology
- MRP Template: 5-section Merge-Readiness Package for Gate G4

**Added in 5.3.0-6.0.5**:
- Document Consolidation: Governance-Compliance (7→4), Documentation-Standards (13→7)
- Quality Assurance System (Section 7): Anti-Vibecoding, Vibecoding Index
- Stage Dependencies: Explicit stage prerequisites and exit criteria
- Unified Specification Standard (Section 8): YAML frontmatter + BDD requirements
- Sprint Governance: [02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md](02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md)
- Quality+Security Gates: [02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md](02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md)
- Team Collaboration: [02-Core-Methodology/Documentation-Standards/SDLC-Team-Collaboration.md](02-Core-Methodology/Documentation-Standards/SDLC-Team-Collaboration.md)
- Observability Checklist: [02-Core-Methodology/Governance-Compliance/SDLC-Observability-Checklist.md](02-Core-Methodology/Governance-Compliance/SDLC-Observability-Checklist.md)

**NEW in 4.9**:
- BFlow 52-Day Journey: [06-Case-Studies/BFlow-52-Day-Journey-Case-Study.md](06-Case-Studies/BFlow-52-Day-Journey-Case-Study.md)

---

The framework represents not theory but battle-tested patterns from 10 months of real platform development across the NQH Technology Ecosystem. With SDLC 6.3.1, we achieve excellence faster: **7-Pillar Architecture, Sprint Planning Governance, 10-stage complete lifecycle, Quality Assurance System (Anti-Vibecoding), Unified Specification Standard, CLAUDE.md Standard, Autonomous Codegen Patterns, SASE SOULs + TEAMs, 4-tier classification, 11 training modules (39h), production-ready in 1-2 weeks.**

**Last Updated**: April 17, 2026
**Framework Version**: SDLC 6.3.1
**Status**: PRODUCTION READY - 7-Pillar + Lean Ring 1 + 8 Mental Models + Long-Running Agent Protocol + Fix-First + Effort Compression + Terminal Status Taxonomy + 11 Training Modules (39h)
