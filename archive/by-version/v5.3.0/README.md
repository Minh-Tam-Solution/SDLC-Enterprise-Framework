# SDLC Framework 5.3.0 Archive

**Archived Date**: January 28, 2026
**Archived By**: PM/PJM Team
**Reason**: Major version upgrade to 6.0.0 (Unified Specification Standard)

---

## Archive Purpose

This folder preserves SDLC Framework 5.3.0 state before the major upgrade to 6.0.0.

### Why Archive?

**5.3.0 → 6.0.0 is a MAJOR version jump** with breaking changes:

| Aspect | 5.3.0 | 6.0.0 |
|--------|-------|-------|
| **Spec Format** | Free-form markdown | YAML frontmatter required |
| **Requirements** | Prose format | BDD (GIVEN-WHEN-THEN) required |
| **Design Decisions** | Full ADRs only | Lightweight DD + full ADR |
| **Version Tracking** | CHANGELOG only | SPEC_DELTA.md per spec |
| **AGENTS.md** | Static | Dynamic (4 zones) |

### Breaking Changes in 6.0.0

1. **All new specs MUST use YAML frontmatter**
   - `spec_id`, `tier`, `stage`, `status` required
   - Old format specs will fail validation

2. **BDD requirements format MANDATORY**
   - GIVEN-WHEN-THEN syntax required
   - Prose requirements deprecated

3. **Tier awareness required**
   - Each spec must declare target tier
   - Tier-specific validation enforced

---

## Archived Documents

### Core 5.3.0 Features (Preserved)

| Document | Path | Description |
|----------|------|-------------|
| Stage Dependencies | `SDLC-Stage-Dependencies.md` | ADR-041, explicit prerequisites |
| Stage Exit Criteria | `SDLC-Stage-Exit-Criteria.md` | Per-tier documentation requirements |
| Sprint-Stage Integration | `SDLC-Stage-Sprint-Integration.md` | Multi-stage sprint handling |
| Quality Assurance System | `SDLC-Quality-Assurance-System.md` | Section 7: Anti-Vibecoding |
| Tier Stage Requirements | `SDLC-Tier-Stage-Requirements.md` | LITE/PRO/ENTERPRISE guidance |

### 5.3.0 → 6.0.0 Migration

**What Changed:**
- 5.3.0 established **governance foundation** (stages, tiers, quality assurance)
- 6.0.0 adds **specification foundation** (unified format, BDD, design decisions)

**Migration Path:**
- Existing 5.3.0 specs: Remain valid, migrate incrementally
- New specs: Must use 6.0.0 format immediately
- `sdlcctl spec convert`: Automates format migration

---

## Version Timeline

```
5.0.0 (Dec 5, 2025)   → 4-Tier Classification
5.1.0 (Dec 11, 2025)  → SASE integration
5.2.0 (Jan 22, 2026)  → AI Governance Principles
5.3.0 (Jan 28, 2026)  → Stage Dependencies + Quality Assurance  ← ARCHIVED
6.0.0 (Jan 28, 2026)  → Unified Specification Standard ← CURRENT
```

---

## Restoration Instructions

If rollback to 5.3.0 is needed:

```bash
# 1. Check archived documents
ls SDLC-Enterprise-Framework/99-Legacy/v5.3.0-Archive/

# 2. Compare with current version
diff -r v5.3.0-Archive/documents/ 02-Core-Methodology/

# 3. Restore specific document
cp v5.3.0-Archive/documents/SDLC-Stage-Dependencies.md 02-Core-Methodology/
```

---

## Archive Manifest

| File | Original Location | Size | Checksum |
|------|-------------------|------|----------|
| README-5.3.0-snapshot.md | README.md | - | - |
| VERSION-5.3.0 | (marker file) | - | - |

---

*SDLC Enterprise Framework - Legacy Archive*
*Maintained by CPO Office*
