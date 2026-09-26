---
document_id: "TRAINING-MODULE-05"
title: "Module 05: Development Workflow"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "4 hours (7 parts)"
audience: "All team members — developers, pod leads, architects"
prerequisite: "Module 01-04 (SDLC Overview, Six Pillars, Zero Mock, Code Quality)"
format: "Lecture + Live Demo + Hands-on Exercises"
---

# Module 05: Development Workflow

> **Core principle**: "Code without a branch strategy is code without a safety net." Git workflow, CI/CD, and SASE integration form the backbone of every delivery.

---

## 1. Workflow Overview (20 minutes)

The SDLC 6.3.0 development workflow is **Integration-First** with SASE collaboration. Every feature follows this path:

```
BRS (intent) -> Design -> API Contract -> Build -> Test -> Review -> Deploy -> Monitor
     SE4H         SE4H      SE4H/SE4A     SE4A    SE4A    SE4H      SE4A      SE4H
```

### Workflow Principles

| Principle | Description |
|-----------|-------------|
| **Integration-First** | API contracts finalized before code (Stage 03 before 04) |
| **SASE Collaboration** | SE4H guides, SE4A executes, BRS-to-VCR flow |
| **Zero Mock** | Real data and real services from day one |
| **Quality-First** | Tests written alongside code, 80%+ coverage |
| **Conventional Commits** | Structured commit messages for traceability |

---

## 2. Git Workflow (45 minutes)

### Branch Strategy

```
Main branches:
  main     — Production-ready code, protected, requires PR
  develop  — Integration branch, CI/CD runs on every push

Feature branches:
  Format: feature/{ticket-id}-{short-description}
  Examples:
    feature/PROJ-123-bhxh-calculator
    feature/PROJ-456-vat-integration

Bugfix branches:
  Format: bugfix/{ticket-id}-{short-description}
  Examples:
    bugfix/PROJ-321-decimal-precision
    bugfix/PROJ-654-phone-validation

Hotfix branches:
  Format: hotfix/{ticket-id}-{description}
  Examples:
    hotfix/PROJ-999-critical-calculation-fix
```

### Commit Message Convention

```
Format: <type>(<scope>): <description>

Types:
  feat:     New feature
  fix:      Bug fix
  docs:     Documentation only
  style:    Code style (formatting, no logic change)
  refactor: Code refactoring
  test:     Adding or updating tests
  chore:    Maintenance tasks

Examples:
  feat(bhxh): add employer contribution calculator
  fix(vat): correct decimal precision issue
  docs(api): update BHXH endpoint documentation
  test(calculator): add edge case tests for salary cap
  refactor(service): optimize database query performance
```

### Pull Request Process

```
PR Creation:
  1. Create feature branch from develop
  2. Implement feature with tests
  3. Push branch to remote
  4. Create PR using template

PR Template:
  ## Description
  Brief description of changes

  ## Type of Change
  - [ ] Bug fix
  - [ ] New feature
  - [ ] Breaking change
  - [ ] Documentation update

  ## Testing
  - [ ] Unit tests added (>=80% coverage)
  - [ ] Integration tests added
  - [ ] Manual testing completed

  ## Checklist
  - [ ] Zero Mock Policy verified
  - [ ] Performance tested (<50ms)
  - [ ] Documentation updated
  - [ ] Code review requested

PR Merge Requirements:
  - At least 1 human approval
  - All CI checks passing
  - No unresolved comments
  - Zero Mock scan passed
```

---

## 3. Code Review Framework (45 minutes)

### 3-Tier System

| Tier | Who Reviews | Time | When to Use | Tools |
|------|------------|------|-------------|-------|
| **Tier 1** | Developer + AI assist | 30-60 min | Small changes, hotfixes | GitHub PR + Copilot |
| **Tier 2** | AI reviewer + human approval | 10-15 min | Standard features | Claude Code |
| **Tier 3** | Automated tools + human oversight | <2 min | Large PRs, frequent changes | CodeRabbit, SonarQube |

### Code Review Checklist

```
Functionality:
  [ ] Feature works as described
  [ ] Edge cases handled correctly
  [ ] Error handling complete

Quality:
  [ ] Test coverage >=80% for new code
  [ ] Zero mock violations: none
  [ ] Code style compliant (black/flake8/eslint)
  [ ] No TODO/FIXME in core functionality

Performance:
  [ ] API response <50ms verified
  [ ] No N+1 query problems
  [ ] Database indexes appropriate

Security:
  [ ] Input validation present
  [ ] Authentication/authorization correct
  [ ] No sensitive data in logs
  [ ] SQL injection prevention verified
```

### Review Rules

1. **At least one human approval** is always required — AI review alone is not sufficient.
2. **Self-review first** — use AI to catch issues before creating the PR.
3. **Feature branches live at most 1 week** — if longer, split into smaller tasks.
4. **AI cannot approve PRs** — SE4H (human) always gives final approval.

---

## 4. CI/CD Pipeline (45 minutes)

### Pipeline Stages

| Stage | Tool | Duration | Fail Condition |
|-------|------|----------|----------------|
| 1. Lint | black, flake8, eslint | ~1 min | Any lint error |
| 2. Test | pytest, jest (with coverage) | ~5 min | Coverage <80% or test failures |
| 3. Zero Mock Scan | Custom scanner | ~30 sec | Any mock pattern found |
| 4. Security Scan | bandit, npm audit | ~2 min | High severity issues |
| 5. Build | Docker | ~3 min | Build failure |
| 6. Deploy (Staging) | Docker Compose | ~2 min | Smoke test failure |
| 7. Deploy (Production) | Docker Compose | ~2 min | Requires approval + all gates |

### Pipeline Configuration Example

```yaml
# Simplified GitHub Actions workflow

quality-check:
  steps:
    - name: Lint
      run: |
        black --check .
        flake8 .
        eslint src/

    - name: Test
      run: |
        pytest --cov=src --cov-fail-under=80

    - name: Zero Mock Scan
      run: |
        python scripts/check_zero_mock.py

    - name: Security Scan
      run: |
        bandit -r src/
        npm audit --audit-level=high

deploy-staging:
  needs: quality-check
  if: github.ref == 'refs/heads/develop'
  steps:
    - name: Deploy to staging
      run: docker compose -f docker-compose.staging.yml up -d
```

### Key Rules

- **Staging is never skipped** — every change goes through staging before production.
- **Pipeline failures block merge** — no exceptions, even for "urgent" fixes.
- **Production deployment requires** — all gates passed + human approval.

---

## 5. Environment Management (20 minutes)

### Three Environments

| Environment | Purpose | Database | URL |
|-------------|---------|----------|-----|
| **Development** | Local development | Local PostgreSQL | localhost:8000 |
| **Staging** | Integration testing | Dedicated PostgreSQL | staging.domain.com |
| **Production** | Live environment | Production PostgreSQL | app.domain.com |

### Environment Variables

```
Required variables:
  DATABASE_URL          PostgreSQL connection string
  REDIS_URL             Redis connection string
  SECRET_KEY            Application secret key
  JWT_SECRET_KEY        JWT signing key
  ALLOWED_HOSTS         Allowed host list

Security rules:
  - NEVER commit .env files to git
  - Use secrets management (Vault, AWS Secrets Manager)
  - Rotate keys on a regular schedule
  - Different secrets per environment
```

---

## 6. SASE Integration in Daily Workflow (30 minutes)

### The BRS-to-VCR Flow

```
Step 1 — BRS (BriefingScript):
  Creator:  SE4H (Human)
  Content:  Feature description, requirements, acceptance criteria
  Example:  "Implement BHXH calculator with exact 17.5%/8% rates"

Step 2 — LPS (LoopScript):
  Creator:  SE4A (AI)
  Content:  Implementation plan, step-by-step execution
  Example:  "1. Create service  2. Add tests  3. Create API endpoint"

Step 3 — CRP (Consultation Report Protocol):
  Creator:  SE4A (AI) when uncertain
  Content:  Question, options considered, impact of each
  Example:  "Should salary cap be 36M or 29M VND for 2025?"

Step 4 — MRP (Merge Request Protocol):
  Creator:  SE4A (AI)
  Content:  Summary, tests, performance, zero mock verification
  Required: For every PR

Step 5 — VCR (Validation Certificate Report):
  Creator:  SE4H (Human)
  Content:  Validation results, approval status
  Final:    Human always gives final decision
```

### Daily Development Flow

```
Day 1 — Planning:
  Morning:  Review BRS, create LPS, design database schema
  Afternoon: Design API contracts, review with team, get approval

Day 2-3 — Development:
  Morning:  Implement with AI assistance, write unit tests
  Afternoon: Code review (Tier 2/3), address feedback, integration tests

Day 4 — Testing and Deploy:
  Morning:  E2E testing, performance verification, create MRP
  Afternoon: Deploy to staging, QA verification, deploy to production

Day 5 — Monitor:
  Monitor production, address issues, update docs, complete VCR
```

---

## 7. Hands-on Exercises (35 minutes)

### Exercise 1: Write Correct Commit Messages (10 minutes)

For each scenario, write the correct conventional commit message:

**1.** You added a new BHXH calculator endpoint to the HR module.
**2.** You fixed a bug where VAT was calculated with floating point instead of Decimal.
**3.** You updated the API documentation for the invoice endpoints.
**4.** You refactored the user service to use connection pooling.

### Exercise 1 Answers

**1.** `feat(hr): add BHXH calculator endpoint`
**2.** `fix(vat): use Decimal instead of float for VAT calculation`
**3.** `docs(api): update invoice endpoint documentation`
**4.** `refactor(user-service): implement connection pooling`

### Exercise 2: PR Review Simulation (25 minutes)

A teammate submits a PR with the following issues. Identify each issue and state which checklist item it violates:

```
- File named "BhxhCalculator.py" (PascalCase)
- Test coverage at 65%
- Contains: users_db = {} (in-memory dict)
- Has a comment: # tinh bhxh
- No input validation on salary parameter
- API response time measured at 120ms
```

### Exercise 2 Answers

| Issue | Checklist Violation |
|-------|-------------------|
| `BhxhCalculator.py` | File naming: Python must be snake_case (`bhxh_calculator.py`) |
| 65% test coverage | Test coverage: minimum 80% required |
| `users_db = {}` | Zero Mock Policy: in-memory mock database |
| `# tinh bhxh` | Code style: comments must be in English only |
| No input validation | Security: input validation required |
| 120ms response | Performance: must be <100ms at p95 |

**Verdict**: PR must be rejected. Fix all 6 issues before re-review.

---

## Reference Materials

| Document | Location |
|----------|----------|
| Sprint Governance | `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md` |
| Quality Gates Framework | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md` |
| SASE Agentic Principles | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` |
| Sprint Planning Guide | `02-Core-Methodology/Documentation-Standards/SDLC-Sprint-Planning-Guide.md` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | Workflow Overview — principles and flow | 20 min |
| 2 | Git Workflow — branches, commits, PRs | 45 min |
| 3 | Code Review Framework — 3-tier system | 45 min |
| 4 | CI/CD Pipeline — 7 stages, fail conditions | 45 min |
| 5 | Environment Management — dev/staging/production | 20 min |
| 6 | SASE Integration — BRS to VCR daily flow | 30 min |
| 7 | Hands-on Exercises — commits, PR review | 35 min |
| | **Total** | **4h** |

### After completing this module, participants must be able to:

1. Create feature branches following the naming convention.
2. Write conventional commit messages with correct type and scope.
3. Apply the 3-tier code review system for the appropriate context.
4. Describe the CI/CD pipeline stages and their fail conditions.
5. Follow the BRS-to-VCR flow for daily feature development.

> **Remember**: "Code without a branch strategy is code without a safety net." The workflow exists to protect the team from itself.

---

## Assessment Questions

**Q1.** What is the correct branch naming format for a new feature?
> **Answer**: `feature/{ticket-id}-{short-description}` (e.g., `feature/PROJ-123-bhxh-calculator`).

**Q2.** Can staging be skipped for urgent fixes?
> **Answer**: No. Every change must go through staging before production. No exceptions.

**Q3.** Which code review tier is appropriate for a large PR touching 15 files?
> **Answer**: Tier 3 (Automated tools + human oversight) for the initial automated scan, combined with Tier 2 (AI-powered review + human approval) for the detailed review.

**Q4.** What happens if the CI/CD pipeline fails at the Zero Mock Scan stage?
> **Answer**: The build fails, the PR is blocked from merging, and the developer must fix the mock patterns before re-running the pipeline.

**Q5.** Who creates the VCR (Validation Certificate Report)?
> **Answer**: SE4H (Human). The VCR is always created by a human — AI cannot validate and approve merge requests.
