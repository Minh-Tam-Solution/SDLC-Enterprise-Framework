# Governance & Compliance Standards

**Version**: 6.2.1
**Date**: February 18, 2026
**Stage**: 02 - Core Methodology
**Pillar**: 2 - Sprint Planning × Pillar 4 - Quality Gates × Pillar 5 - SASE × Pillar 7 - Quality Assurance System
**Status**: ACTIVE - Production Standard
**Authority**: CTO + CPO Office
**AI Governance**: Aligned with 03-AI-GOVERNANCE principles (Verification-First, Human Accountability)
**6.2.0**: Quality Assurance System + Quality-Security Gates consolidated into single framework. Observability moved to Ring 2.

---

## Purpose

Define governance, quality, security, and compliance standards that form the **core pillars of SDLC 6.2.0**:

| Pillar | Document | Focus |
|--------|----------|-------|
| **Pillar 2** | [SDLC-Sprint-Governance.md](./SDLC-Sprint-Governance.md) | Sprint execution + 3-Phase Lifecycle + TDD Integration |
| **Pillar 4+5+Section 7** | [SDLC-Quality-Gates-Assurance-Framework.md](./SDLC-Quality-Gates-Assurance-Framework.md) | Quality gates (G0-G4) + Anti-Vibecoding + Security (consolidated 6.2.0) |

---

## Documents in This Section

| Document | Pillar | Purpose | Tier Required |
|----------|--------|---------|---------------|
| [SDLC-Sprint-Governance.md](./SDLC-Sprint-Governance.md) | **Pillar 2** | 10 Golden Rules, Sprint gates, Stage-Sprint integration, Change management | ALL tiers |
| [SDLC-Quality-Gates-Assurance-Framework.md](./SDLC-Quality-Gates-Assurance-Framework.md) | **Pillar 4 + 5** | Quality gates (G0-G4), Security gates, SBOM, SAST, OWASP ASVS | ALL tiers |
### Consolidated Documents (6.2.0)

| New Document | Merged From | Version |
|--------------|-------------|---------|
| **SDLC-Quality-Gates-Assurance-Framework.md** | Quality-Assurance-System + Quality-Security-Gates | 6.2.0 |
| **SDLC-Sprint-Governance.md** | Sprint-Planning-Governance + Stage-Sprint-Integration + Change-Management | 5.3.0 |

### Moved to Ring 2 (6.2.0)
| Document | New Location |
|----------|-------------|
| SDLC-Observability-Checklist.md | `05-Templates-Tools/05-Checklists/` (redirect stub at old location) |

Previous versions: `10-Archive/02-Legacy/v6.2.0-Pre-Consolidation/` + `10-Archive/02-Legacy/5.2.0-Deprecated/`

---

## Pillar Integration Map

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE & COMPLIANCE PILLARS                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │ Pillar 2: Sprint Planning Governance (SDLC-Sprint-Governance) │     │
│  │ ┌─────────────────────────────────────────────────────────┐   │     │
│  │ │ • 10 Golden Rules (Sprint Numbers, Documentation, SSOT) │   │     │
│  │ │ • Sprint Gates: G-Sprint + G-Sprint-Close               │   │     │
│  │ │ • 3-Phase Sprint Lifecycle (6.0.4): PRE → EXEC → POST   │   │     │
│  │ │ • TDD Workflow: RED → GREEN → REFACTOR (6.0.4)          │   │     │
│  │ │ • Tier-Aware TDD Coverage: 70% → 85% → 95% (6.0.4)      │   │     │
│  │ │ • Stage × Sprint Integration (Multi-stage sprints)      │   │     │
│  │ │ • Change Management (Standard/Normal/Emergency/Roadmap) │   │     │
│  │ └─────────────────────────────────────────────────────────┘   │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                              │                                          │
│                              ▼                                          │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │ Pillar 4+5: Quality & Security Gates (SDLC-Quality-Security)  │     │
│  │ ┌─────────────────────────────────────────────────────────┐   │     │
│  │ │ • Feature Track: G0 → G1 → G2 → G3 → G4                 │   │     │
│  │ │ • Quality by Tier: LITE → STANDARD → PRO → ENTERPRISE   │   │     │
│  │ │ • Security: SBOM, SAST, DAST, OWASP ASVS L1/L2          │   │     │
│  │ │ • DORA Metrics: DF, LT, MTTR, CFR                       │   │     │
│  │ └─────────────────────────────────────────────────────────┘   │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                              │                                          │
│                              ▼                                          │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │ Pillar 7: Quality Assurance System (Anti-Vibecoding)          │     │
│  │ ┌─────────────────────────────────────────────────────────┐   │     │
│  │ │ • Vibecoding Index (0-100) - 5 weighted signals         │   │     │
│  │ │ • Progressive Routing (Green → Yellow → Orange → Red)   │   │     │
│  │ │ • Auto-Generation Layer (Intent, Ownership, Context)    │   │     │
│  │ │ • Kill Switch Criteria (>80% rejection, >500ms latency) │   │     │
│  │ └─────────────────────────────────────────────────────────┘   │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Dual-Track Quality Gates (Pillar 4)

### Feature Gates (Lifecycle Track)

| Gate | Stage | Focus |
|------|-------|-------|
| **G0** | 00-FOUNDATION | Problem statement validated |
| **G1** | 01-PLANNING | Requirements signed off |
| **G2** | 02-DESIGN | Architecture approved |
| **G3** | 04-BUILD | Code review + tests pass |
| **G4** | 06-DEPLOY | Production readiness verified |

### Sprint Gates (Execution Track)

| Gate | Timing | Focus |
|------|--------|-------|
| **G-Sprint** | Sprint Start | Sprint plan complete, scope defined |
| **G-Sprint-Close** | Sprint End | DoD met, retro completed, metrics captured |

**Key Insight**: Sprint Gates run IN PARALLEL with Feature Gates. A sprint can span multiple stages.

---

## Sprint Planning Governance (Pillar 2)

### 10 Golden Rules

| # | Rule | Purpose |
|---|------|---------|
| 1 | **One Roadmap Rules All** | Single truth for phases/milestones |
| 2 | **Phase Before Sprint** | Sprint must align to phase |
| 3 | **Sprint Scope is Sacred** | No mid-sprint scope changes |
| 4 | **Backlog Feeds Sprint** | Only from refined backlog |
| 5 | **SSOT or Chaos** | One system of record |
| 6 | **Close Before Start** | Finish sprint N before N+1 |
| 7 | **Carryover is Debt** | Track and reduce carryover |
| 8 | **Velocity is History** | Use past data, not wishes |
| 9 | **Dependencies Declared** | Explicit before sprint starts |
| 10 | **Retro Before Repeat** | Learn before next sprint |

### Planning Hierarchy

```
Roadmap (6-12 months)
    └── Phase (1-3 months)
            └── Sprint (1-2 weeks)
                    └── Backlog (individual items)
```

---

## Security Gates (Pillar 5)

### SASE Integration by Stage

| Stage | Security Activities |
|-------|-------------------|
| 00-FOUNDATION | Threat modeling, data classification |
| 01-PLANNING | Security requirements, compliance mapping |
| 02-DESIGN | Secure architecture review, OWASP checklist |
| 04-BUILD | SAST, secret scanning, dependency audit |
| 05-TEST | DAST, penetration testing (PROFESSIONAL+) |
| 06-DEPLOY | SBOM generation, runtime security |
| 07-OPERATE | Vulnerability management, incident response |

---

## Quick Start by Tier

### LITE Tier (1-2 people)
```yaml
Sprint Governance:
  - Basic sprint plan (informal)
  - Single Backlog

Quality Gates:
  - Manual code review (informal)
  - Basic tests

Security:
  - .env files (not in git)
  - Basic dependency awareness
```

### STANDARD Tier (3-10 people)
```yaml
Sprint Governance:
  - Formal Sprint Plan with scope
  - G-Sprint gate (checklist)
  - Sprint Retrospective

Quality Gates:
  - CI/CD with linting, unit tests
  - PR reviews required

Security:
  - npm audit / pip-audit on PRs
  - Dependabot enabled
  - Critical CVEs within 7 days
```

### PROFESSIONAL Tier (10-50 people)
```yaml
Sprint Governance:
  - Full Planning Hierarchy (Roadmap → Sprint)
  - G-Sprint + G-Sprint-Close gates
  - Velocity tracking
  - Carryover management

Quality Gates:
  - 80%+ test coverage
  - DORA metrics tracking
  - Full gate compliance (G0-G4)

Security:
  - Full SBOM generation
  - SAST in CI/CD
  - OWASP ASVS Level 1
  - Quarterly audits
```

### ENTERPRISE Tier (50+ people)
```yaml
Sprint Governance:
  - Everything in PROFESSIONAL
  - Multi-team sprint coordination
  - Sprint metrics dashboard
  - Weekly velocity reviews

Quality Gates:
  - 95%+ test coverage
  - Automated gate enforcement
  - Compliance reporting

Security:
  - OWASP ASVS Level 2+
  - Penetration testing
  - Continuous compliance
  - Annual third-party audits
```

---

## Governance vs. Stage 09 (GOVERN)

| Aspect | 02-Governance-Compliance (This Folder) | 09-GOVERN Stage |
|--------|----------------------------------------|-----------------|
| **Scope** | Standards & policies (HOW to comply) | Strategic oversight (WHAT to report) |
| **Audience** | All teams (mandatory compliance) | Executives (decision making) |
| **Content** | Quality gates, security gates, sprint governance | Status reports, risk reports, KPIs |
| **When** | Every stage (continuous) | Stage 09 specific activities |

---

## Related Documents

- [SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 8-Pillar Architecture (incl. Pillar 7: Quality Assurance System)
- [SDLC-Quality-Gates-Assurance-Framework.md](../SDLC-Quality-Gates-Assurance-Framework.md) - Pillar 7 (Anti-Vibecoding)
- [SDLC-Stage-Lifecycle-Framework.md](../SDLC-Stage-Lifecycle-Framework.md) - Stage completion requirements
- [Documentation-Standards/](../Documentation-Standards/) - Pillar 6 standards
- [SDLC-Sprint-Planning-Guide.md](../Documentation-Standards/SDLC-Sprint-Planning-Guide.md) - Sprint planning guide (flattened in 6.0.0)

---

## Changelog

### v6.0.4 (February 8, 2026)
- **TDD Workflow Integration**: RED-GREEN-REFACTOR cycle integrated into Sprint Governance
- **3-Phase Sprint Lifecycle Enhanced**: PRE-SPRINT → EXECUTION → POST-SPRINT
- **Tier-Aware TDD Coverage**: LITE 70%, STANDARD 85%, PRO/ENT 95%
- Production validation: 113 tests, 100% pass rate

### v6.0.3 (February 2, 2026)
- Boris Cherny Best Practices Consolidation

### v6.0.0 (January 28, 2026)
- Folder flattening (remove layer 3), version upgrade
- Updated all SDLC references to 6.0.0

### v5.3.0 (January 28, 2026)
- **Document Consolidation**: Reduced from 7 → 4 documents
  - SDLC-Quality-Gates.md + SDLC-Security-Gates.md → **SDLC-Quality-Gates-Assurance-Framework.md**
  - SDLC-Sprint-Planning-Governance.md + SDLC-Stage-Sprint-Integration.md + SDLC-Change-Management-Standard.md → **SDLC-Sprint-Governance.md**
- **Pillar 7: Quality Assurance System** - Anti-Vibecoding governance integration
- Added Vibecoding Index, Progressive Routing references
- Updated to 8-Pillar Architecture structure
- Stage Dependency Matrix integration

### v5.2.0 (January 2026)
- AI Governance integration (aligned with 03-AI-GOVERNANCE principles)
- Added Verification-First and Human Accountability references
- Updated to principle-centric framework structure

### v5.1.3 (January 2026)
- Restructured around Pillar 2, 4, 5 integration
- Added Pillar Integration Map diagram
- Added 10 Golden Rules summary
- Added Dual-Track Quality Gates explanation
- Added SASE Integration by Stage table

### v5.1.2 (December 2025)
- Initial governance folder structure

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for all SDLC projects
**Last Updated**: February 16, 2026
**Owner**: CTO + CPO Office
