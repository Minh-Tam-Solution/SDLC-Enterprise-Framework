# Deprecated Governance-Compliance Documents (SDLC 5.2.0)

**Deprecated Date**: January 28, 2026
**Framework Version**: 5.3.0
**Reason**: Document consolidation for improved clarity

---

## Consolidation Summary

These documents were merged into consolidated versions in SDLC 5.3.0:

| Deprecated File | Merged Into | Location |
|----------------|-------------|----------|
| SDLC-Quality-Gates.md | **SDLC-Quality-Security-Gates.md** | `02-Core-Methodology/Governance-Compliance/` |
| SDLC-Security-Gates.md | **SDLC-Quality-Security-Gates.md** | `02-Core-Methodology/Governance-Compliance/` |
| SDLC-Sprint-Planning-Governance.md | **SDLC-Sprint-Governance.md** | `02-Core-Methodology/Governance-Compliance/` |
| SDLC-Stage-Sprint-Integration.md | **SDLC-Sprint-Governance.md** | `02-Core-Methodology/Governance-Compliance/` |
| SDLC-Change-Management-Standard.md | **SDLC-Sprint-Governance.md** | `02-Core-Methodology/Governance-Compliance/` |

---

## Migration Guide

### If you referenced SDLC-Quality-Gates.md:
**New location**: `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Security-Gates.md`
- Quality Requirements by Tier → Part 1
- Gate-Specific Requirements → Part 3
- DORA Metrics → Part 8
- Code Quality Thresholds → Part 12

### If you referenced SDLC-Security-Gates.md:
**New location**: `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Security-Gates.md`
- Security Requirements by Tier → Part 2
- SBOM → Part 4
- SAST Rules → Part 5
- OWASP ASVS → Part 6
- Threat Modeling → Part 7
- Incident Response → Part 9

### If you referenced SDLC-Sprint-Planning-Governance.md:
**New location**: `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md`
- 10 Golden Rules → Part 1
- G-Sprint Gates → Part 2
- SSOT Validation → Part 5
- Tier Requirements Matrix → Part 4

### If you referenced SDLC-Stage-Sprint-Integration.md:
**New location**: `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md`
- Multi-Stage Sprint Scenarios → Part 3
- Stage-Specific Responsibilities → Part 3
- Rollback Procedure → Part 3

### If you referenced SDLC-Change-Management-Standard.md:
**New location**: `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md`
- Change Types → Part 6
- Roadmap Change Request → Part 6
- Risk Scoring Matrix → Part 6
- Rollback Requirements → Part 6

---

## Why Consolidate?

1. **Reduced complexity**: 7 files → 4 files (43% reduction)
2. **Better discoverability**: Related content in single documents
3. **Eliminated duplication**: Sprint gates were duplicated across files
4. **Clearer navigation**: Pillar 2 + Pillar 4+5 clearly separated

---

**Last Updated**: January 28, 2026
**Framework Version**: SDLC 5.3.0
