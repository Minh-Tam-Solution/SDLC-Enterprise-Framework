# 🛠️ SDLC 5.0.0 Framework Scripts & Automation Tools
## Battle-Tested Automation from Real Platform Experience

**Version**: 5.0.0 - Complete 10-Stage Lifecycle + Team Collaboration Standards
**Status**: ACTIVE - CORE SCRIPTS OPERATIONAL
**Date**: December 5, 2025
**Foundation**: Tools proven on BFlow, NQH-Bot, MTEP (3 platforms)
**Philosophy**: Build when needed + AI tools for flexibility

---

## 🆕 What's New in SDLC 5.0.0

### Team Collaboration Standards Validation (NEW)
`sdlc_validator.py` now validates Team Collaboration documents:
- **SDLC-Team-Communication-Protocol.md** - Tiered communication requirements
- **SDLC-Team-Collaboration-Protocol.md** - RACI matrices, handoff protocols
- **SDLC-Escalation-Path-Standards.md** - 4-level escalation framework

### 4-Tier Classification Support (NEW)
Validation adapts based on project tier:
| Tier | Team Size | Team Collaboration Required |
|------|-----------|---------------------------|
| LITE | 1-2 | Optional |
| STANDARD | 3-10 | Basic communication protocol |
| PROFESSIONAL | 10-50 | Full team collaboration |
| ENTERPRISE | 50+ | All + SLA enforcement |

### Code File Naming Standards (from 5.0.0)
- **Python**: `snake_case`, max 50 chars (e.g., `user_service.py`)
- **TypeScript**: `camelCase`, max 50 chars (e.g., `userService.ts`)
- **React**: `PascalCase`, max 50 chars (e.g., `UserDashboard.tsx`)

See `compliance/sdlc_validator.py` for complete validation.

---

## 🎯 What's Operational in SDLC 5.0.0

### ✅ Core Compliance Validators (READY)
```bash
compliance/
├── sdlc_validator.py                 # ⭐ PRIMARY: Complete 10-stage + 6-pillar + Team Collaboration validation
├── design_thinking_validator.py      # ✨ Pillar 0 validation (5 DT phases)
└── sdlc_scanner.py                   # Backward compatibility wrapper
```

**SDLC 5.0.0 Enhancement**: `sdlc_validator.py` now includes:
- Team Collaboration Standards validation (Pillar 2)
- 4-Tier Classification awareness
- Code File Naming validation (Python, TypeScript, React)

### ✅ Quick-Start Setup (PARTIAL)
```bash
quick-start/
└── solo_setup.py                     # ✅ Solo developer (2 days → 10x)
    # startup/growth/enterprise: Implement when demanded
```

### ✅ AI Tools (COMPLETE)
```bash
ai-tools/                              # Universal AI integration patterns
├── design-to-code/                   # Any design tool → Any framework
├── design-thinking/                  # 5-phase methodology with AI
├── code-review/                      # 3-tier review automation
└── platform-examples/                # Real implementation examples
```

**See**: `/06-Templates-Tools/ai-tools/README.md` for complete AI tooling

---

## 🚀 Quick Start

### Essential Commands (Use These Daily)

```bash
# 1. SDLC 5.0.0 Complete 10-Stage + Team Collaboration Validation
python3 scripts/compliance/sdlc_validator.py .

# 2. Design Thinking Compliance (Pillar 0)
python3 scripts/compliance/design_thinking_validator.py .

# 3. Backward Compatible Scan
python3 scripts/compliance/sdlc_scanner.py . [solo|startup|growth|enterprise]

# 4. Quick Start Solo Project
python3 scripts/quick-start/solo_setup.py /path/to/project
```

### For Everything Else: Use AI Tools

**Design-to-Code** (5-10 min):
```bash
# See: /ai-tools/design-to-code/universal-prompts.md
"Convert [design tool] to [framework] with SDLC 5.0 compliance"
```

**Design Thinking** (5 min per phase):
```bash
# See: /ai-tools/design-thinking/
"[Phase] for [problem] with [context]"
```

**Code Review** (5-10 min):
```bash
# See: /ai-tools/code-review/
"Review [code] for SDLC 5.0 compliance"
```

---

## 📂 Current Structure

```
4-Scripts/
├── README.md                         # This file
│
├── compliance/                       # ✅ OPERATIONAL
│   ├── sdlc_validator.py            # Complete 10-stage + 6-pillar + file naming validation
│   ├── design_thinking_validator.py  # Pillar 0 validation (5 DT phases)
│   └── sdlc_scanner.py              # Backward compatibility
│
└── quick-start/                      # ⚠️ PARTIAL
    └── solo_setup.py                # Solo developer setup (READY)
        # Others: Implement when demanded
```

**Note**: SDLC 5.0.0 now includes Code File Naming Standards validation in `sdlc_validator.py`

---

## 🎯 Key Scripts Explained

### SDLC 5.0.0 Complete Validator ✅

**Validates complete 10-stage lifecycle + 6-pillar architecture + code file naming**

```bash
# Usage
python3 compliance/sdlc_validator.py /path/to/project

# What it checks:
## 10-Stage Lifecycle:
- Stage 00 (WHY): Problem validation, user research
- Stage 01 (WHAT): Requirements, acceptance criteria
- Stage 02 (HOW): Architecture, design decisions
- Stage 03 (BUILD): Implementation, code quality
- Stage 04 (TEST): Test coverage, UAT completion
- Stage 05 (DEPLOY): Deployment readiness, rollback plan
- Stage 06 (OPERATE): Monitoring, incident response
- Stage 07 (INTEGRATE): API contracts, integration tests
- Stage 08 (COLLABORATE): Documentation, team alignment
- Stage 09 (GOVERN): Compliance, audit trail

## 6-Pillar Architecture:
- Pillar 0: Design Thinking methodology applied
- Pillar 1: Zero Mock Policy compliance
- Pillar 2: AI+Human Orchestration patterns
- Pillar 3: Quality Governance with Code Review
- Pillar 4: Documentation Permanence standards
- Pillar 5: Continuous Compliance monitoring

## Code File Naming (NEW in 5.0.0):
- Python files: snake_case, max 50 chars
- TypeScript files: camelCase, max 50 chars
- React components: PascalCase, max 50 chars
- Alembic migrations: {rev}_{desc}.py, max 60 chars

# Output example:
✅ Stage 00-03 (WHY→BUILD): COMPLIANT
✅ Stage 04-09 (TEST→GOVERN): COMPLIANT
✅ Pillar 0-5 (All Pillars): COMPLIANT
✅ File Naming Standards: COMPLIANT
🎉 SDLC 5.0.0 FULLY COMPLIANT (10 stages + 6 pillars + file naming)
```

### Design Thinking Validator ✨ NEW

**Ensures 5-phase methodology compliance**

```bash
# Usage
python3 scripts/compliance/design_thinking_validator.py /path/to/project

# What it validates:
- Phase 1 (Empathize): User research documented
- Phase 2 (Define): Problem statement validated
- Phase 3 (Ideate): Solution generation evidence
- Phase 4 (Prototype): Rapid validation performed
- Phase 5 (Test): User testing completed

# Output example:
✅ Phase 1 (Empathize): User research documented
✅ Phase 2 (Define): Problem statement validated
✅ Phase 3 (Ideate): 15 solutions generated
✅ Phase 4 (Prototype): Rapid prototype created
✅ Phase 5 (Test): User validation completed
📊 Design Thinking Score: 96% (NQH-Bot level)
```

### Solo Setup Script ✅

**2 days to 10x productivity for solo developers**

```bash
# Usage
python3 scripts/quick-start/solo_setup.py /path/to/project

# What it does:
1. Creates SDLC 5.0 complete 10-stage structure
2. Installs compliance validators (10-stage + 6-pillar)
3. Sets up Design Thinking templates (5 phases)
4. Configures Code Review Tier 1 (Manual)
5. Creates AI development environment
6. Sets performance targets (<50ms API, <2s page)
7. Initializes documentation structure
8. Sets up monitoring and governance templates

# Timeline: 2 days to 10x productivity
# Cost: $0-50/month (free tier focus)
# Stages Covered: All 10 stages (WHY → GOVERN)
```

---

## 💻 Why So Few Scripts?

### Modern Approach: AI Tools + Core Validators

**Traditional MTS SDLC Framework** (Before 5.0):
```
❌ 31 custom scripts for every scenario
❌ High maintenance overhead
❌ Platform-specific implementations
❌ Rigid, inflexible automation
```

**SDLC 5.0 Approach**:
```
✅ 3 core validators (Python scripts)
✅ 1 quick-start setup (Python script)
✅ Universal AI tools (prompts + patterns)
✅ Case studies for patterns
✅ Playbooks for crisis response
```

### Coverage Comparison

| Need | Traditional | SDLC 5.0 | Result |
|------|------------|----------|---------|
| Validation | Python script | Python script | ✅ SAME |
| Design Thinking | Python scripts (6) | AI prompts | ✅ BETTER |
| Code Review | Python scripts (5) | AI tools + configs | ✅ BETTER |
| Patterns | Python scripts (4) | Case studies | ✅ BETTER |
| Crisis | Python scripts (4) | Playbooks | ✅ BETTER |

**Functional Coverage**: 100% with 87% fewer scripts to maintain!

---

## 📊 Implementation Status

### What's Implemented ✅

| Script | Status | Use Case |
|--------|--------|----------|
| `sdlc_validator.py` | ✅ READY | Daily 10-stage + 6-pillar compliance |
| `design_thinking_validator.py` | ✅ READY | Pillar 0 validation (5 DT phases) |
| `sdlc_scanner.py` | ✅ READY | Backward compatibility |
| `solo_setup.py` | ✅ READY | Solo developer 10-stage onboarding |

### What's Covered by AI Tools 🤖

| Need | Alternative | Location |
|------|-------------|----------|
| Design-to-code | AI prompts | `/ai-tools/design-to-code/` |
| Design Thinking phases | AI prompts | `/ai-tools/design-thinking/` |
| Code Review tiers | AI prompts | `/ai-tools/code-review/` |
| Pattern extraction | Case studies | `/07-Case-Studies/` |
| Crisis response | Playbooks | `/03-Implementation-Guides/` |

### What's Demand-Driven 📋

| Script | Status | Implementation Trigger |
|--------|--------|----------------------|
| `startup_setup.py` | TEMPLATE | When 3+ startups request |
| `growth_setup.py` | TEMPLATE | When 3+ growth teams request |
| `enterprise_setup.py` | TEMPLATE | When 3+ enterprises request |

**Philosophy**: Build when needed, not when imagined

---

## 💡 Usage Patterns

### Daily Development

```bash
# Morning: Start work
cd /path/to/project
python3 path/to/sdlc_validator.py .

# During: Use AI for tasks
# - Design-to-code: AI prompts
# - Code review: AI-assisted
# - Problem solving: AI pair programming

# Evening: Validate before commit
python3 path/to/design_thinking_validator.py .
python3 path/to/sdlc_validator.py .
```

### New Project Setup

```bash
# Solo Developer (Day 1)
python3 scripts/quick-start/solo_setup.py /path/to/new-project

# Follow 2-day timeline in script output
# Day 1: Setup + First feature with 10-stage methodology
# Day 2: Development + Quality checks across all stages

# Result: 10x productivity with complete lifecycle coverage
```

### Feature Development

```bash
# 1. Design Thinking (1 hour with AI)
# See: /ai-tools/design-thinking/ for prompts
# - Empathize: Synthesize user research
# - Define: Generate problem statement
# - Ideate: 15+ solutions in minutes
# - Prototype: Rapid validation
# - Test: User feedback analysis

# 2. Implementation (AI-assisted)
# See: /ai-tools/design-to-code/ for prompts
# - Convert designs to code (5-10 min/component)
# - Generate tests (automatic)
# - Review with AI (5-10 min)

# 3. Validation (automated)
python3 scripts/compliance/design_thinking_validator.py .
python3 scripts/compliance/sdlc_validator.py .

# Total: Hours instead of days, all 10 stages covered
```

---

## 🎯 Success Stories

### Scripts That Work

1. **SDLC 5.0 Validator**: Enforces all 6 pillars across 3 platforms
2. **Design Thinking Validator**: Achieved 96% time savings on NQH-Bot
3. **Solo Setup**: 2 days to 10x productivity proven

### AI Tools That Replace Scripts

1. **Design-to-Code**: 95% time savings (2-4 hours → 5-10 min)
2. **Design Thinking AI**: 96% time savings (26 hours → 1 hour)
3. **Code Review AI**: 498% ROI with Tier 3 automation

### Why This Approach Wins

```yaml
Maintenance:
  31 Scripts: 31 files to maintain, update, debug
  4 Scripts + AI: 4 files + flexible AI prompts
  Reduction: 87% less maintenance overhead

Flexibility:
  Scripts: Fixed logic, requires code changes
  AI Tools: Natural language, adapts to context
  Result: AI tools handle edge cases better

Coverage:
  Scripts Only: 31 scripts = limited scenarios
  Scripts + AI: 4 scripts + infinite AI flexibility
  Result: Better coverage with less code

ROI:
  Scripts: High development + maintenance cost
  AI Tools: Low cost, high flexibility
  Result: 10x-50x productivity vs traditional automation
```

---

## 📚 Complete Documentation

### Core Scripts
- **SDLC Validator**: [sdlc_validator.py](compliance/sdlc_validator.py) - 10-stage + 6-pillar validation
- **Design Thinking**: [design_thinking_validator.py](compliance/design_thinking_validator.py) - Pillar 0 (5 DT phases)
- **Solo Setup**: [solo_setup.py](quick-start/solo_setup.py) - Complete 10-stage onboarding

### AI Tools (Recommended for Most Tasks)
- **Design-to-Code**: [/ai-tools/design-to-code/](../ai-tools/design-to-code/)
- **Design Thinking**: [/ai-tools/design-thinking/](../ai-tools/design-thinking/)
- **Code Review**: [/ai-tools/code-review/](../ai-tools/code-review/)

### Alternative Resources
- **Case Studies**: [/07-Case-Studies/](../../07-Case-Studies/)
- **Implementation Guides**: [/03-Implementation-Guides/](../../03-Implementation-Guides/)
- **Crisis Response**: [SDLC-5.0-Crisis-Response-Guide.md](../../03-Implementation-Guides/SDLC-5.0-Crisis-Response-Guide.md)

---

## 🔧 Contributing Scripts

### Before Creating a New Script

1. **Check AI Tools**: Can AI prompts solve this?
2. **Check Alternatives**: Is there a guide/case study?
3. **Prove Demand**: Do 3+ projects need this?
4. **Calculate ROI**: Will it save 10x+ time?

### When to Create a Script

✅ **CREATE WHEN**:
- Core validation logic (not replaceable by AI)
- Frequently repeated automation (daily use)
- Clear 10x+ time savings
- Universal need (not platform-specific)

❌ **DON'T CREATE WHEN**:
- AI prompts can handle it
- One-time or rare use case
- Platform-specific need
- Unclear ROI

### Script Requirements

If creating a new script:
- Must follow SDLC 5.0 template
- Must be universal (no platform-specific code)
- Must have 80%+ test coverage
- Must include complete documentation
- Must show proven demand (3+ projects)

---

## 📞 Support & Contribution

### Get Help
- **Scripts**: See this README and script docstrings
- **AI Tools**: See `/06-Templates-Tools/ai-tools/`
- **Case Studies**: See `/07-Case-Studies/`
- **CPO Office**: taidt@mtsolution.com.vn

### Request a Script

If you need automation that doesn't exist:

1. Open issue with:
   - **Use Case**: Specific scenario
   - **Frequency**: How often needed (daily/weekly/monthly)
   - **ROI**: Time currently spent vs expected savings
   - **Why AI Insufficient**: What AI tools can't do

2. Proof of demand:
   - Show 3+ projects with same need
   - Calculate time savings (>10x target)
   - Explain why AI tools insufficient

3. We'll evaluate and implement if justified

### Contribute a Script

1. Follow contribution guidelines
2. Prove demand from community
3. Show ROI calculation
4. Keep universal approach
5. Include tests and docs

---

## 🎯 Quick Reference

### Daily Commands

```bash
# Validate SDLC 5.0 compliance (10 stages + 6 pillars)
python3 scripts/compliance/sdlc_validator.py .

# Validate Design Thinking (Pillar 0, 5 phases)
python3 scripts/compliance/design_thinking_validator.py .

# For everything else: Use AI
# See: /ai-tools/ for prompts
```

### New Project Setup

```bash
# Solo Developer (Complete 10-stage setup)
python3 scripts/quick-start/solo_setup.py /path/to/project

# Startup/Growth/Enterprise
# Implement these when demanded by 3+ projects
```

---

**Status**: CORE SCRIPTS OPERATIONAL + AI TOOLS COMPLETE
**Coverage**: 100% functional coverage with 87% fewer scripts
**Philosophy**: Build when needed + AI for flexibility = Optimal balance
**Result**: Lean, maintainable, highly effective automation

***"4 scripts + AI > 31 scripts alone."*** 🤖

***"Validate with code, automate with AI."*** ⚡

***"Build when needed, not when imagined."*** 🎯

***"Functional coverage beats script count."*** ✅

---

**For Implementation Status**: See [SCRIPTS-STATUS-NOV7-2025.md](SCRIPTS-STATUS-NOV7-2025.md)
**For AI Tools**: See [/06-Templates-Tools/ai-tools/README.md](../ai-tools/README.md)
