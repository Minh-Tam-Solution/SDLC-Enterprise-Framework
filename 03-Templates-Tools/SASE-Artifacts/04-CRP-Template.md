# Consultation Request Protocol (CRP) Template
## SASE Artifact for SE 3.0 SDLC Integration

**Reference:** arXiv:2509.06216v2 - Software Agentic Software Engineering

**Purpose:** AI-generated request for human guidance when facing uncertainty or blockers
**Author:** SE4A (Software Engineering for Agents - Agent Executor)
**Consumer:** SE4H (Software Engineering for Humans - Agent Coach)

**Version:** 1.1.0
**Framework:** SDLC 5.1.3 (7-Pillar Architecture)
**Created:** December 2025
**Updated:** January 2025

---

## 📋 CRP METADATA

| Field | Value |
|-------|-------|
| **CRP ID** | CRP-YYYY-NNN (e.g., CRP-2026-001) |
| **Created** | YYYY-MM-DD HH:MM:SS UTC |
| **Status** | OPEN \| IN_REVIEW \| RESOLVED \| CANCELLED |
| **Priority** | P0-BLOCKER \| P1-HIGH \| P2-MEDIUM \| P3-LOW |
| **Category** | CLARIFICATION \| DECISION \| PERMISSION \| TECHNICAL \| SCOPE |

---

## 🔗 CONTEXT REFERENCES

| Reference | ID | Description |
|-----------|------|-------------|
| **Source BRS** | BRS-YYYY-NNN | The BriefingScript being executed |
| **Source LPS** | LPS-YYYY-NNN | The LoopScript in progress |
| **Blocked Step** | STEP-X.Y | Specific step that is blocked |
| **Project** | PRJ-XXX | Project identifier |
| **Agent Session** | SESSION-XXXXX | Current execution session |

### Sprint Planning Governance (NEW in 5.1.3)

| Governance | Value |
|------------|-------|
| **Sprint ID** | SPRINT-XXX |
| **Backlog Item** | US-XXX \| BUG-XXX \| TT-XXX |
| **Sprint Goal Impact** | Blocking \| Delaying \| No Impact |
| **DoD Risk** | CRP resolution required for DoD |

---

## ❓ CONSULTATION REQUEST

### Request Type

- [ ] **CLARIFICATION** - Need clarity on ambiguous requirement
- [ ] **DECISION** - Multiple valid approaches, need human choice
- [ ] **PERMISSION** - Action may exceed authorized scope
- [ ] **TECHNICAL** - Technical challenge beyond current capability
- [ ] **SCOPE** - Potential scope creep or boundary issue

### Summary

> **One-line summary:** [Brief description of what guidance is needed]

### Detailed Question

[Provide a detailed explanation of the situation and what specific guidance is needed]

```
Example:
The BRS specifies "implement user authentication" but does not clarify:
1. Should we use JWT tokens or session-based authentication?
2. Is OAuth integration required for social login?
3. What should be the token expiration policy?

Without this clarification, I cannot proceed with STEP-2.2 (Implement auth service).
```

---

## 📊 SITUATION ANALYSIS

### Current State

| Aspect | Status | Details |
|--------|--------|---------|
| **Execution Progress** | XX% complete | Steps 1-3 done, blocked at Step 4 |
| **Time Elapsed** | X hours Y minutes | Started at YYYY-MM-DD HH:MM |
| **Iteration** | N of M | Current loop iteration |

### What I've Tried

1. **Attempt 1:** [Description of first approach]
   - Result: [What happened]
   - Why it failed: [Explanation]

2. **Attempt 2:** [Description of second approach]
   - Result: [What happened]
   - Why it failed: [Explanation]

3. **Research Conducted:**
   - Checked MentorScript for guidance: [Found/Not found]
   - Searched codebase for patterns: [Results]
   - Reviewed related ADRs: [Relevant findings]

### Why Human Guidance Needed

[Explain why this cannot be resolved autonomously]

```
Example:
This is a DECISION request because:
- Both JWT and session-based approaches are valid
- Each has trade-offs (stateless vs server memory)
- The choice impacts future architecture
- This architectural decision should not be made autonomously
```

---

## 🎯 OPTIONS ANALYSIS

### Option A: [First Option Name]

**Description:** [What this option entails]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Effort Estimate:** [Low/Medium/High]

**Risk Level:** [Low/Medium/High]

---

### Option B: [Second Option Name]

**Description:** [What this option entails]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Effort Estimate:** [Low/Medium/High]

**Risk Level:** [Low/Medium/High]

---

### Option C: [Third Option Name] (if applicable)

**Description:** [What this option entails]

**Pros:**
- [Advantage 1]
- [Advantage 2]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]

**Effort Estimate:** [Low/Medium/High]

**Risk Level:** [Low/Medium/High]

---

## 💡 AGENT RECOMMENDATION

### Recommended Option

> **Recommendation:** Option [A/B/C]

### Rationale

[Explain why this option is recommended based on:]
- Alignment with BRS requirements
- Consistency with MentorScript patterns
- Risk/effort trade-offs
- Long-term maintainability

### Confidence Level

| Metric | Value |
|--------|-------|
| **Confidence** | LOW \| MEDIUM \| HIGH |
| **Uncertainty Factors** | [List what makes this uncertain] |
| **Would Benefit From** | [Additional context that would help] |

---

## ⏰ IMPACT OF DELAY

### Current Block Status

| Metric | Status |
|--------|--------|
| **Execution State** | PAUSED at STEP-X.Y |
| **Blocking Others** | Yes/No - [Details if yes] |
| **Deadline Impact** | [How delay affects timeline] |

### Time Sensitivity

- [ ] **CRITICAL** - Blocks all progress, immediate response needed
- [ ] **HIGH** - Blocks current phase, response needed within 2 hours
- [ ] **MEDIUM** - Can work on other items, response needed within 1 day
- [ ] **LOW** - Non-blocking, response needed before next iteration

---

## 📝 SE4H RESPONSE SECTION

> *This section to be completed by SE4H (Agent Coach)*

### Decision

| Field | Response |
|-------|----------|
| **Responded By** | [Name/Role] |
| **Responded At** | YYYY-MM-DD HH:MM:SS UTC |
| **Selected Option** | A \| B \| C \| Other |

### Guidance Provided

[SE4H's detailed guidance for the agent]

```
Example:
Use Option A (JWT tokens) with the following specifications:
- Access token expiry: 15 minutes
- Refresh token expiry: 7 days
- Use RS256 algorithm
- Store refresh tokens in Redis

Rationale: JWT aligns with our microservices roadmap and the short
access token expiry mitigates token theft risk.
```

### Additional Context

[Any additional information or constraints to consider]

### Updated Constraints

- [ ] No new constraints
- [ ] New constraint added: [Description]
- [ ] Existing constraint modified: [Description]

### Approval to Proceed

- [ ] **APPROVED** - Proceed with selected option
- [ ] **APPROVED WITH MODIFICATIONS** - Proceed with noted changes
- [ ] **REJECTED** - Do not proceed, wait for further guidance
- [ ] **ESCALATED** - Escalating to [Role/Person]

---

## 📎 ATTACHMENTS

### Code Snippets

```python
# Relevant code that illustrates the question
def authenticate_user(username: str, password: str):
    # Current implementation - need guidance on next step
    user = await get_user_by_username(username)
    if verify_password(password, user.password_hash):
        # QUESTION: What should happen here?
        # Option A: Generate JWT token
        # Option B: Create session in Redis
        pass
```

### Screenshots/Diagrams

[Link or embed relevant visuals]

### Related Documents

- [Link to relevant ADR]
- [Link to related BRS section]
- [Link to MentorScript section]

---

## 🔄 RESOLUTION TRACKING

### Resolution Status

| Field | Value |
|-------|-------|
| **Resolved At** | YYYY-MM-DD HH:MM:SS UTC |
| **Resolution Time** | X hours Y minutes |
| **Resolved By** | [SE4H Name] |

### Resolution Summary

[Brief summary of how this was resolved]

### Follow-up Actions

- [ ] Update MentorScript with new guidance
- [ ] Create ADR for architectural decision
- [ ] Update BRS for future clarity
- [ ] No follow-up needed

### Lessons Learned

[What can be done to prevent similar CRPs in the future?]

---

## 📊 CRP METRICS (Auto-populated)

| Metric | Value |
|--------|-------|
| **Time to First Response** | X hours |
| **Time to Resolution** | X hours |
| **Category** | CLARIFICATION/DECISION/etc |
| **Priority** | P0/P1/P2/P3 |
| **Required Escalation** | Yes/No |

---

## 🏷️ TEMPLATE USAGE NOTES

### When to Create a CRP

**DO create CRP when:**
- Requirement is genuinely ambiguous
- Multiple valid approaches exist
- Action may exceed authorized scope
- Technical challenge requires human expertise
- Potential scope creep detected

**DON'T create CRP for:**
- Issues covered in MentorScript
- Standard coding decisions
- Obvious next steps
- Performance optimizations within tolerance

### CRP Lifecycle

```
CREATED → OPEN → IN_REVIEW → RESOLVED
                      ↓
                  CANCELLED (if no longer needed)
```

### Priority Guidelines

| Priority | Response Time | Use When |
|----------|---------------|----------|
| P0-BLOCKER | < 30 min | All progress blocked |
| P1-HIGH | < 2 hours | Phase blocked |
| P2-MEDIUM | < 1 day | Can work around |
| P3-LOW | < 3 days | Nice to have clarity |

### Quality Checklist

Before submitting CRP:
- [ ] Checked MentorScript for existing guidance
- [ ] Searched codebase for similar patterns
- [ ] Reviewed relevant ADRs
- [ ] Provided at least 2 options
- [ ] Included recommendation with rationale
- [ ] Specified impact of delay

**Reference:** SDLC-Agentic-Core-Principles.md
