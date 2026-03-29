# Principle 5: Context Management

**Version**: 6.2.1
**Status**: ACTIVE
**Date**: January 28, 2026

---

## The Rule

> **AI needs context to be effective. Keep it concise (<60 lines).**
>
> More context ≠ better results. Focused context = better results.

---

## Context File Hierarchy

### 1. AGENTS.md (PRIMARY - Industry Standard)

```yaml
Purpose: Universal AI context file
Adoption: 60K+ repos on GitHub
Works With: ALL AI coding tools
Location: Repo root
Target Size: <60 lines (CRITICAL)
```

**Use AGENTS.md by default.** It works everywhere.

### 2. CLAUDE.md (OPTIONAL - Claude-specific)

```yaml
Purpose: Claude-specific extension
When to Use: Only if team uses Claude Code exclusively
Location: .claude/ directory or repo root
Relationship: Extends AGENTS.md, adds Claude-specific config
```

### 3. .claude/rules/ (PROGRESSIVE DISCLOSURE)

```yaml
Purpose: Split large context into focused files
When to Use: Codebase needs >150 lines of context
Location: .claude/rules/
Files: building.md, testing.md, security.md, etc.
Reference: From AGENTS.md via @imports
```

---

## Decision Tree

```
Do you use ONLY Claude Code?
├── NO → Use AGENTS.md only
└── YES →
    ├── Simple project → Use AGENTS.md only
    └── Complex project → AGENTS.md + CLAUDE.md extension
        └── Very large codebase → Add .claude/rules/
```

**Rule**: If in doubt, use AGENTS.md only.

---

## The 60-Line Limit

> "Frontier thinking LLMs can follow ~150-200 instructions with reasonable consistency."
> "Keep CLAUDE.md under 60 lines for highest effectiveness."
> — HumanLayer Research

| Lines | Effectiveness | Recommendation |
|-------|---------------|----------------|
| <60 | Highest | TARGET THIS |
| 60-150 | Good | Acceptable |
| 150-300 | Declining | Consider splitting |
| >300 | Poor | Must restructure |

---

## What TO Include in AGENTS.md

```markdown
# AGENTS.md

## Quick Start
[3-5 essential commands to build/test/run]

## Architecture
[1 paragraph + simple diagram if needed]

## Conventions
[5-10 bullet points of coding standards]

## DO NOT
[5-10 anti-patterns specific to this project]
```

---

## What NOT to Include

| Don't Include | Why | Alternative |
|---------------|-----|-------------|
| Code style rules | Linters enforce this | Use .eslintrc, ruff.toml |
| Full API docs | Too verbose | Link to docs/ |
| Historical context | Clutters | Use ADRs |
| Generic best practices | AI knows these | Only project-specific |
| Verbose explanations | Wastes tokens | Be concise |

> "Never send an LLM to do a linter's job."
> — HumanLayer

---

## Static vs Dynamic Context

### Static Context (AGENTS.md - COMMITTED)

```yaml
Content:
  - Conventions and standards
  - Setup commands
  - Architecture overview
  - DO/DON'T boundaries

Changes: Rarely (with PR review)
Location: Repo root (committed to git)
```

### Dynamic Context (NOT COMMITTED)

```yaml
Content:
  - Current gate status
  - Known issues/blockers
  - Sprint-specific constraints
  - Strict mode flags

Changes: Frequently (per gate, per sprint)
Delivery: PR comments, CLI overlay, IDE extension
```

---

## Dynamic Context Delivery

| Channel | Description | Use Case |
|---------|-------------|----------|
| PR Comments | Auto-posted on PR open | Gate status, known issues |
| CLI Overlay | `[SDLC CLI] context pull` | CI/CD integration |
| IDE Extension | Inject into chat | IDE users |

Example dynamic context (PR comment):

```markdown
<!-- SDLC Dynamic Context -->
## Gate Status
- ✅ G2: Design approved
- 🔄 G3: In progress

## Constraints
- 🔒 Architecture decisions LOCKED
- ✅ Unit tests required
<!-- /SDLC Dynamic Context -->
```

---

## Progressive Disclosure Pattern

For large codebases, split context:

```
.claude/rules/
├── building.md     # Build commands, env setup
├── testing.md      # Test patterns, coverage
├── security.md     # Security requirements
├── api.md          # API conventions
└── database.md     # DB patterns, migrations
```

Reference from AGENTS.md:
```markdown
## Detailed Rules
- Building: @.claude/rules/building.md
- Testing: @.claude/rules/testing.md
```

**Limit**: Max 5 hops for imports.

---

## Tool-Agnostic Application

The context file principle applies universally:
- Claude: AGENTS.md or CLAUDE.md
- Cursor: .cursorrules or similar
- Copilot: .github/copilot-instructions.md
- Any tool: Project-level context file

**The pattern is universal; the filename varies by tool.**

---

## Related Principles

- [01-AI-Human-Collaboration](01-AI-Human-Collaboration.md) - Context enables collaboration
- [06-Tool-Evaluation-Criteria](06-Tool-Evaluation-Criteria.md) - Evaluate context support
- [07-Anti-Patterns](07-Anti-Patterns.md) - Context anti-patterns

---

**Document Status**: ACTIVE
**Last Updated**: January 22, 2026
