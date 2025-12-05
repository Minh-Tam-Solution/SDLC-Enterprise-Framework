#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""
=========================================================================
Version: 4.6.0 - Emergency Enhanced Scanner
Date: September 24, 2025
Purpose: Lightweight wrapper around SDLC 4.6 TSI Validator for backward compatibility

EMERGENCY ENHANCED FEATURES:
- Universal project scale support (solo to enterprise)
- Testing Standards Integration validation
- Implementation authenticity verification
- Vietnamese Cultural Testing validation
- Backward compatibility with existing workflows

USAGE:
This script provides backward compatibility for existing workflows that use sdlc_scanner.py
while leveraging the new SDLC 4.6 TSI Validator for actual validation logic.

For new implementations, use sdlc_4_6_tsi_validator.py directly.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

def run_universal_validator(project_path: str, project_scale: Optional[str] = None) -> Dict[str, Any]:
    """
    Run SDLC 4.6 Universal Validator and return results in legacy format
    """
    script_dir = Path(__file__).parent
    validator_script = script_dir / "sdlc_4_5_universal_validator.py"
    
    # Build command
    cmd = [sys.executable, str(validator_script), project_path]
    if project_scale:
        cmd.append(project_scale)
    
    try:
        # Run validator and capture output
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            cwd=project_path
        )
        
        # Parse output for backward compatibility
        output_lines = result.stdout.split('\n')
        
        # Extract key metrics from output
        compliance_percentage = 0.0
        authenticity_score = 0.0
        business_risk = "unknown"
        facade_violations = 0
        project_scale_detected = "unknown"
        
        for line in output_lines:
            if "Compliance:" in line:
                try:
                    compliance_percentage = float(line.split(':')[1].strip().rstrip('%'))
                except:
                    pass
            elif "Authenticity Score:" in line:
                try:
                    authenticity_score = float(line.split(':')[1].strip())
                except:
                    pass
            elif "Business Risk:" in line:
                business_risk = line.split(':')[1].strip().lower()
            elif "FACADE VIOLATIONS" in line:
                try:
                    facade_violations = int(line.split('(')[1].split(')')[0])
                except:
                    pass
            elif "Project Scale:" in line:
                project_scale_detected = line.split(':')[1].strip().lower()
        
        # Return legacy-compatible format
        return {
            "scan_result": {
                "project_path": project_path,
                "scan_timestamp": datetime.now().isoformat(),
                "sdlc_version": "4.5.0",
                "framework_scale": project_scale_detected,
                "facade_violations_count": facade_violations,
                "authenticity_score": authenticity_score,
                "business_risk_level": business_risk,
                "compliance_percentage": compliance_percentage,
                "exit_code": result.returncode
            },
            "raw_output": result.stdout,
            "raw_error": result.stderr
        }
        
    except Exception as e:
        return {
            "error": f"Failed to run SDLC 4.6 Universal Validator: {str(e)}",
            "scan_result": None
        }

def main():
    """Main execution function with backward compatibility"""
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        logger.info("SDLC 4.6 Universal Scanner")
        logger.info("==========================")
        logger.info()
        logger.info("Usage: python sdlc_scanner.py <project_path> [project_scale]")
        logger.info()
        logger.info("Project scales:")
        logger.info("  solo       - 1 developer")
        logger.info("  small      - 2-5 developers")  
        logger.info("  medium     - 6-15 developers")
        logger.info("  enterprise - 16+ developers")
        logger.info("  auto       - Auto-detect (default)")
        logger.info()
        logger.info("Examples:")
        logger.info("  python sdlc_scanner.py /path/to/project")
        logger.info("  python sdlc_scanner.py /path/to/project enterprise")
        logger.info("  python sdlc_scanner.py . auto")
        logger.info()
        logger.info("Note: This is a compatibility wrapper around sdlc_4_5_universal_validator.py")
        logger.info("For new implementations, use sdlc_4_5_universal_validator.py directly")
        sys.exit(1)
    
    project_path = sys.argv[1]
    project_scale = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != "auto" else None
    
    # Validate project path
    if not os.path.exists(project_path):
        logger.info(f"Error: Project path '{project_path}' does not exist")
        sys.exit(1)
    
    logger.info("SDLC 4.6 Universal Scanner")
    logger.info("==========================")
    logger.info(f"Scanning project: {project_path}")
    if project_scale:
        logger.info(f"Project scale: {project_scale}")
    else:
        logger.info("Project scale: Auto-detect")
    logger.info()
    
    # Run validation
    result = run_universal_validator(project_path, project_scale)
    
    if "error" in result:
        logger.info(f"❌ Scanner Error: {result['error']}")
        sys.exit(1)
    
    # Display results
    scan_result = result["scan_result"]
    
    logger.info("📊 SCAN RESULTS")
    logger.info("===============")
    logger.info(f"Project Scale: {scan_result['framework_scale'].title()}")
    logger.info(f"SDLC Version: {scan_result['sdlc_version']}")
    logger.info(f"Compliance: {scan_result['compliance_percentage']:.1f}%")
    logger.info(f"Authenticity: {scan_result['authenticity_score']:.2f}")
    logger.info(f"Business Risk: {scan_result['business_risk_level'].upper()}")
    logger.info(f"Facade Violations: {scan_result['facade_violations_count']}")
    logger.info()
    
    # Display raw validator output
    logger.info("📋 DETAILED VALIDATION REPORT")
    logger.info("=============================")
    logger.info(result["raw_output"])
    
    if result["raw_error"]:
        logger.info("⚠️  VALIDATION WARNINGS")
        logger.info("======================")
        logger.info(result["raw_error"])
    
    # JSON output for programmatic usage
    if "--json" in sys.argv:
        logger.info("\n" + "="*50)
        logger.info("JSON OUTPUT")
        logger.info("="*50)
        logger.info(json.dumps(scan_result, indent=2))
    
    # Exit with same code as validator
    sys.exit(scan_result["exit_code"])

if __name__ == "__main__":
    main()
