---
doc_id: F3-SCOPE-DRIFT-DETECTION
title: "Scope Drift Detection Checklist"
version: "1.0.0"
framework: "6.3.0"
ring: 2
created: 2026-03-29
gate_trigger: [G3-Ship-Ready, G-Sprint-Close]
classification: governance-template
---

# F3 — Scope Drift Detection Checklist

**Framework**: SDLC 6.3.0 | **Ring**: 2 (Governance Template)
**Run at**: G3 (Ship Ready) and G-Sprint-Close gates
**Source**: gstack methodology analysis (2026-03-29)

> v1 died from scope creep to 231K LOC — this checklist prevents that.

---

## Purpose

Detect whether **work done** matches **work planned**. Catches unauthorized additions, missing requirements, and silent scope expansion before code ships.

---

## 3-Step Process

### Step 1: Read Stated Intent

- [ ] Locate the sprint spec / ticket / user story that authorized this work
- [ ] Extract the **stated deliverables** (features, endpoints, files, screens)
- [ ] Extract the **stated boundaries** (out-of-scope items, deferred items)
- [ ] Confirm the spec was approved **before** implementation started

### Step 2: Diff Files Against Intent

- [ ] Run `git diff main...HEAD --stat` to list all changed/added files
- [ ] For each changed file, verify it maps to a stated deliverable
- [ ] Flag any file not traceable to the spec (new model, new route, new UI page)
- [ ] Check LOC delta — does the magnitude match the scope? (e.g., 50-line ticket producing 800 LOC)
- [ ] Review any new dependencies added (`requirements.txt`, `package.json`)

### Step 3: Classify Result

- [ ] Assign one classification below
- [ ] Record classification in sprint close evidence
- [ ] If not CLEAN, document the drift items and disposition (keep / revert / defer)

---

## Classification Definitions

| Classification | Definition | Example |
|---|---|---|
| **CLEAN** | All changes trace to stated intent. No extras, no gaps. | Ticket says "add /users endpoint" — only /users route + tests changed. |
| **SCOPE_CREEP** | Work includes items **not in the spec**. May be useful but unauthorized. | Ticket says "add /users endpoint" — developer also added /roles, /permissions, and a new admin dashboard page. |
| **MISSING_REQUIREMENTS** | Spec deliverables are **not present** in the diff. Work is incomplete. | Ticket says "add /users endpoint with pagination" — endpoint exists but pagination is missing. |

> A single sprint can be both SCOPE_CREEP and MISSING_REQUIREMENTS simultaneously.

### Gate Actions per Classification

| Classification | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---|---|---|---|---|
| **CLEAN** | Advance | Advance | Advance | Advance |
| **SCOPE_CREEP** | Log + advance | **Blocks G3** — resolve or waiver | **Blocks G3 + G-Sprint-Close** | Blocks + Senior Review Board waiver |
| **MISSING_REQUIREMENTS** | Log + advance | **Blocks G3** — complete work or re-scope | **Blocks G3 + G-Sprint-Close** | Blocks + audit trail required |

> **Connection to Terminal Status Taxonomy** (Section 8, [Agentic Core Principles](../../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md)):
> CLEAN → DONE (auto-advance). SCOPE_CREEP → DONE_WITH_CONCERNS (flag for review). MISSING_REQUIREMENTS → BLOCKED (work incomplete, gate paused).

---

## Tier-Specific Rules

| Tier | G3 (Ship Ready) | G-Sprint-Close | Enforcement |
|---|---|---|---|
| **LITE** | Informational only | N/A | Log result, no gate block |
| **STANDARD** | Mandatory — SCOPE_CREEP blocks G3 | Informational | Must resolve or get waiver before ship |
| **PRO** | Mandatory — blocks G3 | Mandatory — blocks G-Sprint-Close | Both gates require CLEAN or documented waiver |
| **ENTERPRISE** | Mandatory — blocks G3 | Mandatory — blocks G-Sprint-Close | Audit trail required; waiver needs Senior Review Board approval |

---

## Quick Reference Commands

```bash
# Files changed in this branch
git diff main...HEAD --stat

# LOC added vs removed
git diff main...HEAD --shortstat

# New files only (potential unauthorized additions)
git diff main...HEAD --diff-filter=A --name-only
```

---

**Classification**: __________ | **Reviewer**: __________ | **Date**: __________
