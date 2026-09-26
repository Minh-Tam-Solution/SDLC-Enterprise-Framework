---
document_id: "TRAINING-MODULE-09"
title: "Module 09: Quality Gate Workshop"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "2 hours (6 parts)"
audience: "All team members — developers, pod leads, architects, product managers"
prerequisite: "Module 01-08 (SDLC Overview, Pillars, Zero Mock, Code Quality, Workflow, AI Tools, SASE, Authority)"
format: "Hands-on Workshop (instructor-led + practice on staging environment)"
---

# Module 09: Quality Gate Workshop

> **Core principle**: "No evidence = no quality. No gate = no governance."

---

## 1. The 5 Gates Explained (30 minutes)

The Quality Gate system ensures every deliverable meets standards before advancing to the next stage. Each gate answers ONE question.

| Gate | Name | Question | Approved By | When |
|------|------|----------|-------------|------|
| G0 | Discovery | **WHY?** Why do we need this feature? | CEO/CPO | Before sprint begins |
| G1 | Requirements | **WHAT?** What exactly needs to be done? | CPO + PM | User stories + acceptance criteria ready |
| G2 | Architecture | **HOW?** How will it be designed? | CTO | ADR or tech spec exists |
| G3 | Ship Ready | **DONE?** Are code + tests sufficient? | CEO/CPO (Pod Lead submits) | Sprint done, QA passed |
| G4 | Release | **SAFE?** Is it production-ready? | CTO + CEO joint | Deploy to production |

> **Instructor note**: Draw the 5 gates on the board. Emphasize: each gate = 1 question. If you cannot answer that question = gate FAIL.

### Gate Details

| Gate | Required Evidence | FAILS When | Real Example |
|------|------------------|------------|--------------|
| **G0** | Problem statement, user research, priority justification | Cannot explain "why"; no data supporting the need | Performance baseline data for a frontend optimization sprint |
| **G1** | User stories + acceptance criteria, scope boundary, sprint plan committed | Vague user stories; no acceptance criteria; sprint plan not committed | Multi-tenant sprint with specific user stories, API 201 verified |
| **G2** | ADR or tech spec, API contract, impact analysis | No ADR; API contract does not match implementation | OAuth flow ADR with encryption specification |
| **G3** | Code + PR, tests pass, CLAUDE.md updated, build OK | Tests fail or missing; build broken; CLAUDE.md not updated | 48 unit tests + 5 E2E specs, build passes |
| **G4** | G3 approved, security review, deployment plan + rollback. **Human-only approval** | G3 not passed; no rollback plan; self-approved | CTO + CEO joint approval of OWASP security fixes |

> **Instructor note**: Ask participants: "If a CTO self-approves gate G4 for their own code, is that valid?" -- Answer: NO. Self-approval is prohibited at every level.

---

## 2. Hands-on: SDLC Orchestrator (45 minutes)

> **Instructor note**: Prepare in advance: ensure the SDLC Orchestrator instance is running, create workshop accounts for all participants, verify the messaging bot is online.

### Step 1: Log In

1. Open a browser and navigate to your SDLC Orchestrator instance
2. Log in with the credentials provided by the instructor
   - If no account exists: click **Sign Up** or use the messaging bot signup command
3. After login, the **Dashboard** displays with the project list

> **Screen**: Dashboard shows: sidebar (Projects, Settings), header (user avatar, notifications). First-time users see an empty project list.

### Step 2: Create a Test Project

1. Click **Projects** in the sidebar
2. Click **+ New Project**
3. Enter details:
   - **Name**: `workshop-[your-name]` (e.g., `workshop-alex`)
   - **Description**: "Test project for Quality Gate Workshop"
4. Click **Create Project**

> **Screen**: Project created, navigates to project detail page. Shows: project name, members (only you -- Owner), gates (empty).

### Step 3: Create a Gate

1. In the project detail view, click **+ Create Gate**
2. Fill in:
   - **Gate Type**: select `G2_ARCHITECTURE`
   - **Gate Name**: `G2-workshop-test`
   - **Exit Criteria** (enter one per line):
     - "Design doc exists"
     - "CTO reviewed"
3. Click **Create Gate**

> **Screen**: New gate appears in the list with status **CREATED** (gray badge). Shows: gate name, type, created date, status badge.

> **Instructor note**: Explain the 5 gate states: CREATED -> SUBMITTED -> APPROVED / REJECTED -> RE-SUBMITTED. This is a mandatory lifecycle -- no skipping steps.

### Step 4: Upload Evidence

1. Click on gate `G2-workshop-test` to open the **Gate Detail** view
2. Click **+ Upload Evidence**
3. Create a file `test-results.txt` on your computer with the following content:
   ```
   Unit tests: 15/15 passed
   Integration tests: 3/3 passed
   Coverage: 87%
   ```
4. Drag and drop the file into the upload area or click **Choose File**
5. Select evidence type: `TEST_RESULT`
6. Click **Upload**

> **Screen**: Evidence appears in the list with: file name, upload date, **SHA256 hash** (64-character string). This hash ensures the evidence cannot be modified after upload.

> **Instructor note**: Emphasize the SHA256 hash -- this is immutable evidence. If someone modifies the file and re-uploads it, the hash will be DIFFERENT. This is the anti-fraud mechanism.

### Step 5: Submit the Gate

1. Click **Submit Gate** (blue button)
2. Gate transitions from CREATED to **SUBMITTED** (yellow badge)
3. A notification is sent to the project Owner/Admin

> **Screen**: Status badge changes to "SUBMITTED". Timeline shows: "Created by [your name] -> Submitted by [your name]".

> **Instructor note**: Now the instructor plays the CTO role. Visit each participant's gate and **REJECT** it with feedback: "Missing ADR -- please provide an Architecture Decision Record before approval."

### Step 6: Fix and Re-submit

1. After rejection, the gate transitions to **REJECTED** (red badge)
2. Read the CTO's feedback: "Missing ADR"
3. Create a file `ADR-workshop.md` with the following content:
   ```
   # ADR: Workshop Architecture Decision
   ## Context: Need to design a new module for the workshop
   ## Decision: Use existing pattern from prior sprints
   ## Consequences: No impact on current architecture
   ```
4. Upload the ADR file to the gate (repeat Step 4 with the new file)
5. Click **Re-submit**

> **Screen**: Gate transitions to **RE-SUBMITTED**. Timeline now shows the full chain: Created -> Submitted -> Rejected (feedback) -> Re-submitted.

> **Instructor note**: Approve the participants' gates. Explain: in practice, the CTO reviews the new evidence (ADR) before approving. No blind approvals.

### Step 7: View the Audit Trail

1. Navigate to the **Audit** page (or `/audit` in the URL)
2. Find your gate `G2-workshop-test`
3. View the full chain:

> **Screen**: Audit trail displays:
> ```
> [10:01] CREATED      -- G2-workshop-test created by workshop-alex
> [10:05] SUBMITTED    -- Submitted by workshop-alex (1 evidence)
> [10:08] REJECTED     -- Rejected by instructor (reason: Missing ADR)
> [10:12] EVIDENCE     -- ADR-workshop.md uploaded (SHA256: a3f2...)
> [10:13] RESUBMITTED  -- Re-submitted by workshop-alex (2 evidences)
> [10:15] APPROVED     -- Approved by instructor
> ```
> Every entry has a timestamp, actor, action, and Merkle hash chain ensuring no one can delete or modify the audit trail.

> **Instructor note**: Ask participants: "Why is the Merkle hash chain important?" -- Answer: If someone deletes an entry in the middle of the chain, the hashes of all subsequent entries will not match. Tampering is detected immediately.

---

## 3. Sprint Gates (15 minutes)

In addition to the 5 feature gates (G0-G4), SDLC Orchestrator includes 2 **Sprint Gates**:

### G-Sprint -- Before Starting a Sprint

Evaluates the 10 Golden Rules before a sprint is permitted to begin:

| # | Golden Rule | Check |
|---|-------------|-------|
| 1 | Sprint plan committed | File exists in git? |
| 2 | Scope is clear | Has acceptance criteria? |
| 3 | Dependencies identified | Any blockers? |
| 4 | Team capacity confirmed | Who does what? |
| 5 | Design docs ready | ADR/spec exists? |
| 6 | Test strategy defined | What to test, how to test? |
| 7 | Risk assessed | What risks need mitigation? |
| 8 | Previous sprint closed | Was the previous sprint closed? |
| 9 | CLAUDE.md current | Version correct? |
| 10 | Stakeholder aligned | CEO/CPO agree on scope? |

> **Instructor note**: G-Sprint was introduced to prevent teams from starting sprints without verifying preconditions. Without it: scope creep, missing docs, stale metadata.

### G-Sprint-Close -- After Completing a Sprint

Confirms sprint deliverables are documented and verified:

- Code committed and pushed
- Tests pass (0 failures)
- Build succeeds
- CLAUDE.md updated (version + history + test count)
- Sprint plan marked COMPLETED
- Evidence uploaded for all related gates

---

## 4. What Fails a Gate? (15 minutes)

The 7 most common reasons a gate is REJECTED -- drawn from audit reports and real sprint experience:

| # | Reason | Explanation | Reference |
|---|--------|-------------|-----------|
| 1 | **Missing tests** | Code shipped with zero tests. Had to rewrite later, costing twice the time. | PM Audit violation |
| 2 | **No evidence uploaded** | Gate SUBMITTED but no files attached. "I already tested" without proof does not count. | -- |
| 3 | **Scope creep** | Sprint plan says "feature A" but commits include refactor B and fix C. Out-of-scope changes need their own gate. | -- |
| 4 | **CLAUDE.md stale** | Code is at Sprint 53 but CLAUDE.md still says Sprint 50. Sprint history missing entries, test count wrong. | -- |
| 5 | **Design doc missing** | Multiple docs untracked. Code written but no ADR, no tech spec. | PM Audit violation |
| 6 | **False compliance** | Status marked "SHIPPED" but build was never run. Claimed "tests pass" but pytest was never executed. | PM Audit violation |
| 7 | **Self-approved gates** | Owner approved a gate for their own PR. The person who builds is not the person who reviews. | -- |

> **Instructor note**: Print these 7 reasons on a sheet and distribute to each participant. This is a checklist to verify before submitting any gate.

---

## 5. Hands-on Exercises (15 minutes)

> **Instructor note**: These exercises are performed on the staging environment. Ensure all participants have accounts and are logged in.

### Exercise 1: Full Gate Lifecycle

1. Create a new gate: `G3_SHIP_READY`, name: `G3-exercise-[your-name]`
2. Upload 1 evidence (any file)
3. Submit the gate
4. Wait for the instructor to reject with feedback
5. Upload additional evidence (fix per the feedback)
6. Re-submit
7. Wait for the instructor to approve
8. Check the audit trail -- ensure all 6 steps are visible

### Exercise 2: Audit Trail Verification

1. Navigate to the `/audit` page
2. Find the gate you just created in Exercise 1
3. Answer these questions:
   - When was the gate created?
   - Who rejected it? What was the reason?
   - How many evidence files were uploaded?
   - What is the Merkle hash of the final entry?

### Exercise 3: Permission Check

1. Create a new project: `workshop-permission-test`
2. Invite another participant to the project with role **Member**
3. Ask them to try to **Approve** your gate
4. Expected result: **Permission Denied** -- Members cannot approve gates

> **Screen**: Error message displays: "Permission denied: only Owner or Admin can approve gates."

### Exercise 4: Messaging Bot Evidence Upload

1. Open your messaging platform and find the SDLC Orchestrator bot
2. Send the command to switch to your project
3. Send the command to view current gates
4. Send the evidence upload command with an attached file
5. Confirm the evidence appears on the Web UI

> **Instructor note**: Exercise 4 only works if the messaging bot is online. If offline, skip and explain that the messaging platform is a secondary channel; the Web UI is the primary interface.

---

## 6. Reference Materials

| Document | Location |
|----------|----------|
| User Guide -- Gate Management | Project `docs/08-collaborate/user-guides/` |
| Gate Engine (source code) | `backend/app/services/gate_engine.py` |
| Evidence Vault (SHA256 + S3) | `backend/app/services/evidence_service.py` |
| Sprint Workflow Enforcement Rules | Project `CLAUDE.md` |
| SDLC 6.3.0 Framework -- Gate Checklists | `SDLC-Enterprise-Framework/05-Templates-Tools/05-Checklists/` |
| Quality Gates & Assurance Framework | `SDLC-Enterprise-Framework/02-Core-Methodology/Governance-Compliance/` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | 5 Gates Explained -- G0 through G4, evidence + failure reasons | 30 min |
| 2 | Hands-on SDLC Orchestrator -- 7-step practice | 45 min |
| 3 | Sprint Gates -- G-Sprint and G-Sprint-Close | 15 min |
| 4 | What Fails a Gate -- 7 common reasons | 15 min |
| 5 | Hands-on Exercises -- 4 exercises on staging | 15 min |
| | **Total** | **2h** |

### After completing this module, participants must be able to:

1. Explain the purpose of each gate (G0-G4) and the question each gate answers.
2. Know which evidence to upload for each gate type.
3. Practice the full gate lifecycle on SDLC Orchestrator (create -> submit -> reject -> fix -> re-submit -> approve).
4. Understand the Merkle hash chain and why the audit trail is immutable.
5. Distinguish which roles can approve gates and which cannot.
6. Use both the Web UI and messaging bot to manage gates.

> **Remember**: "No evidence = no quality." Every claim must have proof. Every proof must have a hash. Every hash must be in the chain. This is governance -- not bureaucracy.

---

## Assessment Questions

**Q1.** How many quality gates are in the SDLC 6.3.0 framework?
> **Answer**: 5 gates -- G0 (Discovery), G1 (Requirements), G2 (Architecture), G3 (Ship Ready), G4 (Release)

**Q2.** Which gate requires CTO + CEO joint approval?
> **Answer**: G4 (Release) -- production deployment requires both CTO and CEO approval

**Q3.** What evidence type fails a gate submission?
> **Answer**: A submission with no tests and no evidence. "I already tested" without proof is not valid evidence.

**Q4.** What happens after 3 rejections of the same gate?
> **Answer**: Escalation. Repeated rejections indicate a fundamental issue that must be escalated to leadership (Pod Lead -> CTO -> CPO) for resolution.

**Q5.** What is the Merkle chain used for?
> **Answer**: Immutable audit trail. The Merkle hash chain ensures that no entry in the audit log can be deleted or modified without detection. If any entry is tampered with, the hashes of all subsequent entries will not match.
