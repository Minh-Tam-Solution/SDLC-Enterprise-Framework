# Cursor - Tool Profile

**Last Updated**: January 2026  
**Version Tracked**: Cursor IDE 0.45+  
**Status**: SECONDARY TOOL (SDLC Orchestrator)

---

## Overview

Cursor is an AI-native IDE focused on pair-programming workflows. It blends a code editor, chat interface, and repository-aware agents that can plan and execute multi-step changes. Cursor is popular for solo developers and small squads who want to move fast with an AI partner while staying inside a traditional IDE experience.

---

## Key Capabilities

| Capability | Status | Notes |
|------------|--------|-------|
| Context file | ✅ `.cursorrules` | Supports repo-level guardrails (60 line target) |
| Multi-file editing | ✅ | "Edit" and "Write" actions across files |
| Human approval | ⚠️ | Manual approval before applying diff |
| Sub-agents | ⚠️ | "Continue plan" forks session, limited orchestration |
| MCP integration | ❌ | No native MCP server support (roadmap) |
| Extended thinking | ⚠️ | "Deep" mode increases analysis budget |
| Custom commands | ✅ | Slash commands + JSON snippets |
| Headless mode | ⚠️ | Cursor CLI available, no full non-interactive mode |
| Audit trail | ⚠️ | Local session log; no central export yet |

**Legend**: ✅ Full | ⚠️ Partial | ❌ Not supported

---

## Orchestrator Integration

### Current Status: PARTIAL INTEGRATION

| Integration Point | Implementation | Notes |
|-------------------|----------------|-------|
| Context overlay | `.cursorrules` committed | Humans maintain guardrails manually |
| Quality gates | Rely on repo CI & pre-commit | No native enforcement hooks |
| Evidence capture | Manual copy of chat transcript | Export to Evidence Vault required |
| Audit trail | Local logs | Add Git hooks to sync logs if needed |

### Recommended Governance Hooks

1. **Context File Discipline** – Keep `.cursorrules` <60 lines, refresh each sprint.
2. **Approval Checklist** – Use AGENTS.md `## Review Checklist` before applying diff.
3. **CI Enforcement** – Require tests+lint via `pre-commit` and GitHub Actions.
4. **Log Retention** – Add script to sync Cursor logs into central store weekly.

---

## Cursor-Specific Best Practices

### Planning Command

```
User: "Plan a safe refactor of the billing service.
Break it into steps and highlight risky files before editing anything."
```

- Cursor generates a plan panel; review every step before approving execution.
- If risk is high, pause and open Planning Mode (per governance principle #3).

### Scoped Editing

```
User: "Only modify functions inside billing/discounts/*.py.
Do not alter tests until we confirm the approach."
```

- Helps maintain human control when the repo contains sensitive modules.
- Pair with `git diff --cached` to inspect Cursor's proposed patch.

### `.cursorrules` Pattern (Excerpt)

```markdown
# Cursor Rules
- Keep conversations under 200 lines
- Never commit directly to main
- Always tag TODOs with owner
- Tests must pass: `npm test`, `pytest`
```

---

## Governance Alignment

| Principle | Cursor Support | Notes |
|-----------|----------------|-------|
| AI-Human Collaboration | ✅ | Human approves each applied change |
| Agent Accountability | ✅ | Human retains Git authorship |
| Planning Mode | ⚠️ | Manual trigger; no risk classifier |
| Verification-First | ⚠️ | Dependent on human running tests |
| Context Management | ✅ | `.cursorrules` enforced |
| Tool Evaluation | ⚠️ | Needs scripted checklist |
| Anti-Patterns | ⚠️ | Avoid "apply without review" scenarios |

---

## Known Gaps & Mitigations

- **No MCP** – Wrap Cursor with Orchestrator CLI hooks until vendor adds support.
- **Limited Audit Trail** – Export `~/.cursor/logs` nightly to maintain compliance.
- **Security Review** – Ensure API keys, local models stored via OS keychain.
- **Large Rewrites** – Encourage incremental edits; fall back to human-driven IDE for sweeping migrations.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| 0.40 | Q3 2025 | Added `.cursorrules`, plan refinement |
| 0.45 | Q1 2026 | Cursor CLI beta, improved test integration |

---

## References

- [Cursor Changelog](https://cursor.sh/changelog)  
- [Cursor CLI Beta Announcement](https://cursor.sh/blog)  
- [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) – Timeless principles that govern Cursor usage

---

**Profile Status**: ACTIVE  
**Review Cycle**: Quarterly
