# SDLC Visual Documentation Standards

**Version**: 6.1.2
**Date**: February 2, 2026
**Status**: ACTIVE
**Framework**: SDLC 6.1.2
**Ring**: 1 (Core - Timeless Standards)
**Source**: Consolidated from RFC-SDLC-607 (Boris Cherny Tactic #5)

---

## Overview

Visual documentation (ASCII diagrams, HTML presentations) explains architectural decisions and workflows far better than text alone. This standard defines how to create **explanatory documentation** that reduces onboarding time from **2 hours to 30 minutes**.

### Problem Addressed

Technical documentation is typically **text-heavy markdown** without visual aids. New team members spend hours reading to understand what a single diagram could explain in minutes.

**Visual memory > text memory** - Diagrams explain complex systems faster.

---

## Output Formats

### Format 1: ASCII Diagrams

**Use Cases**: Architecture, sequences, decision trees, workflows

**Benefits**:
- **Universal**: Plain text, works everywhere
- **Git-friendly**: Diffs show changes clearly
- **AI-parseable**: Any AI tool can generate/read
- **Zero dependencies**: No special rendering needed

**Example**: Progressive Routing Zones

```
┌──────────────────────────────────────────┐
│   Progressive Routing Zones              │
├──────────────────────────────────────────┤
│ 🟢 GREEN (0-30)  - Auto-approve          │
│ 🟡 YELLOW (30-60) - Quick review         │
│ 🟠 ORANGE (60-80) - Deep review          │
│ 🔴 RED (80+)     - Full audit            │
└──────────────────────────────────────────┘
```

**ASCII Diagram Library**:
- **Box Drawing**: Unicode characters (┌─┐│└┘)
- **Arrows**: Unicode arrows (→ ← ↑ ↓ ↔)
- **Emojis**: Zone indicators (🟢 🟡 🟠 🔴)
- **Bullets**: • ◦ ▪ ▫

### Format 2: Sequence Diagrams

**Use Cases**: API flows, authentication, user journeys

**Example**: Authentication Flow

```
User          Frontend        Backend         Database
 │               │               │               │
 │ 1. Login      │               │               │
 ├──────────────>│               │               │
 │               │ 2. POST /auth/login           │
 │               ├──────────────>│               │
 │               │               │ 3. Query user │
 │               │               ├──────────────>│
 │               │               │<──────────────┤
 │               │               │ 4. bcrypt verify
 │               │               │               │
 │               │ 5. JWT token  │               │
 │               │<──────────────┤               │
 │ 6. Token      │               │               │
 │<──────────────┤               │               │
 │               │               │               │
```

### Format 3: HTML Presentations

**Use Cases**: Onboarding, decision timelines, training materials

**Benefits**:
- **Interactive**: Click to see full decision
- **Timeline view**: See decision history visually
- **Slide deck**: Present to stakeholders

**Example Structure**:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Project Decision Timeline</title>
</head>
<body>
  <section class="slide">
    <h1>Gate G1: Legal + Market Validation</h1>
    <p>Decision: Proceed with open-source Apache-2.0</p>
    <p>Date: Nov 15, 2025</p>
  </section>
  <!-- More slides -->
</body>
</html>
```

---

## When to Use Visual Documentation

| Scenario | Format | Priority |
|----------|--------|----------|
| **Onboarding new team members** | ASCII + Markdown | HIGH |
| **Architecture review** | ASCII Diagram | HIGH |
| **Decision history** | HTML Timeline | MEDIUM |
| **API documentation** | Sequence Diagram | HIGH |
| **Workshop/Training** | HTML Slides | MEDIUM |
| **Sprint retrospective** | Decision tree | MEDIUM |

---

## Creation Guidelines

### Manual Creation

**Tools**:
- **asciiflow.com** - Web-based ASCII diagram editor
- **PlantUML** - Text-to-diagram converter (requires Java)
- **Mermaid.js** - Markdown diagram syntax (GitHub renders)
- **draw.io (diagrams.net)** - Export to ASCII via copy-paste

**Process**:
1. Sketch diagram concept on paper
2. Use ASCII flow tool to create diagram
3. Embed in markdown documentation
4. Link to Evidence artifacts for traceability

### AI-Generated

**Prompt Examples**:
```
"Create an ASCII diagram showing the authentication flow with 4 components: User, Frontend, Backend, Database"

"Generate a decision tree diagram in ASCII format for the Progressive Routing zones (Green/Yellow/Orange/Red)"

"Create a sequence diagram showing the PR review workflow from submission to merge"
```

---

## Documentation Standards

### Diagram Headers

Every diagram should include:
```markdown
## Authentication Flow

**Format**: ASCII Sequence Diagram
**Version**: 6.1.2
**Date**: 2026-02-02
**Source**: Design specification (SPEC-042)
**Evidence**: EVD-2026-02-042

[Diagram here]

**Components**:
- User: End user submitting credentials
- Frontend: React application
- Backend: FastAPI authentication service
- Database: PostgreSQL user store
```

### Traceability

All diagrams must reference Evidence artifacts:
```markdown
## Evidence Artifacts Referenced

- EVD-2026-01-042: Progressive Routing assessment decision
- EVD-2026-02-015: E2E Testing completion evidence
- EVD-2026-03-001: User auth implementation plan

## Approval
- Architect: @architect_name (2026-02-02)
- CTO: @cto_name (2026-02-02)
```

### Update Frequency

| Diagram Type | Update Trigger |
|--------------|----------------|
| **Architecture** | Major design changes (Gate G2) |
| **Sequence diagrams** | API contract changes |
| **Decision trees** | Policy updates |
| **Timelines** | Monthly (or after major milestones) |

---

## Benefits

### Onboarding Speed

**Before** (Text-only):
- New developer reads 50 pages of documentation
- Time: 2 hours
- Retention: Low (text overload)

**After** (Visual + Text):
- New developer sees 5 diagrams + 10 pages summary
- Time: 30 minutes
- Retention: High (visual memory)

**Result**: **4x faster onboarding**

### Knowledge Retention

**Research**: Visual memory is 60% better than text memory
- Diagrams explain tradeoffs clearly
- Decision context preserved visually
- Easier to spot architectural issues

### Decision Clarity

**Architecture decisions** become clearer with diagrams:
- Why X was chosen over Y (decision tree)
- How components interact (sequence diagram)
- When decisions were made (timeline)

---

## Implementation Checklist

### For New Projects

- [ ] Create `docs/09-govern/Diagrams/` directory
- [ ] Document architecture with ASCII diagrams
- [ ] Create authentication flow sequence diagram
- [ ] Add decision timeline (HTML if needed)
- [ ] Link all diagrams to Evidence artifacts

### For Existing Projects

- [ ] Audit existing documentation for missing visuals
- [ ] Identify top 5 complex concepts to visualize
- [ ] Create ASCII diagrams for architecture
- [ ] Add sequence diagrams for critical flows
- [ ] Update onboarding guide with visual aids

---

## Examples Library

### Architecture Diagram Template

```
┌─────────────────────────────────────────────────────┐
│              System Architecture                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────┐      ┌─────────────┐              │
│  │  Frontend   │─────>│  API Gateway │              │
│  │   (React)   │      │  (FastAPI)  │              │
│  └─────────────┘      └──────┬──────┘              │
│                               │                     │
│         ┌─────────────────────┼─────────────┐       │
│         ▼                     ▼             ▼       │
│  ┌──────────┐         ┌──────────┐   ┌──────────┐  │
│  │ Auth Svc │         │ Data Svc │   │ File Svc │  │
│  └────┬─────┘         └────┬─────┘   └────┬─────┘  │
│       │                    │              │        │
│       ▼                    ▼              ▼        │
│  ┌──────────────────────────────────────────────┐  │
│  │          PostgreSQL Database                 │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Decision Tree Template

```
                    Feature Request
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
    Complexity < 30?              Complexity ≥ 30?
          │                               │
          │ YES                           │ NO
          ▼                               ▼
    🟢 AUTO-APPROVE                   More checks...
    (No review needed)                     │
                                  ┌────────┴────────┐
                                  ▼                 ▼
                          30-60?              60-80?
                              │                 │
                         🟡 QUICK           🟠 DEEP
                         (15 min)          (1 hour)
```

---

## Complementary Tools

**Rendering Tools** (Optional):
- **Mermaid.js**: GitHub/GitLab render automatically
- **PlantUML**: Generate PNG/SVG from text
- **Graphviz**: Programmatic graph generation

**When to Use**:
- ASCII insufficient (complex diagrams)
- Need high-quality exports (presentations)
- Interactive features required (zoom, click)

**When NOT to Use**:
- Simple diagrams (ASCII is faster)
- Git-friendly diffs needed (binary images don't diff)
- No rendering dependencies desired

---

## Related Standards

- [SDLC-Naming-Standards.md](./SDLC-Naming-Standards.md) - Document naming conventions
- [SDLC-Project-Structure-Standard.md](./SDLC-Project-Structure-Standard.md) - Folder structure
- [SDLC-Team-Collaboration.md](./SDLC-Team-Collaboration.md) - Communication standards

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Framework**: SDLC 6.1.2
**Ring**: 1 (Core - Timeless Standards)
**Source**: Consolidated from RFC-SDLC-607 (Boris Cherny Tactic #5)
**Owner**: Engineering + Documentation Team
**Approval**: CTO @nqh ✅
