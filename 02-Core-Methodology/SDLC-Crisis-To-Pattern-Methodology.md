# SDLC Crisis-to-Pattern Methodology

```yaml
document_id: "SDLC-CRISIS-TO-PATTERN"
title: "Crisis-to-Pattern Methodology"
version: "6.1.1"
status: "ACTIVE"
section: "02-Core-Methodology"
ring: "Core"
pillar: "0 (Foundation)"
audience: ["Tech Leads", "CTOs", "Architects", "Senior Engineers"]
prerequisites: ["SDLC-System-Thinking-Foundation"]
created: "2026-02-18"
last_updated: "2026-02-18"
```

---

## Purpose

The Crisis-to-Pattern Methodology formalizes **Mental Model #5** from [System Thinking](./SDLC-System-Thinking-Foundation.md): _"Every crisis contains a reusable pattern."_ It provides a 5-step pipeline for transforming production incidents, team failures, and project crises into durable SDLC artifacts — Quality Gates, policies, framework principles, and automation rules.

> **"A crisis wasted is a crisis repeated."**

---

## The 5-Step Pipeline

```
┌──────────┐     ┌──────────────┐     ┌───────────┐     ┌──────────┐     ┌───────────┐
│ 1. DIAG- │────>│ 2. CREATE    │────>│ 3. AUTO-  │────>│ 4. EN-   │────>│ 5. DOCU-  │
│ NOSE     │     │ POLICY       │     │ MATE      │     │ FORCE    │     │ MENT      │
└──────────┘     └──────────────┘     └───────────┘     └──────────┘     └───────────┘
  Iceberg          Rule/Gate            CI/CD hook       Gate blocks       Framework
  Analysis         definition           or script        bad patterns      artifact
```

---

### Step 1: DIAGNOSE — Use the Iceberg Model

Before writing any policy, understand _all 4 layers_ (see [System Thinking](./SDLC-System-Thinking-Foundation.md)):

```yaml
Diagnostic Questions:
  Event:        "What happened? When? Who was affected? What was the blast radius?"
  Pattern:      "Has this happened before? How often? Across which projects?"
  Structure:    "What process/gate/tool gap allowed this?"
  Mental Model: "What belief made this seem acceptable beforehand?"
```

**Output**: Root cause statement identifying the _deepest_ layer involved.

**Example** (NQH-Bot Crisis):
- Event: 78% of integrations failed in production
- Pattern: Mock-based tests passed CI but failed against real services (3 projects)
- Structure: No integration testing requirement in CI pipeline
- Mental Model: "Mock it now, integrate later"
- **Root Cause**: Mental Model — integration treated as optional step

---

### Step 2: CREATE POLICY — Define the Rule

Write a clear, enforceable policy that addresses the structural and mental model layers:

```yaml
Policy Format:
  name: "<descriptive-name>"
  trigger: "<what event/condition activates this>"
  rule: "<the specific requirement>"
  evidence: "<how to prove compliance>"
  exception: "<when this can be bypassed, and who approves>"
```

**Example**:
```yaml
name: "Zero Mock Policy"
trigger: "Any code committed to main branch"
rule: "No mock/stub/placeholder implementations in production code"
evidence: "grep -r 'TODO\\|pass #\\|mock.*true' returns zero matches"
exception: "Test files only (test_*.py, *.test.ts). No exceptions for production code."
```

**Good policies are**:
- **Specific**: Clear enough for a CI script to check
- **Evidenced**: Compliance is provable, not subjective
- **Proportional**: Strictness matches the risk level
- **Tier-aware**: Enforcement may vary by tier (LITE → ENTERPRISE)

---

### Step 3: AUTOMATE — Build the Check

Move the policy from documentation to automation. Use the **Automation Ladder**:

| Level | Method | Example | Cost |
|-------|--------|---------|------|
| **L0** | Manual checklist | "Did you check for mocks?" in PR template | Free |
| **L1** | Pre-commit hook | `grep -r 'TODO' --include='*.py'` blocks commit | Low |
| **L2** | CI pipeline check | GitHub Action runs the check on every PR | Low |
| **L3** | Quality Gate integration | OPA policy evaluated at G3 gate | Medium |
| **L4** | Real-time monitoring | Production alerting on policy violations | Higher |

**Progression rule**: Start at L0, graduate to L2+ within 2 sprints: _"If it's worth checking, it's worth automating."_

**Example automation** (Zero Mock Policy):
```yaml
# .github/workflows/zero-mock.yml
name: Zero Mock Policy
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check for mock patterns
        run: |
          if grep -rn 'TODO\|pass #\|return.*mock\|placeholder' \
            --include='*.py' --exclude-dir='tests'; then
            echo "❌ Zero Mock Policy violation"
            exit 1
          fi
```

---

### Step 4: ENFORCE — Gate the Pattern

Connect the automated check to a Quality Gate so violations **block progress**:

| Enforcement Point | Mechanism | Blocks |
|-------------------|-----------|--------|
| Pre-commit | Git hook | Commit |
| Pull Request | CI check (required) | Merge |
| Quality Gate G3 | OPA policy evaluation | Release |
| Sprint Close | G-Sprint-Close criteria | Next sprint |

**Enforcement checklist**:
- [ ] Automated check exists (Step 3)
- [ ] Check is a **required** status check (not optional)
- [ ] Bypass requires explicit approval (Tech Lead+ for STANDARD, CTO for ENTERPRISE)
- [ ] Bypass is logged in Evidence Vault with rationale
- [ ] False positive rate < 5% (tune the rule to avoid alarm fatigue)

---

### Step 5: DOCUMENT — Create Framework Artifact

The final step transforms the crisis response into a **permanent SDLC artifact** so the pattern is available to all teams, all projects, forever:

| Root Cause Level | Artifact Type | Location |
|-----------------|---------------|----------|
| Pattern | Gate criteria addition | Quality Gate documentation |
| Structure | Process document or policy | `02-Core-Methodology/` or `09-govern/` |
| Mental Model | Framework principle | Core Methodology or AI Governance section |

**Documentation template**:
```yaml
Pattern Name: "<name>"
Origin: "<crisis/incident that triggered this>"
Date Discovered: "YYYY-MM-DD"
Iceberg Layer: "Event | Pattern | Structure | Mental Model"

Problem:
  Description: "<what happened>"
  Impact: "<blast radius, cost, downtime>"
  Recurrence: "<how often, across how many projects>"

Solution:
  Policy: "<the rule created>"
  Automation: "<CI check, OPA policy, etc.>"
  Enforcement: "<which gate, which tier>"
  SDLC Artifact: "<which document was created/updated>"

Verification:
  Command: "<how to verify compliance>"
  Expected: "<what passing looks like>"

Lessons:
  - "<key insight 1>"
  - "<key insight 2>"
```

---

## Real-World Pattern Library

### Pattern 1: Zero Mock Policy

| Field | Value |
|-------|-------|
| **Origin** | NQH-Bot Crisis (2024): 679 mock implementations → 78% production failure |
| **Iceberg Layer** | Mental Model: "Mock it now, integrate later" |
| **Policy** | No mock/stub/placeholder in production code |
| **Automation** | Pre-commit hook + CI grep + OPA policy |
| **Enforcement** | G3 Ship Ready gate (all tiers) |
| **SDLC Artifacts** | Zero Mock Policy, Contract-First API Design (Stage 03) |

### Pattern 2: Contract-First API Design

| Field | Value |
|-------|-------|
| **Origin** | BFlow API integration failures: 3 services disagreed on response format |
| **Iceberg Layer** | Structure: No shared API contract before implementation |
| **Policy** | OpenAPI spec must exist and be validated before any endpoint code |
| **Automation** | CI validates code against OpenAPI spec (spectral lint) |
| **Enforcement** | G2 Design Approved gate |
| **SDLC Artifacts** | Stage 03 INTEGRATE mandatory, API-first principle |

### Pattern 3: Code File Naming Standard

| Field | Value |
|-------|-------|
| **Origin** | Cross-project naming chaos: 5 NQH projects with inconsistent conventions |
| **Iceberg Layer** | Structure: No naming convention enforced |
| **Policy** | Python: snake_case ≤50 chars. TypeScript: camelCase/PascalCase ≤50 chars |
| **Automation** | Pre-commit hook validates filenames |
| **Enforcement** | CI blocking (STANDARD+ tiers) |
| **SDLC Artifacts** | [Naming Standards](./Documentation-Standards/SDLC-Naming-Standards.md) |

---

## When to Trigger the Pipeline

Not every bug needs this process. Use these triggers:

| Trigger | Severity | Action |
|---------|----------|--------|
| Production outage (P0) | Critical | **Mandatory** — full 5-step pipeline within 1 sprint |
| Recurring bug (≥3 occurrences) | High | **Mandatory** — pattern clearly exists |
| Near-miss (caught in staging/review) | Medium | **Recommended** — structure gap exists |
| Cross-project issue | High | **Mandatory** — systemic problem |
| AI-generated code failure | Medium-High | **Recommended** — AI governance gap |
| Sprint governance violation | Medium | **Recommended** — process gap |

---

## Connection to SDLC Framework

| SDLC Component | Crisis-to-Pattern Integration |
|----------------|-------------------------------|
| **Quality Gates** (Pillar 4) | Crises generate new gate criteria |
| **Sprint Governance** (Pillar 2) | Retrospectives use Iceberg Model |
| **4-Tier Classification** (Pillar 3) | Enforcement level scales with tier |
| **Section 7: QA System** | Vibecoding Index criteria refined from AI crises |
| **SASE Integration** (Pillar 5) | Agent failures create new MRP evidence requirements |
| **ADRs** | Each pattern may generate an Architecture Decision Record |
| **Evidence Vault** | Crisis artifacts stored as evidence for governance |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| **Symptom Fixing** | Only addressing the event layer | Use Iceberg — always go at least to structure |
| **Over-Engineering** | Creating heavy process for minor issues | Match enforcement to severity and tier |
| **Document-Only** | Writing the policy but never automating it | Automation Ladder: reach L2+ within 2 sprints |
| **Blame-First** | Using the pipeline to assign blame | Focus on structures and mental models, never individuals |
| **One-Project Fix** | Fixing only the affected project | Check all projects — patterns cross boundaries |

---

## Related Documents

| Document | Ring | Purpose |
|----------|------|---------|
| [SDLC-System-Thinking-Foundation](./SDLC-System-Thinking-Foundation.md) | Core | The Iceberg Model (prerequisite) |
| [SDLC-Design-Thinking-Principles](./SDLC-Design-Thinking-Principles.md) | Core | User-centered approach to solutions |
| [SDLC-Core-Methodology](./SDLC-Core-Methodology.md) | Core | Hub document for 7 Pillars + Sections |
| [SDLC-Quality-Assurance-System](./SDLC-Quality-Assurance-System.md) | Core | Section 7: Anti-Vibecoding (product of crises) |
| [Agentic Core Principles](../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md) | Governance | Agent-specific crisis patterns |

---

**Document Status**: ACTIVE
**Framework Version**: SDLC 6.1.1
**Last Updated**: February 18, 2026
