# Testing

> Who reads this: whoever writes, reviews or fixes tests — person or agent — and whoever decides what "tested" means for a change.
> When: while writing acceptance criteria, before merging, and when a test fails for no clear reason.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: developers and agents writing or fixing tests; reviewers deciding whether a change is proven
**Review by**: 2026-12-26

*Shortens:* the time between a defect being written and a test catching it — and the false confidence of a green suite that proves nothing.

What each stage must show is in [`core/lifecycle.md`](../core/lifecycle.md) (stages 04–05); known failing tests go into a skip file with owner and expiry ([`controls/gates.md`](../controls/gates.md)). This standard says what a good test is.

## Tests prove requirements

- **Write each requirement as a testable scenario** (Given / When / Then) and name the test level that proves it: unit, integration or end-to-end.
- **Every acceptance criterion traces to at least one test**, and every test file names what it covers (`Covers:` in its header, [`documentation.md`](documentation.md#header-of-a-source-file)). A criterion no test references is untested, whatever the coverage number says.
- **Test the edges, not only the happy path:** boundaries, caps, invalid and negative input, and exact decimal arithmetic for money.
- **Each API endpoint is tested for:** success, duplicate, invalid input, unauthenticated (401), forbidden (403), and one user reaching another user's object. An undocumented endpoint, or a response that differs from the contract, is a finding: fix the contract or the code.

## Real over fake

- **Prefer the real implementation.** When it is not feasible — slow, costly, external — use a fake, owned by whoever owns the real thing and **verified against it by shared contract tests**. Avoid heavy stubbing and interaction-only mocks: they are easy to write and rarely find bugs.
- **Risk-floor behaviour is tested through the real code:** token validation, role checks, tenant isolation, money calculations and database constraints ([`controls/risk-floor-paths.md`](../controls/risk-floor-paths.md)). A double there hides exactly the failure that matters. *Burn case: a suite passed while authentication was bypassed and authorisation simulated — over a hundred mocks sat in the security and auth tests.*
- **Database behaviour is tested on the production database engine,** with the real migrations applied, data built by factories, and each test isolated by rollback.
- **A "temporary" double gets an owner and an expiry,** like a skipped test. Without them it is permanent.
- **Production code contains no stand-ins:** no always-succeeding payment call, no empty body, no hard-coded response, no in-memory map posing as a database.
- **Between services, use consumer-driven contract tests:** each consumer states what it relies on; the provider runs those expectations on every build.

## A green suite must mean something

- **Coverage finds untested code; it is not a target.** Report the changed lines no test executes. A coverage percentage as a goal is met with tests that assert nothing — and agents meet any number set for them.
- **Show skipped and expected-failure tests next to any coverage figure.** *Burn case: a suite at 94% coverage had quietly gathered 78 skip markers.*
- **A flaky test is a defect.** Passing on a retry is not a fix: once people ignore one red test, they ignore the healthy ones too. Move it to a quarantine list with an owner and an expiry, cap the list, and fix or delete within the expiry.
- **Check the tests themselves:** mutation testing on the changed lines, at review time, shows whether the tests would notice the code being wrong. Start it as a report.
- **Use property-based tests for invariants** — totals, rounding, idempotency, round-trips — where examples written by the same author that wrote the code tend to miss the edge.
- **Test quality beats test shape.** The right mix of unit, integration and end-to-end is the one whose tests run fast, run reliably and fail only for useful reasons; do not argue percentages per level.

## Agents and tests

Agents optimise for a passing run, and asking them not to game it barely helps. The check lives outside the agent.

- **An agent fixing a failure must not delete tests, add skip markers or weaken assertions.** CI flags any of these in a diff; a test-file change inside a "fix" gets its own look.
- **Protect test and scoring code.** Changes to eval sets, fixtures that define "correct", and test harness code are reviewed like production code.
- **On risk-floor paths, commit the tests first and show them failing** before the implementation — the history then shows the tests were not fitted to the code.
- **A fix-and-retest loop is bounded:** after three attempts the agent stops and hands over with the root cause it found.
- **Features whose behaviour comes from a model are evaluated in levels:** cheap assertions on every change; graded evals against the eval set ([`core/constitution.md`](../core/constitution.md)) on a set cadence; comparisons in production only after significant changes. Expensive evals run behind an explicit switch and a budget, not on every commit. Keep reading real traces.

## Test data and environments

- **One canonical seed data set** for the team, built by factories — not ad-hoc data per developer.
- **Test data holds no real personal data.** Use generated data; if production data is ever needed, anonymise it first.
- **Tests against production are read-only** and use credentials that cannot write.
- **Runtime artifacts** — tokens, raw result files — are ignored by git; only the report is kept, and CI runs are the evidence, not dated report files.
- **Diff-based test selection is fine**, except that changes to shared infrastructure — migrations, configuration, middleware, CI — run the full suite.

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md).

| Candidate | Command idea |
|---|---|
| no weakened tests in a fix | diff: removed assertions, new skip markers, deleted test files |
| skip count beside coverage | count skip/expected-failure markers in the report |
| doubles on risk-floor modules | flag patching of risk-floor modules inside tests |
| stand-ins in production code | syntax-tree scan of non-test code, with a planted positive control |
| criterion without a test | acceptance-criterion ids with no test referencing them |
| flaky quarantine | list with owner, expiry and a cap, checked like the skip file |

## Sources

Harvested from `archive/` (rows in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md)). Current practice: test doubles and fakes (abseil.io/resources/swe-book, chapter 13); consumer-driven contracts, test shapes, test coverage and non-determinism in tests (martinfowler.com); mutation testing at scale (research.google/pubs/state-of-mutation-testing-at-google); property-based testing (hypothesis.works); reward hacking by AI models (metr.org, 2025-06-05); evals for model-driven features (hamel.dev/blog/posts/evals).
