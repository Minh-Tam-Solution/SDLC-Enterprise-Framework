---
spec_id: SPEC-NNNN
spec_name: "<feature or component>"
spec_version: "1.0.0"
status: draft
sdlc_framework: "7.0.0"
tier: <LITE | STANDARD | PROFESSIONAL | ENTERPRISE>
stage: "02"
category: functional
owner: "<role or handle>"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
related_adrs: []
related_specs: []
---

# SPEC-NNNN: <feature or component>

## Overview

<two or three paragraphs: what and for whom>

**Out of scope:** <what a reader could reasonably expect that this change will not do>

## Context

<the problem, with the evidence from stage 00>

## Requirements

| # | Requirement | AC id | Acceptance criterion |
|---|---|---|---|
| R1 | <behaviour> | AC-NNNN-1 | GIVEN … WHEN … THEN … |
| R2 | <limit: latency, size, retention> | AC-NNNN-2 | <number> measured by <how> |

<AC id = `AC-<spec number>-<n>`. An id is never renumbered or reused; a dropped criterion stays in the table marked `retired`. Tests cite the id ([`testing.md`](../../standards/testing.md#tests-prove-requirements)). Pattern adapted from OpenBA-Kit (MIT, dea3e3a8).>

## Design decisions

<links to ADRs; do not copy them>

## Technical specification

<interfaces, data, error behaviour>

## Dependencies

<systems, teams, other specs>

## Open questions

<each with who can answer it; one that needs a person's choice is a NEEDS_DECISION>
