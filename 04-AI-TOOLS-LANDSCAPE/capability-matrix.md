# AI Tool Capability Matrix (January 2026)

**Version**: 5.3.0  
**Status**: ACTIVE - OUTER RING  
**Purpose**: Compare AI coding tools against SDLC Orchestrator governance requirements.

---

## Summary Matrix

| Capability | Claude Code | Cursor | Copilot | Codeium | Amazon Q |
|------------|-------------|--------|---------|---------|----------|
| Context file discipline | ✅ CLAUDE.md enforced | ✅ `.cursorrules` | ⚠️ `copilot-instructions.md` (beta) | ⚠️ Team prompts | ⚠️ Project prompts |
| Human approval workflow | ✅ Required before apply | ⚠️ Manual confirm | ✅ Manual author applies | ⚠️ Optional | ✅ Team-based |
| Multi-file editing | ✅ Native | ✅ Native | ⚠️ Limited | ⚠️ Limited | ✅ |
| Sub-agents / task orchestration | ✅ Task tool | ⚠️ Plan forks | ❌ | ❌ | ⚠️ Workflows (preview) |
| MCP / plugin integration | ✅ Native MCP | ❌ | ❌ | ❌ | ❌ |
| Headless / CI mode | ✅ `claude code -p` | ⚠️ CLI beta | ⚠️ CLI chat | ⚠️ API | ⚠️ CLI (limited) |
| Audit trail export | ✅ Session log + Evidence Vault | ⚠️ Local log only | ⚠️ GitHub audit log | ⚠️ Enterprise telemetry | ⚠️ CloudWatch logs |
| Governance automation | ✅ Orchestrator-ready | ⚠️ Needs wrappers | ⚠️ PR gates only | ⚠️ Custom scripts | ⚠️ AWS toolchain |
| Enterprise compliance | ✅ SOC2, ISO27001 | ✅ SOC2 | ✅ SOC2 | ✅ SOC2 | ✅ FedRAMP High (AWS) |

**Legend**: ✅ Full support | ⚠️ Partial / manual | ❌ Not supported (requires workaround)

---

## Capability Detail

### Context Management

- **Claude Code** – CLAUDE.md + `.claude/rules/` enforceable via MCP server.
- **Cursor** – `.cursorrules` respected, but needs governance reviews to stay <60 lines.
- **Copilot** – `copilot-instructions.md` available in enterprise beta; human discipline required.
- **Codeium / Amazon Q** – Provide team-level prompts; need manual synchronization with AGENTS.md.

### Verification & Quality Gates

- **Claude Code** – Runs `pytest`, `npm test`, custom pipelines via MCP tasks.
- **Cursor** – Relies on repo scripts; encourage `pre-commit` and CI for enforcement.
- **Copilot** – Pull request checks only; must integrate with branch protection.
- **Codeium** – Offers "test suggestion" but no automated enforcement.
- **Amazon Q** – Integrates with AWS CodeCatalyst; configure for mandatory test runs.

### Audit Trail

- **Claude Code** – Session transcripts + Evidence Vault webhook; meets compliance requirements.
- **Cursor** – Local logs; add sync task to central storage for traceability.
- **Copilot** – GitHub audit log captures invocation metadata, not code context; augment with PR annotations.
- **Codeium** – Enterprise plan exports telemetry; verify retention policy.
- **Amazon Q** – CloudTrail + CodeCatalyst logs; ensure retention aligns with governance policy.

### Agentic Readiness Score

| Tool | Readiness (0-5) | Notes |
|------|-----------------|-------|
| Claude Code | **5** | Only tool with native MCP + full audit trail |
| Cursor | **3** | Strong IDE experience, governance wrappers needed |
| Copilot | **2** | Human-in-loop only; no autonomous execution |
| Codeium | **2** | Good completions, limited governance hooks |
| Amazon Q | **3** | Deep AWS integration; still maturing agent support |

> **Agentic Readiness** measures how quickly SDLC Orchestrator can enforce the 7 AI Governance Principles without heavy customization.

---

## Recommended Governance Actions

1. **Claude Code** – Maintain MCP config in `.mcp.json`; run quarterly audits.
2. **Cursor** – Ship helper scripts (`cursor-sync-logs.sh`) to centralize audit data.
3. **Copilot** – Enforce `copilot-instructions.md` presence via CI check; require PR templates capturing AI usage.
4. **Codeium** – Add pre-commit hook verifying completion provenance tags.
5. **Amazon Q** – Integrate with AWS IAM condition keys for project-based access control.

---

## Change Log

| Date | Change |
|------|--------|
| Jan 2026 | Initial matrix for SDLC Framework 5.2.0 |

---

**Document Status**: ACTIVE  
**Owner**: CTO Office  
**Review Cycle**: Quarterly (align with Tool Profiles)
