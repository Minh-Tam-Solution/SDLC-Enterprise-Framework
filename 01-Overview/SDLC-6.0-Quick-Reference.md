# SDLC Framework 6.0.2 Quick Reference Guide

**Version**: 6.0.2
**Date**: February 2, 2026
**Status**: ACTIVE - PRODUCTION READY
**Purpose**: Fast lookup for key SDLC 6.0 concepts, navigation, and breaking changes

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

SDLC Orchestrator Integration:
  - sdlcctl e2e validate         # Validate E2E compliance
  - sdlcctl e2e cross-reference  # Validate Stage 03 ↔ 05 links
  - sdlcctl e2e generate-report  # Generate E2E test report
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
  - CLI validation commands (sdlcctl validate-consistency)
  - CI/CD integration examples (GitHub Actions, GitLab)
  - Tier-specific validation depths

Historical Context:
  - Sprint 128-129: Backend 100%, Frontend 0% (classic drift)
  - Solution: Mandatory stage alignment validation
```

**Implementation Guide**: [07-Implementation-Guides/SDLC-Stage-Consistency-Validation-Guide.md](../07-Implementation-Guides/SDLC-Stage-Consistency-Validation-Guide.md)

---

## What's New in 6.0.2 (MAJOR)

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
║                    SDLC 6.0.2 - 7 PILLARS + 2 SECTIONS                     ║
╠════════════════════════════════════════════════════════════════════════════╣
║  CORE PILLARS (0-6): Stable Foundation                                     ║
║    P0: Design Thinking    P3: 4-Tier Classification                        ║
║    P1: 10-Stage Lifecycle P4: Quality Gates                                ║
║    P2: Sprint Governance  P5: SASE (AI-Human)                              ║
║                           P6: Documentation Standards                      ║
║                                                                            ║
║  EXTENSION SECTIONS (7-8): Additive Capabilities                           ║
║    Section 7: Quality Assurance System (5.3.0)                            ║
║      - Vibecoding Index (0-100)                                           ║
║      - Progressive Routing (Green → Red)                                  ║
║                                                                            ║
║    Section 8: Unified Specification Standard (6.0.0)                      ║
║      - YAML Frontmatter (MANDATORY)                                        ║
║      - BDD Requirements (GIVEN-WHEN-THEN)                                 ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

## Quick Navigation

| I Want To... | Go To |
|--------------|-------|
| Understand SDLC 6.0 | [01-Overview/SDLC-Executive-Summary.md](SDLC-Executive-Summary.md) |
| Write a specification | [05-Templates-Tools/Framework-6.0/](../05-Templates-Tools/Framework-6.0/) |
| Use AI governance | [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) |
| Find a topic | [CONTENT-MAP.md](../CONTENT-MAP.md) |
| Understand changes | [CHANGELOG.md](../CHANGELOG.md) |
| Migrate from 5.3.0 | [99-Legacy/v5.3.0-Archive/](../99-Legacy/v5.3.0-Archive/) |

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
sdlcctl spec validate your-spec.md
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
├── 99-Legacy/                # Archived versions
├── CHANGELOG.md              # Version history
├── CONTENT-MAP.md            # Topic → file mapping
├── DEPRECATION-POLICY.md     # Redirect rules
└── CLAUDE.md                 # AI context file
```

---

## Migration from 5.3.0

1. **Archive Reference**: Old 5.3.0 docs at [99-Legacy/v5.3.0-Archive/](../99-Legacy/v5.3.0-Archive/)
2. **Add Frontmatter**: Add YAML metadata to all specs
3. **Convert to BDD**: Rewrite requirements as GIVEN-WHEN-THEN
4. **Declare Tier**: Add tier field (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
5. **Validate**: Run `sdlcctl spec validate --fix`

---

## Key Documents

| Document | Purpose |
|----------|---------|
| [SDLC-Specification-Standard.md](../05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md) | Core spec template |
| [SDLC-Core-Methodology.md](../02-Core-Methodology/SDLC-Core-Methodology.md) | 10-stage lifecycle |
| [03-AI-GOVERNANCE/README.md](../03-AI-GOVERNANCE/README.md) | 7 AI principles |
| [CONTENT-MAP.md](../CONTENT-MAP.md) | Topic navigation |

---

## Quick Checklist: Is This 6.0 Compliant?

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
```

---

**Document Status**: ACTIVE
**Last Updated**: January 28, 2026
**Framework**: SDLC 6.0.2 (7-Pillar + 2-Section)

*Quick reference for SDLC Framework 6.0.2 - Keep this handy!*
