# Integration and data

> Who reads this: whoever designs an API, an event, a file feed or a schema that another system uses — and whoever consumes one, person or agent.
> When: before the first consumer exists, on every change to an interface, and when two systems disagree about a number.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: developers and agents building or consuming APIs, events and shared data; reviewers of interface changes
**Review by**: 2026-12-26

*Shortens:* the time from an interface change to the first consumer that breaks — and the argument, weeks later, about which system's number is right.

What stage 03 must show is in [`core/lifecycle.md`](../core/lifecycle.md) (the contract of each external call; from PROFESSIONAL, contract tests and failure behaviour). Contract tests and the per-endpoint test set are in [`testing.md`](testing.md); expand/contract migrations, versioning what others depend on and the deprecation timeline are in [`change-and-deployment.md`](change-and-deployment.md); checks on inbound integrations are in [`security.md`](security.md). This standard does not repeat them.

## The contract is the source

- **Every interface another system uses has a machine-readable contract** in version control, in the provider's repository: an API description for HTTP, a schema for events, messages and files. It is the interface's one home ([`documentation.md`](documentation.md#one-home-per-fact)); consumers fetch it or generate from it, never keep a hand copy.
  *Burn case: one repository held four copies of the same API description at four versions; a failing test took six hours to trace to the stale copy the tests loaded.*
- **One direction of generation per repository.** Contract-first (code generated from the contract) or code-first (contract generated from code) — either works; both at once does not. CI regenerates in that direction and expects an empty diff.
- **Lint the contract in CI:** it parses, every reference resolves, and each operation has an id, a summary, typed parameters and bodies, its error responses and its security scheme. An operation open to anyone says so explicitly; "no security declared" is a finding, not a public endpoint.
- **Examples are realistic,** not `"string"` or `"foo"`; they document the contract and seed its tests.
- **A human-readable endpoint list is generated from the contract,** never maintained beside it.
- **One error shape across services:** Problem Details (`application/problem+json`: type, title, status, detail, instance), plus the request or trace id so an error joins its logs ([`observability.md`](observability.md)).

## Compatibility

- **Within a major version, change only by adding.** Breaking changes: removing or renaming a field, operation or enum value; changing a type, a default or how a value is serialised; adding a required request field; tightening validation on input that used to pass. Adding an optional field or a new operation is safe when "absent" keeps the old behaviour.
- **Let a machine find breaking changes:** diff the contract against the last released one in CI. A breaking diff needs a new major version or a new operation, and the change record in [`change-and-deployment.md`](change-and-deployment.md#flags-and-releases).
- **Consumers are tolerant readers:** read only the fields they use, ignore unknown fields, and handle an enum value they do not know without failing. Providers never rely on that to slip a breaking change through.
- **Messages outlive code.** For each event stream or stored format, choose a compatibility mode and check new schemas against it: *backward* (new readers read old data — upgrade consumers first), *forward* (old readers read new data — upgrade producers first) or *full* (either order). Where old messages can be replayed, check against every version still readable, not only the last.
- **Only the major version is visible** in the path or the name; old and new majors run side by side through the transition window.
- **Deprecation is machine-readable too:** mark the operation deprecated in the contract; respond with a `Deprecation` header and, once a removal date is set, a `Sunset` header no earlier than it. The dates themselves follow the timeline in [`change-and-deployment.md`](change-and-deployment.md#flags-and-releases).

## Data ownership between systems

- **Each data set has one owning system** — its system of record — which alone writes it. Other systems read through its API or its events, never its tables. A table two services write has no owner, and its schema can no longer change safely.
- **Name the owner of every shared entity** (customer, product, price, employee, account) in the design documents. A consumer may keep a copy only as a cache or projection, labelled as one, with its refresh path and its lag. A wrong value is fixed at the owner, never in the copy.
- **Change and announce atomically.** Write the change and the outgoing message in one transaction (an outbox table) and relay after commit. Writing the database and then the broker loses messages on a crash; writing the broker first announces changes that never happened.
- **Consumers are idempotent.** Delivery is at least once: deduplicate on a message id. A call with a side effect that cannot be undone carries an idempotency key and is controlled before the side effect ([`controls/tiers.md`](../controls/tiers.md), non-compensable harm).
- **Reconcile what two systems both hold.** Where money or stock appears in two systems, a scheduled query compares them and reports the difference; a planted mismatch proves it can see one ([`gates.md`](../controls/gates.md), G1).

## Failure between systems

- **Every outbound call has a timeout,** retries only idempotent operations, with backoff and a cap, and states what the product does while the dependency is down: fail, degrade or queue.
- **A consumer's contract test fails the provider's build** before the provider ships the change ([`testing.md`](testing.md#real-over-fake)); a provider that learns of a break from a consumer's incident has no contract, only a hope.

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md); none is in the rule register.

| Candidate | Command idea |
|---|---|
| contract lint | lint the contract files in CI; a planted unresolved reference must fail |
| breaking change | diff the contract against the last release tag; a breaking change without a major bump is counted |
| generated contract drift | regenerate in the declared direction; expect an empty diff |
| no copied contracts | count files of the contract's kind outside its home; a planted copy must fail and the real home must pass |
| one writer per table | tables written by migrations or queries in more than one repository |
| deprecated without dates | operations marked deprecated with no removal date |

## Sources

From the archive: the rows for this standard in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- OpenAPI Specification v3.1.0 — <https://spec.openapis.org/oas/v3.1.0> (accessed 2026-09-26)
- AIP-180 — Backwards compatibility — <https://google.aip.dev/180> (accessed 2026-09-26)
- RFC 9457 — Problem Details for HTTP APIs — <https://www.rfc-editor.org/rfc/rfc9457> (accessed 2026-09-26)
- RFC 9745 — The Deprecation HTTP Response Header Field — <https://www.rfc-editor.org/rfc/rfc9745> (accessed 2026-09-26)
- Martin Fowler — Tolerant Reader — <https://martinfowler.com/bliki/TolerantReader.html> (accessed 2026-09-26)
- Schema Evolution and Compatibility for Schema Registry on Confluent Platform (compatibility modes) — <https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html> (accessed 2026-09-26)
- microservices.io — Pattern: Database per service — <https://microservices.io/patterns/data/database-per-service.html> (accessed 2026-09-26)
- microservices.io — Pattern: Transactional outbox — <https://microservices.io/patterns/data/transactional-outbox.html> (accessed 2026-09-26)
