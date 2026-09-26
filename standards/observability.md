# Observability and operations

> Who reads this: whoever runs a service in production, writes its logging and alerts, is on duty for it, or lets agents act on it.
> When: before the first real user, when an alert fires, and after every incident.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: developers and agents running services; whoever is on duty; incident reviewers
**Review by**: 2026-12-26

*Shortens:* the time from something breaking to someone knowing — and from knowing to users being safe.

What stage 07 must show by tier is in [`core/lifecycle.md`](../core/lifecycle.md); incident records, `price_paid` and `rule_ref` are in [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md); the deploy log and rollback rule are in [`controls/gates.md`](../controls/gates.md). Every service with real users has at least the stage-07 minimum: an uptime check and error logs someone reads.

## Signals

- **Measure what users feel:** for each service, request rate, errors and duration; report latency as percentiles (p50, p95, p99), never as an average.
- **For each resource** — CPU, memory, disk, connections, queues — check utilisation, saturation and errors. Saturation is where capacity problems show first.
- **Across services, carry one trace context through every hop**, queues included, in the standard trace-context header, so one request can be followed end to end.

## Logs

- **Every log line is machine-readable** and carries timestamp (ISO 8601), level, service, request or trace id, and message; errors add the error type and stack. Use the standard trace and span id fields so logs join traces without guessing.
- **Never log secrets or personal data:** no passwords, tokens, session ids, keys or card data. Agent-written logging code readily dumps whole request objects — check it.
- **Always log security events:** logins and failures, authorisation denials, validation failures, access to sensitive data, configuration changes. Where money or personal data is involved, this log is append-only and tamper-evident, and kept as long as the law requires.
- **Debug logging is off in production** unless someone is actively troubleshooting.

## Alerts

- **Page on symptoms, not causes.** Wake a person for what users feel — errors, latency, unavailability, a service-level objective at risk. High CPU or memory is a cause: use it to diagnose, not to page.
- **Every page is actionable.** If the right response is always the same, automate it and stop paging.
- **Three classes:** *page* (a person now), *ticket* (working hours), *log* (record only). Each alert rule declares its class.
- **Every page names a runbook, an owner and the next person to escalate to**, with a time limit before escalating.
- **Test that a monitor can fire:** at ship time, plant a failure and check that it reaches the log and a human. A monitor that has never fired proves nothing ([`gates.md`](../controls/gates.md), G1).
- **Monitoring configuration lives in version control**, and the running configuration is compared with it, so nobody switches an alert off without it showing.

## Objectives and error budgets

From PROFESSIONAL up, each user-facing service has a few service-level objectives, set from what users need rather than from current performance, measured by a probe.

- **Write the error-budget policy before you need it:** when the budget is spent, changes other than fixes for that service and security fixes stop until it is back within objective. This is the brake on autonomous deploys.
- **Alert on how fast the budget burns**, over a short and a long window together, so a sharp outage pages quickly and a slow leak opens a ticket instead of waking someone.
- **Low-traffic services** do not give a meaningful rate: add synthetic traffic or combine services, and say "not measured" rather than "healthy".

## Health checks

- **Liveness and readiness are separate.** Liveness answers "restart me?" and fails only on an unrecoverable fault in the process itself. Readiness answers "send me traffic?" and may depend on what the service needs.
- **A liveness check calls no external dependency.** If it checks the database, a database blip restarts — or rolls back — healthy code. Automatic rollback reads the new release's own health, not its dependencies'.
- **Back up and prove it:** a backup counts once a timed restore from it has succeeded.

## Incidents

- **Contain first, explain later.** The first two questions: *can we roll back?* and *what changed recently?* — the deploy log answers the second.
- **Record how the incident was detected:** by a monitor, by a user, or by the author. "A user found it first" is itself a finding about monitoring.
- **Review blamelessly after any of:** user-visible degradation beyond the objective, data loss, a rollback or other on-duty intervention, resolution slower than the agreed limit, or a monitoring failure. Look for structures and assumptions, never for a person to blame. Every review ends with follow-up actions that have owners and dates.
- **Update the runbook before closing** when the incident showed a new cause, or record why it did not change.
- **Fix everywhere, not only where it broke:** run the new check across every repository that could have the same pattern.
- A rollback or emergency change always ends with an incident record ([`standards/change-and-deployment.md`](change-and-deployment.md)).

## Agents in operation

- **Caps:** each agent session has a spend cap, a retry cap and a delegation-depth cap. At 80% of the budget a person is told; at a cap the agent stops and hands over instead of retrying.
- **Traces:** each agent run is one trace — one span per model call and per tool call — so "what did it do, with what, how long, at what cost" can be answered afterwards. Hand-overs between agents are logged with both identities.
- **Content off by default:** prompts, tool arguments and outputs are not copied into telemetry unless someone turns it on for a reason; they carry the same data they operate on. The conventions for agent telemetry are still changing; treat them as `ADVISORY`.
- **Pause at a sensitive boundary:** before an action that touches authentication, payment or personal data, a long-running agent saves its state and waits for a person.

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md).

| Candidate | Command idea |
|---|---|
| monitor can fire | planted error and test alert in the deploy-tree harness; assert they arrive |
| paging alert completeness | each page rule has runbook, owner, escalation and a service-level indicator |
| monitoring config drift | diff running alert configuration against the repository |
| log hygiene | secret scan over a sample of emitted logs, with a planted token as positive control |
| liveness independence | liveness handler makes no outbound call |
| detection source | incident records carry `detected_by: monitor, user or author` |

## Sources

Harvested from `archive/` (rows in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md)). Current practice: monitoring distributed systems, service-level objectives, error-budget policy, alerting on SLOs, postmortem culture (sre.google — the public SRE book and workbook); the USE method (brendangregg.com/usemethod.html); OpenTelemetry logs data model and generative-AI semantic conventions (opentelemetry.io); OWASP Logging Cheat Sheet (cheatsheetseries.owasp.org); delivery metrics (dora.dev/guides/dora-metrics); liveness, readiness and startup probes (kubernetes.io documentation — the principle applies to any runtime).
