#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""
SDLC 4.6 Universal Framework Validator
=====================================
Version: 4.5.0 - Enhanced Oversight + Zero Facade Tolerance
Date: 2025-09-21
Purpose: Universal SDLC validation for all project scales with facade detection

UNIVERSAL FRAMEWORK FEATURES:
- Scalable validation for solo developers to enterprise teams
- Multi-layer oversight integration and reporting
- Universal AI+Human collaboration validation
- Framework version compatibility checking
- Business value and authenticity verification

ENHANCED OVERSIGHT CAPABILITIES:
- Automated facade pattern detection (AST + regex)
- Implementation authenticity verification
- Database-backed functionality validation
- Multi-layer oversight compliance checking
- Executive reporting with business impact assessment
- Revenue protection through quality enforcement
"""

import os
import sys
import json
import re
import ast
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum

class ProjectScale(Enum):
    """Project scale classification"""
    SOLO = "solo"           # 1 developer
    SMALL = "small"         # 2-5 developers
    MEDIUM = "medium"       # 6-15 developers
    ENTERPRISE = "enterprise"  # 16+ developers

class ViolationSeverity(Enum):
    """Violation severity levels"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    BLOCKING = "blocking"

@dataclass
class FacadeViolation:
    """Facade detection violation"""
    file_path: str
    line_number: int
    pattern_type: str
    matched_pattern: str
    severity: ViolationSeverity
    description: str
    authenticity_score: float
    required_action: str

@dataclass
class OversightViolation:
    """Multi-layer oversight violation"""
    component: str
    layer: str  # automated, cto, cpo, ceo
    violation_type: str
    severity: ViolationSeverity
    description: str
    business_impact: str
    required_action: str

@dataclass
class UniversalValidationResult:
    """Universal framework validation result"""
    project_scale: ProjectScale
    framework_version: str
    validation_timestamp: datetime
    total_files_scanned: int
    facade_violations: List[FacadeViolation]
    oversight_violations: List[OversightViolation]
    authenticity_score: float
    compliance_percentage: float
    business_risk_level: str
    recommended_actions: List[str]
    multi_layer_status: Dict[str, str]

class UniversalSDLCValidator:
    """Universal SDLC Framework Validator"""
    
    def __init__(self, project_path: str, project_scale: ProjectScale = None):
        self.project_path = Path(project_path)
        self.project_scale = project_scale or self._detect_project_scale()
        self.facade_violations = []
        self.oversight_violations = []
        
        # Zero Facade Tolerance patterns
        self.facade_patterns = {
                r'\bfake\b|\bFake\b|\bFAKE\b',
                r'\bdummy\b|\bDummy\b|\bDUMMY\b',
                r'\bplaceholder\b|\bPlaceholder\b',
                r'\bsample\b|\bSample\b.*data',
                r'\btest\b.*\bdata\b.*hardcoded',
            ],
            'implementation_patterns': [
                r'TODO.*replace.*with.*real',
                r'FIXME.*implement.*actual',
                r'return\s+\{.*hardcoded.*\}',
                r'static.*response.*=.*\{',
                r'const.*MOCK.*=',
            ],
            'database_patterns': [
                r'sqlite.*memory.*:',
                r'fake.*connection',
                r'in_memory.*db',
            ]
        }
        
        # Business logic authenticity patterns
        self.authenticity_patterns = {
            'database_required': [
                r'class.*Model.*:',
                r'def.*save.*\(',
                r'def.*create.*\(',
                r'SELECT.*FROM',
                r'INSERT.*INTO',
            ],
            'api_integration': [
                r'requests\.',
                r'httpx\.',
                r'urllib\.',
                r'@api_route',
                r'@app\.route',
            ],
            'business_logic': [
                r'def.*calculate.*\(',
                r'def.*process.*\(',
                r'def.*validate.*\(',
                r'class.*Service.*:',
                r'class.*Manager.*:',
            ]
        }

    def _detect_project_scale(self) -> ProjectScale:
        """Auto-detect project scale based on codebase characteristics"""
        py_files = list(self.project_path.rglob("*.py"))
        js_files = list(self.project_path.rglob("*.js")) + list(self.project_path.rglob("*.ts"))
        total_files = len(py_files) + len(js_files)
        
        # Check for team indicators
        has_roles = any([
            (self.project_path / "docs").exists(),
            (self.project_path / "tests").exists(),
            (self.project_path / ".github").exists(),
        ])
        
        # Scale detection logic
        if total_files < 10:
            return ProjectScale.SOLO
        elif total_files < 50 and not has_roles:
            return ProjectScale.SMALL
        elif total_files < 200 or not has_roles:
            return ProjectScale.MEDIUM
        else:
            return ProjectScale.ENTERPRISE

    def scan_for_facades(self) -> List[FacadeViolation]:
        """Scan codebase for facade patterns"""
        violations = []
        
        for file_path in self.project_path.rglob("*.py"):
            violations.extend(self._scan_python_file(file_path))
        
        for file_path in self.project_path.rglob("*.js"):
            violations.extend(self._scan_javascript_file(file_path))
            
        for file_path in self.project_path.rglob("*.ts"):
            violations.extend(self._scan_typescript_file(file_path))
            
        return violations

    def _scan_python_file(self, file_path: Path) -> List[FacadeViolation]:
        """Scan Python file for facade patterns"""
        violations = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # AST analysis for semantic patterns
            try:
                tree = ast.parse(content)
                violations.extend(self._analyze_ast(file_path, tree))
            except SyntaxError:
                pass  # Skip files with syntax errors
            
            # Regex pattern matching
            for line_num, line in enumerate(lines, 1):
                violations.extend(self._check_line_patterns(file_path, line_num, line))
                
        except Exception as e:
            logger.info(f"Error scanning {file_path}: {e}")
            
        return violations

    def _analyze_ast(self, file_path: Path, tree: ast.AST) -> List[FacadeViolation]:
        """Analyze AST for semantic facade patterns"""
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                    violations.append(FacadeViolation(
                        file_path=str(file_path),
                        line_number=node.lineno,
                        matched_pattern=node.name,
                        severity=ViolationSeverity.CRITICAL,
                        authenticity_score=0.0,
                        required_action="Replace with authentic implementation"
                    ))
            
            if isinstance(node, ast.FunctionDef):
                    violations.append(FacadeViolation(
                        file_path=str(file_path),
                        line_number=node.lineno,
                        matched_pattern=node.name,
                        severity=ViolationSeverity.ERROR,
                        authenticity_score=0.2,
                        required_action="Implement authentic business logic"
                    ))
                    
            # Check for hardcoded return values
            if isinstance(node, ast.Return) and isinstance(node.value, (ast.Dict, ast.List)):
                if hasattr(node.value, 'keys') or hasattr(node.value, 'elts'):
                    violations.append(FacadeViolation(
                        file_path=str(file_path),
                        line_number=node.lineno,
                        pattern_type="hardcoded_return",
                        matched_pattern="hardcoded data structure",
                        severity=ViolationSeverity.WARNING,
                        description="Potentially hardcoded return value",
                        authenticity_score=0.5,
                        required_action="Verify data source authenticity"
                    ))
                    
        return violations

    def _check_line_patterns(self, file_path: Path, line_num: int, line: str) -> List[FacadeViolation]:
        """Check line against facade patterns"""
        violations = []
        
        for pattern_category, patterns in self.facade_patterns.items():
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    severity = self._determine_severity(pattern_category, pattern)
                    violations.append(FacadeViolation(
                        file_path=str(file_path),
                        line_number=line_num,
                        pattern_type=pattern_category,
                        matched_pattern=pattern,
                        severity=severity,
                        description=f"Facade pattern detected: {line.strip()}",
                        authenticity_score=self._calculate_authenticity_score(pattern_category),
                        required_action=self._get_required_action(pattern_category)
                    ))
                    
        return violations

    def _scan_javascript_file(self, file_path: Path) -> List[FacadeViolation]:
        """Scan JavaScript file for facade patterns"""
        violations = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                # JavaScript-specific facade patterns
                js_patterns = [
                    r'sinon\.stub',
                    r'return.*\{.*hardcoded.*\}',
                ]
                
                for pattern in js_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(FacadeViolation(
                            file_path=str(file_path),
                            line_number=line_num,
                            matched_pattern=pattern,
                            severity=ViolationSeverity.ERROR,
                            description=f"JavaScript facade pattern: {line.strip()}",
                            authenticity_score=0.3,
                            required_action="Replace with authentic implementation"
                        ))
                        
        except Exception as e:
            logger.info(f"Error scanning JavaScript file {file_path}: {e}")
            
        return violations

    def _scan_typescript_file(self, file_path: Path) -> List[FacadeViolation]:
        """Scan TypeScript file for facade patterns"""
        # Similar to JavaScript scanning with TypeScript-specific patterns
        return self._scan_javascript_file(file_path)

    def validate_multi_layer_oversight(self) -> List[OversightViolation]:
        """Validate multi-layer oversight compliance"""
        violations = []
        
        # Only apply to medium and enterprise projects
        if self.project_scale in [ProjectScale.MEDIUM, ProjectScale.ENTERPRISE]:
            violations.extend(self._check_automated_layer())
            violations.extend(self._check_technical_layer())
            violations.extend(self._check_business_layer())
            
            if self.project_scale == ProjectScale.ENTERPRISE:
                violations.extend(self._check_executive_layer())
                
        return violations

    def _check_automated_layer(self) -> List[OversightViolation]:
        """Check automated oversight layer"""
        violations = []
        
        # Check for CI/CD integration
        ci_files = [
            ".github/workflows",
            ".gitlab-ci.yml",
            "Jenkinsfile",
            ".travis.yml"
        ]
        
        has_ci = any((self.project_path / ci_file).exists() for ci_file in ci_files)
        
        if not has_ci:
            violations.append(OversightViolation(
                component="ci_cd",
                layer="automated",
                violation_type="missing_automation",
                severity=ViolationSeverity.ERROR,
                description="No CI/CD automation detected",
                business_impact="Quality gate failures not prevented",
                required_action="Implement automated CI/CD pipeline"
            ))
            
        # Check for pre-commit hooks
        if not (self.project_path / ".pre-commit-config.yaml").exists():
            violations.append(OversightViolation(
                component="pre_commit",
                layer="automated",
                violation_type="missing_hooks",
                severity=ViolationSeverity.WARNING,
                description="No pre-commit hooks configured",
                business_impact="Facade code may reach repository",
                required_action="Configure pre-commit facade detection"
            ))
            
        return violations

    def _check_technical_layer(self) -> List[OversightViolation]:
        """Check technical oversight layer (CTO level)"""
        violations = []
        
        # Check for code review requirements
        if (self.project_path / ".github").exists():
            branch_protection = self.project_path / ".github" / "branch_protection.json"
            if not branch_protection.exists():
                violations.append(OversightViolation(
                    component="code_review",
                    layer="technical",
                    violation_type="missing_protection",
                    severity=ViolationSeverity.ERROR,
                    description="No branch protection rules configured",
                    business_impact="Code may bypass technical review",
                    required_action="Configure mandatory code review"
                ))
                
        return violations

    def _check_business_layer(self) -> List[OversightViolation]:
        """Check business oversight layer (CPO level)"""
        violations = []
        
        # Check for design documentation requirements
        docs_dir = self.project_path / "docs"
        if not docs_dir.exists():
            violations.append(OversightViolation(
                component="documentation",
                layer="business",
                violation_type="missing_docs",
                severity=ViolationSeverity.WARNING,
                description="No documentation directory found",
                business_impact="Business requirements may not be documented",
                required_action="Create design documentation structure"
            ))
            
        return violations

    def _check_executive_layer(self) -> List[OversightViolation]:
        """Check executive oversight layer (CEO level)"""
        violations = []
        
        # Check for governance documentation
        governance_files = [
            "GOVERNANCE.md",
            "COMPLIANCE.md",
            "RISK-MANAGEMENT.md"
        ]
        
        missing_governance = [f for f in governance_files if not (self.project_path / f).exists()]
        
        if missing_governance:
            violations.append(OversightViolation(
                component="governance",
                layer="executive",
                violation_type="missing_governance",
                severity=ViolationSeverity.CRITICAL,
                description=f"Missing governance files: {missing_governance}",
                business_impact="Executive oversight capabilities limited",
                required_action="Create enterprise governance documentation"
            ))
            
        return violations

    def _determine_severity(self, pattern_category: str, pattern: str) -> ViolationSeverity:
        """Determine violation severity based on pattern"""
            return ViolationSeverity.CRITICAL
        elif 'dummy' in pattern.lower() or 'placeholder' in pattern.lower():
            return ViolationSeverity.ERROR
        elif 'todo' in pattern.lower() or 'fixme' in pattern.lower():
            return ViolationSeverity.WARNING
        else:
            return ViolationSeverity.INFO

    def _calculate_authenticity_score(self, pattern_category: str) -> float:
        """Calculate authenticity score based on pattern category"""
        scores = {
            'implementation_patterns': 0.3,
            'database_patterns': 0.1,
        }
        return scores.get(pattern_category, 0.5)

    def _get_required_action(self, pattern_category: str) -> str:
        """Get required action based on pattern category"""
        actions = {
            'implementation_patterns': "Complete implementation with real business logic",
            'database_patterns': "Configure real database connection",
        }
        return actions.get(pattern_category, "Review and verify authenticity")

    def calculate_compliance_metrics(self) -> Tuple[float, float, str]:
        """Calculate compliance metrics"""
        total_files = len(list(self.project_path.rglob("*.py"))) + \
                     len(list(self.project_path.rglob("*.js"))) + \
                     len(list(self.project_path.rglob("*.ts")))
        
        if total_files == 0:
            return 100.0, 1.0, "low"
        
        # Calculate authenticity score
        if self.facade_violations:
            avg_authenticity = sum(v.authenticity_score for v in self.facade_violations) / len(self.facade_violations)
        else:
            avg_authenticity = 1.0
            
        # Calculate compliance percentage
        critical_violations = len([v for v in self.facade_violations if v.severity == ViolationSeverity.CRITICAL])
        compliance_percentage = max(0, 100 - (critical_violations / total_files * 100))
        
        # Determine business risk
        if critical_violations > total_files * 0.1:  # More than 10% critical violations
            risk_level = "high"
        elif critical_violations > 0:
            risk_level = "medium"
        else:
            risk_level = "low"
            
        return compliance_percentage, avg_authenticity, risk_level

    def generate_recommendations(self) -> List[str]:
        """Generate recommended actions based on violations"""
        recommendations = []
        
        if self.facade_violations:
            critical_count = len([v for v in self.facade_violations if v.severity == ViolationSeverity.CRITICAL])
            if critical_count > 0:
                recommendations.append(f"URGENT: Address {critical_count} critical facade violations immediately")
                
                
        if self.oversight_violations:
            automated_violations = [v for v in self.oversight_violations if v.layer == "automated"]
            if automated_violations:
                recommendations.append("Implement automated CI/CD pipeline with facade detection")
                
        # Scale-specific recommendations
        if self.project_scale == ProjectScale.SOLO:
            recommendations.append("Consider upgrading to SDLC 3.x when adding team members")
        elif self.project_scale == ProjectScale.SMALL:
            recommendations.append("Implement peer review processes for quality assurance")
        elif self.project_scale == ProjectScale.MEDIUM:
            recommendations.append("Consider role-based development with specialized AI assistants")
        elif self.project_scale == ProjectScale.ENTERPRISE:
            recommendations.append("Ensure multi-layer oversight compliance for risk management")
            
        return recommendations

    def validate(self) -> UniversalValidationResult:
        """Perform universal SDLC validation"""
        logger.info(f"Validating {self.project_scale.value} scale project at {self.project_path}")
        
        # Scan for facade violations
        self.facade_violations = self.scan_for_facades()
        
        # Validate oversight compliance
        self.oversight_violations = self.validate_multi_layer_oversight()
        
        # Calculate metrics
        compliance_percentage, authenticity_score, business_risk_level = self.calculate_compliance_metrics()
        
        # Generate recommendations
        recommendations = self.generate_recommendations()
        
        # Multi-layer status
        multi_layer_status = {
            "automated": "compliant" if not [v for v in self.oversight_violations if v.layer == "automated"] else "non_compliant",
            "technical": "compliant" if not [v for v in self.oversight_violations if v.layer == "technical"] else "non_compliant",
            "business": "compliant" if not [v for v in self.oversight_violations if v.layer == "business"] else "non_compliant",
            "executive": "compliant" if not [v for v in self.oversight_violations if v.layer == "executive"] else "non_compliant",
        }
        
        return UniversalValidationResult(
            project_scale=self.project_scale,
            framework_version="4.5.0",
            validation_timestamp=datetime.now(),
            total_files_scanned=len(list(self.project_path.rglob("*.py"))) + 
                              len(list(self.project_path.rglob("*.js"))) + 
                              len(list(self.project_path.rglob("*.ts"))),
            facade_violations=self.facade_violations,
            oversight_violations=self.oversight_violations,
            authenticity_score=authenticity_score,
            compliance_percentage=compliance_percentage,
            business_risk_level=business_risk_level,
            recommended_actions=recommendations,
            multi_layer_status=multi_layer_status
        )

def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        logger.info("Usage: python sdlc_4_5_universal_validator.py <project_path> [project_scale]")
        logger.info("Project scales: solo, small, medium, enterprise")
        sys.exit(1)
        
    project_path = sys.argv[1]
    project_scale = None
    
    if len(sys.argv) > 2:
        scale_mapping = {
            'solo': ProjectScale.SOLO,
            'small': ProjectScale.SMALL,
            'medium': ProjectScale.MEDIUM,
            'enterprise': ProjectScale.ENTERPRISE
        }
        project_scale = scale_mapping.get(sys.argv[2].lower())
        
    # Create validator and run validation
    validator = UniversalSDLCValidator(project_path, project_scale)
    result = validator.validate()
    
    # Output results
    logger.info(f"\n{'='*60}")
    logger.info(f"SDLC 4.6 Universal Framework Validation Report")
    logger.info(f"{'='*60}")
    logger.info(f"Project Scale: {result.project_scale.value.title()}")
    logger.info(f"Framework Version: {result.framework_version}")
    logger.info(f"Validation Time: {result.validation_timestamp}")
    logger.info(f"Files Scanned: {result.total_files_scanned}")
    logger.info(f"Compliance: {result.compliance_percentage:.1f}%")
    logger.info(f"Authenticity Score: {result.authenticity_score:.2f}")
    logger.info(f"Business Risk: {result.business_risk_level.upper()}")
    
    # Facade violations summary
    if result.facade_violations:
        logger.info(f"\n🚫 FACADE VIOLATIONS ({len(result.facade_violations)}):")
        for violation in result.facade_violations[:10]:  # Show first 10
            logger.info(f"  - {violation.file_path}:{violation.line_number} [{violation.severity.value}] {violation.description}")
        if len(result.facade_violations) > 10:
            logger.info(f"  ... and {len(result.facade_violations) - 10} more violations")
    else:
        logger.info(f"\n✅ NO FACADE VIOLATIONS DETECTED")
        
    # Oversight violations summary
    if result.oversight_violations:
        logger.info(f"\n👁️ OVERSIGHT VIOLATIONS ({len(result.oversight_violations)}):")
        for violation in result.oversight_violations:
            logger.info(f"  - {violation.layer.title()} Layer: {violation.description}")
    else:
        logger.info(f"\n✅ OVERSIGHT COMPLIANCE VERIFIED")
        
    # Multi-layer status
    logger.info(f"\n📊 MULTI-LAYER OVERSIGHT STATUS:")
    for layer, status in result.multi_layer_status.items():
        status_icon = "✅" if status == "compliant" else "❌"
        logger.info(f"  {status_icon} {layer.title()} Layer: {status}")
        
    # Recommendations
    if result.recommended_actions:
        logger.info(f"\n💡 RECOMMENDATIONS:")
        for i, recommendation in enumerate(result.recommended_actions, 1):
            logger.info(f"  {i}. {recommendation}")
            
    # Exit code based on compliance
    if result.business_risk_level == "high" or result.compliance_percentage < 80:
        logger.info(f"\n❌ VALIDATION FAILED - Critical issues detected")
        sys.exit(1)
    elif result.business_risk_level == "medium" or result.compliance_percentage < 95:
        logger.info(f"\n⚠️  VALIDATION WARNING - Issues require attention")
        sys.exit(2)
    else:
        logger.info(f"\n✅ VALIDATION PASSED - Framework compliance verified")
        sys.exit(0)

if __name__ == "__main__":
    main()
