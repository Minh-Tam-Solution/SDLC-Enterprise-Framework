# Constitution

> Who reads this: anyone proposing a rule, a gate, a tool or a new doc for v7.
> When: before you write it. If your proposal breaks a line here, change this file first — by PR.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: anyone proposing a rule, gate, tool or document
**Review by**: 2026-12-26

## The first rule

> No feature is promoted from *experiment* to *default* because it sounds right.
> It must beat the baseline on your eval set, or handle an invariant a model cannot be trusted with.

*Shortens:* the list of things that run on every change.

## Four assets you own

| Asset | Owned because |
|---|---|
| **Policy** | intent outlives any vendor; adapters die, policy must not die with them |
| **Repo knowledge** | no vendor has your domain, your sources, your users |
| **Runnable gates** | only a command you own gives exit codes your meaning |
| **Eval set** | without it, "better" is an opinion |

Everything else is rented. Rent what a vendor ships; build only what nobody else can.

## Six verbs on one methodology base

| Verb | Who does it | Layer |
|---|---|---|
| **EXECUTE** | vendor agents (CLI, subagents, skills, hooks) | L1 in-session |
| **GUIDE** | policy + generated adapters + repo knowledge | L2 work |
| **CONSTRAIN** | gates (`MACHINE` / `REVIEW` / `ADVISORY`) | L2 work |
| **COMPARE** | eval set | L2 work |
| **OBSERVE** | traces work already leaves: PRs, CI runs, deploy log | L2 work |
| **DECIDE** | people | L3 management |

The methodology (this repo) sits under all six. Its thinking lenses — [systems thinking](systems-thinking.md) and [design thinking](design-thinking.md) — stay `ADVISORY`: they shape the questions a review asks and never block.

| Layer | Example | Owner |
|---|---|---|
| **L1** in-session execution | an agent spawns a researcher and a tester | vendor — do not compete |
| **L2** work coordination | who takes the next item, who reviews, what is blocked | a table + a 15-minute weekly ritual; AI proposes, people assign |
| **L3** management | priorities, accepted risk, who works on what | people |

## A control enters the framework only if it answers four questions

1. Who runs it? 2. When? 3. What does it detect or block? 4. **If it is wrong, what does a false positive cost?**
No enforcement, no evidence and no decision value ⇒ not in v7. Question 4 is mandatory for every `MACHINE` gate.

## Principles

| Principle | Means | Shortens |
|---|---|---|
| **Bounded price to learn** | give agents autonomy where a mistake is cheap; write the ceiling of the price before you pay it; every price paid becomes a burn case | waiting for approval on low-risk work |
| **Not seen ≠ absent. Green ≠ measured.** | a negative result needs a positive control; a gate needs an output for "cannot measure" | time spent trusting clean-looking zeros |
| **The owner's account is not an exception; an agent in my session is not me.** | owners pass the same gates; an agent acting with an owner's credential is not an owner's approval | the audit you do after a self-approved change |
| **Do, try, fail, fix** | start at the lowest step with a counter; let failure be cheap and leave a trace (burn case → selftest); kill criteria say "failed" in numbers | big design up front |
| **Proportional to risk** | the right process is sized to the risk of the artefact, not to the organisation | ritual on sandboxes |
| **Docs follow traces** | documentation is generated from PRs, CI and evidence, not written ahead of the work | docs that nobody reads and nothing checks |

## Demand before surface

Agents make producing code, documents, gates and tools almost free; that is exactly why each one must earn its place.

- **Every artifact names its consumer and the job that breaks without it** — a document, gate, template, tool, role, ritual, or an agent's new skill or command. "Future adopters" is not a consumer; "compliance with §X" is not a job.
- **No consumer yet: do not build it,** or keep it only with a dated trigger and a default outcome. No trigger: remove it.
- **No template before its first real instance.** A gate with no named decider is a checklist. A number no decision moves on is dropped. A ceremony that produces no new evidence is dropped. A review of a review is removed: one responsible reviewer, one approver.
- **Rigour is measured by use, not by artifact count,** and a principle proves itself when a decision it did not author cites it ([systems-thinking](systems-thinking.md#measures-get-gamed)).
- **Build the smallest thing that is used,** then measure the outcome — not lines, files or tickets ([`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md#never-measure-agent-output-as-progress)).
- **A manual clean-up with nothing to hold it drifts back.** It is finished when a check keeps it clean.

## What the framework does NOT build

A closed list. Adding to it needs a recorded decision.

- In-session orchestration, agent runtimes, schedulers, queues.
- Servers or dashboards. Use the channels people already read.
- Coordination for large teams: RACI matrices, sprint governance, assignment software. Not even a thin version "for later".
- Adapters for a tool without a named consumer.
- A second ledger for anything that already has one (decisions, deadlines, incidents).
- Collectors before identity is clean. Fix identity at the source first ([`adoption`](../adoption/adoption.md)).

*Shortens:* the framework itself. v6.x grew to 189 live docs; nobody could say which were still true.
