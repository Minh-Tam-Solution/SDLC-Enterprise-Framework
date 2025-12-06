# 📋 3-Manual-Templates - Traditional Process Templates
## Backup Templates for SDLC 5.0.0 (Use When AI Unavailable)

**Version**: 5.0.0
**Date**: December 6, 2025
**Priority**: ⭐⭐ (BACKUP)
**Purpose**: Manual templates for when AI tools are unavailable or for training
**Status**: COMPLETE (9 templates for Stage 00-01)
**Recommendation**: Use [/1-AI-Tools/](../1-AI-Tools/) first (96% faster)

---

## 🎯 SDLC 5.0.0 Integration

### Stage Mapping

Manual templates primarily cover **Stage 00-01** (Design Thinking / Foundation):

| Stage | Name | Manual Templates | AI Alternative |
|-------|------|------------------|----------------|
| 00 | WHY? (Foundation) | Empathy Map, User Journey, Problem Statement | `design-thinking/*.md` |
| 01 | WHAT? (Planning) | POV Statement, HMW Questions, Ideation | `design-thinking/*.md` |
| 02-09 | Other Stages | See AI Tools | [/1-AI-Tools/](../1-AI-Tools/) |

### 4-Tier Classification

| Tier | Team Size | Manual Templates | Recommendation |
|------|-----------|------------------|----------------|
| **LITE** | 1-2 | Optional | Use AI tools only |
| **STANDARD** | 3-10 | For training only | AI first, manual backup |
| **PROFESSIONAL** | 10-50 | Hybrid approach | AI + manual validation |
| **ENTERPRISE** | 50+ | Audit documentation | Full suite for compliance |

---

## ⚠️ When to Use Manual Templates

### ✅ USE Manual Templates When:

**Scenario 1: AI Unavailable**
- No internet access
- Security-restricted environment
- Air-gapped systems

**Scenario 2: Learning & Training (All Tiers)**
- Teaching Design Thinking methodology
- New team onboarding
- Workshops and facilitation

**Scenario 3: Regulatory Requirements (PROFESSIONAL/ENTERPRISE)**
- Paper trail needed for audits
- Compliance documentation required
- SOC 2 / HIPAA evidence

**Scenario 4: Critical Validation (ENTERPRISE)**
- High-stakes decisions
- Stakeholder presentations
- Board-level documentation

### ❌ DON'T Use Manual Templates When:

- AI tools available (96% faster)
- Speed is critical (sprints, deadlines)
- Solo developer or small team
- Already familiar with methodology

---

## 📂 Directory Structure

```
3-Manual-Templates/
├── README.md                        # This file
└── design-thinking/                 # Stage 00-01: Stanford d.school templates
    ├── README.md                    # Comparison: Manual vs AI vs Hybrid
    │
    ├── Phase 1: Empathize (Stage 00)
    │   ├── Empathy-Map-Canvas-Template.md     # 8 hours (AI: 20 min)
    │   └── User-Journey-Map-Template.md       # 4 hours (AI: 20 min)
    │
    ├── Phase 2: Define (Stage 00-01)
    │   ├── Problem-Statement-Template.md      # 2 hours (AI: 5 min)
    │   ├── POV-Statement-Template.md          # 1 hour (AI: 5 min)
    │   └── HMW-Questions-Worksheet.md         # 1 hour (AI: 5 min)
    │
    ├── Phase 3: Ideate (Stage 01)
    │   └── Ideation-Brainstorming-Template.md # 3 hours (AI: 10 min)
    │
    ├── Phase 4: Prototype (Stage 01)
    │   └── Prototype-Test-Plan-Template.md    # 4 hours (AI: 25 min)
    │
    └── Phase 5: Test (Stage 01)
        ├── User-Testing-Script-Template.md    # 3 hours (AI: 25 min)
        └── Feedback-Analysis-Template.md      # 5 hours (AI: 10 min)
```

---

## ⏱️ Time Comparison by Approach

### Manual Approach (This Directory)

```yaml
Total Time: 26 hours per feature

Stage 00 (WHY?):
  Empathy Map: 8 hours
  User Journey: 4 hours
  Problem Statement: 2 hours
  POV Statement: 1 hour
  HMW Questions: 1 hour
  Subtotal: 16 hours

Stage 01 (WHAT?):
  Ideation: 3 hours
  Prototype Plan: 4 hours
  Testing Script: 3 hours
  Feedback Analysis: 5 hours
  Subtotal: 10 hours (overlap with 00)
```

### AI Approach (Recommended)

```yaml
Total Time: 1 hour per feature

Stage 00-01:
  empathy-synthesis.md: 20 minutes
  problem-statement.md: 5 minutes
  ideation-facilitator.md: 10 minutes
  prototype-validator.md: 25 minutes

TIME SAVINGS: 96% (25 hours saved)
```

### Hybrid Approach (Best Quality for ENTERPRISE)

```yaml
Total Time: 3-4 hours per feature

Stage 00:
  AI: Quick synthesis (20 min)
  Manual: Structured documentation (30 min)

Stage 01:
  AI: Generate ideas (15 min)
  Manual: Team workshop (60 min)
  AI: Validate approach (25 min)
  Manual: Detailed documentation (60 min)

TIME SAVINGS: 85-92% (22-23 hours saved)
QUALITY: Highest (AI speed + human validation)
```

---

## 📊 Usage by Tier

### LITE Tier (1-2 People)

```yaml
Recommendation: Skip manual templates
Use: AI tools only

Why:
  - Limited time available
  - No team for workshops
  - Maximum productivity needed
  - 96% time savings critical

Time Investment: 0 hours on manual
ROI: 26x faster with AI
```

### STANDARD Tier (3-10 People)

```yaml
Recommendation: Manual for training only

When to Use Manual:
  - Team onboarding (first 2 weeks)
  - Methodology workshops
  - New hire training

Production Use: AI tools
Training Use: Manual templates

Time Investment: 26 hours (one-time training)
ROI: Understanding + 96% faster execution after
```

### PROFESSIONAL Tier (10-50 People)

```yaml
Recommendation: Hybrid approach

Use Manual For:
  - Critical features (high stakes)
  - Stakeholder presentations
  - Compliance documentation
  - Cross-team workshops

Use AI For:
  - Daily development
  - Quick iterations
  - Time-sensitive features

Time Investment: 3-4 hours per feature (hybrid)
ROI: 85% savings + high quality
```

### ENTERPRISE Tier (50+ People)

```yaml
Recommendation: Full suite

Use Manual For:
  - Audit documentation
  - Regulatory compliance
  - Board presentations
  - Multi-team facilitation
  - SOC 2 / HIPAA evidence

Use AI For:
  - First draft generation
  - Quick iterations
  - Individual work

Time Investment: 3-4 hours (hybrid) or 26 hours (full manual)
ROI: Compliance + quality assurance
```

---

## 📋 Design Thinking Templates (Stage 00-01)

### Phase 1: Empathize (Stage 00 - WHY?)

**1. Empathy Map Canvas Template**
```yaml
File: design-thinking/Empathy-Map-Canvas-Template.md
Purpose: Synthesize user research into 4 quadrants
Time: 8 hours manual / 20 min AI
When: After user interviews

Sections:
  - THINK & FEEL: User thoughts and emotions
  - SEE: User environment and observations
  - SAY & DO: User actions and statements
  - HEAR: Influences and information sources
  - PAINS: Frustrations and obstacles
  - GAINS: Goals and motivations

AI Alternative: 1-AI-Tools/design-thinking/empathy-synthesis.md
```

**2. User Journey Map Template**
```yaml
File: design-thinking/User-Journey-Map-Template.md
Purpose: Map user touchpoints end-to-end
Time: 4 hours manual / 20 min AI
When: Understanding user experience

Sections:
  - User Persona Profile
  - Journey Stages (Awareness → Retention)
  - Touchpoints per stage
  - Pain Points and Emotions
  - Opportunities

AI Alternative: Included in empathy-synthesis.md
```

### Phase 2: Define (Stage 00-01 Transition)

**3. Problem Statement Template**
```yaml
File: design-thinking/Problem-Statement-Template.md
Purpose: Define problem with evidence
Time: 2 hours manual / 5 min AI
Format: [User] needs [need] because [insight]

Sections:
  - User Profile Summary
  - Key Needs (prioritized)
  - Evidence-Based Insights
  - Problem Statement Drafts
  - Validation Criteria

AI Alternative: 1-AI-Tools/design-thinking/problem-statement.md
```

**4. POV Statement Template**
```yaml
File: design-thinking/POV-Statement-Template.md
Purpose: Frame problem from user perspective
Time: 1 hour manual / 5 min AI

Sections:
  - User Definition
  - Need Description
  - Insight Synthesis
  - POV Statement
  - Challenge Identification

AI Alternative: Included in problem-statement.md
```

**5. HMW Questions Worksheet**
```yaml
File: design-thinking/HMW-Questions-Worksheet.md
Purpose: Reframe problems as opportunities
Time: 1 hour manual / auto-generated with AI

Format: "How Might We...?"
Examples:
  - HMW make [process] faster?
  - HMW reduce [pain point]?
  - HMW help users [goal]?

AI Alternative: Auto-generated in problem-statement.md
```

### Phase 3: Ideate (Stage 01 - WHAT?)

**6. Ideation Brainstorming Template**
```yaml
File: design-thinking/Ideation-Brainstorming-Template.md
Purpose: Generate 15+ solution ideas
Time: 3 hours manual / 10 min AI
Method: SCAMPER + Six Thinking Hats

Sections:
  - SCAMPER Analysis
  - Six Hats Perspectives
  - Idea Generation (15+ ideas)
  - Feasibility Scoring
  - Top 3 Selection

AI Alternative: 1-AI-Tools/design-thinking/ideation-facilitator.md
```

### Phase 4: Prototype (Stage 01)

**7. Prototype Test Plan Template**
```yaml
File: design-thinking/Prototype-Test-Plan-Template.md
Purpose: Plan prototype approach and validation
Time: 4 hours manual / 25 min AI

Sections:
  - Solution Description
  - Prototype Type (paper/digital/code)
  - Success Criteria
  - Test Scenarios
  - Resource Requirements

AI Alternative: 1-AI-Tools/design-thinking/prototype-validator.md
```

### Phase 5: Test (Stage 01)

**8. User Testing Script Template**
```yaml
File: design-thinking/User-Testing-Script-Template.md
Purpose: Structured testing protocol
Time: 3 hours manual / 25 min AI

Sections:
  - Participant Profile
  - Introduction Script
  - Task Scenarios (5-7 tasks)
  - Observation Checklist
  - Post-Task Questions
  - Wrap-Up Questions

AI Alternative: 1-AI-Tools/design-thinking/user-testing-analyzer.md
```

**9. Feedback Analysis Template**
```yaml
File: design-thinking/Feedback-Analysis-Template.md
Purpose: Synthesize testing feedback
Time: 5 hours manual / 10 min AI

Sections:
  - Participant Summary
  - Task Completion Rates
  - Success/Failure Patterns
  - User Quotes (verbatim)
  - Iteration Priorities
  - Recommendations

AI Alternative: Included in user-testing-analyzer.md
```

---

## 📊 ROI Analysis by Tier

### LITE Tier (Skip Manual)

```yaml
Manual Cost: 26 hours × $50/hr = $1,300
AI Cost: 1 hour × $50/hr + $20 tools = $70

Savings: $1,230 per feature (95%)
Annual (10 features): $12,300 saved

Recommendation: AI only (no manual)
```

### STANDARD Tier (Training + AI)

```yaml
Training Investment: 26 hours × $50/hr = $1,300 (one-time)
Production Cost: 1 hour × $50/hr + $20 = $70 per feature

Year 1: $1,300 + (10 × $70) = $2,000
Year 2+: 10 × $70 = $700

vs Manual: 10 × $1,300 = $13,000/year
Savings Year 1: $11,000 (85%)
Savings Year 2+: $12,300 (95%)

Recommendation: Train once, AI forever
```

### PROFESSIONAL Tier (Hybrid)

```yaml
Hybrid Cost: 3.5 hours × $50/hr + $20 = $195 per feature
Annual (10 features): $1,950

vs Manual: $13,000/year
Savings: $11,050 (85%)

Benefits:
  - High quality documentation
  - Stakeholder-ready output
  - Compliance artifacts

Recommendation: Hybrid for critical features
```

### ENTERPRISE Tier (Full Suite)

```yaml
Full Manual: For audits, $1,300/feature
Hybrid: For production, $195/feature

Annual Mix (5 audit + 5 production):
  Audit: 5 × $1,300 = $6,500
  Production: 5 × $195 = $975
  Total: $7,475

vs All Manual: $13,000
Savings: $5,525 (42%)

Benefits:
  - Audit-ready documentation
  - SOC 2 / HIPAA compliance
  - Board presentation quality

Recommendation: Full suite for compliance
```

---

## 🎓 Learning Path

### New to Design Thinking? (All Tiers)

```yaml
Week 1:
  - Read all 9 manual templates (4 hours)
  - Understand methodology structure

Week 2:
  - Do first feature manually (26 hours)
  - Experience full process

Week 3:
  - Learn AI prompts (2 hours)
  - Compare AI vs manual output

Week 4+:
  - Switch to AI or hybrid
  - Use manual for training others

Result: Methodology mastery + 96% faster execution
```

### Already Know Design Thinking?

```yaml
Day 1:
  - Skip manual templates
  - Go directly to: 1-AI-Tools/design-thinking/
  - Start using AI prompts

Result: 96% time savings from day 1
```

### Teaching a Team? (STANDARD+)

```yaml
Day 1 (8 hours):
  - Manual templates workshop
  - Hands-on practice

Day 2 (8 hours):
  - Real feature exercise
  - Full manual process

Week 2 (4 hours):
  - Introduce AI acceleration
  - Side-by-side comparison

Week 3 (4 hours):
  - Hybrid approach practice
  - Team workflow setup

Result: Team knows methodology + productivity tools
```

---

## 🔗 Related Resources

### Primary (Use First)

- **AI Tools**: [/1-AI-Tools/](../1-AI-Tools/) - 96% time savings
- **Design Thinking AI**: [/1-AI-Tools/design-thinking/](../1-AI-Tools/design-thinking/)

### Secondary

- **Agent Templates**: [/2-Agent-Templates/](../2-Agent-Templates/)
- **Scripts**: [/4-Scripts/](../4-Scripts/)

### Reference

- **Core Methodology**: [/02-Core-Methodology/](../../02-Core-Methodology/)
- **SDLC 5.0.0 Overview**: [/00-Overview/](../../00-Overview/)

---

## ✅ Quick Decision Guide

| Situation | Use | Time |
|-----------|-----|------|
| Solo developer | AI only | 1 hour |
| Small team (production) | AI only | 1 hour |
| Team training | Manual | 26 hours |
| Critical feature | Hybrid | 3-4 hours |
| Audit documentation | Manual | 26 hours |
| Regulatory compliance | Hybrid/Manual | 3-26 hours |
| Stakeholder presentation | Hybrid | 3-4 hours |

---

**Folder Status**: BACKUP - SDLC 5.0.0 Complete
**Last Updated**: December 6, 2025
**Owner**: CPO Office

***"Manual templates teach, AI accelerates, hybrid delivers both."*** 🎯

***"Use AI first, fall back to manual when needed."*** ⚡
