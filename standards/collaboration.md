# Collaboration and hand-over

> Who reads this: whoever hands work to someone else — person to person, agent to person, person to agent, one session to the next — and whoever is asked to decide.
> When: before stopping work that someone else will continue, when an agent cannot go on, and when a decision is made that others will build on.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: people and agents handing over or escalating work; whoever answers an escalation or records a decision
**Review by**: 2026-12-26

*Shortens:* the time a receiver spends reconstructing what the sender knew — and the time an agent spends guessing at a decision that was never its to make.

Sized for a team of one to a few people, often with agents. What the framework does not build — RACI matrices, escalation levels by org chart, assignment software — is in [`core/constitution.md`](../core/constitution.md#what-the-framework-does-not-build); coordination is one table and a 15-minute weekly look (L2 in the same file). The session hand-over artifact is in [`context-and-hats`](../ai-engineering/context-and-hats.md) (Tier 3), the checkpoint and one-line escalation in [`templates/agent/PREAMBLE-example.md`](../templates/agent/PREAMBLE-example.md), agent caps and logged hand-overs in [`observability.md`](observability.md#agents-in-operation). This standard does not repeat them.

## Hand-over

- **State, not history:** done (with evidence — commit, PR, CI run), open, blockers, decisions each with its source, known concerns, next action. The list is the Tier 3 artifact; use it for people too.
- **Written where the receiver reads it** — the repository, the PR or the issue. A private chat or one machine's agent folder is not a hand-over.
- **A hand-over is finished when the receiver confirms it,** not when the sender sends it. Until the receiver says "I have it", the sender still owns the work. A structured hand-over with the receiver reading back the essentials is one of the few collaboration practices with measured outcomes.
- **The receiver re-checks before acting.** A hand-over is a claim, not evidence: re-read the files it names and re-run its check. If the branch moved since the checkpoint, diff the checkpoint against the current state first.
- **After acceptance the receiver owns the ending** — one of the four statuses below.
- **Person to agent:** the brief states the problem, who uses the result and what "done" means ([`context-and-hats`](../ai-engineering/context-and-hats.md), intent confirmation). An agent does not start a high-tier task on an ambiguous brief.
- **From one person to a small team** is a hand-over of artifacts, not a change of process ([`controls/tiers.md`](../controls/tiers.md#solo-vs-small-team-is-a-measured-state)).

## How a task ends

Every task — a person's or an agent's — ends in exactly one of four statuses. "Mostly done", a silent timeout and a stalled session are not endings.

| Status | Means | Carries | Then |
|---|---|---|---|
| `DONE` | acceptance criteria met | what changed and the evidence | the tier's gates and review |
| `DONE_WITH_CONCERNS` | criteria met, with risks the author would not sign alone | each concern with a severity; the follow-up proposed | a person acknowledges the concerns before it counts as done |
| `BLOCKED` | cannot go on until someone *acts*: access, a credential, a broken dependency or environment | what blocks, who can unblock it, the suggested next step, partial progress | stop and hand over |
| `NEEDS_DECISION` | can go on only after a *choice* or information that belongs to a person: an ambiguous requirement, several valid approaches with lasting consequences, an action outside the granted scope | the question, two or three options with their trade-offs, a recommendation, what waiting costs | stop that line of work; continue anything not blocked by it |

- **These are about your own task.** A review of someone else's work uses the typed verdict — `approve`, `changes_requested`, `insufficient_evidence` ([`context-and-hats`](../ai-engineering/context-and-hats.md)).
- **An agent at a cap ends `BLOCKED`,** never by retrying until something passes ([`observability.md`](observability.md#agents-in-operation)).
- **Ask before you guess.** An agent does not decide business rules, tenant isolation, money handling, data classes or a contract change on its own; it ends `NEEDS_DECISION`.
- **Check what the repository already answers first** — `AGENTS.md`, the ADRs, the issue. A `NEEDS_DECISION` that the docs answer is a docs finding; a repeated one on the same topic means the brief or `AGENTS.md` lacks something — fix that source.
- **The ask is specific:** "I need a decision on X by Y because Z", with the evidence (file and line, or the command run). "I need help" is not an ask.
- **Urgent does not mean undocumented.** An emergency fix may act first; its record follows within 48 hours ([`change-and-deployment.md`](change-and-deployment.md#change-classes)).

## Decisions

- **A decision that is expensive to reverse is recorded before the work,** as an ADR: context, decision, consequences, alternatives rejected ([`documentation.md`](documentation.md)). Written after the code, it is a story, not a decision.
- **One decision log** (`docs/09-govern/`, or where `AGENTS.md` says). A chat message becomes a decision when it is copied there with a link; there is no second ledger.
- **A decision names who decided, when, and where** (a link to the PR, issue or message). "The owner decided X", carried over from another session without that source, is a proposal.
- **A replaced decision stays,** marked superseded with a link to its successor. It is never rewritten.
- **The answer to a `NEEDS_DECISION`** is a decision record when it binds future work, and a line in the PR or issue when it does not.

## Roles for one to a few people

- **Roles are hats, not headcount.** One person may wear several. What must hold: each change has one author, one responsible reviewer and — where the tier requires one — one approver who is neither the author nor the person operating the author's agent ([`gates.md`](../controls/gates.md#approver-independence)).
- **Each open item has one owner** — the person who answers for it. Two owners is none.
- **Technical authority is not change authority.** A structural change — moving folders, restructuring a codebase, replacing part of the stack — goes through its decision record first, whoever proposes it.
  *Burn case: a structural move of thousands of files, made without a record or a notice, left documents and code out of step and the rest of the team unable to find files; putting it right took longer than the decision would have.*
- **Bound the load, not the process.** When one person carries too many things in flight, cut the things in flight; adding meetings, channels or levels adds load.

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md); none is in the rule register.

| Candidate | Command idea |
|---|---|
| hand-over accepted | hand-over records with no receiver confirmation after a set number of days |
| task has an ending | agent run records and PR descriptions carry one of the four statuses |
| decision has a source | decision records carry who, when and a link |
| record before structure | a PR that moves or renames more than a set number of files links a decision record |
| stale escalations | `BLOCKED` and `NEEDS_DECISION` older than their deadline appear in the weekly digest |

## Sources

From the archive: the rows for this standard in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- Google SRE Book — Managing Incidents (explicit hand-over of command, clear roles) — <https://sre.google/sre-book/managing-incidents/> (accessed 2026-09-26)
- AHRQ PSNet — Changes in medical errors after implementation of a handoff program (structured hand-over; 23% relative reduction in preventable adverse events) — <https://psnet.ahrq.gov/issue/changes-medical-errors-after-implementation-handoff-program> (accessed 2026-09-26)
- Michael Nygard — Documenting Architecture Decisions — <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions> (accessed 2026-09-26)
- Anthropic — Building Effective AI Agents (pause at checkpoints or blockers; stopping conditions) — <https://www.anthropic.com/engineering/building-effective-agents> (accessed 2026-09-26)
- Anthropic — Effective harnesses for long-running agents (progress file, structured updates between sessions) — <https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents> (accessed 2026-09-26)
- Team Topologies — Key Concepts (cognitive load) — <https://teamtopologies.com/key-concepts> (accessed 2026-09-26)
