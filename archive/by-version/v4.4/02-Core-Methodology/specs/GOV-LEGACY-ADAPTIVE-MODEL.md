# GOV-LEGACY-ADAPTIVE-MODEL – Legacy Artifact Governance & Adaptive Transition Model
Status: DRAFT (Phase B – Curation Execution)
Version: 0.7
Last Updated: 2025-09-16
Owner: CPO Governance Office (CTO Technical Steward)

---

## 1. Purpose

Define governance model for historical SDLC versions (1.x–4.3) under 4.4 Adaptive Governance to ensure: (a) canonical single source per version, (b) integrity + traceability, (c) guided migration, (d) noise reduction.

## 2. Objectives

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| Canonicalization | Exactly one authoritative artifact per category/version | 100% uniqueness table compliance |
| Supersede Clarity | Users instantly see status (Active / Superseded / Historical) | <10s average navigation decision |
| Guided Selection | Teams adopt correct baseline (≥4.4 unless exception) | ≥95% new teams start on 4.4 |
| Integrity Prep | Structure supports future hash chain + drift link | Ledger ingestion <5m |

## 3. Classification Model

| Class | Label | Usage Allowed | Examples |
|-------|-------|--------------|----------|
| ACTIVE | Current normative baseline | Full | 4.4 Core Principles (outside legacy) |
| SUPERSEDED | Replaced by newer major/minor | Read-only reference | 4.3 Implementation Guide |
| HISTORICAL | Architectural / cultural lineage only | Contextual research | 1.x Comprehensive Guide |
| TRANSITIONAL | Temporary staging during migration | Limited editing (≤30 days) | Temporary dual-weight docs |

## 4. Supersede Banner Pattern

Applied at top of each legacy file (insert after H1 or add H1 if missing):

```text
> [!IMPORTANT] SUPERSSEDED – This document belongs to SDLC {VERSION}. It has been superseded by SDLC 4.4 Adaptive Governance. Use only for historical reference unless an approved migration plan cites this version.
```

Historical variant:

```text
> [!NOTE] HISTORICAL – Pre-modern AI-native evolution artifact. Not for operational adoption.
```

## 5. Canonical Mapping (Derived from LEGACY-VERSION-INDEX)

| Version | Core Principles | Implementation Guide | Training | Deployment | Controls |
|---------|-----------------|----------------------|----------|------------|----------|
| 4.3 | SDLC-4.3-Core-Principles.md | SDLC-4.3-IMPLEMENTATION-GUIDE.md | SDLC-4.3-Training-Framework.md | SDLC-4.3-Deployment-Framework.md | (NONE – use 4.2 controls) |
| 4.2 | SDLC-4.2-Core-Principles.md | SDLC-4.2-IMPLEMENTATION-GUIDE.md | SDLC-4.2-Training-Framework.md | SDLC-4.2-Deployment-Framework.md | FRAMEWORK-CONTROLS-4.2.md |
| 4.1 | SDLC-4.1-Core-Principles.md | SDLC-4.1-IMPLEMENTATION-GUIDE.md | SDLC-4.1-Training-Framework.md | SDLC-4.1-Deployment-Framework.md | FRAMEWORK-CONTROLS-4.1.md |
| 4.0 | SDLC-4.0-Core-Principles.md | SDLC-4.0-IMPLEMENTATION-GUIDE.md | SDLC-4.0-Training-Framework.md | SDLC-4.0-Deployment-Framework.md | FRAMEWORK-CONTROLS-4.0.md |
| 3.x | SDLC-3.x-COMPREHENSIVE-GUIDE.md | (Consolidated) | (Embedded) | (Embedded) | (Embedded) |
| 2.x | SDLC-2.x-COMPREHENSIVE-GUIDE.md | (Embedded) | (Embedded) | (Embedded) | (Embedded) |
| 1.x | SDLC-1.x-COMPREHENSIVE-GUIDE.md | (Embedded) | (Embedded) | (Embedded) | (Embedded) |

## 6. Governance Controls

| Control | Rule | Enforcement Mode |
|---------|------|------------------|
| LC-01 Canonical Single Source | Duplicate functional docs removed or redirected | Manual review (Phase B) |
| LC-02 Supersede Banner | All superseded files contain banner block | Shadow scan script (planned) |
| LC-03 Historical Isolation | Historical class files must not claim active status | Manual + future lint |
| LC-04 No Forward Drift | Legacy doc must not describe features exclusive to newer versions | Manual spot review |
| LC-05 Selection Guide Link | Legacy README must link `VERSION-SELECTION-GUIDE.md` | Verified (DONE) |
| LC-06 Integrity Ledger Ready | Filenames stable & hashed snapshot committed | Phase C |

## 7. Migration Decision Flow

1. New team? → Adopt 4.4 immediately.  
2. Existing on 4.3 with active delivery? → Plan upgrade within 2 sprints (use dual-weight continuity shadow).  
3. On ≤4.2? → Execute staged migration: (a) 4.2 → 4.3 (role consolidation), (b) 4.3 → 4.4 (adaptive layer).  
4. On ≤3.x? → Re-baseline; do not extend legacy line.  

## 8. Exception Policy

| Case | Allowed? | Requirement | Max Duration |
|------|----------|-------------|--------------|
| Security Hotfix on 4.3 | Yes | CPO approval + backport plan | 14 days |
| New Feature targeting <4.4 | No | Must upgrade first | N/A |
| Regulatory Freeze (cannot switch) | Conditional | Documented defer + timeline | 30 days |

## 9. Integrity & Hash Plan

Future file: `99-Legacy/LEGACY-INTEGRITY-LEDGER.jsonl`

Entry schema:

```json
{"ts":"2025-09-20T00:00:00Z","path":"99-Legacy/SDLC-4.2-Core-Principles.md","sha256":"...","supersede_class":"SUPERSEDED"}
```

Rotation cadence: weekly or post structural change.

## 10. Automation Roadmap

| Phase | Script | Function |
|-------|--------|----------|
| B | banner_inject.py | Insert banners idempotently |
| C | legacy_hash_seed.py | Generate initial hash ledger |
| C | legacy_scan.py | Verify compliance with LC controls |
| D | drift_linker.py | Attach drift metrics per file |

## 11. Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Missed Banner | User misinterprets status | Idempotent batch injector |
| Unauthorized Edit of Superseded | Silent divergence | Hash ledger delta alerts |
| Over-Retention Noise | Slower decision cycle | Canonical mapping review quarterly |

## 12. Acceptance Checklist

- [x] Canonical table present  
- [x] Supersede banner pattern documented  
- [x] Exception policy defined  
- [ ] Banners injected into 4.0–4.3 files  
- [ ] CHANGELOG cross-link  
- [ ] Hash ledger created (placeholder)  

---
END OF SPEC
