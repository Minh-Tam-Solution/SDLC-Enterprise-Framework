# SDLC Design Thinking Principles

```yaml
document_id: "SDLC-DESIGN-THINKING-PRINCIPLES"
title: "Design Thinking Principles — Build the RIGHT Thing"
version: "6.3.1"
status: "ACTIVE"
section: "02-Core-Methodology"
ring: "Core"
pillar: "Pillar 0 — Design Thinking (WHY Before WHAT)"
audience: ["Product Managers", "Designers", "Engineers", "Tech Leads"]
created: "2024-10-15"
last_updated: "2026-02-18"
```

> **Pillar 0** of the SDLC Framework. Design Thinking is the mandatory starting point before any SDLC stage. It ensures we build the RIGHT thing (user-centered) before building the thing RIGHT (engineering-discipline).

---

## Why Design Thinking?

**The 70% Waste Problem**: Industry data shows 60–70% of software features are rarely or never used. The root cause is building solutions without understanding problems — the **"Solution Before Problem"** anti-pattern.

Design Thinking inverts this by demanding **evidence of user need** before investing in design or code:

```
Traditional: Idea → Build → Hope users like it (60-70% waste)
DT Approach: Empathize → Define → Ideate → Prototype → Test → Build (waste <30%)
```

**Connection to System Thinking**: Design Thinking addresses the *visible* layer (events & patterns) of the [Iceberg Model](SDLC-System-Thinking-Foundation.md). To solve problems sustainably, combine DT with System Thinking — understanding the *invisible* layers (structures, mental models) that generate the patterns you observe.

**Connection to Crisis-to-Pattern**: When DT-discovered issues become recurring, the [Crisis-to-Pattern Methodology](SDLC-Crisis-To-Pattern-Methodology.md) provides a pipeline to convert them into permanent policies and automation.

---

## The 5 Phases

```
     ┌─────────────────── DIVERGE ───────────────────┐
     │                                                │
  EMPATHIZE ──→ DEFINE ──→ IDEATE ──→ PROTOTYPE ──→ TEST
     │              │          │           │           │
  Understand     Frame the   Generate    Build to    Validate
  the user       problem     solutions   learn       with users
     │              │          │           │           │
     └── CONVERGE ──┘          └── CONVERGE ──────────┘

  ← Problem Space →          ← Solution Space →

  The loop repeats until validation passes (expect 3-5 iterations).
```

---

### Phase 1: EMPATHIZE — Understand the User

**Purpose**: Discover real user needs through observation and conversation — not assumptions.

| Element | Detail |
|---------|--------|
| **Key Activities** | User interviews (5–10 per persona), contextual observation, empathy mapping, journey mapping |
| **Outputs** | Interview transcripts, empathy maps, journey maps, persona profiles |
| **Time Budget** | 2–3 days per sprint cycle |
| **AI Assistance** | Transcription (Otter.ai), pattern extraction (Claude), affinity clustering |

**Core Principle**: Ask open-ended questions about behavior, not opinions. Observe what users *do*, not what they *say* they do.

**Pitfall**: "Fake Empathy" — assuming you know user needs without fresh interviews. Your assumptions ≠ reality.

> **Templates**: See [SDLC-Design-Thinking-Templates.md](Documentation-Standards/SDLC-Design-Thinking-Templates.md) for interview scripts, empathy map canvas, and journey map template.

---

### Phase 2: DEFINE — Frame the Problem

**Purpose**: Synthesize empathy data into a clear, actionable problem statement.

| Element | Detail |
|---------|--------|
| **Key Activities** | Affinity clustering, problem statement formulation, HMW question generation, POV statements |
| **Outputs** | Problem statement, 3+ HMW questions, success criteria |
| **Time Budget** | 1 day per sprint cycle |
| **AI Assistance** | Pattern recognition, problem statement variations, HMW generation |

**Problem Statement Formula**:
```
[User persona] needs [a way to do something]
because [surprising insight from research],
but currently [barrier/frustration].
```

**HMW (How Might We) Rules**: Not too broad ("improve their life") — not too narrow ("add a blue button") — just right ("reduce attendance fraud without expensive hardware").

**Pitfall**: "Solution Before Problem" — jumping to solutions before defining the problem. Spend 2× time on Define vs Prototype.

> **Templates**: See [SDLC-Design-Thinking-Templates.md](Documentation-Standards/SDLC-Design-Thinking-Templates.md) for problem statement, POV, and HMW generator templates.

---

### Phase 3: IDEATE — Generate Solutions

**Purpose**: Explore the widest possible solution space before converging.

| Element | Detail |
|---------|--------|
| **Key Activities** | Brainstorming (50+ ideas), SCAMPER technique, Crazy 8s, cross-industry analogies, prioritization matrix |
| **Outputs** | 50+ raw ideas, prioritization matrix, top 3 concepts with rationale |
| **Time Budget** | 1 day per sprint cycle |
| **AI Assistance** | Bulk idea generation (30+), cross-domain analogies, challenge assumptions |

**Brainstorming Rules** (Stanford d.school): Defer judgment, encourage wild ideas, build on others ("Yes, AND..."), go for quantity (50+ in 30 min), be visual.

**Prioritization**: Use Impact × Effort matrix. Quick Wins (high impact, low effort) first. Avoid Money Pits (low impact, high effort).

**Pitfall**: Converging too early on the first "good" idea. Force quantity before quality.

> **Templates**: See [SDLC-Design-Thinking-Templates.md](Documentation-Standards/SDLC-Design-Thinking-Templates.md) for SCAMPER table, Crazy 8s template, and AI brainstorming prompts.

---

### Phase 4: PROTOTYPE — Build to Learn

**Purpose**: Create the minimum artifact needed to test your hypothesis — not a production feature.

| Element | Detail |
|---------|--------|
| **Key Activities** | Select fidelity level, build core workflow, prepare test plan |
| **Outputs** | Testable prototype, test plan with scenarios and success metrics |
| **Time Budget** | 2–3 days per sprint cycle |
| **AI Assistance** | UI generation (v0.dev), component scaffolding (Claude Code), rapid iteration |

**4 Fidelity Levels**:

| Level | What | When | Time |
|-------|------|------|------|
| **L1 Paper** | Sketches, wireframes | Early exploration | 30 min |
| **L2 Digital** | Clickable mockups | Concept validation | 2–4 hours |
| **L3 MVP** | Working code, real data | Usability testing | 2–5 days |
| **L4 Pilot** | Full feature, limited rollout | Business validation | 1–2 weeks |

**Core Principle**: Prototype fidelity matches learning goal. Build the minimum testable, not the minimum marketable.

**Pitfall**: "Overbuilt Prototype" — spending 2 months on pixel-perfect UI before validation. Timebox to 1 week max.

> **Templates**: See [SDLC-Design-Thinking-Templates.md](Documentation-Standards/SDLC-Design-Thinking-Templates.md) for prototype planning template and AI-assisted workflow.

---

### Phase 5: TEST — Validate with Users

**Purpose**: Verify your solution actually works for real users in realistic conditions.

| Element | Detail |
|---------|--------|
| **Key Activities** | Moderated user testing (5–8 users), think-aloud protocol, observation, feedback synthesis |
| **Outputs** | Test results, feedback categorization, iterate/pivot/ship decision |
| **Time Budget** | 1–2 days per sprint cycle |
| **AI Assistance** | Transcript analysis, pattern identification, feedback categorization |

**Feedback Categories**:

| Category | Priority | Action |
|----------|----------|--------|
| **Usability** (can't do) | HIGH if >50% affected | Fix before next test |
| **Confusion** (don't understand) | MEDIUM | Redesign or add guidance |
| **Preference** (want different) | LOW | Note for future |
| **Delight** (love it) | LEARN | Amplify the pattern |

**Decision Tree**:
- **>70% success** → ITERATE (refine details, ship soon)
- **30–70% success** → DIG DEEPER (more interviews, identify specific failures)
- **<30% success** → PIVOT (rethink approach, return to Ideate or Empathize)

**Pitfall**: "Confirmation Bias Testing" — only testing with friendly users. Test with skeptical users; measure behavior, not opinions.

> **Templates**: See [SDLC-Design-Thinking-Templates.md](Documentation-Standards/SDLC-Design-Thinking-Templates.md) for testing protocol, feedback analysis framework, and iterate-vs-pivot guide.

---

## DT × SDLC Stage Mapping

Design Thinking spans primarily the WHY (Stage 00) and WHAT (Stage 01) stages, but its influence extends through the entire lifecycle:

| SDLC Stage | DT Phase | Key Activity | Gate |
|------------|----------|-------------|------|
| **00 Foundation** (WHY) | EMPATHIZE + DEFINE | User interviews, problem framing, evidence collection | G0.1, G0.2 |
| **01 Planning** (WHAT) | DEFINE + IDEATE | Requirements from DT insights, solution exploration | G1 |
| **02 Design** (HOW) | IDEATE + PROTOTYPE | Architecture informed by user data, prototype-driven design | G2 |
| **03 Integrate** | PROTOTYPE | Integration patterns validated through prototyping | — |
| **04 Build** | PROTOTYPE + TEST | Build validated features, user testing during sprints | G3 |
| **05 Test** | TEST | Functional + usability testing, DT acceptance criteria | — |
| **06 Deploy** | TEST → ITERATE | Post-deploy user feedback loop | G4 |
| **07 Operate** | EMPATHIZE (continuous) | Monitor real usage patterns, new pain point discovery | — |
| **08 Collaborate** | All phases | Cross-team DT workshops, shared insights | — |
| **09 Govern** | TEST (metrics) | DT compliance checks, feature waste metrics | — |

**Key Insight**: DT is not a one-time pre-development activity. Stage 07 (Operate) feeds back into Stage 00 (Foundation) — creating a continuous empathy loop that reduces feature waste over time.

---

## The Iteration Loop

```
               EMPATHIZE
              ↗         ↘
         TEST              DEFINE
           ↑                  ↓
       PROTOTYPE ←──── IDEATE

  Inner loop: 3-5 iterations before shipping
  Outer loop: Post-launch (Stage 07 → Stage 00)
```

**When to iterate**:
- Test results show 30–70% success → refine and re-test
- User feedback reveals new pain points → update empathy map
- Business context changes → re-validate problem statement

**When to exit the loop**:
- Test results show >70% success on core tasks
- Gate 0.4 (User Validation) passes
- Diminishing returns on iteration (improvements <5% per cycle)

---

## Anti-Patterns

### 1. Fake Empathy
**Symptom**: "We already know what users want" without fresh interviews.
**Fix**: Conduct 5–10 fresh interviews per project. Observe behavior, not just opinions.

### 2. Solution Before Problem
**Symptom**: "Let's add AI chatbot" without knowing what problem it solves.
**Fix**: Write problem statement BEFORE ideating. Ask "What problem does this solve?" for every solution.

### 3. Overbuilt Prototype
**Symptom**: 2 months on pixel-perfect UI before any user testing.
**Fix**: Match fidelity to learning goal. Timebox to 1 week max before testing. Build minimum *testable*, not minimum *marketable*.

### 4. Confirmation Bias Testing
**Symptom**: Only testing with friends or fans; ignoring negative feedback.
**Fix**: Test with skeptical/critical users. Measure behavior ("Did they use it?"), not opinions ("Did they like it?").

### 5. One-Shot Design
**Symptom**: Design once, build exactly that, never iterate.
**Fix**: Expect 3–5 iterations before shipping. Continue iterating post-launch based on real usage data.

---

## Quality Gates 0.1 – 0.5

Design Thinking integrates with the SDLC Quality Gate system through 5 gates that progressively validate user-centered decisions:

### Gate 0.1: Problem Definition (After EMPATHIZE + DEFINE)

> "Have we defined the RIGHT problem?"

| Criteria | Evidence |
|----------|----------|
| Problem statement based on 5+ user interviews | Interview transcripts |
| Measurable success criteria defined | Problem statement document |
| Team alignment on the problem | Empathy map + journey map |

**Pass** → Proceed to IDEATE. **Fail** → More interviews. **Reject if**: Problem based on "we think" not "users said."

### Gate 0.2: Solution Validation (After IDEATE)

> "Are we exploring diverse solutions?"

| Criteria | Evidence |
|----------|----------|
| 50+ ideas generated before converging | Ideation session notes |
| Top 3 concepts address HMW questions | Prioritization matrix |
| Selection based on impact × effort, not gut feel | Concept sketches + rationale |

**Pass** → Proceed to PROTOTYPE. **Fail** → Generate more ideas. **Reject if**: Only one solution considered.

### Gate 0.3: Prototype Quality (After PROTOTYPE)

> "Is the prototype testable with users?"

| Criteria | Evidence |
|----------|----------|
| Core workflow functional (happy path works) | Working prototype |
| Fidelity appropriate for learning goal | Test plan document |
| Test plan defined (5–8 users, scenarios, metrics) | Learning objectives |

**Pass** → Proceed to TEST. **Fail** → Simplify prototype or improve test plan.

### Gate 0.4: User Validation (After TEST)

> "Did we validate with real users?"

| Criteria | Evidence |
|----------|----------|
| Tested with 5+ representative users | Session recordings/notes |
| Usability goals met (completion, time, satisfaction) | Synthesis document |
| Iteration plan evidence-based | Decision rationale |

**Pass** → Iterate, Pivot, or Ship. **Fail** → More testing. **Reject if**: No user testing conducted.

### Gate 0.5: Pre-Launch Readiness (Before SHIP)

> "Are we ready to ship to broader users?"

| Criteria | Evidence |
|----------|----------|
| User acceptance criteria met (from Define phase) | Final test results |
| Zero critical bugs | Technical QA report |
| Adoption plan defined (onboarding, support, monitoring) | Launch plan document |

**Pass** → Ship to production. **Fail** → Fix critical issues. **Reject if**: User testing skipped.

---

## Key Metrics

### Process Metrics (Track per project)
- **User interviews conducted**: Target 5–10 per persona
- **Iteration cycles before launch**: Target 3–5
- **Gate 0.1–0.5 first-pass rate**: Target 90%+

### Outcome Metrics (Track quarterly)
- **Feature adoption rate**: Target >70% (vs 30% industry average)
- **Feature waste**: Target <30% unused features (vs 60–70% baseline)
- **Time to first value**: Target <30 min for users
- **User satisfaction**: Target 4.5/5.0+

### Business Metrics (Track annually)
- **Development waste reduction**: 50%+ fewer unused features
- **Time to market**: 30%+ faster (prototype-to-ship)
- **Customer retention**: Target 80%+ (vs 60% without DT)

---

## Related Documents

### Core Methodology (Ring 1)
- [SDLC-System-Thinking-Foundation.md](SDLC-System-Thinking-Foundation.md) — Iceberg Model, mental models for root-cause analysis
- [SDLC-Crisis-To-Pattern-Methodology.md](SDLC-Crisis-To-Pattern-Methodology.md) — Converting DT-discovered issues into permanent policies
- [SDLC-Core-Methodology.md](SDLC-Core-Methodology.md) — 7-Pillar hub (Design Thinking = Pillar 0)
- [SDLC-Quality-Gates-Assurance-Framework.md](SDLC-Quality-Gates-Assurance-Framework.md) — Quality Assurance System (anti-vibecoding)

### Templates & Case Studies
- [SDLC-Design-Thinking-Templates.md](Documentation-Standards/SDLC-Design-Thinking-Templates.md) — All detailed templates, interview scripts, case study (AI Attendance System), workshop curriculum, AI tool integration guide

### AI Governance (Ring 1)
- [13-AGENTIC-CORE-PRINCIPLES.md](../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md) — 7 Agentic Principles, SE4H/SE4A framework
- [14-AGENTIC-MATURITY-MODEL.md](../03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md) — L0–L3 maturity progression

### Governance (Ring 2)
- [04-Governance-Compliance/SDLC-Quality-Gates-Framework.md](../04-Governance-Compliance/SDLC-Quality-Gates-Framework.md) — Full gate framework (G0–G4)

---

**Document**: SDLC Design Thinking Principles
**Version**: SDLC 6.3.0
**Status**: ACTIVE — Ready for Implementation
**Last Updated**: February 18, 2026

> *"Ask the RIGHT questions in the RIGHT order. That's more valuable than having the RIGHT tools."*
>
> — SDLC 6.3.0: WHY grounds you. WHAT focuses you. HOW structures you. BUILD validates you. GOVERN sustains you.
