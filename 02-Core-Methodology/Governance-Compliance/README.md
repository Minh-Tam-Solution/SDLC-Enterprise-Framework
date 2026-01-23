# Governance & Compliance Standards

**Version**: 5.2.0
**Date**: January 22, 2026
**Stage**: 02 - Core Methodology
**Pillar**: 2 - Sprint Planning Governance × Pillar 4 - Quality Gates × Pillar 5 - SASE Integration
**Status**: ACTIVE - Production Standard
**Authority**: CTO + CPO Office
**AI Governance**: Aligned with 03-AI-GOVERNANCE principles (Verification-First, Human Accountability)

---

## Purpose

Define governance, quality, security, and compliance standards that form the **core pillars of SDLC 5.2.0**:

| Pillar | Document | Focus |
|--------|----------|-------|
| **Pillar 2** | SDLC-Sprint-Planning-Governance.md | Sprint execution governance |
| **Pillar 4** | SDLC-Quality-Gates.md | Feature gates (G0-G4) & Sprint gates |
| **Pillar 5** | SDLC-Security-Gates.md | Security throughout lifecycle |

---

## Documents in This Section

| Document | Pillar | Purpose | Tier Required |
|----------|--------|---------|---------------|
| [SDLC-Sprint-Planning-Governance.md](./SDLC-Sprint-Planning-Governance.md) | **Pillar 2** | Planning Hierarchy, 10 Golden Rules, Sprint gates | ALL tiers |
| [SDLC-Quality-Gates.md](./SDLC-Quality-Gates.md) | **Pillar 4** | Dual-Track Quality Gates (G0-G4 + G-Sprint) | ALL tiers |
| [SDLC-Security-Gates.md](./SDLC-Security-Gates.md) | **Pillar 5** | SBOM, SAST, DAST, OWASP ASVS | STANDARD+ |
| [SDLC-Observability-Checklist.md](./SDLC-Observability-Checklist.md) | Supporting | Metrics, logging, tracing, alerting | PROFESSIONAL+ |
| [SDLC-Change-Management-Standard.md](./SDLC-Change-Management-Standard.md) | **Pillar 2** | Change types, CAB process, rollback | PROFESSIONAL+ |

---

## Pillar Integration Map

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE & COMPLIANCE PILLARS                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │ Pillar 2: Sprint Planning Governance                          │     │
│  │ ┌─────────────────────────────────────────────────────────┐   │     │
│  │ │ Planning Hierarchy: Roadmap → Phase → Sprint → Backlog  │   │     │
│  │ │ 10 Golden Rules                                         │   │     │
│  │ │ Sprint Gates: G-Sprint (Start) + G-Sprint-Close (End)   │   │     │
│  │ └─────────────────────────────────────────────────────────┘   │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                              │                                          │
│                              ▼                                          │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │ Pillar 4: Quality Gates (Dual-Track)                          │     │
│  │ ┌─────────────────────┐   ┌──────────────────────────────┐   │     │
│  │ │ Feature Track       │   │ Sprint Track                 │   │     │
│  │ │ G0: Ideation        │   │ G-Sprint: Sprint Start       │   │     │
│  │ │ G1: Planning        │   │ G-Sprint-Close: Sprint End   │   │     │
│  │ │ G2: Design          │   │                              │   │     │
│  │ │ G3: Development     │   │ (per-sprint quality          │   │     │
│  │ │ G4: Production      │   │  verification)               │   │     │
│  │ └─────────────────────┘   └──────────────────────────────┘   │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                              │                                          │
│                              ▼                                          │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │ Pillar 5: SASE Integration                                    │     │
│  │ ┌─────────────────────────────────────────────────────────┐   │     │
│  │ │ Security THROUGHOUT lifecycle, not bolted on            │   │     │
│  │ │ SBOM, SAST, DAST, Secret scanning at every stage        │   │     │
│  │ │ OWASP ASVS compliance by tier                           │   │     │
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

- [SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 7-Pillar Architecture
- [Documentation-Standards/](../Documentation-Standards/) - Pillar 6 standards
- [Documentation-Standards/Team-Collaboration/](../Documentation-Standards/Team-Collaboration/) - Team coordination
- [Situation-Specific-Guides/When-Planning-Sprint.md](../Documentation-Standards/Situation-Specific-Guides/When-Planning-Sprint.md) - Sprint planning guide

---

## Changelog

### v5.2.0 (January 2026)
- AI Governance integration (aligned with 03-AI-GOVERNANCE principles)
- Added Verification-First and Human Accountability references
- Updated to principle-centric framework structure

### v5.1.3 (January 2025)
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
**Last Updated**: January 22, 2026
**Owner**: CTO + CPO Office
