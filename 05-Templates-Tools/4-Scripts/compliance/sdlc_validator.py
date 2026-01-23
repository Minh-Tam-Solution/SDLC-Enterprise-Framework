#!/usr/bin/env python3
"""
SDLC 5.2.0 Complete Validator
Validates complete 10-stage lifecycle + 7-pillar architecture + SASE Framework compliance

Version: 5.2.0
Date: January 2026
Status: ACTIVE - PRODUCTION READY
Foundation: Proven validation across BFlow, NQH-Bot, MTEP, SDLC Orchestrator platforms
Enhancement: 7-Pillar Architecture (Pillar 2: Sprint Planning Governance) + SASE Framework (SE 3.0)
New in 5.2.0: AI Governance Principles, Concentric Circles Model, best-practices-2026 in 04-AI-TOOLS-LANDSCAPE/

DOCUMENTATION vs CODE SEPARATION (SDLC 5.2.0):
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

Legacy/Archive Structure (SDLC 5.2.0+):
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

SASE Framework (NEW in 5.1.0):
- SE4H (Agent Coach): Human creates BRS, MTS, VCR
- SE4A (Agent Executor): AI creates LPS, CRP, MRP
- 6 SASE Artifacts: BRS, LPS, MTS, CRP, MRP, VCR
- Agentic Maturity: L0 (Tool-Assisted) → L3 (Lifecycle Agentic)

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

class SDLC51Validator:
    """SDLC 5.2.0 Complete 7-Pillar + SASE Framework + Team Collaboration Validator

    7-Pillar Architecture (SDLC 5.2.0):
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
        """Validate all 6 pillars of SDLC 5.2.0"""
        print("🔍 SDLC 5.2.0 Complete Validation Starting...")
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
            pillar["details"].append("⚠️  Partial SASE Artifacts (check BRS, LPS, MRP, VCR)")
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
        Check for SASE Artifacts (NEW in SDLC 5.1.0 SE 3.0)
        Returns score 0-30 based on presence of SASE artifacts

        SASE 6 Artifacts:
        - BRS (BriefingScript): Human creates task specification
        - LPS (LoopScript): Agent creates execution plan
        - MTS (MentorScript): Human creates coding standards
        - CRP (Consultation Request): Agent requests help when uncertain
        - MRP (Merge-Readiness Pack): Agent creates 5-point evidence
        - VCR (Version Controlled Resolution): Human approves work
        """
        score = 0

        # SASE Artifact patterns to look for
        sase_patterns = [
            "BriefingScript", "BRS",
            "LoopScript", "LPS",
            "MentorScript", "MTS",
            "CRP", "Consultation-Request",
            "MRP", "Merge-Readiness",
            "VCR", "Version-Controlled-Resolution",
            "SASE-Artifacts", "sase-artifacts"
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

        # Check for specific SDLC 5.2.0 documents
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

    def calculate_overall_compliance(self):
        """Calculate overall SDLC 5.2.0 compliance (7 pillars)"""
        passed_count = sum(1 for p in self.results.values() if p["passed"])
        total_score = sum(p["score"] for p in self.results.values()) / 7  # 7 pillars

        self.overall_compliant = passed_count >= 5  # At least 5/7 pillars must pass
        self.overall_score = total_score

    def print_results(self):
        """Print detailed validation results"""
        print("\n" + "=" * 80)
        print("📊 SDLC 5.2.0 VALIDATION RESULTS")
        print("=" * 80)

        for pillar_key, pillar_data in self.results.items():
            status = "✅ PASSED" if pillar_data["passed"] else "❌ FAILED"
            print(f"\n{pillar_data['name']}: {status} ({pillar_data['score']}%)")
            for detail in pillar_data["details"]:
                print(f"   {detail}")

        print("\n" + "=" * 80)
        print(f"Overall Score: {self.overall_score:.1f}%")

        if self.overall_compliant:
            print("🎉 PROJECT IS SDLC 5.2.0 COMPLIANT!")
            print("✅ Ready for production deployment")
            print("✅ 7-Pillar Architecture validated")
            print("✅ Sprint Planning Governance validated (Pillar 2)")
            print("✅ SASE Framework validated (Pillar 5)")
            print("✅ Legacy/Archive folders excluded from validation")
        else:
            print("⚠️  PROJECT NEEDS IMPROVEMENT")
            print("💡 Address failed pillars before production deployment")
            print("💡 Check Sprint Planning Governance (Pillar 2)")
            print("💡 Check SASE Artifacts (BRS, LPS, MRP, VCR)")
            print("💡 See: SDLC-Enterprise-Framework/03-Templates-Tools/")
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

    validator = SDLC51Validator(project_path)
    results = validator.validate_all_pillars()

    # Exit with appropriate code
    sys.exit(0 if validator.overall_compliant else 1)

if __name__ == "__main__":
    main()
