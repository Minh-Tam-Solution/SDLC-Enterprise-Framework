# Systems thinking

> Who reads this: whoever reviews an incident, designs a rule or a gate, sets a metric, or decides how agents and people work together.
> When: when something happens twice, when a fix is about to be "be more careful", and before adding any new rule.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: incident reviewers; rule and gate authors; whoever designs how agents and people work
**Review by**: 2026-12-26

*Shortens:* the number of times the same kind of failure comes back in a new form.

This is a lens, not a gate ([`constitution.md`](constitution.md)): it shapes the questions a review asks. Nothing here blocks a change, and no document is required to prove it was used.

## Look below the event

Read what happened on four levels. Each level asks a different question.

| Level | Question |
|---|---|
| Event | What happened? |
| Pattern | Has it happened before, and under what conditions? |
| Structure | Which process, tool, incentive or rule allowed it — or produced it? |
| Belief | What assumption made that structure seem acceptable? |

- **Structure drives behaviour.** A fix aimed at people ("be more careful", "write better tests", "add another reviewer") is the weakest response. A fix aimed at the environment — a deterministic fixture, a check in CI, a narrower permission — lasts.
- **A policy does not change a belief.** To change an assumption, change the incentive and let people see the new behaviour working.
- **Our own rules are structures too.** When a failure repeats, ask first whether an existing rule, gate or context file produced it, before adding another.
- **AI speeds up whatever belief is already there.** "Agent output is accepted without an independent look" is a structure; "the agent is usually right" is the belief behind it.

## Contributing factors, not the root cause

- **A failure in a complex system has several contributing factors,** not one root cause. A review that stops at one cause produces one rule and misses the rest. List the factors; fix the ones with the most leverage.
- **Hindsight makes the wrong step look obvious.** Judge a decision by what the person or agent knew at the time.
- **Look for structures and assumptions, never for someone to blame** ([`standards/observability.md`](../standards/observability.md)). Blame hides the next occurrence.
- **Fix everywhere the pattern can occur,** not only in the repo where it broke.
- **Not every bug needs this.** Go below the event for a production incident, a failure seen three times, a near-miss caught in review or staging, a problem that crosses repositories, or a failure produced by an agent.
- **A near-miss is worth reviewing even though it cost nothing.** It enters the record as `rule_ref: reference`; a rule row still needs a burn case with a price paid ([`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md)).

## Where to push

Interventions differ in power. From weakest to strongest: adjusting a number · adding a buffer · shortening a delay · strengthening a feedback loop · changing who sees what information · changing a rule · changing a goal · changing the underlying assumption.

- **Tuning a threshold is the weakest move.** When a gate misfires, first ask whether the right people see the count, or whether the rule itself is wrong.
- **Match the speed of sensing to the speed of change.** A delay only matters relative to how fast the system changes. Agents change code in minutes; a weekly counter or a monthly review cannot steer that. Per-change drift needs a per-change check.
- **Relieve one binding constraint at a time.** Find what slows real delivery this week, apply the smallest fix, measure whether lead time or quality moved, then look again.

## Measures get gamed

- **When a measure becomes a target, it stops being a good measure.** The more a number drives decisions, the more pressure there is to move the number instead of the thing. Agents optimise hard against whatever the loop rewards: coverage, green checks, closed tickets.
- **Pair every enforced number with a red case and an outcome.** A gate proves it can go red ([`controls/gates.md`](../controls/gates.md)); a delivery metric is read next to what users experienced.
- **Evidence that a principle works comes from an independent decision,** not from its own authors citing it.
- **Watch the ratio of governance work to product work.** Governance can grow faster than the product and still look like progress.

## Pick the method for the kind of problem

| Kind | Cause and effect | Do |
|---|---|---|
| Clear | obvious | follow the known practice; a rule fits |
| Complicated | knowable with analysis | analyse, then decide; ask an expert |
| Complex | visible only afterwards | run small experiments that are safe to fail, watch, adjust |
| Chaotic | none visible | act to stabilise first, then sense |

A new agent workflow is usually complex: run it as a bounded experiment with kill criteria ([`adoption/adoption.md`](../adoption/adoption.md)), not as a rule.

## Agents and people in one system

- **With agents, the human job moves from writing to designing the loop:** define the task, let the agent produce, validate automatically, review independently, feed what reviewers keep correcting back into the agent's context ([`ai-engineering/context-and-hats.md`](../ai-engineering/context-and-hats.md)).
- **Automation leaves people the hardest part and less practice at it.** Reviewers who no longer write lose the skill they need to catch what the agent got wrong. Keep people authoring some real work, and treat very fast approvals as a signal ([`controls/tiers.md`](../controls/tiers.md)).
- **"More artifacts means more rigour" is a belief that produces theatre.** A gate with nobody deciding on it, a score no decision depends on, a review of a review: each is a structure to remove.

## Sources

From the archive: the rows for this document in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- Donella Meadows — Leverage Points: Places to Intervene in a System — <https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/> (accessed 2026-09-26)
- Richard I. Cook — How Complex Systems Fail — <https://how.complexsystems.fail/> (accessed 2026-09-26)
- Google SRE Book — Postmortem Culture: Learning from Failure — <https://sre.google/sre-book/postmortem-culture/> (accessed 2026-09-26)
- Goodhart's law (Strathern's formulation; Campbell's law) — <https://en.wikipedia.org/wiki/Goodhart%27s_law> (accessed 2026-09-26)
- Cynefin framework (Snowden) — <https://en.wikipedia.org/wiki/Cynefin_framework> (accessed 2026-09-26)
- NPC — The Iceberg Model — <https://www.thinknpc.org/resource-hub/systems-practice-toolkit/the-iceberg-model/> (accessed 2026-09-26)
- Ironies of Automation (Bainbridge, 1983) — <https://en.wikipedia.org/wiki/Ironies_of_Automation> (accessed 2026-09-26)
