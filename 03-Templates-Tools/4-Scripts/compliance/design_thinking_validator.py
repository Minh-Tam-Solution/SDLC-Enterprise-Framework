#!/usr/bin/env python3
"""
=========================================================================
SDLC 5.0 Design Thinking Validator
Validates Design Thinking 5-phase methodology compliance (Pillar 0)

Version: 5.0.0
Date: November 7, 2025
Status: ACTIVE - PRODUCTION READY
Authority: CPO Office + Design Thinking Excellence
Foundation: Battle-tested on NQH-Bot (96% time savings proven)

VALIDATION PHASES:
Phase 1: Empathize - User research and empathy mapping
Phase 2: Define - Problem statement clarity and validation
Phase 3: Ideate - Solution generation and creativity
Phase 4: Prototype - Rapid validation and iteration
Phase 5: Test - User testing and feedback incorporation

SUCCESS CRITERIA:
- All 5 phases documented
- User research evidence present
- Problem statement validated
- Multiple solutions considered
- Prototype tested with users
- Feedback incorporated
- 75-90% feature adoption target

PROVEN RESULTS (NQH-Bot):
- Time: 26 hours → 1 hour (96% reduction)
- Adoption: 30% → 75-90% (2.5-3x improvement)
- Rework: -60% reduction
- ROI: 6,824% documented
=========================================================================
"""

import os
import sys
import re
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Any
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

class DesignThinkingValidator:
    """
    Validates Design Thinking methodology compliance in projects

    Checks for evidence of Stanford d.school 5-phase approach:
    1. Empathize (user research)
    2. Define (problem statements)
    3. Ideate (solution generation)
    4. Prototype (rapid validation)
    5. Test (user testing)
    """

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.results = {
            'phase_1_empathize': {'score': 0, 'evidence': [], 'status': 'NOT_FOUND'},
            'phase_2_define': {'score': 0, 'evidence': [], 'status': 'NOT_FOUND'},
            'phase_3_ideate': {'score': 0, 'evidence': [], 'status': 'NOT_FOUND'},
            'phase_4_prototype': {'score': 0, 'evidence': [], 'status': 'NOT_FOUND'},
            'phase_5_test': {'score': 0, 'evidence': [], 'status': 'NOT_FOUND'},
            'overall_score': 0,
            'compliance_level': 'NONE'
        }

        # Phase detection patterns
        self.phase_patterns = {
            'empathize': [
                r'user\s+research',
                r'empathy\s+map',
                r'user\s+interview',
                r'customer\s+discovery',
                r'pain\s+point',
                r'user\s+journey',
                r'persona'
            ],
            'define': [
                r'problem\s+statement',
                r'point\s+of\s+view',
                r'how\s+might\s+we',
                r'design\s+challenge',
                r'needs\s+statement',
                r'user\s+needs'
            ],
            'ideate': [
                r'ideation',
                r'brainstorm',
                r'solution\s+generation',
                r'scamper',
                r'thinking\s+hats',
                r'concept\s+development',
                r'alternative\s+solutions'
            ],
            'prototype': [
                r'prototype',
                r'mvp',
                r'mockup',
                r'wireframe',
                r'proof\s+of\s+concept',
                r'rapid\s+prototype',
                r'low\s+fidelity'
            ],
            'test': [
                r'user\s+testing',
                r'usability\s+test',
                r'user\s+feedback',
                r'validation',
                r'iteration',
                r'feedback\s+loop',
                r'user\s+validation'
            ]
        }

        # Documentation locations to search
        self.doc_locations = [
            'docs',
            'documentation',
            'design',
            'research',
            'planning',
            'requirements'
        ]

    def validate(self) -> Dict[str, Any]:
        """
        Run complete Design Thinking validation

        Returns:
            Dict with validation results for all 5 phases
        """
        logger.info("🎨 SDLC 5.0 Design Thinking Validator")
        logger.info("=" * 60)
        logger.info(f"Project: {self.project_path}")
        logger.info(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("")

        # Validate each phase
        self._validate_phase_1_empathize()
        self._validate_phase_2_define()
        self._validate_phase_3_ideate()
        self._validate_phase_4_prototype()
        self._validate_phase_5_test()

        # Calculate overall score
        self._calculate_overall_score()

        # Display results
        self._display_results()

        return self.results

    def _validate_phase_1_empathize(self):
        """Validate Empathize phase - User research and empathy"""
        logger.info("📊 Phase 1: EMPATHIZE (User Research)")
        logger.info("-" * 60)

        evidence = self._search_for_patterns('empathize')

        if evidence:
            score = min(100, len(evidence) * 20)  # 20 points per evidence, max 100
            self.results['phase_1_empathize'] = {
                'score': score,
                'evidence': evidence,
                'status': 'COMPLIANT' if score >= 60 else 'PARTIAL'
            }
            logger.info(f"✅ Found {len(evidence)} evidence items")
            for item in evidence[:3]:  # Show first 3
                logger.info(f"   • {item}")
            logger.info(f"Score: {score}/100")
        else:
            logger.info("❌ No user research evidence found")
            logger.info("   Missing: User interviews, empathy maps, personas")

        logger.info("")

    def _validate_phase_2_define(self):
        """Validate Define phase - Problem statement clarity"""
        logger.info("🎯 Phase 2: DEFINE (Problem Statement)")
        logger.info("-" * 60)

        evidence = self._search_for_patterns('define')

        if evidence:
            score = min(100, len(evidence) * 25)  # 25 points per evidence
            self.results['phase_2_define'] = {
                'score': score,
                'evidence': evidence,
                'status': 'COMPLIANT' if score >= 60 else 'PARTIAL'
            }
            logger.info(f"✅ Found {len(evidence)} problem statements")
            for item in evidence[:3]:
                logger.info(f"   • {item}")
            logger.info(f"Score: {score}/100")
        else:
            logger.info("❌ No problem statements found")
            logger.info("   Missing: Clear problem definition, 'How Might We' statements")

        logger.info("")

    def _validate_phase_3_ideate(self):
        """Validate Ideate phase - Solution generation"""
        logger.info("💡 Phase 3: IDEATE (Solution Generation)")
        logger.info("-" * 60)

        evidence = self._search_for_patterns('ideate')

        if evidence:
            score = min(100, len(evidence) * 20)
            self.results['phase_3_ideate'] = {
                'score': score,
                'evidence': evidence,
                'status': 'COMPLIANT' if score >= 60 else 'PARTIAL'
            }
            logger.info(f"✅ Found {len(evidence)} ideation activities")
            for item in evidence[:3]:
                logger.info(f"   • {item}")
            logger.info(f"Score: {score}/100")
        else:
            logger.info("❌ No ideation evidence found")
            logger.info("   Missing: Brainstorming sessions, multiple solution concepts")

        logger.info("")

    def _validate_phase_4_prototype(self):
        """Validate Prototype phase - Rapid validation"""
        logger.info("🔨 Phase 4: PROTOTYPE (Rapid Validation)")
        logger.info("-" * 60)

        evidence = self._search_for_patterns('prototype')

        if evidence:
            score = min(100, len(evidence) * 20)
            self.results['phase_4_prototype'] = {
                'score': score,
                'evidence': evidence,
                'status': 'COMPLIANT' if score >= 60 else 'PARTIAL'
            }
            logger.info(f"✅ Found {len(evidence)} prototypes")
            for item in evidence[:3]:
                logger.info(f"   • {item}")
            logger.info(f"Score: {score}/100")
        else:
            logger.info("❌ No prototype evidence found")
            logger.info("   Missing: MVPs, mockups, proof of concepts")

        logger.info("")

    def _validate_phase_5_test(self):
        """Validate Test phase - User testing and iteration"""
        logger.info("🧪 Phase 5: TEST (User Validation)")
        logger.info("-" * 60)

        evidence = self._search_for_patterns('test')

        if evidence:
            score = min(100, len(evidence) * 20)
            self.results['phase_5_test'] = {
                'score': score,
                'evidence': evidence,
                'status': 'COMPLIANT' if score >= 60 else 'PARTIAL'
            }
            logger.info(f"✅ Found {len(evidence)} user testing activities")
            for item in evidence[:3]:
                logger.info(f"   • {item}")
            logger.info(f"Score: {score}/100")
        else:
            logger.info("❌ No user testing evidence found")
            logger.info("   Missing: User feedback, validation tests, iterations")

        logger.info("")

    def _search_for_patterns(self, phase: str) -> List[str]:
        """
        Search project for evidence of specific Design Thinking phase

        Args:
            phase: Phase name (empathize, define, ideate, prototype, test)

        Returns:
            List of evidence items found
        """
        evidence = []
        patterns = self.phase_patterns.get(phase, [])

        # Search in documentation directories
        for doc_dir in self.doc_locations:
            doc_path = self.project_path / doc_dir
            if not doc_path.exists():
                continue

            # Search markdown files
            for md_file in doc_path.rglob('*.md'):
                try:
                    content = md_file.read_text(encoding='utf-8', errors='ignore')
                    content_lower = content.lower()

                    for pattern in patterns:
                        if re.search(pattern, content_lower):
                            relative_path = md_file.relative_to(self.project_path)
                            evidence.append(f"{relative_path}: {pattern}")
                            break  # One evidence per file
                except Exception:
                    continue

        return list(set(evidence))  # Remove duplicates

    def _calculate_overall_score(self):
        """Calculate overall Design Thinking compliance score"""
        phase_scores = [
            self.results['phase_1_empathize']['score'],
            self.results['phase_2_define']['score'],
            self.results['phase_3_ideate']['score'],
            self.results['phase_4_prototype']['score'],
            self.results['phase_5_test']['score']
        ]

        self.results['overall_score'] = sum(phase_scores) / 5

        # Determine compliance level
        score = self.results['overall_score']
        if score >= 80:
            self.results['compliance_level'] = 'EXCELLENT'
        elif score >= 60:
            self.results['compliance_level'] = 'GOOD'
        elif score >= 40:
            self.results['compliance_level'] = 'PARTIAL'
        else:
            self.results['compliance_level'] = 'MINIMAL'

    def _display_results(self):
        """Display validation results summary"""
        logger.info("=" * 60)
        logger.info("📊 DESIGN THINKING VALIDATION SUMMARY")
        logger.info("=" * 60)

        # Phase results
        phases = [
            ('Phase 1 (Empathize)', 'phase_1_empathize'),
            ('Phase 2 (Define)', 'phase_2_define'),
            ('Phase 3 (Ideate)', 'phase_3_ideate'),
            ('Phase 4 (Prototype)', 'phase_4_prototype'),
            ('Phase 5 (Test)', 'phase_5_test')
        ]

        for phase_name, phase_key in phases:
            result = self.results[phase_key]
            status_icon = '✅' if result['status'] == 'COMPLIANT' else '⚠️' if result['status'] == 'PARTIAL' else '❌'
            logger.info(f"{status_icon} {phase_name}: {result['score']}/100 - {result['status']}")

        logger.info("")
        logger.info(f"Overall Score: {self.results['overall_score']:.1f}/100")
        logger.info(f"Compliance Level: {self.results['compliance_level']}")
        logger.info("")

        # Recommendations
        if self.results['compliance_level'] == 'EXCELLENT':
            logger.info("🎉 EXCELLENT Design Thinking compliance!")
            logger.info("   Similar to NQH-Bot level (96% time savings)")
        elif self.results['compliance_level'] == 'GOOD':
            logger.info("✅ GOOD Design Thinking practice")
            logger.info("   Continue strengthening weaker phases")
        elif self.results['compliance_level'] == 'PARTIAL':
            logger.info("⚠️  PARTIAL Design Thinking adoption")
            logger.info("   Recommend strengthening all phases for full ROI")
        else:
            logger.info("❌ MINIMAL Design Thinking evidence")
            logger.info("   Strongly recommend implementing 5-phase methodology")
            logger.info("   Expected ROI: 6,824% (NQH-Bot proven)")

        logger.info("")
        logger.info("📚 Resources:")
        logger.info("   • SDLC 5.0 Design Thinking Guide: /00-Overview/SDLC-5.0-Overview.md")
        logger.info("   • AI Tools: /06-Templates-Tools/ai-tools/design-thinking/")
        logger.info("   • Case Study: NQH-Bot 96% time savings")
        logger.info("")

def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        logger.info("SDLC 5.0 Design Thinking Validator")
        logger.info("=" * 60)
        logger.info("")
        logger.info("Usage: python design_thinking_validator.py <project_path>")
        logger.info("")
        logger.info("Validates 5-phase Design Thinking methodology:")
        logger.info("  Phase 1: Empathize (user research)")
        logger.info("  Phase 2: Define (problem statements)")
        logger.info("  Phase 3: Ideate (solution generation)")
        logger.info("  Phase 4: Prototype (rapid validation)")
        logger.info("  Phase 5: Test (user testing)")
        logger.info("")
        logger.info("Example:")
        logger.info("  python design_thinking_validator.py /path/to/project")
        logger.info("")
        logger.info("Expected Results:")
        logger.info("  • 96% time savings (26 hours → 1 hour)")
        logger.info("  • 2.5-3x feature adoption (30% → 75-90%)")
        logger.info("  • 60% less rework")
        logger.info("  • 6,824% ROI (NQH-Bot proven)")
        logger.info("")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        logger.error(f"Error: Project path '{project_path}' does not exist")
        sys.exit(1)

    # Run validation
    validator = DesignThinkingValidator(project_path)
    results = validator.validate()

    # Exit with appropriate code
    if results['compliance_level'] in ['EXCELLENT', 'GOOD']:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
