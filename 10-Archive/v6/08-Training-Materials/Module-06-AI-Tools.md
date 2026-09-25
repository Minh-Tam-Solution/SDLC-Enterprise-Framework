---
document_id: "TRAINING-MODULE-06"
title: "Module 06: AI Tools Integration"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "4 hours (7 parts)"
audience: "All team members — developers, pod leads, architects"
prerequisite: "Module 01-05 (SDLC Overview, Six Pillars, Zero Mock, Code Quality, Workflow)"
format: "Lecture + Live Demo + Hands-on Exercises"
---

# Module 06: AI Tools Integration

> **Core principle**: "AI proposes, human disposes." Every AI-generated line of code must be reviewed, tested, and validated by a human before it enters the codebase.

---

## 1. AI Tools in SDLC 6.3.0 (30 minutes)

### SASE Framework for AI Integration

AI tools in SDLC 6.3.0 operate within the **SASE (Software Agentic Software Engineering)** framework with clear role separation:

```
SE4H (Human as Agent Coach):
  - Defines BRS (BriefingScript) — describes intent
  - Validates AI outputs — reviews every line
  - Makes final approval decisions — VCR sign-off
  - Handles security-critical reviews

SE4A (AI as Agent Executor):
  - Executes code generation
  - Performs automated code reviews
  - Generates documentation drafts
  - Runs pattern analysis
```

### Core Principles of AI Usage

| Principle | Description |
|-----------|-------------|
| **Human Final Decision** | AI proposes, human approves. SE4H always has final authority. |
| **Context-Rich Prompting** | Provide complete BRS, include SDLC requirements, specify Zero Mock. |
| **Verification Mandatory** | Always review AI output. Validate Vietnamese business logic. Test before commit. |
| **Appropriate Tool Selection** | Simple tasks: local AI (Ollama). Complex tasks: cloud AI (Claude Code). |

---

## 2. AI Tool Selection Matrix (30 minutes)

### Available Tools

```
Self-Hosted (Primary):
  Ollama + Qwen models (local, zero cost, full privacy)
  Continue.dev IDE extension (integrates with Ollama)

Cloud (Complex tasks):
  Claude Code CLI (multi-file, architecture, OAuth)
  Fallback: OpenAI, Gemini for specialized tasks

Automated:
  CodeRabbit (CI/CD code review)
  SonarQube (quality analysis)
```

### When to Use Which Tool

| Task Type | Ollama (Free) | Claude Code | Notes |
|-----------|:------------:|:-----------:|-------|
| Quick fix (1-2 files) | Best | Overkill | Use local tool |
| Add unit tests | Good | Overkill | Local is sufficient |
| Basic code review | Best | Overkill | Use Continue.dev /review |
| Multi-file refactor (5+ files) | Limited | **Best** | Needs large context window |
| Architecture review | Limited | **Best** | Needs full codebase understanding |
| Complex debugging | Limited | **Best** | Needs multi-file trace |
| Design-to-code | Good | Better | Depends on complexity |
| SASE artifact generation (MRP) | Good | **Best** | MRP needs evidence gathering |

### When NOT to Use AI

| Situation | Reason |
|-----------|--------|
| Stage 00 Foundation decisions | 100% human strategic decisions |
| Final approval (VCR) | Human accountability required |
| Security-critical code | Requires expert human review |
| Financial calculations (BHXH, VAT) | Must verify manually |
| Customer data handling | Privacy and regulatory concerns |
| Production hotfixes | Too high risk for auto-generation |

---

## 3. Design-to-Code Automation (30 minutes)

### Universal Prompt Pattern

When asking AI to generate code, always include SDLC 6.3.0 requirements:

```
Convert [DESIGN_SOURCE] to [FRAMEWORK] component:

Design: [URL or description]
Component: [ComponentName]
Framework: [React/FastAPI/etc.]
Location: [target directory]

SDLC 6.3.0 Requirements:
  Zero Mock Policy compliance (no fake data)
  Unit test coverage >=80%
  Performance <50ms render time
  Documentation complete (English comments)
  Design tokens used (no hardcoded colors/sizes)
  Accessibility WCAG 2.1 AA
  Vietnamese i18n support

Generate complete implementation with tests.
```

### ROI of Design-to-Code

```
Traditional development:
  Time per component:  2-4 hours
  Test coverage:       ~60%
  Documentation:       Often missing

With AI assistance:
  Time per component:  15-30 minutes
  Test coverage:       80%+ (auto-generated)
  Documentation:       Complete

Savings: 75-90% time reduction per component
```

---

## 4. AI-Powered Code Review (45 minutes)

### Tier 1: Self-Review with AI Assist

```
Tool: Continue.dev + Ollama
Time: 15-20 minutes
When: Standard PRs, daily work

Process:
  1. Author runs self-review with AI before creating PR
  2. Fix AI-found issues
  3. Create PR
  4. Reviewer uses Continue.dev /review for second pass

Prompt pattern:
  "Review this code following SDLC 6.3.0 standards:
   1. Zero Mock Policy compliance
   2. Code quality (readability, error handling)
   3. Performance (<50ms target)
   4. Test coverage (>=80%)
   5. Vietnamese compliance (BHXH, VAT, VND)
   Provide specific feedback with line numbers."
```

### Tier 2: AI-Powered Review for Complex PRs

```
Tool: Claude Code
Time: 5-10 minutes
When: Complex PRs, multi-file changes

Process:
  1. AI reviews entire PR diff
  2. AI generates review comments with severity levels
  3. Human validates AI suggestions
  4. Human makes final approval decision

Output format:
  Critical issues (must fix before merge)
  Major issues (should fix)
  Minor issues (nice to have)
  SASE MRP summary
```

### Tier 3: Automated CI/CD Review

```
Tool: CodeRabbit, SonarQube, custom scripts
Time: <2 minutes
When: Every PR (runs automatically)

Automated checks:
  Zero Mock Scan — reject if mock patterns found
  Test Coverage — reject if coverage <80%
  Performance — flag if response time >50ms
  Security — flag high severity vulnerabilities
```

---

## 5. Design Thinking Acceleration with AI (30 minutes)

AI can accelerate each of the 5 Design Thinking phases:

| Phase | AI Can Do | Human Must Do |
|-------|----------|---------------|
| **Empathize** | Synthesize interview notes, generate empathy maps, identify patterns | Conduct actual interviews, validate synthesis |
| **Define** | Generate problem statements, suggest HMW questions | Validate with stakeholders, select final statement |
| **Ideate** | Generate 15+ solutions using SCAMPER, score feasibility | Review suggestions, add domain expertise, vote |
| **Prototype** | Generate code scaffolding, create UI mockups | Build actual prototype, test with users |
| **Test** | Generate test scenarios, analyze results | Run user tests, observe behavior, make decisions |

### Time Savings

```
Traditional Design Thinking:  26 hours per feature
With AI Assistance:           1 hour per feature
Time reduction:               96%
User adoption improvement:    2.8x (30% to 85%)
```

---

## 6. SASE Artifact Generation with AI (30 minutes)

### AI-Generated MRP Template

The MRP (Merge Request Protocol) is the most common AI-generated SASE artifact:

```markdown
## Merge Request Protocol (MRP)

### 1. Summary
[AI-generated summary of all changes]

### 2. Files Changed
[List of files with change types: added/modified/deleted]

### 3. Evidence Points
| Check | Status | Details |
|-------|--------|---------|
| Tests | PASS/FAIL | X tests added, Y% coverage |
| Performance | PASS/FAIL | Measured response time |
| Zero Mock | PASS/FAIL | Scan results |
| Vietnamese Compliance | PASS/FAIL | BHXH/VAT verification |
| Documentation | PASS/FAIL | Docs updated |

### 4. BRS Reference
Implements requirements from: [BRS-XXX]

### 5. Approval Request
Requesting VCR from: [SE4H reviewer name]

Generated by: SE4A (AI tool name)
Date: [date]
```

### Best Practices for AI-Generated Artifacts

```
DO:
  Provide rich context (BRS, requirements, constraints)
  Include SDLC 6.3.0 standards in every prompt
  Always review AI output before committing
  Validate Vietnamese business logic manually
  Document which sections were AI-generated

DO NOT:
  Accept AI code without reviewing it
  Paste passwords or API keys into AI prompts
  Use AI for Stage 00 Foundation decisions
  Let AI approve PRs (VCR is always human)
  Skip test verification on AI-generated tests
  Over-rely on AI — understand the code yourself
```

---

## 7. Hands-on Exercises (45 minutes)

### Exercise 1: Tool Selection (15 minutes)

For each scenario, select the appropriate AI tool and explain why:

**1.** Fix a typo in a single Python file.
**2.** Refactor authentication logic across 8 files.
**3.** Generate unit tests for a new BHXH calculator service.
**4.** Review a PR that adds a new multi-tenant database schema.
**5.** Decide whether to use PostgreSQL or MongoDB for a new service.

### Exercise 1 Answers

**1.** Ollama (local) — simple single-file fix, no need for cloud AI.
**2.** Claude Code — multi-file refactor requires large context window.
**3.** Ollama (local) — test generation for a single service is straightforward.
**4.** Claude Code (Tier 2 review) — complex PR with architectural implications.
**5.** Human only — this is an architecture decision (Stage 02) requiring human judgment, not AI generation.

### Exercise 2: Write an SDLC-Compliant AI Prompt (15 minutes)

Write a prompt asking AI to implement a VAT calculator endpoint. Include all SDLC 6.3.0 requirements.

**Expected answer should include**:
- Component name and location
- Framework specification
- Zero Mock Policy requirement
- Test coverage requirement (>=80%)
- Performance target (<50ms)
- Vietnamese compliance (exact 10% VAT rate, VND formatting)
- English-only comments

### Exercise 3: Review AI Output (15 minutes)

The following code was generated by AI. Identify what must be fixed before committing:

```python
# Calculate VAT
def calc_vat(amt):
    # tinh thue VAT
    tax = amt * 0.1
    return {"amount": amt, "tax": tax, "total": amt + tax}
```

### Exercise 3 Answers

| Issue | Fix Required |
|-------|-------------|
| `calc_vat` — abbreviated name | Rename to `calculate_vat` |
| `amt` — abbreviated parameter | Rename to `amount` |
| `# tinh thue VAT` — Vietnamese comment | Rewrite in English |
| `0.1` — float for financial calculation | Use `Decimal("0.10")` |
| No type hints | Add type hints for all parameters and return |
| No docstring | Add docstring explaining purpose, args, returns |
| No input validation | Validate that amount is non-negative |
| No tests | Write unit tests covering normal, edge, and error cases |

---

## Reference Materials

| Document | Location |
|----------|----------|
| AI Governance Principles | `03-AI-GOVERNANCE/` (docs 01-09) |
| Agentic Core Principles | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` |
| AI Tools Landscape | `04-AI-TOOLS-LANDSCAPE/` |
| SASE Artifacts Templates | `05-Templates-Tools/04-SASE-Artifacts/` |
| Model Registry (SSOT) | `backend/app/core/model_registry.py` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | AI Tools in SDLC 6.3.0 — SASE framework, core principles | 30 min |
| 2 | AI Tool Selection Matrix — when to use which tool | 30 min |
| 3 | Design-to-Code Automation — prompt patterns, ROI | 30 min |
| 4 | AI-Powered Code Review — 3-tier system with AI | 45 min |
| 5 | Design Thinking Acceleration — AI per DT phase | 30 min |
| 6 | SASE Artifact Generation — MRP template, best practices | 30 min |
| 7 | Hands-on Exercises — tool selection, prompts, review | 45 min |
| | **Total** | **4h** |

### After completing this module, participants must be able to:

1. Select the appropriate AI tool for a given task (Ollama vs Claude Code vs human-only).
2. Write SDLC-compliant prompts that include Zero Mock, coverage, and performance requirements.
3. Review AI-generated code and identify issues before committing.
4. Generate an MRP using AI with all 5 evidence points.
5. Know when NOT to use AI (Stage 00, VCR approval, security decisions).

> **Remember**: "AI proposes, human disposes." The 96% time savings only materialize when humans remain accountable for every line that ships.

---

## Assessment Questions

**Q1.** Who has final approval authority for merge requests?
> **Answer**: SE4H (Human). AI can assist with review, but the VCR (Validation Certificate Report) must always be signed by a human.

**Q2.** When should you use Claude Code instead of Ollama?
> **Answer**: For complex tasks requiring large context: multi-file refactoring (5+ files), architecture reviews, complex debugging, and full codebase analysis.

**Q3.** What must every AI prompt include for SDLC 6.3.0 compliance?
> **Answer**: Zero Mock Policy requirement, test coverage target (>=80%), performance target (<50ms), English-only comments, and Vietnamese compliance needs (BHXH/VAT/VND if applicable).

**Q4.** Can AI be used for Stage 00 (Foundation) decisions?
> **Answer**: No. Stage 00 is 100% human. Strategic vision, business case, and stakeholder alignment are human-only decisions.

**Q5.** What are the 5 evidence points required in an MRP?
> **Answer**: (1) Tests passing, (2) Coverage met (>=80%), (3) Quality score (>=95%), (4) Performance verified (<50ms), (5) Zero mocks confirmed.
