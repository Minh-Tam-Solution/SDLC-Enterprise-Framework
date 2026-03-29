---
version: "6.2.1"
document_type: "Framework Standard"
section: "05-Templates-Tools/06-Manual-Templates"
status: "APPROVED"
owner: "CTO"
last_updated: "2026-02-18"
context_zone: "Governance"
update_frequency: "Per major version (quarterly)"
priority: "P1"
source: "Industry merge documentation practices + SDLC Evidence methodology"
sprint: "176"
---

# MRP: Merge-Readiness Package Template

**Framework Version**: SDLC 6.2.0
**Pillar**: 02 — Core Methodology
**Classification**: ORANGE (New Process Artifact — affects merge workflow)
**Effective Date**: February 19, 2026

---

## 1. Purpose

MRP (Merge-Readiness Package) is the structured artifact that proves a feature is ready for production merge. It replaces ad-hoc PR descriptions with evidence-linked documentation.

### 1.1 Why MRP Exists

Traditional PR descriptions are:
- **Inconsistent**: Each developer writes differently (some write nothing)
- **Unlinked**: No connection to Quality Gate evidence
- **Ephemeral**: Lost when PRs are squash-merged
- **Unauditable**: Cannot prove compliance after the fact

MRP solves these by providing a **standardized, evidence-linked, auditable** merge package.

### 1.2 Industry Context

Leading AI-native teams use AI assistants to summarize completed work sessions and update documentation automatically. SDLC 6.2.0 extends session summaries into comprehensive merge packages that:
- Link to Quality Gate evidence (not just git history)
- Include rollback plans (not just "what changed")
- Provide deployment instructions (not just "how to build")
- Create an immutable audit trail (stored in Evidence Vault)

---

## 2. MRP Structure (5 Sections)

Every MRP must contain exactly 5 sections. Sections can be partially auto-generated but must be human-reviewed before merge.

### Section 1: Change Summary

**Purpose**: What changed, why, and what's affected.
**Max Length**: 100 words (forces conciseness)

#### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| **What Changed** | 3-5 bullet points describing the changes | "Added prompt caching to code generation API" |
| **Why It Changed** | Link to Gate G1 approval or business justification | "Gate G1 Approval: EVD-12345" |
| **Impact Scope** | Systems, APIs, tables, and services affected | "Systems: Code Generation; APIs: POST /codegen/generate" |

#### Template

```markdown
### 1. Change Summary

**Changes**:
- [Change 1]
- [Change 2]
- [Change 3]

**Justification**: [Gate G1 approval reference or business requirement link]

**Impact Scope**:
- **Systems**: [list affected systems]
- **APIs**: [list affected endpoints]
- **Tables**: [list affected database tables, if any]
- **Dependencies**: [new or changed external dependencies]
```

#### Example

```markdown
### 1. Change Summary

**Changes**:
- Added Redis-based prompt caching to code generation API
- Integrated provider-side cache hints for L2 caching
- Reduced generation cost by 8x ($0.016 → $0.002 per request)

**Justification**: Gate G1 Approval [EVD-12345] — Cost optimization initiative

**Impact Scope**:
- **Systems**: Code Generation Service
- **APIs**: `POST /api/v1/codegen/generate` (new header: `X-Cache-Status`)
- **Tables**: None (cache-only, no schema changes)
- **Dependencies**: Redis 7.2+ required (existing infrastructure)
```

---

### Section 2: Evidence Vault References

**Purpose**: Link every claim to stored evidence. Each Quality Gate must have at least one evidence artifact.

#### Required Evidence by Gate

| Gate | Evidence Type | Required? | Description |
|------|--------------|-----------|-------------|
| **G1** | Legal clearance | PRO/ENTERPRISE | License scan result, stakeholder sign-off |
| **G1** | Stakeholder approval | All tiers | Product owner or architect sign-off |
| **G2** | SAST report | All tiers | Semgrep scan results (0 critical findings) |
| **G2** | Dependency audit | PRO/ENTERPRISE | License compatibility report |
| **G3** | Test coverage report | All tiers | Coverage percentage + key test names |
| **G3** | E2E test recordings | PRO/ENTERPRISE | Playwright recordings or screenshots |
| **G4** | Architect review | For >500 LOC | Architect sign-off with review notes |
| **G4** | Performance benchmark | PRO/ENTERPRISE | Before/after latency comparison |

#### Template

```markdown
### 2. Evidence Vault References

| Gate | Evidence ID | Type | Status | Verified By |
|------|-------------|------|--------|-------------|
| G1   | EVD-XXXXX  | [type] | [APPROVED/PASS/FAIL] | [reviewer] |
| G2   | EVD-XXXXX  | [type] | [APPROVED/PASS/FAIL] | [reviewer] |
| G3   | EVD-XXXXX  | [type] | [APPROVED/PASS/FAIL] | [reviewer] |
| G4   | EVD-XXXXX  | [type] | [APPROVED/PASS/FAIL] | [reviewer] |
```

#### Example

```markdown
### 2. Evidence Vault References

| Gate | Evidence ID | Type | Status | Verified By |
|------|-------------|------|--------|-------------|
| G1 | EVD-12345 | Legal Clearance | APPROVED | CTO |
| G2 | EVD-12346 | Semgrep Report | PASS (0 critical) | Security Lead |
| G3 | EVD-12347 | Test Coverage | 94.2% (target: 90%) | QA Lead |
| G4 | EVD-12348 | Perf Benchmark | p95: 80ms → 65ms (-19%) | Backend Lead |
```

---

### Section 3: Rollback Plan

**Purpose**: Define failure conditions, rollback steps, and data migration reversal. Must be executable by any on-call engineer, not just the feature author.

#### Required Fields

| Field | Description |
|-------|-------------|
| **Rollback Trigger** | Specific failure conditions that warrant rollback |
| **Rollback Steps** | 1-2-3 numbered instructions (copy-pasteable commands) |
| **Data Migration** | Schema rollback migration if applicable |
| **Estimated Time** | Expected time to complete rollback |
| **Verification** | How to confirm rollback succeeded |

#### Template

```markdown
### 3. Rollback Plan

**Trigger**: [specific failure conditions]

**Steps**:
1. [command or action]
2. [command or action]
3. [command or action]

**Data Migration**: [N/A or migration steps]

**Estimated Time**: [X minutes]

**Verification**:
```bash
[health check command]
# Expected: [expected output]
```
```

#### Example

```markdown
### 3. Rollback Plan

**Trigger**: Cache hit rate <50% OR latency increase >100ms OR error rate >1%

**Steps**:
1. Rollback deployment:
   ```bash
   [container orchestrator] rollback deployment/[service-name] --to-revision=[N]
   ```
2. Clear corrupted cache:
   ```bash
   redis-cli -h [cache-host] -p 6379 FLUSHDB
   ```
3. Monitor health:
   ```bash
   curl https://[api-host]/health
   ```

**Data Migration**: N/A (cache-only, no persistent schema changes)

**Estimated Time**: 5 minutes

**Verification**:
```bash
curl https://[api-host]/api/v1/health
# Expected: {"status": "healthy", "cache": "disconnected"}
```
```

---

### Section 4: Testing Evidence

**Purpose**: Prove that the change has been tested at all levels. Not just coverage numbers — specific test names and scenarios.

#### Required Fields

| Field | Description |
|-------|-------------|
| **Unit Tests** | Coverage %, count pass/fail, key test names |
| **Integration Tests** | E2E scenarios with expected/actual results |
| **Manual QA** | Screenshots or video recordings of critical flows |
| **Performance** | Before/after latency comparison (for performance-sensitive changes) |

#### Template

```markdown
### 4. Testing Evidence

**Unit Tests**: [X]% coverage ([N] tests pass, [M] fail)
- `test_[key_test_1]()` — validates [what]
- `test_[key_test_2]()` — validates [what]

**Integration Tests**: [N] E2E scenarios
- Scenario 1: [description] → [result]
- Scenario 2: [description] → [result]

**Manual QA**: [description of manual verification]
- [Screenshot/video reference]

**Performance** (if applicable):
- Before: [metric]
- After: [metric]
- Improvement: [percentage]
```

#### Example

```markdown
### 4. Testing Evidence

**Unit Tests**: 94.2% coverage (272 tests pass, 0 fail)
- `test_context_cache_hit_rate()` — validates 85% cache hit on repeated requests
- `test_cache_key_collision_prevention()` — ensures unique keys per context hash
- `test_redis_connection_retry()` — validates reconnection after transient failure

**Integration Tests**: 12 E2E scenarios (all pass)
- Scenario 1: Fresh codegen request (cache miss) → 1200ms latency, cache stored
- Scenario 2: Repeated request (cache hit) → 180ms latency (-85% improvement)
- Scenario 3: Redis down → Graceful fallback to uncached path, no errors

**Manual QA**: Video recording of codegen workflow
- Verified: Cache status header (`X-Cache-Status: HIT/MISS`) visible in response
- Verified: Cache statistics command shows accurate hit/miss counts

**Performance**:
- Before: p95 codegen latency = 1200ms
- After: p95 codegen latency = 180ms (cache hit) / 1250ms (cache miss)
- Improvement: 85% latency reduction on cached requests
```

---

### Section 5: Deployment Notes

**Purpose**: Everything needed to deploy this change safely. A DevOps engineer reading only this section should be able to deploy and verify.

#### Required Fields

| Field | Description |
|-------|-------------|
| **Config Changes** | New environment variables, feature flags, config file changes |
| **Deployment Order** | If multi-service, the exact sequence of deployments |
| **Post-Deployment Validation** | Health check commands with expected output |
| **Feature Flags** | If behind a flag, how to enable/disable |

#### Template

```markdown
### 5. Deployment Notes

**New Configuration**:
- `ENV_VAR_NAME=value` — [description]

**Deployment Order**:
1. [step 1]
2. [step 2]
3. [step 3]

**Post-Deployment Validation**:
```bash
[health check command]
# Expected: [expected output]
```

**Feature Flags**: [N/A or flag details]
```

#### Example

```markdown
### 5. Deployment Notes

**New Configuration**:
- `CACHE_URL=redis://[cache-host]:6379/2` — Cache database
- `CACHE_TTL_SECONDS=3600` — Cache TTL (1 hour)
- `CACHE_ENABLED=true` — Feature flag to enable/disable caching

**Deployment Order**:
1. Ensure cache is available: `redis-cli -h [cache-host] PING` → PONG
2. Deploy service: `[container orchestrator] apply -f k8s/[service].yaml`
3. Run smoke test: verify health endpoint returns "healthy"

**Post-Deployment Validation**:
```bash
# Check cache is operational
redis-cli -h [cache-host] PING
# Expected: PONG

# Check service health
curl https://[api-host]/api/v1/health
# Expected: {"status": "healthy", "cache": "connected"}
```

**Feature Flags**:
- `CACHE_ENABLED=false` disables all caching (safe fallback)
- No code changes needed to disable — env var only
```

---

## 3. MRP Generation Workflow

### 3.1 Manual Generation (Baseline)

Engineer writes MRP as part of PR creation using this template. All 5 sections required for PRO/ENTERPRISE tiers; LITE tier requires Sections 1, 3, 4.

### 3.2 Semi-Automated Generation

Platform CLI tools can pre-fill MRP from CI/CD artifacts:

```
mrp generate --pr-number=1234 --auto-evidence --auto-tests
```

**Output**: 80% pre-filled MRP. Engineer reviews and adds rollback plan + deployment notes.

### 3.3 Fully Automated Generation

AI assistant workflow:
1. Reads PR commits + evidence store artifacts
2. Generates Change Summary from commit messages
3. Links Evidence IDs from Gate approvals
4. Creates rollback plan from deployment history and infrastructure state
5. Embeds test coverage reports from CI pipeline
6. Outputs MRP draft for **human approval** (mandatory review — never auto-merge)

---

## 4. Integration with Quality Gates

### 4.1 Gate G4 Requirement

Gate G4 (Ship Ready) requires a complete MRP before merge approval.

### 4.2 Policy-as-Code Enforcement

Gate G4 policy must enforce:

1. **MRP existence**: Block merge if MRP is not attached to the PR
2. **Section completeness**: Block merge if required sections are empty or missing
3. **Tier-aware requirements**: LITE requires 3 sections; PRO/ENTERPRISE requires all 5
4. **Evidence linkage**: At least one valid evidence ID per gate referenced

Platform implementations should encode these rules in their policy engine (OPA, Sentinel, Cedar, or CI/CD pipeline checks).

### 4.3 Tier-Specific Requirements

| Section | LITE | STANDARD | PRO | ENTERPRISE |
|---------|------|----------|-----|-----------|
| **1. Change Summary** | Required | Required | Required | Required |
| **2. Evidence References** | Optional | Required | Required | Required |
| **3. Rollback Plan** | Required | Required | Required | Required |
| **4. Testing Evidence** | Required | Required | Required | Required |
| **5. Deployment Notes** | Optional | Optional | Required | Required |

---

## 5. MRP Storage and Lifecycle

### 5.1 Storage Locations

| Format | Location | Purpose |
|--------|----------|---------|
| **Markdown** | PR description body | Human-readable, in code review context |
| **Structured** | Evidence Vault (JSON) | Machine-parseable, auditable, queryable |
| **Archive** | Evidence Vault (immutable) | Compliance record, post-merge reference |

### 5.2 Lifecycle

```
DRAFT → REVIEW → APPROVED → ARCHIVED
  │                           │
  └── REVISION_REQUESTED ─────┘
```

- **DRAFT**: MRP created (manual or auto-generated)
- **REVIEW**: Submitted with PR for reviewer assessment
- **REVISION_REQUESTED**: Reviewer found issues, returned to author
- **APPROVED**: All sections complete, evidence linked, ready for merge
- **ARCHIVED**: PR merged, MRP stored in Evidence Vault as immutable record

---

## 6. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **MRP completion rate** | 100% of PRs >100 LOC have MRP | CI/CD gate check |
| **Rollback success rate** | >95% (clear instructions prevent mistakes) | Post-incident review |
| **Merge confidence** | >90% team survey: "confident merging with MRP" | Quarterly developer survey |
| **Audit readiness** | 100% of MRPs retrievable from Evidence Vault | Automated audit check |
| **Auto-generation accuracy** | >80% sections correctly pre-filled (future enhancement) | Manual review sampling |

---

## 7. Anti-Patterns

### 7.1 Empty MRP

**Problem**: MRP template filled with "N/A" or "TBD" for all sections.
**Fix**: Gate G4 OPA policy blocks merge if required sections are empty.

### 7.2 Copy-Paste MRP

**Problem**: Same MRP text reused across PRs with minor edits.
**Fix**: Evidence IDs must be unique per PR. Automated duplicate detection.

### 7.3 MRP Without Evidence

**Problem**: MRP claims "all tests pass" without linking to Evidence Vault artifact.
**Fix**: Section 2 (Evidence References) must contain valid EVD-XXXXX identifiers.

### 7.4 Post-Merge MRP

**Problem**: MRP written after merge as a retroactive formality.
**Fix**: Gate G4 enforces MRP exists BEFORE merge approval. No bypass.

---

## 8. References

- **SDLC 6.0.6**: Section 7 (Quality Assurance System), Gate G4 requirements
- **Evidence methodology**: 8-state lifecycle (generated → merged/aborted)
- **Industry**: PR documentation best practices for compliance-driven development

---

**Document Status**: APPROVED
**Approved By**: CTO
**Ring**: Governance (stable process artifact, tool-agnostic)
**Next Review**: After semi-automated generation is validated
