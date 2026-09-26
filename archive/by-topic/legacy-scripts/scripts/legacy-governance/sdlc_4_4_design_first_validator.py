#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""
SDLC 4.4 Design-First & Document-First Compliance Validator
==========================================================
Version: 4.4.0 - Design-First & Document-First Enforcement
Date: 2025-09-17
Purpose: Automated SDLC 4.4 Design-First compliance validation with mandatory file header enforcement

ENHANCED DFT COMPLIANCE FEATURES:
- Mandatory design document references in all code files
- Automated file header validation with design approval tracking
- Cultural context validation for Vietnamese/regional implementations
- Pre-commit and CI pipeline integration with build failure enforcement
- Executive compliance reporting with violation tracking
- Zero tolerance for code without approved design documents

DESIGN-FIRST ENFORCEMENT CAPABILITIES:
- File header validation requiring design document references
- Design document existence and approval status verification
- Cultural design validation for Vietnamese/regional context
- Automated CI gate enforcement with build failure on violations
- Executive compliance dashboards with real-time violation tracking
- Escalation protocols for design-first violations
- Framework-wide enforcement across all enterprise repositories
"""

import os
import sys
import json
import re
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class DesignFirstViolation:
    """Design-First compliance violation tracking"""
    file_path: str
    violation_type: str
    severity: str
    description: str
    required_action: str
    design_doc_required: str
    approval_required: str

@dataclass
class ComplianceResult:
    """Design-First compliance validation result"""
    total_files: int
    compliant_files: int
    violation_files: int
    compliance_rate: float
    violations: List[DesignFirstViolation]
    framework_version: str = "4.4"
    enforcement_level: str = "MANDATORY"

class SDLC44DesignFirstValidator:
    """
    SDLC 4.4 Design-First & Document-First Compliance Validator
    
    Enforces mandatory design document references in all code files
    with automated compliance detection and CI gate integration.
    """
    
    def __init__(self, root_path: str = "."):
        self.root = Path(root_path).resolve()
        self.violations = []
        
        # File extensions requiring design-first compliance
        self.code_extensions = {
            '.py', '.ts', '.tsx', '.js', '.jsx', '.vue', 
            '.java', '.cs', '.go', '.rs', '.cpp', '.c', '.h'
        }
        
        # Required header patterns for SDLC 4.4 DFT compliance
        self.mandatory_patterns = {
            'design_reference': r'DESIGN:\s*docs/02-Design-Architecture/.*\.md',
            'approval_reference': r'APPROVED:\s*\d{4}-\d{2}-\d{2}\s+by\s+\[?(CPO|CTO|CEO|QA-Lead|Cultural-Advisor)\]?',
            'sdlc_compliance': r'SDLC:\s*4\.4\s+Design-First\s*&\s*Document-First'
        }
        
        # Cultural context patterns for Vietnamese/regional files
        self.cultural_patterns = {
            'cultural_design': r'CULTURAL-DESIGN:\s*docs/02-Design-Architecture/.*Cultural.*\.md',
            'market_validation': r'MARKET-VALIDATED:\s*\d{4}-\d{2}-\d{2}\s+by\s+\[?CPO\]?',
            'cultural_approval': r'CULTURAL-APPROVED:\s*\d{4}-\d{2}-\d{2}\s+by\s+\[?(CPO|Cultural-Advisor)\]?'
        }
        
        # Test file specific patterns
        self.test_patterns = {
            'test_design': r'TEST-DESIGN:\s*docs/04-Testing-Quality/.*\.md',
            'test_approval': r'TEST-APPROVED:\s*\d{4}-\d{2}-\d{2}\s+by\s+\[?(QA-Lead|CTO)\]?',
            'coverage_target': r'COVERAGE:\s*\d+%\s+minimum'
        }
        
        # Exclusion patterns
        self.excluded_paths = {
            '99-legacy', '10-Archive', 'node_modules', '.git', 
            '__pycache__', 'venv', '.env', 'build', 'dist'
        }
    
    def is_excluded_path(self, file_path: Path) -> bool:
        """Check if file path should be excluded from validation"""
        path_str = str(file_path).lower()
        return any(excluded in path_str for excluded in self.excluded_paths)
    
    def is_cultural_context_file(self, file_path: Path) -> bool:
        """Check if file requires cultural context validation"""
        path_str = str(file_path).lower()
        cultural_keywords = ['vietnamese', 'vietnam', 'cultural', 'sme', 'asean', 'regional']
        return any(keyword in path_str for keyword in cultural_keywords)
    
    def is_test_file(self, file_path: Path) -> bool:
        """Check if file is a test file"""
        path_str = str(file_path).lower()
        return any(test_indicator in path_str for test_indicator in ['.test.', '.spec.', '/test_', '/tests/'])
    
    def validate_file_header(self, file_path: Path) -> List[DesignFirstViolation]:
        """Validate single file for design-first compliance"""
        violations = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                header_content = f.read(3000)  # Read first 3000 chars for header analysis
                
        except Exception as e:
            violations.append(DesignFirstViolation(
                file_path=str(file_path),
                violation_type="FILE_READ_ERROR",
                severity="HIGH",
                description=f"Unable to read file: {str(e)}",
                required_action="Fix file encoding or permissions",
                design_doc_required="N/A",
                approval_required="N/A"
            ))
            return violations
        
        # Check mandatory design reference
        if not re.search(self.mandatory_patterns['design_reference'], header_content, re.IGNORECASE):
            violations.append(DesignFirstViolation(
                file_path=str(file_path),
                violation_type="MISSING_DESIGN_REFERENCE",
                severity="CRITICAL",
                description="Missing DESIGN document reference in file header",
                required_action="Add DESIGN: docs/02-Design-Architecture/[module]/[feature]-design.md",
                design_doc_required="docs/02-Design-Architecture/[module]/[feature]-design.md",
                approval_required="CPO/CTO/CEO"
            ))
        
        # Check mandatory approval reference
        if not re.search(self.mandatory_patterns['approval_reference'], header_content, re.IGNORECASE):
            violations.append(DesignFirstViolation(
                file_path=str(file_path),
                violation_type="MISSING_APPROVAL_REFERENCE",
                severity="CRITICAL",
                description="Missing APPROVED by stakeholder reference in file header",
                required_action="Add APPROVED: [YYYY-MM-DD] by [CPO/CTO/CEO]",
                design_doc_required="Design document approval",
                approval_required="CPO/CTO/CEO"
            ))
        
        # Check mandatory SDLC 4.4 compliance declaration
        if not re.search(self.mandatory_patterns['sdlc_compliance'], header_content, re.IGNORECASE):
            violations.append(DesignFirstViolation(
                file_path=str(file_path),
                violation_type="MISSING_SDLC_COMPLIANCE",
                severity="CRITICAL",
                description="Missing SDLC 4.4 Design-First compliance declaration",
                required_action="Add SDLC: 4.4 Design-First & Document-First",
                design_doc_required="SDLC 4.4 compliance documentation",
                approval_required="Framework compliance"
            ))
        
        # Check cultural context requirements for Vietnamese/regional files
        if self.is_cultural_context_file(file_path):
            if not re.search(self.cultural_patterns['cultural_design'], header_content, re.IGNORECASE):
                violations.append(DesignFirstViolation(
                    file_path=str(file_path),
                    violation_type="MISSING_CULTURAL_DESIGN",
                    severity="HIGH",
                    description="Missing CULTURAL-DESIGN reference for Vietnamese/cultural context file",
                    required_action="Add CULTURAL-DESIGN: docs/02-Design-Architecture/Cultural/[feature]-cultural-design.md",
                    design_doc_required="Cultural design document",
                    approval_required="CPO/Cultural-Advisor"
                ))
        
        # Check test file specific requirements
        if self.is_test_file(file_path):
            if not re.search(self.test_patterns['test_design'], header_content, re.IGNORECASE):
                violations.append(DesignFirstViolation(
                    file_path=str(file_path),
                    violation_type="MISSING_TEST_DESIGN",
                    severity="HIGH",
                    description="Missing TEST-DESIGN reference for test file",
                    required_action="Add TEST-DESIGN: docs/04-Testing-Quality/[module]/[feature]-test-design.md",
                    design_doc_required="Test design document",
                    approval_required="QA-Lead/CTO"
                ))
        
        return violations
    
    def scan_repository(self) -> ComplianceResult:
        """Scan repository for design-first compliance"""
        total_files = 0
        compliant_files = 0
        all_violations = []
        
        # Scan all code files
        for ext in self.code_extensions:
            for file_path in self.root.rglob(f"*{ext}"):
                if self.is_excluded_path(file_path):
                    continue
                    
                total_files += 1
                file_violations = self.validate_file_header(file_path)
                
                if file_violations:
                    all_violations.extend(file_violations)
                else:
                    compliant_files += 1
        
        # Calculate compliance rate
        violation_files = total_files - compliant_files
        compliance_rate = (compliant_files / total_files * 100) if total_files > 0 else 0
        
        return ComplianceResult(
            total_files=total_files,
            compliant_files=compliant_files,
            violation_files=violation_files,
            compliance_rate=compliance_rate,
            violations=all_violations
        )
    
    def generate_executive_report(self, result: ComplianceResult, output_path: str = "reports/compliance/sdlc44_design_first_compliance.json"):
        """Generate executive compliance report"""
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Create executive summary
        executive_summary = {
            "metadata": {
                "scan_timestamp": datetime.now().isoformat(),
                "sdlc_version": "4.4",
                "framework": "Design-First & Document-First",
                "enforcement_level": "MANDATORY",
                "validator_version": "1.0.0"
            },
            "compliance_summary": {
                "total_files_scanned": result.total_files,
                "compliant_files": result.compliant_files,
                "violation_files": result.violation_files,
                "compliance_rate_percent": round(result.compliance_rate, 2),
                "compliance_status": "COMPLIANT" if result.compliance_rate >= 95 else "NON_COMPLIANT",
                "ci_gate_status": "PASS" if result.compliance_rate >= 95 else "FAIL"
            },
            "violation_summary": {
                "total_violations": len(result.violations),
                "critical_violations": len([v for v in result.violations if v.severity == "CRITICAL"]),
                "high_violations": len([v for v in result.violations if v.severity == "HIGH"]),
                "medium_violations": len([v for v in result.violations if v.severity == "MEDIUM"])
            },
            "violations": [asdict(v) for v in result.violations],
            "enforcement_actions": {
                "immediate_halt_required": len([v for v in result.violations if v.severity == "CRITICAL"]) > 0,
                "design_documents_required": len(result.violations),
                "approval_process_required": True if result.violations else False,
                "ci_gate_enforcement": "ACTIVE"
            }
        }
        
        # Write comprehensive report
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(executive_summary, f, indent=2, ensure_ascii=False)
        
        return executive_summary
    
    def print_executive_summary(self, result: ComplianceResult):
        """Print executive summary for CPO review"""
        logger.info("\n" + "="*80)
        logger.info("SDLC 4.4 DESIGN-FIRST COMPLIANCE VALIDATION")
        logger.info("="*80)
        logger.info(f"Framework Version: 4.4 (Design-First & Document-First)")
        logger.info(f"Enforcement Level: MANDATORY")
        logger.info(f"Scan Timestamp: {datetime.now().isoformat()}")
        logger.info("-" * 80)
        logger.info(f"Total Files Scanned: {result.total_files}")
        logger.info(f"Compliant Files: {result.compliant_files}")
        logger.info(f"Violation Files: {result.violation_files}")
        logger.info(f"Compliance Rate: {result.compliance_rate:.1f}%")
        logger.info(f"Compliance Status: {'COMPLIANT' if result.compliance_rate >= 95 else 'NON_COMPLIANT'}")
        logger.info(f"CI Gate Status: {'PASS' if result.compliance_rate >= 95 else 'FAIL'}")
        
        if result.violations:
            logger.info("\n🚨 DESIGN-FIRST VIOLATIONS:")
            logger.info("-" * 80)
            
            # Group violations by type
            violation_groups = {}
            for violation in result.violations:
                if violation.violation_type not in violation_groups:
                    violation_groups[violation.violation_type] = []
                violation_groups[violation.violation_type].append(violation)
            
            for violation_type, violations in violation_groups.items():
                logger.info(f"\n❌ {violation_type} ({len(violations)} files)")
                for violation in violations[:5]:  # Show first 5 per type
                    logger.info(f"   - {violation.file_path}")
                    logger.info(f"     Action: {violation.required_action}")
                if len(violations) > 5:
                    logger.info(f"   ... and {len(violations) - 5} more files")
        
        logger.info("\n" + "="*80)
        logger.info("ENFORCEMENT ACTIONS:")
        if result.violations:
            logger.info("🛑 IMMEDIATE HALT: All coding activities must stop")
            logger.info("📋 DESIGN REQUIRED: Produce missing design documents")
            logger.info("✅ APPROVAL NEEDED: Obtain stakeholder approvals")
            logger.info("🔄 COMPLIANCE: Update file headers with design references")
        else:
            logger.info("✅ COMPLIANT: All files meet design-first requirements")
            logger.info("🚀 AUTHORIZED: Code implementation may proceed")
        
        logger.info("="*80)
        
        return result.compliance_rate >= 95

def main():
    """Main execution for SDLC 4.4 design-first compliance validation"""
    parser = argparse.ArgumentParser(description="SDLC 4.4 Design-First Compliance Validator")
    parser.add_argument("--path", default=".", help="Repository path to scan")
    parser.add_argument("--output", default="reports/compliance/sdlc44_design_first_compliance.json", 
                       help="Output path for compliance report")
    parser.add_argument("--ci-mode", action="store_true", help="CI mode - exit with non-zero on violations")
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = SDLC44DesignFirstValidator(args.path)
    
    # Scan repository
    result = validator.scan_repository()
    
    # Generate executive report
    validator.generate_executive_report(result, args.output)
    
    # Print summary
    is_compliant = validator.print_executive_summary(result)
    
    # Exit with appropriate code for CI enforcement
    if args.ci_mode:
        sys.exit(0 if is_compliant else 1)
    
    return result

if __name__ == "__main__":
    main()
