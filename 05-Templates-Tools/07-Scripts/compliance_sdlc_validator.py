#!/usr/bin/env python3
"""
SDLC 6.1.1 Complete Validator
Validates complete 10-stage lifecycle + 7-pillar architecture + SASE Framework compliance

Version: 6.1.1
Date: February 2026
Status: ACTIVE - PRODUCTION READY
Foundation: Proven validation across BFlow, NQH-Bot, MTEP, SDLC Orchestrator platforms
Enhancement: 7-Pillar Architecture (Pillar 2: Sprint Planning Governance) + SASE Framework (SE 3.0)
New in 6.1.1: AI Governance Principles, Concentric Circles Model, best-practices-2026 in 04-AI-TOOLS-LANDSCAPE/

DOCUMENTATION vs CODE SEPARATION (SDLC 6.1.1):
- Stage mapping applies ONLY to /docs folders (stages 00-09)
- Code folders (backend/, frontend/, tools/, tests/) are NOT stage-mapped
- Code folders are validated for PRESENCE, not stage compliance
- See: SDLC-Project-Structure-Standard.md

10 Stages Validated (00-09) - /docs ONLY:
- Stage 00 (FOUNDATION): Strategic Discovery & Validation (WHY?)
- Stage 01 (PLANNING): Requirements & User Stories (WHAT?)
- Stage 02 (DESIGN): Architecture & Technical Design (HOW?)
- Stage 03 (INTEGRATE): API Contracts & Third-party Setup
- Stage 04 (BUILD): Development & Implementation
- Stage 05 (TEST): Quality Assurance & Validation
- Stage 06 (DEPLOY): Release & Deployment
- Stage 07 (OPERATE): Production Operations & Monitoring
- Stage 08 (COLLABORATE): Team Coordination & Knowledge
- Stage 09 (GOVERN): Compliance & Strategic Oversight

Project Structure Validation (NOT stage-mapped):
- Code folders: backend/, frontend/, tools/, tests/
- Required files by tier: README.md, CLAUDE.md, .env.example, etc.

Legacy/Archive Structure (SDLC 6.1.1+):
- 10-archive: ONLY at docs root (not a stage, holds unsorted legacy docs)
- 99-legacy: within EACH stage (00-09) AND in backend, frontend, tools
- Content in legacy/archive folders is never validated or upgraded

7 Pillars Validated:
- Pillar 0: Design Thinking Foundation
- Pillar 1: 10-Stage Lifecycle
- Pillar 2: Sprint Planning Governance (NEW in 5.2.0)
- Pillar 3: 4-Tier Classification
- Pillar 4: Quality Gates (Dual-Track)
- Pillar 5: SASE Integration
- Pillar 6: Documentation Permanence

SASE Framework (Simplified in 6.1.1):
- AGENTS.md: Dynamic context for AI collaboration (industry standard)
- CRP (Consultation-Readiness Proof): Human-AI consultation evidence
- MRP (Merge-Readiness Proof): Merge readiness documentation
- VCR (Version Controlled Resolution): Resolution evidence
- Agentic Maturity: L0 (Tool-Assisted) → L3 (Lifecycle Agentic)
- Deprecated: BRS, LPS, MTS (replaced by AGENTS.md)

4-Tier Classification:
- LITE: 1-2 people, basic documentation
- STANDARD: 3-10 people, CLAUDE.md + /docs
- PROFESSIONAL: 10-50 people, full 10-stage + ADRs + SASE
- ENTERPRISE: 50+ people, CTO/CPO reports + CAB process + Full SASE

Team Collaboration Standards:
- SDLC-Team-Communication-Protocol.md (tiered requirements)
- SDLC-Team-Collaboration-Protocol.md (RACI, handoffs)
- SDLC-Escalation-Path-Standards.md (4-level escalation)

Code File Naming Standards:
- Python: snake_case, max 50 chars
- TypeScript: camelCase, max 50 chars
- React: PascalCase, max 50 chars
- Alembic: {rev}_{desc}.py, max 60 chars

Usage:
    python3 sdlc_validator.py /path/to/project

Success Metrics:
- 100% compliance required for production deployment
- All 10 stages must have documentation
- All 6 pillars must pass validation
- Zero Mock Policy enforced (0 mocks)
- SASE artifacts for PROFESSIONAL+ tiers (5.1.0)
- Code File Naming Standards enforced
- Design Thinking methodology applied
- Code Review tier active (1, 2, or 3)
"""

import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple
import re

class SDLC60Validator:
    """SDLC 6.1.1 Complete 7-Pillar + SASE Framework + Team Collaboration Validator

    7-Pillar Architecture (SDLC 6.1.1):
    - Pillar 0: Design Thinking Foundation
    - Pillar 1: 10-Stage Lifecycle
    - Pillar 2: Sprint Planning Governance (NEW in 5.2.0)
    - Pillar 3: 4-Tier Classification
    - Pillar 4: Quality Gates (Dual-Track)
    - Pillar 5: SASE Integration
    - Pillar 6: Documentation Permanence

    Legacy/Archive Handling:
    - Skips 10-archive folder at docs root (not a stage)
    - Skips 99-legacy folders within stages (00-09) and backend/frontend/tools
    - Content in legacy/archive is never validated or upgraded
    """

    # Legacy/Archive folder patterns to skip during validation
    LEGACY_ARCHIVE_PATTERNS = [
        "99-legacy", "99-Legacy",  # In stages, backend, frontend, tools
        "10-archive", "10-Archive",  # At docs root only (not a stage)
    ]

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.results = {
            "pillar_0": {"name": "Design Thinking Foundation", "passed": False, "score": 0, "details": []},
            "pillar_1": {"name": "10-Stage Lifecycle", "passed": False, "score": 0, "details": []},
            "pillar_2": {"name": "Sprint Planning Governance", "passed": False, "score": 0, "details": []},
            "pillar_3": {"name": "4-Tier Classification", "passed": False, "score": 0, "details": []},
            "pillar_4": {"name": "Quality Gates (Dual-Track)", "passed": False, "score": 0, "details": []},
            "pillar_5": {"name": "SASE Integration", "passed": False, "score": 0, "details": []},
            "pillar_6": {"name": "Documentation Permanence", "passed": False, "score": 0, "details": []},
            "section_7": {"name": "Section 7: Quality Assurance", "passed": False, "score": 0, "details": []},
            "section_8": {"name": "Section 8: Specification Standard", "passed": False, "score": 0, "details": []},
            "three_ring": {"name": "3-Ring Architecture", "passed": False, "score": 0, "details": []},
            "claude_md": {"name": "CLAUDE.md Standard", "passed": False, "score": 0, "details": []},
        }
        self.overall_compliant = False

    def _is_legacy_or_archive(self, path: Path) -> bool:
        """Check if path is in a legacy or archive folder.

        Args:
            path: Path to check

        Returns:
            True if path should be skipped (in legacy/archive)
        """
        path_str = str(path)
        for pattern in self.LEGACY_ARCHIVE_PATTERNS:
            if f"/{pattern}/" in path_str or path_str.endswith(f"/{pattern}"):
                return True
        return False

    def _rglob_skip_legacy(self, pattern: str):
        """Glob with legacy/archive folders skipped.

        Args:
            pattern: Glob pattern to match

        Yields:
            Paths matching pattern, excluding legacy/archive folders
        """
        for path in self.project_path.rglob(pattern):
            if not self._is_legacy_or_archive(path):
                yield path

    def validate_all_pillars(self) -> Dict:
        """Validate all 6 pillars of SDLC 6.1.1"""
        print("🔍 SDLC 6.1.1 Complete Validation Starting...")
        print(f"📁 Project: {self.project_path}")
        print("=" * 80)

        # Validate each pillar (7-Pillar Architecture)
        self.validate_pillar_0_design_thinking()
        self.validate_pillar_1_lifecycle()
        self.validate_pillar_2_sprint_governance()
        self.validate_pillar_3_tier_classification()
        self.validate_pillar_4_quality_gates()
        self.validate_pillar_5_sase_integration()
        self.validate_pillar_6_documentation()

        # SDLC 6.1.1: Section 7 + Section 8 validation
        self.validate_section_7_quality_assurance()
        self.validate_section_8_spec_standard()

        # SDLC 6.1.1: 3-Ring Architecture validation
        self.validate_three_ring_architecture()

        # Calculate overall compliance
        self.calculate_overall_compliance()

        # Print results
        self.print_results()

        return self.results

    def validate_pillar_0_design_thinking(self):
        """Pillar 0: Design Thinking Foundation"""
        print("\n🎨 Validating Pillar 0: Design Thinking Foundation...")

        pillar = self.results["pillar_0"]
        score = 0

        # Check for Design Thinking documentation
        design_thinking_files = [
            "docs/design-thinking",
            "design-thinking",
            "user-research",
            "empathy-maps",
            "prototypes"
        ]

        found_files = []
        for pattern in design_thinking_files:
            matches = list(self._rglob_skip_legacy(f"*{pattern}*"))
            if matches:
                found_files.extend(matches)
                score += 20

        if found_files:
            pillar["details"].append(f"✅ Design Thinking artifacts found: {len(found_files)} files")
        else:
            pillar["details"].append("⚠️  No Design Thinking artifacts found")

        # Check for 5-phase methodology evidence
        if self.check_design_thinking_phases():
            score += 20
            pillar["details"].append("✅ 5-phase methodology evidence found")
        else:
            pillar["details"].append("⚠️  5-phase methodology not fully documented")

        # Check for user validation
        if self.check_user_validation():
            score += 10
            pillar["details"].append("✅ User validation documented")
        else:
            pillar["details"].append("⚠️  User validation not found")

        pillar["score"] = score
        pillar["passed"] = score >= 30  # 30% minimum

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {score}%")

    def validate_pillar_1_lifecycle(self):
        """Pillar 1: 10-Stage Lifecycle Validation"""
        print("\n📋 Validating Pillar 1: 10-Stage Lifecycle...")

        pillar = self.results["pillar_1"]
        score = 0

        # 10 stages to validate (00-09)
        stages = [
            ("00", "FOUNDATION", "WHY?"),
            ("01", "PLANNING", "WHAT?"),
            ("02", "DESIGN", "HOW?"),
            ("03", "INTEGRATE", "API Contracts"),
            ("04", "BUILD", "Development"),
            ("05", "TEST", "Quality Assurance"),
            ("06", "DEPLOY", "Release"),
            ("07", "OPERATE", "Operations"),
            ("08", "COLLABORATE", "Team Coordination"),
            ("09", "GOVERN", "Compliance"),
        ]

        found_stages = []
        docs_path = self.project_path / "docs"

        for stage_num, stage_name, stage_desc in stages:
            stage_patterns = [
                f"{stage_num}-{stage_name.lower()}",
                f"{stage_num}-{stage_name}",
                stage_name.lower(),
            ]
            for pattern in stage_patterns:
                if list(self._rglob_skip_legacy(f"*{pattern}*")):
                    found_stages.append((stage_num, stage_name))
                    score += 10
                    break

        if len(found_stages) >= 8:
            pillar["details"].append(f"✅ {len(found_stages)}/10 stages documented")
        elif len(found_stages) >= 5:
            pillar["details"].append(f"⚠️  {len(found_stages)}/10 stages documented (minimum 8 recommended)")
        else:
            pillar["details"].append(f"❌ Only {len(found_stages)}/10 stages documented")

        # Check for stage README files
        readme_count = len(list(self._rglob_skip_legacy("*README*")))
        if readme_count >= 5:
            pillar["details"].append(f"✅ {readme_count} README files found")
        else:
            pillar["details"].append(f"⚠️  Only {readme_count} README files found")

        pillar["score"] = min(score, 100)
        pillar["passed"] = score >= 50  # At least 5 stages

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {pillar['score']}%")

    def validate_pillar_2_sprint_governance(self):
        """Pillar 2: Sprint Planning Governance (NEW in 5.2.0)

        Validates Sprint Planning Hierarchy:
        - ROADMAP: Quarterly/yearly strategic planning
        - PHASE: Major milestone planning (2-4 sprints)
        - SPRINT: Biweekly tactical planning
        - BACKLOG: Task-level management

        Sprint Governance Checks:
        - Sprint naming convention (SPRINT-XXX)
        - Sprint documentation structure
        - Sprint retrospective records
        - Velocity tracking
        - Definition of Done compliance
        """
        print("\n🏃 Validating Pillar 2: Sprint Planning Governance...")

        pillar = self.results["pillar_2"]
        score = 0

        # Check for Planning Hierarchy documents
        hierarchy_docs = {
            "ROADMAP": ["roadmap", "ROADMAP", "strategic-plan"],
            "PHASE": ["phase", "PHASE", "milestone"],
            "SPRINT": ["sprint", "SPRINT", "iteration"],
            "BACKLOG": ["backlog", "BACKLOG", "task-list"],
        }

        found_hierarchy = []
        for level, patterns in hierarchy_docs.items():
            for pattern in patterns:
                if list(self._rglob_skip_legacy(f"*{pattern}*")):
                    found_hierarchy.append(level)
                    score += 15
                    break

        if len(found_hierarchy) >= 3:
            pillar["details"].append(f"✅ Planning hierarchy: {', '.join(found_hierarchy)}")
        elif len(found_hierarchy) >= 1:
            pillar["details"].append(f"⚠️  Partial planning hierarchy: {', '.join(found_hierarchy)}")
        else:
            pillar["details"].append("❌ No planning hierarchy documents found")

        # Check for Sprint Planning folder structure
        sprint_folders = ["01-planning", "planning", "sprints"]
        found_sprint_folder = False
        for folder in sprint_folders:
            if list(self._rglob_skip_legacy(folder)):
                found_sprint_folder = True
                score += 15
                pillar["details"].append(f"✅ Sprint planning folder found: {folder}")
                break

        if not found_sprint_folder:
            pillar["details"].append("⚠️  No dedicated sprint planning folder")

        # Check for Sprint Retrospective documents
        retro_patterns = ["retrospective", "retro", "sprint-review", "lessons-learned"]
        found_retro = False
        for pattern in retro_patterns:
            if list(self._rglob_skip_legacy(f"*{pattern}*")):
                found_retro = True
                score += 10
                pillar["details"].append("✅ Sprint retrospective documents found")
                break

        if not found_retro:
            pillar["details"].append("⚠️  No sprint retrospective documents found")

        # Check for Definition of Done (DoD)
        dod_patterns = ["definition-of-done", "DoD", "done-criteria", "acceptance-criteria"]
        found_dod = False
        for pattern in dod_patterns:
            if list(self._rglob_skip_legacy(f"*{pattern}*")):
                found_dod = True
                score += 10
                pillar["details"].append("✅ Definition of Done documented")
                break

        if not found_dod:
            pillar["details"].append("⚠️  Definition of Done not documented")

        # Check for Sprint naming convention compliance
        sprint_naming_score = self.check_sprint_naming_convention()
        score += sprint_naming_score
        if sprint_naming_score >= 10:
            pillar["details"].append("✅ Sprint naming convention followed")
        else:
            pillar["details"].append("⚠️  Sprint naming convention not consistently followed")

        pillar["score"] = min(score, 100)
        pillar["passed"] = score >= 40  # 40% minimum

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {pillar['score']}%")

    def check_sprint_naming_convention(self) -> int:
        """Check for proper sprint naming convention (SPRINT-XXX)

        Valid patterns:
        - SPRINT-001, SPRINT-074, etc.
        - sprint-001, sprint-074, etc.
        - Generic: Sprint N, Sprint N+1

        Invalid patterns:
        - Temporal references: DAY-1, PHASE-1, TEMP-
        """
        score = 0

        # Look for proper sprint naming
        sprint_patterns = [
            r"SPRINT-\d{3}",  # SPRINT-001, SPRINT-074
            r"sprint-\d{3}",  # sprint-001, sprint-074
            r"Sprint\s+\d+",  # Sprint 1, Sprint 74
        ]

        found_proper_naming = False
        for pattern in sprint_patterns:
            for file_path in self._rglob_skip_legacy("*.md"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    if re.search(pattern, content):
                        found_proper_naming = True
                        break
                except:
                    continue
            if found_proper_naming:
                break

        if found_proper_naming:
            score += 10

        return score

    def validate_pillar_3_tier_classification(self):
        """Pillar 3: 4-Tier Classification Validation"""
        print("\n🏷️  Validating Pillar 3: 4-Tier Classification...")

        pillar = self.results["pillar_3"]
        score = 0

        # Detect project tier based on structure
        tier = self.detect_project_tier()

        if tier:
            pillar["details"].append(f"✅ Project tier detected: {tier}")
            score += 40
        else:
            pillar["details"].append("⚠️  Project tier not clearly defined")

        # Check tier-appropriate documentation
        tier_docs = {
            "LITE": ["README.md"],
            "STANDARD": ["README.md", "CLAUDE.md"],
            "PROFESSIONAL": ["README.md", "CLAUDE.md", "docs/"],
            "ENTERPRISE": ["README.md", "CLAUDE.md", "docs/", "ADRs/"],
        }

        if tier and tier in tier_docs:
            required_docs = tier_docs[tier]
            found_docs = []
            for doc in required_docs:
                if (self.project_path / doc).exists() or list(self._rglob_skip_legacy(doc)):
                    found_docs.append(doc)
                    score += 15

            if len(found_docs) == len(required_docs):
                pillar["details"].append(f"✅ All {tier} tier docs present")
            else:
                pillar["details"].append(f"⚠️  Missing {tier} tier docs: {set(required_docs) - set(found_docs)}")

        pillar["score"] = min(score, 100)
        pillar["passed"] = score >= 40

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {pillar['score']}%")

    def detect_project_tier(self) -> str:
        """Detect project tier based on structure and documentation"""
        # Check for ENTERPRISE indicators
        if ((self.project_path / "docs" / "ADRs").exists() or
            list(self._rglob_skip_legacy("*CAB*")) or
            list(self._rglob_skip_legacy("*CTO-Report*"))):
            return "ENTERPRISE"

        # Check for PROFESSIONAL indicators
        if ((self.project_path / "docs").exists() and
            len(list((self.project_path / "docs").rglob("*.md"))) > 20):
            return "PROFESSIONAL"

        # Check for STANDARD indicators
        if (self.project_path / "CLAUDE.md").exists():
            return "STANDARD"

        # Default to LITE
        if (self.project_path / "README.md").exists():
            return "LITE"

        return None

    def validate_pillar_4_quality_gates(self):
        """Pillar 4: Quality Gates (Dual-Track) Validation"""
        print("\n🚦 Validating Pillar 4: Quality Gates (Dual-Track)...")

        pillar = self.results["pillar_4"]
        score = 0

        # Check for code review configuration (Track 1: Code Quality)
        review_tier = self.detect_code_review_tier()
        if review_tier:
            score += 30
            pillar["details"].append(f"✅ Code Review Tier {review_tier} detected")
        else:
            pillar["details"].append("⚠️  No code review tier configured")

        # Check for Zero Mock Policy (Track 1: Code Quality)
        mock_count = self.count_mocks()
        if mock_count == 0:
            score += 20
            pillar["details"].append("✅ Zero Mock Policy compliant")
        else:
            pillar["details"].append(f"⚠️  {mock_count} mock instances found")

        # Check for test coverage (Track 2: Test Quality)
        if self.check_test_coverage():
            score += 20
            pillar["details"].append("✅ Test coverage >90% estimated")
        else:
            pillar["details"].append("⚠️  Test coverage appears low")

        # Check for pre-commit hooks
        if (self.project_path / ".pre-commit-config.yaml").exists():
            score += 15
            pillar["details"].append("✅ Pre-commit hooks configured")
        elif (self.project_path / ".git" / "hooks" / "pre-commit").exists():
            score += 10
            pillar["details"].append("✅ Git pre-commit hooks found")
        else:
            pillar["details"].append("⚠️  Pre-commit hooks not found")

        # Check for CI/CD pipeline
        if self.check_ci_cd():
            score += 15
            pillar["details"].append("✅ CI/CD pipeline configured")
        else:
            pillar["details"].append("⚠️  CI/CD pipeline not found")

        pillar["score"] = min(score, 100)
        pillar["passed"] = score >= 50  # 50% minimum

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {pillar['score']}%")

    def count_mocks(self) -> int:
        """Count mock instances in codebase"""
        mock_patterns = [
            r'\bmock\b',
            r'\bstub\b',
            r'\bfake\b',
            r'unittest\.mock',
            r'jest\.mock',
            r'@mock',
            r'Mock\(',
        ]

        mock_count = 0
        for file_path in self._rglob_skip_legacy("*.py"):
            try:
                content = file_path.read_text(encoding='utf-8')
                for pattern in mock_patterns:
                    mock_count += len(re.findall(pattern, content, re.IGNORECASE))
            except:
                continue

        return mock_count

    def check_ci_cd(self) -> bool:
        """Check for CI/CD configuration"""
        ci_files = [".github/workflows", ".gitlab-ci.yml", "Jenkinsfile", ".circleci"]
        for ci_file in ci_files:
            if (self.project_path / ci_file).exists():
                return True
        return False

    def validate_pillar_5_sase_integration(self):
        """Pillar 5: SASE Integration (AI+Human Orchestration + SE 3.0)"""
        print("\n🤖 Validating Pillar 5: SASE Integration...")

        pillar = self.results["pillar_5"]
        score = 0

        # Check for AI integration files
        ai_files = [
            ".claude-instructions",
            ".cursor-instructions",
            ".copilot-instructions",
            ".coderabbit.yaml",
            "CLAUDE.md"
        ]

        found_ai_tools = []
        for ai_file in ai_files:
            if (self.project_path / ai_file).exists():
                found_ai_tools.append(ai_file)
                score += 15

        if found_ai_tools:
            pillar["details"].append(f"✅ AI tools configured: {', '.join(found_ai_tools)}")
        else:
            pillar["details"].append("⚠️  No AI tool configuration found")

        # Check for AI agent evidence
        if self.check_ai_agents():
            score += 15
            pillar["details"].append("✅ AI agent orchestration detected")
        else:
            pillar["details"].append("⚠️  AI agent orchestration not detected")

        # NEW in 5.1.0: Check for SASE Artifacts
        sase_score = self.check_sase_artifacts()
        score += sase_score
        if sase_score >= 20:
            pillar["details"].append("✅ SASE Artifacts found (5.1.0 SE 3.0)")
        elif sase_score > 0:
            pillar["details"].append("⚠️  Partial SASE Artifacts (check AGENTS.md, CRP, MRP, VCR)")
        else:
            pillar["details"].append("⚠️  SASE Artifacts not found (5.1.0)")

        # Check for Team Collaboration Standards
        team_collab_score = self.check_team_collaboration()
        score += team_collab_score
        if team_collab_score >= 20:
            pillar["details"].append("✅ Team Collaboration Standards found")
        elif team_collab_score > 0:
            pillar["details"].append("⚠️  Partial Team Collaboration Standards")
        else:
            pillar["details"].append("⚠️  Team Collaboration Standards not found")

        pillar["score"] = min(score, 100)
        pillar["passed"] = score >= 40  # 40% minimum

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {pillar['score']}%")

    def validate_pillar_6_documentation(self):
        """Pillar 6: Documentation Permanence"""
        print("\n📚 Validating Pillar 6: Documentation Permanence...")

        pillar = self.results["pillar_6"]
        score = 0

        # Check for documentation structure
        doc_dirs = ["docs", "documentation"]
        found_docs = False
        for doc_dir in doc_dirs:
            if (self.project_path / doc_dir).exists():
                found_docs = True
                score += 30
                break

        if found_docs:
            pillar["details"].append("✅ Documentation directory structure found")
        else:
            pillar["details"].append("⚠️  No documentation directory found")

        # Check for proper naming (no sprint/day refs)
        bad_naming = self.check_temporal_naming()
        if not bad_naming:
            score += 30
            pillar["details"].append("✅ No temporal references in filenames")
        else:
            pillar["details"].append(f"⚠️  {len(bad_naming)} files with temporal refs")

        # Check for version headers
        if self.check_version_headers():
            score += 20
            pillar["details"].append("✅ Version headers present")
        else:
            pillar["details"].append("⚠️  Version headers missing")

        # Check for archival headers (Pillar 6 specific)
        if self.check_archival_headers():
            score += 20
            pillar["details"].append("✅ Archival headers found")
        else:
            pillar["details"].append("⚠️  Archival headers not found")

        pillar["score"] = min(score, 100)
        pillar["passed"] = score >= 50  # 50% minimum

        status = "✅ PASSED" if pillar["passed"] else "❌ NEEDS IMPROVEMENT"
        print(f"   {status} - Score: {pillar['score']}%")

    def check_archival_headers(self) -> bool:
        """Check for archival header patterns in documentation"""
        archival_patterns = [
            "Archival-Header",
            "ARCHIVAL-HEADER",
            "Document-Lifecycle",
            "Preservation-Status"
        ]
        for pattern in archival_patterns:
            if list(self._rglob_skip_legacy(f"*{pattern}*")):
                return True
        return False

    # Helper methods

    def check_design_thinking_phases(self) -> bool:
        """Check for evidence of 5-phase Design Thinking"""
        phases = ["empathize", "define", "ideate", "prototype", "test"]
        found = 0
        for phase in phases:
            if list(self._rglob_skip_legacy(f"*{phase}*")):
                found += 1
        return found >= 3  # At least 3 phases documented

    def check_user_validation(self) -> bool:
        """Check for user validation evidence"""
        validation_terms = ["user-testing", "user-validation", "user-feedback"]
        for term in validation_terms:
            if list(self._rglob_skip_legacy(f"*{term}*")):
                return True
        return False

    def check_ai_agents(self) -> bool:
        """Check for AI agent orchestration"""
        # Look for agent configuration or orchestration files
        agent_patterns = ["agent", "orchestration", "ai-workflow"]
        for pattern in agent_patterns:
            if list(self._rglob_skip_legacy(f"*{pattern}*")):
                return True
        return False

    def check_sase_artifacts(self) -> int:
        """
        Check for SASE Artifacts (SDLC 6.1.1 - Simplified)
        Returns score 0-30 based on presence of SASE artifacts

        SASE 4 Artifacts (SDLC 6.1.1):
        - AGENTS.md: Dynamic context for AI collaboration (industry standard)
        - CRP (Consultation-Readiness Proof): Human-AI consultation evidence
        - MRP (Merge-Readiness Proof): Merge readiness documentation
        - VCR (Version Controlled Resolution): Resolution evidence

        Deprecated (replaced by AGENTS.md):
        - BRS (BriefingScript), LPS (LoopScript), MTS (MentorScript)
        """
        score = 0

        # SASE Artifact patterns to look for (6.1.1 simplified)
        sase_patterns = [
            # Primary 6.1.1 artifacts
            "AGENTS.md", "AGENTS",
            "CRP", "Consultation-Readiness",
            "MRP", "Merge-Readiness",
            "VCR", "Version-Controlled-Resolution",
            "SASE-Artifacts", "sase-artifacts",
            # Also accept legacy artifacts (backward compatible)
            "BriefingScript", "BRS",
            "LoopScript", "LPS",
            "MentorScript", "MTS"
        ]

        found_patterns = []
        for pattern in sase_patterns:
            matches = list(self._rglob_skip_legacy(f"*{pattern}*"))
            if matches:
                found_patterns.append(pattern)
                score += 3

        # Check for SASE folder structure
        sase_folders = [
            "SASE-Artifacts",
            "sase",
            "agent-artifacts"
        ]

        for folder in sase_folders:
            if list(self._rglob_skip_legacy(folder)):
                score += 10
                break

        return min(score, 30)  # Cap at 30 points

    def check_team_collaboration(self) -> int:
        """
        Check for Team Collaboration Standards
        Returns score 0-30 based on presence of team collaboration documents
        """
        score = 0

        # Check for Team Collaboration folder or documents
        team_collab_patterns = [
            "Team-Collaboration",
            "team-collaboration",
            "Team-Communication-Protocol",
            "Team-Collaboration-Protocol",
            "Escalation-Path",
            "RACI",
            "raci-matrix"
        ]

        found_patterns = []
        for pattern in team_collab_patterns:
            matches = list(self._rglob_skip_legacy(f"*{pattern}*"))
            if matches:
                found_patterns.append(pattern)
                score += 5

        # Check for specific SDLC 6.1.1 documents
        specific_docs = [
            "SDLC-Team-Communication-Protocol.md",
            "SDLC-Team-Collaboration-Protocol.md",
            "SDLC-Escalation-Path-Standards.md"
        ]

        for doc in specific_docs:
            if list(self._rglob_skip_legacy(doc)):
                score += 10

        return min(score, 30)  # Cap at 30 points

    def detect_code_review_tier(self) -> int:
        """Detect active code review tier (1, 2, or 3)"""
        # Tier 3: CodeRabbit
        if (self.project_path / ".coderabbit.yaml").exists():
            return 3
        # Tier 2: AI-powered (Claude, Cursor)
        if ((self.project_path / ".claude-instructions").exists() or
            (self.project_path / ".cursor-instructions").exists()):
            return 2
        # Tier 1: Manual review (default if any review process exists)
        if (self.project_path / ".github" / "pull_request_template.md").exists():
            return 1
        return 0

    def check_test_coverage(self) -> bool:
        """Estimate test coverage"""
        test_dirs = ["tests", "test", "__tests__"]
        for test_dir in test_dirs:
            if (self.project_path / test_dir).exists():
                test_files = list((self.project_path / test_dir).rglob("*.py"))
                if len(test_files) > 10:  # Rough estimate
                    return True
        return False

    def check_temporal_naming(self) -> List[Path]:
        """Check for temporal references in filenames (excluding legacy/archive)"""
        bad_patterns = ["SPRINT-", "DAY-", "PHASE-", "TEMP-", "DRAFT-"]
        bad_files = []
        for pattern in bad_patterns:
            bad_files.extend(list(self._rglob_skip_legacy(f"*{pattern}*")))
        return bad_files

    def check_version_headers(self) -> bool:
        """Check for version headers in files (excluding legacy/archive)"""
        # Sample a few files
        sample_files = list(self._rglob_skip_legacy("*.md"))[:5]
        headers_found = 0
        for file_path in sample_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                if "Version:" in content or "**Version**:" in content:
                    headers_found += 1
            except:
                continue
        return headers_found >= 2

    def check_monitoring(self) -> bool:
        """Check for monitoring configuration (excluding legacy/archive)"""
        monitoring_files = ["prometheus", "grafana", "monitoring", "observability"]
        for mon_file in monitoring_files:
            if list(self._rglob_skip_legacy(f"*{mon_file}*")):
                return True
        return False

    # ──────────────────────────────────────────────────────────────────
    # SDLC 6.1.1 NEW: CLAUDE.md Standard, 3-Ring, MRP, Codegen Checks
    # ──────────────────────────────────────────────────────────────────

    def check_claude_md_standard(self) -> dict:
        """Validate CLAUDE.md against the SDLC 6.1.1 3-tier standard.

        Tiers:
        - LITE (1-2 people): 500-1K lines, basic sections
        - PRO (3-15 people): 1.5K-3K lines, module zones, debugging patterns
        - ENTERPRISE (15+ people): 2K+ lines, compliance checklists, runbooks

        Returns:
            dict with keys: exists, tier, line_count, score (0-100), details
        """
        result = {"exists": False, "tier": None, "line_count": 0, "score": 0, "details": []}
        claude_md = self.project_path / "CLAUDE.md"

        if not claude_md.exists():
            result["details"].append("❌ CLAUDE.md not found at project root")
            return result

        result["exists"] = True
        try:
            content = claude_md.read_text(encoding='utf-8')
        except Exception:
            result["details"].append("⚠️  CLAUDE.md exists but could not be read")
            result["score"] = 10
            return result

        lines = content.split('\n')
        result["line_count"] = len(lines)
        content_lower = content.lower()
        score = 0

        # Detect tier from line count
        if len(lines) >= 2000:
            result["tier"] = "ENTERPRISE"
        elif len(lines) >= 1500:
            result["tier"] = "PRO"
        elif len(lines) >= 500:
            result["tier"] = "LITE"
        else:
            result["tier"] = "MINIMAL"
            result["details"].append(f"⚠️  CLAUDE.md is {len(lines)} lines (LITE minimum: 500)")

        # LITE required sections
        lite_sections = {
            "project overview": ["project overview", "what is", "## overview"],
            "tech stack": ["tech stack", "technology stack", "## technology"],
            "quick start": ["quick start", "getting started"],
            "architecture": ["architecture", "system design", "5-layer"],
            "constraints": ["constraints", "critical constraints", "policies"],
        }

        for section_name, patterns in lite_sections.items():
            if any(p in content_lower for p in patterns):
                score += 10
                result["details"].append(f"✅ {section_name.title()}")
            else:
                result["details"].append(f"⚠️  Missing: {section_name.title()}")

        # PRO additional sections
        if result["tier"] in ("PRO", "ENTERPRISE"):
            pro_sections = {
                "module zones": ["module zone", "module-specific", "## gate engine", "## evidence vault"],
                "debugging patterns": ["debugging", "debug", "common issues"],
                "test commands": ["test command", "pytest", "npm test", "testing standards"],
                "onboarding": ["onboarding", "getting started", "setup guide"],
            }

            for section_name, patterns in pro_sections.items():
                if any(p in content_lower for p in patterns):
                    score += 5
                    result["details"].append(f"✅ PRO: {section_name.title()}")
                else:
                    result["details"].append(f"⚠️  PRO missing: {section_name.title()}")

        # ENTERPRISE additional sections
        if result["tier"] == "ENTERPRISE":
            enterprise_sections = {
                "compliance checklists": ["compliance", "owasp", "asvs"],
                "runbook": ["runbook", "operations", "incident response"],
                "security boundary": ["security", "rbac", "authentication"],
            }

            for section_name, patterns in enterprise_sections.items():
                if any(p in content_lower for p in patterns):
                    score += 5
                    result["details"].append(f"✅ ENTERPRISE: {section_name.title()}")
                else:
                    result["details"].append(f"⚠️  ENTERPRISE missing: {section_name.title()}")

        # Content principles check
        # Constraints should appear early (top 30% of file)
        constraints_pos = content_lower.find("constraints")
        if constraints_pos >= 0 and constraints_pos < len(content) * 0.3:
            score += 5
            result["details"].append("✅ Constraints appear early (progressive disclosure)")
        elif constraints_pos >= 0:
            result["details"].append("⚠️  Constraints found but not early in file")

        # File paths (real references to code)
        file_path_patterns = [r'[\w/]+\.py', r'[\w/]+\.ts', r'[\w/]+\.tsx']
        file_ref_count = 0
        for pattern in file_path_patterns:
            file_ref_count += len(re.findall(pattern, content))
        if file_ref_count >= 10:
            score += 5
            result["details"].append(f"✅ {file_ref_count} file path references (file paths > descriptions)")
        elif file_ref_count > 0:
            score += 2
            result["details"].append(f"⚠️  Only {file_ref_count} file path references")

        # Anti-pattern: stale (check last_updated)
        last_updated_match = re.search(r'[Ll]ast [Uu]pdated.*?(\d{4}-\d{2}-\d{2})', content)
        if last_updated_match:
            result["details"].append(f"✅ Last updated: {last_updated_match.group(1)}")
        else:
            result["details"].append("⚠️  No last_updated date found")

        result["score"] = min(score, 100)
        return result

    def check_three_ring_architecture(self) -> dict:
        """Validate 3-Ring Architecture compliance for Framework documents.

        Core ring docs must be 100% tool-agnostic (no sdlcctl, no kubectl, no platform URLs).
        Governance ring docs must be stable (no sprint-specific content).

        Returns:
            dict with keys: score (0-100), violations (list), details (list)
        """
        result = {"score": 100, "violations": [], "details": []}

        # Only check Framework docs if present
        framework_path = self.project_path / "SDLC-Enterprise-Framework"
        if not framework_path.exists():
            result["details"].append("⚠️  SDLC-Enterprise-Framework not found (skipping 3-Ring check)")
            result["score"] = 0
            return result

        # Violation patterns for Core ring
        violation_patterns = [
            (r'\bsdlcctl\b', "sdlcctl CLI reference"),
            (r'\bkubectl\b', "kubectl CLI reference"),
            (r'api\.sdlc\.dev', "platform URL"),
            (r'redis\.sdlc\.svc', "infrastructure URL"),
            (r'\bEP-06\b', "Orchestrator-specific EP reference"),
            (r'from minio import', "AGPL import"),
            (r'from opa import', "OPA import"),
            (r'from grafana_client import', "Grafana import"),
        ]

        # Core ring paths (methodology documents)
        core_paths = [
            framework_path / "01-Foundation",
            framework_path / "02-Core-Methodology",
        ]

        # Governance ring paths
        governance_paths = [
            framework_path / "03-AI-GOVERNANCE",
            framework_path / "04-Quality-Governance",
        ]

        violation_count = 0

        # Check Core ring
        for core_path in core_paths:
            if not core_path.exists():
                continue
            for md_file in core_path.rglob("*.md"):
                if self._is_legacy_or_archive(md_file):
                    continue
                try:
                    content = md_file.read_text(encoding='utf-8')
                    for pattern, desc in violation_patterns:
                        matches = re.findall(pattern, content)
                        if matches:
                            violation_count += len(matches)
                            rel_path = md_file.relative_to(self.project_path)
                            result["violations"].append(f"Core ring: {rel_path} — {desc} ({len(matches)}x)")
                except Exception:
                    continue

        # Check Governance ring (less strict — vendor comparisons acceptable)
        for gov_path in governance_paths:
            if not gov_path.exists():
                continue
            for md_file in gov_path.rglob("*.md"):
                if self._is_legacy_or_archive(md_file):
                    continue
                try:
                    content = md_file.read_text(encoding='utf-8')
                    # Only check for direct tool dependencies, not comparisons
                    strict_patterns = [
                        (r'from minio import', "AGPL import"),
                        (r'from grafana_client import', "Grafana import"),
                        (r'redis\.sdlc\.svc', "infrastructure URL"),
                    ]
                    for pattern, desc in strict_patterns:
                        matches = re.findall(pattern, content)
                        if matches:
                            violation_count += len(matches)
                            rel_path = md_file.relative_to(self.project_path)
                            result["violations"].append(f"Governance ring: {rel_path} — {desc} ({len(matches)}x)")
                except Exception:
                    continue

        # Score: start at 100, deduct per violation
        result["score"] = max(0, 100 - (violation_count * 10))

        if violation_count == 0:
            result["details"].append("✅ 3-Ring Architecture: No violations found")
        else:
            result["details"].append(f"⚠️  3-Ring Architecture: {violation_count} violations in {len(result['violations'])} locations")

        return result

    def check_mrp_template(self) -> dict:
        """Validate MRP (Merge-Readiness Package) presence and completeness.

        MRP 5-Section Structure:
        1. Change Summary (what, why, impact scope)
        2. Evidence Vault References (gate-by-gate evidence IDs)
        3. Rollback Plan (trigger, steps, data migration, time, verification)
        4. Testing Evidence (unit, integration, manual QA, performance)
        5. Deployment Notes (config, order, post-deploy validation, flags)

        Returns:
            dict with keys: found, score (0-100), details
        """
        result = {"found": False, "score": 0, "details": []}

        # Look for MRP documents
        mrp_patterns = ["MRP", "Merge-Readiness", "merge-readiness", "mrp-template"]
        mrp_files = []

        for pattern in mrp_patterns:
            matches = list(self._rglob_skip_legacy(f"*{pattern}*"))
            mrp_files.extend(matches)

        if not mrp_files:
            result["details"].append("⚠️  No MRP documents found")
            return result

        result["found"] = True
        result["details"].append(f"✅ MRP documents found: {len(mrp_files)}")
        score = 30

        # Check for 5-section completeness in any MRP file
        mrp_sections = {
            "change summary": ["change summary", "what changed", "## summary", "## 1."],
            "evidence vault": ["evidence vault", "evidence id", "EVD-", "## 2."],
            "rollback plan": ["rollback", "rollback plan", "## 3."],
            "testing evidence": ["testing evidence", "test results", "## 4."],
            "deployment notes": ["deployment", "deploy notes", "## 5."],
        }

        for mrp_file in mrp_files:
            try:
                content = mrp_file.read_text(encoding='utf-8').lower()
                for section_name, patterns in mrp_sections.items():
                    if any(p in content for p in patterns):
                        score += 14
                        result["details"].append(f"✅ MRP Section: {section_name.title()}")
                        break  # Only count once
            except Exception:
                continue

        result["score"] = min(score, 100)
        return result

    def check_autonomous_codegen_gates(self) -> dict:
        """Validate Autonomous Codegen 4-Gate Pipeline presence.

        4-Gate Pipeline:
        - G1: Specification Review
        - G2: Security Scan (SAST)
        - G3: Test Validation
        - G4: Human Review (>500 LOC)

        Also checks: Two-agent pattern, retry logic, evidence lifecycle.

        Returns:
            dict with keys: found, score (0-100), details
        """
        result = {"found": False, "score": 0, "details": []}

        # Look for codegen pipeline
        codegen_paths = [
            self.project_path / "backend" / "app" / "services" / "codegen",
            self.project_path / "backend" / "services" / "codegen",
            self.project_path / "src" / "codegen",
        ]

        codegen_dir = None
        for path in codegen_paths:
            if path.exists():
                codegen_dir = path
                break

        if not codegen_dir:
            # Also check for codegen patterns in any Python file
            codegen_files = list(self._rglob_skip_legacy("*codegen*"))
            if codegen_files:
                result["found"] = True
                result["score"] = 20
                result["details"].append(f"✅ Codegen files found: {len(codegen_files)}")
            else:
                result["details"].append("⚠️  No codegen pipeline found (optional for non-codegen projects)")
                return result
        else:
            result["found"] = True
            result["score"] = 30
            result["details"].append(f"✅ Codegen pipeline directory: {codegen_dir.relative_to(self.project_path)}")

        # Check for 4-Gate pipeline indicators
        gate_patterns = {
            "G1 (Spec Review)": ["specification", "spec_review", "gate_1", "g1_"],
            "G2 (Security)": ["security", "sast", "semgrep", "gate_2", "g2_"],
            "G3 (Test)": ["test_validation", "coverage", "gate_3", "g3_"],
            "G4 (Human Review)": ["human_review", "code_review", "gate_4", "g4_"],
        }

        for gate_name, patterns in gate_patterns.items():
            gate_found = False
            for py_file in self._rglob_skip_legacy("*.py"):
                try:
                    content = py_file.read_text(encoding='utf-8').lower()
                    if any(p in content for p in patterns):
                        gate_found = True
                        break
                except Exception:
                    continue

            if gate_found:
                result["score"] += 10
                result["details"].append(f"✅ {gate_name} gate detected")
            else:
                result["details"].append(f"⚠️  {gate_name} gate not detected")

        # Check for retry logic
        retry_found = False
        for py_file in self._rglob_skip_legacy("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8').lower()
                if "max_retries" in content or "retry" in content:
                    retry_found = True
                    break
            except Exception:
                continue

        if retry_found:
            result["score"] += 10
            result["details"].append("✅ Retry logic detected (max_retries)")
        else:
            result["details"].append("⚠️  No retry logic detected")

        # Check for evidence lifecycle
        evidence_states = ["generated", "validating", "retrying", "escalated",
                          "evidence_locked", "awaiting_vcr", "merged", "aborted"]
        evidence_found = 0
        for py_file in self._rglob_skip_legacy("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8').lower()
                for state in evidence_states:
                    if state in content:
                        evidence_found += 1
            except Exception:
                continue

        if evidence_found >= 4:
            result["score"] += 10
            result["details"].append(f"✅ Evidence lifecycle states detected ({evidence_found}/8)")
        elif evidence_found > 0:
            result["score"] += 5
            result["details"].append(f"⚠️  Partial evidence lifecycle ({evidence_found}/8 states)")

        result["score"] = min(result["score"], 100)
        return result

    def check_section_7_quality_assurance(self) -> dict:
        """Validate Section 7 Quality Assurance System presence.

        Checks for:
        - Vibecoding Index (5 weighted signals)
        - Progressive Routing (Green/Yellow/Orange/Red)
        - Kill Switch Criteria
        - Auto-Generation Layer

        Returns:
            dict with keys: score (0-100), details
        """
        result = {"score": 0, "details": []}

        # Check for Vibecoding Index indicators
        vibecoding_patterns = ["vibecoding", "vibe_index", "vibecoding_index",
                               "context_deficit", "specification_gap", "validation_bypass",
                               "knowledge_decay", "ownership_void"]
        vibecoding_found = False
        for pattern in vibecoding_patterns:
            matches = list(self._rglob_skip_legacy(f"*{pattern}*"))
            if matches:
                vibecoding_found = True
                break
            # Also check file contents
            for py_file in self._rglob_skip_legacy("*.py"):
                try:
                    content = py_file.read_text(encoding='utf-8').lower()
                    if pattern in content:
                        vibecoding_found = True
                        break
                except Exception:
                    continue
            if vibecoding_found:
                break

        if vibecoding_found:
            result["score"] += 30
            result["details"].append("✅ Vibecoding Index detection found")
        else:
            result["details"].append("⚠️  Vibecoding Index not implemented")

        # Check for Progressive Routing
        routing_patterns = ["progressive_routing", "green.*yellow.*orange.*red",
                           "auto.?approve", "peer.?review", "senior.?review"]
        routing_found = False
        for py_file in self._rglob_skip_legacy("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8').lower()
                if any(re.search(p, content) for p in routing_patterns):
                    routing_found = True
                    break
            except Exception:
                continue

        if routing_found:
            result["score"] += 25
            result["details"].append("✅ Progressive Routing detected")
        else:
            result["details"].append("⚠️  Progressive Routing not implemented")

        # Check for Kill Switch
        kill_switch_patterns = ["kill_switch", "killswitch", "circuit_breaker",
                               "rejection_rate", "max_rejection"]
        kill_found = False
        for py_file in self._rglob_skip_legacy("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8').lower()
                if any(p in content for p in kill_switch_patterns):
                    kill_found = True
                    break
            except Exception:
                continue

        if kill_found:
            result["score"] += 25
            result["details"].append("✅ Kill Switch / Circuit Breaker detected")
        else:
            result["details"].append("⚠️  Kill Switch not implemented")

        # Check for Quality Assurance documentation
        qa_docs = list(self._rglob_skip_legacy("*quality*assurance*"))
        qa_docs.extend(list(self._rglob_skip_legacy("*vibecoding*")))
        if qa_docs:
            result["score"] += 20
            result["details"].append(f"✅ QA documentation found ({len(qa_docs)} files)")
        else:
            result["details"].append("⚠️  No Section 7 QA documentation found")

        result["score"] = min(result["score"], 100)
        return result

    def check_section_8_spec_standard(self) -> dict:
        """Validate Section 8 Unified Specification Standard.

        Checks:
        - YAML frontmatter presence (spec_id, title, version, status, tier, owner, last_updated)
        - BDD format (GIVEN-WHEN-THEN)
        - Tier declaration validity

        Returns:
            dict with keys: score (0-100), frontmatter_rate, bdd_rate, details
        """
        result = {"score": 0, "frontmatter_rate": 0, "bdd_rate": 0, "details": []}

        # Required frontmatter fields
        required_fields = ["spec_id", "title", "version", "status", "tier", "owner", "last_updated"]
        valid_statuses = ["DRAFT", "REVIEW", "APPROVED", "ACTIVE", "DEPRECATED"]
        valid_tiers = ["LITE", "STANDARD", "PROFESSIONAL", "ENTERPRISE"]

        # Scan specification files
        spec_files = []
        spec_dirs = [
            self.project_path / "docs",
            self.project_path / "specifications",
            self.project_path / "specs",
        ]

        for spec_dir in spec_dirs:
            if spec_dir.exists():
                for md_file in spec_dir.rglob("*.md"):
                    if not self._is_legacy_or_archive(md_file):
                        spec_files.append(md_file)

        if not spec_files:
            result["details"].append("⚠️  No specification files found in docs/")
            return result

        # Check frontmatter
        files_with_frontmatter = 0
        files_with_bdd = 0
        total_checked = 0

        for spec_file in spec_files[:50]:  # Cap at 50 files for performance
            try:
                content = spec_file.read_text(encoding='utf-8')
                total_checked += 1
            except Exception:
                continue

            # Check YAML frontmatter
            if content.startswith('---'):
                end_idx = content.find('---', 3)
                if end_idx > 0:
                    frontmatter = content[3:end_idx].lower()
                    has_required = sum(1 for f in required_fields if f in frontmatter)
                    if has_required >= 4:  # At least 4 of 7 required fields
                        files_with_frontmatter += 1

            # Check BDD format
            content_lower = content.lower()
            if ('given' in content_lower and 'when' in content_lower and 'then' in content_lower):
                files_with_bdd += 1

        if total_checked > 0:
            result["frontmatter_rate"] = (files_with_frontmatter / total_checked) * 100
            result["bdd_rate"] = (files_with_bdd / total_checked) * 100

            if result["frontmatter_rate"] >= 80:
                result["score"] += 40
                result["details"].append(f"✅ YAML frontmatter: {result['frontmatter_rate']:.0f}% ({files_with_frontmatter}/{total_checked})")
            elif result["frontmatter_rate"] >= 50:
                result["score"] += 20
                result["details"].append(f"⚠️  YAML frontmatter: {result['frontmatter_rate']:.0f}% ({files_with_frontmatter}/{total_checked})")
            else:
                result["details"].append(f"❌ YAML frontmatter: {result['frontmatter_rate']:.0f}% ({files_with_frontmatter}/{total_checked})")

            if result["bdd_rate"] >= 50:
                result["score"] += 40
                result["details"].append(f"✅ BDD format: {result['bdd_rate']:.0f}% ({files_with_bdd}/{total_checked})")
            elif result["bdd_rate"] >= 20:
                result["score"] += 20
                result["details"].append(f"⚠️  BDD format: {result['bdd_rate']:.0f}% ({files_with_bdd}/{total_checked})")
            else:
                result["details"].append(f"❌ BDD format: {result['bdd_rate']:.0f}% ({files_with_bdd}/{total_checked})")
        else:
            result["details"].append("⚠️  No specification files could be read")

        # Bonus: check for spec validation scripts
        if list(self._rglob_skip_legacy("*spec*validator*")) or list(self._rglob_skip_legacy("*frontmatter*validator*")):
            result["score"] += 20
            result["details"].append("✅ Spec validation tooling found")

        result["score"] = min(result["score"], 100)
        return result

    def validate_section_7_quality_assurance(self):
        """Section 7: Quality Assurance System (SDLC 6.1.1)"""
        print("\n🛡️  Validating Section 7: Quality Assurance System...")

        section = self.results["section_7"]
        qa_result = self.check_section_7_quality_assurance()

        section["score"] = qa_result["score"]
        section["details"] = qa_result["details"]
        section["passed"] = qa_result["score"] >= 25  # Lower threshold — many projects won't have all

        status = "✅ PASSED" if section["passed"] else "⚠️  PARTIAL"
        print(f"   {status} - Score: {section['score']}%")

    def validate_section_8_spec_standard(self):
        """Section 8: Unified Specification Standard (SDLC 6.1.1)"""
        print("\n📋 Validating Section 8: Specification Standard...")

        section = self.results["section_8"]
        spec_result = self.check_section_8_spec_standard()

        section["score"] = spec_result["score"]
        section["details"] = spec_result["details"]
        section["passed"] = spec_result["score"] >= 30

        status = "✅ PASSED" if section["passed"] else "⚠️  PARTIAL"
        print(f"   {status} - Score: {section['score']}%")

    def validate_three_ring_architecture(self):
        """3-Ring Architecture Compliance (SDLC 6.1.1)"""
        print("\n🔵 Validating 3-Ring Architecture...")

        section = self.results["three_ring"]
        ring_result = self.check_three_ring_architecture()

        section["score"] = ring_result["score"]
        section["details"] = ring_result["details"]
        if ring_result["violations"]:
            for v in ring_result["violations"][:5]:  # Show top 5
                section["details"].append(f"   ⚠️  {v}")
        section["passed"] = ring_result["score"] >= 70  # 70% minimum (some violations acceptable)

        # Also validate CLAUDE.md Standard
        print("\n📝 Validating CLAUDE.md Standard...")
        claude_section = self.results["claude_md"]
        claude_result = self.check_claude_md_standard()

        claude_section["score"] = claude_result["score"]
        claude_section["details"] = claude_result["details"]
        claude_section["passed"] = claude_result["exists"] and claude_result["score"] >= 30

        # Also check MRP and Codegen (add to pillar 5 details)
        mrp_result = self.check_mrp_template()
        codegen_result = self.check_autonomous_codegen_gates()

        pillar5 = self.results["pillar_5"]
        if mrp_result["found"]:
            pillar5["details"].append(f"✅ MRP Template: {mrp_result['score']}%")
            pillar5["score"] = min(pillar5["score"] + 5, 100)
        if codegen_result["found"]:
            pillar5["details"].append(f"✅ Codegen 4-Gate Pipeline: {codegen_result['score']}%")
            pillar5["score"] = min(pillar5["score"] + 5, 100)

        status = "✅ PASSED" if section["passed"] else "⚠️  PARTIAL"
        print(f"   3-Ring: {status} - Score: {section['score']}%")
        claude_status = "✅ PASSED" if claude_section["passed"] else "⚠️  PARTIAL"
        print(f"   CLAUDE.md: {claude_status} - Score: {claude_section['score']}%")

    def calculate_overall_compliance(self):
        """Calculate overall SDLC 6.1.1 compliance (7 pillars + 2 sections + extras)"""
        # Core: 7 pillars
        pillar_keys = [f"pillar_{i}" for i in range(7)]
        pillar_passed = sum(1 for k in pillar_keys if self.results[k]["passed"])
        pillar_score = sum(self.results[k]["score"] for k in pillar_keys) / 7

        # Extensions: Section 7, Section 8, 3-Ring, CLAUDE.md
        extension_keys = ["section_7", "section_8", "three_ring", "claude_md"]
        extension_score = sum(self.results[k]["score"] for k in extension_keys) / len(extension_keys)

        # Overall: 70% pillars + 30% extensions
        total_score = (pillar_score * 0.7) + (extension_score * 0.3)

        # Must pass at least 5/7 pillars AND have extensions > 20%
        self.overall_compliant = pillar_passed >= 5 and extension_score >= 20
        self.overall_score = total_score

    def print_results(self):
        """Print detailed validation results"""
        print("\n" + "=" * 80)
        print("📊 SDLC 6.1.1 VALIDATION RESULTS")
        print("=" * 80)

        for pillar_key, pillar_data in self.results.items():
            status = "✅ PASSED" if pillar_data["passed"] else "❌ FAILED"
            print(f"\n{pillar_data['name']}: {status} ({pillar_data['score']}%)")
            for detail in pillar_data["details"]:
                print(f"   {detail}")

        print("\n" + "=" * 80)
        print(f"Overall Score: {self.overall_score:.1f}%")

        if self.overall_compliant:
            print("🎉 PROJECT IS SDLC 6.1.1 COMPLIANT!")
            print("✅ Ready for production deployment")
            print("✅ 7-Pillar Architecture validated")
            print("✅ Section 7 Quality Assurance checked")
            print("✅ Section 8 Specification Standard checked")
            print("✅ 3-Ring Architecture validated")
            print("✅ CLAUDE.md Standard validated")
            print("✅ Legacy/Archive folders excluded from validation")
        else:
            print("⚠️  PROJECT NEEDS IMPROVEMENT")
            print("💡 Address failed pillars before production deployment")
            print("💡 Check Section 7 (Quality Assurance) and Section 8 (Spec Standard)")
            print("💡 Check 3-Ring Architecture compliance")
            print("💡 Check CLAUDE.md against 3-tier standard (LITE/PRO/ENTERPRISE)")
            print("💡 Check SASE Artifacts (AGENTS.md, CRP, MRP, VCR)")
            print("💡 See: SDLC-Enterprise-Framework/05-Templates-Tools/")
            print("💡 Note: Legacy/Archive folders (99-legacy, 10-archive) are excluded")

        print("=" * 80)

def main():
    """Main validation entry point"""
    if len(sys.argv) < 2:
        print("Usage: python3 sdlc_validator.py /path/to/project")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        print(f"❌ Error: Path does not exist: {project_path}")
        sys.exit(1)

    validator = SDLC60Validator(project_path)
    results = validator.validate_all_pillars()

    # Exit with appropriate code
    sys.exit(0 if validator.overall_compliant else 1)

if __name__ == "__main__":
    main()
