# SDLC 5.0.0 Training Materials - Complete Learning Package

**Version**: 5.0.0
**Date**: December 5, 2025
**Audience**: All team members (developers, designers, product managers, QA)
**Duration**: 8 hours total (can be split across multiple sessions)
**Prerequisites**: Basic SDLC 4.9 knowledge (or 2-hour SDLC fundamentals course)

---

## 🆕 What's New in SDLC 5.0.0 (December 5, 2025)

**Governance & Compliance Standards**: SDLC 5.0.0 introduces comprehensive Governance & Compliance with 4-Tier Classification (LITE → ENTERPRISE), Quality Gates, Security Gates, Observability, and Team Collaboration Standards.

Key naming conventions:
- **Python**: `snake_case` (max 50 chars) - e.g., `user_service.py`
- **TypeScript**: `camelCase` (max 50 chars) - e.g., `arService.ts`
- **React**: `PascalCase` (max 50 chars) - e.g., `ARDashboard.tsx`

See Session 3 for details on code quality standards including file naming.

---

## 🎯 Training Program Overview

### Learning Objectives

By completing this training, participants will be able to:

1. ✅ **Explain** what Design Thinking is and why it matters (reduce 70% feature waste)
2. ✅ **Apply** all 5 Design Thinking phases to real projects (Empathize → Test)
3. ✅ **Use** 9 practical templates without assistance (15-30 min per template)
4. ✅ **Map** Design Thinking to SDLC 5.0.0 10-Stage Framework (WHY → GOVERN)
5. ✅ **Validate** assumptions with real users before building (5-8 user tests)
6. ✅ **Integrate** SDLC 5.0.0 into daily workflow (80%+ compliance within 2 weeks)
7. ✅ **Apply** code quality standards including file naming conventions
8. ✅ **Understand** 4-Tier Classification and select appropriate tier for projects

### Training Structure

```yaml
Session 1: SDLC 5.0.0 Overview & Design Thinking Fundamentals
  Duration: 2 hours
  Format: Lecture + Discussion
  Deliverable: Understanding quiz (80% pass rate)
  Topics: 10-Stage Lifecycle, 6 Pillars, Design Thinking foundation

Session 2: Design Thinking Hands-On Workshop
  Duration: 3 hours
  Format: Workshop + Practice
  Deliverable: Completed empathy map + problem statement

Session 3: Templates, Code Quality & Code Review Excellence
  Duration: 2 hours
  Format: Walkthrough + Examples
  Deliverable: Template usage + code quality confidence assessment
  Topics: Templates, code standards, file naming conventions, code review tiers

Session 4: Real Project Application
  Duration: 1 hour (ongoing)
  Format: Guided practice on actual project
  Deliverable: Pilot project with SDLC 4.9.1 applied

Total: 8 hours core + ongoing practice
```

---

## 📚 SESSION 1: SDLC 4.9.1 Overview & Design Thinking Fundamentals

**Duration**: 2 hours
**Format**: Lecture (60 min) + Discussion (30 min) + Quiz (30 min)
**Facilitator**: CPO or trained team lead

---

### Part 1: Why SDLC 4.9.1? (15 minutes)

**Slide 1: The Problem We're Solving**

```
Industry Reality (Standish Group, 2020):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ 70% of features rarely or never used
❌ 64% of features NOT essential (waste)
❌ 45% of features built are never used at all

Root Cause: Building solutions before understanding problems

Cost: $100M feature × 64% waste = $64M wasted
```

**Discussion Prompt**:
- "Can you think of a feature we built that users don't actually use?"
- "What would have prevented that waste?"

---

**Slide 2: SDLC Evolution (4.7 → 4.8 → 4.9 → 4.9.1)**

```
SDLC 4.7 (September 2025):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Focus: Build things RIGHT (5 Pillars, HOW)
  ✅ 10x-50x productivity with AI
  ✅ Zero Mock Policy
  ✅ 95% quality scores

SDLC 4.8 (November 7, 2025):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Focus: Build RIGHT things RIGHT (6 Pillars, 4 stages)
  ✅ + Design Thinking (Pillar 0)
  ✅ 4 stages: WHY, WHAT, HOW, BUILD
  ✅ 7,322% ROI proven

SDLC 4.9 (November 13, 2025):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Focus: Complete Lifecycle Excellence (6 Pillars, 10 stages)
  ✅ 10 stages: WHY → GOVERN
  ✅ 14,822% ROI proven (2x improvement)
  ✅ Perfect /docs alignment (00-09)

SDLC 4.9.1 (November 29, 2025):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Focus: Complete Lifecycle + Code Consistency
  ✅ Code File Naming Standards restored
  ✅ All 4.9 features maintained
```

---

**Slide 3: What is Design Thinking?**

```
Traditional Approach (Build-First):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Developer assumption → Build → Ship → Users don't use it → Waste

Design Thinking Approach (Understand-First):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Empathize (Understand users) →
Define (Frame right problem) →
Ideate (Generate solutions) →
Prototype (Build minimum testable) →
Test (Validate with users) →
Ship validated solution

Result: 3-10x higher adoption, sustainable product-market fit
```

**Key Message**: Design Thinking ensures we build features users actually need and will use.

---

### Part 2: Design Thinking 5 Phases (30 minutes)

**Slide 4: Phase 1 - EMPATHIZE 🧠**

```
Purpose: Deeply understand users' pain, context, needs

Activities:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ User interviews (5-10 per persona)
✅ Journey mapping (visualize end-to-end experience)
✅ Empathy mapping (what they see, hear, think, feel)
✅ Observational research (watch in real context)

Deliverables:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 User personas (evidence-based)
📋 Pain points ranked by severity
📋 Journey maps with emotional journey
📋 50+ direct user quotes (evidence)

Time: 3-5 days
Template: Empathy-Map-Canvas-Template.md
```

**Real Example (NQH-Bot)**:
```
Problem discovered: "I don't trust the data anymore"
  → NOT "tracking is slow" (assumed problem)
  → ROOT CAUSE: Trust erosion, not efficiency

Insight: Emotional problem (anxiety), not functional problem (speed)

Impact: Complete solution pivot
  → Instead of "faster tracking"
  → Built "trust restoration through verification"

Result: 90% trust restoration (solved root cause)
```

---

**Slide 5: Phase 2 - DEFINE 🎯**

```
Purpose: Frame the RIGHT problem to solve

Activities:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Problem statement (evidence-based, specific)
✅ POV statement (user + need + insight)
✅ HMW questions (transform to opportunities)
✅ Success metrics (measurable outcomes)

Deliverables:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Problem statement (validated with 3+ users)
📋 POV statement (functional + emotional)
📋 20-50 HMW questions
📋 Success criteria (quantified)

Time: 2-3 days
Templates: Problem-Statement, POV-Statement, HMW-Questions
```

**Good vs Bad Problem Statements**:
```
❌ BAD: "Users need a mobile app for attendance"
  → This is a SOLUTION, not a problem

✅ GOOD: "Managers cannot trust attendance data due to
         5-10% manual errors, preventing data-driven decisions"
  → Describes actual problem, solution-neutral
```

---

**Slide 6: Phase 3 - IDEATE 💡**

```
Purpose: Generate diverse solution ideas

Activities:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Brainstorming (100+ ideas target)
✅ SCAMPER technique
✅ Analogies (borrow from other industries)
✅ Concept sketching

Deliverables:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 100+ raw ideas
📋 10-15 idea themes (clustered)
📋 Top 3 concepts (voted)
📋 Concept sketches

Time: 3-4 days
Template: Ideation-Brainstorming-Template.md

Rule: Defer judgment - no "that won't work" during generation
```

**Why 100+ Ideas?**:
```
First 20 ideas: Obvious, incremental
Ideas 21-50: Getting interesting
Ideas 51-100: Breakthrough possibilities

Real example (NQH-Bot):
  154 ideas → Top concept: GPS + photo auto-verification
  Eliminated: Biometric kiosks ($50K hardware cost)
  Saved: $50K by exploring alternatives
```

---

**Slide 7: Phase 4 - PROTOTYPE 🛠️**

```
Purpose: Build minimum testable version to learn

Fidelity Levels:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Paper (4 hours) → Digital mockup (1-3 days) → Code (1-2 weeks)

Always start at LOWEST fidelity!

Deliverables:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Paper prototype (8 screens, hand-drawn)
📋 Digital mockup (Figma, clickable)
📋 Code prototype (working, not production-ready)
📋 Known limitations document

Time: 5-7 days
Template: Prototype-Test-Plan-Template.md

Goal: Build minimum to LEARN, not minimum to SHIP
```

**Real Example**:
```
NQH-Bot Progression:
  → Paper prototype (4 hours): Found navigation issues
  → Digital mockup (3 days): Validated flow
  → Code prototype (2 days): Tested with real users

Total: 1 week vs building full solution (4-6 weeks)
Savings: 3-5 weeks by testing assumptions early
```

---

**Slide 8: Phase 5 - TEST 🧪**

```
Purpose: Validate with real users, decide ship/iterate/pivot

Activities:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ User testing (5-8 participants)
✅ Task completion measurement
✅ Qualitative feedback
✅ Assumption validation

Deliverables:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Test results (quantitative metrics)
📋 User feedback patterns
📋 Assumption validation report
📋 Decision: Ship / Iterate / Pivot

Time: 5-7 days
Templates: User-Testing-Script, Feedback-Analysis

Decision Criteria:
  ✅ SHIP: >80% task completion, validated assumptions
  🔄 ITERATE: 50-80% completion, fixable issues
  ❌ PIVOT: <50% completion, false assumptions
```

---

### Part 3: SDLC 4.9 Integration (15 minutes)

**Slide 9: Design Thinking + 4-Stage Framework**

```
┌───────────────────────────────────────────────────────────┐
│  Design Thinking    SDLC Stage       Deliverable          │
├───────────────────────────────────────────────────────────┤
│  EMPATHIZE 🧠    →  Stage 00 (WHY?) →  User Persona      │
│  DEFINE 🎯       →  Stage 00-01     →  Problem Statement │
│  IDEATE 💡       →  Stage 01-02     →  100+ Ideas        │
│  PROTOTYPE 🛠️    →  Stage 03        →  Working Prototype│
│  TEST 🧪         →  Stage 03        →  User Feedback     │
└───────────────────────────────────────────────────────────┘

Integration = Seamless
  Design Thinking phases ARE part of stages (not separate)
```

---

**Slide 10: Quality Gates Enhanced**

```
Traditional SDLC 4.7:
  Gate 1: Design review
  Gate 2: Implementation review
  Gate 3: Production ready

SDLC 4.9 (5 NEW Design Thinking Gates):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Gate 0.1: Problem Definition (user-validated)
  Gate 0.2: Solution Diversity (100+ ideas)
  Gate 0.3: Prototype Fidelity (minimum to learn)
  Gate 0.4: Test Validity (right users, context)
  Gate 0.5: Ship Decision (validated assumptions)

  Gate 1: Design review (as before)
  Gate 2: Implementation review
  Gate 3: Production ready

Total: 8 quality gates (5 new + 3 existing)
```

---

### Part 4: Discussion & Q&A (30 minutes)

**Discussion Questions**:

1. **"Can you think of a recent project where Design Thinking would have helped?"**
   - What assumptions did we make?
   - Did we validate with users first?
   - What was the outcome?

2. **"What concerns do you have about adding Design Thinking to our process?"**
   - Time investment?
   - Learning curve?
   - Client expectations?

3. **"How will this change our daily work?"**
   - More user research upfront
   - More prototyping, less full builds
   - More iteration based on feedback

**Key Messages to Reinforce**:
- Design Thinking SAVES time (4-6 weeks vs 12-24 weeks)
- AI accelerates 70% of DT work (synthesis, generation)
- We already have templates (no starting from scratch)

---

### Part 5: Understanding Quiz (30 minutes)

**Quiz: 20 questions, 80% pass rate required**

**Sample Questions**:

1. What problem does Design Thinking solve?
   - a) Slow development
   - b) **Building features users don't use (70% waste)** ✅
   - c) Code quality issues
   - d) Team coordination

2. In which phase do we generate 100+ solution ideas?
   - a) Empathize
   - b) Define
   - c) **Ideate** ✅
   - d) Prototype

3. What is the purpose of a paper prototype?
   - a) Create production-ready UI
   - b) **Test assumptions with minimum effort** ✅
   - c) Show to stakeholders
   - d) Document requirements

4. How many users should we test with in the TEST phase?
   - a) 1-2
   - b) **5-8** ✅
   - c) 20-30
   - d) 100+

5. What does "ship decision" mean in SDLC 4.9?
   - a) Deploy to production immediately
   - b) **Validated assumptions, >80% completion → build full solution** ✅
   - c) Skip testing and ship
   - d) Get stakeholder approval

[... 15 more questions covering all 5 phases, quality gates, integration]

**Pass Requirement**: 16/20 correct (80%)

**If Failed**: Retake after reviewing materials

---

## 📚 SESSION 2: Design Thinking Hands-On Workshop

**Duration**: 3 hours
**Format**: Workshop with real exercise
**Facilitator**: CPO (Design Thinking expert)
**Group Size**: 5-8 people per group

---

### Workshop Structure

**Part 1: Mini Project Brief (15 minutes)**

**Scenario**: Improve team's daily standup meetings

**Current Situation**:
- 15-minute daily standup (9:00 AM)
- 15 team members
- Attendance: 70% (5 people frequently miss)
- Engagement: Mixed (some actively participate, others silent)
- Perceived value: 6/10 average rating

**Your Challenge**:
Use Design Thinking to understand the real problem and propose solution.

---

### Part 2: EMPATHIZE Exercise (45 minutes)

**Activity**: Interview 3 colleagues about standup meetings

**Interview Guide** (10 minutes per person):
```
Opening:
  "Hi, I'm learning Design Thinking and would love your help.
   Can I ask you a few questions about our daily standup?"

Questions:
  1. Walk me through your typical standup experience
  2. What do you find most valuable about standup?
  3. What frustrates you about standup?
  4. Do you attend every standup? Why or why not?
  5. If you could change one thing, what would it be?

Closing:
  "Thank you! This really helps me understand different perspectives."
```

**Facilitator's Role**:
- Pair people up for interviews
- Monitor time (10 min per interview)
- Encourage "why?" follow-up questions

**Deliverable**: Interview notes (3 sets, ~15 minutes of notes total)

---

**Activity**: Create Empathy Map (30 minutes)

**Using Template**: Empathy-Map-Canvas-Template.md

**Instructions**:
1. Review your 3 interview notes
2. Fill out empathy map:
   - What do they SEE? (standup room, others' body language, time pressure)
   - What do they HEAR? (updates, blockers, "let's take this offline")
   - What do they THINK & FEEL? (anxious, bored, rushed, valued?)
   - What do they SAY & DO? (give updates, ask questions, multitask?)

3. Synthesize insights:
   - Top 3 pain points (ranked by frequency)
   - Top 3 needs (functional + emotional)

**Facilitator's Role**:
- Walk around, review empathy maps
- Ask clarifying questions
- Ensure evidence-based (not assumptions)

**Group Share** (15 minutes):
- Each group presents their empathy map (3 min)
- Identify common patterns across groups

**Expected Insight**: Problem likely NOT "standup is too long" - might be "standup feels like reporting to manager" or "I don't get value from others' updates"

---

### Part 3: DEFINE Exercise (30 minutes)

**Activity**: Write Problem Statement (15 minutes)

**Using Template**: Problem-Statement-Template.md

**Instructions**:
```
Fill in the formula:

[User] has a problem: [describe problem]
This matters because [impact/consequence]
Currently, they [what they do now]
But this approach [why it fails]

Example (from interviews):
  Team members have a problem: they feel standup is
  "reporting to manager" not "team sync"

  This matters because 70% attendance indicates low perceived value,
  and missed blockers delay project delivery

  Currently, they give status updates in round-robin format

  But this approach doesn't facilitate team collaboration or
  problem-solving, just information broadcast
```

**Facilitator's Role**:
- Review problem statements
- Challenge: "Is this evidence-based?" (from interviews)
- Challenge: "Is this a problem or a solution in disguise?"

---

**Activity**: Generate HMW Questions (15 minutes)

**Using Template**: HMW-Questions-Worksheet.md

**Instructions**:
```
From your problem statement, generate 10 HMW questions:

Strategy 1 (Amp up the good):
  HMW make standup more collaborative? (amplify what works)

Strategy 2 (Remove the bad):
  HMW eliminate "reporting to manager" feeling?

Strategy 3 (Explore opposite):
  HMW make standup optional? (challenge assumption)

Strategy 4 (Question assumption):
  HMW sync without a meeting? (maybe standup isn't needed)

Strategy 5 (Identify resources):
  HMW leverage Slack for async updates?

[Generate 10 total HMWs]
```

**Group Share** (10 minutes):
- Each group shares top 3 HMWs
- Vote on most interesting HMW across all groups

---

### Part 4: IDEATE Exercise (45 minutes)

**Activity**: Brainstorm Solutions (30 minutes)

**Selected HMW** (from group vote): [Example] "How might we make standup collaborative instead of status broadcast?"

**Brainstorming Rules**:
```
✅ Defer judgment (no "that won't work")
✅ Go for quantity (50+ ideas target)
✅ Encourage wild ideas
✅ Build on others ("yes, and...")
```

**Process**:
1. **Silent brainstorming** (10 min)
   - Everyone writes ideas on sticky notes
   - One idea per note
   - Target: 10 ideas per person

2. **Share & cluster** (10 min)
   - Each person reads ideas aloud
   - Stick on wall
   - Group similar ideas into themes

3. **Build & combine** (10 min)
   - Pick most interesting themes
   - "Yes, and..." - build on promising ideas
   - Create 3-5 hybrid concepts

**Facilitator's Role**:
- Enforce "defer judgment" rule
- Encourage wild ideas ("what if standup was 5 minutes?")
- Help cluster ideas into themes

**Expected Output**: 50+ ideas clustered into 5-7 themes

---

**Activity**: Concept Selection (15 minutes)

**Dot Voting**:
- Each person gets 3 votes
- Vote for concepts that are:
  - Highest impact on problem
  - Most exciting/innovative
  - Feasible to prototype

**Result**: Top 1 concept selected

**Example Concept**:
```
"Async Standup + Weekly Sync"

Description:
  - Daily: Slack thread (3 questions, <5 min per person)
  - Weekly: 30-min collaborative problem-solving (blockers only)
  - Manager gets daily updates async
  - Team gets focused sync time weekly

Benefits:
  - Eliminates "reporting" feeling (async to manager)
  - Focuses sync time on collaboration
  - Respects different schedules (async flexibility)
```

---

### Part 5: PROTOTYPE Exercise (30 minutes)

**Activity**: Paper Prototype (30 minutes)

**Instructions**:
```
Create paper prototype of selected concept:

Materials: Paper, markers, scissors

For "Async Standup + Weekly Sync":
  Screen 1: Slack standup thread template
  Screen 2: Standup bot questions (3 questions)
  Screen 3: Weekly meeting calendar invite
  Screen 4: Blocker tracking board

Time: 20 minutes to create

Test: 10 minutes - walk through with another group
```

**Facilitator's Role**:
- Provide materials
- Encourage low-fidelity (rough sketches OK)
- Time management

**Deliverable**: Paper prototype that can be "played" (facilitator moves cards, user points and explains)

---

### Part 6: Workshop Debrief (15 minutes)

**Reflection Questions**:
1. What surprised you during this exercise?
2. How was this different from our usual approach?
3. What value did each phase add?
4. What would you do differently next time?

**Key Learnings**:
```
✅ User interviews reveal unexpected insights
   (Problem often NOT what we assumed)

✅ Quantity ideation unlocks breakthrough ideas
   (First 20 ideas = obvious, ideas 50+ = interesting)

✅ Paper prototypes save massive time
   (20 min prototype vs 2 weeks code)

✅ Design Thinking is systematic, not random
   (Templates provide structure)
```

**Next Steps**:
- Apply to real project (Session 4)
- Use templates on own
- Ask CPO for guidance when stuck

---

## 📚 SESSION 3: Templates, Code Quality & Code Review Excellence

**Duration**: 2 hours
**Format**: Template walkthrough (45 min) + Code quality standards (30 min) + Code review training (45 min)
**Facilitator**: Product Manager + CTO

---

### Part 1: Template Library Tour (45 minutes)

**9 Templates Overview** (5 min each template):

For each template:
1. **When to use**: Which DT phase?
2. **Time required**: How long to complete?
3. **Example**: Show filled-in version (NQH-Bot)
4. **Common mistakes**: What to avoid
5. **Quick demo**: Fill out 1 section live

**Templates**:
1. Empathy-Map-Canvas-Template.md (Phase 1)
2. User-Journey-Map-Template.md (Phase 1)
3. Problem-Statement-Template.md (Phase 2)
4. POV-Statement-Template.md (Phase 2)
5. HMW-Questions-Worksheet.md (Phase 2)
6. Ideation-Brainstorming-Template.md (Phase 3)
7. Prototype-Test-Plan-Template.md (Phase 4)
8. User-Testing-Script-Template.md (Phase 5)
9. Feedback-Analysis-Template.md (Phase 5)

**Facilitator's Role**:
- Show real examples (NQH-Bot case study)
- Emphasize: "Use templates, don't reinvent"
- Encourage questions

**Deliverable**: Confidence assessment (1-5 scale for each template)

---

### Part 2: Code Quality Standards (30 minutes)

**SDLC 4.9.1 Code Standards Overview** (10 min):

```yaml
Code File Naming Standards (Restored from SDLC 4.3/4.4):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Python Files:
  Format: snake_case
  Max Length: 50 characters
  Examples:
    ✅ user_service.py
    ✅ invoice_repository.py
    ✅ bcc_activities.py
    ❌ UserService.py (wrong - use snake_case)
    ❌ invoice-repository.py (wrong - use underscores)

TypeScript Files:
  Format: camelCase
  Max Length: 50 characters
  Examples:
    ✅ arService.ts
    ✅ paymentSlice.ts
    ✅ userContext.ts
    ❌ ar_service.ts (wrong - use camelCase)
    ❌ ARService.ts (wrong - use camelCase)

React Components:
  Format: PascalCase
  Max Length: 50 characters
  Examples:
    ✅ ARDashboard.tsx
    ✅ InvoiceList.tsx
    ✅ CustomerForm.tsx
    ❌ arDashboard.tsx (wrong - use PascalCase)
    ❌ invoice_list.tsx (wrong - use PascalCase)

Alembic Migrations:
  Format: {revision}_{description}.py
  Max Length: 60 characters
  Examples:
    ✅ 001_initial_schema.py
    ✅ 002_add_tenant_field.py
    ❌ add_tenant_field.py (wrong - missing revision)
```

**Why File Naming Matters** (5 min):
```
Benefits:
  → Consistency across codebase
  → Better IDE navigation and search
  → AI tools understand code structure better
  → Team collaboration efficiency
  → Reduced confusion for new team members

Enforcement:
  → Pre-commit hooks validate naming
  → CI/CD pipeline checks
  → Code review checklist item
```

**Other Code Quality Standards** (15 min):
```yaml
Test Coverage Requirements:
  Unit Tests: ≥80%
  Integration Tests: ≥70%
  E2E Tests: ≥60%

Performance Targets:
  API Response: <50ms (p50), <100ms (p95)
  Uptime: 99.9%+

Code Style:
  Python: PEP 8, Black formatting
  JavaScript/TypeScript: ESLint, Prettier
  Documentation: English-only comments, SDLC headers

Vietnamese Authenticity:
  BHXH: 17.5% employer, 8% employee (exact)
  VAT: 10% standard rate (exact)
  VND: No decimals, proper formatting
```

**Reference**: `08-Documentation-Standards/SDLC-Code-File-Naming-Standards.md`

---

### Part 3: Code Review Excellence (45 minutes)

**Subscription-Powered Methodology** (MTS/NQH Tier 2):

**3-Layer System**:
```
Layer 1: PRE-COMMIT (Cursor + Local AI)
  → Catch 70-80% issues BEFORE commit

Layer 2: PR REVIEW (Claude Max + Copilot)
  → Human-AI collaborative review

Layer 3: POST-MERGE LEARNING
  → Extract patterns, prevent recurrence
```

**Live Demo** (30 minutes):

**Demo 1: Pre-Commit with Cursor** (10 min)
```
1. Write code with intentional SDLC violation
   (e.g., Vietnamese comment in code)

2. Show Cursor real-time warning
   → Red underline, suggests fix

3. Run pre-commit hook
   → Commit BLOCKED

4. Fix violation
   → Commit successful

Key Message: "Catch at commit = 10x cheaper than PR-level fix"
```

**Demo 2: PR Review with Claude Max** (15 min)
```
1. Create PR with 3 intentional issues:
   - SQL injection vulnerability
   - N+1 query problem
   - Missing test coverage

2. Copy PR diff to Claude Max
   → Use PR Review Template

3. Show Claude output:
   → 3 issues found with specific line numbers
   → Severity ranking (Critical/High/Medium)
   → Suggested fixes

4. Post Claude review as PR comment
   → Request changes from author

Time: 5 min (vs 45 min manual review)
Savings: 40 min per PR × 80 PRs/month = 53 hours/month
```

**Demo 3: Post-Merge Learning** (5 min)
```
1. Show monthly pattern analysis:
   → "Vietnamese date format errors: 32% of PRs"

2. Show preventive action taken:
   → Added to .cursorrules
   → Created utility function
   → Team training scheduled

3. Show reduction:
   → Next month: 12% (down from 32%)

Key Message: "Learn from mistakes, prevent recurrence"
```

**Practice Exercise** (20 minutes):
- Pair up
- One person writes code with 2-3 issues
- Other person reviews using Claude Max
- Switch roles

**ROI Calculation** (10 minutes):
```
MTS/NQH Reality (15 developers):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Monthly Cost: $750
  Cursor Pro: $20 × 15 = $300
  Copilot: $10 × 15 = $150
  Claude Max: $20 × 15 = $300

Monthly Value: $16,000
  Pre-commit: 100 hours saved = $10,000
  PR review: 40 hours saved = $4,000
  Post-merge learning: 20 hours saved = $2,000

ROI: 2,033%
Payback: 13.5 days

Key Message: "Subscriptions already paid for - just optimize usage"
```

---

## 📚 SESSION 4: Real Project Application

**Duration**: 1 hour initial + ongoing practice
**Format**: Guided application on actual project
**Facilitator**: CPO (first time), then autonomous

---

### Pilot Project Selection

**Criteria**:
```
✅ Small-medium scope (completable in 2-3 weeks)
✅ Real user problem (not internal tech debt)
✅ Accessible users (can interview 5-8 people)
✅ Team commitment (1-2 people dedicated)
```

**Suggested Pilot Projects** (MTS/NQH context):
1. Improve internal tool (e.g., timesheet system)
2. New feature for existing product (e.g., BFlow enhancement)
3. Client project with flexible timeline

---

### Week-by-Week Guide

**Week 1: EMPATHIZE + DEFINE**
```
Monday:
  □ Select pilot project
  □ Identify 5-8 users to interview
  □ Prepare interview guide (30 min)

Tuesday-Wednesday:
  □ Conduct 5-8 user interviews (10 min each)
  □ Fill out Empathy Map Canvas
  □ Create User Journey Map

Thursday:
  □ Write Problem Statement
  □ Create POV Statement
  □ Generate 20 HMW questions

Friday:
  □ CPO Review Session (30 min)
    - Validate problem statement with CPO
    - Get feedback on empathy insights
    - Approve/iterate before moving to ideation
```

**Week 2: IDEATE + PROTOTYPE**
```
Monday:
  □ Ideation session (90 min, whole team)
  □ Generate 100+ ideas
  □ Cluster into themes
  □ Select top 3 concepts (dot voting)

Tuesday:
  □ Paper prototype selected concept (4 hours)
  □ Test internally (3 colleagues)
  □ Iterate based on feedback

Wednesday-Thursday:
  □ Digital mockup (Figma, 2 days)
  □ Clickable prototype
  □ Prepare for user testing

Friday:
  □ CPO Review Session (30 min)
    - Validate prototype approach
    - Review test plan
    - Recruit 5-8 users for testing
```

**Week 3: TEST + DECIDE**
```
Monday-Wednesday:
  □ Conduct 5-8 user testing sessions (60 min each)
  □ Record results (quantitative + qualitative)
  □ Synthesize findings (Feedback Analysis Template)

Thursday:
  □ Analyze results
  □ Validate assumptions
  □ Make decision: Ship / Iterate / Pivot

Friday:
  □ CPO Final Review (60 min)
    - Present findings
    - Justify decision (ship/iterate/pivot)
    - If ship: Plan production build
    - If iterate: Plan fixes and retest
```

---

### Success Criteria

**Pilot Project Success** = 80%+ on checklist:

```
EMPATHIZE Phase:
  □ Conducted 5+ user interviews (evidence-based)
  □ Created empathy map (4 quadrants filled)
  □ Identified 3+ pain points with user quotes

DEFINE Phase:
  □ Problem statement validated with 3 users
  □ POV statement includes insight (not obvious)
  □ Generated 20+ HMW questions

IDEATE Phase:
  □ Generated 50+ ideas (quantity achieved)
  □ Identified 5+ themes (diversity)
  □ Team voted on top concept (alignment)

PROTOTYPE Phase:
  □ Started at paper (low fidelity first)
  □ Built minimum to test (not over-built)
  □ Known limitations documented

TEST Phase:
  □ Tested with 5+ real users (not internal)
  □ Captured quant + qual data (complete)
  □ Made ship/iterate/pivot decision (clear)

Overall:
  □ Team learned Design Thinking (80%+ confidence)
  □ Used templates successfully (no major blockers)
  □ CPO validated at 2 checkpoints (approved)
  □ Delivered validated solution OR learned why pivot needed
```

---

## 📊 Training Assessment & Certification

### Individual Assessment

**Knowledge Assessment** (Session 1 Quiz):
- 20 questions, 80% pass rate
- Covers all 5 DT phases + SDLC 4.9 integration
- Retake allowed if failed

**Skills Assessment** (Session 2 Workshop):
- Completed empathy map (evidence-based)
- Problem statement (validated)
- 10+ HMW questions (diverse)
- Paper prototype (testable)

**Application Assessment** (Session 4 Pilot):
- Real project using all 5 phases
- Template usage (6+ templates used correctly)
- CPO validation at 2 checkpoints (passed)

---

### SDLC 4.9 Certification

**Requirements**:
```
✅ Attended all 4 training sessions (8 hours)
✅ Passed knowledge quiz (16/20 or 80%+)
✅ Completed hands-on workshop (deliverables submitted)
✅ Applied to pilot project (80%+ success criteria)
✅ CPO approval (validated at 2 checkpoints)
```

**Certificate Issued**:
```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║          SDLC 4.9 CERTIFIED PRACTITIONER                  ║
║                                                           ║
║  This certifies that [Name]                               ║
║  has successfully completed SDLC 4.9 training and         ║
║  demonstrated proficiency in:                             ║
║                                                           ║
║  ✅ Design Thinking 5-phase methodology                   ║
║  ✅ 9 practical templates application                     ║
║  ✅ SDLC 4.9 4-Stage Framework integration                ║
║  ✅ Subscription-powered code review excellence           ║
║  ✅ Real project validation                               ║
║                                                           ║
║  Date: [Completion Date]                                  ║
║  Validated by: [CPO Name]                                 ║
║                                                           ║
║  Certificate ID: SDLC48-[Number]                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

**Benefits**:
- Authorization to lead Design Thinking workshops
- Mentor new team members on SDLC 4.9
- Quality gate reviewer (peer validation)

---

## 📚 Self-Learning Resources

### For Those Who Miss Live Training

**Self-Paced Learning Path** (10 hours total):

**Week 1: Foundations** (3 hours)
```
Day 1-2: Read Core Documents
  □ SDLC-4.8-Core-Methodology.md (50KB, 2 hours)
  □ SDLC-4.8-Design-Thinking-Principles.md (54KB, 2 hours)

Day 3: Watch Case Study
  □ SDLC-4.8-Design-Thinking-Case-Study-NQH-Bot.md (30KB, 1 hour)
  □ Note: Real 4-week timeline, 96% time savings

Day 4: Self-Assessment Quiz
  □ Take knowledge quiz (20 questions)
  □ Score: ___/20 (need 16+ to proceed)
```

**Week 2: Templates Practice** (4 hours)
```
Day 5-6: Template Walkthrough
  □ Read all 9 templates (160KB, 2 hours)
  □ Download templates to local folder

Day 7-8: Mini Exercise
  □ Pick personal problem (e.g., morning routine)
  □ Apply 5 phases with templates
  □ Interview 3 friends/family
  □ Create paper prototype
  □ Self-grade: Did I follow process?
```

**Week 3: Real Application** (3 hours)
```
Day 9-10: Pilot Project
  □ Apply to real work project (small scope)
  □ Use templates
  □ Document learnings

Day 11: CPO 1-on-1
  □ Schedule 30-min review with CPO
  □ Present pilot project results
  □ Get feedback and certification
```

---

### Continuous Learning

**Monthly Design Thinking Meetup** (1 hour):
- Share pilot project outcomes
- Discuss challenges and solutions
- Guest speakers (CPO, external DT experts)
- Template refinement based on usage

**Quarterly Refresher** (2 hours):
- Review SDLC 4.9 enhancements (if any)
- Advanced techniques (e.g., remote user testing)
- Cross-team case study sharing

---

## 🎯 Training Success Metrics

### Team-Level Metrics

**Training Completion**:
- Target: 100% team attendance
- Actual: ___% (tracked)

**Certification Rate**:
- Target: 80%+ certified within 4 weeks
- Actual: ___% (tracked)

**Template Usage**:
- Target: 80%+ projects use 3+ templates
- Actual: ___% (tracked)

---

### Business Impact Metrics (3 Months Post-Training)

**Feature Adoption**:
- Baseline: 30% (industry average)
- Target: 70%+ (SDLC 4.9 validated)
- Actual: ___% (measured)

**Time to Validated Solution**:
- Baseline: 12-24 weeks (traditional)
- Target: 4-6 weeks (SDLC 4.9)
- Actual: ___ weeks (measured)

**Development Waste**:
- Baseline: 64% features not essential
- Target: <20% (validated before build)
- Actual: ___% (measured)

---

## 📞 Support & Resources

### During Training

**CPO Office Hours**:
- Monday & Thursday, 2:00 PM - 3:00 PM
- Drop-in for questions, template help
- No appointment needed

**Slack Channel**: `#sdlc-4-8-training`
- Ask questions
- Share learnings
- Peer support

**1-on-1 Coaching** (if needed):
- Schedule with CPO (taidt@mtsolution.com.vn)
- 30 minutes per session
- For those struggling with certification

---

### Post-Training

**Template Library**:
- Location: `/06-Templates-Tools/Design-Thinking/`
- Always accessible
- Updated based on team feedback

**Case Study Library**:
- Location: `/07-Case-Studies/`
- NQH-Bot (completed)
- BFlow, MTEP (coming soon)
- Add your own pilot projects

**Expert Consultation**:
- CPO available for complex projects
- CTO for technical DT integration
- CEO for strategic DT application

---

**Document**: SDLC-4.9.1-Training-Materials
**Purpose**: Complete learning package for team adoption
**Audience**: All team members (developers, designers, PM, QA)
**Duration**: 8 hours core + ongoing practice
**Certification**: SDLC 4.9.1 Certified Practitioner
**Version**: 2.0
**Date**: November 29, 2025
**License**: MTS Internal Use
**What's New**: Code File Naming Standards restored, 10-Stage Lifecycle integration
