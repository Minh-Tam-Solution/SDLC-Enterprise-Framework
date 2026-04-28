---
title: "Evidence Integration Standard — Multi-Source Ingestion"
version: "6.3.1"
ring: 2
sdlc_version: "6.3.1"
last_updated: "2026-04-06"
status: "ACTIVE"
pillar: "NEW — Evidence Integration"
source: "SDLC Orchestrator v2 Sprint 17 + V2 Independence Principle + CEO directive"
---

# Evidence Integration Standard — Multi-Source Ingestion

> NEW in Framework 6.3.0. Validated by SDLC Orchestrator v2 Sprint 17 (evidence ingestion API, 371 tests).

## Principle

> Evidence from any source is treated equally. No source receives preferential treatment in gate evaluation.

## Evidence Sources

| Source | Transport | Example |
|---|---|---|
| `manual` | File upload (Telegram, Web) | Developer uploads test report |
| `telegram` | OTT command (/evidence) | Team uploads via chat |
| `mtclaw` | Webhook / API push | MTClaw agent transcript |
| `api` | REST API (POST /ingest) | External tool pushes results |
| `ci_cd` | Webhook (GitHub Actions, GitLab CI) | CI pipeline test results |

## Evidence Types

| Type | What It Contains |
|---|---|
| `test_results` | Test pass/fail counts, coverage report |
| `code_review` | Review comments, approval status |
| `deployment_proof` | Deploy logs, environment verification |
| `transcript` | Agent conversation transcript (SHA256 hash chain) |
| `agent_output` | Agent analysis, recommendations |
| `static_analysis` | AST analysis, impact radius, code graph results |

## Ingestion API Contract

```
POST /api/v1/evidence/ingest
Auth: Bearer JWT (user) OR X-Integration-Key (service-to-service)
Body: {
  gate_id, evidence_type, source,
  external_reference_id (idempotency),
  content OR file_url,
  metadata (flexible JSONB)
}
```

**Rules**:
- `external_reference_id` uniqueness enforced — prevents duplicate ingestion
- Text content → auto-stored as file (MinIO S3), SHA256 computed
- `source` field indexed — gate evaluator can query by source
- `uploaded_by` nullable — service-to-service has no user identity

## Integration Auth

Service-to-service authentication via `X-Integration-Key` header:
- Key identifies source system, not a user
- Keys stored as JSON dict in settings
- HMAC-safe comparison (`hmac.compare_digest`)
- Logged in audit trail with `source` field

## Gate Evaluation

Gate evaluator counts evidence by source:
```python
evidence_sources = {"manual": 2, "mtclaw": 3, "ci_cd": 1}
# Passed to OPA PolicyInput — all sources weighted equally
```

**No source preference**: A manual upload has exactly the same weight as an MTClaw-produced transcript. The governance platform evaluates quality, not provenance.
