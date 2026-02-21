# SDLC Tier-Stage Requirements

**Framework**: SDLC 6.1.1
**Last Updated**: January 28, 2026
**Status**: PRODUCTION-READY
**Related**: [Stage Dependencies](../SDLC-Stage-Dependencies.md), [Stage Exit Criteria](../SDLC-Stage-Exit-Criteria.md)

---

## Purpose

This document defines **tier-specific stage requirements** for LITE, PRO, and ENTERPRISE tiers. It answers the critical question: *"When can I safely skip optional stages?"*

**Three Tiers**:
- **LITE**: 1-2 developers, small projects, rapid prototypes
- **PRO**: 3-10 developers, production apps, moderate complexity
- **ENTERPRISE**: 10+ developers, regulated industries, high complexity

**Key Principle**: Stages 00, 01, 02, 04 are **always required**. Stages 03, 05, 06, 07, 08, 09 are **tier-dependent**.

---

## Tier Comparison Matrix

| Stage | LITE (1-2 devs) | PRO (3-10 devs) | ENTERPRISE (10+ devs) | Skip Risk |
|-------|-----------------|-----------------|----------------------|-----------|
| **00-FOUNDATION** | ✅ Required | ✅ Required | ✅ Required | N/A |
| **01-PLANNING** | ✅ Required | ✅ Required | ✅ Required | N/A |
| **02-DESIGN** | ✅ Required | ✅ Required | ✅ Required | N/A |
| **03-INTEGRATE** | ⚠️ Optional | ✅ Recommended | ✅ Required | LOW |
| **04-BUILD** | ✅ Required | ✅ Required | ✅ Required | N/A |
| **05-TEST** | ⚠️ Optional | ✅ Required | ✅ Required | HIGH |
| **06-DEPLOY** | ⚠️ Optional | ✅ Required | ✅ Required | MEDIUM |
| **07-OPERATE** | ⚠️ Optional | ✅ Recommended | ✅ Required | HIGH |
| **08-COLLABORATE** | ⚠️ Optional | ✅ Required | ✅ Required | LOW |
| **09-GOVERN** | ⚠️ Optional* | ⚠️ Optional* | ✅ Required | CRITICAL |

*AI/ML Exception: Always required for AI/ML systems regardless of tier (AI Governance Principles 1-6)

---

## LITE Tier (1-2 Developers)

**Target Projects**:
- Solo developer or pair programming
- Internal tools, prototypes, MVPs
- Short timeline (2-4 weeks)
- No compliance requirements
- No production users (yet)

### Required Stages (4/10)

#### Stage 00: FOUNDATION ✅ REQUIRED
**Why**: Without clear problem statement, you'll build the wrong thing.

**Simplified Exit Criteria**:
- Business case (1 page)
- Problem statement (1 paragraph)
- 3 user interviews (minimum)
- No evidence vault required

**Time Investment**: 2-3 days

---

#### Stage 01: PLANNING ✅ REQUIRED
**Why**: Without requirements, you'll miss critical features.

**Simplified Exit Criteria**:
- Requirements doc (1-2 pages)
- Basic API spec (if applicable)
- 5-10 user stories
- No legal review required (unless regulated)

**Time Investment**: 3-5 days

---

#### Stage 02: DESIGN ✅ REQUIRED
**Why**: Without architecture, code becomes unmaintainable mess.

**Simplified Exit Criteria**:
- 2 ADRs minimum (technology choice, architecture pattern)
- Basic architecture diagram (single C4 Level 2)
- No security architecture required (unless handling sensitive data)

**Time Investment**: 2-4 days

---

#### Stage 04: BUILD ✅ REQUIRED
**Why**: This is the actual development work.

**Simplified Exit Criteria**:
- Code complete
- Unit tests (40%+ coverage)
- README.md with setup instructions
- No code review required (if solo)

**Time Investment**: 1-4 weeks (depends on scope)

---

### Optional Stages (6/10)

#### Stage 03: INTEGRATE ⚠️ OPTIONAL

**Skip If**:
- ✅ No third-party APIs (no Stripe, Twilio, SendGrid)
- ✅ Monolithic application (no microservices)
- ✅ No external integrations

**Required If**:
- ❌ Payment integrations (Stripe, PayPal)
- ❌ Third-party APIs (Twilio, SendGrid)
- ❌ Microservices architecture

**Skip Risk Level**: **LOW**  
**Skip Consequence**: Integration issues discovered during BUILD instead of INTEGRATE (adds 10-20% time)

**Decision Tree**:
```
Do you integrate with external APIs?
├─ No → SKIP Stage 03 ✅
└─ Yes
    ├─ Critical APIs (payments) → REQUIRED ❌
    └─ Non-critical APIs (email) → OPTIONAL ⚠️
```

**Time Saved**: 1-2 days  
**Time Cost if Skip**: +2-3 days debugging integration issues

---

#### Stage 05: TEST ⚠️ OPTIONAL

**Skip If**:
- ✅ Unit tests only (no integration/E2E tests)
- ✅ Single developer (no QA team)
- ✅ Internal prototype (no production deployment)

**Required If**:
- ❌ User-facing application
- ❌ Financial/health data
- ❌ Production users expected

**Skip Risk Level**: **HIGH**  
**Skip Consequence**: Bugs reach production, user complaints, technical debt

**Recommendation**: **Always include for production apps** (even LITE tier)

**Decision Tree**:
```
Is this going to production?
├─ No (prototype) → SKIP Stage 05 ⚠️
└─ Yes
    ├─ Internal tool → OPTIONAL (unit tests sufficient)
    └─ User-facing → REQUIRED ❌
```

**Time Saved**: 2-3 days  
**Time Cost if Skip**: +5-10 days fixing production bugs

---

#### Stage 06: DEPLOY ⚠️ OPTIONAL

**Skip If**:
- ✅ Local development only
- ✅ No production users
- ✅ Prototype/demo

**Required If**:
- ❌ Production deployment planned
- ❌ Users exist (even 1 user)

**Skip Risk Level**: **MEDIUM**  
**Skip Consequence**: No deployment strategy, manual deployments, downtime

**Recommendation**: **Always include for shipped products**

**Decision Tree**:
```
Will this run in production?
├─ No (local demo) → SKIP Stage 06 ✅
└─ Yes → REQUIRED ❌
```

**Time Saved**: 1 day  
**Time Cost if Skip**: +3-5 days creating ad-hoc deployment process

---

#### Stage 07: OPERATE ⚠️ OPTIONAL

**Skip If**:
- ✅ No production monitoring needed
- ✅ Internal tool with no SLA
- ✅ No production users

**Required If**:
- ❌ SLA commitments
- ❌ Production users
- ❌ Revenue-generating app

**Skip Risk Level**: **HIGH**  
**Skip Consequence**: No production monitoring, outages undetected, user churn

**Recommendation**: **Required for any production app**

**Decision Tree**:
```
Do you need to know if your app is down?
├─ No (internal tool, no users) → SKIP Stage 07 ⚠️
└─ Yes → REQUIRED ❌
```

**Time Saved**: 1 day  
**Time Cost if Skip**: Unknown downtime, lost revenue, user complaints

---

#### Stage 08: COLLABORATE ⚠️ OPTIONAL

**Skip If**:
- ✅ Solo developer (no team)
- ✅ No external stakeholders (PM, designer, QA)

**Required If**:
- ❌ 2+ developers
- ❌ External stakeholders involved

**Skip Risk Level**: **LOW**  
**Skip Consequence**: No code reviews, lower code quality, knowledge silos

**Recommendation**: Even solo developers benefit from peer reviews (optional)

**Decision Tree**:
```
Are you working alone?
├─ Yes → SKIP Stage 08 ✅
└─ No (2+ people) → REQUIRED ❌
```

**Time Saved**: Ongoing (no meetings, no code reviews)  
**Time Cost if Skip**: Lower code quality, no knowledge transfer

---

#### Stage 09: GOVERN ⚠️ OPTIONAL*

**Skip If**:
- ✅ Internal tool
- ✅ No compliance requirements (no HIPAA, GDPR, SOC 2)
- ✅ No regulated data
- ✅ **Not an AI/ML system** (critical exception)

**Required If**:
- ❌ Regulated industry (healthcare, finance, government)
- ❌ Compliance required (SOC 2, HIPAA, GDPR)
- ❌ **AI/ML system** (always required, see exception below)

**Skip Risk Level**: **CRITICAL**  
**Skip Consequence**: Legal/compliance violations, fines, lawsuits

**AI/ML Exception**: **Always required for AI/ML systems regardless of tier**
- AI Governance Principles 1-6 must be followed
- Bias testing required
- Data privacy validation mandatory
- Model explainability documented

**Decision Tree**:
```
Is this an AI/ML system?
├─ Yes → REQUIRED (AI Governance Principles 1-6) ❌
└─ No
    ├─ Regulated industry? → REQUIRED ❌
    ├─ Compliance requirements? → REQUIRED ❌
    └─ Internal tool, no compliance → SKIP ✅
```

**Time Saved**: 1-2 weeks (audit execution)  
**Time Cost if Skip**: Fines, lawsuits, reputational damage

---

## PRO Tier (3-10 Developers)

**Target Projects**:
- Small to medium teams
- Production applications
- Moderate complexity
- Some compliance requirements
- Active user base

### Required Stages (7/10)

**Always Required**: 00, 01, 02, 03, 04, 05, 06, 07  
**Optional**: 08 (if team < 3), 09 (if no compliance)

### Key Differences from LITE

| Stage | LITE | PRO | Reason |
|-------|------|-----|--------|
| **03-INTEGRATE** | Optional | ✅ Required | Teams use more integrations (APIs, microservices) |
| **05-TEST** | Optional | ✅ Required | QA team exists, production users expect quality |
| **06-DEPLOY** | Optional | ✅ Required | Production deployments mandatory |
| **07-OPERATE** | Optional | ✅ Required | SLA commitments, monitoring needed |
| **08-COLLABORATE** | Optional | ✅ Required | 3+ developers need coordination |
| **09-GOVERN** | Optional | ⚠️ Optional* | Required if compliance (SOC 2, HIPAA) or AI/ML |

*AI/ML Exception: Always required for AI/ML systems

### Enhanced Exit Criteria

**Compared to LITE**:
- **Stage 02**: 5+ ADRs (not 2)
- **Stage 04**: 60%+ code coverage (not 40%)
- **Stage 05**: Integration + E2E tests (not just unit tests)
- **Stage 06**: Automated CI/CD (not manual deployment)
- **Stage 07**: Full observability stack (not basic monitoring)

---

## ENTERPRISE Tier (10+ Developers)

**Target Projects**:
- Large teams
- Regulated industries
- High complexity
- Mandatory compliance
- Mission-critical systems

### Required Stages (10/10)

**All stages required** - No optional stages for ENTERPRISE tier.

**Rationale**:
- Large teams need full coordination (Stage 08)
- Compliance mandatory for regulated industries (Stage 09)
- All quality gates enforced
- Evidence vault mandatory for all artifacts

### Enhanced Requirements

| Stage | ENTERPRISE Enhancement |
|-------|------------------------|
| **00-FOUNDATION** | 5+ user interviews (not 3), evidence vault mandatory |
| **01-PLANNING** | Legal review mandatory, formal stakeholder signoff |
| **02-DESIGN** | Security architecture required, formal design reviews |
| **03-INTEGRATE** | Contract testing mandatory, integration partner agreements |
| **04-BUILD** | Code review mandatory, 80%+ code coverage |
| **05-TEST** | Performance testing, accessibility audits, security testing |
| **06-DEPLOY** | Blue-green deployment, canary releases, rollback tested |
| **07-OPERATE** | SLO tracking, on-call rotation, incident drills |
| **08-COLLABORATE** | Formal sprint ceremonies, cross-team sync meetings |
| **09-GOVERN** | Full audit (SOC 2, ISO 27001), certifications, ongoing governance |

---

## AI/ML Governance Exception (CRITICAL)

**Rule**: Stage 09 (GOVERN) is **always required** for AI/ML systems **regardless of tier**.

**Rationale**:
- AI systems have unique risks (bias, data privacy, model explainability)
- AI Governance Principles 1-6 must be followed
- Legal/ethical implications of AI decisions

**AI Governance Principles (from SDLC 6.1.1)**:
1. **Transparency**: Model decisions must be explainable
2. **Fairness**: Bias testing on protected classes (race, gender, age)
3. **Privacy**: Data privacy validation (GDPR, CCPA compliance)
4. **Accountability**: Audit trail for AI decisions
5. **Safety**: Adversarial testing, robustness validation
6. **Human Oversight**: Human-in-the-loop for critical decisions

**Required Activities**:
- Bias testing (gender, race, age, disability)
- Data privacy audit (PII handling, consent)
- Model explainability documentation (SHAP, LIME)
- Audit trail for model decisions
- Adversarial testing (input manipulation)
- Human oversight procedures

**Example**:
```yaml
Project: Instagram Clone (LITE Tier)
  AI/ML Component: Image classification (detect NSFW content)
  Stage 09 Required: YES (AI Governance Principles 1-6)
  Activities:
    - Bias testing: Test on diverse demographics
    - Privacy: Ensure image metadata stripped
    - Explainability: Document why image flagged
    - Audit trail: Log all classification decisions
```

---

## Decision Tree: When to Skip Stages

### Overall Decision Process

```
1. What tier are you? (LITE, PRO, ENTERPRISE)
   └─ ENTERPRISE → All 10 stages required ❌

2. Is this an AI/ML system?
   ├─ Yes → Stage 09 required regardless of tier ❌
   └─ No → Continue

3. Is this going to production?
   ├─ No (prototype) → Can skip Stages 05, 06, 07 ⚠️
   └─ Yes → Continue

4. Do you have external integrations?
   ├─ No → Can skip Stage 03 ✅
   └─ Yes → Stage 03 required ❌

5. Do you have production users?
   ├─ No → Can skip Stages 06, 07 ⚠️
   └─ Yes → Stages 06, 07 required ❌

6. Are you working alone?
   ├─ Yes → Can skip Stage 08 ✅
   └─ No → Stage 08 required ❌

7. Are you in a regulated industry?
   ├─ Yes → Stage 09 required ❌
   └─ No → Can skip Stage 09 ✅
```

---

## Skip Risk Matrix

| Stage | Skip If | Required If | Skip Risk | Time Saved | Time Cost |
|-------|---------|-------------|-----------|------------|-----------|
| **03-INTEGRATE** | No APIs | Payments, APIs | LOW | 1-2 days | +2-3 days |
| **05-TEST** | Prototype | Production | HIGH | 2-3 days | +5-10 days |
| **06-DEPLOY** | Local only | Production | MEDIUM | 1 day | +3-5 days |
| **07-OPERATE** | No users | Production | HIGH | 1 day | Unknown downtime |
| **08-COLLABORATE** | Solo | 2+ devs | LOW | Ongoing | Lower quality |
| **09-GOVERN** | Internal tool | Regulated/AI | CRITICAL | 1-2 weeks | Fines, lawsuits |

---

## Cost-Benefit Analysis

### Example: LITE Tier Project (Instagram Clone Prototype)

**Scenario**: Solo developer, 4-week timeline, no production users yet

| Stage | Required? | Time Investment | Skip Savings | Skip Risk | Decision |
|-------|-----------|-----------------|--------------|-----------|----------|
| 00-FOUNDATION | ✅ Required | 2 days | N/A | N/A | DO |
| 01-PLANNING | ✅ Required | 3 days | N/A | N/A | DO |
| 02-DESIGN | ✅ Required | 2 days | N/A | N/A | DO |
| 03-INTEGRATE | Optional | 1 day | 1 day | LOW | SKIP (no APIs) |
| 04-BUILD | ✅ Required | 2 weeks | N/A | N/A | DO |
| 05-TEST | Optional | 2 days | 2 days | HIGH | DO (prototype → production) |
| 06-DEPLOY | Optional | 1 day | 1 day | MEDIUM | SKIP (no users yet) |
| 07-OPERATE | Optional | 1 day | 1 day | HIGH | SKIP (no users yet) |
| 08-COLLABORATE | Optional | Ongoing | Ongoing | LOW | SKIP (solo dev) |
| 09-GOVERN | Optional | 1 week | 1 week | CRITICAL | SKIP (internal tool) |

**Total Time**: 17 days (vs 26 days full SDLC)  
**Time Saved**: 9 days (35% reduction)  
**Risk Level**: LOW (prototype, no production users)

**Decision**: APPROVED for LITE tier prototype

---

## Frequently Asked Questions

### Q1: Can I skip Stage 05 (TEST) for LITE tier?
**A**: Only if it's a prototype with no production users. For any production app, Stage 05 is strongly recommended even for LITE tier. Skip risk is HIGH (bugs reach production).

### Q2: What if my LITE tier project has payment integrations?
**A**: Stage 03 (INTEGRATE) becomes required. Payment integrations are critical and need dedicated integration testing. Skip risk is CRITICAL.

### Q3: Can ENTERPRISE tier skip any stages?
**A**: No. All 10 stages required for ENTERPRISE tier. Large teams and regulated industries need full SDLC compliance.

### Q4: What about AI/ML projects in LITE tier?
**A**: Stage 09 (GOVERN) is always required for AI/ML systems, even LITE tier. AI Governance Principles 1-6 must be followed. This is a hard requirement.

### Q5: Can I upgrade from LITE to PRO mid-project?
**A**: Yes. Go back and complete skipped stages (03, 05, 06, 07). This is called "Stage Backfill" and is documented in Stage Transition Checklist.

---

## Related Documents

- [SDLC-Stage-Dependencies.md](../SDLC-Stage-Dependencies.md) - Stage dependencies
- [SDLC-Stage-Exit-Criteria.md](../SDLC-Stage-Exit-Criteria.md) - Stage completion criteria
- [SDLC-Sprint-Governance.md](../Governance-Compliance/SDLC-Sprint-Governance.md) - Sprint-stage coordination
- [Stage-Transition-Checklist.md](../../05-Templates-Tools/05-Checklists/Stage-Transition-Checklist.md) - Stage transition checklists
- [AI Governance Principles](../../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md) - AI/ML governance requirements

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 2.0 | 2026-01-28 | Folder flattening (remove layer 3), version upgrade to 6.0.0 | CTO (Tai) |
| 1.0 | 2026-01-28 | Initial version - Tier-specific stage requirements with AI/ML exception | CTO (Tai) |

---

**Last Updated**: January 28, 2026
**Framework Version**: SDLC 6.1.1
**Status**: PRODUCTION-READY
