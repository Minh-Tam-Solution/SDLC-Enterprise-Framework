# SDLC Change Management Standard

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Status**: ACTIVE - Production Standard
**Authority**: CTO Office
**Industry Standards**: ITIL 4, ISO 20000

---

## Purpose

Define **change management processes** to minimize risk while enabling rapid delivery. Changes are controlled, not blocked.

---

## Change Types

### Standard Change (Pre-Approved)

```yaml
Definition:
  - Low risk, well-understood changes
  - Follow documented procedure
  - Pre-approved by change authority

Examples:
  - Security patches (critical/high)
  - Dependency updates (minor versions)
  - Configuration changes (documented)
  - Scheduled maintenance

Approval: None required (pre-approved template)
Lead Time: Immediate to 24 hours
Documentation: Change log entry
```

### Normal Change (Requires Approval)

```yaml
Definition:
  - Medium risk changes
  - Require assessment and approval
  - Follow standard change process

Examples:
  - New feature deployments
  - Major dependency updates
  - Infrastructure changes
  - Database schema changes

Approval: CAB or delegated authority
Lead Time: 24-72 hours
Documentation: Change request + review
```

### Emergency Change (Expedited)

```yaml
Definition:
  - Urgent fix for production incident
  - Cannot wait for normal process
  - Higher risk accepted for speed

Examples:
  - P0 bug hotfix
  - Security vulnerability patch
  - Data corruption fix
  - Service outage recovery

Approval: Post-hoc CAB review (within 48h)
Lead Time: Immediate
Documentation: Incident + change record
```

---

## Change Management by Tier

### LITE Tier (1-2 people)

```yaml
Process:
  - Informal change tracking
  - Git commits as change log
  - No formal approval process

Documentation:
  - Commit messages describe changes
  - README updates for major changes
```

### STANDARD Tier (3-10 people)

```yaml
Process:
  - Pull request as change request
  - Code review as approval
  - Merge = deployment approval

Documentation:
  - PR description includes:
    - What changed
    - Why it changed
    - How to test
    - Rollback plan (for significant changes)

Approval Authority:
  - Standard: Code reviewer (1+)
  - Infrastructure: Tech Lead
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Process:
  - Formal change request for significant changes
  - CAB-lite review (async or sync)
  - Change calendar for coordination

Documentation:
  - Change Request Template (see below)
  - Risk assessment
  - Rollback procedure
  - Communication plan

Approval Authority:
  - Standard: Code reviewers (2+)
  - Normal (feature): Tech Lead + PM
  - Normal (infra): CTO or delegate
  - Emergency: On-call lead (post-hoc review)

CAB-Lite:
  - Async review via PR/ticket for most changes
  - Sync meeting weekly for complex changes
  - Attendees: Tech Leads, PM, QA Lead
```

### ENTERPRISE Tier (50+ people)

```yaml
Process:
  - Full CAB process for significant changes
  - Change freeze periods (before major releases)
  - Change windows (scheduled deployment times)

Documentation:
  - Full Change Request
  - Impact assessment
  - Test evidence
  - Rollback tested and documented
  - Communication sent to stakeholders

Approval Authority:
  - Standard: Pre-approved templates
  - Normal: CAB approval
  - Emergency: Emergency CAB (CTO + Security + On-call)

CAB (Change Advisory Board):
  - Weekly meeting (or as needed)
  - Attendees: CTO, Tech Leads, Security, QA, PM
  - Reviews all Normal changes
  - Authority to approve, reject, or defer
```

---

## Change Request Template

```markdown
# Change Request: [Title]

## Summary
**Change Type**: Standard / Normal / Emergency
**Requested By**: [Name]
**Date**: [YYYY-MM-DD]
**Target Date**: [YYYY-MM-DD]

## Description
### What is changing?
[Describe the change]

### Why is this change needed?
[Business justification]

### What is the expected outcome?
[Success criteria]

## Impact Assessment
### Affected Systems
- [System 1]
- [System 2]

### Affected Users
- [User group and count]

### Risk Level
- [ ] Low - Minimal impact, easily reversible
- [ ] Medium - Some impact, reversible with effort
- [ ] High - Significant impact, complex rollback

### Dependencies
- [Upstream: None / List]
- [Downstream: None / List]

## Implementation Plan
### Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Timeline
- Start: [Time]
- Duration: [X minutes/hours]
- Completion: [Time]

## Rollback Plan
### Trigger Conditions
- [When to rollback]

### Rollback Steps
1. [Step 1]
2. [Step 2]

### Rollback Time
- Estimated: [X minutes]

## Testing
### Pre-deployment
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Staging deployment verified

### Post-deployment
- [ ] Health check passing
- [ ] Key metrics stable
- [ ] No new errors in logs

## Communication
### Pre-change
- [Who to notify before]

### Post-change
- [Who to notify after]

## Approval
| Role | Name | Decision | Date |
|------|------|----------|------|
| Tech Lead | | Approve/Reject | |
| PM | | Approve/Reject | |
| CAB | | Approve/Reject | |
```

---

## Risk Scoring Matrix

### Risk Factors

```yaml
Impact (1-5):
  1: No user impact
  2: Minor inconvenience, workaround exists
  3: Moderate impact, degraded service
  4: Major impact, feature unavailable
  5: Critical, service down

Likelihood (1-5):
  1: Very unlikely (<5%)
  2: Unlikely (5-20%)
  3: Possible (20-50%)
  4: Likely (50-80%)
  5: Very likely (>80%)

Risk Score = Impact × Likelihood

Risk Level:
  1-5: Low (Green) - Standard process
  6-12: Medium (Yellow) - Enhanced review
  13-25: High (Red) - CAB required
```

### Risk Mitigation Requirements

```yaml
Low Risk (1-5):
  - Standard deployment process
  - Basic rollback plan
  - Post-deployment monitoring

Medium Risk (6-12):
  - Detailed rollback plan (tested)
  - Staged rollout (canary or blue-green)
  - Extended monitoring period
  - Communication to stakeholders

High Risk (13-25):
  - CAB approval required
  - Full rollback plan (tested in staging)
  - War room during deployment
  - Immediate rollback trigger defined
  - Executive notification
```

---

## Change Windows

### Production Change Windows (ENTERPRISE)

```yaml
Preferred Windows:
  - Tuesday-Thursday, 10:00-14:00 (low traffic)
  - Tuesday-Thursday, 22:00-02:00 (maintenance window)

Avoided:
  - Friday afternoon (reduced support)
  - Monday morning (peak traffic)
  - Month-end (business critical)
  - Holiday periods

Change Freeze:
  - 2 weeks before major releases
  - During critical business periods
  - Emergency changes only during freeze
```

---

## Rollback Requirements

### Rollback Criteria

```yaml
When to Rollback:
  - Error rate increases >5% after deploy
  - Latency p95 increases >50%
  - Critical functionality broken
  - Security vulnerability introduced
  - Customer-reported P0 issues

Rollback Decision Authority:
  - On-call engineer: Can rollback immediately
  - No approval needed for automated rollback triggers
```

### Rollback Verification

```yaml
Before Deployment (PROFESSIONAL+):
  □ Rollback procedure documented
  □ Rollback tested in staging
  □ Database rollback tested (if applicable)
  □ Rollback time < [X minutes] verified

After Rollback:
  □ Service health confirmed
  □ No data loss verified
  □ Incident created for investigation
  □ Post-mortem scheduled if needed
```

---

## Deployment Strategies

### Strategy Selection

```yaml
Direct Deployment:
  When: Low risk, small changes
  Rollback: Redeploy previous version

Rolling Deployment:
  When: Stateless services, medium risk
  Rollback: Continue rolling to previous version

Blue-Green:
  When: Need instant rollback, higher risk
  Rollback: Switch traffic to blue (previous)

Canary:
  When: High risk, need gradual validation
  Rollback: Route all traffic away from canary

Feature Flags:
  When: Large features, A/B testing
  Rollback: Disable flag (instant)
```

---

## Change Audit

### Audit Log Requirements

```yaml
Required Fields:
  - Change ID
  - Timestamp
  - Requester
  - Approver(s)
  - Change type
  - Description
  - Systems affected
  - Outcome (success/failure/rollback)

Retention:
  - STANDARD: 90 days
  - PROFESSIONAL: 1 year
  - ENTERPRISE: 3-7 years (compliance dependent)
```

### Change Metrics

```yaml
Track Monthly:
  - Total changes by type
  - Change success rate
  - Change failure rate (CFR)
  - Mean time to deploy (lead time)
  - Rollback frequency
  - Emergency change percentage

Targets:
  - Change success rate: >95%
  - CFR: <15% (DORA Elite)
  - Emergency changes: <5% of total
```

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for PROFESSIONAL+ tiers
**Last Updated**: December 5, 2025
**Owner**: CTO Office
