# Design thinking

> Who reads this: whoever decides what to build, frames a problem, plans a prototype, or asks users anything.
> When: before stage 00 exits, before a feature is scoped, and whenever an agent is about to build something nobody has asked for.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: whoever decides what to build; developers and agents scoping a feature; anyone running user tests
**Review by**: 2026-12-26

*Shortens:* the time spent building things nobody uses.

This is a lens, not a gate ([`constitution.md`](constitution.md)). The evidence it produces is what stages 00–02 already ask for ([`lifecycle.md`](lifecycle.md)); it adds how to get evidence that is worth something.

## Deciding what to build is the bottleneck

Agents make building cheap: a working prototype costs hours. The scarce thing is knowing which prototype is worth building, and that knowledge comes only from users. Keep contact with users at the pace you build — a weekly conversation beats a quarterly study.

*Burn case, from the archive: a product ran for more than two hundred sprints of careful engineering — high coverage, clean reviews — without a single external user evaluating it. Its quality numbers were real; its demand was never measured. A large codebase without user data is unevaluated, not proven.*

## Frame the problem first

- **Write the problem before the solution.** For every proposed solution, ask what problem it solves and for whom.
- **Check that the problem exists for these users.** Industry reports and internal pain are not evidence that *these* people will change behaviour or pay. "We think" and "we already know what users want" are not evidence.
- **The first framing is usually a symptom or a tool.** "We need a better tracking tool" becomes "we cannot trust the data". Reframe until the statement names the need.
- **Frame by the job, not the persona.** People take up a product to get a job done in a circumstance; that circumstance explains the choice better than age or role. A job statement is cheaper than a persona and closer to the cause.
- **Anchor the statement in what users said and did,** quoted or linked, then synthesise.
- **Explore more than one solution before converging.** Diverge and converge twice: once on the problem, once on solutions. Stopping at the first good idea is a failure, not speed.

## Weigh evidence by strength

| Strength | Kind of evidence |
|---|---|
| Near zero | the team's conviction, an opinion, "users would love this" |
| Weak | anecdotes, a survey, "I would use this" |
| Medium | observed behaviour in interviews and tests; past behaviour described in detail |
| Strong | real users using the real thing: usage data, retention, a repeat purchase |

- **Watch what people do; do not believe what they predict they will do.** "Would you use this?" produces the weakest evidence there is.
- **Label stage-00 evidence by its strength**, not only by its presence. A problem backed only by conviction is still an open question.

## Test the riskiest assumptions, not the whole idea

- **Four risks decide a product:** value (will they use or buy it), usability (can they), feasibility (can we build it), viability (does it work for the business). Agents mostly remove feasibility risk; value and viability remain, and they are what discovery should target.
- **Before prototyping, list the few assumptions that would kill the idea if false,** each with a test and a success criterion written *before* the test runs. Test those, not whole ideas: a failed whole-idea test does not say why it failed.
- **Test assumptions, not features.** "Is the button easy to tap?" is usability; "do users trust the automatic check?" decides whether there is a product.
- **Build the cheapest thing that answers the question:** minimum *testable*, not minimum *marketable*. Do not code what a sketch can answer.
- **Write kill criteria in numbers before building** — one for discovery, one for the product ([`constitution.md`](constitution.md), do, try, fail, fix).

## Test with real users

- **Real, representative users in their real context,** including the hard conditions: old devices, poor network, interruptions. Not the team, not friendly proxies.
- **About five users per round finds most usability problems;** run several small rounds between iterations rather than one large study. Use three or four per group when users differ, and around twenty when you need numbers.
- **Facilitate, do not help:** give the task without explaining how, ask the user to think aloud, tolerate silence.
- **Read feedback by what it means.** "I could not do it" outranks "I would like it different". One showstopper blocks shipping, however positive the rest.

## Keep scope honest

- **Every feature traces to the problem statement** and to a user who asked. "What if a customer needs this?" is not a user.
- **Measure progress as time until a real user tries the real thing,** not sprints finished or features completed. Fix the date; cut scope to meet it.
- **Anything new names who uses it and what breaks if it disappears;** otherwise freeze it with a dated review, or remove it ([demand before surface](constitution.md#demand-before-surface)).
- **Discovery never finishes.** What operations learn from real use (stage 07) reopens stage 00. Agents can prepare interview guides and summarise notes; they cannot replace talking to users.

## Sources

From the archive: the rows for this document in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- Andrew Ng — How to Get Through the Product Management Bottleneck (The Batch) — <https://www.deeplearning.ai/the-batch/how-to-get-through-the-product-management-bottleneck> (accessed 2026-09-26)
- Teresa Torres — Opportunity Solution Trees — <https://www.producttalk.org/opportunity-solution-trees/> (accessed 2026-09-26)
- Teresa Torres — Assumption Testing — <https://www.producttalk.org/2023/10/assumption-testing/> (accessed 2026-09-26)
- Marty Cagan — The Four Big Risks — <https://www.svpg.com/four-big-risks/> (accessed 2026-09-26)
- HBS Working Knowledge — Clay Christensen's Milkshake Marketing — <https://www.library.hbs.edu/working-knowledge/clay-christensens-milkshake-marketing> (accessed 2026-09-26)
- Design Council — The Double Diamond — <https://www.designcouncil.org.uk/our-resources/the-double-diamond/> (accessed 2026-09-26)
- Jakob Nielsen — First Rule of Usability? Don't Listen to Users — <https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/> (accessed 2026-09-26)
- Jakob Nielsen — Why You Only Need to Test with 5 Users — <https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/> (accessed 2026-09-26)
- Itamar Gilad — Product Discovery With ICE and The Confidence Meter — <https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/> (accessed 2026-09-26)
