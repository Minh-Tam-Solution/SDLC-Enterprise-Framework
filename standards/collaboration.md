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
- **Written where the receiver reads it** — the repository, the PR or the issue. A private chat or one machine's agent folder is not a hand-over, and neither is work that exists only on one machine: unpushed commits or a local-only branch.
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
- **What earns an ADR:** a choice that shapes the structure, a dependency between parts, an interface others consume, a quality such as security or availability, or how the system is built (framework, library, tool). A choice inside existing boundaries — an endpoint that follows the pattern, a bug fix, an internal refactor — does not. One decision per ADR, one or two pages; the technical detail goes in a spec that links it.
- **An ADR written after the change says so** and carries the date it was written; it is still worth writing, but it approved nothing. **The reviewer reads the diff against the accepted ADRs:** a change that breaks one is fixed, or a new ADR supersedes the old one first.
- **One decision log** (`docs/09-govern/`, or where `AGENTS.md` says). A chat message becomes a decision when it is copied there with a link; there is no second ledger.
- **A decision names who decided, when, and where** (a link to the PR, issue or message). "The owner decided X", carried over from another session without that source, is a proposal.
- **A replaced decision stays,** marked superseded with a link to its successor. It is never rewritten.
- **The answer to a `NEEDS_DECISION`** is a decision record when it binds future work, and a line in the PR or issue when it does not.
- **Not kept from v6:** ADR review by two named job titles within 48 hours (signing follows the tier, [`lifecycle`](../core/lifecycle.md#who-signs-a-stage-gate)); the context file as the home of the version, sprint history and test count (state is written once, [`documentation.md`](documentation.md#one-home-per-fact)); "shipped" meaning pushed to the main branch with a passing build (merging is the stage 04 exit; shipped is a deploy, stage gate G4 in [`lifecycle`](../core/lifecycle.md#ten-stages-one-question-each)).

## Roles for one to a few people

- **Roles are hats, not headcount.** One person may wear several. What must hold: each change has one author, one responsible reviewer and — where the tier requires one — one approver who is neither the author nor the person operating the author's agent ([`gates.md`](../controls/gates.md#approver-independence)).
- **The person who runs an agent answers for what it ships.** An agent is not accountable and never certifies for a person: it does not add a person's sign-off or approval. The commit records the agent as an assistant and the person as accountable ([`adoption`](../adoption/adoption.md#agent-identity-separate-the-agent-from-the-approver), identity layers). "The agent wrote it" is not a defense in a review, an incident or an audit. How deeply the person reviews follows the risk of the change ([`tiers`](../controls/tiers.md)); some projects require contributors to review every generated line, a stricter choice a project may make.
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
- Michael Nygard — Documenting Architecture Decisions (architecturally significant decisions affect structure, non-functional characteristics, dependencies, interfaces or construction techniques; one or two pages; a reversed decision is marked superseded) — <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions> (accessed 2026-09-28)
- AWS Prescriptive Guidance — Architectural decision record process (an ADR for every architecturally significant decision; accepted ADRs are immutable, a new ADR supersedes; code reviewers check changes against the ADRs and link the one a change violates) — <https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html> (accessed 2026-09-28)
- Hassan et al. — Agentic Software Engineering: Foundational Pillars and a Research Roadmap, arXiv 2509.06216v2 (SASE is Structured Agentic Software Engineering; an agent that needs human input raises a Consultation Request Pack; work is submitted as a Merge-Readiness Pack; how much process the agent follows is set by the coach per task) — <https://arxiv.org/abs/2509.06216> (accessed 2026-09-28)
- Anthropic — Building Effective AI Agents (pause at checkpoints or blockers; stopping conditions) — <https://www.anthropic.com/engineering/building-effective-agents> (accessed 2026-09-26)
- Anthropic — Effective harnesses for long-running agents (progress file, structured updates between sessions) — <https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents> (accessed 2026-09-26)
- Team Topologies — Key Concepts (cognitive load) — <https://teamtopologies.com/key-concepts> (accessed 2026-09-26)
- The Linux Kernel documentation — AI Coding Assistants (agents must not add a sign-off; the human submitter reviews and takes full responsibility; an `Assisted-by` trailer names the tool) — <https://docs.kernel.org/process/coding-assistants.html> (accessed 2026-09-27)
