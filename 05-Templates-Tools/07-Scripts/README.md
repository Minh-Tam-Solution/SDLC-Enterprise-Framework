# SDLC 6.1.1 Framework Scripts & Automation Tools
## Battle-Tested Automation from Real Platform Experience

**Version**: 6.1.1
**Status**: ACTIVE - PRODUCTION READY
**Date**: February 16, 2026
**Architecture**: 7-Pillar + 2-Section (Core + Extensions)
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) (7 Principles)
**Foundation**: Tools proven on BFlow, NQH-Bot, MTEP platforms
**Philosophy**: Build when needed + AI tools for flexibility

**7 Pillars + 2 Sections (SDLC 6.1.1)**:
- **Pillars 0-6**: Design Thinking → Documentation Permanence
- **Section 7**: Quality Assurance System (Vibecoding Index, Kill Switch)
- **Section 8**: Unified Specification Standard (YAML frontmatter, BDD)

**Legacy/Archive Policy**: Content in 10-Archive/{NN}-Legacy folders is never validated (RFC-001, SDLC 6.1.1).

---

## What's New in SDLC 6.1.1

### 7-Pillar + 2-Section Architecture Validation

`sdlc_validator.py` validates the complete architecture:

| Component | Name | Validation Focus |
|-----------|------|------------------|
| **Pillar 0** | Design Thinking | 5-phase methodology |
| **Pillar 1** | 10-Stage Lifecycle | Stage documentation (00-09) |
| **Pillar 2** | Sprint Governance | Planning hierarchy, retrospectives |
| **Pillar 3** | 4-Tier Classification | Project tier detection |
| **Pillar 4** | Quality Gates | Code review, Zero Mock, tests |
| **Pillar 5** | SASE Integration | AI+Human orchestration |
| **Pillar 6** | Documentation | Archival headers, version control |
| **Section 7** | Quality Assurance | Vibecoding Index, Progressive Routing |
| **Section 8** | Spec Standard | YAML frontmatter, BDD format |

### Section 8: Unified Specification Standard

Scripts now validate Section 8 compliance:
- **YAML frontmatter**: Mandatory metadata (`spec_id`, `tier`, `stage`, `status`)
- **BDD requirements**: GIVEN-WHEN-THEN format
- **Tier-awareness**: LITE/STANDARD/PROFESSIONAL/ENTERPRISE

### CLAUDE.md Standard (NEW in 6.0.6)

- **CLAUDE.md detection**: Validates presence of AI assistant context file at project root
- **AGENTS.md support**: Industry-standard AI collaboration context
- **AI Governance Principles**: 7 principles checked (Human Accountability through Continuous Learning)
- **Solo setup creates template**: `quickstart_solo_setup.py` generates CLAUDE.md automatically

### 3-Ring Architecture (Concentric Circles Model)

Validation aligns with the 3-Ring Architecture:
- **Core Ring** (timeless): Business logic, domain models - validated for stability
- **Governance Ring** (stable): Quality gates, SDLC compliance - enforced by validators
- **Outer Ring** (tools/changing): AI tools, CI/CD - configuration files checked

### MRP (Merge-Readiness Proof) Validation

- **MRP template detection**: Checks for MRP templates in `.sdlc/templates/`
- **SASE artifact awareness**: CRP, MRP, VCR artifact presence validated
- **Solo setup creates template**: `quickstart_solo_setup.py` generates MRP-TEMPLATE.md
- **Deprecated artifacts**: BRS, LPS, MTS no longer validated (replaced by AGENTS.md)

---

## Core Compliance Validators

```bash
07-Scripts/
├── README.md                             # This file
├── compliance_sdlc_validator.py          # PRIMARY: 7-Pillar + 2-Section validation
├── compliance_design_thinking_validator.py  # Pillar 0 validation (5 DT phases)
├── compliance_sdlc_scanner.py            # Backward compatibility wrapper
└── quickstart_solo_setup.py              # Solo developer (2 days → 10x)
```

---

## Quick Start

### Essential Commands

```bash
# 1. SDLC 6.1.1 Complete Validation (7 Pillars + 2 Sections)
python3 compliance_sdlc_validator.py /path/to/project

# 2. Design Thinking Compliance (Pillar 0)
python3 compliance_design_thinking_validator.py /path/to/project

# 3. Backward Compatible Scan
python3 compliance_sdlc_scanner.py /path/to/project

# 4. Quick Start Solo Project
python3 quickstart_solo_setup.py /path/to/project
```

---

## Key Scripts Explained

### SDLC 6.1.1 Complete Validator

**Validates complete 7-Pillar + 2-Section architecture**

```bash
# Usage
python3 compliance_sdlc_validator.py /path/to/project

# What it checks:
# - 7 Pillars (Design Thinking → Documentation)
# - Section 7 (Quality Assurance System - Vibecoding Index)
# - Section 8 (Specification Standard - YAML frontmatter, BDD)
# - SASE Artifacts (CRP, MRP, VCR, AGENTS.md)
# - CLAUDE.md / AGENTS.md presence (AI Governance)
# - 3-Ring Architecture alignment (Core → Governance → Outer)
# - Code File Naming Standards
# - MRP template availability
# - Legacy/Archive folders excluded

# Output example:
✅ Pillar 0-6: COMPLIANT
✅ Section 7 (Quality Assurance): COMPLIANT
✅ Section 8 (Spec Standard): COMPLIANT
✅ SASE Artifacts: DETECTED
✅ CLAUDE.md: PRESENT
✅ MRP Template: AVAILABLE
✅ File Naming Standards: COMPLIANT
🎉 SDLC 6.1.1 FULLY COMPLIANT
```

### Design Thinking Validator

**Ensures 5-phase methodology compliance**

```bash
# Usage
python3 compliance_design_thinking_validator.py /path/to/project

# What it validates:
# - Phase 1 (Empathize): User research documented
# - Phase 2 (Define): Problem statement validated
# - Phase 3 (Ideate): Solution generation evidence
# - Phase 4 (Prototype): Rapid validation performed
# - Phase 5 (Test): User testing completed
# - AI Governance: CLAUDE.md, AGENTS.md, 7 Principles awareness

# Output example:
✅ Phase 1 (Empathize): User research documented
✅ Phase 2 (Define): Problem statement validated
✅ Phase 3 (Ideate): 15 solutions generated
✅ Phase 4 (Prototype): Rapid prototype created
✅ Phase 5 (Test): User validation completed
✅ AI Governance (6.1.1): Principles awareness detected
📊 Design Thinking Score: 96% (NQH-Bot level)
```

### Solo Setup Script

**2 days to 10x productivity for solo developers**

```bash
# Usage
python3 quickstart_solo_setup.py /path/to/project

# What it does:
# 1. Creates SDLC 6.1.1 complete structure
# 2. Installs compliance validators
# 3. Sets up Design Thinking templates
# 4. Configures Code Review Tier 1
# 5. Creates AI development environment
# 6. Sets performance targets (<50ms)
# 7. Creates CLAUDE.md template (AI assistant context)
# 8. Creates MRP template (Merge-Readiness Proof)
```

---

## 4-Tier Classification Support

Validation adapts based on project tier:

| Tier | Team Size | Validation Requirements |
|------|-----------|------------------------|
| **LITE** | 1-2 | Basic validation, optional SASE |
| **STANDARD** | 3-10 | Full validation, CRP + MRP recommended |
| **PROFESSIONAL** | 10-50 | All + Section 8 spec compliance |
| **ENTERPRISE** | 50+ | Everything + audit compliance |

---

## Code File Naming Standards

- **Python**: `snake_case`, max 50 chars (e.g., `user_service.py`)
- **TypeScript**: `camelCase`, max 50 chars (e.g., `userService.ts`)
- **React**: `PascalCase`, max 50 chars (e.g., `UserDashboard.tsx`)
- **Alembic**: `{rev}_{desc}.py`, max 60 chars

---

## Implementation Status

| Script | Status | Use Case |
|--------|--------|----------|
| `sdlc_validator.py` | ✅ READY | Daily 7-Pillar + 2-Section validation |
| `design_thinking_validator.py` | ✅ READY | Pillar 0 (5 DT phases) |
| `sdlc_scanner.py` | ✅ READY | Backward compatibility |
| `solo_setup.py` | ✅ READY | Solo developer onboarding |

---

## Related Resources

### Core Documentation
- [SDLC-Core-Methodology.md](../../02-Core-Methodology/SDLC-Core-Methodology.md) - 10-stage lifecycle
- [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) - 7 AI Governance Principles
- [01-Specification-Standard/](../01-Specification-Standard/) - Section 8 templates

### AI Tools
- [02-AI-Tools/](../02-AI-Tools/) - AI-powered development tools
- [04-SASE-Artifacts/](../04-SASE-Artifacts/) - CRP, MRP, VCR templates

---

**Status**: PRODUCTION READY
**Framework**: SDLC 6.1.1 (7-Pillar + 2-Section)
**Philosophy**: Build when needed + AI for flexibility = Optimal balance

***"Validate with code, automate with AI."***
