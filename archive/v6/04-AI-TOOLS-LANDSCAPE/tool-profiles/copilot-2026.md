# GitHub Copilot - Tool Profile

**Last Updated**: January 2026  
**Version Tracked**: Copilot Chat + Copilot CLI (2026.1)  
**Status**: REFERENCE PROFILE

> **Framework Independence**: SDLC methodology does not depend on any specific tool.
> These are Ring 2 reference profiles. Governance principles in `03-AI-GOVERNANCE/` apply regardless.

---

## Overview

GitHub Copilot is an AI pair programmer embedded in IDEs (VS Code, JetBrains, Neovim) and GitHub.com. Copilot accelerates code authoring through inline completions and chat-based assistance, but it lacks native governance hooks required for autonomous workflows. Within SDLC Orchestrator, Copilot remains a **human-first augmentation** tool.

---

## Key Capabilities

| Capability | Status | Notes |
|------------|--------|-------|
| Context file | ⚠️ `copilot-instructions.md` (beta) | Repo instructions supported but unenforced |
| Multi-file editing | ⚠️ | Chat suggestions limited; no automated diff apply |
| Human approval | ✅ | Human applies suggestions manually |
| Sub-agents | ❌ | No parallel task execution |
| MCP integration | ❌ | No MCP or plugin API |
| Extended thinking | ❌ | Short reasoning horizon |
| Custom commands | ❌ | Prompt only |
| Headless mode | ⚠️ | Copilot CLI for chat, no automated apply |
| Audit trail | ⚠️ | GitHub audit logs capture limited context |

**Legend**: ✅ Full | ⚠️ Partial | ❌ Not supported

---

## Orchestrator Integration

### Current Status: MINIMAL INTEGRATION

| Integration Point | Implementation | Notes |
|-------------------|----------------|-------|
| Context overlay | Optional `copilot-instructions.md` | Must be enforced via repo policy |
| Quality gates | Rely on GitHub branch protection | Works only after PR |
| Evidence capture | Manual screenshots or PR comments | Encourage attaching to MRPs |
| Audit trail | GitHub activity log | No detail on rejected suggestions |

### Governance Position

- **Primary Use Case**: Developer assist while human remains editor of record.
- **Not Approved For**: Autonomous edits, unattended refactors, agentic workflows.
- **Mitigation**: Pair Copilot with `AGENTS.md` + manual Plan/Review checklists.

---

## Copilot-Specific Best Practices

### Repository Instructions (Beta)

```
# copilot-instructions.md
- Always prefer framework utilities in /libs/shared
- Use pytest fixtures from tests/fixtures.py
- Require docstrings on public functions
- Do not create new endpoints without ADR
```

- Keep file short (<60 lines) to align with Context Management principle.
- Commit alongside AGENTS.md to keep human+AI guidance in sync.

### Pull Request Governance

1. Require PR reviews from CODEOWNERS.
2. Block merges until tests + lint succeed.
3. Capture rationale in MRP (Merge-Readiness Pack) referencing Copilot usage.

### Copilot CLI Guardrail

```
copilot chat --limit-output \
  --rule "Never run git commit" \
  --rule "Prompt user to run pytest before final answer"
```

- Wrap CLI in shell aliases to remind developers about verification steps.

---

## Governance Alignment

| Principle | Copilot Support | Notes |
|-----------|-----------------|-------|
| AI-Human Collaboration | ✅ | Human is active driver |
| Agent Accountability | ✅ | Human authors commits |
| Planning Mode | ⚠️ | Requires manual checklists |
| Verification-First | ⚠️ | Enforcement via CI/PR gates |
| Context Management | ⚠️ | Depends on instructions file discipline |
| Tool Evaluation | ⚠️ | Checklist needed for each repository |
| Anti-Patterns | ⚠️ | Watch for "rubber-stamp" approvals |

---

## Known Gaps & Mitigations

- **No Automated Audit Trail** – Encourage developers to note Copilot-generated code in PR descriptions.
- **Limited Context Persistence** – Remind teams to refresh prompts and include architecture context.
- **Security & Privacy** – Verify enterprise plan; disable data retention where required.
- **Model Drift** – Review completions quarterly to ensure alignment with standards.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| 2025.4 | Q4 2025 | Introduced Copilot CLI |
| 2026.1 | Q1 2026 | Repository instructions private beta |

---

## References

- [GitHub Copilot Enterprise Docs](https://docs.github.com/en/copilot)  
- [Copilot CLI](https://githubnext.com/projects/copilot-cli/)  
- [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) – Governing principles for Copilot usage

---

**Profile Status**: ACTIVE  
**Review Cycle**: Quarterly
