# SDLC Framework Versioning Rules

**Version**: 1.0.1
**Effective Date**: 2026-01-28
**Last Updated**: 2026-01-29

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

- **Framework Version**: 6.1.1 (Production)
- **Release**: February 16, 2026
- **Status**: ACTIVE

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

**Last Updated**: 2026-01-28
**Status**: Active
**Next Review**: 2026-Q2
