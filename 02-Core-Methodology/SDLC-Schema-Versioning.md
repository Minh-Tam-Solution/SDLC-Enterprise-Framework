# SDLC Framework Versioning Rules

**Version**: 1.1.0 *(doc's own semver — independent of Framework version; see [§Document Version Convention](#document-version-convention-convention-a--formalized-amendment-b-2026-06-03) below)*
**Effective Date**: 2026-01-28
**Last Updated**: 2026-06-03 (added §"Document Version Convention (Convention A)" per Amendment B + MM#9 — see CHANGELOG v6.3.2)
**SDLC Framework Version**: 6.3.2

---

## Overview

This document defines versioning rules for the SDLC Enterprise Framework and its machine-readable specifications:
- `02-Core-Methodology/Governance-Compliance/*.yaml` - Controls and gates
- `05-Templates-Tools/01-Specification-Standard/*.json` - JSON Schema validations

## Framework Version (Semantic Versioning)

The Framework follows [Semantic Versioning 2.0.0](https://semver.org/):

```
MAJOR.MINOR.PATCH
```

### Version Components

- **MAJOR**: Breaking changes to core methodology
  - Examples: Restructuring pillar system, removing/renaming stages
  - Impact: Existing documentation may need significant updates
  - Frequency: Rarely (years between major versions)

- **MINOR**: New features, backward compatible
  - Examples: Adding new templates, new quality gates, new tier requirements
  - Impact: Existing projects can adopt new features optionally
  - Frequency: Quarterly

- **PATCH**: Bug fixes, clarifications
  - Examples: Typo fixes, clarified wording, updated examples
  - Impact: No functional changes
  - Frequency: As needed

### Current Version

- **Framework Version**: 6.3.2 (Production — Amendment B: Ship-Useful Principle + MM#9)
- **Release**: June 3, 2026 (Amendment B PATCH; 6.3.1 originated April 17, 2026)
- **Status**: ACTIVE

## Document Version Convention (Convention A — Formalized Amendment B, 2026-06-03)

> **Authority**: CEO ratified 2026-06-03 (Amendment B, Framework 6.3.2). This convention resolves the per-doc Version vs Framework Version mismatch pattern surfaced during Amendment B sync. **Convention A is the standard going forward; Convention B (blanket-bump on Framework patch) is explicitly rejected because it would have the Framework violating MM#9 — Demand Before Surface (the very principle Amendment B added).**

### What Convention A says

Every Framework document carries TWO independent version markers in its header. They MAY differ — and frequently SHOULD.

| Field | Purpose | When it changes |
|-------|---------|----------------|
| `**Version**: X.Y.Z` (per-doc semver) | The document's OWN version. Tracks substantive edits to THIS specific doc. | ONLY when the doc body is substantively revised. PATCH for clarifications/typos; MINOR for new sections; MAJOR for restructuring or breaking-meaning changes. |
| `sdlc_framework: "X.Y.Z"` (YAML frontmatter) OR `**SDLC Framework Version**: X.Y.Z` (markdown) | Which Framework version this doc was last **validated against** | ONLY when the doc was substantively reviewed/validated against a new Framework version. Does NOT blanket-bump on every Framework patch. |

### Canonical field name

Going forward, the canonical field is the YAML frontmatter:

```yaml
---
sdlc_framework: "6.3.2"
---
```

Existing markdown patterns (`**Framework**: SDLC X.Y.Z`, `**SDLC Framework Version**: X.Y.Z`) remain valid for backward compatibility but should be migrated to the YAML form when a doc is otherwise substantively edited. **Mass-migration of field names alone is explicitly NOT required** (per MM#9 — no daily-user for the rename).

### Why the two fields differ honestly

A Framework PATCH (e.g., 6.3.1 → 6.3.2 Amendment B) means:

- The **Framework methodology** advances at the new version.
- The **Framework documentation surface** does NOT automatically advance — only the docs whose bodies actually integrate the patch content do.

**Example: Amendment B (Framework 6.3.2)**

- `02-Core-Methodology/SDLC-System-Thinking-Foundation.md` substantively adds MM#9 → `Version` bump + `sdlc_framework: 6.3.2`. Both reflect real change.
- `02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md` was NOT substantively changed by Amendment B → `Version` stays at its prior semver + `sdlc_framework` stays at whatever it was last validated against. **Honest content-state signal.**

A blanket bump of every doc's `sdlc_framework` field to `"6.3.2"` (without body validation) would create false-update claims and violate MM#9 ("no surface ships without named daily-user / job / re-eval"). The reader of an unchanged doc gets the lie "this doc was updated for 6.3.2" when it wasn't.

### Convention A in practice

| Scenario | per-doc `Version` | `sdlc_framework` |
|----------|-------------------|------------------|
| Doc substantively edited for new Framework patch | Bump (semver) | Bump to new Framework version |
| Doc unchanged; Framework patches | **Stay** | **Stay** (last validated version) |
| Doc edited for typo/clarification only; no Framework dependency | PATCH bump | Stay |
| Doc body content references old Framework version (e.g., body discusses Pillar 3 changes from 6.0.5) | Stay | Stay (last validated; honest "this doc is from era X") |
| New doc authored | 1.0.0 | Current Framework version at author time |

### What this convention rejects

- **Blanket-bump every doc on Framework patch** (Convention B) — anti-MM#9; creates false-update claims; reader-misleading
- **Header-only updates without body changes** (anti-pattern surfaced 2026-06-03) — exactly the Mistake 3 "Partial Content Updates" warned about in SDLC-Continuous-Improvement-Guide
- **`[Current Date]` template placeholders never filled** (pre-existing debt; fixed 2026-06-03 sweep) — these should be filled with the file's git-mtime (when the doc was last actually edited), not "today"
- **Per-doc `Version` field used as Framework-alignment proxy** — these are SEPARATE concerns

### When in doubt

> When a doc has not been substantively reviewed for the new Framework version, **leave both version markers as they are**. Honest staleness > inflated freshness.

This is the OSS-community-credibility posture: readers can trust that the Framework's own docs honestly reflect their authoring/validation state.

### References

- Amendment B (Framework 6.3.2) CHANGELOG entry — documents the originating decision
- MM#9 (Demand Before Surface) in `SDLC-System-Thinking-Foundation.md` — the principle this convention serves
- `SDLC-Ship-Useful-Principle.md` — Anti-Theater Catalog Mistake 3 "Partial Content Updates"

---

## Schema Version (Independent Versioning)

Each schema in `/spec/` declares its own `schema_version` field and follows semantic versioning independently:

```yaml
metadata:
  schema_version: "1.0.0"
  framework_compatibility: ">=6.0.0"
```

### Schema Versioning Rules

- Schemas can evolve independently of Framework major versions
- Breaking schema changes require 2-sprint deprecation window
- Old schema versions remain available for backward compatibility

### Example: spec-frontmatter-schema.json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://sdlc-framework.org/spec/evidence/frontmatter/v1",
  "version": "1.0.0"
}
```

**Version History**:
- `1.0.0` (2026-01-28): Initial spec-first POC release

## Compatibility Matrix

| Framework Version | Minimum Schema Version | Notes |
|-------------------|------------------------|-------|
| 6.x | schema_version >= 1.0.0 | Spec-first architecture introduced |
| 7.x | schema_version >= 2.0.0 | Future: Breaking schema changes expected |

### Breaking Schema Changes

When a schema requires breaking changes:

1. **Sprint N**: Announce deprecation in CHANGELOG.md
2. **Sprint N+1**: Mark old version as deprecated in schema
3. **Sprint N+2**: Release new schema version, remove old version
4. **Tooling**: Update validators to support both versions during transition

## Schema Reference in Specifications

Specifications should reference schemas with version pinning:

```markdown
---
spec_id: "SPEC-0001"
title: "Anti-Vibecoding Specification"
version: "1.0.0"
schema_ref: "spec/evidence/spec-frontmatter-schema.json@1.0.0"
---
```

### Version Pinning Format

```
<path>/<schema-file>.json@<version>
```

**Examples**:
- `spec/evidence/spec-frontmatter-schema.json@1.0.0`
- `spec/controls/anti-vibecoding.yaml@1.0.0`
- `spec/gates/gates.yaml@1.0.0`

## Backward Compatibility Policy

### Framework Level

- **MAJOR versions**: May introduce breaking changes (2+ sprints notice)
- **MINOR versions**: Always backward compatible
- **PATCH versions**: Always backward compatible

### Schema Level

- **Breaking changes**: Require new major version (1.x → 2.x)
- **New optional fields**: Allowed in minor versions (1.0 → 1.1)
- **Bug fixes**: Patch versions (1.0.0 → 1.0.1)

### Deprecation Process

1. **Announcement**: Document deprecation in CHANGELOG.md
2. **Warning Period**: 2 sprints minimum (4-6 weeks)
3. **Migration Guide**: Provide clear upgrade path
4. **Removal**: After warning period expires

## Validation

### Schema Version Validation

Tools implementing SDLC Framework MUST validate:

1. Schema version compatibility with Framework version
2. Required fields match schema version
3. Deprecated fields trigger warnings
4. Unknown fields trigger warnings (forward compatibility)

### Example Validation Error

```
ERROR: Specification SPEC-0001 requires schema_version 1.0.0
       but Framework 7.0 requires schema_version >= 2.0.0

ACTION: Update specification frontmatter or upgrade schema
```

## Version Upgrade Path

### Framework 5.3.0 → 6.0

**Changes** (In Progress):
- Added `/spec/` directory with machine-readable schemas
- Introduction of spec-first architecture
- Enhanced quality assurance system (Anti-Vibecoding)
- No breaking changes to existing methodology
- Backward compatible

**Migration**:
- Optional: Add YAML frontmatter to specifications
- Optional: Adopt machine-readable gate definitions
- Existing 5.3.0 documentation remains valid

### Future: Framework 6.0 → 6.1

**Expected Changes** (Planned):
- Additional machine-readable schemas
- Expanded control definitions
- Enhanced gate validation rules

**Migration Path**:
- Backward compatible minor version
- No breaking changes expected
- Optional adoption of new features

### Future: Framework 6.x → 7.0

**Expected Changes** (Hypothetical):
- Major pillar restructuring
- New compliance tier requirements
- Breaking schema changes (schema_version 2.0.0)

**Migration Path** (Will be documented when planned):
- Detailed migration guide provided
- Automated migration tools released
- 2+ sprint transition period

## References

- [Semantic Versioning 2.0.0](https://semver.org/)
- [JSON Schema Versioning Best Practices](https://json-schema.org/blog)
- Framework CHANGELOG: `/CHANGELOG.md`
- Spec Directory: `/spec/`

---

**Last Updated**: 2026-06-03 (Amendment B added Document Version Convention §)
**Status**: Active
**Next Review**: 2026-Q3
