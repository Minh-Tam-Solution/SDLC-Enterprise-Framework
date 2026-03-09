# 10-archive: Centralized Legacy Content

**Version**: 6.0.6
**Status**: AI-NEVER-READ
**Date**: February 13, 2026
**Standard**: RFC-001 Legacy Document Organization

---

## AI-NEVER-READ Directive

```yaml
directive: AI-NEVER-READ
reason: Contains archived, deprecated, and historical content
exception: User explicitly requests historical information
```

**AI assistants MUST NOT read content from this folder unless specifically requested by the user.**

---

## Structure

Stage-aligned subdirectories preserve lineage to original SDLC stages:

```
10-archive/
├── README.md           # This file (AI-NEVER-READ)
├── 00-Legacy/          # From Stage 00 (Foundation) - Version evolution
├── 01-Legacy/          # From Stage 01 (Planning) - Implementation scripts
├── 02-Legacy/          # From Stage 02 (Design) - Validation tools, deprecated specs
├── 04-Legacy/          # From Stage 04 (Build) - Sprint POCs
├── 05-Legacy/          # From Stage 05 (Templates) - Tool guides, SASE artifacts
├── 06-Legacy/          # From Stage 06 (Deploy) - Deployment guides
└── 09-Legacy/          # From Stage 09 (Govern) - Deprecated RFCs, scripts
```

---

## Archive Policy

- **Move, don't delete**: Documents are archived, never deleted
- **Stage alignment**: Archive subdirectory matches original stage number
- **No active references**: Active docs should not link to archived content
- **Periodic review**: Quarterly cleanup cadence

---

**Owner**: CTO Office
**Last Updated**: February 13, 2026
