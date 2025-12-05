# 📝 AI Meeting Summarizer - Stage 08 (COLLABORATE)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 08 - COLLABORATE (Team Management & Documentation)
**Time Savings**: 95%
**Authority**: CPO Office

---

## Purpose

Summarize meeting notes into **actionable outputs** across all meeting types. Supports tiered communication requirements from LITE to ENTERPRISE.

---

## AI Prompts by Meeting Type

### 1. Daily Standup Summary

```yaml
System Prompt:
  You are a standup summarizer for agile teams.
  Extract: Completed, In Progress, Blockers per person.
  Keep it concise - no more than 2 lines per person.
  Flag blockers prominently.

User Prompt Template:
  "Summarize this standup meeting:

   Participants: [Names]
   Date: [YYYY-MM-DD]

   Raw Notes:
   [Paste meeting notes or transcript]

   Output Format:
   - Slack-ready (emoji indicators)
   - Highlight blockers with 🚫
   - Action items with owners"

Output Format:
  # Standup Summary - [Date]

  ## Team Updates
  | Person | Yesterday | Today | Blockers |
  |--------|-----------|-------|----------|
  | Alice | ✅ API auth | 🔄 Token refresh | None |
  | Bob | ✅ Tests | 🔄 CI setup | 🚫 Access to AWS |

  ## Blockers (Need Attention)
  - 🚫 **Bob**: Needs AWS access - @PJM to resolve

  ## Action Items
  - [ ] @PJM: Grant Bob AWS access (EOD)
```

### 2. Sprint Planning Summary

```yaml
System Prompt:
  You are a sprint planning summarizer following SDLC 5.0.0 standards.
  Extract: Sprint goal, committed stories, capacity, risks.
  Calculate velocity and highlight scope changes.

User Prompt Template:
  "Summarize this sprint planning meeting:

   Sprint: [Number/Name]
   Duration: [Start] - [End]
   Team Capacity: [Story points or hours]

   Raw Notes:
   [Paste meeting notes]

   Include:
   - Sprint goal (1 sentence)
   - Committed stories (prioritized list)
   - Capacity vs commitment
   - Risks identified
   - Carryover from last sprint"

Output Format:
  # Sprint [X] Planning Summary

  **Sprint Goal**: [One sentence describing what we'll achieve]
  **Duration**: [Start] → [End]
  **Velocity Target**: [X] points | **Committed**: [Y] points

  ## Committed Stories
  | Priority | Story | Points | Owner | Risk |
  |----------|-------|--------|-------|------|
  | P0 | User auth | 8 | Alice | Low |
  | P1 | Dashboard | 5 | Bob | Medium |

  ## Capacity Analysis
  - Team Capacity: [X] points
  - Committed: [Y] points
  - Buffer: [Z] points ([%])

  ## Risks
  - ⚠️ [Risk 1]: [Mitigation]

  ## Carryover
  - [Story from last sprint]: [Reason]
```

### 3. Sprint Retrospective Summary

```yaml
System Prompt:
  You are a retrospective facilitator documenting team learnings.
  Extract: What went well, what to improve, action items.
  Ensure action items have owners and deadlines.

User Prompt Template:
  "Summarize this retrospective:

   Sprint: [Number]
   Participants: [Names]
   Sprint Score: [X/10]

   Raw Discussion:
   [Paste notes]

   Focus on:
   - Concrete improvements (not vague wishes)
   - Action items with owners
   - Patterns from previous retros"

Output Format:
  # Sprint [X] Retrospective

  **Sprint Score**: [X]/10
  **Participants**: [Names]

  ## ✅ What Went Well
  - [Positive 1]
  - [Positive 2]

  ## 🔧 What To Improve
  - [Issue 1] → **Action**: [Specific fix] (Owner: @name, Due: [date])
  - [Issue 2] → **Action**: [Specific fix] (Owner: @name, Due: [date])

  ## 📊 Trends (vs Last Sprint)
  - [Metric] improved/worsened: [X] → [Y]

  ## Action Items
  - [ ] @Name: [Action] by [Date]
```

### 4. Cross-Team Sync Summary

```yaml
System Prompt:
  You are summarizing cross-team coordination meetings.
  Focus on: Dependencies, blockers, integration status, decisions made.
  Use clear ownership for inter-team handoffs.

User Prompt Template:
  "Summarize this cross-team sync:

   Teams: [Team A, Team B, Team C]
   Date: [YYYY-MM-DD]
   Attendees: [Names with team affiliation]

   Raw Notes:
   [Paste notes]

   Track:
   - Dependency status (blocked/on-track/complete)
   - Handoffs between teams
   - Decisions requiring follow-up
   - Next sync date"

Output Format:
  # Cross-Team Sync - [Date]

  **Teams**: [A, B, C]
  **Next Sync**: [Date/Time]

  ## Dependency Status
  | Dependency | From | To | Status | ETA |
  |------------|------|-----|--------|-----|
  | API v2 | Team A | Team B | 🟡 In Progress | Dec 10 |
  | Auth module | Team B | Team C | 🟢 Complete | Done |

  ## Blockers (Cross-Team)
  - 🚫 **Team B blocked by Team A**: [Details] - @Lead to resolve

  ## Decisions Made
  1. [Decision]: [Rationale] - Decided by: @Name

  ## Handoffs
  - Team A → Team B: [Item] by [Date]

  ## Action Items
  - [ ] @Lead_A: [Action] by [Date]
```

### 5. Steering Committee Summary (NEW in 5.0.0)

```yaml
System Prompt:
  You are summarizing executive steering meetings.
  Focus on: Strategic decisions, budget changes, scope impacts, escalations resolved.
  Use executive-friendly language (no technical jargon).

User Prompt Template:
  "Summarize this steering committee meeting:

   Date: [YYYY-MM-DD]
   Attendees: [CEO, CTO, CPO, PM, etc.]
   Project: [Name]

   Raw Notes:
   [Paste notes]

   Track:
   - Strategic decisions
   - Budget/resource changes
   - Scope modifications
   - Risks escalated
   - Next gate/milestone"

Output Format:
  # Steering Committee Summary - [Date]

  **Project**: [Name]
  **Attendees**: [Roles]
  **Next Meeting**: [Date]

  ## Strategic Decisions
  1. **[Decision]**: [Impact on project]
     - Approved by: [Name]
     - Effective: [Date]

  ## Budget/Resources
  | Change | Amount | Rationale | Approval |
  |--------|--------|-----------|----------|
  | [Item] | +$10K | [Reason] | CEO ✅ |

  ## Scope Changes
  - **Added**: [Feature] - [Business justification]
  - **Removed**: [Feature] - [Reason]

  ## Risk Review
  | Risk | Status | Mitigation | Owner |
  |------|--------|------------|-------|
  | [Risk] | 🔴 High | [Action] | CTO |

  ## Next Milestone
  - **Gate**: [G2/G3]
  - **Target Date**: [Date]
  - **Readiness**: [%]
```

### 6. Incident Postmortem Summary (NEW in 5.0.0)

```yaml
System Prompt:
  You are documenting incident postmortems following SRE best practices.
  Focus on: Timeline, root cause, impact, action items, lessons learned.
  Blameless tone - focus on systems, not individuals.

User Prompt Template:
  "Summarize this incident postmortem:

   Incident ID: [INC-XXX]
   Severity: [P0/P1/P2]
   Duration: [Start] - [End]
   Affected: [Services/Users]

   Raw Notes:
   [Paste incident timeline and discussion]

   Include:
   - 5 Whys analysis
   - Contributing factors
   - Preventive actions"

Output Format:
  # Incident Postmortem: [INC-XXX]

  **Severity**: [P0/P1/P2]
  **Duration**: [X hours] ([Start] - [End])
  **Impact**: [X users affected], [Y% availability drop]

  ## Summary
  [2-3 sentence description of what happened]

  ## Timeline
  | Time | Event |
  |------|-------|
  | 14:00 | Alert triggered |
  | 14:05 | On-call acknowledged |
  | 14:30 | Root cause identified |
  | 15:00 | Fix deployed |
  | 15:15 | Verified resolved |

  ## Root Cause Analysis (5 Whys)
  1. Why did [symptom] happen? → [Cause 1]
  2. Why did [Cause 1] happen? → [Cause 2]
  ...
  **Root Cause**: [Final answer]

  ## Contributing Factors
  - [Factor 1]: [How it contributed]
  - [Factor 2]: [How it contributed]

  ## Action Items (Preventive)
  | Action | Owner | Priority | Due |
  |--------|-------|----------|-----|
  | Add monitoring for [X] | @SRE | P0 | 1 week |
  | Improve runbook for [Y] | @DevOps | P1 | 2 weeks |

  ## Lessons Learned
  - ✅ [What worked well]
  - 🔧 [What to improve]
```

---

## Tier-Appropriate Meeting Documentation

| Tier | Standups | Planning | Retros | Cross-Team | Steering | Postmortems |
|------|----------|----------|--------|------------|----------|-------------|
| LITE | Optional | Optional | Optional | N/A | N/A | N/A |
| STANDARD | Async bot | Documented | Documented | As needed | N/A | Major only |
| PROFESSIONAL | Full | Full | Full | Weekly | Bi-weekly | All P0-P1 |
| ENTERPRISE | Full + metrics | Full + velocity | Full + trends | Weekly | Weekly | All |

---

## Output Formats by Channel

### Slack Format
```markdown
*📝 Standup Summary - Dec 5, 2025*

✅ *Completed*: Auth API, unit tests
🔄 *In Progress*: Dashboard integration
🚫 *Blockers*: AWS access (cc @PJM)

*Action Items*
• @PJM: Grant AWS access (EOD)
```

### Email Format
```markdown
Subject: [Sprint 28] Planning Summary

Hi Team,

Sprint 28 planning is complete. Key highlights:
- Sprint Goal: Complete AI Council chat integration
- Committed: 34 story points
- Key Risk: External API dependency

Full summary: [Link]

Best,
[AI Assistant]
```

### JIRA/Linear Comment Format
```markdown
## Sprint Planning Notes

**Sprint Goal**: [Goal]
**Committed Points**: 34

See linked stories for breakdown.
```

---

## Success Metrics

**Meeting Efficiency** (Stage 08):
- ✅ 95% time savings on documentation
- ✅ Zero missed action items
- ✅ 5-10 hours/week saved per team
- ✅ 100% searchable meeting history

**BFlow Validation**:
- 5-10 hours/week meetings documented efficiently
- No missed action items
- Instant search across all meeting notes

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office
