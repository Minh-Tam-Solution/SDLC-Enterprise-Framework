# SDLC Framework 6.3.0 Quick Reference Guide

**Version**: 6.3.0
**Date**: March 18, 2026
**Status**: ACTIVE - PRODUCTION READY
**Purpose**: Fast lookup for key SDLC 6.3.0 concepts, navigation, and breaking changes

---

## What's New in 6.3.0 (AGENTIC SDLC + LEAN RING 1)

### Lean Ring 1 Consolidation + Agentic SDLC Alignment

```yaml
Key Changes (6.3.0 — Mar 18, 2026):

  Lean Ring 1 Consolidation:
    - Ring 1 files: 41→30 substantive, 584→463KB (-21%)
    - 3 stage docs merged → SDLC-Stage-Lifecycle-Framework.md
    - 2 quality docs merged → SDLC-Quality-Gates-Assurance-Framework.md
    - 9 implementation docs moved to Ring 2 (redirect stubs expire Sep 2026)
    - 42 tool-specific references sanitized → 0 product refs in Ring 1

  New Content:
    - Mental Model #7: "Agent Continuity" (checkpoint/resume across sessions)
    - Mental Model #8: "More People Build, Under Guardrails" (citizen developers)
    - 03-AI-GOVERNANCE/16-LONG-RUNNING-AGENT-PROTOCOL.md (Ring 1)
    - 07-Implementation-Guides/Citizen-Developer-Guide.md (Ring 3)
    - 05-Templates-Tools/Agentic-ROI-Calculator.md (Ring 2)

  Evidence Base:
    - Anthropic "2026 Agentic Coding Trends Report" (8 trends)
    - NIST AI Agent Standards Initiative (emerging, 2027+)
    - Singapore Model AI Governance Framework (Jan 2026)
    - Anthropic Context Engineering Guide

  Breaking Changes:
    - 14 file paths changed (redirect stubs at old locations)
    - Old originals archived: 10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/
```

## What Was in 6.1.x (Previous Releases)

### 6.1.2 (Mar 2026) — SOULs + TEAMs Templates
18 SOUL role templates + 10 TEAM charters added to Ring 2.

### 6.1.0 (Feb 2026) — Ring 1 Slim + Consolidation

### Ring 1 Monolith Slim + Dedicated Foundation Documents

```yaml
Key Changes (6.1.0 — Feb 18, 2026):
  Ring 1 Monolith Slim:
    - Design Thinking Principles: 2,018→364 lines (82% reduction)
    - Agentic Core Principles: 1,313→293 lines (moved to 03-AI-GOVERNANCE)
    - 9 Design Thinking templates extracted to Documentation-Standards/

  Dedicated Foundation Documents:
    - 02-Core-Methodology/SDLC-System-Thinking-Foundation.md
        Standalone doc for core concept (since SDLC 4.0): 4-Layer Iceberg Model, 6 Mental Models
    - 02-Core-Methodology/SDLC-Crisis-To-Pattern-Methodology.md
        Extracted from Design Thinking (formalizes Mental Model #5): 5-step pipeline
    - 07-Implementation-Guides/MULTI-AGENT-PATTERNS.md
        NEW: 10 multi-agent collaboration patterns (lane queues, failover, snapshots, @mention routing)

  Structural Reorganization:
    - 03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md (moved from 02-Core)
    - 03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md (moved from 02-Core)
    - BRS/MTS/LPS deprecated → use AGENTS.md (industry standard)

  Version Alignment: 636 stale refs updated to 6.1.0
  Breaking Changes: NONE (additive consolidation)
```

---

## What's New in 6.0.6 (MINOR)

### Anthropic Best Practices Integration

```yaml
Key Changes:
  3 New AI Governance Methodology Documents:
    - 05-Templates-Tools/03-Agent-Templates/CLAUDE-MD-STANDARD.md
        CLAUDE.md 3-tier structure: LITE (500-1K lines), PRO (1.5K-3K), ENTERPRISE (2K+)
        Content principles: Constraints first, file paths > descriptions, commands > explanations
        Anti-patterns: Information dump, stale docs, abstract philosophy, copy-paste README

    - 07-Implementation-Guides/AUTONOMOUS-CODEGEN-PATTERNS.md
        Two-agent pattern: Initializer Agent → Coding Agent loop → Quality Gates
        4-Gate Pipeline: G1 (Spec Review) → G2 (Security) → G3 (Tests) → G4 (Human Review)
        Retry logic: max_retries=3 with deterministic feedback, escalation path

    - 05-Templates-Tools/06-Manual-Templates/SDLC-MRP-Template.md
        5-section Merge-Readiness Package: Change Summary, Evidence Refs, Rollback, Tests, Deploy
        Gate G4 requires MRP for PRs >100 LOC at STANDARD+ tier

  3-Ring Compliance:
    - All 3 documents are Core Ring (tool-agnostic, vendor-neutral)
    - Source: Anthropic Data Infrastructure team + claude-quickstarts
    - Framework-First: Methodology created before any platform automation
```

---

## What's New in 6.0.5 (MINOR)

### RFC-001 + Governance Loop + Cleanup

```yaml
Key Changes:
  RFC-001 Legacy Document Organization:
    - Eliminates 99-Legacy/ from active stages (00-09)
    - Centralizes to 10-archive/{NN}-Legacy/ with stage alignment
    - Production-validated: 57% size reduction (211MB→91MB)
    - Migration script: migrate-legacy-to-archive.sh
    - CI/CD blocks 99-Legacy/ reintroduction
    - Adoption deadline: March 15, 2026

  SPEC-0001 Anti-Vibecoding Alignment:
    - Vibecoding Index signals updated (5 signals, SPEC-0001 authoritative)
    - Progressive Routing thresholds: <20/20-40/40-60/>=60
    - Kill Switch: rejection >80%, latency >500ms, CVEs >5
    - Machine-readable controls in anti-vibecoding.yaml

  4 New Framework Templates:
    - deployment_go-live-readiness-checklist.md (100-item tactical)
    - deployment_go-live-readiness-assessment.md (Go/No-Go scoring)
    - governance_maturity-assessment-framework.md (per-stage 0-100%)
    - governance_risk-register-analyzer.md (L×I scoring matrix)

  Governance Loop + Cleanup:
    - Code review consolidation (3 guides → 1 unified)
    - Simplified overengineered modules
    - Framework scripts upgraded

  SDLC CLI Enhancements:
    - Fuzzy P0 detection for legacy stage names
    - 3-strategy resolution: exact → alternative → fuzzy
    - Production-validated: P0 detection improved from 0% to 64-71%
```

---

## What's New in 6.0.4 (MINOR)

### TDD Workflow Integration + 3-Phase Sprint Enhancement

```yaml
Production Validation:
  Total Tests: 113 (all written FIRST per TDD)
  Pass Rate: 100% on first implementation
  Coverage: Exceeds tier requirements

TDD Workflow (RED-GREEN-REFACTOR):
  1. RED Phase: Write tests FIRST (must fail initially)
  2. GREEN Phase: Implement minimal code to pass (100% pass required)
  3. REFACTOR Phase: Clean up code, maintain passing tests

Tier-Aware TDD Coverage Targets:
  - LITE: 70%
  - STANDARD: 85%
  - PROFESSIONAL: 95%
  - ENTERPRISE: 95%+ with security tests

3-Phase Sprint Lifecycle Enhanced:
  Phase 1: PRE-SPRINT (1-2 days)
    - Design doc validation (ADR/Spec/API contracts)
    - TDD test strategy + coverage targets per tier
    - G-Sprint gate approval

  Phase 2: EXECUTION (5-8 days)
    - TDD Cycle per feature: RED → GREEN → REFACTOR
    - Daily standups + progress tracking
    - Mid-sprint check (Day 5): 50% progress?

  Phase 3: POST-SPRINT (24h max)
    - Documentation completion (MANDATORY)
    - G-Sprint-Close gate
    - Retrospective (max 3 action items)

Spec Converter Methodology (Section 8 Enhancement):
  - SpecIR: Format-agnostic intermediate representation
  - OpenSpec → SDLC 6.0 conversion: SDLC CLI spec convert
  - SDLC 6.0 → OpenSpec export: SDLC CLI spec export
  - BDD ↔ API mapping: Automatic test generation

Key Files Updated:
  - SDLC-Sprint-Planning-Guide.md (+TDD Workflow)
  - SDLC-Specification-Standard.md (+Section 8: Spec Converter)
  - SDLC-Continuous-Improvement-Guide.md (+6.0.4 Success Story)
```

**Rationale**: TDD proven effective for AI-assisted development through production validation. 3-Phase Sprint Model enhanced with explicit TDD integration. Spec Converter enables format interoperability.

**References**:
- [CHANGELOG.md (6.0.4)](../CHANGELOG.md)
- [SDLC-Sprint-Planning-Guide.md](../02-Core-Methodology/Documentation-Standards/SDLC-Sprint-Planning-Guide.md)
- [SDLC-Specification-Standard.md](../05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md)

---

## What's New in 6.0.3 (MINOR)

### Boris Cherny Best Practices Consolidation

```yaml
Consolidation (5 RFC → Framework):
  - RFC-603 → MCP Integration Guide (6x faster bug triage)
  - RFC-604 → Git Workflow Patterns (2.5x productivity with worktrees)
  - RFC-605 → Continuous Learning Protocol (zero repeated bugs)
  - RFC-606 → Research Delegation Pattern (3.3x faster research)
  - RFC-607 → Visual Documentation Standards (4x faster onboarding)

New Files Created (2):
  - 07-Implementation-Guides/MCP-Integration-Guide.md (~450 lines)
  - 04-AI-Tools-Landscape/best-practices-2026/04-git-workflow-patterns.md (~575 lines)

Enhanced Files (3):
  - memory-context-management.md (+130 lines: Continuous Learning)
  - sub-agent-orchestration.md (+95 lines: Research Delegation)
  - Visual Documentation Standards (new +280 lines)

Key Features:
  - MCP Integration: GitHub/Slack/Jira automated bug triage
  - Git Worktrees: Parallel AI development (4 sessions simultaneously)
  - Continuous Learning: .claude/learnings/ → auto-update CLAUDE.md
  - Research Delegation: Parallel subagents for pattern discovery
  - Visual Documentation: ASCII diagrams, HTML presentations, sequence diagrams

Framework-First Compliance:
  - Zero RFC naming in Framework (reserved for Orchestrator only)
  - 3-Circle Architecture (Ring 1: Core, Ring 2: Governance, Ring 3: Implementation)
  - Net change: -3 files (5 deleted - 2 created = better organization)
  - Content loss: 0 methodology lines (100% preservation)

Productivity Metrics Preserved:
  - MCP: 6x faster bug triage
  - Git Worktrees: 2.5x faster (20h → 8h with 4 parallel sessions)
  - Research Delegation: 3.3x faster (5h → 1.5h)
  - Visual Docs: 4x faster onboarding (2h → 30min)
```

**Rationale**: Boris Cherny's 10 AI Development Lessons consolidated into Framework structure following 3-Circle Architecture. All RFCs renamed and integrated to eliminate Framework-Orchestrator naming confusion.

**References**:
- [CHANGELOG.md (6.0.3)](../CHANGELOG.md)
- [CONTENT-MAP.md (Boris Cherny Consolidation)](../CONTENT-MAP.md)
- [MCP Integration Guide](../07-Implementation-Guides/MCP-Integration-Guide.md)
- [Git Workflow Patterns](../04-AI-Tools-Landscape/best-practices-2026/04-git-workflow-patterns.md)

---

## What's New in 6.0.2 (MINOR)

### E2E API Testing Enhancement (RFC-SDLC-602)

```yaml
New Templates (5):
  - testing_e2e-api-testing-workflow.md     # 6-phase testing workflow
  - testing_security-testing-checklist.md   # OWASP API Top 10 (2023)
  - SDLC-Stage-Cross-Reference.md           # Stage 03 ↔ 05 traceability
  - SDLC-Testing-Artifacts-Structure.md     # Test folder structure
  - API Documentation Template              # Per-endpoint test status

Key Features:
  - 6-phase E2E testing workflow (Discovery → Execution → Reporting)
  - Stage 03 ↔ 05 cross-reference matrix (bidirectional traceability)
  - OWASP API Security Top 10 checklist (all 10 items)
  - Testing artifacts folder structure (SDLC-compliant)
  - SSOT principle for openapi.json (single source in Stage 03)

Automation Integration:
  - [SDLC CLI] e2e validate         # Validate E2E compliance
  - [SDLC CLI] e2e cross-reference  # Validate Stage 03 ↔ 05 links
  - [SDLC CLI] e2e generate-report  # Generate E2E test report
  - 4 new evidence artifact types
  - 2 new OPA policies (e2e_testing_compliance, stage_cross_reference)

Validation Metrics (SOP Generator Pilot):
  - 58 endpoints tested
  - 84.5% pass rate
  - 83% time savings (3h → 30min)
  - CTO Approval: 9.2/10
```

**RFC**: [RFC-SDLC-602-E2E-API-TESTING.md](../09-Continuous-Improvement/RFC/RFC-SDLC-602-E2E-API-TESTING.md)

---

## What's New in 6.0.1 (MINOR)

### Stage Consistency Validation (SPEC-0021)

```yaml
New Specification:
  - SPEC-0021: Stage Consistency Validation Service
  - Prevents "spec drift" (implementation diverges from design)
  - 4-stage consistency model (01 → 02 → 03 → 04)

Key Features:
  - Pre/Post-implementation checklists
  - Artifact integrity hashing (SHA256 checksums)
  - CLI validation commands (SDLC compliance validator)
  - CI/CD integration examples (GitHub Actions, GitLab)
  - Tier-specific validation depths

Historical Context:
  - Historical example: Backend 100%, Frontend 0% (classic drift)
  - Solution: Mandatory stage alignment validation
```

**Implementation Guide**: [07-Implementation-Guides/SDLC-Stage-Consistency-Validation-Guide.md](../07-Implementation-Guides/SDLC-Stage-Consistency-Validation-Guide.md)

---

## What's New in 6.0.0 (MAJOR)

### Section 8: Unified Specification Standard (MAJOR)

```yaml
Breaking Changes:
  - All new specs MUST use YAML frontmatter
  - Requirements MUST use BDD format (GIVEN-WHEN-THEN)
  - Tier declaration is MANDATORY

New Templates:
  - SDLC-Specification-Standard.md    # Core template
  - DESIGN_DECISIONS.md               # Lightweight ADR
  - SPEC_DELTA.md                     # Version tracking
  - CONTEXT_AUTHORITY_METHODOLOGY.md  # Dynamic AGENTS.md
```

**Location**: [05-Templates-Tools/01-Specification-Standard/](../05-Templates-Tools/01-Specification-Standard/)

---

## 7-Pillar + 2-Section Architecture

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    SDLC 6.3.0 - 7 PILLARS + 2 SECTIONS                     ║
╠════════════════════════════════════════════════════════════════════════════╣
║  CORE PILLARS (0-6): Stable Foundation                                     ║
║    P0: Design Thinking    P3: 4-Tier Classification                        ║
║    P1: 10-Stage Lifecycle P4: Quality Gates                                ║
║    P2: Sprint Governance  P5: SASE (AI-Human)                              ║
║       + 3-Phase Lifecycle P6: Documentation Standards                      ║
║       + TDD Integration                                                    ║
║                                                                            ║
║  EXTENSION SECTIONS (7-8): Additive Capabilities                           ║
║    Section 7: Quality Assurance System (5.3.0)                            ║
║      - Vibecoding Index (0-100)                                           ║
║      - Progressive Routing (Green → Red)                                  ║
║                                                                            ║
║    Section 8: Unified Specification Standard (6.0.4)                      ║
║      - YAML Frontmatter (MANDATORY)                                        ║
║      - BDD Requirements (GIVEN-WHEN-THEN)                                 ║
║      - Spec Converter (SpecIR format-agnostic)                            ║
║      - Tier-Aware TDD Coverage Requirements                               ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

## Quick Navigation

| I Want To... | Go To |
|--------------|-------|
| Understand SDLC 6.3.0 | [01-Overview/SDLC-Executive-Summary.md](SDLC-Executive-Summary.md) |
| Write a specification | [05-Templates-Tools/Framework-6.0/](../05-Templates-Tools/Framework-6.0/) |
| Use AI governance | [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) |
| Find a topic | [CONTENT-MAP.md](../CONTENT-MAP.md) |
| Understand changes | [CHANGELOG.md](../CHANGELOG.md) |
| Migrate from 5.3.0 | [10-archive/02-Legacy/v5.3.0-Archive/](../10-archive/02-Legacy/v5.3.0-Archive/) |

---

## 4-Tier Classification

| Tier | Team | Budget | Key Requirements |
|------|------|--------|------------------|
| **LITE** | 1-2 | <$50K | Minimal spec, basic AI tools |
| **STANDARD** | 3-10 | $50-200K | Full spec format, SASE artifacts |
| **PROFESSIONAL** | 10-50 | $200K-1M | All sections, compliance features |
| **ENTERPRISE** | 50+ | $1M+ | Everything + custom + audit |

---

## 10-Stage Lifecycle

| Stage | Name | Key Deliverable |
|-------|------|-----------------|
| 00 | FOUNDATION (WHY?) | Problem validated |
| 01 | PLANNING (WHAT?) | Requirements defined |
| 02 | DESIGN (HOW?) | Architecture designed |
| 03 | INTEGRATE | API contracts, systems connected |
| 04 | BUILD | Code implemented |
| 05 | TEST | Tests passing |
| 06 | DEPLOY | Released to production |
| 07 | OPERATE | Running, monitored |
| 08 | COLLABORATE | Teams aligned |
| 09 | GOVERN | Compliant + auditable |

---

## 7 AI Governance Principles

| # | Principle | One-Line Summary |
|---|-----------|------------------|
| 1 | AI-Human Collaboration | Human guides, AI executes, Human verifies |
| 2 | Agent Accountability | Human ALWAYS owns shipped code |
| 3 | Planning Mode | Risk-based trigger (auth, API, payments) |
| 4 | Verification-First | TDD, evidence, validation before merge |
| 5 | Context Management | AGENTS.md <60 lines |
| 6 | Tool Evaluation | Criteria to evaluate ANY AI tool |
| 7 | Anti-Patterns | What NOT to do with AI |

**Location**: [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/)

---

## Specification Quick Start

### 1. Minimum YAML Frontmatter

```yaml
---
spec_id: SPEC-0001
spec_name: "Your Specification Name"
spec_version: "1.0.0"
status: draft
tier: STANDARD
stage: "03"
category: functional
owner: "your-team"
created: 2026-01-28
last_updated: 2026-01-28
---
```

### 2. BDD Requirement Format

```markdown
#### FR-001: [Requirement Title]
**Priority**: P0
**Tier**: STANDARD

GIVEN [initial context]
WHEN [action occurs]
THEN [expected outcome]
```

### 3. Validate

```bash
# Run SDLC compliance validation on your specification
[SDLC CLI] spec validate your-spec.md
```

---

## Folder Structure

```
SDLC-Enterprise-Framework/
├── 01-Overview/              # Executive summary, quick start
├── 02-Core-Methodology/      # 10-stage, sprint governance
├── 03-AI-GOVERNANCE/         # 7 AI principles (Core ring)
├── 04-AI-TOOLS-LANDSCAPE/    # Tool profiles (Outer ring)
├── 05-Templates-Tools/       # All templates
│   └── 01-Specification-Standard/  # Section 8 templates (6.0)
├── 06-Case-Studies/          # Battle-tested patterns
├── 07-Implementation-Guides/ # How-to guides
├── 08-Training-Materials/    # Learning resources
├── 09-Continuous-Improvement/
├── 10-archive/               # Centralized legacy archive (RFC-001, 6.0.6)
├── CHANGELOG.md              # Version history
├── CONTENT-MAP.md            # Topic → file mapping
├── DEPRECATION-POLICY.md     # Redirect rules
└── CLAUDE.md                 # AI context file
```

---

## Migration from 5.3.0

1. **Archive Reference**: Old 5.3.0 docs at [10-archive/02-Legacy/v5.3.0-Archive/](../10-archive/02-Legacy/v5.3.0-Archive/)
2. **Add Frontmatter**: Add YAML metadata to all specs
3. **Convert to BDD**: Rewrite requirements as GIVEN-WHEN-THEN
4. **Declare Tier**: Add tier field (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
5. **Validate**: Run SDLC compliance validation with auto-fix

---

## Key Documents

| Document | Purpose |
|----------|---------|
| [SDLC-Specification-Standard.md](../05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md) | Core spec template |
| [SDLC-Core-Methodology.md](../02-Core-Methodology/SDLC-Core-Methodology.md) | 10-stage lifecycle |
| [03-AI-GOVERNANCE/README.md](../03-AI-GOVERNANCE/README.md) | 7 AI principles |
| [CONTENT-MAP.md](../CONTENT-MAP.md) | Topic navigation |

---

## Quick Checklist: Is This 6.3.0 Compliant?

```yaml
Specification:
  [ ] Has YAML frontmatter with all required fields?
  [ ] Uses BDD format (GIVEN-WHEN-THEN) for requirements?
  [ ] Declares tier (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)?
  [ ] References stage (00-09)?

AI Usage:
  [ ] Following AI-Human collaboration model?
  [ ] Using Planning Mode for risk factors?
  [ ] Context file <60 lines?
  [ ] Evidence before merge?

TDD Compliance (6.0.4):
  [ ] Tests written FIRST (RED phase)?
  [ ] All tests passing before merge (GREEN phase)?
  [ ] Code refactored with tests maintained (REFACTOR phase)?
  [ ] Coverage meets tier target (LITE 70%, STANDARD 85%, PRO/ENT 95%)?

Sprint Governance (3-Phase):
  [ ] Pre-Sprint: Design docs validated, TDD strategy defined?
  [ ] Execution: TDD cycle followed per feature?
  [ ] Post-Sprint: Documentation completed within 24h?

Legacy Organization (6.3.0 RFC-001):
  [ ] No 99-Legacy/ folders in active stages (00-09)?
  [ ] Legacy content in 10-archive/{NN}-Legacy/?
  [ ] CI/CD blocks 99-Legacy/ reintroduction?
```

---

**Document Status**: ACTIVE
**Last Updated**: March 18, 2026
**Framework**: SDLC 6.3.0 (7-Pillar + 2-Section + TDD + RFC-001 + Anthropic Patterns)

*Quick reference for SDLC Framework 6.3.0 - Keep this handy!*
