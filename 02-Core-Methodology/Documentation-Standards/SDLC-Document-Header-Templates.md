# 📋 SDLC Document Header Templates
## Universal Header Standards for Active and Archived Documents

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - UNIVERSAL DOCUMENTATION STANDARD
**Scope**: All SDLC framework documents (active and archived)
**Authority**: CEO + CPO + CTO Documentation Standards

---

## 🎯 Purpose

This document provides **standardized header templates** for both **active documents** and **archived documents** in the SDLC 5.0 framework, ensuring:
- Clear version identification
- Proper status indication
- Authority and approval tracking
- Migration and traceability
- Consistency across all documentation

---

## 📄 Template 1: Active Document Header

### When to Use
Apply this header to **all active SDLC 5.0 documents** that are currently in use and maintained.

### Template
```markdown
# [Document Title]
## [Subtitle - Purpose]

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - [Specific Status]
**Authority**: [Who Approved]
**Foundation**: [What This Builds On]
**Enhancement**: [What's New in 5.0 - Optional]

---

[Document content starts here]
```

### Field Definitions

**Version**:
- Format: `5.0.0` (MAJOR.MINOR.PATCH)
- Always use current framework version for active docs

**Date**:
- Format: `Month DD, YYYY` (e.g., December 5, 2025)
- Last significant update date
- Update when major content changes

**Status**:
- Format: `ACTIVE - [Specific Context]`
- Examples:
  - `ACTIVE - PRODUCTION READY`
  - `ACTIVE - ENHANCED WITH CODE REVIEW`
  - `ACTIVE - ESSENTIAL FOR 10x PRODUCTIVITY`
  - `ACTIVE - BATTLE-TESTED PATTERNS`

**Authority**:
- Who approved or owns this document
- Examples:
  - `CEO + CPO + CTO Leadership`
  - `Chairman + CEO + CPO Approved`
  - `CTO Technical Review`
  - `CPO Office (taidt@mtsolution.com.vn)`

**Foundation**:
- What this document builds on
- Examples:
  - `Battle-Tested from 3 Platforms (BFlow, NQH-Bot, MTEP)`
  - `Lessons from 679 mock crisis`
  - `Real crisis, Real solutions, Real results`

**Enhancement** (Optional):
- What's new in SDLC 5.0
- Examples:
  - `Governance & Compliance + 4-Tier Classification`
  - `Industry Best Practices Integration (CMMI, SAFe, DORA)`
  - `Enhanced with 4.9.1 → 5.0.0 upgrade lessons`

### Examples

**Example 1: Implementation Guide**
```markdown
# SDLC 5.0 Implementation Guide - Enhanced Deployment with Governance

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - PRODUCTION READY
**Authority**: Chairman + CPO + CTO Approved
**Timeline**: 1-2 Week Rollout
**Key Enhancement**: Governance & Compliance + 4-Tier Classification

---
```

**Example 2: AI Tool Template**
```markdown
# Claude Code Developer Template - SDLC 5.0

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - ESSENTIAL FOR 10x PRODUCTIVITY
**Foundation**: Proven with Claude Code, Cursor, GitHub Copilot
**Enhancement**: AI Governance Layer integrated

---
```

**Example 3: Case Study**
```markdown
# SDLC 5.0 Design Thinking Case Study - NQH-Bot Success

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - VALIDATED REAL-WORLD RESULTS
**Authority**: CPO Office
**Foundation**: Complete 5-phase Design Thinking methodology
**Achievement**: 96% time savings, 3x higher feature adoption

---
```

---

## 🔒 Template 2: Archived Document Header

### When to Use
Apply this header to **documents that have been superseded** by newer versions or are no longer actively maintained.

### Template
```markdown
# [Document Title]
## [Subtitle - Purpose]

**ARCHIVAL STATUS**: 🔒 ARCHIVED (READ-ONLY)
**Original Version**: [Version Tag]
**Superseded By**: [Active Version Doc Reference]
**Archival Date**: November 7, 2025
**Archive Location**: [Path to Archive]
**Reason**: [Why Archived]

---

## ⚠️ ARCHIVE NOTICE

This document has been **archived** and is **READ-ONLY**. For current active version, see:
- **Active Version**: [Link to Active Document]
- **Migration Guide**: [Link to Migration Guide if applicable]

**When to Reference This Archive**:
- Historical context and evolution understanding
- Version comparison studies
- Research on methodology origins

**Do NOT Use This Archive For**:
- New implementations (use active SDLC 5.0)
- Active projects (upgrade to current version)
- Team training (use current materials)

---

**Original Document Content Below (Preserved As-Is)**

[Original document content - UNMODIFIED]
```

### Field Definitions

**ARCHIVAL STATUS**:
- Always: `🔒 ARCHIVED (READ-ONLY)`
- Clear visual indicator with emoji

**Original Version**:
- The version when document was active
- Examples: `4.7.0`, `4.6.0`, `3.7.3`

**Superseded By**:
- What replaced this document
- Example: `SDLC-4.8-Implementation-Guide.md`

**Archival Date**:
- When moved to archive
- Format: `Month DD, YYYY`

**Archive Location**:
- Full path in archive structure
- Example: `99-Legacy/SDLC-4.9.1-Archive/03-Implementation-Guides/`

**Reason**:
- Why this was archived
- Examples:
  - `Upgraded to SDLC 5.0.0 with Governance & Compliance Integration`
  - `Replaced by enhanced version with 4-Tier Classification`
  - `Superseded by consolidated guide`

### Archive Notice Section

Must include:
- Clear warning this is archived
- Link to active version
- Migration guide (if applicable)
- When to reference archive
- When NOT to use archive

### Examples

**Example 1: Archived Implementation Guide**
```markdown
# SDLC 4.9.1 Implementation Guide

**ARCHIVAL STATUS**: 🔒 ARCHIVED (READ-ONLY)
**Original Version**: 4.9.1
**Superseded By**: SDLC-Implementation-Guide.md
**Archival Date**: December 5, 2025
**Archive Location**: 99-Legacy/SDLC-4.9.1-Archive/03-Implementation-Guides/
**Reason**: Upgraded to SDLC 5.0.0 with Governance & Compliance Integration

---

## ⚠️ ARCHIVE NOTICE

This document has been **archived** and is **READ-ONLY**. For current active version, see:
- **Active Version**: [SDLC-Implementation-Guide.md](../../03-Implementation-Guides/SDLC-Implementation-Guide.md)
- **Migration Guide**: [README-SDLC-4.9.1-ARCHIVE.md](../README-SDLC-4.9.1-ARCHIVE.md)

**Good News**: **NO breaking changes!** SDLC 5.0.0 is additive.

**Migration Steps** (2-4 hours):
1. ✅ Keep Everything - All 4.9.1 processes remain valid
2. ➕ Add Governance & Compliance Standards
3. ➕ Add 4-Tier Classification - Choose tier
4. ✅ Update Templates - Use 5.0.0 versions

---

**Original Document Content Below (Preserved As-Is)**

[Original 4.9.1 content here - UNMODIFIED]
```

**Example 2: Archived README**
```markdown
# SDLC 4.9.1 Archive - Historical Reference

**Archive Date**: December 5, 2025
**Status**: ARCHIVED - Reference Only
**Active Version**: SDLC 5.0.0
**Reason**: Upgraded to SDLC 5.0.0 with Governance & Compliance Integration

---

## 📋 Archive Purpose

This directory contains the **complete SDLC 4.9.1 documentation** (November 2025 release) for historical reference and version comparison purposes.

[Archive README content continues...]
```

---

## 🔄 Template 3: Migration Document Header

### When to Use
Apply this header to documents that guide users from one version to another.

### Template
```markdown
# Migration Guide: SDLC [Old Version] → [New Version]

**Version**: [New Version].0
**Date**: [Migration Date]
**Status**: ACTIVE - MIGRATION GUIDE
**Source**: SDLC [Old Version]
**Target**: SDLC [New Version]
**Timeline**: [Estimated Migration Time]
**Disruption**: [None|Minimal|Moderate]

---

## 🎯 Migration Summary

**Migration Type**: [Enhancement|Replacement|Consolidation]
**Breaking Changes**: [Yes|No]
**Backward Compatible**: [Yes|No]
**Estimated Time**: [Time estimate]

---

[Migration guide content]
```

### Example
```markdown
# Migration Guide: SDLC 4.9.1 → SDLC 5.0.0

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - MIGRATION GUIDE
**Source**: SDLC 4.9.1 (6-pillar framework)
**Target**: SDLC 5.0.0 (enhanced with Governance & Compliance)
**Timeline**: 2-4 hours
**Disruption**: None (zero breaking changes)

---

## 🎯 Migration Summary

**Migration Type**: Enhancement (not replacement)
**Breaking Changes**: No
**Backward Compatible**: Yes (100%)
**Estimated Time**: 2-4 hours for complete migration

**What's Preserved**: All 6 pillars from 4.9.1
**What's Added**: Governance & Compliance Standards + 4-Tier Classification
**What's Enhanced**: Industry Best Practices (CMMI, SAFe, DORA) Integration

---

[Detailed migration steps...]
```

---

## 📊 Header Compliance Checklist

### For Active Documents
- [ ] Version is 5.0.0
- [ ] Date is current (December 5, 2025 or later)
- [ ] Status starts with "ACTIVE"
- [ ] Authority/ownership clear
- [ ] Foundation documented
- [ ] Enhancement noted (if applicable)

### For Archived Documents
- [ ] ARCHIVAL STATUS prominently displayed
- [ ] Original version documented
- [ ] Superseded by reference included
- [ ] Archive location specified
- [ ] Reason for archival clear
- [ ] Archive notice section complete
- [ ] Link to active version working
- [ ] Migration guide referenced
- [ ] Original content UNMODIFIED

### For Migration Documents
- [ ] Source and target versions clear
- [ ] Migration timeline specified
- [ ] Disruption level indicated
- [ ] Migration type documented
- [ ] Breaking changes noted
- [ ] Backward compatibility stated

---

## 🚨 Common Mistakes to Avoid

### Mistake 1: Inconsistent Version Numbers
```yaml
Wrong:
  Version: 5.0 (missing .0)
  Version: v5.0.0 (extra 'v')

Right:
  Version: 5.0.0
```

### Mistake 2: Missing Archive Warnings
```yaml
Wrong:
  [Just changing version in archived doc]

Right:
  [Adding complete archive header with warnings]
```

### Mistake 3: Editing Archived Content
```yaml
Wrong:
  Updating terminology in archived document

Right:
  Preserving original content EXACTLY as-is
```

### Mistake 4: Vague Status
```yaml
Wrong:
  Status: ACTIVE

Right:
  Status: ACTIVE - PRODUCTION READY
```

---

## 📈 Header Evolution History

```yaml
SDLC 4.6 (September 2025):
  - Basic version headers
  - Archival template introduced

SDLC 4.7 (September 2025):
  - Enhanced with foundation tracking
  - Battle-tested indicators

SDLC 4.9 (November 2025):
  - Complete header standardization
  - Active + Archive + Migration templates
  - Enhancement tracking added
  - Design Thinking integration noted

SDLC 5.0.0 (December 2025):
  - Governance & Compliance Integration
  - 4-Tier Classification System
  - Industry Best Practices (CMMI, SAFe, DORA)
  - Team Collaboration Framework
```

---

## ✅ Quick Reference

### Active Document Header (Minimal)
```markdown
# Document Title

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: ACTIVE - [Context]
**Authority**: [Owner]

---
```

### Archived Document Header (Minimal)
```markdown
# Document Title

**ARCHIVAL STATUS**: 🔒 ARCHIVED (READ-ONLY)
**Original Version**: [Old Version]
**Superseded By**: [New Document]
**Archival Date**: December 5, 2025

---

## ⚠️ ARCHIVE NOTICE
See: [Link to Active Version]

---

[Original content - UNMODIFIED]
```

---

**Document**: SDLC-Document-Header-Templates
**Status**: ACTIVE - UNIVERSAL DOCUMENTATION STANDARD
**Purpose**: Standardize headers across all SDLC 5.0 documentation
**Compliance**: Mandatory for all new and updated documents
**Last Updated**: December 5, 2025

***"Clear headers, clear purpose, clear value."*** 📋

***"Every document tells its story through its header."*** ✨
