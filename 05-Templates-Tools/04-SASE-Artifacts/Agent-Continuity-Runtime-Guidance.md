# Agent Continuity Runtime Guidance

**Version**: 1.0.0
**Status**: RECOMMENDED (SHOULD)
**Framework**: SDLC 6.3.1
**Category**: SASE Artifact — Runtime Guidance
**Addresses**: Mental Model #7 (Agent Continuity)
**Added**: April 17, 2026

---

## Overview

This guidance documents a runtime pattern for **closing the Agent Continuity gap** —
the failure mode in which an AI agent with filesystem access asks the user for
project state (sprint number, backlog, tech stack, file layout) that the agent
could discover by reading the workspace.

Mental Model #7 states: *"Each new AI session should inherit enough context to
continue work without re-briefing the human."* When agents ask generic questions
instead of reading available context, they violate this model and defeat the
purpose of documented sprint plans, CLAUDE.md files, and agent configuration docs.

---

## Non-Normative Implementation Note (CPO Condition 1)

> *This guidance documents a pattern first implemented in MTClaw (commit 5b1463e,
> 2026-04-17) and subsequently adopted by SDLC Orchestrator (Sprint 59). Runtime
> implementors SHOULD adopt this pattern but MAY implement equivalent workspace
> discovery via alternative mechanisms (e.g., tool-use preambles, context
> injection, or agent configuration) provided the behavioral outcome — agent
> reads project state before querying user — is preserved.*

Framework docs prescribe outcomes, not implementations. The Layer 1.25 approach
described below is one valid implementation, not the canonical one.

---

## Applicability

This recommendation applies to **runtime implementations of SDLC 6.3.1 agents**
that satisfy ALL of the following:

1. Agent receives a system prompt at invocation time
2. Agent has filesystem-access tools (read_file, list_files, glob, search or equivalent)
3. Agent may be asked project-state questions (planning, status, next steps, architecture)

This recommendation does **NOT** apply to:

- Agents without filesystem access (sandboxed LLMs, pure-reasoning agents)
- Single-turn evaluation prompts (gate evaluation, scoring, classification)
- Agents invoked with pre-populated context that already contains project state

---

## Recommended Outcome

Before answering any question about project planning, status, sprint state, tech
stack, file layout, or backlog, the agent MUST first discover the relevant
project context using its available tools. The agent MUST NOT ask the user for
information obtainable from the workspace.

---

## Discovery Protocol (Reference Implementation)

The following protocol is a reference implementation. Implementors MAY substitute
equivalent mechanisms (see non-normative note above).

```text
## Workspace Awareness (MANDATORY)

Before answering ANY question about the project, planning, status, or next steps,
you MUST first read the project context using your tools.

Discovery protocol — run these reads BEFORE responding:
1. read_file on CLAUDE.md (root) — project overview
2. list_files on docs/04-build/02-Sprint-Plans/ — find latest sprint
3. read_file on most recent SPRINT-NNN-*.md — current scope/status
4. read_file on AGENTS.md if present — per-project agent rules

Never ask the user:
- "What sprint is this?" → read sprint docs
- "What's the backlog?" → read sprint plans + git log
- "What's the tech stack?" → read CLAUDE.md
- "What files are in the project?" → use list_files/glob
```

Adapt directory paths to each project's layout. The protocol is structural, not
path-literal.

---

## Implementation Patterns

### Pattern A — System Prompt Injection (Layer-Based Composers)

For runtimes using layered prompt composition (e.g., SDLC Orchestrator's 4-layer
builder), add a dedicated layer between role-specific content (SOUL/persona) and
project-specific configuration.

**Reference**: SDLC Orchestrator Sprint 59 (`prompt_builder.py` Layer 1.25,
ADR-015).

### Pattern B — Tool-Use Preamble

For runtimes that emit a "preamble" step before agent reasoning, the preamble
itself performs the discovery reads and feeds the results into agent context
before the agent begins reasoning.

**Reference**: MTClaw `buildWorkspaceAwarenessSection()` in
`internal/agent/systemprompt_sections.go` (commit 5b1463e).

### Pattern C — Agent Configuration Flag

For runtimes with per-agent configuration, enable a `workspace_discovery_required`
flag that the runtime enforces by executing discovery reads before handing
control to the agent.

**Reference**: No upstream reference yet; available for future implementations.

---

## Security Considerations

The workspace-awareness instruction is a **trust-elevating** directive — it tells
the agent to fetch and rely on workspace content. If an attacker can inject or
mutate this instruction at runtime, they can:

- Redirect discovery to attacker-controlled paths
- Suppress discovery entirely (re-expose the Agent Continuity gap)
- Inject malicious "context" into the agent's reasoning

**Mitigation**: Implementations SHOULD treat the workspace-awareness instruction
as a **static module-level constant**, not a runtime-mutable value. SDLC
Orchestrator Sprint 59 enforces this via `test_workspace_awareness_is_static_constant`
which verifies the instruction is a module attribute, not a function-generated
string.

---

## Quality Gate Alignment

Runtime implementations adopting this pattern SHOULD update their quality gate
evaluations to check:

- **G0 (Design)**: Agent configuration documents workspace-discovery mechanism
- **G3 (Test)**: Tests verify agents read expected files before answering project-state queries
- **G4 (Approve)**: Human reviewer confirms no regression in agent discovery behavior

---

## References

- **Mental Model #7**: Agent Continuity — `02-Core-Methodology/SDLC-System-Thinking-Foundation.md`
- **MTClaw trigger report**: `MTClaw/docs/03-integrate/workspace-awareness-notice.md` (2026-04-17)
- **MTClaw implementation**: commit `5b1463e` in MTClaw repository
- **SDLC Orchestrator implementation**: Sprint 59, ADR-015, `prompt_builder.py`
- **AGENTS.md template**: `AGENTS-MD-Template.md` (this directory)

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-04-17 | Initial release as SDLC 6.3.1 addendum (SASE Artifact) |

---

**Document Status**: RECOMMENDED (SHOULD)
**Replaces**: Nothing (new document)
**Last Updated**: April 17, 2026
