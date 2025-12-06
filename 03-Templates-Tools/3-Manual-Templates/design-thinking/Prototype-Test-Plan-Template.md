# 🛠️ Prototype & Test Plan Template

**Purpose**: Build minimum testable version to validate assumptions quickly
**When to Use**: PROTOTYPE → TEST phases (SDLC Stage 03 - BUILD)
**Time Required**: 1-4 weeks (depending on fidelity)
**Participants**: Designer, developer, product manager

---

## 📋 How to Use This Template

1. **Select concept from ideation** - Focus on ONE concept (not all ideas)
2. **Choose appropriate fidelity** - Paper → Digital → Code (start lowest)
3. **Define what to learn** - What assumptions are we testing?
4. **Build minimum to test** - Not production-ready, just learn-ready
5. **Test with 5-8 real users** - Iterate based on feedback

---

## 🎯 PROTOTYPE PLANNING

### Concept to Prototype:

```yaml
Concept Name: [From ideation session]
One-Sentence Description: [What is this concept?]
User Need It Addresses: [From POV statement]
Key Innovation: [What's new/different about this?]
```

**Example (NQH-Bot)**:
```yaml
Concept Name: TrustCheck - Auto-Verify Attendance
One-Sentence Description: Staff check in via smartphone with GPS + photo verification
User Need It Addresses: Managers need to trust attendance data without manual verification
Key Innovation: Automatic verification at source (GPS + photo + timestamp) eliminates 45-minute manager review
```

---

### Critical Assumptions to Test:

**List 3-5 assumptions that, if wrong, would invalidate the concept**

```yaml
Assumption 1: [What must be true for this to work?]
  Test: [How will we validate this assumption?]
  Success Criteria: [What result confirms assumption?]

Assumption 2: [What must be true for this to work?]
  Test: [How will we validate this assumption?]
  Success Criteria: [What result confirms assumption?]

Assumption 3: [What must be true for this to work?]
  Test: [How will we validate this assumption?]
  Success Criteria: [What result confirms assumption?]
```

**Example (NQH-Bot)**:
```yaml
Assumption 1: Staff have smartphones and will use them for check-in
  Test: Interview 10 staff - do they have smartphones? Will they use work app?
  Success Criteria: 8/10 staff have smartphones, 7/10 willing to use app

Assumption 2: GPS accuracy is sufficient to verify location (restaurant vs competitor)
  Test: Test GPS at 3 restaurant locations, measure accuracy within 50m
  Success Criteria: GPS accurate to within 50m in 9/10 tests

Assumption 3: Photo check-in feels trustworthy (not surveillance) to staff
  Test: Show prototype to 5 staff, ask "Does this feel like surveillance or transparency?"
  Success Criteria: 4/5 staff say "transparency" not "surveillance"

Assumption 4: Managers trust auto-verification more than manual process
  Test: Show side-by-side (current vs prototype) to 3 managers
  Success Criteria: 3/3 managers prefer automated verification

Assumption 5: One-tap check-in takes <10 seconds (not burdensome)
  Test: Time 10 staff using prototype, measure check-in duration
  Success Criteria: Average <10 seconds, 9/10 complete successfully
```

---

## 📐 FIDELITY DECISION

### Choose Prototype Fidelity Level:

**Fidelity** = How close to final product (functionality + visual polish)

| Fidelity | Time to Build | Cost | Best For | Example |
|----------|---------------|------|----------|---------|
| **Paper** | 1-4 hours | Free | Concept validation, early ideas | Hand-drawn UI on paper |
| **Digital Mockup** | 1-3 days | Low | Flow validation, visual design | Figma clickable prototype |
| **Code Prototype** | 1-2 weeks | Medium | Technical feasibility, real data | Working app (limited features) |
| **MVP** | 4-12 weeks | High | Market validation, early adopters | Shippable product (core features) |

**Decision Framework**:

```
Use PAPER if:
  - First time testing concept
  - Validating flow / information architecture
  - Need feedback in <1 week
  - Budget is $0

Use DIGITAL MOCKUP if:
  - Concept validated on paper
  - Need realistic visual design
  - Testing interaction patterns
  - Budget is <$1,000

Use CODE PROTOTYPE if:
  - Digital mockup validated
  - Technical feasibility questions exist
  - Need to test with real data
  - Budget is $1,000-$10,000

Use MVP if:
  - Code prototype validated
  - Ready for market testing
  - Need to test business model (pricing, retention)
  - Budget is $10,000+
```

**Our Prototype Fidelity**: [Paper / Digital / Code / MVP]

**Rationale**: [Why this fidelity level?]

---

## 🛠️ PROTOTYPE BUILD PLAN

### Paper Prototype (1-4 hours):

```yaml
Materials Needed:
  - Blank paper or index cards
  - Markers/pens
  - Scissors (for movable elements)
  - Optional: Templates (smartphone frame, browser window)

Build Process:
  1. Sketch key screens (one screen per card)
  2. Draw interactive elements (buttons, forms, menus)
  3. Create movable pieces (dropdowns, modals)
  4. Number cards in order of flow
  5. Practice "playing" the prototype (facilitator moves cards)

Time: 1-4 hours
```

**Example (NQH-Bot - Paper Prototype)**:
```
Card 1: Login Screen
  - App logo
  - "Check In" button
  - "View My Hours" button

Card 2: Check-In Screen
  - Live camera preview (draw rectangle)
  - "Location: Restaurant B ✅" (GPS status)
  - "Tap to Check In" button
  - Current time display

Card 3: Confirmation Screen
  - Checkmark icon
  - "Checked in at 7:32am"
  - Photo thumbnail
  - "View My Hours" button

Card 4: Hours Dashboard
  - Calendar view with check-ins
  - Daily total hours
  - Week total
  - "Export" button
```

---

### Digital Mockup (1-3 days):

```yaml
Tool: [Figma / Adobe XD / Sketch / Balsamiq]

Build Process:
  1. Create wireframes (low-fidelity screens)
  2. Add content (real text, not lorem ipsum)
  3. Create interaction prototypes (click to next screen)
  4. Add transitions (optional, helps realism)
  5. Share prototype link for testing

Deliverables:
  - Figma/XD file with 5-15 screens
  - Clickable prototype link
  - Design notes (context for developers)

Time: 1-3 days
```

**Example (NQH-Bot - Digital Mockup)**:
```
Figma Prototype Structure:
  Screen 1: Splash / Login
  Screen 2: Home Dashboard
  Screen 3: Check-In Flow
    - 3a: Camera preview
    - 3b: GPS verification
    - 3c: Confirmation
  Screen 4: Hours History
  Screen 5: Manager Dashboard (if testing manager view)

Interactions:
  - "Check In" button → Screen 3a (camera)
  - Camera capture → Screen 3b (GPS verification)
  - "Confirm" → Screen 3c (success)
  - "View Hours" → Screen 4 (history)

Design Notes:
  - Use Vietnamese language (primary language)
  - Large touch targets (minimum 44px, F&B workers may wear gloves)
  - High contrast (outdoor visibility, bright sunlight)
  - Simple navigation (staff are not tech-savvy)
```

---

### Code Prototype (1-2 weeks):

```yaml
Tech Stack: [React Native / Flutter / Django / FastAPI / etc.]

Scope (Minimum Features):
  - [Feature 1 - core to assumption test]
  - [Feature 2 - core to assumption test]
  - [Feature 3 - core to assumption test]
  - [Feature 4 - optional, nice to have]

NOT Building (Out of Scope):
  - Authentication (use hardcoded users for test)
  - Edge cases (happy path only)
  - Error handling (minimal)
  - Performance optimization
  - Production infrastructure

Build Process:
  Week 1:
    - Day 1-2: Set up environment, scaffold app
    - Day 3-4: Implement core feature 1 & 2
    - Day 5: Quick internal test, fix blockers

  Week 2:
    - Day 6-7: Implement feature 3
    - Day 8: Polish UX (not pixel-perfect, just usable)
    - Day 9: Test with 2-3 internal users
    - Day 10: Prepare for user testing (deploy to test devices)

Deliverables:
  - Working app (installable on test devices)
  - Test data (realistic, not production)
  - Short demo video (30 sec)
  - Known limitations document

Time: 1-2 weeks
```

**Example (NQH-Bot - Code Prototype)**:
```
Tech Stack:
  - React Native (cross-platform mobile)
  - Expo (rapid development)
  - Mock backend (JSON server or Firebase)

Scope (Minimum Features):
  1. GPS location capture on check-in ✅
  2. Camera photo capture with timestamp ✅
  3. Display check-in history (last 7 days) ✅
  4. Manager dashboard (view all check-ins today) ⚠️ (optional)

NOT Building:
  - User authentication (hardcoded 3 test users)
  - Push notifications
  - Offline mode
  - Data export
  - Production database (use Firebase for quick setup)
  - Edge cases (what if GPS unavailable? - skip for now)

Build Plan:
  Week 1:
    - Day 1: Expo init, navigation structure
    - Day 2: Camera integration, GPS permissions
    - Day 3: Check-in flow (camera → GPS → save)
    - Day 4: History screen (display past check-ins)
    - Day 5: Internal test (3 team members try on phones)

  Week 2:
    - Day 6-7: Manager dashboard (optional, if time allows)
    - Day 8: UI polish (buttons, spacing, Vietnamese labels)
    - Day 9: Load test data (20 fake check-ins for demo)
    - Day 10: Deploy to TestFlight/Firebase (3 staff test devices)

Deliverables:
  - App installable via link (TestFlight or Firebase App Distribution)
  - 30-second demo video (show check-in flow)
  - Known limitations doc:
      "This prototype does NOT include authentication, offline mode, or error handling.
       Happy path only. GPS accuracy not validated in all locations."
```

---

## 🧪 TEST PLAN

### Test Objectives:

```yaml
Primary Goal: [What are we trying to learn?]
Secondary Goals:
  - [Additional learning objective 1]
  - [Additional learning objective 2]

Success Metrics:
  - [Metric 1 - quantitative]
  - [Metric 2 - qualitative]
  - [Metric 3 - behavioral]
```

**Example (NQH-Bot)**:
```yaml
Primary Goal: Validate that GPS + photo verification feels trustworthy (not surveillance)

Secondary Goals:
  - Measure check-in duration (target <10 seconds)
  - Identify UX friction points in check-in flow
  - Test if staff understand verification transparency

Success Metrics:
  - 4/5 staff say check-in feels "transparent" not "surveillance" ✅
  - Average check-in time <10 seconds ✅
  - 5/5 staff complete check-in without assistance ✅
  - 4/5 managers say they trust auto-verification ✅
```

---

### Test Participants:

```yaml
Recruitment Criteria:
  - [Criterion 1, e.g., "Current restaurant staff"]
  - [Criterion 2, e.g., "Use smartphone daily"]
  - [Criterion 3, e.g., "Work at 3+ different locations"]

Number of Participants: 5-8 (for qualitative insights, 5 is sufficient per Jakob Nielsen)

Recruitment Plan:
  - Source: [Where will we find participants?]
  - Incentive: [What compensation? e.g., ₫200,000 gift card, 1-hour paid time]
  - Schedule: [When will tests occur?]
```

**Example (NQH-Bot)**:
```yaml
Recruitment Criteria:
  - Restaurant staff currently using paper attendance forms
  - Own a smartphone (Android or iOS)
  - Work at multi-location F&B business
  - Age 20-45 (representative of staff demographics)

Number of Participants: 6 (5 staff + 1 manager)

Recruitment Plan:
  - Source: NQ Holding' partner restaurants (existing relationship)
  - Incentive: ₫200,000 Grab gift card + 1 hour paid work time
  - Schedule: Week of Nov 18-22, 2025 (1 session per day)
```

---

### Test Sessions:

```yaml
Session Duration: 45-60 minutes
Location: [In-person at user's location / Remote video call / Lab]

Session Structure:
  1. Introduction (5 min) - Build rapport, explain purpose
  2. Context Questions (5 min) - Understand current process
  3. Prototype Demo (5 min) - Show how it works
  4. User Tasks (20 min) - User tries prototype with tasks
  5. Feedback Interview (10 min) - Open-ended questions
  6. Wrap-Up (5 min) - Thank participant, explain next steps
```

**Example (NQH-Bot Session)**:
```
Session Duration: 60 minutes
Location: In-person at participant's restaurant (test in real environment)

Session Structure:
  1. Introduction (5 min)
     - "Thank you for helping us test this new check-in app"
     - "We're testing the app, not you - there are no wrong answers"
     - "Please think aloud as you use the app"

  2. Context Questions (5 min)
     - "Walk me through how you currently check in for shifts"
     - "What's frustrating about the current process?"
     - "Do you trust that your hours are recorded accurately?"

  3. Prototype Demo (5 min)
     - Facilitator demonstrates one check-in
     - "This is how the app works: tap button, take photo, confirm"
     - Hand phone to participant

  4. User Tasks (25 min)
     TASK 1: Check in for your shift
       - Observe: Can they complete without help?
       - Time: How long does check-in take?
       - Ask: "What are you thinking right now?"

     TASK 2: View your hours history
       - Observe: Can they find history screen?
       - Ask: "Does this match what you expect?"

     TASK 3: Check in again (second attempt)
       - Observe: Is second attempt faster?
       - Measure: Time improvement

     TASK 4: Show manager dashboard (if built)
       - Ask manager: "Do you trust this data?"
       - Probe: "Why or why not?"

  5. Feedback Interview (15 min)
     - "How did check-in feel? Transparent or surveillance?"
     - "Would you use this daily? Why/why not?"
     - "What would make you NOT want to use this?"
     - "If you could change one thing, what would it be?"

  6. Wrap-Up (5 min)
     - "Thank you! Your feedback will help us improve"
     - Provide gift card
     - Ask: "Can we follow up in 2 weeks to show improvements?"
```

---

### Data Collection:

```yaml
Quantitative Data:
  - [Metric 1: e.g., Task completion rate]
  - [Metric 2: e.g., Time on task]
  - [Metric 3: e.g., Error rate]

Qualitative Data:
  - [Observation 1: e.g., User hesitations]
  - [Observation 2: e.g., Facial expressions]
  - [Quote collection: e.g., "This feels like..."]

Tools:
  - Video recording: [Yes/No, with consent]
  - Screen recording: [Yes/No]
  - Note-taking: [Who is the note-taker?]
  - Survey (post-test): [Optional, link]
```

**Example (NQH-Bot)**:
```yaml
Quantitative Data:
  - Task completion rate (can they check in without help?)
  - Time on task (check-in duration in seconds)
  - Error rate (failed attempts, retries)

Qualitative Data:
  - Emotional reactions (surprise, confusion, delight)
  - Verbal feedback ("This is easy!" vs "I don't understand")
  - Body language (hesitation, confidence)
  - Direct quotes about trust/surveillance perception

Tools:
  - Video recording: YES (with written consent)
  - Screen recording: YES (phone screen capture)
  - Note-taking: Product Manager (dedicated note-taker)
  - Survey: YES - post-test SUS (System Usability Scale)
```

---

## 📊 ANALYSIS & ITERATION

### Synthesis Template:

**After 5-8 test sessions, synthesize findings:**

```yaml
Key Findings:
  1. [Finding 1 - pattern across 3+ users]
     Evidence: [Quotes, metrics]
     Severity: [Critical / High / Medium / Low]

  2. [Finding 2]
     Evidence: [Quotes, metrics]
     Severity: [Critical / High / Medium / Low]

  3. [Finding 3]
     Evidence: [Quotes, metrics]
     Severity: [Critical / High / Medium / Low]

What Worked Well:
  - [Positive finding 1]
  - [Positive finding 2]

What Needs Improvement:
  - [Issue 1 - specific problem]
  - [Issue 2 - specific problem]

Unexpected Insights:
  - [Surprise 1 - something we didn't anticipate]
  - [Surprise 2]
```

---

### Iteration Decision:

**Based on findings, choose next step:**

```
✅ SHIP IT (if validated)
  - All critical assumptions confirmed
  - Task completion rate >80%
  - Users express strong positive sentiment
  - No critical usability issues
  → Next: Build MVP for market launch

🔄 ITERATE (if partially validated)
  - Some assumptions confirmed, others need refinement
  - Task completion rate 50-80%
  - Mixed user sentiment
  - Medium usability issues identified
  → Next: Fix issues, test again with 3-5 users

❌ PIVOT (if invalidated)
  - Critical assumptions proven false
  - Task completion rate <50%
  - Strong negative user sentiment
  - Fundamental concept issues
  → Next: Return to ideation, generate new concepts

⏸️ PAUSE (if unclear)
  - Results inconclusive
  - Need different user segment
  - External blockers (technical, business)
  → Next: Refine test plan, recruit different users
```

---

## ✅ PROTOTYPE & TEST CHECKLIST

### Before Building:

- [ ] **Concept selected** from ideation (team alignment)
- [ ] **Assumptions documented** (3-5 critical assumptions)
- [ ] **Fidelity chosen** (appropriate for stage)
- [ ] **Scope defined** (what's in, what's out)
- [ ] **Timeline set** (realistic for fidelity)

### Before Testing:

- [ ] **Prototype complete** (minimum features working)
- [ ] **Test plan written** (objectives, tasks, questions)
- [ ] **Participants recruited** (5-8 users confirmed)
- [ ] **Tools prepared** (recording, note-taking)
- [ ] **Test script practiced** (facilitator comfortable)

### After Testing:

- [ ] **Findings synthesized** (patterns identified)
- [ ] **Metrics analyzed** (quant + qual)
- [ ] **Iteration decision made** (ship/iterate/pivot)
- [ ] **Next steps defined** (timeline, owners)
- [ ] **Stakeholders informed** (share results)

---

## 🤖 AI ASSISTANCE TIPS

**Use Claude/ChatGPT to**:
- Generate test tasks based on user stories
- Synthesize findings from test session notes
- Suggest improvements based on user feedback
- Draft test scripts and interview questions

**Prompt Example**:
```
I conducted 6 user tests of our attendance app prototype. Here are the notes:

[Paste raw notes from 6 sessions]

Please help me:
1. Identify top 3 patterns (issues mentioned by 3+ users)
2. Extract 5 most impactful direct quotes
3. Categorize findings by severity (critical/high/medium/low)
4. Suggest 3-5 specific improvements to address critical issues
5. Recommend: Should we ship, iterate, or pivot?
```

**Warning**: AI can help synthesize, but cannot replace observing real users. Always test with humans.

---

## 💡 PRO TIPS

### Tip 1: Start with Lowest Fidelity
> "Don't code what you can mockup. Don't mockup what you can sketch. Start paper, increase fidelity only when validated."

### Tip 2: Test with Real Users in Real Context
> "Test attendance app at real restaurant during shift change. Context matters. Lab testing misses critical insights."

### Tip 3: Observe, Don't Lead
> "Don't say 'Click here'. Say 'How would you check in?' Let them struggle - that's where you learn."

### Tip 4: Iterate After Every 3-5 Users
> "Don't wait for all 8 tests. Fix critical issues after 3 users, test improved version with remaining 5."

### Tip 5: Build Minimum to Learn (Not Minimum to Ship)
> "Prototype goal is learning, not launching. Throw away 50% of prototype features after testing."

---

## 📚 NEXT STEPS

### After Prototype Testing:

1. **Synthesize Findings** → [Feedback-Analysis-Template.md](Feedback-Analysis-Template.md)
   - Analyze test results
   - Identify patterns

2. **Decide: Ship, Iterate, or Pivot**
   - Present findings to stakeholders
   - Make go/no-go decision

3. **If ITERATE**: Fix issues, test again
4. **If SHIP**: Build MVP for market launch
5. **If PIVOT**: Return to ideation phase

---

**Template**: Prototype-Test-Plan-Template
**Part of**: SDLC 5.0 Design Thinking Framework
**Phase**: PROTOTYPE → TEST (Stage 03 - BUILD)
**Version**: 1.0
**Last Updated**: November 13, 2025
**License**: MTS Internal Use
