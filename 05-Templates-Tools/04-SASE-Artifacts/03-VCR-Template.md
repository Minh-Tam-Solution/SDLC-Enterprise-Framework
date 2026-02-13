# Version Controlled Resolution (VCR) Template
## SASE Artifact for SE 3.0 SDLC Integration

**Reference:** arXiv:2509.06216v2 - Software Agentic Software Engineering

**Purpose:** Human decision record for accepting, rejecting, or requesting revision of agent work
**Author:** SE4H (Software Engineering for Humans - Agent Coach)
**Consumer:** SE4A (for revision) + Git History (permanent record)

**Version:** 1.2.0
**Framework:** SDLC 6.0.5 (7-Pillar Architecture)
**Created:** December 2025
**Updated:** January 22, 2026
**AI Governance:** Aligned with [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) principles

---

## 📋 VCR METADATA

| Field | Value |
|-------|-------|
| **VCR ID** | VCR-YYYY-NNN (e.g., VCR-2026-001) |
| **Created** | YYYY-MM-DD HH:MM:SS UTC |
| **Decision** | APPROVED \| REJECTED \| REVISION_REQUIRED |
| **Reviewer** | [SE4H Name/Role] |

---

## 🔗 TRACEABILITY

| Reference | ID | Link |
|-----------|------|------|
| **Source MRP** | MRP-YYYY-NNN | [Link to Merge-Readiness Pack] |
| **Source BRS** | BRS-YYYY-NNN | [Link to BriefingScript] |
| **Source LPS** | LPS-YYYY-NNN | [Link to LoopScript] |
| **Project** | PRJ-XXX | [Link to Project] |
| **Pull Request** | PR #NNN | [Link to GitHub PR] |
| **SDLC Gate** | G0.1 \| G1 \| G2 \| G3 \| G4 \| G-Sprint \| G-Sprint-Close | Gate this work supports |

### Sprint Planning Governance Verification (SDLC 6.0.5)

| Criterion | Verified | Notes |
|-----------|----------|-------|
| **Sprint Reference** | ✅ / ❌ | SPRINT-XXX present in BRS/PR |
| **Backlog Item Linked** | ✅ / ❌ | US-XXX / BUG-XXX / TT-XXX traced |
| **Sprint Goal Alignment** | ✅ / ❌ | Work supports sprint goal |
| **G-Sprint Approved** | ✅ / ❌ | Work started after gate approval |
| **DoD Verification** | ✅ / ❌ | All DoD criteria met |

---

## 📊 MRP EVALUATION SUMMARY

### Quick Assessment

| Category | MRP Claimed | Verified | Status |
|----------|-------------|----------|--------|
| **Sprint Governance (5.2.0)** | Compliant | XX% | ✅ / ⚠️ / ❌ |
| **Definition of Done** | Complete | XX/6 criteria | ✅ / ⚠️ / ❌ |
| **Functional Completeness** | 100% | XX% | ✅ / ⚠️ / ❌ |
| **Test Coverage** | 95% | XX% | ✅ / ⚠️ / ❌ |
| **Security Scan** | Clean | XX findings | ✅ / ⚠️ / ❌ |
| **Performance (p95)** | 85ms | XXms | ✅ / ⚠️ / ❌ |
| **Code Quality** | A | X | ✅ / ⚠️ / ❌ |
| **Documentation** | Complete | XX% | ✅ / ⚠️ / ❌ |

### Overall Readiness Score

| Score | Range | Decision Guidance |
|-------|-------|-------------------|
| **X.X / 10** | 9-10: APPROVE | 7-8: APPROVE WITH CONDITIONS |
| | 5-6: REVISION | < 5: REJECT |

---

## ✅ DECISION

### Primary Decision

> **Decision:** [ ] APPROVED  [ ] REJECTED  [ ] REVISION_REQUIRED

### Decision Rationale

[Explain the reasoning behind the decision]

```
Example (APPROVED):
The MRP demonstrates complete implementation of all BRS requirements.
Sprint Governance verified: SPRINT-086 context present, US-456 linked.
DoD complete: all 6 criteria met. Test coverage exceeds threshold 
(95% vs 90% required). Security scan is clean. Performance meets 
targets. Code follows project standards. Ready for merge.

Example (REJECTED):
Critical security vulnerability found (SQL injection in line 45).
Fundamental architectural issue - violates AGPL containment by
importing MinIO SDK directly. Requires complete rewrite of storage
integration.

Example (REVISION_REQUIRED):
Good implementation overall, but:
1. Missing test for concurrent update scenario
2. Docstrings incomplete on 3 methods
3. Performance slightly above target (105ms vs 100ms target)
Minor fixes required before approval.
```

---

## 📝 DETAILED REVIEW

### Functional Review

| Requirement | MRP Status | Verified | Notes |
|-------------|------------|----------|-------|
| F1: [Description] | ✅ PASS | ✅ Confirmed | Works as expected |
| F2: [Description] | ✅ PASS | ⚠️ Partial | Edge case not covered |
| F3: [Description] | ✅ PASS | ✅ Confirmed | Tested manually |

**Functional Gaps Identified:**
- [Gap 1 description, if any]
- [Gap 2 description, if any]

### Security Review

| Check | MRP Status | Verified | Notes |
|-------|------------|----------|-------|
| Authentication | ✅ | ✅ | All endpoints protected |
| Authorization | ✅ | ✅ | RBAC correctly applied |
| Input Validation | ✅ | ⚠️ | Missing validation on field X |
| AGPL Containment | ✅ | ✅ | No AGPL imports |
| Secrets Handling | ✅ | ✅ | Using env variables |

**Security Concerns:**
- [Concern 1, if any]
- [Concern 2, if any]

### Code Quality Review

| Aspect | Assessment | Notes |
|--------|------------|-------|
| Readability | ⭐⭐⭐⭐⭐ | Clean, well-organized |
| Maintainability | ⭐⭐⭐⭐ | Good separation of concerns |
| Test Quality | ⭐⭐⭐⭐⭐ | Comprehensive test cases |
| Documentation | ⭐⭐⭐⭐ | Minor gaps in docstrings |
| Patterns Adherence | ⭐⭐⭐⭐⭐ | Follows MentorScript |

**Code Quality Notes:**
- [Note 1]
- [Note 2]

### Performance Review

| Metric | Target | Claimed | Verified | Status |
|--------|--------|---------|----------|--------|
| API p95 Latency | < 100ms | 85ms | 92ms | ✅ |
| Database Query | < 50ms | 15ms | 18ms | ✅ |
| Memory Impact | < 10MB | +4MB | +5MB | ✅ |

**Performance Notes:**
- [Note 1]
- [Note 2]

---

## 🔧 REQUIRED CHANGES (if REVISION_REQUIRED)

### Critical Changes (MUST fix before re-submission)

| ID | Description | File/Location | Severity |
|----|-------------|---------------|----------|
| RC-1 | [Description of required change] | `path/to/file.py:45` | CRITICAL |
| RC-2 | [Description of required change] | `path/to/file.py:78` | HIGH |

### Recommended Changes (SHOULD fix, but not blocking)

| ID | Description | File/Location | Priority |
|----|-------------|---------------|----------|
| RR-1 | [Description of recommended change] | `path/to/file.py:120` | MEDIUM |
| RR-2 | [Description of recommended change] | `path/to/file.py:135` | LOW |

### Revision Instructions

[Detailed instructions for SE4A on how to address the required changes]

```
Example:
1. Fix SQL injection vulnerability in user_service.py:45
   - Use parameterized query instead of string interpolation
   - Add test case for malicious input

2. Complete docstrings for:
   - get_user_by_id() - missing Args section
   - create_project() - missing Raises section
   - update_gate_status() - missing Example

3. Improve performance:
   - Add index on resources.project_id
   - Use eager loading for projects.gates relationship
```

### Re-submission Checklist

When resubmitting, SE4A must:
- [ ] Address all CRITICAL and HIGH severity issues
- [ ] Run full test suite again
- [ ] Update MRP with revision notes
- [ ] Reference this VCR in revision

---

## 📊 EVIDENCE VERIFICATION

### MRP Evidence Spot-Checked

| Evidence | Verified | Method | Result |
|----------|----------|--------|--------|
| Test Report | ✅ | Ran `pytest` locally | Matches MRP |
| Coverage | ✅ | Reviewed coverage.html | 95% confirmed |
| Security Scan | ✅ | Ran Semgrep | 0 critical/high |
| Benchmark | ⚠️ | Ran quick test | Slightly higher than claimed |

### Additional Evidence Requested (if any)

- [ ] [Description of additional evidence needed]
- [ ] [Description of additional evidence needed]

---

## 🏷️ APPROVAL DETAILS (if APPROVED)

### Merge Authorization

| Field | Value |
|-------|-------|
| **Approved By** | [Name] |
| **Role** | [Tech Lead / Architect / CTO] |
| **Approved At** | YYYY-MM-DD HH:MM:SS UTC |
| **Merge Deadline** | YYYY-MM-DD (e.g., 48 hours from approval) |

### Merge Conditions (if any)

- [ ] **No conditions** - Merge immediately
- [ ] **Condition 1:** [Description]
- [ ] **Condition 2:** [Description]

### Post-Merge Actions

- [ ] Monitor error rates for 24 hours
- [ ] Verify performance metrics in production
- [ ] Update project documentation
- [ ] Close related issues/tickets

---

## 🚫 REJECTION DETAILS (if REJECTED)

### Rejection Reason

> **Primary Reason:** [Brief statement of why rejected]

### Fundamental Issues

1. **Issue 1:** [Description]
   - Why this is blocking: [Explanation]
   - What would need to change: [Guidance]

2. **Issue 2:** [Description]
   - Why this is blocking: [Explanation]
   - What would need to change: [Guidance]

### Remediation Path

[Guidance on how to proceed after rejection]

```
Example:
This implementation cannot be salvaged due to fundamental architecture
violations. Please:

1. Start fresh with a new BRS that clarifies the AGPL containment requirement
2. Review MentorScript Section 3.3 (AGPL Containment) before implementation
3. Schedule architecture review before coding begins
4. Consider reaching out via CRP for guidance on storage integration
```

### Re-attempt Allowed?

- [ ] **Yes** - New MRP can be submitted after addressing issues
- [ ] **No** - Requires new BRS and LPS
- [ ] **Escalated** - Decision to be made by [Role]

---

## 📈 METRICS & ANALYTICS

### Review Metrics

| Metric | Value |
|--------|-------|
| **MRP Submitted** | YYYY-MM-DD HH:MM |
| **Review Started** | YYYY-MM-DD HH:MM |
| **Review Completed** | YYYY-MM-DD HH:MM |
| **Review Duration** | X hours Y minutes |
| **Iterations** | N (1 = first submission) |

### Agent Performance Assessment

| Metric | Score | Notes |
|--------|-------|-------|
| Requirement Coverage | X/10 | All requirements addressed |
| Code Quality | X/10 | Follows standards |
| Testing Thoroughness | X/10 | Comprehensive tests |
| Documentation | X/10 | Clear and complete |
| Security Awareness | X/10 | No vulnerabilities |
| **Overall** | **X/10** | [Summary] |

### Feedback for Agent Improvement

[Constructive feedback to help SE4A improve on future tasks]

```
Example:
Strengths:
- Excellent test coverage and test case design
- Clean code following project patterns
- Good error handling

Areas for improvement:
- Consider edge cases earlier (found 2 during review)
- Performance testing should include concurrent users
- Docstrings should include Examples section for complex methods
```

---

## 🔄 VERSION CONTROL INTEGRATION

### Git Operations (if APPROVED)

```bash
# Merge command
git checkout main
git pull origin main
git merge --no-ff feature/xxx -m "Merge PR #NNN: [Description]

VCR: VCR-YYYY-NNN
MRP: MRP-YYYY-NNN
BRS: BRS-YYYY-NNN

Reviewed-by: [Name] <email@company.com>

🤖 AI-assisted development with human review"

git push origin main

# Tag release (if applicable)
git tag -a v1.X.X -m "Release v1.X.X: [Description]"
git push origin v1.X.X
```

### Evidence Vault Entry

| Field | Value |
|-------|-------|
| **VCR Path** | `/evidence/vcr/VCR-YYYY-NNN/` |
| **VCR SHA256** | `xxx...` |
| **Archived At** | YYYY-MM-DD HH:MM:SS UTC |
| **Retention** | 7 years (compliance) |

---

## ✍️ REVIEWER ATTESTATION

I, [Reviewer Name], as SE4H (Agent Coach), attest that:

- [x] I have reviewed the MRP thoroughly
- [x] I have verified critical evidence claims
- [x] I have assessed security implications
- [x] I have considered performance impact
- [x] My decision is based on objective criteria
- [x] This VCR accurately reflects my assessment

**Reviewer Signature:** [Digital signature or name]
**Role:** [Tech Lead / Architect / etc.]
**Date:** YYYY-MM-DD

---

## 📎 ATTACHMENTS

### Review Notes

[Any additional notes, screenshots, or diagrams from the review]

### Communication Log

| Date | From | To | Subject | Reference |
|------|------|----|---------|-----------|
| YYYY-MM-DD | SE4A | SE4H | CRP-XXX clarification | CRP-YYYY-NNN |
| YYYY-MM-DD | SE4H | SE4A | Design guidance | Email thread |

---

## 🏷️ TEMPLATE USAGE NOTES

### VCR Principles

1. **Objective Assessment:** Base decisions on evidence, not assumptions
2. **Clear Communication:** Explain reasoning for SE4A to learn
3. **Actionable Feedback:** Provide specific guidance for revisions
4. **Permanent Record:** VCR is the authoritative decision document

### Decision Criteria

| Decision | When to Use |
|----------|-------------|
| **APPROVED** | All requirements met, no blocking issues |
| **APPROVED WITH CONDITIONS** | Minor issues, can merge after small fixes |
| **REVISION_REQUIRED** | Significant issues, but approach is sound |
| **REJECTED** | Fundamental issues, requires new approach |

### VCR Lifecycle

```
MRP Submitted → VCR Created → Review → Decision
                                          ↓
                            ┌─────────────┼─────────────┐
                            ↓             ↓             ↓
                        APPROVED    REVISION      REJECTED
                            ↓             ↓             ↓
                         Merge    New MRP cycle   New BRS needed
```

### Reviewer Responsibilities

- Verify MRP claims (spot-check, not 100% audit)
- Assess security implications
- Consider long-term maintainability
- Provide constructive feedback
- Make timely decisions (< 24h for P1 items)

**Reference:** SDLC-Agentic-Core-Principles.md
