# Principle 6: Tool Evaluation Criteria

**Version**: 6.1.1
**Status**: ACTIVE
**Date**: January 28, 2026

---

## The Rule

> **Evaluate tools against principles, not hype.**
>
> Tools change constantly. Have criteria ready.

---

## Mandatory Criteria

When adopting ANY new AI coding tool, verify these MUST-HAVE capabilities:

| Criterion | Test | Why Critical |
|-----------|------|--------------|
| **Context file support** | Can use AGENTS.md or equivalent | Context enables effectiveness |
| **Human approval workflow** | Requires approval before changes | Accountability principle |
| **Quality gate integration** | Can block on test/lint failure | Verification principle |
| **Audit trail** | Logs what AI did and when | Compliance requirement |
| **Session isolation** | Changes don't persist unexpectedly | Safety requirement |

---

## Evaluation Checklist

### Must-Have (Reject if missing)

```yaml
Context Support:
  - [ ] Reads project context file (AGENTS.md, .cursorrules, etc.)
  - [ ] Respects context constraints
  - [ ] Supports progressive disclosure (file imports)

Human-in-Loop:
  - [ ] Requires human approval for code changes
  - [ ] Shows diff before applying
  - [ ] Allows partial acceptance/rejection

Quality Integration:
  - [ ] Can run tests before committing
  - [ ] Can run linters before committing
  - [ ] Respects CI/CD gate results

Audit & Safety:
  - [ ] Logs all actions with timestamps
  - [ ] Session isolation (no cross-session pollution)
  - [ ] Can rollback changes
```

### Nice-to-Have (Differentiation)

```yaml
Productivity:
  - [ ] Multi-file editing capability
  - [ ] Sub-agent/parallel execution
  - [ ] Custom commands/skills
  - [ ] IDE integration

Intelligence:
  - [ ] Model selection options
  - [ ] Extended thinking mode
  - [ ] Memory across sessions
  - [ ] Learning from corrections

Integration:
  - [ ] MCP server support
  - [ ] Git integration
  - [ ] CI/CD hooks
  - [ ] Team sharing
```

---

## Evaluation Matrix Template

| Criterion | Weight | Tool A | Tool B | Tool C |
|-----------|--------|--------|--------|--------|
| Context file | MUST | ✅ | ✅ | ❌ |
| Human approval | MUST | ✅ | ✅ | ✅ |
| Quality gates | MUST | ✅ | ⚠️ | ✅ |
| Audit trail | MUST | ✅ | ❌ | ✅ |
| Session isolation | MUST | ✅ | ✅ | ⚠️ |
| **MUST-HAVE Score** | — | **5/5** | **3/5** | **4/5** |
| Multi-file edit | NICE | ✅ | ✅ | ❌ |
| Sub-agents | NICE | ✅ | ❌ | ❌ |
| MCP support | NICE | ✅ | ❌ | ❌ |
| **Total Score** | — | **8/8** | **4/8** | **4/8** |

**Decision**: Tool A passes all must-haves and has best nice-to-haves.

---

## Red Flags (Reject Immediately)

| Red Flag | Why Dangerous |
|----------|---------------|
| No human approval workflow | Violates accountability principle |
| Auto-commits without review | Safety risk |
| No context file support | Effectiveness severely limited |
| Closed-source with no audit | Compliance risk |
| Requires sending code to unknown servers | Security/privacy risk |

---

## When to Switch Tools

Consider switching when:

| Trigger | Action |
|---------|--------|
| Tool deprecated | Evaluate alternatives |
| Security vulnerability found | Immediate review |
| Better tool emerges | Evaluate against criteria |
| Team friction with current tool | Investigate and evaluate |
| Cost/value ratio changes | Re-evaluate |

**Never switch based on**:
- Hype alone ("everyone's using X")
- Single feature ("X has cool Y feature")
- Without evaluation against criteria

---

## Tool-Specific vs Principle-Specific

| Keep in Framework | Keep in Tool Docs |
|-------------------|-------------------|
| Evaluation criteria | Installation steps |
| Principles (this doc) | Configuration syntax |
| What to look for | How to use features |
| Decision framework | Keyboard shortcuts |

**Framework stays principle-focused; tool docs handle specifics.**

---

## Sunset Criteria

When to retire a tool from team use:

```yaml
Mandatory Retirement:
  - [ ] Tool no longer maintained (6+ months no updates)
  - [ ] Critical security vulnerability unfixed (30+ days)
  - [ ] Vendor goes out of business
  - [ ] Fails must-have criterion that previously passed

Optional Retirement:
  - [ ] Better alternative available (>2x improvement)
  - [ ] Cost becomes prohibitive
  - [ ] Team adoption <20% after 3 months
```

---

## Related Principles

- [01-AI-Human-Collaboration](01-AI-Human-Collaboration.md) - Tools must support this model
- [05-Context-Management](05-Context-Management.md) - Context file support is mandatory
- [07-Anti-Patterns](07-Anti-Patterns.md) - Tool adoption anti-patterns

---

**Document Status**: ACTIVE
**Last Updated**: January 22, 2026
