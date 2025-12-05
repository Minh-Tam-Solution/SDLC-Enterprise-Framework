# 🎯 Problem Statement Template

**Purpose**: Frame the RIGHT problem to solve (not symptoms, not solutions)
**When to Use**: DEFINE phase (SDLC Stage 00-01 transition - WHY? → WHAT?)
**Time Required**: 30-60 minutes
**Participants**: Product team, key stakeholders

---

## 📋 How to Use This Template

1. **Complete EMPATHIZE first** - Empathy Map + Journey Map required
2. **Focus on user needs, not technology** - Describe problem, not solution
3. **Be specific and measurable** - Vague problems lead to vague solutions
4. **Get team alignment** - Everyone must agree this is THE problem to solve
5. **Validate with users** - Read problem statement to users, they should say "YES! That's my problem!"

---

## ✅ PROBLEM STATEMENT FORMULA

### **The [user] has a problem: [describe the problem]**
### **This matters because [impact/consequence]**
### **Currently, they [what they do now / status quo]**
### **But this approach [why current approach fails]**

---

## 📝 PROBLEM STATEMENT BUILDER

### 1. WHO is experiencing this problem?

```yaml
User Persona: [Name and role from Empathy Map]
Context: [Where/when does problem occur?]
Scope: [How many users affected? Scale of problem?]
```

**Example (NQH-Bot)**:
```yaml
User Persona: Lan - Restaurant Manager (3 locations, 45 staff)
Context: Daily operations at multi-location F&B businesses
Scope: 10 restaurant managers interviewed, all experience same issue
```

**Anti-Pattern**: ❌ "Users need attendance tracking"
**Why Wrong**: Too generic, not specific about WHO

**Good Example**: ✅ "Multi-location restaurant managers with 20-50 staff members"

---

### 2. WHAT is the core problem? (Not symptom, not solution)

```yaml
Problem (One Sentence):
[Describe the problem in user's own words]

Evidence:
- [Quote 1 from user interviews]
- [Quote 2 from user interviews]
- [Data point showing problem exists]

NOT a problem:
- [Common confusion #1 - this is actually a symptom]
- [Common confusion #2 - this is actually a solution]
```

**Example (NQH-Bot)**:
```yaml
Problem (One Sentence):
Multi-location restaurant managers cannot trust their attendance data, preventing strategic decision-making.

Evidence:
- "I don't trust the data anymore" (7/10 managers)
- "Manual tracking causes 5-10% error rate" (measured)
- "I spend 2 hours daily on attendance, not strategy" (10/10 managers)

NOT a problem:
- "We need an attendance app" ← This is a SOLUTION, not the problem
- "Staff submit wrong hours" ← This is a SYMPTOM, root problem is trust erosion
```

**Anti-Pattern**: ❌ "We need to build a mobile app for attendance"
**Why Wrong**: This is jumping to solution. Problem is trust, not lack of mobile app.

**Good Example**: ✅ "Managers cannot trust attendance data due to manual processes creating 5-10% error rate"

---

### 3. WHY does this problem matter? (Impact & Consequences)

```yaml
Business Impact:
- [Quantify time wasted]
- [Quantify money lost]
- [Quantify opportunity cost]

Emotional Impact:
- [How does this affect user's well-being?]
- [What does this prevent them from achieving?]

Strategic Impact:
- [What bigger goals are blocked by this problem?]
- [What could user do if problem was solved?]
```

**Example (NQH-Bot)**:
```yaml
Business Impact:
- 60 hours/month wasted on manual tracking (₫15M opportunity cost)
- ₫15B revenue at risk due to operational inefficiency
- 5-10% payroll errors causing staff disputes

Emotional Impact:
- Constant anxiety about data accuracy (affects sleep)
- Adversarial relationship with staff (trust erosion)
- Burnout from 2 hours daily on administrative work

Strategic Impact:
- Cannot make data-driven decisions (no trust in data)
- Cannot scale to more locations (current process doesn't scale)
- Manager relegated to admin work instead of strategy
```

**Anti-Pattern**: ❌ "This is annoying for users"
**Why Wrong**: Not quantified, not compelling for stakeholders

**Good Example**: ✅ "60 hours/month wasted + ₫15B revenue at risk + manager burnout"

---

### 4. CURRENTLY, how do users try to solve this? (Status Quo)

```yaml
Current Approach:
[Describe step-by-step what users do now]

Tools Used:
- [Tool 1]
- [Tool 2]

Workarounds:
- [Hack 1 users created]
- [Hack 2 users created]
```

**Example (NQH-Bot)**:
```yaml
Current Approach:
1. Print paper attendance forms (7:00am)
2. Travel to 3 locations to collect forms (7:30am-9:00am)
3. Manually enter data into Excel (9:30am-10:15am)
4. Review security footage for discrepancies (10:15am-11:00am)
5. Submit to payroll with anxiety (5:00pm)

Tools Used:
- Paper forms
- Excel spreadsheets
- Security camera system
- Calculator

Workarounds:
- Call staff to verify times when handwriting illegible
- Review security footage to prove check-in times
- Double-check payroll data multiple times before submission
```

**Anti-Pattern**: ❌ "Users don't have a solution"
**Why Wrong**: Users ALWAYS have a solution (even if it's bad). Understanding status quo is critical.

**Good Example**: ✅ "Manual paper-based process taking 2 hours daily with 5-10% error rate"

---

### 5. BUT, why does current approach fail?

```yaml
Failure Mode 1: [Why current approach doesn't work]
Evidence: [Quote or data]

Failure Mode 2: [Another reason it fails]
Evidence: [Quote or data]

Failure Mode 3: [Another reason it fails]
Evidence: [Quote or data]

Root Cause: [Underlying reason ALL failure modes exist]
```

**Example (NQH-Bot)**:
```yaml
Failure Mode 1: Manual data entry creates 5-10% error rate
Evidence: "I make typos when entering 45 staff records daily" (8/10 managers)

Failure Mode 2: Paper-based system has no audit trail
Evidence: "He-said-she-said disputes, no definitive proof" (7/10 managers)

Failure Mode 3: 2-hour delay means no real-time visibility
Evidence: "Cannot see attendance until 10:15am, shift started at 7am" (10/10 managers)

Root Cause: Human-in-the-loop for every data point (not automated at source)
```

**Anti-Pattern**: ❌ "Current solution is old"
**Why Wrong**: "Old" is not a failure mode. Must identify specific ways it fails.

**Good Example**: ✅ "Manual process creates errors + no audit trail + delayed visibility"

---

## 🎯 FINAL PROBLEM STATEMENT

### Synthesize into Compelling Narrative:

```
[User persona] has a problem: [core problem in one sentence].

This matters because [business + emotional + strategic impact].

Currently, they [describe status quo approach].

But this approach [failure modes and why it doesn't work].

As a result, [ultimate negative consequence - what's at stake?].
```

---

**Example (NQH-Bot - Final Problem Statement)**:

```
Multi-location restaurant managers (20-50 staff) have a problem:
they cannot trust their attendance data due to manual tracking processes
creating 5-10% error rates.

This matters because 60 hours/month are wasted on administrative work
instead of strategy, ₫15B in revenue is at risk due to operational
inefficiency, and managers experience constant anxiety about payroll accuracy.

Currently, they use paper-based attendance forms, manually enter data
into Excel spreadsheets, and review security camera footage to resolve
discrepancies - a process taking 2 hours daily.

But this approach creates errors through manual data entry, provides no
audit trail (leading to he-said-she-said disputes), and results in 2-hour
delays before attendance data is available.

As a result, managers cannot make data-driven decisions, cannot scale
operations to additional locations, and suffer burnout from being relegated
to administrative work instead of strategic management.
```

**Validation Test**: Read this to a restaurant manager. They should say "YES! That's EXACTLY my problem!"

---

## ✅ PROBLEM STATEMENT QUALITY CHECKLIST

### Must Have (Non-Negotiable):

- [ ] **User-centric**: Describes problem from user's perspective (not company's)
- [ ] **Evidence-based**: Backed by quotes and data from user interviews
- [ ] **Specific**: Concrete details (not vague generalities)
- [ ] **Measurable**: Quantified impact (time/money/emotion)
- [ ] **No solutions embedded**: Describes problem, NOT how to solve it

### Red Flags (Rewrite if ANY are true):

- ❌ **Solution in disguise**: "We need to build X" - this is a solution, not a problem
- ❌ **Symptom, not root**: "Users submit wrong data" - WHY do they submit wrong data?
- ❌ **Technology-focused**: "We need AI/blockchain/mobile" - focus on user need first
- ❌ **Vague impact**: "This is frustrating" - quantify the frustration
- ❌ **Team disagrees**: If team members have different interpretations, problem not clear

---

## 🎯 EXAMPLE PROBLEM STATEMENTS (Good vs Bad)

### ❌ BAD Example 1: Solution in Disguise
```
"Users need a mobile app for attendance tracking."
```
**Why Bad**: This is a SOLUTION (mobile app), not a PROBLEM. Maybe users don't need mobile - maybe they need trust, visibility, or automation.

### ✅ GOOD Example 1: User-Centric Problem
```
"Restaurant managers waste 60 hours/month on manual attendance tracking,
creating 5-10% error rates that damage trust and prevent data-driven decisions."
```
**Why Good**: Describes the actual problem (time waste + errors + trust damage) without prescribing solution.

---

### ❌ BAD Example 2: Symptom, Not Root Cause
```
"Staff submit inaccurate attendance hours."
```
**Why Bad**: This is a SYMPTOM. Root problem is why they submit inaccurate hours (illegible handwriting? Confusing forms? Lack of real-time feedback?).

### ✅ GOOD Example 2: Root Cause Identified
```
"Manual paper-based attendance forms cause illegibility and confusion,
leading staff to submit inaccurate hours, which managers must verify via
45-minute security footage reviews."
```
**Why Good**: Traces symptom (inaccurate hours) to root cause (manual paper forms) and quantifies impact (45 min reviews).

---

### ❌ BAD Example 3: Vague and Unmeasurable
```
"Attendance tracking is difficult and frustrating for managers."
```
**Why Bad**: "Difficult" and "frustrating" are vague. How difficult? How frustrating? Can't measure success if problem not quantified.

### ✅ GOOD Example 3: Specific and Measurable
```
"Managers spend 2 hours daily (60 hours/month) on manual attendance tracking,
experiencing constant anxiety due to 5-10% error rates affecting payroll accuracy."
```
**Why Good**: Quantified time (2 hours daily), quantified errors (5-10%), specific emotion (anxiety about payroll).

---

## 🧪 VALIDATION: Test Your Problem Statement

### Test 1: The User Recognition Test
**Read problem statement to 3-5 users. They should:**
- ✅ Immediately say "YES! That's my problem!"
- ✅ Add more details (not contradict)
- ✅ Express emotion (frustration/relief that someone understands)

**If users say "That's not quite right" or "Sort of" → Rewrite**

---

### Test 2: The Team Alignment Test
**Ask each team member to explain the problem in their own words:**
- ✅ All team members describe same core problem
- ✅ All agree on priority (this is THE problem to solve)
- ✅ No one mentions solutions (only problem)

**If team members describe different problems → Rewrite**

---

### Test 3: The Solution-Neutral Test
**Can this problem be solved in 5+ different ways?**
- ✅ YES → Good problem statement (solution-neutral)
- ❌ NO → Rewrite (probably embedded a solution)

**Example (NQH-Bot)**:
Problem: "Managers cannot trust attendance data"
Possible Solutions:
1. Mobile app with GPS verification
2. Biometric check-in kiosks
3. Blockchain audit trail
4. AI-powered anomaly detection
5. Manager-approved digital forms

All 5 are valid → Problem statement is solution-neutral ✅

---

### Test 4: The "So What?" Test
**Ask "So what?" 3 times to ensure you found root problem:**

```
Problem: Staff submit wrong hours
  → So what?
Problem: Managers waste time verifying hours
  → So what?
Problem: Managers cannot trust data
  → So what?
Problem: Cannot make strategic decisions, ₫15B revenue at risk
  → THIS is the root problem ✅
```

**If you can still ask "So what?" and get a bigger problem → Keep digging**

---

## 📚 NEXT STEPS

### After completing Problem Statement:

1. **Create POV Statement** → [POV-Statement-Template.md](POV-Statement-Template.md)
   - Synthesize user + need + insight into actionable perspective

2. **Generate HMW Questions** → [HMW-Questions-Worksheet.md](HMW-Questions-Worksheet.md)
   - Transform problem into opportunity questions

3. **Validate with stakeholders**
   - Present problem statement to leadership
   - Get approval before moving to ideation

---

## 🤖 AI ASSISTANCE TIPS

**Use Claude/ChatGPT to**:
- Help identify root cause (vs symptoms)
- Synthesize patterns from multiple user interviews
- Quantify impact (time/money calculations)
- Rewrite vague statements into specific ones

**Prompt Example**:
```
I'm trying to write a problem statement. Here's what I have:

"Users find attendance tracking difficult."

This feels too vague. Here's my user research:
- [Paste empathy map insights]
- [Paste journey map pain points]

Please help me:
1. Identify the root problem (not symptom)
2. Quantify the impact (time/money/emotion)
3. Rewrite into specific, measurable problem statement
4. Test if problem is solution-neutral (can be solved 5+ ways)
```

**Warning**: AI can help refine, but cannot replace user empathy. Problem must come from real user insights.

---

## 💡 PRO TIPS

### Tip 1: Start with User Quotes
> "Copy-paste actual quotes from users, then synthesize into problem statement. This keeps you honest - can't make up problems if you're anchored to evidence."

### Tip 2: Avoid "Need" Language
> "Users need X" is solution-focused. Instead: "Users struggle to Y because Z" (problem-focused).

**Bad**: "Users need a mobile app"
**Good**: "Users cannot access data in real-time, causing 2-hour delays in decision-making"

### Tip 3: Quantify Everything
> "Vague problems get vague solutions. Quantify time, money, emotion - creates urgency and measurability."

**Bad**: "This is frustrating for users"
**Good**: "Users experience daily anxiety, affecting sleep quality (8/10 managers reported)"

### Tip 4: Problem Statement Drives Everything
> "This document is your North Star. Every feature, every design decision must trace back to solving THIS problem. If it doesn't solve the problem → cut it."

---

**Template**: Problem-Statement-Template
**Part of**: SDLC 4.9 Design Thinking Framework
**Phase**: DEFINE (Stage 00-01 transition - WHY? → WHAT?)
**Version**: 1.0
**Last Updated**: November 13, 2025
**License**: MTS Internal Use
