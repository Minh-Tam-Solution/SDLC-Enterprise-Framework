# ✅ AI Compliance Checker - Stage 09 (GOVERN)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 09 - GOVERN (Governance & Compliance)
**Time Savings**: 95%
**Authority**: CTO Office

---

## Purpose

Automated **compliance checking** for SDLC 5.0.0 projects covering regulatory, security, process, and team collaboration standards. Supports real-time detection with <5 min violation alerts.

---

## AI Prompts by Compliance Type

### 1. SDLC Process Compliance Check

```yaml
System Prompt:
  You are checking SDLC 5.0.0 process compliance.
  Validate: 10-stage structure, 6 pillars, gate evidence, documentation standards.
  Apply tier-appropriate requirements.
  Reference: SDLC-Core-Methodology.md and sdlc_validator.py

User Prompt Template:
  "Check SDLC compliance for:

   Project Path: [/path/to/project]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]

   Check Areas:
   - [ ] Folder structure (10 stages: 00-09)
   - [ ] Documentation naming (kebab-case, no versions)
   - [ ] Code file naming (snake_case/camelCase)
   - [ ] Gate evidence presence
   - [ ] Team Collaboration standards (5.0.0)

   Report Format: [Summary | Detailed | JSON]"

Output Format:
  # SDLC Compliance Check Results

  **Project**: [Name]
  **Tier**: [Tier]
  **Scan Date**: [YYYY-MM-DD HH:MM]
  **Compliance Score**: [X]%

  ---

  ## Quick Summary

  | Category | Pass | Fail | Score |
  |----------|------|------|-------|
  | Folder Structure | [X] | [Y] | [Z]% |
  | Documentation | [X] | [Y] | [Z]% |
  | Code Naming | [X] | [Y] | [Z]% |
  | Gate Evidence | [X] | [Y] | [Z]% |
  | Team Collaboration | [X] | [Y] | [Z]% |
  | **Total** | [X] | [Y] | [Z]% |

  ---

  ## Violations Found

  ### Critical (Must Fix)
  | File/Folder | Rule | Issue | Fix |
  |-------------|------|-------|-----|
  | docs/04-testing | Missing | Stage folder not found | Create 04-Testing-Quality/ |
  | user_guide.md | Naming | Should be kebab-case | Rename to user-guide.md |

  ### Warnings (Should Fix)
  | File/Folder | Rule | Issue | Fix |
  |-------------|------|-------|-----|
  | Team-Collaboration/ | Missing RACI | No RACI matrix | Create per SDLC 5.0.0 |

  ---

  ## Auto-Fix Commands

  ```bash
  # Create missing folders
  mkdir -p docs/04-Testing-Quality

  # Rename files
  mv docs/user_guide.md docs/user-guide.md

  # Run validator
  python sdlc_validator.py --project /path/to/project --fix
  ```

  ---

  ## Next Steps
  1. Fix critical violations (required for gate approval)
  2. Address warnings before next sprint
  3. Re-run compliance check
```

### 2. Security Standards Compliance

```yaml
System Prompt:
  You are checking security compliance against OWASP ASVS and NIST SSDF.
  Check: Authentication, authorization, cryptography, data protection.
  Provide specific remediation guidance.

User Prompt Template:
  "Check security compliance for:

   Project: [Name]
   Baseline: [OWASP ASVS Level 1 | 2 | 3]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]

   Code/Config to Check:
   [Paste relevant code or describe architecture]

   Focus Areas:
   - [ ] Authentication mechanisms
   - [ ] Authorization controls
   - [ ] Cryptography usage
   - [ ] Secrets management
   - [ ] Input validation"

Output Format:
  # Security Compliance Check

  **Project**: [Name]
  **Baseline**: OWASP ASVS Level [X]
  **Score**: [Y]/[Z] requirements ([%])

  ---

  ## Requirements Checked

  ### V2: Authentication
  | ID | Requirement | Status | Notes |
  |----|-------------|--------|-------|
  | V2.1.1 | Password length ≥12 | ✅ PASS | 12 chars enforced |
  | V2.1.2 | Password complexity | ✅ PASS | No sequential chars |
  | V2.8.1 | MFA available | 🟡 PARTIAL | Only for admin |

  ### V3: Session Management
  | ID | Requirement | Status | Notes |
  |----|-------------|--------|-------|
  | V3.5.1 | Token expiry | ✅ PASS | 15 min JWT |
  | V3.5.2 | Refresh token rotation | ✅ PASS | One-time use |

  ### V5: Validation
  | ID | Requirement | Status | Notes |
  |----|-------------|--------|-------|
  | V5.1.1 | Input validation | 🔴 FAIL | SQL injection in user input |
  | V5.2.1 | HTML encoding | ✅ PASS | React auto-escapes |

  ---

  ## Critical Findings

  ### V5.1.1 - SQL Injection Vulnerability
  - **Location**: `backend/app/api/routes/users.py:45`
  - **Risk**: HIGH - Data exfiltration possible
  - **Fix**:
    ```python
    # Before (vulnerable)
    query = f"SELECT * FROM users WHERE name = '{user_input}'"

    # After (safe)
    query = "SELECT * FROM users WHERE name = :name"
    result = db.execute(query, {"name": user_input})
    ```

  ---

  ## Remediation Priority

  | Finding | Severity | Effort | Priority |
  |---------|----------|--------|----------|
  | SQL Injection | Critical | 1 hour | P0 |
  | MFA for all users | Medium | 4 hours | P1 |
```

### 3. Team Collaboration Compliance (NEW in 5.0.0)

```yaml
System Prompt:
  You are checking Team Collaboration compliance per SDLC 5.0.0 standards.
  Validate: Communication protocols, RACI matrices, escalation paths.
  Apply tier-appropriate requirements.
  Reference: Documentation-Standards/Team-Collaboration/

User Prompt Template:
  "Check Team Collaboration compliance for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Team Size: [Number]
   Work Model: [Co-located | Remote | Hybrid | Multi-timezone]

   Existing Documents:
   - [ ] Team Communication Protocol
   - [ ] Team Collaboration Protocol
   - [ ] Escalation Path Standards
   - [ ] RACI Matrix

   Team Structure:
   - [Team 1]: [Size], [Role]
   - [Team 2]: [Size], [Role]"

Output Format:
  # Team Collaboration Compliance Check

  **Project**: [Name]
  **Tier**: [Tier]
  **Team Size**: [X] people
  **Compliance Score**: [Y]%

  ---

  ## Requirements by Tier

  | Document | Required | Present | Status |
  |----------|----------|---------|--------|
  | Team Communication Protocol | STANDARD+ | ✅ | PASS |
  | Team Collaboration Protocol | PROFESSIONAL+ | ❌ | MISSING |
  | Escalation Path Standards | PROFESSIONAL+ | 🟡 | PARTIAL |
  | RACI Matrix | PROFESSIONAL+ | ❌ | MISSING |

  ---

  ## Detailed Analysis

  ### Communication Protocol
  **Status**: ✅ COMPLIANT

  | Requirement | Status | Notes |
  |-------------|--------|-------|
  | Channel definitions | ✅ | 5 channels defined |
  | Response SLAs | ✅ | Tier-appropriate SLAs |
  | Meeting cadence | ✅ | Daily + weekly |

  ### Escalation Path
  **Status**: 🟡 PARTIAL

  | Level | Required | Defined | Issue |
  |-------|----------|---------|-------|
  | L0 Self-service | ✅ | ✅ | OK |
  | L1 Team Lead | ✅ | ✅ | OK |
  | L2 Manager | ✅ | ❌ | Missing contact |
  | L3 Executive | ✅ | ❌ | Not defined |

  ### RACI Matrix
  **Status**: ❌ MISSING

  **Required for PROFESSIONAL tier**:
  - All deliverables need RACI
  - Each row must have exactly ONE 'A'
  - At least ONE 'R' per row

  ---

  ## Remediation

  ### Required Actions
  1. **Create RACI Matrix** (Effort: 2 hours)
     - Use template: [1-AI-Tools/collaboration/raci-matrix-generator.md]

  2. **Complete Escalation Path** (Effort: 30 min)
     - Add L2 and L3 contacts

  3. **Create Team Collaboration Protocol** (Effort: 1 hour)
     - Use template: [team-protocol-generator.md]

  ---

  ## Auto-Generate Commands

  ```bash
  # Generate RACI Matrix
  sdlcctl generate raci --project [name] --teams "Team A,Team B"

  # Validate after changes
  sdlcctl validate --team-collaboration
  ```
```

### 4. Regulatory Compliance Check

```yaml
System Prompt:
  You are checking regulatory compliance for specific jurisdictions.
  Cover: Data protection (GDPR, PDPA), industry-specific (HIPAA, PCI-DSS).
  Provide practical remediation guidance.

User Prompt Template:
  "Check regulatory compliance for:

   Project: [Name]
   Industry: [Healthcare | Finance | E-commerce | General]
   Jurisdictions: [Vietnam, EU, US, etc.]

   Regulations to Check:
   - [ ] Vietnamese regulations (BHXH, VAT)
   - [ ] GDPR (EU data protection)
   - [ ] PDPA (data protection general)
   - [ ] PCI-DSS (payment card)
   - [ ] HIPAA (healthcare)

   Data Types Handled:
   - Personal data: [Yes/No]
   - Payment data: [Yes/No]
   - Health data: [Yes/No]"

Output Format:
  # Regulatory Compliance Check

  **Project**: [Name]
  **Industry**: [Industry]
  **Jurisdictions**: [List]
  **Overall Status**: [Compliant | Partially Compliant | Non-Compliant]

  ---

  ## Applicable Regulations

  | Regulation | Applies | Status | Score |
  |------------|---------|--------|-------|
  | Vietnamese BHXH | ✅ | COMPLIANT | 100% |
  | Vietnamese VAT | ✅ | COMPLIANT | 100% |
  | GDPR | ✅ | PARTIAL | 85% |
  | PDPA | ✅ | COMPLIANT | 95% |
  | PCI-DSS | ❌ | N/A | - |

  ---

  ## GDPR Compliance (85%)

  | Requirement | Article | Status | Gap |
  |-------------|---------|--------|-----|
  | Lawful basis | Art. 6 | ✅ | - |
  | Consent management | Art. 7 | ✅ | - |
  | Data subject rights | Art. 15-22 | 🟡 | Missing deletion |
  | Data protection officer | Art. 37 | ✅ | - |
  | Breach notification | Art. 33-34 | ❌ | No process |

  ### Required Actions
  1. **Implement right to deletion** (Art. 17)
     - Add DELETE /api/users/{id}/data endpoint
     - Ensure cascade deletion

  2. **Create breach notification process** (Art. 33)
     - Define 72-hour notification SLA
     - Create incident template

  ---

  ## Vietnamese Regulations (100%)

  | Regulation | Requirement | Status | Notes |
  |------------|-------------|--------|-------|
  | BHXH Employer | 17.5% contribution | ✅ | Configured |
  | BHXH Employee | 8% contribution | ✅ | Configured |
  | VAT Rate | 10% standard | ✅ | Applied |
  | FIFO Inventory | First-in-first-out | ✅ | Implemented |

  ---

  ## Recommendations

  | Priority | Action | Regulation | Effort |
  |----------|--------|------------|--------|
  | P0 | Add breach notification | GDPR Art. 33 | 1 week |
  | P1 | Implement data deletion | GDPR Art. 17 | 3 days |
```

---

## Automated Compliance Scanning

### Pre-commit Hook Integration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: sdlc-compliance
        name: SDLC 5.0.0 Compliance Check
        entry: python sdlc_validator.py --quick
        language: system
        pass_filenames: false
        stages: [commit]

      - id: security-check
        name: Security Standards Check
        entry: semgrep --config=p/owasp-top-ten
        language: system
        types: [python]
```

### CI/CD Integration

```yaml
# GitHub Actions
name: Compliance Gates

on: [push, pull_request]

jobs:
  sdlc-compliance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: SDLC Structure Check
        run: python sdlc_validator.py --tier PROFESSIONAL

      - name: Team Collaboration Check
        run: python sdlc_validator.py --team-collaboration

      - name: Security Scan
        run: semgrep --config=p/owasp-top-ten

      - name: Upload Compliance Report
        uses: actions/upload-artifact@v3
        with:
          name: compliance-report
          path: reports/compliance.json
```

---

## Tier-Appropriate Compliance Requirements

| Compliance Area | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-----------------|------|----------|--------------|------------|
| SDLC Structure | Basic | 5 stages | 10 stages | 10 + gates |
| Documentation | README | + CLAUDE.md | Full docs | + audit trail |
| Security | Basic | OWASP L1 | OWASP L2 | OWASP L2+ |
| Team Collaboration | N/A | Communication | Full protocols | + SLAs |
| Regulatory | N/A | As needed | Required | Certified |

---

## Success Metrics

**Compliance Automation** (Stage 09):
- ✅ 95% time savings on compliance checks
- ✅ <5 min violation detection
- ✅ Zero compliance surprises
- ✅ 100% audit trail completeness

**BFlow Validation**:
- 100% Vietnamese compliance (BHXH, VAT, FIFO)
- Automated CEO/CTO dashboards
- Zero compliance issues in production

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CTO Office
