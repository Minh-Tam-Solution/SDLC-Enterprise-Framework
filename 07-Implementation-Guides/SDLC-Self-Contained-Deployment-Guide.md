# SDLC 6.1.0 Self-Contained Deployment Guide

**Version**: 6.1.0
**Date**: January 27, 2026
**Status**: ACTIVE - CEO Requirement
**Authority**: CEO + CTO Office
**Purpose**: Enable any team member (AI or Human) to understand SDLC compliance from one folder
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles

---

## 🎯 CEO Requirement

> "Mọi thành viên của team (AI hay Human) chỉ cần truy cập một thư mục là có thể biết tuân thủ SDLC là gì trong mỗi tình huống cụ thể trong dự án"

**Translation**: Every team member (AI or Human) should only need to access ONE folder to understand SDLC compliance for any specific situation in the project.

**Target Folder**: `docs/08-Team-Management/03-SDLC-Compliance/`  
**Principle**: **Self-Contained** - No external dependencies, all guidance in one place

---

## 📋 Self-Contained Deployment Strategy

### Core Principle

**ONE FOLDER = COMPLETE SDLC KNOWLEDGE**

```
docs/08-Team-Management/03-SDLC-Compliance/
├── README.md                           ← Start here
├── Core-Methodology/                   ← What is SDLC 6.1.0?
├── SASE-Artifacts/                     ← How to work with AI agents?
├── Governance-Compliance/              ← What are the rules?
├── Documentation-Standards/            ← How to document?
├── Situation-Specific-Guides/          ← What to do in X situation? 🆕
└── Quick-Reference/                    ← Fast lookup 🆕
```

---

## 📁 Prerequisites

Before deploying SDLC Compliance folder, ensure your project has the correct `/docs` structure for your tier.

**See**: [SDLC-Implementation-Guide.md - Project Folder Structure](SDLC-Implementation-Guide.md#-project-folder-structure-mandatory) for complete folder structure requirements by tier.

> **Note**: The SDLC Self-Contained Compliance folder (`03-SDLC-Compliance/`) is typically placed in `08-collaborate/` for ENTERPRISE tier. For smaller tiers, adapt location appropriately (e.g., root `docs/` for STANDARD).

---

## 🏗️ Deployment Phases

### Phase 1: Foundation (Week 1)

**Create folder structure**:
```bash
cd docs/08-Team-Management/03-SDLC-Compliance/

mkdir -p Core-Methodology
mkdir -p SASE-Artifacts  
mkdir -p Governance-Compliance  # Already exists
mkdir -p Documentation-Standards
mkdir -p Situation-Specific-Guides
mkdir -p Quick-Reference
```

**Deploy core files**:
1. README.md (navigation hub)
2. Core-Methodology/ (15 files from SDLC Framework)
3. SASE-Artifacts/ (6 templates from SDLC Framework)

---

### Phase 2: Governance (Week 2)

**Deploy governance files** (if not exists):
```bash
Governance-Compliance/
├── README.md
├── SDLC-Quality-Gates.md
├── SDLC-Security-Gates.md
├── SDLC-Observability-Checklist.md
└── SDLC-Change-Management-Standard.md
```

**Adapt to project tier**:
- LITE: Minimal gates
- STANDARD: Basic gates
- PROFESSIONAL: Full gates (BFlow = this tier)
- ENTERPRISE: All gates + audit

---

### Phase 3: Documentation Standards (Week 2)

**Deploy documentation files**:
```bash
Documentation-Standards/
├── README.md
├── SDLC-Code-File-Naming-Standards.md
├── SDLC-Document-Naming-Standards.md
├── SDLC-Document-Header-Templates.md
└── Team-Collaboration/
    ├── SDLC-Team-Communication-Protocol.md
    ├── SDLC-Team-Collaboration-Protocol.md
    └── SDLC-Escalation-Path-Standards.md
```

---

### Phase 4: Situation-Specific Guides (Week 3) 🆕 KEY

**Purpose**: Answer "What do I do in this situation?"

```bash
Situation-Specific-Guides/
├── README.md
├── When-Starting-New-Feature.md
├── When-Reviewing-Code.md
├── When-Bug-Found.md
├── When-Security-Issue.md
├── When-Performance-Problem.md
├── When-Deploying-Production.md
├── When-AI-Agent-Helps.md
├── When-Writing-Documentation.md
├── When-Emergency-Hotfix.md
└── When-Onboarding-New-Member.md
```

**Each guide structure**:
```markdown
# When [Situation]

## Quick Answer (30 seconds)
- Step 1: ...
- Step 2: ...
- Step 3: ...

## Full Process (5 minutes)
- Detailed steps
- Quality gates to check
- Templates to use
- Examples

## SASE Integration (if applicable)
- SE4H (Human) creates: [artifacts]
- SE4A (Agent) creates: [artifacts]
- Validation: [checkpoints]

## Related Documents
- Link to core methodology
- Link to templates
- Link to examples
```

---

### Phase 5: Quick Reference (Week 3) �� KEY

**Purpose**: Fast lookup without reading full docs

```bash
Quick-Reference/
├── README.md
├── SDLC-Cheatsheet.md               ← 1-page overview
├── Quality-Gates-Checklist.md       ← Copy/paste checklist
├── Security-Gates-Checklist.md      ← Copy/paste checklist
├── SASE-Workflow-Diagram.md         ← Visual guide
├── File-Naming-Examples.md          ← Quick examples
├── Common-Scenarios-FAQ.md          ← Top 20 questions
└── Emergency-Contacts.md            ← Who to ask
```

---

## 📚 File Deployment Matrix

### From SDLC Framework to Project

| Source (SDLC Framework) | Destination (Project) | Adaptation Needed? |
|-------------------------|----------------------|-------------------|
| `02-Core-Methodology/SDLC-Core-Methodology.md` | `Core-Methodology/` | ✅ YES - Add project context |
| `02-Core-Methodology/SDLC-Agentic-*.md` | `Core-Methodology/` | ✅ YES - Add project examples |
| `05-Templates-Tools/SASE-Artifacts/*.md` | `SASE-Artifacts/` | ✅ YES - Customize for project |
| `02-Core-Methodology/Governance-Compliance/*` | `Governance-Compliance/` | ✅ YES - Adapt to tier |
| `02-Core-Methodology/Documentation-Standards/*` | `Documentation-Standards/` | ✅ YES - Project-specific |
| N/A (Create new) | `Situation-Specific-Guides/` | ✅ NEW - Project-specific |
| N/A (Create new) | `Quick-Reference/` | ✅ NEW - Project cheatsheets |

---

## 🎯 Adaptation Guidelines

### For Each File Deployed

**Step 1: Copy from Framework**
```bash
cp /path/to/SDLC-Framework/source.md \
   docs/08-Team-Management/03-SDLC-Compliance/destination/
```

**Step 2: Add Project Header**
```markdown
---
**SDLC Version**: 6.1.0
**Project**: [Your Project Name]
**Team Tier**: PROFESSIONAL | STANDARD | LITE | ENTERPRISE
**Adapted**: [Date]
**Original**: https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework
---
```

**Step 3: Add Project Context**
- Replace generic examples with project examples
- Add project-specific tools (e.g., "We use Figma MCP for design")
- Add team structure (e.g., "11 members: 6 Remote + 5 Local")
- Add project constraints (e.g., "Python 3.11+, FastAPI, PostgreSQL")

**Step 4: Simplify for Team**
- Remove enterprise-only sections if PROFESSIONAL tier
- Highlight what applies to your team size
- Add "For [Project Name]" annotations

**Step 5: Link Internally**
- Update all links to point to local files
- Add "See also: ../Other-Folder/Related-Doc.md"
- No external dependencies

---

## 🔍 Self-Contained Verification Checklist

### For Each Situation, Can Team Member Answer:

- [ ] **What**: What is SDLC compliance for this situation?
  - Found in: `Situation-Specific-Guides/When-*.md`

- [ ] **Why**: Why do we need this?
  - Found in: `Core-Methodology/SDLC-Core-Methodology.md`

- [ ] **How**: How do I implement this?
  - Found in: `Situation-Specific-Guides/` + templates

- [ ] **Quality**: What quality gates must pass?
  - Found in: `Governance-Compliance/SDLC-Quality-Gates.md`

- [ ] **Security**: What security requirements?
  - Found in: `Governance-Compliance/SDLC-Security-Gates.md`

- [ ] **SASE**: How do AI agents help?
  - Found in: `SASE-Artifacts/README.md` + templates

- [ ] **Examples**: Can I see an example?
  - Found in: `Quick-Reference/` + situation guides

- [ ] **Emergency**: What if urgent?
  - Found in: `Quick-Reference/Emergency-Contacts.md`

### Zero External Dependencies

- [ ] No links to external SDLC Framework repository
- [ ] No "see main SDLC docs" without copying them
- [ ] All templates included locally
- [ ] All checklists copy/pasteable
- [ ] All examples project-specific

---

## 📖 README.md Structure (Navigation Hub)

**Purpose**: Every team member starts here

```markdown
# SDLC 6.1.0 Compliance - [Project Name]

## 🚀 I want to...

### Start Something
- [x] Start a new feature → [When-Starting-New-Feature.md](Situation-Specific-Guides/When-Starting-New-Feature.md)
- [x] Onboard new member → [When-Onboarding-New-Member.md](Situation-Specific-Guides/When-Onboarding-New-Member.md)

### Work with Code
- [x] Review code → [When-Reviewing-Code.md](Situation-Specific-Guides/When-Reviewing-Code.md)
- [x] Fix a bug → [When-Bug-Found.md](Situation-Specific-Guides/When-Bug-Found.md)
- [x] Work with AI agent → [When-AI-Agent-Helps.md](Situation-Specific-Guides/When-AI-Agent-Helps.md)

### Ensure Quality
- [x] Check quality gates → [Quality-Gates-Checklist.md](Quick-Reference/Quality-Gates-Checklist.md)
- [x] Security review → [Security-Gates-Checklist.md](Quick-Reference/Security-Gates-Checklist.md)

### Deploy & Monitor
- [x] Deploy to production → [When-Deploying-Production.md](Situation-Specific-Guides/When-Deploying-Production.md)
- [x] Emergency hotfix → [When-Emergency-Hotfix.md](Situation-Specific-Guides/When-Emergency-Hotfix.md)

### Learn & Reference
- [x] SDLC overview → [SDLC-Cheatsheet.md](Quick-Reference/SDLC-Cheatsheet.md)
- [x] SASE workflow → [SASE-Workflow-Diagram.md](Quick-Reference/SASE-Workflow-Diagram.md)
- [x] Common questions → [Common-Scenarios-FAQ.md](Quick-Reference/Common-Scenarios-FAQ.md)

## 📚 Folders

- **Core-Methodology/** - What is SDLC 6.1.0?
- **SASE-Artifacts/** - How to work with AI agents?
- **Governance-Compliance/** - What are the rules?
- **Documentation-Standards/** - How to document?
- **Situation-Specific-Guides/** - What to do in X situation?
- **Quick-Reference/** - Fast lookup
```

---

## 🎓 Example: BFlow Platform Deployment

### BFlow Context
- **Team**: 11 members (6 Remote + 5 Local)
- **Tier**: PROFESSIONAL
- **Tech**: Python 3.11+, FastAPI, PostgreSQL, React
- **Timeline**: Jan-Feb 2026

### BFlow Adaptation Example

**Generic (SDLC Framework)**:
```markdown
## Quality Gates

Projects must implement quality gates appropriate to their tier.
```

**BFlow-Specific (Adapted)**:
```markdown
## Quality Gates for BFlow (PROFESSIONAL Tier)

**Our Team (11 members)** implements these gates:

1. **G0.1 Problem Definition** ✅ Required
   - ADR created in `docs/02-Design-Architecture/12-Architecture-Decisions/`
   - PM/PJM approval (Local Team)
   
2. **G3 Ship Ready** ✅ Required
   - FastAPI tests pass (pytest ≥80% coverage)
   - React tests pass (Vitest ≥70% coverage)
   - Security scan: Semgrep + Bandit (zero Critical/High)
   - Performance: API latency <50ms p50
   - 2+ code reviewers (GitHub PR)
```

---

## 🚦 Deployment Timeline (Generic Template)

### Week 1: Foundation
- Day 1-2: Create folder structure
- Day 3-4: Deploy Core-Methodology (15 files)
- Day 5: Deploy SASE-Artifacts (6 templates)

### Week 2: Standards
- Day 6-7: Deploy Governance-Compliance
- Day 8-9: Deploy Documentation-Standards
- Day 10: Team review & feedback

### Week 3: Practical Guides
- Day 11-13: Create Situation-Specific-Guides (10 guides)
- Day 14-15: Create Quick-Reference (7 resources)
- Day 16: Final validation

### Week 4: Training
- Day 17-18: Team training
- Day 19: Q&A session
- Day 20: Go-live

---

## ✅ Success Criteria

### Team Can Answer (Without Asking CTO):

1. ✅ "How do I start a new feature?" → Read `When-Starting-New-Feature.md`
2. ✅ "What quality gates for my PR?" → Read `Quality-Gates-Checklist.md`
3. ✅ "How to work with Claude Code?" → Read `When-AI-Agent-Helps.md` + SASE templates
4. ✅ "Emergency production bug!" → Read `When-Emergency-Hotfix.md`
5. ✅ "How to name this file?" → Read `File-Naming-Examples.md`

### Metrics:

- **Self-Service Rate**: 80%+ questions answered from folder
- **Onboarding Time**: New member productive in 1 day (vs 1 week)
- **Compliance Rate**: 95%+ PRs pass gates first time
- **AI Effectiveness**: 90%+ SASE artifacts correctly created

---

## 📞 Support Strategy

### Tier 1: Self-Service (80%)
→ `docs/08-Team-Management/03-SDLC-Compliance/` folder

### Tier 2: Quick Reference (15%)
→ `Quick-Reference/Common-Scenarios-FAQ.md`

### Tier 3: Team Ask (4%)
→ `Quick-Reference/Emergency-Contacts.md` (Slack, team leads)

### Tier 4: CTO Escalation (1%)
→ Complex architecture decisions only

---

## 🔄 Maintenance

### Monthly Review
- Update examples based on actual project use
- Add new situation guides as needed
- Refine quick reference based on FAQs

### Quarterly Update
- Sync with SDLC Framework updates (6.0.x, 6.1...)
- Add lessons learned
- Archive outdated content

### Annual Overhaul
- Major SDLC version upgrade (6.0)
- Team structure changes
- Tech stack evolution

---

## 📚 Related Documents

- **SDLC Framework**: https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework
- **SDLC Deployment Guide**: `07-Implementation-Guides/SDLC-Deployment-Guide.md`
- **Tier Classification**: `02-Core-Methodology/Documentation-Standards/SDLC-Tier-Stage-Requirements.md`

---

## 🎯 Key Takeaway

> **ONE FOLDER** = Complete SDLC knowledge for any situation
> 
> No need to search GitHub, ask CTO, or read 319 files.
> 
> Just go to `docs/08-Team-Management/03-SDLC-Compliance/` and find your answer.

---

**Document Owner**: CTO
**Last Updated**: January 29, 2026
**Next Review**: February 2026
**Framework**: SDLC 6.1.0
