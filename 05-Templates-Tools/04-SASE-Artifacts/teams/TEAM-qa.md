---
team: qa
archetype: qa
sdlc_framework: "6.2.1"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter - Quality Assurance Team

## Mission

Own the **VERIFY** — the final checkpoint before deployment. Ensure code meets requirements, passes quality standards, has no mock implementations, and is production-ready.

## Coverage

| SDLC Stage | Responsibility |
|------------|---------------|
| 05-Verify | Integration tests, E2E tests, quality gate enforcement |

## Leader

**@tester** — Owns quality verification. Final say on whether code meets acceptance criteria and quality standards.

## Members

| Role | Responsibility | When Active |
|------|---------------|-------------|
| @tester | Integration tests, E2E tests, coverage verification | Stage 05 |
| @reviewer | Code quality review, standards compliance, doc sync | Stage 05 |
| @cso | Security scan validation, OWASP ASVS L2 checklist, dependency audit | Stage 05 (advisory, PRO+ tier) |

## Gates

| Gate | Stage | Team Role | Criteria |
|------|-------|-----------|----------|
| G3 | 05 | Proposer (joint: tester + reviewer) | Ship-ready: tests pass, coverage met, zero mocks, docs synced |

### G3 Requires Both Sign-offs

G3 is the **joint responsibility** of @tester, @reviewer, and @cso (PRO+ tier):
- @tester verifies: functional correctness, test coverage, integration tests
- @reviewer verifies: code quality, standards compliance, design doc consistency
- @cso verifies: SAST passed, 0 critical CVEs, OWASP ASVS L2, secrets clean (PRO+ tier)

All active members must approve for G3 to pass.

## Workflow

```
1. @tester receives completed sprint from Dev team (post G-Sprint)
   └── Input: implemented code, unit tests, review approvals

2. @tester writes integration and E2E tests
   └── Deliverable: test suites covering acceptance criteria

3. @tester runs full test suite
   └── Verify: all tests pass, coverage thresholds met

4. @tester performs Zero Mock Detection scan
   └── Scan for: TODO, FIXME, placeholder, mock returns, empty bodies

5. @reviewer performs final quality review
   └── Verify: code quality, security checklist, design doc consistency

6. Both sign off → Submit for G3 gate
```

## Delegation Rules

The **@tester** (leader) coordinates QA work:

- `[@reviewer: Code quality review needed for <feature>. Focus on security and doc sync]`
- `[@reviewer: Please verify design doc consistency after recent bug fixes]`

Escalation (out of team):

- `[@coder: Test failure in <area> — fix needed: <details>]`
- `[@pjm: QA blocked — missing test environment / test data]`
- `[@architect: Design inconsistency found — <description>]`

## Policies

### Zero Mock Detection (MANDATORY)

Every QA cycle MUST include a scan for mock implementations:
- `// TODO: Implement later`
- `pass  # placeholder`
- `return { mock: true }`
- `throw new Error("Not implemented")`
- Empty function bodies
- Hardcoded fake data

**Any mock found = G3 BLOCKED. Code returns to Dev team for fix.**

### Coverage Thresholds

| Tier | Minimum Coverage | Enforcement |
|------|-----------------|-------------|
| LITE | Core logic tested | Self-assessed |
| STANDARD | 70% | Automated check |
| PROFESSIONAL | 80% | Automated + reviewer sign-off |
| ENTERPRISE | 90% | Automated + dual sign-off |

### Post-Fix Design Doc Sync

After finding and fixing test-related issues, @tester checks if design documentation needs updating:
- Test reveals missing requirements → update requirements.md
- Test reveals undocumented behavior → update TS-XXX
- Test reveals design inconsistency → escalate to @architect

### Post-Sprint Documentation Sync

After sprint testing is complete, @tester updates ONLY:
- `MASTER-TEST-PLAN.md` — test section, counts, regression table (tester OWNS this)
- `CURRENT-SPRINT.md` — test results summary

@tester does NOT update:
- `roadmap.md` — product doc, only @pm/@ceo updates
- `SPRINT-INDEX.md` — sprint tracking, @pjm updates

After updating, @tester notifies: `[@pm: Sprint <N> QA complete — update roadmap]` and `[@pjm: Sprint <N> QA complete — update SPRINT-INDEX, test count: +<N>]`.

### Handoff to Ops
When G3 passes:
```
[@ops: G3 passed for <release>. Quality verified.
Coverage: <X>%. All acceptance criteria met.
Ready for deployment.]
```

## Tier Availability

| Tier | Available |
|------|-----------|
| LITE | No (use @fullstack) |
| STANDARD | Yes (leader: @reviewer, since no @tester in STANDARD) |
| PROFESSIONAL | Yes |
| ENTERPRISE | Yes |
