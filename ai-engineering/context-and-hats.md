# Context and Hats

**Version**: 1.0.0 · **Status**: DRAFT (v7) · **Date**: 2026-09-25
**SDLC Framework Version**: 7.0.0
**Verified against**: Claude Code docs as of 2026-09-25 (current to v2.1.281) · Qwen Code 0.22.x docs and source.
Tools change how they load context. When either one ships a change to memory, imports, skills or subagents, check this page again.
**Replaces**: `03-AI-GOVERNANCE/05-Context-Management.md` (v6.x), which taught the loading mechanism wrong:

| v6 said | What the tools actually do |
|---|---|
| "Use AGENTS.md. It works everywhere." | Qwen Code reads `QWEN.md` and `AGENTS.md` by default. Claude Code reads `AGENTS.md` directly **only from v2.1.277** and only when there is no `CLAUDE.md`. On older versions, `CLAUDE.md` is required. It can hold one line, `@AGENTS.md`. |
| `.claude/rules/` + `@imports` = "progressive disclosure" | Imported files and rules without `paths:` **load at launch**. Splitting them into files does not reduce what gets loaded. |
| "Max 5 hops for imports" | Claude Code stops at **4** hops, Qwen Code at 5. The tool enforces the limit, so don't restate it. |
| Dynamic context delivered by PR comments, a CLI overlay or an IDE plugin | That channel belonged to a retired product. Session state now goes in a handoff file (Tier 3). |

## Three tiers

### Tier 1: always loaded (`CLAUDE.md` / `AGENTS.md` / `QWEN.md` at the repo root)

- **Small.** Keep the shared part under 60 lines. Claude Code docs say *"target under 200 lines per CLAUDE.md file"*, and longer files reduce adherence.
- **Point to the source of truth. Don't copy it.** No copied tables, counts, directory trees, dependency lists or architecture overviews. Keep pitfalls, rationale and conventions.
  Burned case: an always-loaded file copied an architecture table from a decision record. The copy drifted from its source for 3.5 months and nothing reported it. The fix re-copied the table from a secondary report and drifted a second time.
- **Context is not enforcement.** Claude Code docs: CLAUDE.md is *"context, not enforced configuration. To block an action … use a PreToolUse hook"*.
  - Exit code `2` blocks the action, in both tools.
  - `permissionDecision: "ask"` prompts the user. In Qwen Code headless runs, "ask" falls back to deny.
  - Hooks run without a controlling terminal, so they cannot open `/dev/tty`. Never build an escape hatch on a TTY prompt inside a hook.
- **Add one compaction line.** *"When compacting, preserve: the list of modified files, the check/test commands, and each decision with its source."* Claude Code docs recommend this pattern. A root `CLAUDE.md` survives compaction.

### Tier 2: loaded on demand

- **Skills.** At startup only the description loads. The full content loads when the skill is invoked. Claude Code truncates `description` + `when_to_use` at 1,536 characters.
  - Don't set `model:` in a skill. Switching model mid-session rereads the whole history with no cache hits.
  - Preload skills into a subagent (`skills:`) only when you have a reason. Preloaded skills load in full at startup.
- **Path-scoped rules** (`paths:` frontmatter, Claude Code) load when the agent **reads a matching file**. Running a command does not load them.
  - A rule about `git` commands will not load on `git commit`. Put rules about commands in a hook or a permission rule.
  - A Qwen Code equivalent is not verified.
- **Search and delegation.** Long reference material stays on disk. The agent searches it, or hands the question to a subagent with its own context window.

### Tier 3: session boundary

- Use `/clear` between unrelated tasks, and after you have corrected the agent more than twice on the same thing.
- **Before `/clear`, write a handoff artifact.** Record state, not history:
  - decisions, each with its source
  - done
  - open
  - blockers
  - next action
- Put it where the **next executor can read it**, such as the shared repo. A personal agent folder on one machine does not count.
- Protocol: `templates/agent/PREAMBLE-example.md` § Long-running work.

## Hats

A hat is a role an agent works in. **v1 has four hats:**

- `fullstack`: the default
- `reviewer`
- `tester`
- `architect`

Every other role stays in a catalog. Promote one only when it has a named consumer, a real use case and a different tool set.

| | Session hat | Subagent hat |
|---|---|---|
| What it is | Instructions worn in the main session | A separate agent definition with its own context window |
| Carries permissions | No. Text only, so it is advisory. | Yes. A tool allowlist (`tools_class` maps to `tools`) and a model |
| Required fields | `name`, `description` | `name`, `description`. Claude Code **skips a subagent with no `description`** and logs an error. Qwen Code accepts the same fields. |

- **`description` says when to use it.** Example: "Use when …; use proactively" if the main agent should delegate without being asked. Keep all descriptions short. Claude Code warns at startup when they add up to more than 15,000 tokens.
- **Reviewer = fresh context.** The agent doing the work isn't the one grading it. A reviewer subagent sees only the diff and the criteria, not the reasoning that produced the change.
- **Typed verdict.** Free text is not a verdict:

```yaml
verdict: changes_requested   # one of: approve | changes_requested | insufficient_evidence
abstain_reason: ""           # required when verdict is insufficient_evidence
findings:
  - {severity: MAJOR, file: <path>, line: <n>, claim: <what is wrong>, evidence: <quote or command output>}   # severity: BLOCKER | MAJOR | MINOR
```

- `approve` with any `BLOCKER` finding counts as `changes_requested`.
- `insufficient_evidence` is a valid outcome. Use it when the reviewer cannot run or see what it needs. It is never a silent approve.
- An AI review is **evidence** (review class). It is not a human approval, and it is never a machine gate by itself. The workflow records who reviewed (`reviewer_type`), not the authoring agent.
- **Intent confirmation.** Before work, the agent states three lines: the problem, who uses the result, and what "done" means. It asks and waits only when the brief is ambiguous or the project tier is high. Keep the record in the PR template (three fields), not in chat.

Templates: `templates/agent/SOUL-example.md` (one hat) · `templates/agent/PREAMBLE-example.md` (shared by all hats).

## What this page does not claim

- "Shorter context is cheaper or better" is a **hypothesis**. The framework has no measured case for it. The 60-line target is a convention, not a gate.
- Claude Code facts here come from the current online docs. An installed version can differ. For example, v2.1.239 does not read `AGENTS.md`. Check with `claude --version` before you rely on a version-gated behavior.
