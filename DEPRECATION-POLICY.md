# SDLC Framework Deprecation Policy

**Version**: 6.3.0
**Status**: ACTIVE
**Date**: March 18, 2026
**Purpose**: Define redirect rules and deprecation procedures
**Framework**: SDLC 6.3.0 (7-Pillar + 2-Section + RFC-001 + Lean Ring 1)

---

## Overview

This policy ensures smooth transitions when restructuring Framework content.
Archive content instead of deleting. Leave redirect stubs at old locations.

---

## Redirect Stub Template

When moving or deprecating a file, create a stub at the original location:

```markdown
# [Original Title]

> ⚠️ **MOVED** (SDLC 6.1.0, January 2026)
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

## Archive Naming Convention (RFC-001, SDLC 6.1.0)

All legacy content is centralized into **`10-archive/`** with stage-aligned subdirectories:

```
10-archive/
├── README.md                   # Archive index with AI-NEVER-READ directive
├── 00-Legacy/                  # Foundation archive (version evolution)
├── 01-Legacy/                  # Planning archive (implementation scripts)
├── 02-Legacy/                  # Design archive (validation tools, deprecated specs)
├── 04-Legacy/                  # Build archive (POC, sprint references)
├── 05-Legacy/                  # Tools archive (tool guides, SASE artifacts)
├── 06-Legacy/                  # Deploy archive (deployment guides)
└── 09-Legacy/                  # Govern archive (deprecated RFCs, scripts)
```

**Why 10-archive/{NN}-Legacy/**:
- Stage alignment: Archive subdirectory matches original stage (e.g., design specs → 02-Legacy)
- No polluting active stages: Eliminates 99-Legacy/ from stages 00-09
- AI-friendly: Centralized location with AI-NEVER-READ directive prevents context pollution
- Production-validated: Implemented on BFlow Platform (57% size reduction: 211MB→91MB)

See [RFC-001 Legacy Document Organization](#legacy-document-organization-rfc-001-sdlc-605) for details.

---

## When to Deprecate vs Archive

| Scenario | Action | Destination | Example |
|----------|--------|-------------|---------|
| Content outdated but historically useful | Archive | `10-archive/{NN}-Legacy/` | Old version guides |
| Content replaced by better alternative | Deprecate + Redirect | `10-archive/{NN}-Legacy/` | MTS → AGENTS.md |
| Content wrong or dangerous | Delete immediately | (none) | Security vulnerabilities |
| Tool-specific content | Archive with date | `10-archive/{NN}-Legacy/` | Claude Code templates |
| Principle extracted to Core | Redirect stub | `10-archive/{NN}-Legacy/` | planning-mode.md → Principle |

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

### 99-Legacy Linter Rule (MANDATORY - RFC-001)

```yaml
# .github/workflows/rfc001-legacy-check.yml
name: RFC-001 Legacy Folder Check
on:
  push:
    paths: ['**.md', '**.yaml', 'docs/**']
  pull_request:
    paths: ['**.md', '**.yaml', 'docs/**']

jobs:
  no-99-legacy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check for 99-Legacy in stages 00-09
        run: |
          # Should not find 99-Legacy in active stages
          if find . -maxdepth 3 -path './[0-9][0-9]-*/99-Legacy' -type d 2>/dev/null | grep -q .; then
            echo "❌ FAIL: RFC-001 violation - found 99-Legacy/ in active stage"
            echo "Migrate to 10-archive/{NN}-Legacy/ instead"
            exit 1
          fi
          echo "✓ PASS: No 99-Legacy in active stages"
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

| Original Location | New Location | Created | Expires | Reason |
|------------------|--------------|---------|---------|--------|
| `2-Agent-Templates/claude-code/` | `10-archive/05-Legacy/tool-guides-2026/claude-code/` | Jan 2026 | Jul 2026 | Tool-specific archive |
| `05-Templates-Tools/02-AI-Tools/*.md` (36 templates) | `10-archive/05-Legacy/ai-tools-templates-sprint173/` | Feb 2026 | Aug 2026 | Frozen prompts |

### 6.3.0 Consolidation Stubs (Lean Ring 1)

**Ring 1 → Ring 2 Moves** (9 redirect stubs):

| Original Location | New Location | Created | Expires | Reason |
|------------------|--------------|---------|---------|--------|
| `03-AI-GOVERNANCE/10-CLAUDE-MD-STANDARD.md` | `05-Templates-Tools/03-Agent-Templates/CLAUDE-MD-STANDARD.md` | Mar 2026 | Sep 2026 | Tool-specific → Ring 2 |
| `03-AI-GOVERNANCE/11-AUTONOMOUS-CODEGEN-PATTERNS.md` | `07-Implementation-Guides/AUTONOMOUS-CODEGEN-PATTERNS.md` | Mar 2026 | Sep 2026 | Implementation pattern → Ring 2 |
| `03-AI-GOVERNANCE/12-MULTI-AGENT-PATTERNS.md` | `07-Implementation-Guides/MULTI-AGENT-PATTERNS.md` | Mar 2026 | Sep 2026 | Implementation pattern → Ring 2 |
| `03-AI-GOVERNANCE/15-CONVERSATION-FIRST-GOVERNANCE.md` | `07-Implementation-Guides/CONVERSATION-FIRST-GOVERNANCE.md` | Mar 2026 | Sep 2026 | Interface-specific → Ring 2 |
| `02-Core-Methodology/Documentation-Standards/SDLC-Design-Thinking-Templates.md` | `05-Templates-Tools/06-Manual-Templates/SDLC-Design-Thinking-Templates.md` | Mar 2026 | Sep 2026 | Templates → Ring 2 |
| `02-Core-Methodology/Documentation-Standards/SDLC-Team-Collaboration.md` | `05-Templates-Tools/05-Checklists/SDLC-Team-Collaboration.md` | Mar 2026 | Sep 2026 | Operational → Ring 2 |
| `02-Core-Methodology/Documentation-Standards/SDLC-Visual-Documentation-Standards.md` | `05-Templates-Tools/06-Manual-Templates/SDLC-Visual-Documentation-Standards.md` | Mar 2026 | Sep 2026 | Tooling → Ring 2 |
| `02-Core-Methodology/Documentation-Standards/SDLC-Testing-Artifacts-Structure.md` | `05-Templates-Tools/05-Checklists/SDLC-Testing-Artifacts-Structure.md` | Mar 2026 | Sep 2026 | Operational → Ring 2 |
| `02-Core-Methodology/Governance-Compliance/SDLC-Observability-Checklist.md` | `05-Templates-Tools/05-Checklists/SDLC-Observability-Checklist.md` | Mar 2026 | Sep 2026 | Operational → Ring 2 |

**Merged Documents** (5 source files → 2 consolidated, originals archived):

| Source File | Consolidated Into | Archive Location |
|------------|------------------|-----------------|
| `SDLC-Stage-Dependencies.md` | `SDLC-Stage-Lifecycle-Framework.md` (Part 1) | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` |
| `SDLC-Stage-Exit-Criteria.md` | `SDLC-Stage-Lifecycle-Framework.md` (Part 2) | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` |
| `SDLC-Tier-Stage-Requirements.md` | `SDLC-Stage-Lifecycle-Framework.md` (Part 3) | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` |
| `SDLC-Quality-Assurance-System.md` | `SDLC-Quality-Gates-Assurance-Framework.md` (Part 1) | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` |
| `SDLC-Quality-Security-Gates.md` | `SDLC-Quality-Gates-Assurance-Framework.md` (Part 2) | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` |

**Archived TEAMs** (organizational cleanup):

| File | Archive Location | Reason |
|------|-----------------|--------|
| `TEAM-advisory.md` | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` | Duplicate of TEAM-executive |
| `TEAM-engineering.md` | `10-Archive/02-Legacy/v6.3.0-Pre-Consolidation/` | Overlapped all functional teams |

**Deleted Stubs** (expired redirects, no archive needed):

| File | Deleted | Reason |
|------|---------|--------|
| `02-Core-Methodology/SDLC-Agentic-Core-Principles.md` | Mar 2026 | Redirect expired, target: 03-AI-GOVERNANCE/13 |
| `02-Core-Methodology/SDLC-Agentic-Maturity-Model.md` | Mar 2026 | Redirect expired, target: 03-AI-GOVERNANCE/14 |
| `02-Core-Methodology/SDLC-MRP-Template.md` | Mar 2026 | Redirect expired, target: 05-Templates-Tools |

---

## Responsibilities

| Role | Responsibility |
|------|---------------|
| **File Mover** | Create redirect stub, update CONTENT-MAP.md |
| **PR Reviewer** | Verify stub exists, check links |
| **CI/CD** | Block merge if links broken |
| **Monthly Review** | Check for expired stubs, remove them |

---

---

## Legacy Document Organization (RFC-001, SDLC 6.1.0)

See dedicated standard document: [SDLC-Legacy-Document-Organization.md](../02-Core-Methodology/Documentation-Standards/SDLC-Legacy-Document-Organization.md)

Key rules:
- **RULE-001 (MANDATORY)**: Stage folders (00-09) must contain zero `99-Legacy/` subfolders
- **RULE-002 (MANDATORY)**: All archived content migrates to `10-archive/{NN}-Legacy/` with stage alignment
- **RULE-003 (RECOMMENDED)**: Create `10-archive/README.md` with `AI-NEVER-READ` directive
- **RULE-004 (RECOMMENDED)**: Use `migrate-legacy-to-archive.sh` script for migration

Migration script available in: [05-Templates-Tools/07-Scripts/migrate-legacy-to-archive.sh](../05-Templates-Tools/07-Scripts/migrate-legacy-to-archive.sh)

**Validation**: BFlow Platform metrics (3 live customers):
- Docs size: 211 MB → 91 MB (57% reduction)
- File count: 6,500 → 4,294 (34% reduction)
- AI context pollution: 40% → <5%

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: March 18, 2026
**Next Stub Review**: September 2026 (delete expired 6.3.0 stubs in 6.3.0)
