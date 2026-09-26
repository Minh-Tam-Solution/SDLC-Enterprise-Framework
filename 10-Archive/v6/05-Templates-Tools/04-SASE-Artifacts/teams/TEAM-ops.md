---
team: ops
archetype: ops
sdlc_framework: "6.4.0"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter - Operations Team

## Mission

Own the **SHIP** and **RUN** — reliable deployments, infrastructure management, and operational excellence. Nothing goes to production without verified health checks and rollback capability.

## Coverage

| SDLC Stage | Responsibility |
|------------|---------------|
| 06-Deploy | Deployment automation, release management, environment configs |
| 07-Operate | Monitoring, incident response, operational health |

## Leader

**@devops** — Owns deployment and operations. Final say on deployment strategy and production readiness.

## Members

| Role | Responsibility | When Active |
|------|---------------|-------------|
| @devops | Deployment pipelines, infrastructure, monitoring | Stage 06-07 |
| @coder | Deployment scripts, infrastructure-as-code support | Stage 06 (advisory) |
| @cso | Deployment security sign-off, SBOM verification, secrets rotation | Stage 06 (advisory, PRO+ tier) |

## Gates

| Gate | Stage | Team Role | Criteria |
|------|-------|-----------|----------|
| G4 | 06 | Proposer | Deployment verified, production ready, rollback documented |

### G4 Checklist

- [ ] All prior gates passed (G1, G2, G-Sprint, G3)
- [ ] Deployment pipeline tested
- [ ] Environment configuration verified
- [ ] Health checks defined and passing
- [ ] Monitoring and alerting configured
- [ ] Rollback procedure documented and tested
- [ ] On-call schedule confirmed
- [ ] Security sign-off from @cso (PRO+ tier): SBOM clean, 0 critical CVEs, AGPL verified

## Workflow

```
1. @devops receives QA-verified release from QA team (post-G3)
   └── Input: tested code, coverage reports, quality sign-offs

2. @devops prepares deployment
   └── Verify: deployment pipeline, environment config, health checks

3. @devops executes deployment (staging first, then production)
   └── Strategy: blue-green or canary per project config

4. @devops monitors post-deployment health
   └── Check: error rates, latency, resource usage

5. Submit for G4 gate review
```

## Delegation Rules

The **@devops** (leader) coordinates operations work:

- `[@coder: Need deployment script update for <change>]`
- `[@coder: Infrastructure-as-code change needed for <requirement>]`

Escalation (out of team):

- `[@cto: Infrastructure escalation — <critical issue>]`
- `[@pjm: Deployment blocked — <reason>]`
- `[@qa: Post-deployment issue found — need regression test]`

## Policies

### No Deploy Without G3
Production deployments require all prior gates to pass. No shortcuts.

### Rollback Capability
Every deployment MUST have a tested rollback procedure. No one-way deployments.

### Post-Fix Design Doc Sync
After fixing infrastructure issues, @devops checks if documentation needs updating:
- Deployment procedure changed → update deployment docs
- Environment config changed → update infra specs
- Monitoring thresholds changed → update runbooks

### Incident Response
```
1. Detect (monitoring alerts)
2. Assess severity (P1/P2/P3)
3. Mitigate (rollback or hotfix)
4. Communicate ([@team: Incident status])
5. Post-mortem (root cause analysis)
```

## Tier Availability

| Tier | Available |
|------|-----------|
| LITE | No (use @fullstack) |
| STANDARD | No |
| PROFESSIONAL | No |
| ENTERPRISE | Yes |
