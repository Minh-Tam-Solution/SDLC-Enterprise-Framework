# 🗺️ User Journey Map Template

**Purpose**: Visualize user's end-to-end experience, identify pain points and opportunities
**When to Use**: EMPATHIZE phase (SDLC Stage 00 - WHY?)
**Time Required**: 1-2 hours per journey
**Participants**: Product team, designers, researchers, stakeholders

---

## 📋 How to Use This Template

1. **Complete Empathy Map first** - understand user's context
2. **Choose specific scenario** - don't map everything, focus on ONE journey
3. **Use real data** - base on actual user observations, not assumptions
4. **Identify emotional journey** - not just functional steps
5. **Spot opportunities** - where can we make biggest impact?

---

## 🎯 JOURNEY DEFINITION

### Scenario Details
```yaml
Journey Name: [Descriptive name, e.g., "Restaurant Manager Daily Attendance Tracking"]
User Persona: [Reference to Empathy Map, e.g., "Lan - Restaurant Manager"]
Timeframe: [How long does this journey take? e.g., "Daily 7am-5pm"]
Frequency: [How often? e.g., "Every workday"]
Goal: [What is user trying to accomplish?]
Success Criteria: [How do they know they succeeded?]
```

**Example (NQH-Bot)**:
```yaml
Journey Name: Restaurant Manager Daily Attendance Tracking
User Persona: Lan - Restaurant Manager (3 locations, 45 staff)
Timeframe: Daily 7:00am - 5:00pm
Frequency: Every workday (Mon-Sun)
Goal: Accurately track staff attendance and submit payroll data
Success Criteria: Payroll data submitted by 5pm with zero errors
```

---

## 📊 JOURNEY STAGES

Divide journey into 3-7 major stages. For each stage, map:
- **Actions** (What do they do?)
- **Thoughts** (What are they thinking?)
- **Feelings** (How do they feel? Rate 1-10)
- **Pain Points** (What frustrates them?)
- **Opportunities** (How could we help?)

---

### 📍 STAGE 1: [Stage Name]

**Time**: [Start time - End time]
**Duration**: [How long does this stage take?]
**Location**: [Where does this happen?]

#### Actions (What They Do):
```
Step-by-step actions:
1. [Action 1]
2. [Action 2]
3. [Action 3]

Tools/Systems Used:
- [Tool 1]
- [Tool 2]

People Involved:
- [Role 1]
- [Role 2]
```

#### Thoughts (Internal Monologue):
```
"[What are they thinking during this stage?]"
"[What questions do they have?]"
"[What are they worried about?]"
```

#### Feelings (Emotional State):
```
Emotion: [Happy/Frustrated/Anxious/Neutral/etc.]
Intensity: [1-10, where 1=terrible, 10=excellent]
Why: [What causes this feeling?]
```

#### Pain Points:
```
1. [Pain point 1 - specific problem]
   Impact: [How does this hurt them?]
   Frequency: [How often does this occur?]

2. [Pain point 2]
   Impact: [How does this hurt them?]
   Frequency: [How often does this occur?]
```

#### Opportunities:
```
💡 [How could we eliminate this pain point?]
💡 [What would delight them at this stage?]
```

---

**Example (NQH-Bot - Stage 1)**:

### 📍 STAGE 1: Morning Preparation

**Time**: 7:00am - 7:30am
**Duration**: 30 minutes
**Location**: Office desk

#### Actions (What They Do):
```
Step-by-step actions:
1. Arrive at office early (before staff)
2. Print blank attendance forms (3 locations × 3 shifts = 9 forms)
3. Organize forms by location and shift
4. Prepare pen, calculator, previous day's forms for reference

Tools/Systems Used:
- Excel template (outdated design)
- Printer (often jams)
- Physical file folders

People Involved:
- Manager (alone at this stage)
```

#### Thoughts (Internal Monologue):
```
"Hope the printer doesn't jam again"
"Did I print enough forms for the new hires?"
"Why am I still doing this manually in 2025?"
```

#### Feelings (Emotional State):
```
Emotion: Resigned Frustration
Intensity: 4/10 (starting day already frustrated)
Why: Knows this is inefficient but has no alternative
```

#### Pain Points:
```
1. Printer Unreliability
   Impact: 10-15 min wasted when printer jams, stress before shift starts
   Frequency: 2-3 times per week

2. Manual Form Design
   Impact: Forms unclear, staff make mistakes filling them out
   Frequency: Daily (3-5 staff errors per day)
```

#### Opportunities:
```
💡 Eliminate paper forms entirely - digital check-in via mobile
💡 Auto-generate forms if paper is necessary (pre-filled with staff roster)
```

---

### 📍 STAGE 2: [Stage Name]

[Repeat same structure as Stage 1]

**Example (NQH-Bot - Stage 2)**:

### 📍 STAGE 2: Staff Check-In Collection

**Time**: 7:30am - 9:00am
**Duration**: 90 minutes (across 3 locations)
**Location**: All 3 restaurant locations

#### Actions (What They Do):
```
Step-by-step actions:
1. Drive to Location A (15 min)
2. Collect attendance forms from shift supervisor
3. Quickly scan for obvious errors
4. Drive to Location B (10 min)
5. Repeat collection process
6. Drive to Location C (10 min)
7. Repeat collection process
8. Return to office (15 min)

Tools/Systems Used:
- Car (travel between locations)
- WhatsApp (communicate with supervisors)
- Physical forms

People Involved:
- Shift supervisors (3 people)
- Staff (45 people total)
```

#### Thoughts (Internal Monologue):
```
"Location B supervisor is late again with the forms"
"These handwritten times are illegible"
"I see 3 errors already - going to be a long day"
```

#### Feelings (Emotional State):
```
Emotion: Anxious & Rushed
Intensity: 3/10 (stress building)
Why: Time pressure, visible errors, dependent on others' reliability
```

#### Pain Points:
```
1. Travel Time Waste
   Impact: 50 minutes daily just driving to collect paper
   Frequency: Daily

2. Handwriting Illegibility
   Impact: Cannot read times, must call staff to verify (adds 15-20 min)
   Frequency: 3-5 forms per day

3. Supervisor Reliability
   Impact: Some supervisors forget forms or submit late
   Frequency: 2-3 times per week
```

#### Opportunities:
```
💡 Real-time digital submission - no travel needed
💡 Mobile app with GPS verification - staff check in from location
💡 Automatic supervisor reminders if not submitted by 8:30am
```

---

### 📍 STAGE 3: Data Entry & Reconciliation

**Time**: 9:30am - 10:15am
**Duration**: 45 minutes
**Location**: Office desk

#### Actions (What They Do):
```
Step-by-step actions:
1. Open Excel master attendance file
2. Manually type data from 9 paper forms
3. Calculate total hours per employee
4. Cross-check against previous day for anomalies
5. Flag discrepancies for follow-up

Tools/Systems Used:
- Excel (with manual formulas)
- Calculator (backup verification)
- Previous day's attendance data

People Involved:
- Manager (alone, manual data entry)
```

#### Thoughts (Internal Monologue):
```
"This is mind-numbing work"
"Did I type 7:30 or 7:00 for employee #23?"
"One typo and payroll will be wrong again"
```

#### Feelings (Emotional State):
```
Emotion: Bored + Anxious (fear of errors)
Intensity: 3/10
Why: Repetitive work with high stakes (payroll accuracy)
```

#### Pain Points:
```
1. Manual Data Entry Errors
   Impact: 5-10% error rate, causes payroll disputes
   Frequency: Daily (average 2-3 errors per day)

2. Time Consumption
   Impact: 45 minutes daily on administrative work (not strategic)
   Frequency: Daily

3. No Real-Time Visibility
   Impact: Cannot see attendance data until 10:15am (3+ hours after shift starts)
   Frequency: Daily
```

#### Opportunities:
```
💡 Automatic data capture - zero manual typing
💡 Real-time dashboard - see attendance as it happens
💡 AI-powered anomaly detection - flag issues automatically
```

---

### 📍 STAGE 4: Discrepancy Resolution

**Time**: 10:15am - 11:00am
**Duration**: 45 minutes (if discrepancies exist)
**Location**: Office desk + security footage review room

#### Actions (What They Do):
```
Step-by-step actions:
1. Identify 3-5 discrepancies from reconciliation
2. Review security camera footage (15-20 min per discrepancy)
3. Call staff to verify times (5-10 min per call)
4. Update Excel with corrected data
5. Document notes about discrepancy

Tools/Systems Used:
- Security camera system (slow playback)
- Phone (call staff)
- Excel (update data)
- Notebook (document issues)

People Involved:
- Manager
- Staff members (phone calls)
- Security team (access footage)
```

#### Thoughts (Internal Monologue):
```
"This employee clocked in at 7:45, not 7:30 like they wrote"
"Why can't people just write the correct time?"
"I'm wasting an hour on detective work"
```

#### Feelings (Emotional State):
```
Emotion: Frustrated + Resentful
Intensity: 2/10 (lowest point in journey)
Why: Feels like policing adults, not managing a business
```

#### Pain Points:
```
1. Manual Verification Required
   Impact: 45 minutes wasted reviewing footage (should be strategic work time)
   Frequency: 3-4 days per week

2. Trust Erosion
   Impact: Damages relationship with staff (feels adversarial)
   Frequency: Ongoing

3. No Audit Trail
   Impact: He-said-she-said disputes, no definitive proof
   Frequency: 2-3 disputes per week
```

#### Opportunities:
```
💡 GPS + Biometric verification - automatic proof of check-in
💡 Photo capture at check-in - visual confirmation
💡 Blockchain audit trail - immutable record (no disputes)
```

---

### 📍 STAGE 5: Payroll Data Submission

**Time**: 4:30pm - 5:00pm
**Duration**: 30 minutes
**Location**: Office desk

#### Actions (What They Do):
```
Step-by-step actions:
1. Review final Excel file for errors
2. Calculate overtime hours (manual formula check)
3. Export data to CSV for payroll system
4. Email CSV to accounting team
5. Double-check sent email (anxiety about errors)

Tools/Systems Used:
- Excel (final review)
- Email (submission)
- Payroll system (accounting team uploads)

People Involved:
- Manager
- Accounting team (receives data)
```

#### Thoughts (Internal Monologue):
```
"Did I catch all the errors?"
"Hope accounting doesn't find mistakes again"
"Relief that this day is done"
```

#### Feelings (Emotional State):
```
Emotion: Anxious Relief (task complete but uncertain about quality)
Intensity: 5/10 (back to neutral, but not confident)
Why: Job done but lacks confidence in data accuracy
```

#### Pain Points:
```
1. No Confidence in Data Quality
   Impact: Constant anxiety about payroll errors (affects sleep)
   Frequency: Daily

2. Manual Export Process
   Impact: 10-15 min to prepare CSV correctly
   Frequency: Daily

3. Delayed Feedback
   Impact: Won't know if errors exist until accounting team reviews (next day)
   Frequency: Daily
```

#### Opportunities:
```
💡 Real-time validation - catch errors before submission
💡 Automatic payroll integration - zero manual export
💡 Confidence score - AI predicts data quality before submission
```

---

## 📈 EMOTIONAL JOURNEY GRAPH

**Plot user's emotional state across all stages (1-10 scale)**

```
10 |
 9 |
 8 |
 7 |
 6 |
 5 |                                      ●  (Stage 5: Relief)
 4 | ●                                       (Stage 1: Resigned)
 3 |     ●───────●                           (Stage 2-3: Anxious)
 2 |                 ●                       (Stage 4: Frustrated)
 1 |_____|_____|_____|_____|_____|
     S1    S2    S3    S4    S5

Key:
● = Emotional intensity at each stage
Baseline (5/10) = Neutral
Above 5 = Positive emotions
Below 5 = Negative emotions
```

**Example (NQH-Bot - Lan's Journey)**:
```
10 |
 9 |
 8 |
 7 |
 6 |
 5 |                                      ●  (5pm: Task complete)
 4 | ●                                       (7am: Starting frustrated)
 3 |     ●───────●                           (9am-10:15am: Building stress)
 2 |                 ●                       (10:15am: Lowest point)
 1 |_____|_____|_____|_____|_____|
     7am   9am  10am  11am  5pm

Average Emotional State: 3.4/10 (NEGATIVE)
Peak Frustration: Stage 4 (Discrepancy Resolution) - 2/10
Never reaches positive territory (6+/10)
```

**Insight**: User never experiences positive emotions during this journey. Opportunity for massive impact.

---

## 🎯 SYNTHESIS: KEY INSIGHTS

### Top 3 Pain Points (Ranked by Impact):

```
1. [Pain Point Name]
   Stages Affected: [List stages]
   Impact: [Quantify time/money/emotion]
   Quote: "[Direct user quote]"
   Opportunity: [How we could solve this]

2. [Pain Point Name]
   Stages Affected: [List stages]
   Impact: [Quantify time/money/emotion]
   Quote: "[Direct user quote]"
   Opportunity: [How we could solve this]

3. [Pain Point Name]
   Stages Affected: [List stages]
   Impact: [Quantify time/money/emotion]
   Quote: "[Direct user quote]"
   Opportunity: [How we could solve this]
```

**Example (NQH-Bot - Lan's Journey)**:
```
1. Loss of Trust in Data Quality
   Stages Affected: 3, 4, 5 (entire back half of journey)
   Impact: ₫15B revenue at risk, cannot make strategic decisions
   Quote: "I don't trust the data anymore. How can I make decisions when I don't believe the numbers?"
   Opportunity: GPS + biometric verification creates immutable trust

2. Time Waste (2 hours daily on manual work)
   Stages Affected: 1, 2, 3, 4 (all stages)
   Impact: 60 hours/month wasted (₫15M opportunity cost)
   Quote: "Manual attendance tracking takes 2 hours daily. That's 60 hours a month I could spend on strategy."
   Opportunity: Real-time automated data collection eliminates 95% of manual work

3. Adversarial Relationship with Staff
   Stages Affected: 4 (discrepancy resolution)
   Impact: Morale damage, retention risk, manager burnout
   Quote: "I feel like I'm policing adults instead of managing a business."
   Opportunity: Transparent system removes need for manager to be "detective"
```

### Moments That Matter (Biggest Opportunity Areas):

```
🔴 CRITICAL PAIN MOMENT:
Stage: [Stage number and name]
What Happens: [Describe the moment]
Why It Matters: [Impact on user]
Opportunity: [How we could transform this moment]

🟡 HIGH-FRICTION MOMENT:
Stage: [Stage number and name]
What Happens: [Describe the moment]
Why It Matters: [Impact on user]
Opportunity: [How we could reduce friction]

🟢 DELIGHT OPPORTUNITY:
Stage: [Stage number and name]
What Could Happen: [Imagine positive moment]
Why It Matters: [Impact on user]
Opportunity: [How we could create this delight]
```

**Example (NQH-Bot - Lan's Journey)**:
```
🔴 CRITICAL PAIN MOMENT:
Stage: 4 - Discrepancy Resolution
What Happens: Manager must review security footage for 45 minutes to verify staff check-in times
Why It Matters: Damages trust, wastes time, feels adversarial
Opportunity: GPS + timestamp + photo = automatic verification, zero manual review needed

🟡 HIGH-FRICTION MOMENT:
Stage: 3 - Manual Data Entry
What Happens: 45 minutes typing data from 9 paper forms into Excel
Why It Matters: Error-prone (5-10% error rate), mind-numbing work
Opportunity: Digital check-in = zero data entry, instant payroll integration

🟢 DELIGHT OPPORTUNITY:
Stage: 5 - Payroll Submission
What Could Happen: Instead of anxious submission, manager sees "100% Data Quality Score - Ready to Submit"
Why It Matters: Transforms anxiety into confidence, sleep better at night
Opportunity: AI validation engine provides real-time confidence scoring
```

---

## 💡 DESIGN PRINCIPLES (From Journey Insights)

Based on this journey map, our design should prioritize:

```
1. [Design Principle 1 - derived from pain points]
   Why: [Rationale from journey insights]

2. [Design Principle 2]
   Why: [Rationale from journey insights]

3. [Design Principle 3]
   Why: [Rationale from journey insights]
```

**Example (NQH-Bot)**:
```
1. TRUST FIRST (Not features first)
   Why: User's biggest pain is "I don't trust the data" - trust must be built into every interaction

2. ZERO MANUAL WORK (Automation is core, not nice-to-have)
   Why: 2 hours daily wasted - anything requiring manual entry will fail adoption

3. STAFF-FRIENDLY (Not just manager-focused)
   Why: Manager's pain stems from staff not using system correctly - must design for staff happiness
```

---

## ✅ VALIDATION CHECKLIST

Before moving to DEFINE phase:

- [ ] **Based on real observation**: Journey stages match actual user behavior (not assumed)
- [ ] **Emotional depth**: Captured emotional journey, not just functional steps
- [ ] **Quantified impact**: Time/money/emotion quantified for top pain points
- [ ] **Moments that matter identified**: Found 1-3 critical moments where intervention creates 10x impact
- [ ] **Design principles extracted**: Derived 3-5 principles to guide solution design

**Red Flags** (Redo journey mapping if true):
- ❌ Journey is generic (could apply to any user/product)
- ❌ No emotional journey captured (only functional steps)
- ❌ No direct quotes from users
- ❌ Team members disagree on which stages matter most

---

## 📚 NEXT STEPS

### After completing this Journey Map:

1. **Write Problem Statement** → [Problem-Statement-Template.md](Problem-Statement-Template.md)
   - Frame the RIGHT problem based on journey insights
   - Focus on highest-impact pain points

2. **Create POV Statement** → [POV-Statement-Template.md](POV-Statement-Template.md)
   - Synthesize user needs into actionable point of view

3. **Generate HMW Questions** → [HMW-Questions-Worksheet.md](HMW-Questions-Worksheet.md)
   - Transform pain points into opportunities

---

## 🤖 AI ASSISTANCE TIPS

**Use Claude/ChatGPT to**:
- Synthesize patterns across multiple user journeys
- Calculate time/cost impact of pain points
- Suggest opportunities based on pain points
- Generate HMW questions from journey insights

**Prompt Example**:
```
I mapped a user journey with 5 stages. Here are the key pain points:

[Paste pain points from journey map]

Please help me:
1. Rank pain points by impact (time × frequency × emotional intensity)
2. Identify which stage has biggest improvement opportunity
3. Generate 10 "How Might We" questions based on top 3 pain points
4. Suggest design principles derived from this journey
```

**Warning**: AI cannot observe real users. Use AI to analyze journey data, not to create fake journeys.

---

**Template**: User-Journey-Map-Template
**Part of**: SDLC 4.9 Design Thinking Framework
**Phase**: EMPATHIZE (Stage 00 - WHY?)
**Version**: 1.0
**Last Updated**: November 13, 2025
**License**: MTS Internal Use
