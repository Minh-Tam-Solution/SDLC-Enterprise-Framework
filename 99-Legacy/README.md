# 📦 SDLC Framework Legacy Archive

**Purpose**: Historical archive for superseded SDLC framework versions and deprecated content
**Status**: READ-ONLY ARCHIVE
**Current Version**: SDLC 6.0.0 (see parent folder)
**Maintainer**: CTO Office
**Last Updated**: January 28, 2026

---

## 📁 Archive Structure

```
99-Legacy/
├── 00-Version-Evolution/         # Complete version history (1.x → 5.1.x)
│   ├── 00-Historical-Documents/
│   ├── 01-SDLC-4.0/ ... 11-SDLC-5.0/
│   └── SDLC-Version-History.md
│
├── v5.3.0-Archive/               # **NEW** SDLC 5.3.0 archive (Jan 28, 2026)
│   ├── README.md                 # Archive documentation
│   ├── VERSION-5.3.0             # Version marker file
│   └── documents/                # Archived 5.3.0 key documents
│       ├── SDLC-Stage-Dependencies.md
│       ├── SDLC-Stage-Exit-Criteria.md
│       ├── SDLC-Quality-Assurance-System.md
│       └── SDLC-Tier-Stage-Requirements.md
│
├── 5.2.0-Deprecated/             # SDLC 5.2.0 deprecated content
│
├── tool-guides-2026/             # Archived tool-specific templates (Jan 2026)
│   ├── claude-code/              # → Use 04-AI-TOOLS-LANDSCAPE/tool-profiles/
│   ├── cursor/
│   ├── copilot/
│   ├── chatgpt/
│   └── gemini/
│
├── deployment-guides-5.1.3/      # Project deployment docs (5.1.3)
│   ├── 08-Team-Management/       # Team compliance docs
│   └── AI-Platform/              # AI Platform specific deployment
│
├── SASE-Deprecated-Artifacts/    # Deprecated SASE templates
│   ├── 01-BriefingScript-Template.yaml  # → Use AGENTS.md
│   ├── 02-LoopScript-Template.yaml      # → AI generates own plans
│   └── 03-MentorScript-Template.md      # → Use AGENTS.md
│
├── 01-Implementation-Scripts/    # Legacy implementation scripts (1.x-3.x)
├── 02-Validation-Tools/          # Legacy validation tools (1.x-3.x)
├── scripts/                      # Compliance validators & scanners
└── README.md                     # This file
```

---

## 🎯 When to Use This Archive

✅ **Use for:**
- Historical learning & evolution tracing
- Understanding framework design decisions
- Compliance/audit reconstruction
- Comparative analysis with current version
- Reference for 5.1.3 deployment configurations

❌ **Do NOT use for:**
- New project baselines (use SDLC 5.2.0)
- Active development guidance
- Current best practices
- Tool-specific templates (use 04-AI-TOOLS-LANDSCAPE/ instead)

---

## 📊 Version Evolution Summary

| Version | Date | Key Feature | Status |
|---------|------|-------------|--------|
| 1.x | Jun 2025 | AI-native prototype | Archived |
| 2.x | Jul 2025 | AI agile ceremonies | Archived |
| 3.x | Aug 2025 | Scientific Org Standard | Archived |
| 4.0-4.3 | Aug-Sep 2025 | Universal roles | Archived |
| 4.4-4.6 | Sep-Oct 2025 | Adaptive Governance | Archived |
| 4.7 | Sep 2025 | 5-Pillar Excellence | Archived |
| 4.8 | Nov 2025 | Design Thinking (Pillar 0) | Archived |
| 4.9 | Nov 2025 | 10-Stage Lifecycle | Archived |
| 5.0 | Dec 2025 | 4-Tier Classification | Archived |
| 5.1.1 | Dec 2025 | SASE Integration | Archived |
| 5.1.3 | Jan 2026 | Sprint Planning Governance | Archived |
| 5.2.0 | Jan 22, 2026 | Principle-Centric + AI Governance | Archived |
| 5.3.0 | Jan 28, 2026 | Stage Dependencies + Quality Assurance | Archived |
| **6.0.0** | **Jan 28, 2026** | **MAJOR: Unified Specification Standard** | **ACTIVE** |

---

## 🆕 What's New in 6.0.0 (January 28, 2026)

SDLC 6.0.0 is a **MAJOR release** introducing the **Unified Specification Standard**:

```
┌─────────────────────────────────────────────────────────────────┐
│                   SDLC 6.0.0 MAJOR CHANGES                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✅ Section 8: Unified Specification Standard                  │
│     • YAML frontmatter REQUIRED for all specs                  │
│     • BDD requirements (GIVEN-WHEN-THEN) format                │
│     • Tier-aware specifications (LITE → ENTERPRISE)            │
│                                                                 │
│  ✅ New Templates (Framework-6.0/)                             │
│     • SDLC-Specification-Standard.md - Unified spec format     │
│     • DESIGN_DECISIONS.md - Lightweight ADRs                   │
│     • SPEC_DELTA.md - Version change tracking                  │
│     • CONTEXT_AUTHORITY_METHODOLOGY.md - Dynamic AGENTS.md     │
│                                                                 │
│  ✅ OpenSpec Alignment                                         │
│     • Industry-standard spec-driven development                │
│     • CEO APPROVED: EXTEND hybrid workflow                     │
│     • sdlcctl spec convert command planned                     │
│                                                                 │
│  ⚠️ BREAKING CHANGES                                          │
│     • New specs MUST use YAML frontmatter                      │
│     • Requirements MUST use BDD format                         │
│     • Tier declaration REQUIRED                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Changes**:
- **Section 8**: Unified Specification Standard (new pillar)
- **YAML frontmatter**: `spec_id`, `tier`, `stage`, `status` required
- **BDD format**: GIVEN-WHEN-THEN requirements syntax
- **DESIGN_DECISIONS.md**: Lightweight ADR alternative for sprint-scoped decisions
- **SPEC_DELTA.md**: Version change tracking template
- **Context Authority**: Dynamic AGENTS.md with 4 zones (Static → Ephemeral)
- **5.3.0 archived**: Stage Dependencies, Quality Assurance now in v5.3.0-Archive/

---

## 🔗 Quick Links

- **Active Framework (6.0.0)**: [../README.md](../README.md)
- **Framework 6.0 Templates**: [../05-Templates-Tools/Framework-6.0/](../05-Templates-Tools/Framework-6.0/)
- **AI Governance Principles**: [../03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/)
- **AI Tools Landscape**: [../04-AI-TOOLS-LANDSCAPE/](../04-AI-TOOLS-LANDSCAPE/)
- **Core Methodology**: [../02-Core-Methodology/](../02-Core-Methodology/)
- **CONTENT-MAP**: [../CONTENT-MAP.md](../CONTENT-MAP.md)
- **DEPRECATION-POLICY**: [../DEPRECATION-POLICY.md](../DEPRECATION-POLICY.md)
- **CHANGELOG**: [../CHANGELOG.md](../CHANGELOG.md)

---

## 📂 Archived Content Index

| Archive Folder | Content | Archived Date | Migration Path |
|----------------|---------|---------------|----------------|
| **v5.3.0-Archive/** | **5.3.0 Stage Governance docs** | **Jan 28, 2026** | **→ Still in 6.0.0 (not deprecated)** |
| 5.2.0-Deprecated/ | 5.2.0 deprecated content | Jan 2026 | Superseded by 5.3.0 |
| tool-guides-2026/ | Tool-specific templates | Jan 2026 | → 04-AI-TOOLS-LANDSCAPE/tool-profiles/ |
| deployment-guides-5.1.3/ | Project deployment configs | Jan 2026 | Copy and adapt for 6.0.0 |
| SASE-Deprecated-Artifacts/ | BRS, MTS, LPS templates | Jan 2026 | → AGENTS.md template |

---

**Archive Status**: ACTIVE (Read-Only)
**Total Files**: ~350 files
**Total Size**: ~6.5MB
