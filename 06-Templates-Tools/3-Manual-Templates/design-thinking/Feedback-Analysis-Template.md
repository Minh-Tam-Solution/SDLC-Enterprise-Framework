# 📊 Feedback Analysis Template

**Purpose**: Synthesize user testing results into actionable insights and decisions
**When to Use**: TEST phase, after completing 5-8 user sessions (SDLC Stage 03 - BUILD)
**Time Required**: 2-4 hours
**Participants**: Facilitator + Note-Taker + Product Manager + Designer

---

## 📋 How to Use This Template

1. **Complete all testing sessions first** - Don't analyze until you have 5+ sessions
2. **Gather all artifacts** - Videos, notes, recordings, debrief summaries
3. **Look for patterns** - Issues mentioned by 3+ users are significant
4. **Quantify where possible** - Task completion rates, time on task, ratings
5. **Prioritize ruthlessly** - Not all feedback is equal

---

## 🎯 TESTING SUMMARY

### Overview:

```yaml
Product/Feature Tested: [Name of prototype]
Test Dates: [Start date] - [End date]
Number of Sessions: [X sessions completed]
Participants: [Brief description of user types]
Facilitators: [Names]
```

**Example**:
```yaml
Product/Feature Tested: TrustCheck Attendance App (Prototype v1)
Test Dates: November 18-22, 2025
Number of Sessions: 6 (5 staff + 1 manager)
Participants:
  - 5 restaurant staff (ages 22-38, locations A, B, C)
  - 1 multi-location manager (3 restaurants, 45 staff)
Facilitators: Nguyen Thi Mai (PM), Tran Van Binh (UX Designer)
```

---

## 📊 QUANTITATIVE RESULTS

### Task Performance Metrics:

| Task | Participants | Completion Rate | Avg Time | Errors | Rating (1-5) |
|------|-------------|-----------------|----------|--------|--------------|
| Task 1: [Name] | [N] | [X/N = %] | [X sec] | [#] | [X.X/5] |
| Task 2: [Name] | [N] | [X/N = %] | [X sec] | [#] | [X.X/5] |
| Task 3: [Name] | [N] | [X/N = %] | [X sec] | [#] | [X.X/5] |
| Task 4: [Name] | [N] | [X/N = %] | [X sec] | [#] | [X.X/5] |

**Definitions**:
- **Completion Rate**: % who completed without facilitator help
- **Avg Time**: Mean time from task start to completion
- **Errors**: Failed attempts, wrong paths, retries
- **Rating**: Self-reported difficulty (1=very hard, 5=very easy)

---

**Example (NQH-Bot)**:

| Task | N | Completion | Avg Time | Errors | Rating |
|------|---|------------|----------|--------|--------|
| Check in for shift | 6 | 6/6 (100%) ✅ | 8.2 sec | 0 | 4.8/5 |
| View hours history | 6 | 4/6 (67%) ⚠️ | 23 sec | 2 | 3.5/5 |
| Check in without photo | 6 | 2/6 (33%) ❌ | N/A | 4 | 2.1/5 |
| Explore app freely | 6 | N/A | 120 sec | N/A | 4.2/5 |

**Key Observations**:
- ✅ **Primary task (check-in) excellent**: 100% completion, 8.2 sec (under 10-sec target)
- ⚠️ **Secondary task (hours history) needs improvement**: 33% failed to find it
- ❌ **Critical blocker (check-in without photo)**: Only 33% success, feature unclear
- ✅ **Overall usability positive**: High ratings for exploration

---

### Overall Usability Metrics:

```yaml
System Usability Scale (SUS): [Score out of 100]
  - Industry Benchmark: 68
  - Our Score: [X]
  - Interpretation: [Excellent/Good/OK/Poor]

Net Promoter Score (NPS): [Score -100 to +100]
  - Question: "How likely would you recommend this app to a colleague?"
  - Promoters (9-10): [X participants]
  - Passives (7-8): [X participants]
  - Detractors (0-6): [X participants]
  - NPS: [(Promoters % - Detractors %) = X]

Adoption Intent:
  - "Would use daily": [X/6 participants = X%]
  - "Would use sometimes": [X/6 participants = X%]
  - "Would not use": [X/6 participants = X%]
```

**Example (NQH-Bot)**:
```yaml
System Usability Scale (SUS): 78/100
  - Industry Benchmark: 68
  - Our Score: 78 ✅ (Above average)
  - Interpretation: Good (B+ grade)

Net Promoter Score (NPS): +67
  - Promoters (9-10): 4 participants (67%)
  - Passives (7-8): 2 participants (33%)
  - Detractors (0-6): 0 participants (0%)
  - NPS: 67 ✅ (Excellent - above 50 is world-class)

Adoption Intent:
  - "Would use daily": 5/6 (83%) ✅
  - "Would use sometimes": 1/6 (17%)
  - "Would not use": 0/6 (0%)
```

**Interpretation**: Strong positive results. High intent to use daily.

---

## 💬 QUALITATIVE INSIGHTS

### Pattern Analysis:

**For each pattern, count mentions across participants**

#### Pattern 1: [Theme Name]

```yaml
Mentioned by: [X/6 participants]
Severity: [Critical / High / Medium / Low]

Description:
[Describe the pattern - what did users say/do?]

Evidence (Quotes):
- P01: "[Direct quote]"
- P03: "[Direct quote]"
- P05: "[Direct quote]"

Impact:
[How does this affect user experience or adoption?]

Recommendation:
[What should we do about this?]
```

---

**Example Patterns (NQH-Bot)**:

#### Pattern 1: Trust Through Transparency (POSITIVE)

```yaml
Mentioned by: 5/6 participants (83%)
Severity: HIGH (Core value proposition)

Description:
Users consistently described GPS + photo verification as "proof" and
"transparency" rather than "surveillance". They appreciated having
verifiable evidence of their check-in.

Evidence (Quotes):
- P01: "This is proof I was here. Manager can't say I didn't show up."
- P03: "I like that there's a photo and location. It protects me."
- P04: "This feels like transparency, not Big Brother watching."
- P05: "Finally! Evidence that I came on time."
- P06 (Manager): "I trust this data more than paper forms."

Impact:
✅ Core assumption VALIDATED: Auto-verification builds trust (not erodes it)
✅ Emotional benefit: Staff feel protected (not surveilled)
✅ Manager buy-in: Increased trust in data accuracy

Recommendation:
✅ KEEP: GPS + photo verification as-is
✅ AMPLIFY: Marketing should emphasize "Staff Protection" angle
✅ CONSIDER: Add feature for staff to view their own verification data
```

---

#### Pattern 2: Battery Anxiety (NEGATIVE)

```yaml
Mentioned by: 4/6 participants (67%)
Severity: CRITICAL (Adoption blocker)

Description:
Multiple users expressed concern about phone battery dying during shift,
preventing check-in/out. This is a real operational risk in F&B where
charging access is limited.

Evidence (Quotes):
- P02: "What if my phone battery dies during my shift?"
- P03: "I can't charge at work. Battery is always low by end of shift."
- P04: "If battery dies, how do I clock out?"
- P06 (Manager): "Some staff have old phones with bad battery life."

Impact:
🚨 CRITICAL BLOCKER: If phone dies, staff cannot clock out → payroll errors
🚨 Adoption risk: Staff may refuse to use app due to battery anxiety
🚨 Inequity: Punishes staff with older phones (socioeconomic bias)

Recommendation:
🔴 FIX REQUIRED (before launch):
  Option 1: Offline mode (cache check-in, sync when reconnected)
  Option 2: Backup check-in method (manager manual entry if phone dead)
  Option 3: Provide charging stations at each location (infrastructure)
  Option 4: SMS-based check-in fallback (low-battery mode)

🔴 TEST: Validate chosen solution with 3 users before MVP
```

---

#### Pattern 3: Photo Hesitation - "Looking Messy" (NEGATIVE)

```yaml
Mentioned by: 3/6 participants (50%)
Severity: MEDIUM (Usability friction)

Description:
Some staff hesitated to take photo check-in because they felt they
"look messy" after cooking or during busy shift. This is especially
true for kitchen staff vs front-of-house staff.

Evidence (Quotes):
- P01: "I look sweaty after cooking. Don't want photo."
- P02: "Can I check in without photo sometimes?"
- P04: "Photo is fine for morning, but not end of shift."

Impact:
⚠️ Adoption friction: Staff may delay check-in to "look presentable"
⚠️ Accuracy risk: Delayed check-in defeats real-time verification purpose
⚠️ Cultural: Vietnamese culture values appearance, photo reluctance understandable

Recommendation:
🟡 CONSIDER (Medium Priority):
  Option 1: Make photo optional (GPS + timestamp only, lower trust but higher adoption)
  Option 2: Blur face in photo (verify presence, not appearance)
  Option 3: Staff can delete/retake photo (3 attempts allowed)
  Option 4: Education: "Photo is for location verification, not beauty contest"

🟡 TEST: Ask 3 users which option feels best
```

---

### What Worked Well (Continue Doing):

```yaml
Positive Finding 1:
[What users loved - keep this!]
Evidence: [Quotes or metrics]

Positive Finding 2:
[What exceeded expectations]
Evidence: [Quotes or metrics]

Positive Finding 3:
[Unexpected delight moment]
Evidence: [Quotes or metrics]
```

**Example (NQH-Bot)**:
```yaml
Positive Finding 1: One-Tap Check-In Speed
Users loved the simplicity. Average 8.2 seconds from app open to confirmed.
Evidence:
  - "This is way faster than paper forms!" (P03)
  - "I could do this while walking to my station" (P05)
  - 6/6 rated ease of use as 4.8/5

Positive Finding 2: Immediate Confirmation
Seeing check-in time immediately after confirming gave users confidence.
Evidence:
  - "I like seeing the exact time right away" (P01)
  - "Good to have proof on my phone" (P04)
  - Manager: "Real-time data is game-changer for me" (P06)

Positive Finding 3: GPS Accuracy Exceeded Expectations
Users were surprised GPS could distinguish between nearby restaurants.
Evidence:
  - "I thought GPS wouldn't work indoors, but it did!" (P02)
  - Tested at 50m apart restaurants - 9/10 accurate ✅
```

---

### What Needs Improvement (Fix Before Launch):

**Prioritize by severity:**

| Issue | Severity | Users Affected | Fix Difficulty | Priority |
|-------|----------|----------------|----------------|----------|
| [Issue 1] | Critical | X/6 | [Easy/Medium/Hard] | P0 |
| [Issue 2] | High | X/6 | [Easy/Medium/Hard] | P1 |
| [Issue 3] | Medium | X/6 | [Easy/Medium/Hard] | P2 |
| [Issue 4] | Low | X/6 | [Easy/Medium/Hard] | P3 |

**Example (NQH-Bot)**:

| Issue | Severity | Affected | Fix | Priority |
|-------|----------|----------|-----|----------|
| Battery anxiety (no fallback) | Critical | 4/6 | Hard | **P0** 🔴 |
| Hours history hard to find | High | 4/6 | Easy | **P1** 🟠 |
| Photo hesitation (appearance) | Medium | 3/6 | Medium | **P2** 🟡 |
| No export feature | Low | 1/6 | Medium | **P3** 🟢 |

**P0 (Must Fix Before Launch)**:
- Battery anxiety: Implement offline mode + SMS fallback

**P1 (Should Fix Before Launch)**:
- Hours history: Add tab navigation, make more prominent

**P2 (Nice to Have)**:
- Photo hesitation: Make photo optional OR allow retakes

**P3 (Future Enhancement)**:
- Export feature: Add to roadmap for v2

---

## 🎯 ASSUMPTION VALIDATION

**Review assumptions from Prototype Test Plan. Were they validated?**

| Assumption | Test Method | Result | Evidence |
|------------|-------------|--------|----------|
| [Assumption 1] | [How tested] | ✅ Validated / ⚠️ Partially / ❌ Invalidated | [Data] |
| [Assumption 2] | [How tested] | ✅ Validated / ⚠️ Partially / ❌ Invalidated | [Data] |
| [Assumption 3] | [How tested] | ✅ Validated / ⚠️ Partially / ❌ Invalidated | [Data] |

**Example (NQH-Bot)**:

| Assumption | Test | Result | Evidence |
|------------|------|--------|----------|
| Staff have smartphones and will use app | Asked all 6 | ✅ VALIDATED | 6/6 have smartphones, 5/6 willing to use daily |
| GPS accuracy sufficient (50m) | Tested at 3 locations | ✅ VALIDATED | 9/10 tests accurate within 50m |
| Photo feels transparent (not surveillance) | Asked 5-point scale | ✅ VALIDATED | 5/6 said "transparent", 1/6 neutral |
| Managers trust auto-verification | Showed to 1 manager | ✅ VALIDATED | Manager: "I trust this more than paper" |
| Check-in takes <10 seconds | Timed all 6 users | ✅ VALIDATED | Average 8.2 sec ✅ |
| No battery concerns | Asked open-ended | ❌ INVALIDATED | 4/6 expressed battery anxiety 🚨 |

**Critical Finding**: 5/6 assumptions validated, BUT battery anxiety is a showstopper.

---

## 🔄 DECISION MATRIX

**Based on findings, what should we do next?**

### Option A: Ship as MVP ✅

**Choose if**:
- ✅ All critical assumptions validated
- ✅ Task completion rate >80%
- ✅ Users express strong positive sentiment
- ✅ No P0 blockers (or blockers fixable in <1 week)
- ✅ Adoption intent >70%

**Next Steps**:
1. Fix P0 issues (if any)
2. Build production-ready version
3. Pilot with 10-20 users for 2 weeks
4. Iterate based on real usage
5. Full launch

---

### Option B: Iterate & Retest 🔄

**Choose if**:
- ⚠️ Some assumptions validated, others need refinement
- ⚠️ Task completion rate 50-80%
- ⚠️ Mixed user sentiment (some love, some hesitant)
- ⚠️ P0 blockers identified that need design changes
- ⚠️ Adoption intent 40-70%

**Next Steps**:
1. Prioritize fixes (P0 first)
2. Redesign problem areas
3. Build updated prototype
4. Test with 3-5 users (focused on fixes)
5. Decide again: Ship or iterate

---

### Option C: Pivot ❌

**Choose if**:
- ❌ Critical assumptions proven false
- ❌ Task completion rate <50%
- ❌ Strong negative user sentiment
- ❌ Fundamental concept issues (not just UX fixes)
- ❌ Adoption intent <40%

**Next Steps**:
1. Document what we learned
2. Return to ideation phase
3. Generate new concepts addressing root issues
4. Prototype new direction
5. Test again

---

### Option D: Pause ⏸️

**Choose if**:
- ⏸️ Results inconclusive
- ⏸️ Need different user segment (tested wrong users)
- ⏸️ External blockers (technical, business, legal)
- ⏸️ Team needs more time to process findings

**Next Steps**:
1. Identify what's unclear
2. Design follow-up research
3. Address blockers
4. Resume when ready

---

## 🎯 OUR DECISION (NQH-Bot Example):

**Decision**: **OPTION B - Iterate & Retest** 🔄

**Rationale**:
```yaml
Positive Signals:
  ✅ 5/6 assumptions validated
  ✅ Primary task (check-in) 100% success, 8.2 sec
  ✅ 83% would use daily
  ✅ NPS +67 (excellent)
  ✅ Trust/transparency validated (core value prop)

Blockers:
  🚨 Battery anxiety is P0 blocker (4/6 users concerned)
  ⚠️ Hours history navigation needs improvement (4/6 struggled)
  ⚠️ Photo hesitation creates friction (3/6 hesitant)

Conclusion:
Core concept VALIDATED, but execution has 1 critical blocker (battery) and
2 medium issues (navigation, photo). These are fixable in 1-2 weeks.

Not ready to ship without addressing battery concern (risk of failed clock-outs).
Not broken enough to pivot (strong positive sentiment overall).

→ ITERATE: Fix P0 (battery), Fix P1 (navigation), then test with 3 users.
```

---

## 📋 ITERATION PLAN

### Fixes to Implement:

**P0: Battery Anxiety (Critical)**
```yaml
Problem: 4/6 users worried about phone battery dying during shift
Impact: Prevents clock-out, causes payroll errors
Solution: Implement offline mode + SMS fallback
  - Offline: Cache check-in, sync when reconnected
  - Fallback: If battery <10%, allow SMS check-in (text code to number)
Timeline: 1 week
Owner: Backend Developer
Validation: Test with 3 users with low-battery phones
```

**P1: Hours History Navigation (High)**
```yaml
Problem: 4/6 users couldn't find hours history (took 23 sec avg)
Impact: Reduces perceived value, adoption friction
Solution: Add bottom tab navigation (Home | History | Profile)
Timeline: 2 days
Owner: UX Designer + Frontend Developer
Validation: Quick 15-min test with 3 users (remote)
```

**P2: Photo Hesitation (Medium)**
```yaml
Problem: 3/6 users hesitant to take photo (appearance concerns)
Impact: Delayed check-in, accuracy risk
Solution: Allow 3 retakes, add educational tooltip
  - "Photo verifies location, not appearance"
  - 3 retake attempts allowed
Timeline: 3 days
Owner: Frontend Developer
Validation: Monitor retake usage in pilot (analytics)
```

---

### Retest Plan:

```yaml
Who: 3 users (2 staff + 1 manager)
  - Include 1 user with old phone (battery anxiety validator)
  - Include 1 user who struggled with navigation (P1 validator)

What: Test updated prototype with fixes
  - Primary: Validate battery fallback works
  - Secondary: Validate navigation improvement
  - Tertiary: Monitor photo retake behavior

When: 1 week after fixes implemented

Success Criteria:
  ✅ 3/3 users understand battery fallback
  ✅ 3/3 users find hours history <10 seconds
  ✅ 0 users express battery anxiety (blocker eliminated)
  ✅ 3/3 would use daily (maintain adoption intent)
```

---

## 📚 ARTIFACTS & DELIVERABLES

### Documents Created:

- [ ] **Feedback Analysis Report** (this document)
- [ ] **Quantitative Results Dashboard** (Excel/Sheets with metrics)
- [ ] **Qualitative Insights Deck** (slides with quotes and themes)
- [ ] **Iteration Plan** (Jira tickets or task list)
- [ ] **Retest Script** (focused on fixes validation)

### Stakeholder Communication:

**Who Needs What**:

```yaml
Product Team:
  - Full feedback analysis report
  - Iteration plan with timelines
  - Retest plan

Engineering:
  - P0/P1 issues with technical details
  - Wireframes for navigation changes

Design:
  - Usability issues with screenshots
  - Recommended UX improvements

Leadership (CPO/CTO):
  - Executive Summary (1 page):
      * Top 3 positive findings
      * Top 3 issues to fix
      * Decision (ship/iterate/pivot)
      * Timeline and budget

Marketing/Sales:
  - User quotes (for testimonials if positive)
  - Validated value props (transparency, trust)
```

---

## ✅ ANALYSIS CHECKLIST

### Quality Checks:

- [ ] **All sessions analyzed**: Reviewed notes from all 6 sessions
- [ ] **Patterns identified**: Found themes mentioned by 3+ users
- [ ] **Quantified results**: Task completion, time, ratings calculated
- [ ] **Assumptions validated**: Checked each assumption against evidence
- [ ] **Prioritized issues**: P0/P1/P2/P3 with rationale
- [ ] **Decision made**: Ship/Iterate/Pivot chosen with clear rationale
- [ ] **Iteration plan created**: Who, what, when for fixes
- [ ] **Stakeholders informed**: Reports sent to relevant teams

---

## 🤖 AI ASSISTANCE TIPS

**Use Claude/ChatGPT to**:
- Synthesize patterns from raw session notes
- Calculate metrics (completion rate, NPS, etc.)
- Generate executive summary from full report
- Suggest fixes for identified usability issues

**Prompt Example**:
```
I conducted 6 user tests. Here are raw notes from all sessions:

[Paste session notes]

Please help me:
1. Identify top 5 patterns (issues mentioned by 3+ users)
2. Calculate task completion rates, average times
3. Extract 10 most impactful user quotes
4. Categorize issues by severity (Critical/High/Medium/Low)
5. Recommend: Should we ship, iterate, or pivot? Why?
```

**Warning**: AI can synthesize, but cannot replace human judgment on prioritization and user empathy.

---

## 💡 PRO TIPS

### Tip 1: Triangulate Evidence
> "Don't trust one data source. Confirm findings with quotes + metrics + observations."

### Tip 2: Count Mentions, Not Volume
> "If 1 user mentions issue 10 times, that's 1 vote. If 5 users mention once each, that's 5 votes (more significant)."

### Tip 3: Fix Fast, Test Again
> "After 3 users, if critical pattern emerges, FIX IT before testing remaining users. Iterate mid-sprint."

### Tip 4: P0 is Sacred
> "Never ship with P0 blocker. No matter how positive other findings are, one showstopper kills adoption."

### Tip 5: Celebrate Wins
> "Share positive quotes with team. User validation fuels motivation for iteration work."

---

**Template**: Feedback-Analysis-Template
**Part of**: SDLC 4.9 Design Thinking Framework
**Phase**: TEST (Stage 03 - BUILD)
**Version**: 1.0
**Last Updated**: November 13, 2025
**License**: MTS Internal Use
