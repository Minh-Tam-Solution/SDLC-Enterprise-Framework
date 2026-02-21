---
sdlc_version: "6.1.1"
document_type: "Framework Standard"
section: "03-AI-GOVERNANCE"
ring: "Core"
status: "APPROVED"
owner: "CTO"
last_updated: "2026-02-18"
context_zone: "Core"
update_frequency: "Per major version (quarterly)"
priority: "P1"
source: "Industry autonomous coding patterns + SDLC 6.1.1 Quality Gates"
sprint: "174"
---

# Autonomous Codegen with Quality Gates

**Framework Version**: SDLC 6.1.1
**Pillar**: 03 — AI Governance
**Classification**: ORANGE (New Methodology — requires ADR)
**Effective Date**: February 18, 2026

---

## 1. Problem Statement

Traditional autonomous coding agents (Devin, AutoGPT, SWE-Agent) have **60-80% feature waste** because they lack Quality Gates. Code is generated without:

- **Legal clearance** — AGPL contamination risk from AI-suggested dependencies
- **Security validation** — Vulnerabilities shipped to production (CWE Top 25)
- **Architectural alignment** — Technical debt accumulates across sessions
- **Evidence traceability** — No audit trail for compliance (SOC2, GDPR)

The gap: AI agents are powerful code generators but have no governance layer to validate output quality before it reaches production.

---

## 2. The Two-Agent Pattern

**Origin**: Open-source autonomous coding reference implementations (Q1 2026)

### 2.1 Architecture

The industry-standard reference implementation uses a **two-agent pattern** with JSON persistence:

**Agent 1: Initializer** (single session, 10-20 minutes)
- Reads `app_spec.txt` (product requirements document)
- Generates `feature_list.json` (comprehensive test cases, typically 50-200 items)
- Sets up project structure and git repository
- Runs once per project initialization

**Agent 2: Coding Agent** (multiple sessions, 5-10 minutes each)
- Reads `feature_list.json` to find the next unimplemented feature
- Implements the feature, runs tests
- Updates `feature_list.json` with pass/fail status
- Commits to git for persistence between sessions
- Auto-continues with 3-second delay between features

### 2.2 Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **JSON persistence** (`feature_list.json`) | Enables resumable sessions across Claude API calls |
| **Git commits per feature** | Rollback granularity at feature level |
| **3-second auto-continue** | Prevents rate limiting while maintaining momentum |
| **Separate init/coding agents** | Separation of concerns: planning vs execution |

### 2.3 Security Model

Anthropic uses a **bash command allowlist** for defense-in-depth:

```python
ALLOWED_COMMANDS = [
    "cd", "ls", "cat", "git", "touch", "mkdir", "mv", "cp", "rm",
    "npm", "python", "pip", "pytest", "node"
]
```

**Limitation**: This is a coarse-grained security model. It prevents catastrophic damage (no `sudo`, `curl | bash`) but doesn't validate the semantic safety of generated code.

---

## 3. SDLC Enhancement: 4-Gate Quality Pipeline

### 3.1 Improvement Over Anthropic Pattern

SDLC 6.1.1 adds **Quality Gates** to catch issues BEFORE merge, transforming the autonomous coding loop from "generate and hope" to "generate, validate, and verify."

| Stage | Anthropic Pattern | SDLC Enhancement |
|-------|-------------------|------------------|
| **Spec → Features** | `app_spec.txt` → `feature_list.json` | Gate G1: Legal + Stakeholder review on spec |
| **Feature → Code** | Coding agent writes code freely | Gate G2: SAST + Security scan on generated code |
| **Code → Tests** | Agent marks tests as passing | Gate G3: Coverage + Integration tests mandatory |
| **Tests → Merge** | Git commit (unreviewed) | Gate G4: Human architect review (for changes >500 LOC) |

### 3.2 Architecture

```
┌─────────────┐
│ app_spec.txt │──── Gate G1 (Legal + Stakeholder) ────┐
└─────────────┘                                         │
                                                        v
┌─────────────────────┐                         ┌──────────────┐
│ feature_list.json   │<──── Initializer ───────│   APPROVED   │
│ (test cases)        │       Agent             └──────────────┘
└─────────────────────┘
         │
         v
┌─────────────────────┐
│ Feature #N          │──── Gate G2 (SAST) ────┐
│ (generated code)    │                         │
└─────────────────────┘                         v
         │                              ┌──────────────┐
         ├───── Gate G3 (Tests) ────────│     PASS     │
         │                              └──────────────┘
         v                                      │
    Loop continues until                        v
    all features complete               ┌──────────────┐
                                        │   Gate G4    │
                                        │(Human Review)│
                                        └──────────────┘
                                                │
                                                v
                                        ┌──────────────┐
                                        │   MERGED     │
                                        └──────────────┘
```

### 3.3 Gate Details

#### Gate G1: Specification Review (Before Coding Starts)

**Trigger**: Initializer agent receives `app_spec.txt`
**Checks**:
- Legal clearance: Spec does not request AGPL-licensed dependencies
- Stakeholder sign-off: Product owner approved the spec
- Scope validation: Feature count within sprint capacity
- Architectural alignment: Spec references existing ADRs

**Outcome**: APPROVED → Initializer generates `feature_list.json` | REJECTED → Spec returned for revision

#### Gate G2: Security Scan (Per Feature)

**Trigger**: Coding agent completes a feature implementation
**Checks**:
- SAST scan (any SAST tool): OWASP Top 10 rules + AI-specific rules
- Dependency audit: No new AGPL/GPL dependencies introduced
- Secret detection: No hardcoded API keys, passwords, tokens
- AGPL containment: No direct imports of AGPL libraries

**Outcome**: PASS → Proceed to tests | FAIL → Coding agent auto-fixes (max 3 retries) → Escalate to human

#### Gate G3: Test Validation (Per Feature)

**Trigger**: Feature passes Gate G2
**Checks**:
- Unit test coverage: >80% for new code
- Integration tests: API contract validation
- Regression tests: No existing tests broken
- Performance baseline: No latency regression >10%

**Outcome**: PASS → Feature marked complete | FAIL → Coding agent auto-fixes (max 3 retries) → Escalate to human

#### Gate G4: Human Review (Before Merge)

**Trigger**: All features complete OR total LOC >500
**Checks**:
- Architect reviews generated code structure
- MRP (Merge-Readiness Package) is complete
- Evidence Vault contains all gate artifacts
- No unresolved security findings

**Outcome**: APPROVED → Auto-merge | REJECTED → Specific features flagged for revision

---

## 4. Security Model Comparison

### 4.1 Anthropic: Command Allowlist

```
Agent → Bash Command → Allowlist Check → Execute/Block
```

**Strengths**: Simple, prevents catastrophic system damage
**Weaknesses**: Doesn't validate code semantics, no audit trail

### 4.2 SDLC: Policy-as-Code + Evidence Trail

```
Agent → Action → Policy Engine Evaluation → Risk Classification → Execute/Approve/Block
                        │
                        v
                 Evidence Store (immutable audit log)
```

Policy engines (OPA, Sentinel, Cedar, or equivalent) evaluate semantic risk:

**Risk Classification**:

| Risk Level | Example Actions | Policy |
|------------|----------------|--------|
| **LOW** | `ls`, `cat`, `git status` | Auto-execute, log to evidence store |
| **MEDIUM** | `npm install`, `pip install` | Auto-execute, dependency audit triggered |
| **HIGH** | `rm -rf`, `DROP TABLE` | Human approval required |
| **CRITICAL** | `chmod 777`, `curl \| bash` | Blocked, security incident created |

**Advantages over command allowlist**:
- Semantic risk assessment (not just command name matching)
- Immutable audit trail for compliance
- Configurable per project (different risk tolerance)
- Evidence-based: every action is traceable

---

## 5. Codegen Pipeline Integration Pattern

### 5.1 Conceptual Flow

Any codegen pipeline implementing this methodology follows this loop:

```
1. INITIALIZE: Spec → Feature List (Gate G1 approval)
2. FOR EACH FEATURE:
   a. Generate code (AI agent or IR-based codegen)
   b. Gate G2: Run SAST scan → PASS or retry with feedback
   c. Gate G3: Run tests → PASS or retry with feedback
   d. If max_retries exceeded → Escalate to human
   e. Store evidence artifact → Git commit
3. MERGE: Gate G4 for changes >500 LOC (human review)
```

### 5.2 Retry Logic

- `max_retries`: 3 (configurable per project tier)
- Retry feedback must be **deterministic**: structured error data, not vague "try again"
- On max retries exhausted: escalate to human with full context (gate results, attempted fixes)

### 5.3 Evidence Lifecycle Per Feature

Each feature in the autonomous loop follows an evidence lifecycle:

```
generated → validating → [retrying] → evidence_locked → awaiting_review → merged
                              │
                              └── escalated (max retries exceeded)
                                      │
                                      └── aborted (human decision)
```

Platform implementations should map these states to their evidence storage system.

---

## 6. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Feature waste reduction** | 60% → 30% | Compare feature acceptance rate (with/without gates) |
| **Security vulnerability rate** | <2% of generated code | SAST findings per 1,000 LOC generated |
| **Human review burden** | Only for >500 LOC changes (~20% of features) | Percentage of features requiring Gate G4 |
| **Time to first feature** | <30 minutes (from spec to deployed code) | End-to-end latency measurement |
| **Retry rate** | <15% of features need >1 attempt | Gate G2/G3 retry counter |
| **Escalation rate** | <5% of features escalated to human | Escalation event count / total features |

---

## 7. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| **Agent generates AGPL code** | Medium | HIGH | Gate G1 blocks specs requesting AGPL; Gate G2 dependency audit catches runtime |
| **Agent bypasses tests** | Low | HIGH | Gate G3 enforces 80% coverage minimum; no bypass mechanism |
| **Agent accumulates tech debt** | Medium | MEDIUM | Gate G4 human architect review for >500 LOC; periodic code quality audits |
| **Agent costs spiral** | Medium | MEDIUM | Prompt caching reduces cost by 8x; per-session cost caps ($5/session default) |
| **Agent enters infinite retry loop** | Low | LOW | `max_retries=3` hard limit; automatic escalation to human |

---

## 8. Adoption Phases

| Phase | Deliverable | Risk Level |
|-------|-------------|-----------|
| **Phase 1** | Document methodology (this standard) + platform ADR | None (documentation only) |
| **Phase 2** | Implement Initializer Agent with Gate G1 integration | LOW |
| **Phase 3** | Implement Coding Agent loop with Gates G2/G3 | MEDIUM |
| **Phase 4** | Full E2E test + internal pilot | MEDIUM |
| **Phase 5** | Customer pilot | HIGH (external dependency) |

---

## 9. Comparison with Industry Approaches

| Aspect | Devin | SWE-Agent | Anthropic Quickstart | SDLC 6.1.1 |
|--------|-------|-----------|---------------------|------------|
| **Quality Gates** | None | None | Command allowlist | 4-Gate Pipeline |
| **Security** | Black box | Sandboxed | Bash allowlist | Policy-as-Code + SAST + Evidence |
| **Audit Trail** | Limited | Git only | Git + JSON | Evidence Vault (immutable) |
| **Human Review** | Optional | Optional | None (auto) | Mandatory for >500 LOC |
| **Resumability** | Proprietary | Per-session | `feature_list.json` + git | Evidence State Machine |
| **Cost Control** | Subscription | Per-API call | Per-API call | Prompt caching (8x reduction) |

---

## 10. AI Governance Principles Alignment

This methodology aligns with SDLC 6.1.1 AI Governance Principles:

| Principle | How This Methodology Complies |
|-----------|-------------------------------|
| **1. Human-in-the-Loop** | Gate G4 requires human architect review for significant changes |
| **2. Framework-First** | Methodology documented in Framework before implementation in any platform |
| **3. Evidence-Based** | Every feature generates Evidence Vault artifacts (SAST, tests, review) |
| **4. Progressive Trust** | Auto-merge for small changes; human review escalates with complexity |
| **5. Transparent Operations** | Full audit trail: spec → features → code → evidence → merge |
| **6. Bounded Autonomy** | `max_retries=3`, cost caps, scope limits prevent runaway agents |
| **7. Continuous Learning** | Retry patterns feed back into prompt optimization |

---

## 11. References

- **SDLC 6.1.1**: Section 7 (Quality Assurance System), AI Governance Principles
- **Industry**: Open-source autonomous coding agent patterns (two-agent, JSON persistence)
- **Security**: OWASP Top 10, CWE Top 25 for AI-generated code validation

---

**Document Status**: APPROVED
**Approved By**: CTO
**Ring**: Core (timeless methodology, tool-agnostic)
**Next Review**: After Phase 4 pilot implementation
