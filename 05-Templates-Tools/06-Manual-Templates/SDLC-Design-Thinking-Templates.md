# SDLC Design Thinking — Templates & Case Studies

```yaml
document_id: "SDLC-DESIGN-THINKING-TEMPLATES"
title: "Design Thinking Templates & Case Studies"
version: "6.3.0"
status: "ACTIVE"
section: "02-Core-Methodology/Documentation-Standards"
ring: "Core"
parent: "SDLC-Design-Thinking-Principles.md"
audience: ["Product Managers", "Designers", "Engineers", "Tech Leads"]
created: "2026-02-18"
last_updated: "2026-02-18"
```

> **This file contains detailed templates and examples extracted from [SDLC-Design-Thinking-Principles.md](../SDLC-Design-Thinking-Principles.md).** Use the parent document for principles and summaries; use this file for hands-on execution.

---

## Phase 1: EMPATHIZE — Detailed Templates

### User Interview Script Template

```markdown
## Interview Script: [Feature/Problem Area]

**Date**: ___________
**Interviewer**: ___________
**Interviewee**: ___________ (Role: ___________)
**Duration**: 30-45 minutes

### Opening (5 min)
- Introduce yourself and the purpose
- "We're trying to understand how you [activity]. No right or wrong answers."
- Ask for consent to record

### Context Questions (10 min)
1. "Walk me through your typical day when you [activity]"
2. "What tools do you currently use for [activity]?"
3. "How long have you been doing [activity]?"

### Pain Point Discovery (15 min)
4. "What's the most frustrating part of [activity]?"
5. "Tell me about the last time [activity] went wrong"
6. "If you could change ONE thing about [activity], what would it be?"
7. "What workaround have you created for [pain point]?"

### Dream State (10 min)
8. "If you had a magic wand, what would the perfect [solution] look like?"
9. "What would success look like for you?"
10. "How would you know if [solution] was working?"

### Closing (5 min)
- "Is there anything else you'd like to share?"
- "Who else should we talk to?"
- Thank them for their time
```

### Empathy Map Template

```
┌───────────────────────────────────────────────────────────────────────┐
│                        EMPATHY MAP                                    │
│                    User: [Persona Name]                               │
├───────────────────────┬───────────────────────────────────────────────┤
│      THINKS & FEELS   │              SEES                             │
│  • Worried about...   │  • Colleagues doing...                        │
│  • Hopes for...       │  • Industry trends...                         │
│  • Frustrated by...   │  • Competitors offering...                    │
├───────────────────────┼───────────────────────────────────────────────┤
│         SAYS & DOES   │              HEARS                            │
│  • "I need..."        │  • Boss says...                               │
│  • Workaround: ...    │  • Friends recommend...                       │
│  • Current tools: ... │  • Market buzz about...                       │
├───────────────────────┴───────────────────────────────────────────────┤
│  PAIN POINTS                    │  GAINS                              │
│  1. ___________                 │  1. ___________                     │
│  2. ___________                 │  2. ___________                     │
│  3. ___________                 │  3. ___________                     │
└─────────────────────────────────┴─────────────────────────────────────┘
```

### Journey Map Template

```
┌──────────────────────────────────────────────────────────────────────────┐
│                     USER JOURNEY MAP                                     │
│  User: [Persona]    Scenario: [Task/Goal]    Date: [YYYY-MM-DD]        │
├──────────┬──────────┬──────────┬──────────┬──────────┬─────────────────┤
│  STAGE   │ DISCOVER │  LEARN   │   USE    │ TROUBLE  │   RESOLVE      │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Actions  │          │          │          │          │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Thoughts │          │          │          │          │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Emotions │  😊/😐/😡 │ 😊/😐/😡 │ 😊/😐/😡 │ 😊/😐/😡 │  😊/😐/😡       │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Pain Pts │          │          │          │          │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Opport.  │          │          │          │          │                 │
└──────────┴──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

---

## Phase 2: DEFINE — Detailed Templates

### Problem Statement Formula

```
[User persona] needs [a way to do something]
because [surprising insight from research],
but currently [barrier/frustration].
```

**Examples**:
- "Night-shift security guards need a way to record attendance reliably because manual sign-in is easily faked, but current biometric systems fail in low-light environments."
- "Junior developers need a way to understand codebase architecture because onboarding documentation is outdated, but existing tools only show file structure without explaining relationships."

### POV (Point of View) Statement

```
We met [user] who [observation].
We were surprised to discover [insight].
We wonder if this means [inference].
It would be game-changing if [potential solution direction].
```

### "How Might We" (HMW) Question Workshop

**Rules**:
1. Start with "How might we..."
2. Not too broad ("...improve their life?") — no actionable direction
3. Not too narrow ("...add a blue button?") — solution embedded in question
4. Just right ("...reduce attendance fraud without expensive hardware?")

**HMW Generator**:
```
Base Problem: [problem statement]

HMW [amplify the positive]?
HMW [remove the bad]?
HMW [explore the opposite]?
HMW [question an assumption]?
HMW [go after an adjective]?
HMW [think about other resources]?
HMW [find an analogy in another domain]?
HMW [shift the challenge to another person]?
```

---

## Phase 3: IDEATE — Detailed Templates

### Brainstorming Rules (Stanford d.school)

```
┌────────────────────────────────────────────────────────────────┐
│  BRAINSTORMING RULES                                           │
│                                                                │
│  1. DEFER JUDGMENT    → No "but..." or "that won't work"      │
│  2. ENCOURAGE WILD    → Crazy ideas welcome                   │
│  3. BUILD ON IDEAS    → "Yes, AND..." not "Yes, BUT..."      │
│  4. STAY ON TOPIC     → Focus on the HMW question             │
│  5. ONE AT A TIME     → Let each person complete their thought│
│  6. BE VISUAL         → Sketch, don't just describe           │
│  7. GO FOR QUANTITY   → Target 50+ ideas in 30 minutes       │
└────────────────────────────────────────────────────────────────┘
```

### SCAMPER Technique

| Letter | Question | Example (Attendance System) |
|--------|----------|-----------------------------|
| **S**ubstitute | What can be replaced? | Replace fingerprint with face recognition |
| **C**ombine | What can be merged? | Combine check-in with task assignment |
| **A**dapt | What can be adapted from elsewhere? | Adapt airport e-gate (walk-through, no stop) |
| **M**odify | What can be enlarged/reduced? | Reduce check-in to 0 steps (auto-detect) |
| **P**ut to other uses | New purpose for existing tech? | Use security cameras for attendance |
| **E**liminate | What can be removed? | Eliminate manual process entirely |
| **R**everse | What if we flip the approach? | Instead of check-in, detect absence only |

### Crazy 8s Template

```
┌────────┬────────┬────────┬────────┐
│  Idea  │  Idea  │  Idea  │  Idea  │
│   #1   │   #2   │   #3   │   #4   │
│        │        │        │        │
│ 1 min  │ 1 min  │ 1 min  │ 1 min  │
├────────┼────────┼────────┼────────┤
│  Idea  │  Idea  │  Idea  │  Idea  │
│   #5   │   #6   │   #7   │   #8   │
│        │        │        │        │
│ 1 min  │ 1 min  │ 1 min  │ 1 min  │
└────────┴────────┴────────┴────────┘
Total: 8 ideas in 8 minutes
Rule: One sketch per box, no revisiting
```

### Prioritization Matrix

```
                    HIGH IMPACT
                        │
         ┌──────────────┼──────────────┐
         │   QUICK       │    BIG        │
         │   WINS ⭐     │    BETS       │
         │              │              │
    LOW ─┼──────────────┼──────────────┼── HIGH
  EFFORT │              │              │  EFFORT
         │   FILL        │    MONEY      │
         │   INS         │    PIT        │
         │              │              │
         └──────────────┼──────────────┘
                        │
                    LOW IMPACT

Priority:
  1. Quick Wins (high impact, low effort) → Do first
  2. Big Bets (high impact, high effort) → Plan carefully
  3. Fill-ins (low impact, low effort) → Do if time allows
  4. Money Pits (low impact, high effort) → Avoid
```

### AI-Assisted Brainstorming Prompt

```markdown
## AI Brainstorming Prompt

Context: [paste problem statement]
Constraints: [paste constraints from AGENTS.md/requirements]

Generate 20 solution ideas for this problem. Include:
- 5 conventional approaches (proven, low-risk)
- 5 innovative approaches (new technology, moderate-risk)
- 5 radical approaches (paradigm shift, high-risk)
- 5 cross-industry analogies (adapted from other domains)

For each idea, provide:
- One-sentence description
- Estimated effort (S/M/L)
- Key assumption to validate
```

---

## Phase 4: PROTOTYPE — Detailed Templates

### 4 Fidelity Levels

| Level | What | When | Tools | Time |
|-------|------|------|-------|------|
| **L1: Paper** | Sketches, wireframes | Early exploration | Paper, whiteboard | 30 min |
| **L2: Digital Mockup** | Clickable screens | Concept validation | Figma, Balsamiq | 2-4 hours |
| **L3: Functional MVP** | Working features, real data | Usability testing | Code, no-code tools | 2-5 days |
| **L4: Production Pilot** | Full feature, limited rollout | Business validation | Production stack | 1-2 weeks |

### Prototype Planning Template

```yaml
Prototype Plan:
  Feature: "[feature name]"
  Fidelity Level: "L1/L2/L3/L4"
  Time Budget: "[hours/days]"
  
  What to include:
    - "[core interaction 1]"
    - "[core interaction 2]"
    - "[core interaction 3]"
  
  What to fake:
    - "[non-critical feature 1] → use static data"
    - "[non-critical feature 2] → use placeholder"
  
  Success Criteria:
    - "Users can complete [task] in < [time]"
    - "Users understand [concept] without explanation"
    - "[metric] improves by [%] compared to current"
  
  Test Plan:
    - Participants: "[number] users from [persona]"
    - Duration: "[minutes] per session"
    - Questions: "[key questions to answer]"
```

### AI-Assisted Prototyping Workflow

```yaml
Step 1: Generate UI with AI
  Tool: v0.dev, Claude Artifacts, or Copilot
  Input: "Create a [component] that [does what] for [persona]"
  Output: Working React/HTML component

Step 2: Review and refine
  Checklist:
    - [ ] Matches user mental model (from empathy map)
    - [ ] Addresses top pain point
    - [ ] Progressive disclosure (simple first, details later)
    - [ ] Accessible (WCAG 2.1 AA minimum)

Step 3: Connect to real data (L3+)
  - Replace static data with API calls
  - Use real (anonymized) user data if possible
  - Test with edge cases (empty state, error state, large data)
```

---

## Phase 5: TEST — Detailed Templates

### User Testing Protocol

```yaml
Test Session Plan:
  Feature: "[feature being tested]"
  Prototype Level: "L1/L2/L3/L4"
  Participants: "[number] from [persona]"
  Duration: "[minutes] per session"
  Facilitator: "[name]"
  Observer: "[name]"

Pre-Test Setup:
  - [ ] Prototype deployed/accessible
  - [ ] Recording consent forms ready
  - [ ] Task list prepared (3-5 tasks)
  - [ ] Observation template ready

Tasks (give these to users):
  1. "[Task phrased as goal, not instruction]"
     Success: "[what 'done' looks like]"
  2. "[Task 2]"
     Success: "[criteria]"
  3. "[Task 3]"
     Success: "[criteria]"

Observation Focus:
  - Where do users hesitate? (>3 seconds)
  - Where do users make errors?
  - What do users say aloud? (think-aloud protocol)
  - What questions do users ask?
  - Where do users smile or express satisfaction?

Post-Test Questions:
  1. "What was your overall impression?"
  2. "What was the most confusing part?"
  3. "What would you change?"
  4. "On a scale of 1-10, how likely would you use this?"
  5. "How does this compare to your current approach?"
```

### Feedback Analysis Framework

```
┌──────────────────────────────────────────────────────────────────┐
│  FEEDBACK CATEGORIZATION                                         │
├──────────────┬───────────────┬───────────────┬──────────────────┤
│  Category    │  Priority      │  Action        │  Example          │
├──────────────┼───────────────┼───────────────┼──────────────────┤
│  Usability   │  High if >50%  │  Fix before    │  "Can't find     │
│  (Can't do)  │  users affected│  next test     │   the button"    │
├──────────────┼───────────────┼───────────────┼──────────────────┤
│  Confusion   │  Medium        │  Redesign or   │  "What does      │
│  (Don't      │               │  add guidance   │   this mean?"    │
│   understand)│               │               │                  │
├──────────────┼───────────────┼───────────────┼──────────────────┤
│  Preference  │  Low           │  Note for      │  "I'd prefer     │
│  (Want       │               │  future        │   blue color"    │
│   different) │               │               │                  │
├──────────────┼───────────────┼───────────────┼──────────────────┤
│  Delight     │  Learn         │  Amplify       │  "Oh, this is    │
│  (Love it)   │  from it       │  the pattern   │   so easy!"      │
└──────────────┴───────────────┴───────────────┴──────────────────┘
```

### Iterate vs. Pivot Decision Tree

```
                    Test Results
                        │
                ┌───────┴───────┐
                │               │
          >70% success     <30% success
                │               │
          ITERATE ✅        PIVOT 🔄
          (Refine details)  (Rethink approach)
                │               │
                │         ┌─────┴─────┐
                │         │           │
                │    Same problem  Different problem
                │    new solution  entirely
                │         │           │
                │    IDEATE again  EMPATHIZE again
                │                     │
                │              Go back to Phase 1
                │
          30-70% success
                │
          DIG DEEPER 🔍
          (More user interviews)
          (Identify specific failures)
```

---

## Case Study: AI Attendance System

> This case study demonstrates all 5 phases applied to a real product.

### Phase 1 Results (EMPATHIZE)

**52 Interviews Conducted**:
- 15 security guards (night-shift)
- 10 factory managers
- 12 HR staff
- 8 IT administrators
- 7 executive sponsors

**Key Insights**:
1. Night guards fake buddy-punch 23% of shifts
2. Biometric systems fail at 15% in low-light
3. Manual processes take 45 min/day for HR reconciliation
4. Guards resent "surveillance" framing vs. "safety" framing

### Phase 2 Results (DEFINE)

**Problem Statement**: "Night-shift security guards need a reliable way to prove attendance because buddy-punching costs companies ₫2.3B annually, but current biometric systems fail in low-light conditions and feel invasive."

**Top 3 HMW Questions**:
1. HMW make attendance verification invisible (no extra steps)?
2. HMW work reliably in all lighting conditions?
3. HMW frame this as a safety benefit, not surveillance?

### Phase 3 Results (IDEATE)

**142 Ideas Generated** → Top 3 Concepts:

| Concept | Description | Effort | Risk |
|---------|-------------|--------|------|
| **A: AI Face + Patrol** | Face recognition + GPS patrol tracking | High | Medium |
| **B: Smart Badge** | NFC badge + motion sensor (no biometric) | Low | Low |
| **C: Voice Check-in** | Voice recognition + scheduled check-in calls | Medium | Medium |

**Decision**: Concept A selected — highest long-term value, acceptable risk.

### Phase 4 Results (PROTOTYPE)

| Level | What Was Built | Duration | Key Learning |
|-------|---------------|----------|--------------|
| L1 (Paper) | Paper wireframes of check-in flow | 2 hours | Guards want ≤2 steps |
| L2 (Mockup) | Figma prototype of mobile app | 1 day | Tab layout confusing — simplified to 1-screen |
| L3 (MVP) | Working face recognition with IR camera | 1 week | 89% accuracy initial → 95.2% after tuning |
| L4 (Pilot) | Full system at 1 factory, 50 guards | 2 weeks | Night accuracy: 95.2% → exceeded 90% target |

### Phase 5 Results (TEST)

**Pilot Results (50 guards, 14 days)**:
- Accuracy: 95.2% (target: 90%) ✅
- Processing time: 1.2s average (target: <3s) ✅
- Guard satisfaction: 4.2/5.0 ✅
- Buddy-punch detection: 100% ✅
- False rejection rate: 3.1% (acceptable for security context)

**6-Month Outcomes**:
- Buddy-punch incidents: 23% → 0.4% (-98%)
- HR reconciliation time: 45 min/day → 2 min/day (-96%)
- Revenue protected: ₫15B annually
- Guard satisfaction maintained: 4.1/5.0

### Lessons Learned

1. **"Safety, not surveillance"** framing was critical for adoption
2. **IR (infrared) camera** was the technical breakthrough for low-light
3. **2-step UX** maximum — guards won't tolerate complex flows at 3 AM
4. **Pilot before scale** — the L4 pilot caught edge cases (rain, dust)

---

## AI Tools Integration by Phase

| Phase | AI Tool | Usage |
|-------|---------|-------|
| EMPATHIZE | Claude / GPT-4o | Summarize interview transcripts, identify patterns |
| DEFINE | Claude | Generate HMW questions from insights, sharpen problem statement |
| IDEATE | GPT-4o / Gemini | Brainstorm 50+ ideas, cross-industry analogies |
| PROTOTYPE | v0.dev / Claude Artifacts | Generate UI components, rapid wireframing |
| TEST | Claude | Analyze feedback transcripts, categorize findings |

### Example AI Prompt (Empathy Synthesis)

```
You are a UX researcher analyzing interview transcripts.

I have [N] interviews about [topic]. 
Identify:
1. Top 5 recurring pain points (with frequency)
2. Top 3 surprising insights (unexpected findings)
3. Opportunity areas for improvement
4. Contradictions between what users SAY vs DO

Format as a structured research brief (max 500 words).
```

---

## Success Metrics by Level

### Team Metrics
- Number of user interviews conducted per sprint
- Empathy map quality score (completeness, specificity)
- HMW question diversity (breadth of exploration)

### Product Metrics
- Feature adoption rate (target: >60% weekly active)
- User satisfaction score (target: >4.0/5.0)
- Time to first value (target: <30 minutes)
- Prototype test pass rate (target: >70%)

### Business Metrics
- Feature waste reduction (target: <30%, from 60-70% baseline)
- Time-to-market improvement (target: 30% faster)
- Cost of rework reduction (target: 50% less)

---

## Training Workshop Outline

### Module 1: Why Design Thinking? (30 min)
- The 70% waste problem
- Case study: Before vs. After
- Exercise: Identify waste in current project

### Module 2: Empathy & Define (60 min)
- Technique: Mini user interview (paired exercise)
- Practice: Build an empathy map from interview
- Practice: Write a problem statement + 3 HMW questions

### Module 3: Ideate & Prototype (60 min)
- Exercise: Crazy 8s (8 ideas in 8 minutes)
- Exercise: SCAMPER on a real product
- Practice: Build L1 paper prototype

### Module 4: Test & Iterate (60 min)
- Exercise: Conduct 3 user tests with paper prototype
- Practice: Categorize feedback using the framework
- Decision: Iterate, Pivot, or Ship?

**Total Duration**: 4 hours (half-day workshop)

---

## Resources & Template Files

Templates referenced in this document can be found at:
- `/06-Templates-Tools/Design-Thinking/` (if available in your project)
- Or use the templates directly from this document

### Quick Reference Card

| Phase | Key Output | Time Budget (1 sprint) |
|-------|------------|----------------------|
| EMPATHIZE | 5+ interviews, personas, journey map | 2-3 days |
| DEFINE | Problem statement, 3 HMW questions | 1 day |
| IDEATE | 50+ ideas, top 3 concepts | 1 day |
| PROTOTYPE | L2-L3 prototype | 2-3 days |
| TEST | Test results, iterate/pivot decision | 1-2 days |

---

**Document Status**: ACTIVE — Extracted from SDLC-Design-Thinking-Principles.md
**Framework Version**: SDLC 6.3.0
**Last Updated**: February 18, 2026
