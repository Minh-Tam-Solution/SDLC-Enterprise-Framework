# Risk Floor Paths

**Version**: 7.0 (extracted from archived `08-Governance-Decision-Matrix.md`, 2026-09-25)
**Status**: ACTIVE
**Pillar**: Core AI Governance

---

## Purpose

A deterministic, path-based risk floor: a fixed list of path patterns that always require the
highest verification tier, regardless of which model or agent produced the change. This is a
**path classification**, not a scoring model — it does not compute an index, and it is never
satisfied by a probabilistic judgment (a model's own confidence is not evidence here).

This table is the generalized, tool-agnostic successor to the Risk Classification Rules table
that lived in `08-Governance-Decision-Matrix.md` (archived v7 — see
`10-Archive/by-topic/ai-governance-v7-retired/08-Governance-Decision-Matrix.md`). The original
table was tied to a retired governance engine and a Vibecoding Index that v7 dropped; the path
list itself is the part worth keeping.

---

## Risk Floor — Path Patterns That Never Get Downgraded

| Path pattern | Risk tier | Why |
|---|---|---|
| `migrations/` | CRITICAL | Irreversible schema change; a bad migration can corrupt or lose data |
| `auth/` | CRITICAL | Authentication — a defect can let anyone in or lock everyone out |
| `tenant/` | CRITICAL | Multi-tenant isolation — a defect can leak one tenant's data to another |
| `permissions/` | CRITICAL | Authorization — a defect can grant access that should be denied |
| `billing/` | CRITICAL | Directly moves or represents money |
| `payment/` | CRITICAL | Directly moves or represents money |
| `infra/` | CRITICAL | Infrastructure/deployment config — a defect can take down production |
| `secrets/` | CRITICAL | Credentials and keys — a leak is not reversible by a patch |

Also treated as CRITICAL wherever they appear (not path-bound): IAM configuration, production
config, and any destructive SQL (`DROP`, `DELETE` / `TRUNCATE` without a `WHERE`/scope guard).

---

## Rule

A change touching any of the above paths **always** requires the highest verification tier
(human review + independent re-derivation of any headline number), no matter what generated
the diff or how confident the generating agent claims to be. This floor sits **below** any
model-routing or capability-tier policy — routing decides which model does the work; this floor
decides the minimum verification the work gets, independent of that choice.

---

## Not in Scope Here

- Model/capability-tier routing (which model should do T0–T4 work) — that is a routing policy,
  tracked separately, not this risk floor.
- Scoring or indexing AI contribution "quality" — this file makes no attempt to measure that;
  the predecessor's index (Vibecoding Index) is retired.

---

**Source**: extracted from `08-Governance-Decision-Matrix.md` L52-59 (Risk Classification Rules),
generalized to remove product-specific examples. Framework-owned, tool-agnostic.
