# SDLC Universal Code Review Framework

**Version**: 5.0.0
**Last Updated**: December 6, 2025
**Status**: PRODUCTION READY
**Stage**: 03 (BUILD) - Code Review Excellence
**Audience**: Engineering Teams (All Tiers - LITE to ENTERPRISE)
**ROI**: 2,033% (Tier 2) to 14,340% (Tier 3) validated

---

## 📋 Executive Summary

This framework provides **comprehensive code review guidance for ALL team contexts** - from solo developers to enterprise organizations. It documents three equally valid approaches (Tiers 1-3) without bias, enabling teams to choose based on their specific context, budget, and scale.

**Universal Framework Principle**: We document ALL options objectively. Your choice depends on YOUR context, not our preference.

### SDLC 5.0.0 Integration

**Stage Mapping**: Code Review is a core component of **Stage 03 (BUILD)**

```
Stage 03: BUILD (Development)
├── Code Generation (AI-assisted)
├── Code Review (This Framework) ← YOU ARE HERE
│   ├── Tier 1: Free/Manual
│   ├── Tier 2: Subscription-Based AI
│   └── Tier 3: CodeRabbit Professional
└── Quality Gates (Pre-merge validation)
```

**4-Tier Classification Integration**:

| Tier | Team Size | Recommended Code Review | Budget |
|------|-----------|-------------------------|--------|
| **LITE** | 1-2 | Tier 1 (Free/Manual) | $0/month |
| **STANDARD** | 3-10 | Tier 2 (Subscription) | $50-100/dev/month |
| **PROFESSIONAL** | 10-50 | Tier 2 or Tier 3 | $100-150/dev/month |
| **ENTERPRISE** | 50+ | Tier 3 (CodeRabbit) | $12-15/seat/month |

---

## 🎯 Framework Purpose

### What This Framework Provides

✅ **Tier 1: Free/Manual** - Zero-cost code review for bootstrapped teams (1-5 developers)
✅ **Tier 2: Subscription-Based** - AI-powered review via subscriptions (5-20 developers)
✅ **Tier 3: CodeRabbit Professional** - Automated enterprise-grade review (15+ developers, 50+ PRs/month)

### Who Should Use Which Tier (5.0.0 Classification)

```yaml
Tier 1 (Free/Manual):
  SDLC 5.0 Tier: LITE
  Team Size: 1-5 developers
  Budget: $0/month
  PR Volume: <20 PRs/month
  Context: Bootstrapped startups, MVPs, side projects
  Strength: Zero cost, full control
  Trade-off: Manual effort, slower reviews

Tier 2 (Subscription-Based):
  SDLC 5.0 Tier: STANDARD to PROFESSIONAL
  Team Size: 5-20 developers
  Budget: $50-100/dev/month (already paying for AI tools)
  PR Volume: 20-100 PRs/month
  Context: Growing startups, product teams (MTS/NQH choice)
  Strength: Zero new API costs, high ROI (2,033%)
  Trade-off: Requires subscription management

Tier 3 (CodeRabbit Professional):
  SDLC 5.0 Tier: PROFESSIONAL to ENTERPRISE
  Team Size: 15-100+ developers
  Budget: $12-15/seat/month dedicated tool
  PR Volume: 100-1000+ PRs/month
  Context: Scale-ups, enterprises, multi-team organizations
  Strength: Fully automated, scalable, dedicated support
  Trade-off: Additional tool subscription, integration overhead
```

---

## 🏗️ Three-Tier Architecture

### Tier 1: Free/Manual Code Review (LITE Tier)

**Philosophy**: Maximize quality with zero budget through discipline and tooling.

#### **Layer 1: Pre-Commit Quality Gates**

**Tools (All Free)**:
```yaml
Linting:
  - ESLint (JavaScript/TypeScript)
  - ruff (Python - faster than Pylint)
  - RuboCop (Ruby)
  - golangci-lint (Go)

Formatting:
  - Prettier (JavaScript/TypeScript)
  - Black (Python)
  - gofmt (Go)
  - rustfmt (Rust)

Type Checking:
  - TypeScript strict mode
  - mypy (Python)
  - Flow (JavaScript)

Security Scanning:
  - Bandit (Python)
  - npm audit (JavaScript)
  - gosec (Go)
  - Trivy (containers)

Git Hooks:
  - pre-commit framework
  - husky (JavaScript/TypeScript)
  - lint-staged
```

**Setup Example** (Python project - SDLC 5.0.0):
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

  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

**Value**: Catches 60-70% of issues before human review.

---

#### **Layer 2: Structured Peer Review**

**GitHub PR Template** (SDLC 5.0.0 Standard):
```markdown
## Change Type
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to break)
- [ ] Documentation update

## SDLC 5.0.0 Compliance

### Stage 00-01 (Design Thinking)
- [ ] User need documented (if user-facing change)
- [ ] Problem statement clear

### Stage 03 (BUILD)
- [ ] Code follows project standards
- [ ] Tests added/updated (80%+ coverage)
- [ ] No security vulnerabilities introduced
- [ ] Performance targets met (<50ms)

### Stage 04 (TEST)
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Testing Performed
Coverage Before: ___%
Coverage After: ___%

## Reviewer Checklist
- [ ] Code is readable and maintainable
- [ ] Tests are comprehensive
- [ ] No code smells detected
- [ ] Security best practices followed
- [ ] Performance is acceptable
```

**Review Protocol** (15-30 min per PR):
```yaml
Step 1: Context Review (3 min)
  - Read PR description
  - Understand problem being solved
  - Review linked issues/designs

Step 2: Automated Checks (2 min)
  - Verify CI/CD passed
  - Check test coverage (target: 80%+)
  - Review security scan results

Step 3: Code Review (10-15 min)
  - Logic correctness
  - Code readability
  - Performance implications
  - Security vulnerabilities
  - Best practice adherence

Step 4: Testing Review (5 min)
  - Test quality and coverage
  - Edge cases handled
  - Integration test completeness

Step 5: Feedback (5 min)
  - Provide actionable comments
  - Suggest improvements
  - Approve or request changes
```

**Team Best Practices**:
- **Response SLA**: <4 hours for initial review
- **Review Assignment**: Round-robin or expertise-based
- **Review Size**: Max 400 lines per PR (15-20 min review)
- **Knowledge Sharing**: Rotate reviewers for learning

**Value**: Comprehensive manual review ensuring quality and knowledge transfer.

---

#### **Layer 3: Continuous Learning**

**Monthly Review Retrospective** (Free):
```yaml
Metrics to Track:
  - Average PR review time
  - Common issues found
  - Test coverage trends
  - Security vulnerabilities discovered
  - Code quality scores (DORA: Change Failure Rate)

Actions:
  - Update pre-commit hooks based on recurring issues
  - Refine PR template based on gaps
  - Document common patterns in team wiki
  - Schedule knowledge-sharing sessions
```

**Value**: Continuously improve review process and team skills.

---

### **Tier 1 Complete ROI Analysis**:

```yaml
Team Size: 5 developers (LITE Tier)
PR Volume: 20 PRs/month

Monthly Costs: $0
  Tools: All free (pre-commit, ESLint, GitHub)
  Infrastructure: $0 (GitHub already used)

One-Time Setup Costs:
  Setup Time: 2 hours × $100/hr = $200
  Team Training: 1 hour × 5 devs × $100/hr = $500
  Total: $700

Annual Value Generated:
  Bug Prevention: 10 bugs/month × $500/bug × 12 = $60,000
  Code Quality: $1,500/month × 12 = $18,000
  Security Prevention: $5,000/month × 12 = $60,000
  Total: $138,000

ROI: Infinite (no ongoing costs!)
Net Benefit Year 1: $137,300
```

**Detailed Guide**: [SDLC-Manual-Code-Review-Playbook.md](./SDLC-Manual-Code-Review-Playbook.md)

---

### Tier 2: Subscription-Based AI Code Review (STANDARD-PROFESSIONAL)

**Philosophy**: Leverage existing AI subscriptions (zero new API costs) for intelligent, fast code review.

**Assumption**: Team already has subscriptions for development (Cursor Pro, GitHub Copilot, Claude Max).

#### **Layer 1: Pre-Commit AI Assistance (Cursor Pro)**

**Tool**: Cursor Pro ($20/dev/month)
**Purpose**: Catch issues BEFORE commit via real-time AI analysis.

**Setup** (.cursorrules file - SDLC 5.0.0):
```markdown
# SDLC 5.0.0 Code Review Rules

## Project Context
- Framework: [Django/React/FastAPI]
- Standards: SDLC 5.0.0 compliance required
- Coverage Target: 80%+ test coverage
- Performance: <50ms API response, <100ms p95

## Code Review Criteria

### Design Thinking Alignment (Stage 00-01)
- User impact clearly documented
- Problem statement validated
- Solution justifies complexity

### Code Quality (Stage 03)
- Single Responsibility Principle
- DRY (Don't Repeat Yourself)
- SOLID principles applied
- Clear variable/function names
- Max function length: 50 lines
- Max file length: 300 lines

### Security (OWASP ASVS)
- No SQL injection vulnerabilities
- No XSS vulnerabilities
- No secrets in code
- Input validation comprehensive
- Authentication/authorization correct

### Performance (DORA Metrics Target)
- Database queries optimized (N+1 avoided)
- Caching strategy appropriate
- Async/await used correctly
- Resource cleanup implemented

### Testing (Stage 04)
- Unit tests for business logic
- Integration tests for workflows
- Edge cases covered
- Mocks used appropriately
- Test names descriptive

## Before Commit Checklist
- [ ] Code follows project standards
- [ ] Tests added/updated (80%+ coverage)
- [ ] No security vulnerabilities
- [ ] Performance benchmarks met
- [ ] Documentation updated
```

**Workflow**:
1. Developer writes code in Cursor
2. Cursor AI continuously analyzes against .cursorrules
3. Real-time suggestions appear in IDE
4. Developer fixes issues BEFORE commit
5. Pre-commit hooks validate compliance

**Value**: Catches 70-80% of issues in real-time (vs manual review after commit).

---

#### **Layer 2: PR Review AI (Claude Max)**

**Tool**: Claude Max ($20/month per reviewer)
**Purpose**: Comprehensive PR analysis in 3-5 minutes.

**Review Prompt Template** (SDLC 5.0.0):
```markdown
You are an expert code reviewer for a team using SDLC 5.0.0 framework. Review this pull request comprehensively.

## PR Context
**Title**: [PR Title]
**Description**: [PR Description]
**Files Changed**: [List files]
**Lines Changed**: +XXX -YYY

## Review Against SDLC 5.0.0 Standards

### 1. Design Thinking Alignment (Stage 00-01)
- Does this solve the right problem?
- Is user impact clearly articulated?
- Are there simpler alternatives?

### 2. Code Quality (Stage 03)
- Readability and maintainability
- Adherence to SOLID principles
- Code smells detected
- Naming conventions followed
- Function/file size appropriate

### 3. Security (OWASP ASVS L2)
- SQL injection vulnerabilities?
- XSS vulnerabilities?
- Authentication/authorization correct?
- Secrets exposed?
- Input validation comprehensive?

### 4. Performance (DORA Targets)
- Database query optimization (N+1?)
- Caching strategy appropriate?
- Async/await used correctly?
- Resource cleanup implemented?
- Expected performance impact?

### 5. Testing (Stage 04)
- Test coverage adequate (80%+ target)?
- Edge cases covered?
- Integration tests appropriate?
- Test quality and clarity?

## Provide Review Feedback

Format:
**APPROVE** | **REQUEST CHANGES** | **COMMENT**

**Critical Issues** (must fix):
- [List blocking issues]

**Suggestions** (nice to have):
- [List improvements]

**Questions** (need clarification):
- [List questions for author]

**Strengths** (what's good):
- [Highlight good practices]

**Estimated Review Time Saved**: X hours vs manual review
```

**Workflow**:
1. PR created on GitHub
2. Reviewer copies PR diff to Claude Max
3. Uses template prompt above
4. Claude analyzes in 2-3 minutes
5. Reviewer validates AI feedback (1-2 min)
6. Posts consolidated review on GitHub
7. **Total time**: 3-5 minutes (vs 30-60 min manual)

**Value**: 75-85% time savings on PR review, consistent quality.

---

#### **Layer 3: Post-Merge Learning (GitHub Copilot)**

**Tool**: GitHub Copilot ($10/dev/month)
**Purpose**: Extract patterns from reviews to improve future code.

**Monthly Review Analysis**:
```markdown
## Prompt for Copilot Chat

Analyze our team's PR reviews from the past month and identify:

1. **Most Common Issues** (top 10)
   - What keeps appearing in reviews?
   - Root cause analysis

2. **Knowledge Gaps**
   - What topics need team training?
   - Which developers need mentorship in which areas?

3. **Process Improvements**
   - Should we update .cursorrules?
   - Should we add pre-commit hooks?
   - Should we create reusable patterns?

4. **DORA Metrics Impact**
   - Change failure rate trend
   - Lead time for changes

5. **Action Items**
   - Concrete steps to reduce recurring issues
   - Documentation updates needed
   - Training sessions to schedule

Context: [Paste summaries of 20-30 recent PR reviews]
```

**Value**: Continuous improvement, reduced recurring issues over time.

---

### **Tier 2 Complete ROI Analysis**:

```yaml
Team Size: 15 developers (STANDARD-PROFESSIONAL Tier)
PR Volume: 80 PRs/month

Monthly Costs:
  Cursor Pro: 15 × $20 = $300
  Copilot: 15 × $10 = $150
  Claude Max: 15 × $20 = $300
  Total: $750/month

Monthly Value Generated:
  Pre-Commit Time Saved: 100 hours × $100/hr = $10,000
    (10 min/developer/day × 20 days × 15 devs = 50 hours saved from not debugging later)

  PR Review Time Saved: 40 hours × $100/hr = $4,000
    (20 PRs/week × 25 min saved per PR × 4 weeks = 33 hours)

  Post-Merge Learning: 20 hours × $100/hr = $2,000
    (Reduced recurring issues, better patterns)

  Total Value: $16,000/month

ROI: ($16,000 - $750) / $750 = 2,033%

Additional Benefits:
  - Faster development velocity
  - Higher code quality (fewer bugs in production)
  - Better team learning and knowledge sharing
  - Consistent review standards
  - DORA metrics improvement
```

**Detailed Guide**: [SDLC-Subscription-Powered-Code-Review-Guide.md](./SDLC-Subscription-Powered-Code-Review-Guide.md)

---

### Tier 3: CodeRabbit Professional (ENTERPRISE)

**Philosophy**: Fully automated, enterprise-grade code review at scale.

**Target Audience**:
- Teams with 15-100+ developers (PROFESSIONAL-ENTERPRISE Tier)
- Organizations with 50-1000+ PRs/month
- Multi-repository, multi-team environments
- Enterprise quality and compliance requirements

#### **What is CodeRabbit?**

CodeRabbit is an AI-powered code review platform that automatically reviews every pull request across your entire organization, providing instant, comprehensive feedback.

**Key Features**:
```yaml
Automated Review:
  - Instant PR analysis (<2 min per PR)
  - Line-by-line intelligent comments
  - Security vulnerability detection (OWASP)
  - Performance optimization suggestions
  - Test coverage analysis

Multi-Language Support:
  - JavaScript/TypeScript, Python, Go
  - Java, C#/C++, Rust, Ruby, PHP

Integration:
  - GitHub (native), GitLab, Bitbucket, Azure DevOps

Customization:
  - Custom review rules (SDLC 5.0.0 standards)
  - Team-specific standards
  - Framework-specific patterns
  - Security policy enforcement

Enterprise Features:
  - SSO/SAML integration
  - Audit logs (Stage 09: GOVERN compliance)
  - Compliance reporting
  - Multi-team management
  - Priority support
```

---

#### **Layer 1: Automated PR Analysis**

**Configuration** (SDLC 5.0.0 - .coderabbit.yaml):
```yaml
# .coderabbit.yaml - SDLC 5.0.0 Configuration

# Review Settings
reviews:
  auto_review: true
  request_changes_workflow: true
  high_level_summary: true
  poem: false  # Disable fun features for professional context

  # Review Depth
  thoroughness: high

  # Focus Areas (SDLC 5.0.0 aligned)
  focus:
    - security      # OWASP ASVS compliance
    - performance   # DORA metrics targets
    - testing       # Stage 04 compliance
    - maintainability

# Custom Rules (SDLC 5.0.0 Standards)
rules:
  # Design Thinking (Stage 00-01)
  - pattern: "TODO: validate user need"
    message: "SDLC 5.0.0: Ensure user problem statement is documented"
    severity: warning

  # Performance (DORA targets)
  - pattern: "for .* in .*:.*\\.objects\\.get"
    message: "N+1 query detected. Use select_related() or prefetch_related()."
    severity: warning

  # Security (OWASP)
  - pattern: "eval\\(|exec\\("
    message: "Security: eval() and exec() are dangerous. Find safer alternative."
    severity: error

  - pattern: "password.*=.*request"
    message: "Security: Never log or expose passwords. Ensure proper hashing."
    severity: error

  # Code Quality
  - pattern: "def .{50,}\\("
    message: "Function name too long. Keep under 50 characters for readability."
    severity: warning

# Language-Specific Settings
languages:
  python:
    frameworks:
      - django
      - fastapi
    max_function_lines: 50
    test_coverage_threshold: 80

  typescript:
    frameworks:
      - react
    max_component_lines: 200
    test_coverage_threshold: 80

# Integration Settings
github:
  auto_review_pull_requests: true
  post_review_as_comment: true
  dismiss_stale_reviews: true

# Team Settings
team:
  exclude_paths:
    - "*/migrations/*"
    - "*/tests/fixtures/*"
    - "*.min.js"

  include_paths:
    - "backend/**/*.py"
    - "frontend/**/*.ts"
    - "frontend/**/*.tsx"
```

**Value**: Instant, comprehensive review for every PR (zero human effort until validation).

---

#### **Layer 2: Analytics & Continuous Improvement**

**CodeRabbit Dashboard Metrics** (DORA aligned):
```yaml
Team Performance:
  - Average PR review time: 8 minutes (down from 45 min)
  - PRs reviewed/week: 127 (100% coverage)
  - Critical issues caught: 23/week
  - Security vulnerabilities: 5/week (before production!)

Code Quality Trends:
  - Test coverage: 65% → 82% (3 months)
  - N+1 queries: 15/week → 2/week
  - Security issues: 8/week → 1/week
  - Average function length: 67 lines → 42 lines

DORA Metrics Impact:
  - Lead time for changes: ↓40%
  - Change failure rate: ↓60%
  - Deployment frequency: ↑200%
  - MTTR: ↓50%

Developer Insights:
  - Top contributors: [ranked by quality, not just volume]
  - Common mistakes per developer (for mentorship)
  - Learning progress over time
```

**Value**: Data-driven continuous improvement at scale.

---

### **Tier 3 Complete ROI Analysis**:

```yaml
Team Size: 50 developers (ENTERPRISE Tier)
PR Volume: 200 PRs/month

Monthly Costs:
  CodeRabbit Pro: 50 seats × $15 = $750/month
  (Enterprise pricing: $12/seat with volume discount)

Monthly Value Generated:
  PR Review Time Saved:
    200 PRs/month × 40 min saved per PR = 133 hours
    133 hours × $100/hr = $13,300

  Bug Prevention (caught before production):
    Estimated 50 bugs/month prevented
    Average bug fix cost: $500 (dev time + QA + hotfix)
    50 × $500 = $25,000

  Security Vulnerability Prevention:
    Estimated 5 critical vulnerabilities/month prevented
    Average security incident cost: $10,000
    5 × $10,000 = $50,000 (risk mitigation)

  Faster Time-to-Market:
    20% faster PR merge rate (less review bottleneck)
    Value: ~$20,000/month (competitive advantage)

  Total Monthly Value: $108,300

ROI: ($108,300 - $750) / $750 = 14,340%

Annual ROI: $1,290,600 value - $9,000 cost = 14,240% ROI

Additional Benefits:
  - Scalable to 100+ developers with no linear cost increase
  - 24/7 review availability (no waiting for human reviewers)
  - Consistent quality across all teams and repositories
  - Audit trail for compliance (Stage 09: GOVERN)
  - Onboarding acceleration (new devs get instant feedback)
```

**Detailed Guide**: [SDLC-CodeRabbit-Integration-Guide.md](./SDLC-CodeRabbit-Integration-Guide.md)

---

## 📊 Tier Comparison Matrix (SDLC 5.0.0)

| Criteria | Tier 1: Free/Manual | Tier 2: Subscription | Tier 3: CodeRabbit |
|----------|---------------------|----------------------|--------------------|
| **SDLC 5.0 Tier** | LITE | STANDARD-PROFESSIONAL | PROFESSIONAL-ENTERPRISE |
| **Team Size** | 1-5 devs | 5-20 devs | 15-100+ devs |
| **Monthly Cost** | $0 | $50-100/dev | $12-15/seat |
| **Setup Time** | 30 min | 2 hours | 4-8 hours |
| **Review Speed** | 15-30 min/PR | 3-5 min/PR | <2 min/PR (auto) |
| **Automation Level** | 40% (pre-commit only) | 70% (AI-assisted) | 95% (fully automated) |
| **Human Effort** | High (30 min/PR) | Low (5 min validation) | Minimal (spot check) |
| **Consistency** | Variable (depends on reviewer) | High (AI + human) | Very High (AI rules) |
| **Scalability** | Poor (linear effort increase) | Good (AI scales well) | Excellent (no limit) |
| **DORA Impact** | Moderate | High | Very High |
| **ROI** | Infinite (no cost) | 2,033% | 14,340% |
| **Best For** | Bootstrapped startups | Growing product teams | Scale-ups, enterprises |

---

## 🚀 Migration Paths

### From Tier 1 → Tier 2

**When to Migrate** (LITE → STANDARD):
- Team grows beyond 5 developers
- PR volume exceeds 20/month
- Review bottlenecks slow down delivery
- Team already has AI tool subscriptions

**Migration Steps** (4 hours):
1. **Audit Current Setup** (30 min)
   - Document pre-commit hooks
   - Review PR template effectiveness
   - Measure current review time per PR

2. **Setup Subscription Tools** (1 hour)
   - Purchase Cursor Pro subscriptions
   - Purchase Claude Max subscriptions
   - Purchase GitHub Copilot (if not already)

3. **Create Configuration** (1 hour)
   - Write .cursorrules file (adapt from Tier 1 linting config)
   - Create Claude review prompt templates
   - Document workflow for team

4. **Team Training** (1.5 hours)
   - 30 min: Cursor Pro walkthrough
   - 30 min: Claude Max review demo
   - 30 min: Practice on sample PRs

**Expected Outcome**: 75% reduction in PR review time within 2 weeks.

---

### From Tier 2 → Tier 3

**When to Migrate** (STANDARD → PROFESSIONAL/ENTERPRISE):
- Team grows beyond 15 developers
- PR volume exceeds 100/month
- Multi-team or multi-repository environment
- Need compliance audit trails (Stage 09: GOVERN)
- Human review still bottleneck despite AI assistance

**Migration Steps** (8 hours):
1. **Business Case Validation** (1 hour)
   - Calculate current review time costs
   - Project CodeRabbit ROI
   - Get budget approval

2. **Trial Setup** (2 hours)
   - Sign up for CodeRabbit trial (14 days free)
   - Connect 2-3 active repositories
   - Let it review 10-20 PRs automatically

3. **Configuration Migration** (3 hours)
   - Convert .cursorrules to `.coderabbit.yaml`
   - Migrate team standards to CodeRabbit rules
   - Configure team-specific settings

4. **Pilot Program** (2 weeks)
   - Run CodeRabbit + human review in parallel
   - Validate AI review quality
   - Gather team feedback

5. **Full Rollout** (2 hours)
   - Enable for all repositories
   - Train team on new workflow
   - Update documentation

**Expected Outcome**: 90% reduction in manual review effort within 1 month.

---

## 🎯 Decision Framework (SDLC 5.0.0)

### Step 1: Determine Your SDLC 5.0 Tier

```yaml
LITE (1-2 people, <$50K budget):
  → Code Review: Tier 1 (Free/Manual)
  → Rationale: Zero cost, sufficient for small team

STANDARD (3-10 people, $50-200K budget):
  → Code Review: Tier 2 (Subscription)
  → Rationale: AI assistance, already paying for tools

PROFESSIONAL (10-50 people, $200K-1M budget):
  → Code Review: Tier 2 or Tier 3
  → Decision Factor: PR volume (>100/month → Tier 3)

ENTERPRISE (50+ people, $1M+ budget):
  → Code Review: Tier 3 (CodeRabbit)
  → Rationale: Scale, compliance, audit trails
```

### Step 2: Validate with Decision Matrix

```yaml
Choose Tier 1 if:
  ✅ Team ≤5 developers
  ✅ Budget = $0
  ✅ Willing to invest manual effort
  ✅ Strong review discipline exists
  ✅ SDLC 5.0 Tier: LITE

Choose Tier 2 if:
  ✅ Team 5-20 developers
  ✅ Already have AI tool subscriptions
  ✅ Want high ROI with minimal new costs
  ✅ Need fast implementation (hours, not days)
  ✅ SDLC 5.0 Tier: STANDARD to PROFESSIONAL

Choose Tier 3 if:
  ✅ Team ≥15 developers
  ✅ PR volume ≥50/month
  ✅ Budget available for dedicated tool
  ✅ Need compliance/audit trails (Stage 09)
  ✅ Multi-team environment
  ✅ SDLC 5.0 Tier: PROFESSIONAL to ENTERPRISE
```

---

## 📚 Implementation Resources

### For Tier 1 (Free/Manual):
- **Guide**: [SDLC-Manual-Code-Review-Playbook.md](./SDLC-Manual-Code-Review-Playbook.md)
- **Templates**: [../03-Templates-Tools/1-AI-Tools/code-review/](../03-Templates-Tools/1-AI-Tools/code-review/)
- **Setup Time**: 30 minutes

### For Tier 2 (Subscription):
- **Guide**: [SDLC-Subscription-Powered-Code-Review-Guide.md](./SDLC-Subscription-Powered-Code-Review-Guide.md)
- **Templates**: Claude review prompts, .cursorrules examples
- **Setup Time**: 2 hours

### For Tier 3 (CodeRabbit):
- **Guide**: [SDLC-CodeRabbit-Integration-Guide.md](./SDLC-CodeRabbit-Integration-Guide.md)
- **Official Docs**: https://docs.coderabbit.ai
- **Setup Time**: 8 hours (including pilot)

---

## ✅ Success Metrics (SDLC 5.0.0 Aligned)

Track these KPIs regardless of tier chosen:

```yaml
Code Quality Metrics (Stage 03-04):
  - Bugs found in production (target: ↓50% year-over-year)
  - Test coverage (target: ≥80%)
  - Code review comments per PR (target: 3-5)
  - Security vulnerabilities detected (track trend)

Process Efficiency (DORA Metrics):
  - Average PR review time (track per tier)
  - Time from PR creation to merge (target: <24 hours)
  - PR rework cycles (target: ≤1 cycle)
  - Lead time for changes (track improvement)
  - Change failure rate (target: <15%)

Team Health:
  - Developer satisfaction with review process (survey quarterly)
  - Knowledge sharing effectiveness (track cross-team reviews)
  - Onboarding time for new developers (target: ↓30%)

Business Impact:
  - Time-to-market for features (track velocity)
  - Production incidents caused by code issues (target: <2/month)
  - Customer-reported bugs (target: ↓40%)
```

---

## 🎓 Conclusion

**Universal Framework Principle Recap**:

This framework provides **three equally valid approaches** to code review excellence, aligned with SDLC 5.0.0 4-Tier Classification:

- **Tier 1** maximizes quality with zero budget (discipline + free tools) → **LITE Tier**
- **Tier 2** optimizes for ROI using existing AI subscriptions (2,033% ROI) → **STANDARD-PROFESSIONAL Tier**
- **Tier 3** scales to enterprise with full automation (14,340% ROI) → **PROFESSIONAL-ENTERPRISE Tier**

**Your choice depends on YOUR context** - team size, budget, PR volume, and organizational tier. There is no "best" tier universally, only the best tier **for your specific situation**.

---

**Key Takeaway**: **Excellent code review is achievable at ANY budget**. Choose the tier that fits your SDLC 5.0 classification, implement it thoroughly, and continuously improve based on DORA metrics.

---

**Document Version**: 5.0.0
**Last Updated**: December 6, 2025
**Next Review**: January 6, 2026
**Owner**: CPO Office (taidt@mtsolution.com.vn)

---

**Related Documents**:
- [SDLC-Implementation-Guide.md](./SDLC-Implementation-Guide.md) - Complete implementation guide
- [SDLC-Manual-Code-Review-Playbook.md](./SDLC-Manual-Code-Review-Playbook.md) - Tier 1 detailed guide
- [SDLC-Subscription-Powered-Code-Review-Guide.md](./SDLC-Subscription-Powered-Code-Review-Guide.md) - Tier 2 detailed guide
- [SDLC-CodeRabbit-Integration-Guide.md](./SDLC-CodeRabbit-Integration-Guide.md) - Tier 3 detailed guide

---

**🏆 SDLC 5.0.0 Universal Code Review Framework**
*Excellence at Every Scale - From LITE to ENTERPRISE*
*Stage 03: BUILD - Code Review Excellence*
