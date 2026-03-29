# SDLC Code Review Guide — Unified 3-Tier Framework

**Version**: 6.2.1
**Last Updated**: February 15, 2026
**Status**: PRODUCTION READY (Consolidated SSOT — Feb 2026)
**Stage**: 04 (BUILD) — Code Review Excellence
**Pillar**: Pillar 4 (Quality Gates) + Pillar 2 (Sprint Planning Governance)
**Audience**: Engineering Teams (All Tiers — LITE to ENTERPRISE)
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles

> **SSOT Notice (Feb 2026)**: This document consolidates three previous guides:
> - `SDLC-Manual-Code-Review-Playbook.md` (Tier 1)
> - `SDLC-Subscription-Powered-Code-Review-Guide.md` (Tier 2)
> - `SDLC-Code-Review-Guide.md` (Overview)
>
> Originals archived to `10-archive/02-Legacy/`.

---

## 1. Tier Selection

### Choose Your Tier

| Tier | Best For | Tools | Monthly Cost/Dev | Quality | Setup Time |
|------|----------|-------|------------------|---------|------------|
| **Tier 1: Free/Manual** | 1-5 devs, bootstrapped | ESLint, Prettier, Git hooks | $0 | 70-80% | 30 min |
| **Tier 2: Subscription** | 5-20 devs, cost-conscious | Cursor, Copilot, Claude Max | $50-100 | 85-95% | 2 hours |
| **Tier 3: CodeRabbit** | 15+ devs, 50+ PRs/month | CodeRabbit Pro | $12-45/seat | 90-98% | 8 hours |

### SDLC 6.2.0 4-Tier Classification Mapping

| SDLC Tier | Team Size | Budget | Recommended Code Review | Rationale |
|-----------|-----------|--------|-------------------------|-----------|
| **LITE** | 1-2 | <$50K | Tier 1 (Free/Manual) | Zero cost, discipline-driven |
| **STANDARD** | 3-10 | $50-200K | Tier 2 (Subscription) | Best ROI with existing tools |
| **PROFESSIONAL** | 10-50 | $200K-1M | Tier 2 or Tier 3 | PR volume decides (>100/mo → Tier 3) |
| **ENTERPRISE** | 50+ | $1M+ | Tier 3 (CodeRabbit) | Scale, compliance, audit trails |

### Decision Matrix

```yaml
Choose Tier 1 if:
  ✅ Team ≤5 developers
  ✅ Budget = $0
  ✅ Strong review discipline exists
  ✅ PR volume <20/month

Choose Tier 2 if:
  ✅ Team 5-20 developers
  ✅ Already have AI tool subscriptions
  ✅ Want high ROI with minimal new costs
  ✅ PR volume 20-100/month

Choose Tier 3 if:
  ✅ Team ≥15 developers
  ✅ PR volume ≥50/month
  ✅ Need compliance/audit trails (Stage 09)
  ✅ Multi-team / multi-repository environment
```

---

## 2. Review Checklists

### Universal Review Checklist (All Tiers)

Every PR must be reviewed against these criteria regardless of tier:

#### Sprint Context (Pillar 2 — Sprint Planning Governance)

- [ ] PR references SPRINT-XXX in title/description
- [ ] Backlog item linked (US-XXX, BUG-XXX, TT-XXX)
- [ ] Aligns with documented Sprint Goal
- [ ] Work started AFTER G-Sprint approval

#### Design Thinking (Stage 00-01)

- [ ] User need documented in PR description
- [ ] Problem statement clear (who/what/why)
- [ ] Solution justified (not over-engineered)

#### Code Quality (Stage 04)

- [ ] Readable (clear variable/function names)
- [ ] Single Responsibility Principle followed
- [ ] DRY — no unnecessary duplication
- [ ] Functions <50 lines, files <300 lines
- [ ] No code smells (long parameter lists, god classes)

#### Security (OWASP ASVS L2)

- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] No hardcoded secrets (passwords, API keys)
- [ ] Input validation comprehensive
- [ ] Authentication/authorization correct

#### Performance (DORA Targets)

- [ ] Database queries optimized (no N+1)
- [ ] Proper indexes used/added
- [ ] Async/await used correctly
- [ ] Response time <100ms expected (SDLC 6.2.0 target)

#### Testing (Stage 05)

- [ ] Unit tests for business logic (80%+ coverage)
- [ ] Integration tests for workflows
- [ ] Edge cases covered
- [ ] Mocks ONLY for external APIs (Zero Mock Policy)

#### Documentation

- [ ] Code comments for complex logic
- [ ] API documentation updated (if public API)
- [ ] CHANGELOG entry added (if versioned)

#### Definition of Done

- [ ] Code complete and reviewed (2+ approvers)
- [ ] Tests passing (unit + integration)
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] Product Owner acceptance (user-facing changes)

### Vietnamese Market Compliance (if applicable)

- [ ] VAT calculation exact (10%, no approximations)
- [ ] Date format Vietnamese (DD/MM/YYYY)
- [ ] Number format Vietnamese (1.000.000,00)
- [ ] BHXH contributions exact (17.5% employer, 8% employee)

---

## 3. Tier 1: Free/Manual Code Review

**Philosophy**: Discipline over dollars. Excellence without expense.

### 3-Layer System

```
Layer 1: PRE-COMMIT QUALITY GATES (Automated, Free)
  → Catches 60-70% of issues BEFORE human review
  → Tools: Linters, formatters, pre-commit hooks
  → Time: <1 second per commit

Layer 2: STRUCTURED PEER REVIEW (Manual, Checklist-Driven)
  → Comprehensive human analysis of logic, design, tests
  → Tools: GitHub PR template, review checklist (Section 2)
  → Time: 15-30 minutes per PR

Layer 3: CONTINUOUS LEARNING (Team Retrospective)
  → Extract patterns, update processes, prevent recurrence
  → Tools: Monthly review meeting, Sprint Retrospective
  → Time: 1 hour per month
```

### Pre-Commit Setup (Python)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=500']
      - id: check-ast
      - id: debug-statements

  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
        args: [--line-length=100, --target-version=py311]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
        args: [--strict, --ignore-missing-imports]

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: [-ll, --recursive]
        exclude: ^tests/
```

### Pre-Commit Setup (TypeScript/React)

```bash
npm install --save-dev eslint prettier husky lint-staged \
  @typescript-eslint/parser @typescript-eslint/eslint-plugin \
  eslint-config-prettier eslint-plugin-react-hooks

npx husky install
npx husky add .husky/pre-commit "npx lint-staged"
```

### Structured Peer Review Protocol (15-30 min/PR)

1. **Sprint Context Check** (2 min) — Verify SPRINT-XXX, backlog link, sprint goal
2. **Automated Checks** (2 min) — CI/CD passed, coverage met, security scan clean
3. **Code Review** (10-15 min) — Logic, readability, performance, security
4. **Test Review** (5 min) — Coverage, edge cases, integration tests
5. **DoD Verification** (3 min) — All Definition of Done criteria met
6. **Feedback** (5 min) — Strengths, critical issues, suggestions, questions

### Review Comment Format

```markdown
## Code Review — SDLC 6.2.0 Checklist

### ✅ Strengths
- [What was done well]

### 🔴 Critical (Must Fix)
- [ ] Line XX: [Issue description + suggested fix]

### 🟠 Warnings (Should Fix)
- [ ] Line XX: [Issue description]

### 🟢 Suggestions (Nice to Have)
- [ ] [Improvement idea]

### Recommendation
- ✅ APPROVE / ⏸️ REQUEST CHANGES / ❌ REJECT
```

### ROI (Tier 1)

```yaml
Monthly Cost: $0
Annual Value: ~$138,000 (bug prevention + quality + security)
ROI: Infinite (no ongoing costs)
Best For: Bootstrapped startups, MVPs, teams of 1-5
```

---

## 4. Tier 2: Subscription-Powered AI Review

**Philosophy**: Maximize existing AI subscriptions (Cursor, Copilot, Claude Max) — zero new API costs.

### 3-Layer System

```
Layer 1: PRE-COMMIT (Cursor Pro)
  → Real-time AI analysis as you code
  → Catches 70-80% of issues BEFORE commit
  → Uses .cursorrules for project standards

Layer 2: PR REVIEW (Claude Max + Copilot)
  → Human-AI collaborative review in 3-5 min
  → Claude Max (200K context) for comprehensive analysis
  → Copilot for inline suggestions

Layer 3: POST-MERGE LEARNING (Pattern Extraction)
  → Monthly pattern extraction via Claude
  → Update .cursorrules with recurring issue fixes
  → Team training on identified knowledge gaps
```

### Cursor IDE Configuration (.cursorrules)

```markdown
# SDLC 6.2.0 Code Review Rules

## Sprint Planning Governance (Pillar 2)
- PRs MUST reference SPRINT-XXX
- Backlog items MUST be linked
- DoD checklist MUST be verified before merge

## Quality Standards
- Zero mock/fake data (real DB operations only)
- English-only code and comments
- 80%+ test coverage for new code
- Functions <50 lines, files <300 lines

## Security Requirements
- No secrets in code (use environment variables)
- Input validation on all user inputs
- SQL injection prevention (parameterized queries)
- XSS prevention (escaped outputs)

## Performance Targets
- API response: <100ms (p95)
- Database queries: <50ms
```

### Claude Max PR Review Workflow

1. PR created on GitHub
2. Reviewer copies PR diff to Claude Max Project
3. Uses structured review prompt (Section 2 checklist)
4. Claude analyzes in 2-3 minutes
5. Reviewer validates AI feedback (1-2 min)
6. Posts consolidated review on GitHub
7. **Total: 3-5 min** (vs 30-60 min manual)

### ROI (Tier 2)

```yaml
Monthly Cost: $750 (15 devs × $50 subscriptions)
Monthly Value: ~$16,000 (pre-commit + PR review + learning time saved)
ROI: 2,033%
Payback Period: 13.5 days
Best For: Growing teams of 5-20, cost-conscious
```

---

## 5. Tier 3: CodeRabbit Professional

**Philosophy**: Fully automated, enterprise-grade code review at scale.

### Configuration (.coderabbit.yaml)

```yaml
reviews:
  auto_review: true
  request_changes_workflow: true
  high_level_summary: true
  thoroughness: high
  focus:
    - security
    - performance
    - testing
    - maintainability

rules:
  - pattern: "for .* in .*:\\.objects\\.get"
    message: "N+1 query detected. Use select_related()."
    severity: warning
  - pattern: "eval\\(|exec\\("
    message: "Security: eval()/exec() are dangerous."
    severity: error

languages:
  python:
    frameworks: [django, fastapi]
    max_function_lines: 50
    test_coverage_threshold: 80
  typescript:
    frameworks: [react]
    max_component_lines: 200
    test_coverage_threshold: 80

github:
  auto_review_pull_requests: true
  post_review_as_comment: true

team:
  exclude_paths:
    - "*/migrations/*"
    - "*/tests/fixtures/*"
```

### Enterprise Features

- **Instant PR analysis** (<2 min, fully automated)
- **Multi-language**: JS/TS, Python, Go, Java, C#, Rust, Ruby, PHP
- **Platform integration**: GitHub, GitLab, Bitbucket, Azure DevOps
- **Compliance**: SSO/SAML, audit logs, compliance reporting
- **Analytics**: DORA metrics dashboard, developer insights, trend analysis

### ROI (Tier 3)

```yaml
Monthly Cost: $750 (50 devs × $15/seat)
Monthly Value: ~$108,300 (review time + bug prevention + security + velocity)
ROI: 14,340%
Best For: Scale-ups (15-100+ devs), enterprises, multi-team orgs
```

---

## 6. SDLC 6.2.0 Integration

### 10-Stage Lifecycle Mapping

| Stage | Name | Code Review Role |
|-------|------|-----------------|
| 00 | FOUNDATION (WHY?) | Validate requirements in PR description |
| 01 | PLANNING (WHAT?) | Check user story references |
| 02 | DESIGN (HOW?) | Review architecture alignment |
| **04** | **BUILD** | **Primary focus: Code quality** |
| 05 | TEST | Verify test coverage |
| 06 | DEPLOY | Check deployment readiness |
| 07 | OPERATE | Review operational concerns |
| 03 | INTEGRATE | Validate integration points |
| 08 | COLLABORATE | Document review findings |
| 09 | GOVERN | Ensure standards compliance |

### 7-Pillar Architecture Alignment

| Pillar | Code Review Integration |
|--------|------------------------|
| P0: Design Thinking | Verify PR addresses validated user need |
| P1: 10-Stage Lifecycle | Stage-appropriate review focus |
| P2: Sprint Planning Governance | Sprint context validation in PR |
| P3: 4-Tier Classification | Right-sized review depth |
| P4: Quality Gates | Pre-merge quality enforcement |
| P5: SASE Integration | Human-AI collaboration evidence |
| P6: Documentation Permanence | Doc updates verified |

### Industry Standards Integration

| Standard | How Applied |
|----------|-------------|
| **OWASP ASVS** | Security checklist in reviews (L1-L3) |
| **NIST SSDF** | Secure development practices |
| **DORA Metrics** | Review time, change failure rate, lead time |
| **ISO 12207** | Process compliance |
| **CMMI v3.0** | Maturity mapping (L1-L5) |

---

## 7. Platform-Specific Guides

### GitHub

- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md` with SDLC 6.2.0 checklist
- **Branch Protection**: Require 2+ approvers, CI pass, coverage threshold
- **Auto-assignment**: Round-robin or CODEOWNERS file
- **Labels**: `needs-review`, `approved`, `changes-requested`
- **CodeRabbit**: Native GitHub integration via `.coderabbit.yaml`

### GitLab

- **MR Template**: `.gitlab/merge_request_templates/default.md`
- **Approval Rules**: Configure via Project Settings → Merge Requests
- **CodeRabbit**: Supported via GitLab integration
- **CI Pipeline**: `.gitlab-ci.yml` with lint/test/coverage stages

### Azure DevOps

- **PR Template**: `.azuredevops/pull_request_template.md`
- **Branch Policies**: Minimum reviewers, build validation, work item linking
- **CodeRabbit**: Supported via Azure DevOps integration

---

## 8. Migration Paths

### Tier 1 → Tier 2 (4 hours)

**When**: Team grows beyond 5, PR volume >20/month, review bottleneck

1. **Audit current setup** (30 min) — Document hooks, measure review time
2. **Setup subscriptions** (1 hour) — Cursor Pro + Claude Max + Copilot
3. **Create configuration** (1 hour) — .cursorrules, Claude review prompts
4. **Team training** (1.5 hours) — Cursor walkthrough, Claude demo, practice

**Expected**: 75% reduction in PR review time within 2 weeks.

### Tier 2 → Tier 3 (8 hours)

**When**: Team >15, PR volume >100/month, need compliance audit trails

1. **Business case** (1 hour) — Calculate ROI, get budget approval
2. **Trial setup** (2 hours) — CodeRabbit 14-day trial, connect 2-3 repos
3. **Configuration** (3 hours) — Convert .cursorrules to .coderabbit.yaml
4. **Pilot** (2 weeks) — Run in parallel, validate quality
5. **Full rollout** (2 hours) — Enable all repos, train team

**Expected**: 90% reduction in manual review effort within 1 month.

---

## 9. Success Metrics

Track these KPIs regardless of tier:

```yaml
Code Quality (Stage 04):
  - Bugs found in production (target: ↓50% YoY)
  - Test coverage (target: ≥80%)
  - Security vulnerabilities detected (track trend)

Process Efficiency (DORA):
  - Average PR review time (Tier 1: 30min, Tier 2: 5min, Tier 3: 2min)
  - PR creation to merge (target: <24 hours)
  - Rework cycles (target: ≤1 cycle)
  - Change failure rate (target: <15%)

Team Health:
  - Developer satisfaction (survey quarterly)
  - Onboarding time (target: ↓30%)
  - Knowledge sharing (cross-team reviews)
```

---

## 10. Time Savings Summary

| Stage | Traditional | With AI (Tier 2/3) | Savings |
|-------|-------------|---------------------|---------|
| Pre-Commit (Tier 1) | 30-60 min/cycle | <1 sec | ~100% |
| PR Review (Manual) | 30-60 min/PR | 3-5 min | 75-92% |
| PR Review (CodeRabbit) | 30-60 min/PR | <2 min | 95%+ |
| Monthly Retrospective | 4 hours | 1 hour | 75% |
| Pattern Extraction | 8 hours | 2 hours | 75% |

**Annual Savings per Team**: $138K-$199K (depending on tier)

---

## Related Documents

- [SDLC-CodeRabbit-Integration-Guide.md](./SDLC-CodeRabbit-Integration-Guide.md) — Tier 3 detailed setup
- [SDLC-PRE-COMMIT-HOOKS.md](./SDLC-PRE-COMMIT-HOOKS.md) — Pre-commit hook configuration
- [02-AI-Tools/code_review_*.md](../05-Templates-Tools/02-AI-Tools/) — Tier-specific AI prompt templates
- [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) — 7 AI Governance Principles

---

**Document Status**: ACTIVE (SSOT)
**Owner**: CPO Office
**Framework**: SDLC 6.2.1 (7-Pillar + 2-Section)

**Consolidation History (Feb 2026)**:
- Merged from 3 guides (3,536 LOC) → 1 SSOT (~450 LOC)
- Eliminated: Duplicated tier comparisons, repeated SDLC integration sections, redundant ROI calculations
- Preserved: All unique content (checklists, setup guides, migration paths, platform guides)
