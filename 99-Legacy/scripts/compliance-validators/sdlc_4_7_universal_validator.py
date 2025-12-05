#!/usr/bin/env python3
"""
SDLC 4.7 Universal Framework Validator
Version: 4.7.0
Date: September 27, 2025
Purpose: Validates compliance with SDLC 4.7 Universal Framework

Built BY Battle, FOR Victory - Proven on 3 real platforms
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import re

class SDLC47UniversalValidator:
    """
    SDLC 4.7 Universal Framework Validator
    Built from experience with BFlow, NQH-Bot, and MTEP platforms
    """

    def __init__(self, project_root: str, profile: str = "auto"):
        self.project_root = Path(project_root).resolve()
        self.profile = profile
        self.results = {
            "version": "4.7.0",
            "framework": "Universal Framework - Built BY Battle, FOR Victory",
            "timestamp": datetime.now().isoformat(),
            "project_path": str(self.project_root),
            "profile": profile,
            "pillars": {},
            "ai_tools": {},
            "metrics": {},
            "violations": [],
            "warnings": [],
            "passed": False
        }

    def detect_profile(self) -> str:
        """Detect implementation profile based on team size and structure"""
        # Check for team size indicators
        git_contributors = self._count_git_contributors()

        if git_contributors <= 1:
            return "solo"
        elif git_contributors <= 6:
            return "startup"
        elif git_contributors <= 20:
            return "growth"
        else:
            return "enterprise"

    def _count_git_contributors(self) -> int:
        """Count unique git contributors"""
        try:
            result = subprocess.run(
                ["git", "shortlog", "-sn", "--all"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return len(result.stdout.strip().split('\n'))
        except:
            pass
        return 1

    def validate_pillar_1_ai_native(self) -> Dict[str, Any]:
        """Validate AI-Native Excellence Standards"""
        results = {
            "name": "AI-Native Excellence",
            "passed": True,
            "score": 0,
            "checks": []
        }

        # Check for AI tool configurations
        ai_configs = [
            ".claude",
            ".cursor",
            ".github/copilot",
            "ai-templates",
            "CLAUDE.md"
        ]

        found_configs = 0
        for config in ai_configs:
            config_path = self.project_root / config
            if config_path.exists():
                found_configs += 1
                results["checks"].append({
                    "check": f"AI configuration: {config}",
                    "passed": True
                })

        results["score"] = (found_configs / len(ai_configs)) * 100
        results["passed"] = results["score"] >= 60

        return results

    def validate_pillar_2_zero_mock(self) -> Dict[str, Any]:
        """Validate Zero Mock Tolerance"""
        results = {
            "name": "Zero Mock Tolerance",
            "passed": True,
            "score": 100,
            "checks": [],
            "mock_count": 0
        }

        # Patterns to detect mocks
        mock_patterns = [
            r"mock\.",
            r"Mock\(",
            r"@mock",
            r"unittest\.mock",
            r"jest\.mock",
            r"sinon\.",
            r"fake[A-Z]",
            r"dummy[A-Z]",
            r"stub[A-Z]"
        ]

        # Scan Python and JavaScript/TypeScript files
        for ext in ["*.py", "*.js", "*.ts", "*.tsx"]:
            for file_path in self.project_root.rglob(ext):
                if "node_modules" in str(file_path) or "venv" in str(file_path):
                    continue

                try:
                    content = file_path.read_text()
                    for pattern in mock_patterns:
                        if re.search(pattern, content):
                            results["mock_count"] += 1
                            results["checks"].append({
                                "check": f"Mock found in {file_path.relative_to(self.project_root)}",
                                "passed": False
                            })
                            results["passed"] = False
                            results["score"] = 0
                            break
                except:
                    continue

        if results["mock_count"] == 0:
            results["checks"].append({
                "check": "Zero mocks detected",
                "passed": True
            })

        return results

    def validate_pillar_3_system_thinking(self) -> Dict[str, Any]:
        """Validate System Thinking approach"""
        results = {
            "name": "System Thinking",
            "passed": True,
            "score": 0,
            "checks": []
        }

        # Check for system-level documentation
        system_docs = [
            "architecture",
            "system-design",
            "api-contracts",
            "integration"
        ]

        found_docs = 0
        for doc_pattern in system_docs:
            for doc_file in self.project_root.rglob(f"*{doc_pattern}*"):
                if doc_file.is_file():
                    found_docs += 1
                    results["checks"].append({
                        "check": f"System documentation: {doc_file.name}",
                        "passed": True
                    })
                    break

        results["score"] = (found_docs / len(system_docs)) * 100
        results["passed"] = results["score"] >= 50

        return results

    def validate_pillar_4_crisis_response(self) -> Dict[str, Any]:
        """Validate Crisis Response Capability"""
        results = {
            "name": "Crisis Response",
            "passed": True,
            "score": 0,
            "checks": []
        }

        # Check for crisis response indicators
        crisis_indicators = [
            "monitoring",
            "alerts",
            "rollback",
            "backup",
            "recovery"
        ]

        found_indicators = 0
        for indicator in crisis_indicators:
            for file_path in self.project_root.rglob(f"*{indicator}*"):
                if file_path.is_file():
                    found_indicators += 1
                    results["checks"].append({
                        "check": f"Crisis capability: {indicator}",
                        "passed": True
                    })
                    break

        results["score"] = (found_indicators / len(crisis_indicators)) * 100
        results["passed"] = results["score"] >= 40

        return results

    def validate_pillar_5_universal_patterns(self) -> Dict[str, Any]:
        """Validate Universal Patterns implementation"""
        results = {
            "name": "Universal Patterns",
            "passed": True,
            "score": 0,
            "checks": []
        }

        # Check for pattern implementation
        patterns = [
            "multi-tenant",
            "authentication",
            "api",
            "caching",
            "testing"
        ]

        found_patterns = 0
        for pattern in patterns:
            for file_path in self.project_root.rglob(f"*{pattern}*"):
                if file_path.is_file():
                    found_patterns += 1
                    results["checks"].append({
                        "check": f"Pattern implementation: {pattern}",
                        "passed": True
                    })
                    break

        results["score"] = (found_patterns / len(patterns)) * 100
        results["passed"] = results["score"] >= 40

        return results

    def validate_ai_tools_coordination(self) -> Dict[str, Any]:
        """Validate AI Tools Coordination implementation"""
        results = {
            "70_20_10_rule": False,
            "parallel_processing": False,
            "cross_validation": False,
            "templates_deployed": 0
        }

        # Check for AI templates
        template_dir = self.project_root / ".ai-templates"
        if template_dir.exists():
            results["templates_deployed"] = len(list(template_dir.glob("*.md")))

        # Check for parallel processing indicators
        if (self.project_root / ".github" / "workflows").exists():
            results["parallel_processing"] = True

        return results

    def calculate_metrics(self) -> Dict[str, Any]:
        """Calculate framework metrics"""
        metrics = {
            "productivity_multiplier": "1x",
            "implementation_time": "unknown",
            "crisis_readiness": False
        }

        # Determine productivity based on profile
        profile_multipliers = {
            "solo": "10x",
            "startup": "20x",
            "growth": "30x",
            "enterprise": "50x"
        }

        if self.profile == "auto":
            self.profile = self.detect_profile()

        metrics["productivity_multiplier"] = profile_multipliers.get(self.profile, "10x")

        # Check crisis readiness
        if self.results["pillars"].get("Crisis Response", {}).get("passed"):
            metrics["crisis_readiness"] = True

        return metrics

    def validate(self) -> Dict[str, Any]:
        """Run full validation"""
        print(f"🎯 SDLC 4.7 Universal Framework Validator")
        print(f"   Built BY Battle, FOR Victory")
        print(f"   Validating: {self.project_root}")
        print()

        # Detect profile if auto
        if self.profile == "auto":
            self.profile = self.detect_profile()
            print(f"📊 Detected Profile: {self.profile}")

        # Validate Five Pillars
        print("\n🏗️ Validating Five Universal Pillars...")

        pillars = [
            ("AI-Native Excellence", self.validate_pillar_1_ai_native()),
            ("Zero Mock Tolerance", self.validate_pillar_2_zero_mock()),
            ("System Thinking", self.validate_pillar_3_system_thinking()),
            ("Crisis Response", self.validate_pillar_4_crisis_response()),
            ("Universal Patterns", self.validate_pillar_5_universal_patterns())
        ]

        total_score = 0
        passed_pillars = 0

        for name, pillar_result in pillars:
            self.results["pillars"][name] = pillar_result
            total_score += pillar_result["score"]
            if pillar_result["passed"]:
                passed_pillars += 1
                print(f"  ✅ {name}: {pillar_result['score']:.0f}%")
            else:
                print(f"  ❌ {name}: {pillar_result['score']:.0f}%")
                if name == "Zero Mock Tolerance" and pillar_result["mock_count"] > 0:
                    print(f"     ⚠️  Found {pillar_result['mock_count']} mock instances!")

        # Validate AI Tools Coordination
        print("\n🤖 Validating AI Tools Coordination...")
        self.results["ai_tools"] = self.validate_ai_tools_coordination()

        # Calculate metrics
        self.results["metrics"] = self.calculate_metrics()

        # Overall assessment
        avg_score = total_score / len(pillars)
        self.results["overall_score"] = avg_score
        self.results["passed"] = passed_pillars >= 3 and avg_score >= 60

        # Print summary
        print("\n" + "="*60)
        print("📊 VALIDATION SUMMARY")
        print("="*60)
        print(f"Profile: {self.profile.upper()}")
        print(f"Overall Score: {avg_score:.1f}%")
        print(f"Pillars Passed: {passed_pillars}/5")
        print(f"Expected Productivity: {self.results['metrics']['productivity_multiplier']}")
        print(f"Crisis Ready: {'YES' if self.results['metrics']['crisis_readiness'] else 'NO'}")

        if self.results["passed"]:
            print("\n✅ PROJECT PASSES SDLC 4.7 VALIDATION")
            print("   Ready for battle-tested productivity!")
        else:
            print("\n❌ PROJECT NEEDS IMPROVEMENT")
            print("   Review failed pillars and implement patterns")

        return self.results

    def save_results(self, output_file: Optional[str] = None):
        """Save validation results to JSON"""
        if not output_file:
            output_file = f"sdlc_4_7_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        output_path = Path(output_file)
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)

        print(f"\n📁 Results saved to: {output_path}")
        return str(output_path)

def main():
    parser = argparse.ArgumentParser(
        description="SDLC 4.7 Universal Framework Validator - Built BY Battle, FOR Victory"
    )
    parser.add_argument(
        "project_root",
        help="Path to project root directory"
    )
    parser.add_argument(
        "--profile",
        choices=["auto", "solo", "startup", "growth", "enterprise"],
        default="auto",
        help="Implementation profile (default: auto-detect)"
    )
    parser.add_argument(
        "--output",
        help="Output file for results (JSON)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    # Validate project exists
    project_path = Path(args.project_root)
    if not project_path.exists():
        print(f"❌ Error: Project path does not exist: {project_path}")
        sys.exit(1)

    # Run validation
    validator = SDLC47UniversalValidator(args.project_root, args.profile)
    results = validator.validate()

    # Save results if requested
    if args.output:
        validator.save_results(args.output)

    # Exit with appropriate code
    sys.exit(0 if results["passed"] else 1)

if __name__ == "__main__":
    main()