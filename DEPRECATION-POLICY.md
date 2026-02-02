# SDLC Framework Deprecation Policy

**Version**: 6.0.2
**Status**: ACTIVE
**Date**: February 2, 2026
**Purpose**: Define redirect rules and deprecation procedures
**Framework**: SDLC 6.0.2 (7-Pillar + 2-Section)

---

## Overview

This policy ensures smooth transitions when restructuring Framework content.
Archive content instead of deleting. Leave redirect stubs at old locations.

---

## Redirect Stub Template

When moving or deprecating a file, create a stub at the original location:

```markdown
# [Original Title]

> ⚠️ **MOVED** (SDLC 5.2.0, January 2026)
>
> This content has moved to: [NEW LOCATION](../path/to/new/file.md)
>
> **Reason**: [Brief explanation - e.g., "Framework restructuring - principles consolidated into 03-AI-GOVERNANCE/"]
>
> This stub will be removed after [DATE - 6 months from move].

---

**Stub Created**: [Date]
**Removal Date**: [Date + 6 months]
**New Location**: [Full path]
```

---

## Deprecation Timeline

| Phase | Duration | Action |
|-------|----------|--------|
| Announcement | Day 0 | Mark as DEPRECATED in CONTENT-MAP.md |
| Redirect | Day 1 | Create redirect stub, move content |
| Grace Period | 6 months | Stub active, users redirected |
| Removal | Month 7 | Delete stub, update CONTENT-MAP.md |

---

## Archive Naming Convention

```
99-ARCHIVE/
├── tool-guides-2026/           # Tool-specific content archived Jan 2026
│   ├── README.md               # Archive index with context
│   ├── claude-code/            # Full folder preserved
│   ├── cursor/
│   ├── copilot/
│   ├── chatgpt/
│   └── gemini/
├── deprecated-artifacts-2026/  # Deprecated SASE artifacts
│   ├── BRS-BriefingScript/
│   ├── MTS-MentorScript/
│   └── LPS-LoopScript/
└── version-X.Y.Z/              # Full version snapshots (if needed)
```

---

## When to Deprecate vs Archive

| Scenario | Action | Example |
|----------|--------|---------|
| Content outdated but historically useful | Archive | Old version guides |
| Content replaced by better alternative | Deprecate + Redirect | MTS → AGENTS.md |
| Content wrong or dangerous | Delete immediately | Security vulnerabilities |
| Tool-specific content | Archive with date | Claude Code templates |
| Principle extracted to Core | Redirect stub | planning-mode.md → Principle |

---

## CI/CD Integration

### Link Checker (Required)

```yaml
# .github/workflows/link-checker.yml
name: Link Checker
on:
  push:
    paths: ['**.md']
  pull_request:
    paths: ['**.md']

jobs:
  check-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check markdown links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          folder-path: 'SDLC-Enterprise-Framework/'
          config-file: '.markdown-link-check.json'
```

### Link Check Config

```json
// .markdown-link-check.json
{
  "ignorePatterns": [
    { "pattern": "^http://localhost" },
    { "pattern": "^https://internal" }
  ],
  "replacementPatterns": [],
  "aliveStatusCodes": [200, 206],
  "retryOn429": true,
  "retryCount": 2
}
```

---

## Stub Expiration Tracking

Maintain in CONTENT-MAP.md under "Active Redirect Stubs":

| Original Location | New Location | Created | Expires |
|------------------|--------------|---------|---------|
| `2-Agent-Templates/claude-code/` | `99-ARCHIVE/tool-guides-2026/claude-code/` | Jan 2026 | Jul 2026 |

---

## Responsibilities

| Role | Responsibility |
|------|---------------|
| **File Mover** | Create redirect stub, update CONTENT-MAP.md |
| **PR Reviewer** | Verify stub exists, check links |
| **CI/CD** | Block merge if links broken |
| **Monthly Review** | Check for expired stubs, remove them |

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: January 22, 2026
