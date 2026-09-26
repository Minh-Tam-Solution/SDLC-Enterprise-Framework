# Claude Code - Tool Profile

**Last Updated**: January 2026
**Version Tracked**: Claude Code 1.x
**Status**: REFERENCE PROFILE

> **Framework Independence**: SDLC methodology does not depend on any specific tool.
> These are Ring 2 reference profiles. Governance principles in `03-AI-GOVERNANCE/` apply regardless.

---

## Overview

Claude Code is Anthropic's CLI-based AI coding assistant. It provides terminal-based AI-assisted development with deep codebase understanding.

---

## Key Capabilities

| Capability | Status | Notes |
|------------|--------|-------|
| Context file | ✅ CLAUDE.md | Project-level instructions |
| Multi-file editing | ✅ | Native support |
| Human approval | ✅ | Required before changes |
| Sub-agents | ✅ | Task delegation |
| MCP integration | ✅ | Native Model Context Protocol |
| Extended thinking | ✅ | Deep reasoning mode |
| Custom commands | ✅ | .claude/commands/ |
| Headless mode | ✅ | -p flag for CI/CD |
| Memory | ✅ | Cross-session learning |

---

## Orchestrator Integration

### Current Status: FULL INTEGRATION

| Integration Point | Implementation |
|-------------------|----------------|
| Context overlay | MCP server delivers gate status |
| Quality gates | Pre-commit hooks + CI checks |
| Evidence capture | Automatic logging to Evidence Vault |
| Audit trail | Session logs stored |

### MCP Configuration

```json
// .mcp.json (committed to repo)
{
  "servers": {
    "sdlc-orchestrator": {
      "command": "sdlcctl",
      "args": ["mcp", "serve"],
      "env": {
        "SDLC_PROJECT_ID": "${PROJECT_ID}"
      }
    }
  }
}
```

---

## Best Practices (Claude Code Specific)

### Context File (CLAUDE.md)

```markdown
# CLAUDE.md

## Quick Start
- `docker compose up -d`
- `npm run dev`

## Conventions
- Python: snake_case, type hints
- TypeScript: PascalCase components

## DO NOT
- Add TODO comments
- Skip tests
```

**Target**: <60 lines (per HumanLayer research)

### Planning Mode

Trigger phrases:
- "Think deeply about..."
- "Plan before implementing..."
- Toggle: Tab key

### Extended Thinking

Use for:
- Architectural decisions
- Complex debugging
- Multi-file refactoring

### Sub-agents

```bash
# Spawn explore sub-agent
"Use Task tool to search for similar patterns"

# Research without polluting main context
"Fork session to investigate this"
```

---

## Governance Alignment

| Principle | Claude Code Support |
|-----------|---------------------|
| AI-Human Collaboration | ✅ Approval workflow |
| Agent Accountability | ✅ Human reviews all changes |
| Planning Mode | ✅ Native support |
| Verification-First | ✅ Can run tests before commit |
| Context Management | ✅ CLAUDE.md + .claude/rules/ |
| Tool Evaluation | N/A |
| Anti-Patterns | ✅ Context prevents common mistakes |

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| 1.0 | 2025 | Initial release |
| 1.x | Jan 2026 | MCP, sub-agents, extended thinking |

---

## References

- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [HumanLayer: Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) - Timeless principles

---

**Profile Status**: ACTIVE
**Review Cycle**: Quarterly
