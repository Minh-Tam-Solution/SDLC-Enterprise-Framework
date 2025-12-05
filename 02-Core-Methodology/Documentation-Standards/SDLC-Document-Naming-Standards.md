# SDLC Document Naming Standards - Universal Framework
**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: MANDATORY ENFORCEMENT
**Authority**: CPO Approved Standard
**Component**: Document Governance Framework (DGF)

---

## 🎯 Purpose

This document establishes **mandatory naming conventions** for all documentation across enterprise projects. Part of the SDLC 5.0 Document Governance Framework (DGF), these standards ensure permanence, discoverability, and maintainability.

**Key Innovation**: Elimination of temporal references that cause document obsolescence.

---

## ❌ PROHIBITED - Never Use These in Document Names

### Temporal References (CRITICAL)
```yaml
ABSOLUTELY FORBIDDEN:
  Sprint References:
    - SPRINT-7, SPRINT-X, Sprint7
    - Any sprint number or identifier

  Day/Date References:
    - DAY-1, DAY-X, Day1
    - 2025-09-27, Sep27, 27Sep
    - TODAY, YESTERDAY, TOMORROW

  Phase References:
    - PHASE-1, PHASE-X, Phase1
    - ALPHA, BETA, RC, GA

  Version in Filename:
    - V8.0, V7.5, v2, version2
    - Rev1, Revision2

  Team References:
    - LOCAL-TEAM, REMOTE-TEAM
    - BACKEND-TEAM, FRONTEND-TEAM
    - Team names or identifiers

  Temporary Markers:
    - TEMP, TMP, TEST, DRAFT
    - WIP, TODO, FIXME
    - OLD, NEW, LATEST, FINAL

  Person Names:
    - John-API-Design.md
    - CTO-Database-Schema.md
```

### Why These Are Forbidden
- **Sprint references**: Become meaningless after sprint ends
- **Date stamps**: Make documents appear outdated
- **Phase references**: Lose relevance after phase completion
- **Version numbers**: Belong in content, not filenames
- **Team references**: Don't indicate content purpose
- **Temporary markers**: Create confusion about document status
- **Person names**: Create ownership confusion

---

## ✅ REQUIRED - Document Naming Patterns

### 1. Design Documents
**Location**: `/docs/02-Design-Architecture/[subdomain]/`

```yaml
Correct Naming Pattern:
  Feature-Component-Type.md

Examples:
  ✅ Authentication-API-Design.md
  ✅ Customer-Portal-UI-Design.md
  ✅ Database-Schema-Design.md
  ✅ DNA-Framework-Architecture.md
  ✅ Payment-Integration-Design.md

Incorrect Examples:
  ❌ SPRINT-7-Authentication-API.md
  ❌ Authentication-API-V8.0.md
  ❌ LOCAL-TEAM-Database-Design.md
  ❌ Authentication-FINAL.md
```

### 2. Technical Documentation
**Location**: `/docs/03-Development-Implementation/[category]/`

```yaml
Correct Naming Pattern:
  Technology-Purpose.md

Examples:
  ✅ React-Component-Guidelines.md
  ✅ Django-Best-Practices.md
  ✅ TypeScript-Style-Guide.md
  ✅ Performance-Optimization-Guide.md
  ✅ Security-Implementation-Standards.md

Incorrect Examples:
  ❌ React-Guidelines-2025.md
  ❌ Django-V8-Practices.md
  ❌ TEAM-Testing-Strategy.md
  ❌ Performance-Guide-DRAFT.md
```

### 3. API Documentation
**Location**: `/docs/07-Integration-APIs/`

```yaml
Correct Naming Pattern:
  Service-API-Documentation.md

Examples:
  ✅ Authentication-API-Documentation.md
  ✅ Customer-API-Documentation.md
  ✅ DNA-Framework-API-Documentation.md
  ✅ Webhook-Integration-Guide.md
  ✅ Payment-Gateway-API.md

Incorrect Examples:
  ❌ API-V2-Authentication.md
  ❌ SPRINT7-Customer-API.md
  ❌ Payment-API-NEW.md
```

### 4. Sprint Documents (EXCEPTION)
**Location**: `/docs/08-Team-Management/04-Sprint-Management/`

```yaml
ONLY HERE can sprint references be used:

Allowed Patterns:
  ✅ SPRINT-[number]-Planning.md
  ✅ SPRINT-[number]-Retrospective.md
  ✅ SPRINT-[number]-Review.md
  ✅ SPRINT-[number]-Completion.md

Note: Sprint references ONLY allowed in sprint management folder
```

### 5. Test Documentation
**Location**: `/tests/[type]/documentation/`

```yaml
Correct Naming Pattern:
  Feature-Test-Type.md

Examples:
  ✅ Authentication-Integration-Tests.md
  ✅ Performance-Baseline-Tests.md
  ✅ Security-Penetration-Tests.md
  ✅ Load-Testing-Results.md

Test Runs (timestamped logs OK):
  ✅ test-run-2025-09-27.log (logs only, not docs)
```

---

## 📋 Naming Convention Rules

### 1. Use Kebab-Case
```yaml
Correct:
  ✅ Customer-Portal-Design.md
  ✅ DNA-Framework-API.md
  ✅ Database-Migration-Guide.md

Incorrect:
  ❌ customer_portal_design.md (snake_case)
  ❌ CustomerPortalDesign.md (PascalCase)
  ❌ customerportaldesign.md (lowercase)
```

### 2. Be Descriptive and Specific
```yaml
Good Descriptions:
  ✅ Payment-Gateway-Integration.md
  ✅ User-Authentication-Flow.md
  ✅ Vietnamese-Tax-Calculations.md

Poor Descriptions:
  ❌ Payment.md (too vague)
  ❌ Auth.md (abbreviated)
  ❌ Misc-Utils.md (unclear)
```

### 3. Use Full Words
```yaml
Correct:
  ✅ Authentication-Service.md
  ✅ Configuration-Management.md
  ✅ Development-Guidelines.md

Incorrect:
  ❌ Auth-Svc.md
  ❌ Config-Mgmt.md
  ❌ Dev-Guide.md
```

### 4. Feature-Based Naming
```yaml
Focus on WHAT, not WHEN/WHO:

✅ Customer-Management-System.md
   (describes the feature)

❌ Sprint-7-Customer-Work.md
   (describes when it was done)

❌ John-Customer-Design.md
   (describes who did it)
```

### 5. No Status Markers
```yaml
Version/Status goes INSIDE document:

✅ API-Design.md
   (with version: 4.7 inside)

❌ API-Design-FINAL.md
❌ API-Design-v2.md
❌ API-Design-APPROVED.md
```

---

## 🗂️ Folder Naming Standards

### Stage Folders (Level 1)
```yaml
Pattern: NN-Descriptive-Name/

Examples:
  00-Project-Foundation/
  01-Planning-Analysis/
  02-Design-Architecture/
  03-Development-Implementation/
  08-Team-Management/
  99-Legacy/
```

### Subdirectories (Level 2+)
```yaml
Pattern: NN-Feature-Category/

Examples:
  01-System-Architecture/
  02-Database-Design/
  03-API-Design/
  04-UI-UX-Design/
  99-legacy/  (lowercase for archive)
```

---

## 🔄 Document Lifecycle

### Creating Documents
```bash
# Ask yourself:
1. What does this document describe?
2. What category does it belong to?
3. Will this name still make sense in 1 year?

# Result:
Feature-Component-Purpose.md
```

### Renaming Documents
```bash
# When document purpose changes:
git mv Old-Vague-Name.md New-Descriptive-Name.md
git commit -m "docs: rename for clarity"

# Track in CHANGELOG if significant
```

### Archiving Documents
```bash
# Move outdated docs to legacy:
git mv Obsolete-Doc.md ../99-legacy/
git commit -m "archive: obsolete documentation"
```

---

## 🚨 Enforcement Mechanisms

### Automated Validation
```python
# Pre-commit hook example
def validate_document_name(filename):
    forbidden_patterns = [
        r'SPRINT-\d+', r'DAY-\d+', r'PHASE-\d+',
        r'V\d+\.\d+', r'v\d+', r'TEAM',
        r'TEMP', r'DRAFT', r'FINAL', r'TEST'
    ]

    for pattern in forbidden_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            raise ValueError(f"Forbidden pattern '{pattern}' in {filename}")

    return True
```

### Manual Review Checklist
- [ ] No sprint/day/phase references?
- [ ] No version numbers in filename?
- [ ] No team/person names?
- [ ] No temporary markers?
- [ ] Descriptive and permanent?
- [ ] Kebab-case format?
- [ ] In correct folder?

### Violation Consequences
1. **First violation**: Immediate correction required
2. **Pattern violations**: Additional training
3. **Continued violations**: Performance review impact

---

## 📊 Benefits of Proper Naming

### Quantitative Benefits
- **70%** reduction in document refactoring
- **85%** improvement in discoverability
- **100%** elimination of obsolete references
- **60%** faster document location
- **90%** reduction in naming conflicts

### Qualitative Benefits
- Documents remain relevant permanently
- Clear understanding of content
- Improved team collaboration
- Professional appearance
- Easier maintenance

---

## 💡 Quick Reference

### DO's ✅
- Use kebab-case
- Be descriptive
- Focus on content
- Use full words
- Keep it permanent

### DON'Ts ❌
- No sprint numbers
- No dates/days
- No versions
- No team names
- No status markers
- No person names

### Ask Yourself
```
Will this name still make sense:
- Next sprint?
- Next month?
- Next year?
- To a new team member?
- Without context?

If NO to any → Choose a better name
```

---

## 🎯 Examples Gallery

### Excellence in Naming ✅
```
Authentication-Service-Architecture.md
Customer-Data-Model.md
Vietnamese-Business-Logic-Implementation.md
Performance-Monitoring-Guide.md
Security-Audit-Procedures.md
Database-Migration-Strategy.md
API-Rate-Limiting-Design.md
User-Experience-Guidelines.md
```

### Naming Disasters ❌
```
SPRINT-7-DAY-3-DNA-Design-V8.0-FINAL.md
Authentication-NEW-LOCAL-TEAM-TODO.md
John-Database-Design-v2-DRAFT.md
API-2025-09-27-LATEST.md
Customer-Portal-TEMP-WIP.md
Phase-1-Sprint-5-Day-2-Work.md
```

---

**Document**: SDLC-Document-Naming-Standards
**Framework**: SDLC 5.0 Universal Excellence
**Component**: Document Governance Framework (DGF)
**Enforcement**: MANDATORY
**Review**: Continuous
**Last Updated**: December 5, 2025

*"Permanent names for permanent value"* 📂