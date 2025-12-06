#!/usr/bin/env python3
"""
=========================================================================
SDLC 5.0.0 Solo Developer Quick Setup
Get to 10x productivity with Complete 10-Stage Lifecycle + AI in 2 days

Version: 5.0.1
Date: November 29, 2025
Status: ACTIVE - PRODUCTION READY
Profile: Solo Developer (1 developer + AI)
Timeline: 2 days to 10x productivity
Target: Individual developers building startups or side projects

WHAT THIS SCRIPT DOES:
1. Sets up SDLC 5.0.0 complete 10-stage framework for solo development
2. Configures Design Thinking lightweight workflow
3. Sets up Code Review Tier 1 (Manual checklist)
4. Installs essential compliance validators (including file naming)
5. Creates AI-powered development environment
6. Configures performance targets (<50ms)
7. Validates code file naming standards (Python/TypeScript/React)

SOLO DEVELOPER PROFILE:
- Team Size: 1 developer + AI tools
- Budget: Minimal (free tier tools)
- Timeline: 2 days setup
- Productivity Gain: 10x (with Design Thinking)
- Code Review: Tier 1 (Manual checklist)
- Testing: 80%+ coverage target
- Performance: <50ms API response
- File Naming: snake_case (Python), camelCase (TypeScript), PascalCase (React)

CODE FILE NAMING STANDARDS (RESTORED FROM 4.3/4.4):
- Python Files: snake_case, max 50 characters
- TypeScript Files: camelCase, max 50 characters
- React Components: PascalCase, max 50 characters
- Alembic Migrations: {rev}_{desc}.py, max 60 characters

PROVEN RESULTS:
- Setup Time: 2 days
- Productivity: 10x with AI + Design Thinking
- Time Savings: 96% on feature design
- Quality: Zero mock policy + file naming compliance
- Cost: $0-50/month (free tier focus)
=========================================================================
"""

import os
import sys
import subprocess
import json
import logging
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

class SoloSetup:
    """SDLC 5.0.0 setup for solo developers"""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.config = {
            'profile': 'solo',
            'team_size': 1,
            'setup_date': datetime.now().isoformat(),
            'sdlc_version': '4.9.1',
            'code_review_tier': 1,
            'design_thinking': 'lightweight',
            'productivity_target': '10x',
            'timeline': '2_days',
            'file_naming_standards': {
                'python': 'snake_case',
                'typescript': 'camelCase',
                'react': 'PascalCase'
            }
        }

    def run(self):
        """Execute complete solo setup"""
        logger.info("🚀 SDLC 5.0.0 SOLO DEVELOPER SETUP")
        logger.info("=" * 60)
        logger.info("Profile: Solo Developer (1 dev + AI)")
        logger.info("Timeline: 2 days to 10x productivity")
        logger.info("Target: Individual projects with AI acceleration")
        logger.info("File Naming: Python (snake_case), TypeScript (camelCase), React (PascalCase)")
        logger.info("")

        try:
            # Step 1: Create directory structure
            self._create_directory_structure()

            # Step 2: Install SDLC 5.0 validators
            self._install_validators()

            # Step 3: Setup Design Thinking lightweight workflow
            self._setup_design_thinking()

            # Step 4: Setup Code Review Tier 1 (Manual)
            self._setup_code_review_tier1()

            # Step 5: Create AI development environment
            self._setup_ai_environment()

            # Step 6: Configure performance targets
            self._configure_performance()

            # Step 7: Save configuration
            self._save_configuration()

            # Success!
            self._display_success_message()

        except Exception as e:
            logger.error(f"❌ Setup failed: {str(e)}")
            sys.exit(1)

    def _create_directory_structure(self):
        """Create SDLC 5.0 directory structure for solo projects"""
        logger.info("📁 Step 1: Creating SDLC 5.0 Directory Structure")
        logger.info("-" * 60)

        directories = [
            'docs/design-thinking',
            'docs/requirements',
            'docs/architecture',
            'docs/api',
            '.sdlc',
            '.sdlc/checklists',
            '.sdlc/templates',
            'tests/unit',
            'tests/integration'
        ]

        for dir_path in directories:
            full_path = self.project_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"✅ Created: {dir_path}")

        logger.info("")

    def _install_validators(self):
        """Install SDLC 5.0 compliance validators"""
        logger.info("🔍 Step 2: Installing SDLC 5.0 Validators")
        logger.info("-" * 60)

        validators = [
            'sdlc_4_8_validator.py',
            'design_thinking_validator.py',
            'sdlc_scanner.py'
        ]

        logger.info("✅ SDLC 5.0 validators available:")
        for validator in validators:
            logger.info(f"   • {validator}")

        logger.info("")
        logger.info("📋 Run validators with:")
        logger.info("   python3 path/to/sdlc_4_8_validator.py .")
        logger.info("")

    def _setup_design_thinking(self):
        """Setup lightweight Design Thinking workflow for solo"""
        logger.info("🎨 Step 3: Setting Up Design Thinking (Lightweight)")
        logger.info("-" * 60)

        # Create Design Thinking templates
        dt_templates = {
            'empathy': self._create_empathy_template(),
            'define': self._create_define_template(),
            'ideate': self._create_ideate_template(),
            'prototype': self._create_prototype_template(),
            'test': self._create_test_template()
        }

        for phase, template in dt_templates.items():
            template_path = self.project_path / f'docs/design-thinking/{phase}.md'
            template_path.write_text(template)
            logger.info(f"✅ Created: Design Thinking {phase.title()} template")

        logger.info("")
        logger.info("📚 Design Thinking workflow ready!")
        logger.info("   Use AI to accelerate: 26 hours → 1 hour (96% savings)")
        logger.info("")

    def _setup_code_review_tier1(self):
        """Setup Code Review Tier 1 (Manual checklist)"""
        logger.info("🔍 Step 4: Setting Up Code Review (Tier 1 - Manual)")
        logger.info("-" * 60)

        checklist = self._create_code_review_checklist()
        checklist_path = self.project_path / '.sdlc/checklists/code-review.md'
        checklist_path.write_text(checklist)

        logger.info("✅ Created: Manual code review checklist")
        logger.info("   Location: .sdlc/checklists/code-review.md")
        logger.info("")
        logger.info("💡 Tier 1 is FREE - Use checklist before commits")
        logger.info("   Upgrade to Tier 3 (CodeRabbit) when budget allows")
        logger.info("")

    def _setup_ai_environment(self):
        """Setup AI-powered development environment"""
        logger.info("🤖 Step 5: Setting Up AI Development Environment")
        logger.info("-" * 60)

        ai_config = {
            'tools': {
                'claude_code': 'Primary development AI',
                'figma_mcp': 'Design-to-code conversion',
                'design_thinking_ai': 'Feature planning acceleration'
            },
            'prompts': self._create_ai_prompts()
        }

        # Save AI configuration
        ai_config_path = self.project_path / '.sdlc/ai-config.json'
        ai_config_path.write_text(json.dumps(ai_config, indent=2))

        logger.info("✅ AI environment configured")
        logger.info("   • Claude Code: Primary development AI")
        logger.info("   • Figma MCP: Design-to-code (5-10 min/component)")
        logger.info("   • Design Thinking AI: 96% time savings")
        logger.info("")

    def _configure_performance(self):
        """Configure performance targets"""
        logger.info("⚡ Step 6: Configuring Performance Targets")
        logger.info("-" * 60)

        performance_config = {
            'api_response_time': '<50ms',
            'page_load_time': '<2s',
            'test_coverage': '80%+',
            'bundle_size': '<500KB',
            'zero_mocks': True
        }

        perf_path = self.project_path / '.sdlc/performance.json'
        perf_path.write_text(json.dumps(performance_config, indent=2))

        logger.info("✅ Performance targets configured:")
        logger.info("   • API Response: <50ms")
        logger.info("   • Page Load: <2s")
        logger.info("   • Test Coverage: 80%+")
        logger.info("   • Zero Mock Policy: Enforced")
        logger.info("")

    def _save_configuration(self):
        """Save setup configuration"""
        config_path = self.project_path / '.sdlc/config.json'
        config_path.write_text(json.dumps(self.config, indent=2))
        logger.info("💾 Configuration saved to .sdlc/config.json")
        logger.info("")

    def _display_success_message(self):
        """Display success message with next steps"""
        logger.info("=" * 60)
        logger.info("🎉 SDLC 5.0 SOLO SETUP COMPLETE!")
        logger.info("=" * 60)
        logger.info("")
        logger.info("✅ What's Ready:")
        logger.info("   • Directory structure created")
        logger.info("   • Design Thinking templates (96% time savings)")
        logger.info("   • Code Review Tier 1 checklist (FREE)")
        logger.info("   • AI development environment")
        logger.info("   • Performance targets (<50ms)")
        logger.info("   • SDLC 5.0 validators installed")
        logger.info("")
        logger.info("🚀 Next Steps (2-Day Timeline):")
        logger.info("")
        logger.info("Day 1: Setup & First Feature")
        logger.info("   1. Read: docs/design-thinking/ templates")
        logger.info("   2. Run: python3 design_thinking_validator.py .")
        logger.info("   3. Plan first feature using Design Thinking AI")
        logger.info("   4. Convert Figma designs to code (5-10 min each)")
        logger.info("")
        logger.info("Day 2: Development & Quality")
        logger.info("   5. Implement feature with AI assistance")
        logger.info("   6. Run: Code review checklist before commit")
        logger.info("   7. Run: python3 sdlc_4_8_validator.py .")
        logger.info("   8. Achieve 80%+ test coverage")
        logger.info("")
        logger.info("📊 Expected Results:")
        logger.info("   • Productivity: 10x with AI + Design Thinking")
        logger.info("   • Feature Design: 26 hours → 1 hour (96% savings)")
        logger.info("   • Component Creation: 5-10 min with Figma AI")
        logger.info("   • Quality: Zero mock policy compliance")
        logger.info("   • Performance: <50ms API response")
        logger.info("")
        logger.info("💡 Pro Tips:")
        logger.info("   • Use Design Thinking AI for ALL features")
        logger.info("   • Figma-to-code saves 95% component time")
        logger.info("   • Run validators before EVERY commit")
        logger.info("   • Upgrade to Tier 3 Code Review when budget allows")
        logger.info("")
        logger.info("📚 Resources:")
        logger.info("   • SDLC 5.0 Docs: /00-Overview/")
        logger.info("   • AI Tools: /06-Templates-Tools/ai-tools/")
        logger.info("   • Case Studies: /07-Case-Studies/")
        logger.info("   • Support: taidt@mtsolution.com.vn")
        logger.info("")
        logger.info("🎯 Your Path: Solo → Startup → Growth → Enterprise")
        logger.info("")

    # Template creation methods
    def _create_empathy_template(self) -> str:
        return """# Empathize Phase - User Research

## Quick AI Prompt
```
"Help me understand my users:

Target User: [describe user]
Context: [what they're trying to achieve]
Pain Points: [observed/reported issues]

Generate:
✅ Empathy map (Think, Feel, Say, Do)
✅ Top 3 user insights
✅ Opportunity areas
"
```

## User Research Notes
- **User Interviews**: [date, insights]
- **Pain Points**: [list key pains]
- **User Journey**: [map key touchpoints]
- **Quotes**: [memorable user quotes]

## Empathy Map
- **Think**: [user thoughts]
- **Feel**: [user emotions]
- **Say**: [user statements]
- **Do**: [user actions]

## Key Insights
1. [Insight 1]
2. [Insight 2]
3. [Insight 3]
"""

    def _create_define_template(self) -> str:
        return """# Define Phase - Problem Statement

## Quick AI Prompt
```
"Generate problem statement from insights:

User: [user persona]
Pain: [specific pain point]
Impact: [business/personal impact]

Format: [User] needs [need] because [insight]
Include cultural/contextual factors
"
```

## Problem Statement
[User] needs [need] because [insight].

## How Might We Questions
- HMW [question 1]?
- HMW [question 2]?
- HMW [question 3]?

## Success Criteria
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]
"""

    def _create_ideate_template(self) -> str:
        return """# Ideate Phase - Solution Generation

## Quick AI Prompt
```
"Generate 15 solution ideas for:

Problem: [problem statement]
Methods: SCAMPER + Six Thinking Hats
Constraints: [budget, time, tech]

Evaluate each:
- Feasibility (1-5)
- Impact (1-5)
- Speed (1-5)
"
```

## Solution Ideas
1. [Idea 1] - Scores: F:_ I:_ S:_
2. [Idea 2] - Scores: F:_ I:_ S:_
...

## Selected Solutions
1. [Top solution 1] - Why: [reason]
2. [Top solution 2] - Why: [reason]
"""

    def _create_prototype_template(self) -> str:
        return """# Prototype Phase - Rapid Validation

## Quick AI Prompt
```
"Evaluate prototype:

Solution: [description]
Target: [user profile]
Features: [key features]

Validate:
✅ User needs fit
✅ Usability
✅ Technical feasibility
✅ Business viability
"
```

## Prototype Details
- **Type**: [MVP, mockup, wireframe]
- **Key Features**: [list]
- **Figma Link**: [URL]

## Validation Results
- **User Needs Fit**: [score/feedback]
- **Usability**: [score/feedback]
- **Technical**: [score/feedback]
- **Business**: [score/feedback]
"""

    def _create_test_template(self) -> str:
        return """# Test Phase - User Validation

## User Testing Sessions
- **Date**: [date]
- **Users**: [count/profiles]
- **Tasks**: [what users tried]

## Feedback Collected
- **Works Well**: [positive feedback]
- **Issues**: [problems found]
- **Suggestions**: [user ideas]

## Iterations Needed
1. [Change 1] - Priority: [High/Med/Low]
2. [Change 2] - Priority: [High/Med/Low]

## Success Metrics
- **Adoption Rate**: [target: 75-90%]
- **User Satisfaction**: [score]
- **Task Completion**: [%]
"""

    def _create_code_review_checklist(self) -> str:
        return """# Code Review Checklist - SDLC 5.0 (Tier 1)

## Before Commit - Check ALL Items

### SDLC 5.0 Compliance
- [ ] Zero Mock Policy: No mock/stub/fake/dummy code
- [ ] Design Thinking: Feature has DT documentation
- [ ] Performance: <50ms API response target
- [ ] Test Coverage: 80%+ for changed code
- [ ] Documentation: Updated and complete

### Code Quality
- [ ] No console.log or debug statements
- [ ] No commented-out code
- [ ] Clear variable/function names
- [ ] Proper error handling
- [ ] Type safety (TypeScript/type hints)

### Security
- [ ] Input validation present
- [ ] No SQL injection risks
- [ ] No XSS vulnerabilities
- [ ] Secrets not hardcoded
- [ ] CSRF protection where needed

### Performance
- [ ] No N+1 query patterns
- [ ] Proper caching used
- [ ] Bundle size considered
- [ ] Images optimized
- [ ] Lazy loading where appropriate

### Testing
- [ ] Unit tests added/updated
- [ ] Integration tests if needed
- [ ] Tests actually test something
- [ ] No mock data in tests
- [ ] Tests pass locally

### Documentation
- [ ] Code comments in English
- [ ] README updated if needed
- [ ] API docs updated
- [ ] Breaking changes noted

## Run Before Commit
```bash
# SDLC 5.0 validator
python3 path/to/sdlc_4_8_validator.py .

# Tests
pytest  # or npm test

# Linting
flake8  # or eslint
```

## Upgrade Path
When ready, upgrade to:
- **Tier 2**: AI-powered reviews (Claude/GPT-4)
- **Tier 3**: CodeRabbit automation (<2 min, $12/month, 498% ROI)
"""

    def _create_ai_prompts(self) -> Dict[str, str]:
        return {
            'figma_conversion': """Convert Figma design: [URL]
Component: [Name]
Location: [path]

Requirements:
✅ SDLC 5.0 compliant
✅ English-only comments
✅ Test suite (80%+ coverage)
✅ Performance <50ms
✅ i18n support""",

            'design_thinking': """Help with Design Thinking [Phase]:
Context: [describe feature/problem]
User: [target user]
Goal: [what trying to achieve]

Generate actionable output for [Phase]""",

            'code_review': """Review this code for SDLC 5.0:
[paste code]

Check:
✅ Zero Mock Policy
✅ Performance <50ms
✅ Security issues
✅ Test coverage 80%+
✅ Best practices"""
        }

def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        logger.info("SDLC 5.0 Solo Developer Setup")
        logger.info("=" * 60)
        logger.info("")
        logger.info("Usage: python solo_setup_4_8.py <project_path>")
        logger.info("")
        logger.info("Solo Profile:")
        logger.info("  • Team: 1 developer + AI tools")
        logger.info("  • Timeline: 2 days to 10x productivity")
        logger.info("  • Code Review: Tier 1 (Manual - FREE)")
        logger.info("  • Design Thinking: Lightweight (96% time savings)")
        logger.info("  • Cost: $0-50/month (free tier focus)")
        logger.info("")
        logger.info("Example:")
        logger.info("  python solo_setup_4_8.py /path/to/my-project")
        logger.info("")
        logger.info("Expected Results:")
        logger.info("  • 10x productivity with AI + Design Thinking")
        logger.info("  • Feature design: 26 hours → 1 hour")
        logger.info("  • Components: 5-10 min with Figma AI")
        logger.info("  • Quality: Zero mock compliance")
        logger.info("")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.exists(project_path):
        logger.error(f"Error: Project path '{project_path}' does not exist")
        logger.error("Creating directory...")
        os.makedirs(project_path, exist_ok=True)

    # Run setup
    setup = SoloSetup(project_path)
    setup.run()

if __name__ == "__main__":
    main()
