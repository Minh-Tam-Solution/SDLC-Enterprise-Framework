# Context and Hats

**Version**: 1.1.0 · **Status**: ACTIVE · **Date**: 2026-10-02
**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: authors of `AGENTS.md`, PREAMBLE and hat files
**Review by**: 2026-12-26
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
- **Only what the agent cannot work out.** A line earns its place if removing it would cause a mistake: commands the agent cannot guess, conventions that differ from the language default, pitfalls, where the decisions live. Cut what reading the code reveals, generic advice ("write clean code"), file-by-file tours, and style rules: a formatter or linter enforces those every time, faster.
- **Specific, not general.** "Errors go through the error type in `<path>`" gets followed; "handle errors properly" does not. One instruction per bullet, grouped by topic.
- **A subproject with its own rules gets its own file** in its folder. In the open format the nearest file wins; when each tool loads a nested file differs, so check before relying on it.
- **Context is not enforcement.** Claude Code docs: CLAUDE.md is *"context, not enforced configuration. To block an action … use a PreToolUse hook"*.
  - Exit code `2` blocks the action, in both tools.
  - `permissionDecision: "ask"` prompts the user. In Qwen Code headless runs, "ask" falls back to deny.
  - Hooks run without a controlling terminal, so they cannot open `/dev/tty`. Never build an escape hatch on a TTY prompt inside a hook.
- **A rule the agent keeps breaking is not fixed by repeating it louder.** First suspect length: the rule is lost among the others, so prune. If it must hold every time, move it into a hook, a linter or a CI check and delete the line; a repeated mistake with a price is a burn case for [lessons-to-rules](../practices/lessons-to-rules.md). v6 kept a dated lesson file per bug and folded them into the context file monthly, which grows the file the rule was getting lost in.
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

## Bounded loops

An agent fixing and re-testing works in a bounded loop: after a configured number of attempts (three is a sensible default) it stops and hands over with what it found, instead of retrying until something passes. The limit is agent policy, set in the policy repo per tier, not a testing rule.

## Briefing an agent

The brief is the task handed to an agent. Intent confirmation (below) says why; the brief says what, where, and how to know it is done.

- **Name the place and the case:** the file or area, the scenario, the constraints, including what not to use. "Add tests for the parser" leaves every choice open; "test the parser on an empty file; no test doubles" does not.
- **Point to the thing, not a description of it:** the path of code that already does the same kind of work, the error output pasted as it is, the issue link.
- **End with a check the agent can run:** a test to write and pass, a build, a script that diffs output against a fixture. Without one, "looks done" is the only stop signal and the person becomes the test loop. For a bug, the check is a failing test that reproduces it, written first.
- **Ask for evidence, not a claim:** the command run and its output. Reading evidence is faster than re-running the work.
- **Name it; do not lean on the conversation.** "Fix the other one" depends on history that compaction may have dropped.
- **Vague on purpose is for exploring** ("what would you improve here?"), never for a change that will be merged.

## Plan before code

Planning separates finding out from changing things: the agent reads and asks first, writes a plan, and changes nothing until the plan is settled. It costs a round trip, so **risk triggers it, not size**.

- **Plan first when** the change touches a [risk-floor path](../controls/risk-floor-paths.md) or a contract others consume (API, event, schema), crosses a service boundary, or when the approach is uncertain, the code unfamiliar, or several files must change together. **Skip the plan** when the whole diff can be described in one sentence: a typo, a log line, a rename.
- **Line and file counts are not the trigger.** A size threshold is met by splitting the change; the paths it touches are not.
- **Explore before planning:** read the code that already does something similar, the decisions that bind it (ADRs, `AGENTS.md`) and its tests. The plan follows those patterns or says why it departs.
- **A plan names** the files and interfaces it changes, what is out of scope, the check that proves it works end to end, and, on the risk floor, how it is rolled back. A plan that does not end in a runnable check is a wish.
- **On the risk floor, a person settles the plan before code is written;** elsewhere the agent proceeds after intent confirmation (below).
- **A plan is not evidence that the code follows it.** Agents drift from long plans and specs; the reviewer, in a fresh context, checks the diff against the plan, and change outside it is a finding. v6 had the generating agent validate its own output against the plan; that is self-grading.

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

## Decisions code consumes

The model understands and writes; a **typed decision function** decides; code executes. When code branches on a model's judgment (routing, gating, classification), rule DEC-1 ([`scripts/check-decision-contract.py`](../scripts/check-decision-contract.py)) holds:

- **Closed enum with an abstain the model can choose.** `insufficient_evidence` is one of the options. Never parse prose; never infer abstention from a low score; never gate on a yes/no question, which has no abstain slot and so returns "safe" on missing input (rule-contract G2).
- **Layer.** REVIEW or ADVISORY, never MACHINE ([rule-contract §2](../controls/rule-contract.md)). It may only **raise** scrutiny (a second reviewer, a path proposed for the risk floor), never **lower** what a deterministic gate decided.
- **Acceptance case, mandatory for every new decision function:** empty state ⇒ `insufficient_evidence`, plus one positive control that must still return its expected option. Declare both in a `*.decision.json`; DEC-1 checks the declaration, and `--run <cmd>` runs the cases against the function in the repo's own tests. Sample: [`scripts/fixtures/pr-risk.decision.json`](../scripts/fixtures/pr-risk.decision.json).
- **Burn case (2026-09-24).** A hosted typed-decision service given an **empty** state chose a class at confidence 0.70. With `insufficient_evidence` added it abstained at 1.0 on empty and on nonsense input; the positive control stayed correct. Its yes/no form returned 0.08 ("not sensitive") on empty input: fail-open. The vendor's own guidance (hand off near 0.5) misses this — the failure was high confidence. Its speed and cost claims (up to 200× faster, 400× cheaper) are unverified here.
- **Where it applies (candidates, not adopted):** a PR risk classification as a second, differently-blind check beside the path-based [risk floor](../controls/risk-floor-paths.md) (REVIEW/ADVISORY: model says risky and the paths do not ⇒ second reviewer and a proposed path; it never downgrades); model-tier routing `{cheap, standard, frontier, insufficient_evidence}` (ADVISORY, only after ≥200 human-labelled cases).

Sources: an adopter's research note of 2026-09-24 (§2 table, §2.1 the empty-state case, §2.2 the yes/no fail-open, ruling §3 on layers, 2026-10-02 addendum row J3) and its ecosystem decision record "Machine decision with human fallback", rule R1 ("closed enum … must contain `insufficient_evidence` … never inferred from a low score"; status: proposed).

## What this page does not claim

- "Shorter context is cheaper or better" is a **hypothesis** for this framework. A vendor reports that recall falls as the context grows ("context rot"); the framework has no measured case of its own. The 60-line target is a convention, not a gate.
- v6 attributed the 60-line figure to research. The article it cited recommends under 300 lines and gives its own file of under sixty as an example, not a measurement.
- Claude Code facts here come from the current online docs. An installed version can differ. For example, v2.1.239 does not read `AGENTS.md`. Check with `claude --version` before you rely on a version-gated behavior.

## Sources

From the archive: the rows for this document in [`migration-map/ai-engineering.md`](../migration-map/ai-engineering.md).

Current practice, each opened on the date shown:

- Claude Code docs — Best practices: explore first, then plan, then code; skip the plan when the diff fits in one sentence; give the agent a check it can run; what to include in and exclude from the context file; a rule broken despite a line against it means the file is too long or the rule belongs in a hook — <https://code.claude.com/docs/en/best-practices> (accessed 2026-09-27)
- Anthropic — Effective context engineering for AI agents (context rot; the smallest set of high-signal tokens; just-in-time retrieval; instructions between brittle and vague) — <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents> (accessed 2026-09-27)
- AGENTS.md — the open format (plain Markdown, no required fields; the nearest file in the tree takes precedence) — <https://agents.md/> (accessed 2026-09-27)
- HumanLayer — Writing a good CLAUDE.md (about 150–200 instructions followed consistently; under 300 lines; never send an LLM to do a linter's job; pointers over copies) — <https://www.humanlayer.dev/blog/writing-a-good-claude-md> (accessed 2026-09-27)
- Birgitta Böckeler — Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl (heavy specs overkill for small changes; agents do not follow every instruction) — <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html> (accessed 2026-09-27)
