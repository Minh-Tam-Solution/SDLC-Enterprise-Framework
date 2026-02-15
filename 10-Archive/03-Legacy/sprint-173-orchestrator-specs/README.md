# Migrated: Orchestrator-Specific Specifications

**Originally Archived**: Sprint 173 (February 15, 2026)
**Migrated to Orchestrator**: February 15, 2026
**Reason**: These SPECs describe **SDLC Orchestrator platform implementation**, not Framework methodology.

## What Happened

The SDLC Framework follows a **3-ring Concentric Circles architecture**:
- **Core (Inner)**: Timeless principles
- **Governance (Middle)**: Stable rules
- **Outer Ring**: Tool-specific content

16 Orchestrator-specific SPEC files were removed from the Framework and placed into the correct **10-Stage lifecycle folders** in `SDLC-Orchestrator/docs/`:

| SPEC | Orchestrator Stage | Target Path |
|------|-------------------|-------------|
| SPEC-0003 | 02-DESIGN | `docs/02-design/02-System-Architecture/` |
| SPEC-0005 | 02-DESIGN | `docs/02-design/02-System-Architecture/` (pre-existing) |
| SPEC-0006 | 02-DESIGN | `docs/02-design/02-System-Architecture/` |
| SPEC-0007 | 02-DESIGN | `docs/02-design/01-ADRs/` (pre-existing) |
| SPEC-0009 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` (pre-existing) |
| SPEC-0010 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` (pre-existing) |
| SPEC-0011 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` |
| SPEC-0013 | 02-DESIGN | `docs/02-design/03-Database-Design/` |
| SPEC-0014 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` |
| SPEC-0015 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` |
| SPEC-0016 | 03-INTEGRATE | `docs/03-integrate/03-Integration-Guides/` |
| SPEC-0017 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` |
| SPEC-0018 | 04-BUILD | `docs/04-build/01-Development-Standards/` |
| SPEC-0019 | 05-TEST | `docs/05-test/01-Test-Strategy/` |
| SPEC-0020 | 02-DESIGN | `docs/02-design/14-Technical-Specs/` |
| SPEC-0021 | 05-TEST | `docs/05-test/01-Test-Strategy/` |

## Methodology SPECs Retained in Framework

| SPEC | Title | Why Framework-Level |
|------|-------|---------------------|
| SPEC-0001 | Anti-Vibecoding QA System | Defines methodology principle |
| SPEC-0002 | Specification Standard | Defines SPEC format itself |
| SPEC-0003 | Policy Guards Design | Defines policy enforcement pattern |
| SPEC-0004 | 4-Tier Policy Enforcement | Defines tier governance model |
| SPEC-0005 | Validation Pipeline Interface | Defines validation contract |
