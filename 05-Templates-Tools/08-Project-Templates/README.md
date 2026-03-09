# Project Templates

**Version**: 6.1.2
**Date**: January 22, 2026
**Stage**: 05 - TEMPLATES & TOOLS
**Pillar**: 2 - Sprint Planning Governance (Planning Templates)
**Status**: ACTIVE - Production Templates
**Authority**: CTO + CPO Office
**Framework**: SDLC 6.1.2 (7-Pillar Architecture)
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) principles

---

## Purpose

This folder contains ready-to-use templates for setting up new SDLC projects. Templates are designed to reduce setup time and ensure consistency across projects.

**Target**: New project setup in <30 minutes (STANDARD tier)

---

## Templates Overview

| Template | Purpose | Tier Required | Setup Time |
|----------|---------|---------------|------------|
| [AI-ONBOARDING-TEMPLATE.md](AI-ONBOARDING-TEMPLATE.md) | CLAUDE.md for AI assistants | STANDARD+ | 30-60 min |
| [PLANNING-HIERARCHY-TEMPLATE/](PLANNING-HIERARCHY-TEMPLATE/) | 4-level planning (Roadmap→Backlog) | STANDARD+ | 1-2 hours |

---

## Quick Start by Tier

### LITE Tier (1-2 people, <$50K)

Minimal templates needed:
```bash
# Only need README.md (not from templates)
# Optional: Copy AI-ONBOARDING-TEMPLATE.md as CLAUDE.md
```

### STANDARD Tier (3-10 people, $50-200K)

```bash
# Copy AI onboarding template
cp AI-ONBOARDING-TEMPLATE.md /your-project/CLAUDE.md

# Copy sprint/backlog templates
cp PLANNING-HIERARCHY-TEMPLATE/SPRINT-TEMPLATE.md /your-project/docs/03-Development-Implementation/02-Sprint-Plans/
cp PLANNING-HIERARCHY-TEMPLATE/BACKLOG-TEMPLATE.md /your-project/docs/03-Development-Implementation/
```

### PROFESSIONAL Tier (10-50 people, $200K-1M)

```bash
# Copy all templates
cp AI-ONBOARDING-TEMPLATE.md /your-project/CLAUDE.md

# Copy full planning hierarchy
cp -r PLANNING-HIERARCHY-TEMPLATE/* /your-project/docs/
```

### ENTERPRISE Tier (50+ people, $1M+)

```bash
# All PROFESSIONAL templates plus:
# - Weekly CTO/CPO report templates
# - Gate review templates
# - Compliance documentation templates
```

---

## Template Contents

### AI-ONBOARDING-TEMPLATE.md

Standardized CLAUDE.md template for AI assistant onboarding.

**Sections**:
- Project Overview
- Current Status
- Tech Stack
- Architecture
- Key Decisions (ADRs)
- Critical Constraints
- Development Guidelines
- Key Documents
- AI Assistant Mandate

**Goal**: AI assistant understands project context in <30 seconds

### PLANNING-HIERARCHY-TEMPLATE/

4-level planning hierarchy templates based on 4-Level Planning Hierarchy.

| Level | Template | Duration |
|-------|----------|----------|
| Roadmap | ROADMAP-TEMPLATE.md | 12 months |
| Phase | PHASE-TEMPLATE.md | 4-8 weeks |
| Sprint | SPRINT-TEMPLATE.md | 5-10 days |
| Backlog | BACKLOG-TEMPLATE.md | Individual items |

---

## Customization Guidelines

### Step 1: Copy the template
```bash
cp TEMPLATE-NAME.md /your-project/path/
```

### Step 2: Replace placeholders
All placeholders are in `[brackets]`:
```markdown
# [PROJECT NAME]  →  # SDLC Orchestrator
**Version**: [X.Y.Z]  →  **Version**: 1.0.0
```

### Step 3: Remove unused sections
For LITE/STANDARD tiers, remove advanced sections:
```markdown
# Remove these for LITE tier:
- Architecture diagram
- ADR table
- Performance budget
```

### Step 4: Add project-specific content
```markdown
# Add your project's unique:
- Constraints
- Tech stack details
- Team structure
```

---

## Compliance Checklist

Before using templates, verify:

- [ ] Correct tier identified for project
- [ ] All `[placeholders]` replaced with real values
- [ ] Unused sections removed (don't leave empty sections)
- [ ] Project-specific content added
- [ ] Version number set appropriately
- [ ] Owner/authority identified

---

## Related Documents

- [SDLC-Team-Collaboration-Standards.md](../../08-Documentation-Standards/Team-Collaboration/)
- [SDLC-Document-Naming-Standards.md](../../08-Documentation-Standards/)
- [4-Level Planning Hierarchy](../../02-Core-Methodology/SDLC-Sprint-Planning-Guide.md)

---

**Document Status**: ACTIVE
**Compliance**: Templates RECOMMENDED for all SDLC 6.1.2 projects
**Last Updated**: January 22, 2026
**Owner**: CTO + CPO Office
