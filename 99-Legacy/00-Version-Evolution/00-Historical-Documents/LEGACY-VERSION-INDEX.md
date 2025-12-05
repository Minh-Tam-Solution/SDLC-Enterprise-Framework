# LEGACY VERSION INDEX

> Canonical mapping of preserved SDLC framework versions (1.x → 4.3) and their primary artifacts. Use with `VERSION-SELECTION-GUIDE.md` to decide adoption path or for historical traceability.

```text
INDEX STATUS: ACTIVE
MAINTAINER: CPO Office
LAST UPDATED: 2025-09-16
SCOPE: Versions 1.x, 2.x, 3.x, 4.0, 4.1, 4.2, 4.3 (superseded by 4.4 adaptive governance)
CANONICAL RULE: One primary representative artifact per artifact class per version.
```

## 1. Canonical Version Table

| Version | Lifecycle | Canonical Executive Summary | Canonical Implementation Guide | Training Framework | Core Principles | Controls/Checklist | Deployment Framework | Notable Innovations |
|---------|-----------|-----------------------------|--------------------------------|--------------------|-----------------|--------------------|----------------------|---------------------|
| 1.x | Historical | `SDLC-1.x-COMPREHENSIVE-GUIDE.md` (Exec section) | `SDLC-1.x-COMPREHENSIVE-GUIDE.md` | (Embedded) | (Embedded) | N/A | N/A | AI-Native foundation, role emergence |
| 2.x | Historical | `SDLC-2.x-COMPREHENSIVE-GUIDE.md` (Exec section) | `SDLC-2.x-COMPREHENSIVE-GUIDE.md` | (Embedded) | (Embedded) | N/A | N/A | AI active agile participation |
| 3.x | Historical | `SDLC-3.x-COMPREHENSIVE-GUIDE.md` (Exec section) | `SDLC-3.x-COMPREHENSIVE-GUIDE.md` | (Embedded) | (Embedded) | N/A | N/A | Scientific Org Standard (SOS) |
| 4.0 | Superseded | `SDLC-4.0-Executive-Summary.md` | `SDLC-4.0-IMPLEMENTATION-GUIDE.md` | `SDLC-4.0-Training-Framework.md` | `SDLC-4.0-Core-Principles.md` | `FRAMEWORK-CONTROLS-4.0.md` | `SDLC-4.0-Deployment-Framework.md` | Universal roles (initial), baseline controls |
| 4.1 | Superseded | `SDLC-4.1-Executive-Summary.md` | `SDLC-4.1-IMPLEMENTATION-GUIDE.md` | `SDLC-4.1-Training-Framework.md` | `SDLC-4.1-Core-Principles.md` | `FRAMEWORK-CONTROLS-4.1.md` | `SDLC-4.1-Deployment-Framework.md` | Expanded governance, refinements |
| 4.2 | Superseded | `SDLC-4.2-Executive-Summary.md` | `SDLC-4.2-IMPLEMENTATION-GUIDE.md` | `SDLC-4.2-Training-Framework.md` | `SDLC-4.2-Core-Principles.md` | `FRAMEWORK-CONTROLS-4.2.md` + `SDLC-4.2-COMPLIANCE-CHECKLIST.md` | `SDLC-4.2-Deployment-Framework.md` | Cultural intelligence integration |
| 4.3 | Superseded | (In 4.4 Executive Review backwards mapping) | (Archived within 4.4 transition docs) | (Replaced by 4.4 adaptive training) | (Replaced) | (Rolled into adaptive controls) | (Replaced) | Universal role-based execution maturity |
| 4.4 | Active | `01-Overview/SDLC-4.4-COMPREHENSIVE-EXECUTIVE-REVIEW.md` | `03-Implementation-Guides/ADOPTION-GUIDE.md` (plus adaptive specs) | `04-Training-Materials/` adaptive set | `02-Core-Methodology/` adaptive set | `specs/` governance specs set | `05-Deployment-Toolkit/` adaptive | Adaptive governance intelligence |

## 2. Supersede & Canonical Selection Rules

1. Single canonical artifact per class per version to minimize maintenance surface.
2. If a COMPREHENSIVE-GUIDE exists, it supersedes fragmented exec/implementation docs for 1.x–3.x.
3. Version 4.x splits (Exec / Implementation / Training / Controls) retained individually due to structural maturity.
4. When adaptive (4.4) fully incorporates a prior artifact's scope, the legacy file is retained only if it contains unique historical rationale.
5. Backup or duplicate script READMEs (`scripts-README-*`) relegated to `99-Archive-Raw/` after rule application.

## 3. Deprecation Classes

| Class | Meaning | Action | Visual Marker |
|-------|---------|--------|---------------|
| Historical | Informational only | No edits; hash later | Header badge HISTORICAL |
| Superseded | Replaced by newer version | Add supersede note | Header badge SUPERSEDED |
| Transitional | Temporary bridging doc | Remove once merged | Header badge TRANSITIONAL |
| Active | Current authoritative | Maintain | Header badge ACTIVE |

## 4. Pending Normalization Actions

- Add supersede headers to all 4.0–4.3 canonical artifacts.
- Move script backup files to `99-Archive-Raw/`.
- Insert cross-links from each legacy version top to 4.4 adoption & selection guide.
- Add integrity hash placeholders (future continuity ledger integration).

## 5. Cross-Link Map (Planned)

| Legacy Version | Forward Link Target | Rationale |
|----------------|---------------------|-----------|
| 1.x | Version Selection Guide | Direct teams away from foundational prototype process |
| 2.x | Version Selection Guide | Encourage leap to adaptive or 3.x+ for quality gates |
| 3.x | Version Selection Guide | Show pathway to universal governance (4.x) |
| 4.0 | 4.4 Adoption Guide | Governance & controls uplift |
| 4.1 | 4.4 Adoption Guide | Incremental improvements absorbed |
| 4.2 | 4.4 Adoption Guide | Cultural & quality innovations integrated |
| 4.3 | 4.4 Executive Review | Fully subsumed by adaptive governance layer |

## 6. Integrity & Traceability Plan (Preview)

Future enhancement will:

- Apply SHA256 content hash chain recorded in `LEGACY-INTEGRITY-LEDGER.jsonl` (planned file).
- Link each canonical artifact header to its hash record.
- Provide drift detection deltas between canonical historical artifact and adaptive implementation snapshot.

---

*End of Index.*
