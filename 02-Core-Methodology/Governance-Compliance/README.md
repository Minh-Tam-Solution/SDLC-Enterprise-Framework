# Governance & Compliance

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology
**Status**: ACTIVE - Production Standard
**Authority**: CTO + CPO Office

---

## Purpose

Define governance, quality, security, and compliance standards that are **core to SDLC methodology**. These standards apply to ALL projects using SDLC Framework.

---

## Documents in This Section

| Document | Purpose | Tier Required |
|----------|---------|---------------|
| [SDLC-Quality-Gates.md](./SDLC-Quality-Gates.md) | Code quality, test coverage, DORA metrics thresholds | ALL tiers |
| [SDLC-Security-Gates.md](./SDLC-Security-Gates.md) | SBOM, SAST, DAST, OWASP ASVS requirements | STANDARD+ |
| [SDLC-Observability-Checklist.md](./SDLC-Observability-Checklist.md) | Metrics, logging, tracing, alerting | PROFESSIONAL+ |
| [SDLC-Change-Management-Standard.md](./SDLC-Change-Management-Standard.md) | Change types, CAB process, rollback | PROFESSIONAL+ |

---

## Governance vs. Stage 09 (GOVERN)

| Aspect | 02-Core-Methodology/Governance-Compliance | 09-Executive-Reports (GOVERN Stage) |
|--------|-------------------------------------------|-------------------------------------|
| **Scope** | Standards & policies (HOW to comply) | Strategic oversight (WHAT to report) |
| **Audience** | All teams (mandatory compliance) | Executives, CTO/CPO (decision making) |
| **Content** | Quality gates, security gates, observability | Status reports, risk reports, financials |
| **When Used** | Every stage (continuous) | Stage 09 specific activities |

---

## Quick Start by Tier

### LITE Tier (1-2 people)
```yaml
Required:
  - Basic Quality Gates (manual code review)
  - README.md + .env.example

Optional:
  - Everything else
```

### STANDARD Tier (3-10 people)
```yaml
Required:
  - Quality Gates (CI/CD with linting, unit tests)
  - Security Gates (dependency scanning)
  - CLAUDE.md for AI onboarding

Recommended:
  - Basic observability (logging)
  - Change management (basic)
```

### PROFESSIONAL Tier (10-50 people)
```yaml
Required:
  - Full Quality Gates (80%+ coverage, DORA tracking)
  - Full Security Gates (SBOM, SAST, OWASP ASVS L1)
  - Full Observability (metrics, logs, traces)
  - Change Management (CAB-lite process)

Mandatory Documentation:
  - ADRs for architectural decisions
  - Full /docs structure (10 stages)
```

### ENTERPRISE Tier (50+ people)
```yaml
Required:
  - Everything in PROFESSIONAL
  - OWASP ASVS Level 2+
  - Full CAB process
  - 95%+ test coverage
  - Weekly CTO/CPO reports
  - Penetration testing

Audit Requirements:
  - Quarterly security audits
  - Annual compliance audits
  - Continuous compliance monitoring
```

---

## Related Documents

- [02-Core-Methodology/SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 10-stage framework
- [Documentation-Standards/Team-Collaboration/](../Documentation-Standards/Team-Collaboration/) - Team coordination
- [03-Templates-Tools/5-Project-Templates/](../../03-Templates-Tools/5-Project-Templates/) - Project templates

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for all SDLC projects
**Last Updated**: December 5, 2025
**Owner**: CTO + CPO Office
