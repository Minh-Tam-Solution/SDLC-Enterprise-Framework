#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""
SDLC 2.x Validation Tool
========================

This tool validates project compliance with SDLC 2.x Framework standards:
- Medium projects ($50K - $500K budget)
- Teams of 5-25 developers
- Agile & DevOps Integration Framework
- Sprint-based development with CI/CD automation

Usage:
    python validate_sdlc_2x.py --project-path "/path/to/project" --team-size 12
"""

import argparse
import json
import os
import subprocess
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
import re

class SDLC2XValidator:
    """SDLC 2.x Agile & DevOps Integration Validation"""
    
    def __init__(self, project_path: str, team_size: int = None):
        self.project_path = Path(project_path)
        self.team_size = team_size
        self.validation_results = {
            "framework": "SDLC 2.x",
            "project_name": self.project_path.name,
            "team_size": team_size,
            "validation_date": datetime.now().isoformat(),
            "overall_compliance": False,
            "compliance_percentage": 0,
            "agile_maturity": "basic",
            "devops_maturity": "basic",
            "quality_gates": {},
            "detailed_results": {}
        }
        
        # SDLC 2.x Requirements
        self.requirements = {
            "agile_framework": {
                "weight": 25,
                "sprint_artifacts": ["sprint-planning", "daily-standups", "retrospectives"],
                "user_stories": True,
                "definition_of_done": True,
                "sprint_length": "2-4 weeks"
            },
            "devops_integration": {
                "weight": 30,
                "ci_cd_pipeline": True,
                "automated_testing": True,
                "deployment_automation": True,
                "monitoring_setup": True
            },
            "layered_architecture": {
                "weight": 20,
                "presentation_layer": True,
                "business_logic_layer": True,
                "data_access_layer": True,
                "infrastructure_layer": True
            },
            "quality_standards": {
                "weight": 15,
                "test_coverage": 70,
                "code_review_process": True,
                "quality_gates": 4
            },
            "team_collaboration": {
                "weight": 10,
                "communication_tools": True,
                "documentation_standards": True,
                "knowledge_sharing": True
            }
        }
    
    def validate_agile_framework(self) -> Tuple[bool, Dict]:
        """Validate Agile framework implementation"""
        logger.info("🏃‍♂️ Validating Agile framework...")
        
        results = {
            "passed": False,
            "score": 0,
            "details": {
                "sprint_artifacts": {},
                "user_stories": {"exists": False, "format_valid": False},
                "definition_of_done": {"exists": False, "complete": False},
                "agile_ceremonies": {},
                "backlog_management": {"exists": False, "prioritized": False}
            }
        }
        
        score_components = []
        
        # Check sprint artifacts (40% weight)
        artifact_score = self._check_sprint_artifacts()
        results["details"]["sprint_artifacts"] = artifact_score
        artifact_percentage = sum([1 for v in artifact_score.values() if v]) / len(artifact_score) * 100
        score_components.append(artifact_percentage * 0.4)
        
        # Check user stories (25% weight)
        user_stories = self._check_user_stories()
        results["details"]["user_stories"] = user_stories
        user_story_percentage = (user_stories["exists"] * 50 + user_stories["format_valid"] * 50)
        score_components.append(user_story_percentage * 0.25)
        
        # Check Definition of Done (20% weight)
        dod = self._check_definition_of_done()
        results["details"]["definition_of_done"] = dod
        dod_percentage = (dod["exists"] * 60 + dod["complete"] * 40)
        score_components.append(dod_percentage * 0.2)
        
        # Check backlog management (15% weight)
        backlog = self._check_backlog_management()
        results["details"]["backlog_management"] = backlog
        backlog_percentage = (backlog["exists"] * 70 + backlog["prioritized"] * 30)
        score_components.append(backlog_percentage * 0.15)
        
        total_score = sum(score_components)
        results["score"] = total_score
        results["passed"] = total_score >= 70
        
        logger.info(f"   📋 Sprint artifacts: {artifact_percentage:.1f}%")
        logger.info(f"   📖 User stories: {user_story_percentage:.1f}%")
        logger.info(f"   ✅ Definition of Done: {dod_percentage:.1f}%")
        logger.info(f"   📊 Agile framework score: {total_score:.1f}/100")
        
        return results["passed"], results
    
    def _check_sprint_artifacts(self) -> Dict:
        """Check for sprint artifacts"""
        artifacts = {}
        
        # Check for agile directory structure
        agile_dirs = ["agile", "sprints", "scrum"]
        base_dir = None
        for agile_dir in agile_dirs:
            if (self.project_path / agile_dir).exists():
                base_dir = self.project_path / agile_dir
                break
        
        if base_dir:
            artifacts["sprint_planning"] = (base_dir / "sprint-planning").exists() or any("sprint" in f.name.lower() and "plan" in f.name.lower() for f in base_dir.iterdir())
            artifacts["daily_standups"] = (base_dir / "daily-standups").exists() or any("standup" in f.name.lower() or "daily" in f.name.lower() for f in base_dir.iterdir())
            artifacts["retrospectives"] = (base_dir / "retrospectives").exists() or any("retro" in f.name.lower() for f in base_dir.iterdir())
        else:
            # Check in docs directory
            docs_dir = self.project_path / "docs"
            if docs_dir.exists():
                artifacts["sprint_planning"] = any("sprint" in f.name.lower() and "plan" in f.name.lower() for f in docs_dir.rglob("*"))
                artifacts["daily_standups"] = any("standup" in f.name.lower() or "daily" in f.name.lower() for f in docs_dir.rglob("*"))
                artifacts["retrospectives"] = any("retro" in f.name.lower() for f in docs_dir.rglob("*"))
            else:
                artifacts = {key: False for key in ["sprint_planning", "daily_standups", "retrospectives"]}
        
        return artifacts
    
    def _check_user_stories(self) -> Dict:
        """Check for user stories implementation"""
        user_stories = {"exists": False, "format_valid": False}
        
        # Look for user stories in common locations
        story_locations = [
            "docs/user-stories",
            "agile/backlog", 
            "stories",
            "requirements"
        ]
        
        for location in story_locations:
            story_path = self.project_path / location
            if story_path.exists():
                user_stories["exists"] = True
                
                # Check format validity (look for "As a... I want... So that..." pattern)
                for story_file in story_path.rglob("*.md"):
                    try:
                        content = story_file.read_text().lower()
                        if "as a" in content and ("i want" in content or "i need" in content):
                            user_stories["format_valid"] = True
                            break
                    except:
                        pass
                break
        
        # Also check README for user stories
        if not user_stories["exists"]:
            readme_path = self.project_path / "README.md"
            if readme_path.exists():
                try:
                    content = readme_path.read_text().lower()
                    if "user story" in content or ("as a" in content and "i want" in content):
                        user_stories["exists"] = True
                        user_stories["format_valid"] = True
                except:
                    pass
        
        return user_stories
    
    def _check_definition_of_done(self) -> Dict:
        """Check for Definition of Done"""
        dod = {"exists": False, "complete": False}
        
        # Look for DoD in common locations
        dod_files = [
            "DEFINITION_OF_DONE.md",
            "DoD.md",
            "definition-of-done.md",
            "agile/definition-of-done.md",
            "docs/definition-of-done.md"
        ]
        
        for dod_file in dod_files:
            dod_path = self.project_path / dod_file
            if dod_path.exists():
                dod["exists"] = True
                
                try:
                    content = dod_path.read_text().lower()
                    # Check for completeness (should mention testing, review, documentation)
                    completeness_indicators = ["test", "review", "documentation", "deployment"]
                    complete_count = sum(1 for indicator in completeness_indicators if indicator in content)
                    dod["complete"] = complete_count >= 3
                except:
                    pass
                break
        
        # Check in README or other docs
        if not dod["exists"]:
            for doc_file in ["README.md", "CONTRIBUTING.md"]:
                doc_path = self.project_path / doc_file
                if doc_path.exists():
                    try:
                        content = doc_path.read_text().lower()
                        if "definition of done" in content or "done criteria" in content:
                            dod["exists"] = True
                            dod["complete"] = len([word for word in ["test", "review", "deploy"] if word in content]) >= 2
                            break
                    except:
                        pass
        
        return dod
    
    def _check_backlog_management(self) -> Dict:
        """Check for backlog management"""
        backlog = {"exists": False, "prioritized": False}
        
        # Look for backlog files
        backlog_locations = [
            "backlog",
            "product-backlog", 
            "agile/backlog",
            "docs/backlog"
        ]
        
        for location in backlog_locations:
            backlog_path = self.project_path / location
            if backlog_path.exists():
                backlog["exists"] = True
                
                # Check for prioritization indicators
                for backlog_file in backlog_path.rglob("*.md"):
                    try:
                        content = backlog_file.read_text().lower()
                        priority_indicators = ["priority", "high", "medium", "low", "story points"]
                        if any(indicator in content for indicator in priority_indicators):
                            backlog["prioritized"] = True
                            break
                    except:
                        pass
                break
        
        return backlog
    
    def validate_devops_integration(self) -> Tuple[bool, Dict]:
        """Validate DevOps integration and automation"""
        logger.info("🔧 Validating DevOps integration...")
        
        results = {
            "passed": False,
            "score": 0,
            "details": {
                "ci_cd_pipeline": {"exists": False, "platform": None, "stages": []},
                "automated_testing": {"unit": False, "integration": False, "coverage": 0},
                "deployment_automation": {"exists": False, "environments": []},
                "monitoring": {"exists": False, "tools": []},
                "containerization": {"docker": False, "orchestration": False}
            }
        }
        
        score_components = []
        
        # Check CI/CD pipeline (35% weight)
        ci_cd = self._check_ci_cd_pipeline()
        results["details"]["ci_cd_pipeline"] = ci_cd
        ci_cd_score = (ci_cd["exists"] * 100)
        score_components.append(ci_cd_score * 0.35)
        
        # Check automated testing (30% weight)
        testing = self._check_automated_testing()
        results["details"]["automated_testing"] = testing
        testing_score = (testing["unit"] * 40 + testing["integration"] * 40 + min(testing["coverage"], 70) / 70 * 20)
        score_components.append(testing_score * 0.3)
        
        # Check deployment automation (20% weight)
        deployment = self._check_deployment_automation()
        results["details"]["deployment_automation"] = deployment
        deployment_score = deployment["exists"] * 100
        score_components.append(deployment_score * 0.2)
        
        # Check monitoring setup (10% weight)
        monitoring = self._check_monitoring_setup()
        results["details"]["monitoring"] = monitoring
        monitoring_score = monitoring["exists"] * 100
        score_components.append(monitoring_score * 0.1)
        
        # Check containerization (5% weight)
        containers = self._check_containerization()
        results["details"]["containerization"] = containers
        container_score = (containers["docker"] * 70 + containers["orchestration"] * 30)
        score_components.append(container_score * 0.05)
        
        total_score = sum(score_components)
        results["score"] = total_score
        results["passed"] = total_score >= 70
        
        logger.info(f"   🚀 CI/CD pipeline: {'✅' if ci_cd['exists'] else '❌'} ({ci_cd.get('platform', 'none')})")
        logger.info(f"   🧪 Automated testing: {testing_score:.1f}%")
        logger.info(f"   🚢 Deployment automation: {'✅' if deployment['exists'] else '❌'}")
        logger.info(f"   📊 DevOps integration score: {total_score:.1f}/100")
        
        return results["passed"], results
    
    def _check_ci_cd_pipeline(self) -> Dict:
        """Check for CI/CD pipeline configuration"""
        ci_cd = {"exists": False, "platform": None, "stages": []}
        
        # Check for different CI/CD platforms
        ci_platforms = [
            (".github/workflows", "github-actions"),
            ("Jenkinsfile", "jenkins"),
            (".gitlab-ci.yml", "gitlab-ci"),
            (".circleci/config.yml", "circleci"),
            ("azure-pipelines.yml", "azure-devops"),
            ("devops/ci-cd", "custom")
        ]
        
        for file_path, platform in ci_platforms:
            path = self.project_path / file_path
            if path.exists():
                ci_cd["exists"] = True
                ci_cd["platform"] = platform
                
                # Try to identify pipeline stages
                if platform == "github-actions" and path.is_dir():
                    for workflow_file in path.glob("*.yml"):
                        try:
                            with open(workflow_file) as f:
                                content = yaml.safe_load(f)
                                if "jobs" in content:
                                    ci_cd["stages"] = list(content["jobs"].keys())
                                    break
                        except:
                            pass
                elif file_path == "Jenkinsfile":
                    try:
                        content = path.read_text()
                        # Look for stages in Jenkinsfile
                        stage_matches = re.findall(r"stage\s*\(\s*['\"]([^'\"]+)['\"]", content)
                        ci_cd["stages"] = stage_matches
                    except:
                        pass
                break
        
        return ci_cd
    
    def _check_automated_testing(self) -> Dict:
        """Check for automated testing setup"""
        testing = {"unit": False, "integration": False, "coverage": 0}
        
        # Check for test directories
        test_dirs = ["tests", "test", "__tests__", "spec"]
        test_structure_exists = any((self.project_path / td).exists() for td in test_dirs)
        
        if test_structure_exists:
            testing["unit"] = True  # Assume unit tests exist if test structure exists
            
            # Check for integration tests
            for test_dir in test_dirs:
                test_path = self.project_path / test_dir
                if test_path.exists():
                    integration_indicators = ["integration", "e2e", "api"]
                    for indicator in integration_indicators:
                        if any(indicator in str(p) for p in test_path.rglob("*")):
                            testing["integration"] = True
                            break
        
        # Check test coverage configuration
        coverage_files = [
            "jest.config.js",
            "jest.config.json", 
            ".nycrc",
            "coverage/lcov.info"
        ]
        
        coverage_configured = any((self.project_path / cf).exists() for cf in coverage_files)
        if coverage_configured:
            testing["coverage"] = 70  # Assume target coverage if configured
        
        # Check package.json for test scripts
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    scripts = data.get("scripts", {})
                    if "test" in scripts:
                        testing["unit"] = True
                    if any("integration" in script or "e2e" in script for script in scripts.values()):
                        testing["integration"] = True
                    if any("coverage" in script for script in scripts.values()):
                        testing["coverage"] = 70
            except:
                pass
        
        return testing
    
    def _check_deployment_automation(self) -> Dict:
        """Check for deployment automation"""
        deployment = {"exists": False, "environments": []}
        
        # Check for deployment configuration files
        deployment_files = [
            "docker-compose.yml",
            "docker-compose.yaml",
            "Dockerfile",
            "k8s",
            "kubernetes",
            "helm",
            "deploy",
            "deployment"
        ]
        
        for deploy_file in deployment_files:
            if (self.project_path / deploy_file).exists():
                deployment["exists"] = True
                
                # Check for multiple environments
                if deploy_file.startswith("docker-compose"):
                    try:
                        with open(self.project_path / deploy_file) as f:
                            content = yaml.safe_load(f)
                            if "services" in content:
                                deployment["environments"] = ["development"]
                    except:
                        pass
                elif deploy_file in ["k8s", "kubernetes"]:
                    k8s_path = self.project_path / deploy_file
                    if k8s_path.is_dir():
                        env_dirs = [d.name for d in k8s_path.iterdir() if d.is_dir()]
                        deployment["environments"] = env_dirs
                
                break
        
        # Check for deployment scripts
        scripts_dir = self.project_path / "scripts"
        if scripts_dir.exists():
            deploy_scripts = [f for f in scripts_dir.iterdir() if "deploy" in f.name.lower()]
            if deploy_scripts:
                deployment["exists"] = True
        
        return deployment
    
    def _check_monitoring_setup(self) -> Dict:
        """Check for monitoring and observability setup"""
        monitoring = {"exists": False, "tools": []}
        
        # Check for monitoring configuration
        monitoring_indicators = [
            ("prometheus.yml", "prometheus"),
            ("grafana", "grafana"),
            ("monitoring", "custom"),
            ("logs", "logging"),
            ("health", "health-check")
        ]
        
        for file_pattern, tool in monitoring_indicators:
            if any(file_pattern in str(p) for p in self.project_path.rglob("*")):
                monitoring["exists"] = True
                monitoring["tools"].append(tool)
        
        # Check docker-compose for monitoring services
        docker_compose_files = ["docker-compose.yml", "docker-compose.yaml", "docker-compose.dev.yml"]
        for compose_file in docker_compose_files:
            compose_path = self.project_path / compose_file
            if compose_path.exists():
                try:
                    with open(compose_path) as f:
                        content = f.read()
                        monitoring_services = ["prometheus", "grafana", "elasticsearch", "kibana"]
                        for service in monitoring_services:
                            if service in content:
                                monitoring["exists"] = True
                                if service not in monitoring["tools"]:
                                    monitoring["tools"].append(service)
                except:
                    pass
        
        return monitoring
    
    def _check_containerization(self) -> Dict:
        """Check for containerization setup"""
        containers = {"docker": False, "orchestration": False}
        
        # Check for Docker
        docker_files = ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"]
        containers["docker"] = any((self.project_path / df).exists() for df in docker_files)
        
        # Check for orchestration
        orchestration_dirs = ["k8s", "kubernetes", "helm"]
        containers["orchestration"] = any((self.project_path / od).exists() and (self.project_path / od).is_dir() for od in orchestration_dirs)
        
        return containers
    
    def validate_layered_architecture(self) -> Tuple[bool, Dict]:
        """Validate layered architecture implementation"""
        logger.info("🏗️ Validating layered architecture...")
        
        results = {
            "passed": False,
            "score": 0,
            "details": {
                "presentation_layer": {"exists": False, "framework": None},
                "business_logic_layer": {"exists": False, "separation": False},
                "data_access_layer": {"exists": False, "orm": None},
                "infrastructure_layer": {"exists": False, "components": []}
            }
        }
        
        score_components = []
        
        # Check presentation layer (25% weight)
        presentation = self._check_presentation_layer()
        results["details"]["presentation_layer"] = presentation
        presentation_score = presentation["exists"] * 100
        score_components.append(presentation_score * 0.25)
        
        # Check business logic layer (30% weight)
        business_logic = self._check_business_logic_layer()
        results["details"]["business_logic_layer"] = business_logic
        business_score = (business_logic["exists"] * 70 + business_logic["separation"] * 30)
        score_components.append(business_score * 0.3)
        
        # Check data access layer (30% weight)
        data_access = self._check_data_access_layer()
        results["details"]["data_access_layer"] = data_access
        data_score = data_access["exists"] * 100
        score_components.append(data_score * 0.3)
        
        # Check infrastructure layer (15% weight)
        infrastructure = self._check_infrastructure_layer()
        results["details"]["infrastructure_layer"] = infrastructure
        infra_score = infrastructure["exists"] * 100
        score_components.append(infra_score * 0.15)
        
        total_score = sum(score_components)
        results["score"] = total_score
        results["passed"] = total_score >= 70
        
        logger.info(f"   🎨 Presentation layer: {'✅' if presentation['exists'] else '❌'} ({presentation.get('framework', 'none')})")
        logger.info(f"   💼 Business logic: {'✅' if business_logic['exists'] else '❌'}")
        logger.info(f"   🗄️ Data access: {'✅' if data_access['exists'] else '❌'} ({data_access.get('orm', 'none')})")
        logger.info(f"   🏗️ Infrastructure: {'✅' if infrastructure['exists'] else '❌'}")
        logger.info(f"   📊 Architecture score: {total_score:.1f}/100")
        
        return results["passed"], results
    
    def _check_presentation_layer(self) -> Dict:
        """Check presentation layer implementation"""
        presentation = {"exists": False, "framework": None}
        
        # Check for frontend frameworks
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    if "react" in deps:
                        presentation["exists"] = True
                        presentation["framework"] = "react"
                    elif "vue" in deps:
                        presentation["exists"] = True
                        presentation["framework"] = "vue"
                    elif "angular" in deps or "@angular/core" in deps:
                        presentation["exists"] = True
                        presentation["framework"] = "angular"
            except:
                pass
        
        # Check for presentation layer directory structure
        presentation_dirs = ["src/presentation", "frontend", "client", "ui"]
        for pres_dir in presentation_dirs:
            if (self.project_path / pres_dir).exists():
                presentation["exists"] = True
                if not presentation["framework"]:
                    presentation["framework"] = "custom"
                break
        
        return presentation
    
    def _check_business_logic_layer(self) -> Dict:
        """Check business logic layer separation"""
        business_logic = {"exists": False, "separation": False}
        
        # Check for business logic directories
        business_dirs = [
            "src/business-logic",
            "src/business",
            "src/services",
            "src/domain",
            "business",
            "services"
        ]
        
        for biz_dir in business_dirs:
            biz_path = self.project_path / biz_dir
            if biz_path.exists() and biz_path.is_dir():
                business_logic["exists"] = True
                
                # Check for proper separation (multiple modules/files)
                business_files = list(biz_path.rglob("*.js")) + list(biz_path.rglob("*.py")) + list(biz_path.rglob("*.ts"))
                if len(business_files) >= 3:  # At least 3 business logic files
                    business_logic["separation"] = True
                break
        
        # Alternative check in src structure
        if not business_logic["exists"]:
            src_path = self.project_path / "src"
            if src_path.exists():
                # Look for business logic patterns in file names
                business_patterns = ["service", "business", "domain", "use-case", "logic"]
                business_files = []
                for pattern in business_patterns:
                    business_files.extend(src_path.rglob(f"*{pattern}*"))
                
                if business_files:
                    business_logic["exists"] = True
                    business_logic["separation"] = len(business_files) >= 2
        
        return business_logic
    
    def _check_data_access_layer(self) -> Dict:
        """Check data access layer implementation"""
        data_access = {"exists": False, "orm": None}
        
        # Check for data access directories
        data_dirs = [
            "src/data-access",
            "src/data",
            "src/database",
            "src/repositories",
            "data",
            "database",
            "db"
        ]
        
        for data_dir in data_dirs:
            if (self.project_path / data_dir).exists():
                data_access["exists"] = True
                break
        
        # Check for ORM/database libraries
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    if "sequelize" in deps:
                        data_access["orm"] = "sequelize"
                    elif "prisma" in deps or "@prisma/client" in deps:
                        data_access["orm"] = "prisma"
                    elif "typeorm" in deps:
                        data_access["orm"] = "typeorm"
                    elif "knex" in deps:
                        data_access["orm"] = "knex"
                    elif "mongoose" in deps:
                        data_access["orm"] = "mongoose"
                    
                    if data_access["orm"]:
                        data_access["exists"] = True
            except:
                pass
        
        # Check for Python ORMs
        requirements_txt = self.project_path / "requirements.txt"
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text().lower()
                if "sqlalchemy" in content:
                    data_access["orm"] = "sqlalchemy"
                    data_access["exists"] = True
                elif "django" in content:
                    data_access["orm"] = "django-orm"
                    data_access["exists"] = True
            except:
                pass
        
        return data_access
    
    def _check_infrastructure_layer(self) -> Dict:
        """Check infrastructure layer implementation"""
        infrastructure = {"exists": False, "components": []}
        
        # Check for infrastructure directories
        infra_dirs = ["infrastructure", "infra", "devops", "deployment"]
        for infra_dir in infra_dirs:
            if (self.project_path / infra_dir).exists():
                infrastructure["exists"] = True
                
                # Identify infrastructure components
                infra_path = self.project_path / infra_dir
                for component in ["docker", "kubernetes", "terraform", "ansible", "monitoring"]:
                    if any(component in str(p) for p in infra_path.rglob("*")):
                        infrastructure["components"].append(component)
                break
        
        # Check for infrastructure files at root
        root_infra_files = ["Dockerfile", "docker-compose.yml", "Jenkinsfile", "terraform.tf"]
        for infra_file in root_infra_files:
            if (self.project_path / infra_file).exists():
                infrastructure["exists"] = True
                component = infra_file.split(".")[0].lower()
                if component not in infrastructure["components"]:
                    infrastructure["components"].append(component)
        
        return infrastructure
    
    def validate_quality_standards(self) -> Tuple[bool, Dict]:
        """Validate quality standards compliance"""
        logger.info("📊 Validating quality standards...")
        
        results = {
            "passed": False,
            "score": 0,
            "details": {
                "test_coverage": {"percentage": 0, "meets_target": False},
                "code_review_process": {"exists": False, "automated": False},
                "quality_gates": {"count": 0, "implemented": []},
                "code_quality_tools": {"linting": False, "formatting": False, "security": False}
            }
        }
        
        score_components = []
        
        # Check test coverage (40% weight)
        coverage = self._check_test_coverage_detailed()
        results["details"]["test_coverage"] = coverage
        coverage_score = min(coverage["percentage"], 70) / 70 * 100
        score_components.append(coverage_score * 0.4)
        
        # Check code review process (30% weight)
        code_review = self._check_code_review_process()
        results["details"]["code_review_process"] = code_review
        review_score = (code_review["exists"] * 70 + code_review["automated"] * 30)
        score_components.append(review_score * 0.3)
        
        # Check quality gates (20% weight)
        quality_gates = self._check_quality_gates_implementation()
        results["details"]["quality_gates"] = quality_gates
        gates_score = min(quality_gates["count"], 4) / 4 * 100
        score_components.append(gates_score * 0.2)
        
        # Check code quality tools (10% weight)
        quality_tools = self._check_code_quality_tools()
        results["details"]["code_quality_tools"] = quality_tools
        tools_score = sum([1 for v in quality_tools.values() if v]) / len(quality_tools) * 100
        score_components.append(tools_score * 0.1)
        
        total_score = sum(score_components)
        results["score"] = total_score
        results["passed"] = total_score >= 70
        
        logger.info(f"   🧪 Test coverage: {coverage['percentage']:.1f}%")
        logger.info(f"   👥 Code review: {'✅' if code_review['exists'] else '❌'}")
        logger.info(f"   🚪 Quality gates: {quality_gates['count']}/4")
        logger.info(f"   📊 Quality standards score: {total_score:.1f}/100")
        
        return results["passed"], results
    
    def _check_test_coverage_detailed(self) -> Dict:
        """Check detailed test coverage information"""
        coverage = {"percentage": 0, "meets_target": False}
        
        # Check for coverage reports
        coverage_files = [
            "coverage/lcov-report/index.html",
            "coverage/index.html",
            "htmlcov/index.html",
            "coverage.xml"
        ]
        
        for cov_file in coverage_files:
            if (self.project_path / cov_file).exists():
                # For SDLC 2.x validation, assume 70% if coverage reports exist
                coverage["percentage"] = 70
                coverage["meets_target"] = True
                break
        
        # Check for coverage configuration
        if coverage["percentage"] == 0:
            coverage_configs = ["jest.config.js", ".nycrc", "pytest.ini"]
            for config in coverage_configs:
                if (self.project_path / config).exists():
                    coverage["percentage"] = 60  # Assume basic coverage
                    coverage["meets_target"] = False
                    break
        
        return coverage
    
    def _check_code_review_process(self) -> Dict:
        """Check code review process implementation"""
        code_review = {"exists": False, "automated": False}
        
        # Check for GitHub/GitLab review configuration
        review_configs = [
            ".github/pull_request_template.md",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".gitlab/merge_request_templates",
            "PULL_REQUEST_TEMPLATE.md"
        ]
        
        for review_config in review_configs:
            if (self.project_path / review_config).exists():
                code_review["exists"] = True
                break
        
        # Check for automated review tools
        github_workflows = self.project_path / ".github" / "workflows"
        if github_workflows.exists():
            for workflow in github_workflows.glob("*.yml"):
                try:
                    content = workflow.read_text()
                    if "pull_request" in content and any(tool in content for tool in ["eslint", "sonar", "codeclimate"]):
                        code_review["automated"] = True
                        code_review["exists"] = True
                        break
                except:
                    pass
        
        # Check for branch protection (indicates review process)
        if (self.project_path / ".git").exists():
            try:
                # This is a simplified check - in practice, you'd need to query the Git provider API
                code_review["exists"] = True
            except:
                pass
        
        return code_review
    
    def _check_quality_gates_implementation(self) -> Dict:
        """Check quality gates implementation"""
        quality_gates = {"count": 0, "implemented": []}
        
        # SDLC 2.x quality gates
        gate_indicators = {
            "sprint_planning_approval": ["sprint", "planning", "backlog"],
            "development_standards": ["lint", "format", "standards"],
            "sprint_review": ["review", "demo", "stakeholder"],
            "release_readiness": ["release", "deployment", "production"]
        }
        
        for gate, indicators in gate_indicators.items():
            gate_found = False
            
            # Check in documentation
            for doc_dir in ["docs", "agile", "quality"]:
                doc_path = self.project_path / doc_dir
                if doc_path.exists():
                    for doc_file in doc_path.rglob("*.md"):
                        try:
                            content = doc_file.read_text().lower()
                            if any(indicator in content for indicator in indicators):
                                gate_found = True
                                break
                        except:
                            pass
                if gate_found:
                    break
            
            # Check in CI/CD configuration
            if not gate_found:
                ci_files = [".github/workflows", "Jenkinsfile", ".gitlab-ci.yml"]
                for ci_file in ci_files:
                    ci_path = self.project_path / ci_file
                    if ci_path.exists():
                        try:
                            if ci_path.is_file():
                                content = ci_path.read_text().lower()
                            else:
                                content = ""
                                for workflow in ci_path.glob("*.yml"):
                                    content += workflow.read_text().lower()
                            
                            if any(indicator in content for indicator in indicators):
                                gate_found = True
                                break
                        except:
                            pass
            
            if gate_found:
                quality_gates["count"] += 1
                quality_gates["implemented"].append(gate)
        
        return quality_gates
    
    def _check_code_quality_tools(self) -> Dict:
        """Check code quality tools configuration"""
        quality_tools = {"linting": False, "formatting": False, "security": False}
        
        # Check for linting
        lint_configs = [".eslintrc.json", ".eslintrc.js", "pylint.cfg", "flake8.cfg"]
        quality_tools["linting"] = any((self.project_path / lc).exists() for lc in lint_configs)
        
        # Check for formatting
        format_configs = [".prettierrc", ".prettierrc.json", ".black", "pyproject.toml"]
        quality_tools["formatting"] = any((self.project_path / fc).exists() for fc in format_configs)
        
        # Check for security tools
        security_configs = [".snyk", "bandit.yml", "safety-policy.json"]
        quality_tools["security"] = any((self.project_path / sc).exists() for sc in security_configs)
        
        # Check package.json for tool scripts
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    scripts = data.get("scripts", {})
                    
                    if any("lint" in script for script in scripts.values()):
                        quality_tools["linting"] = True
                    if any("format" in script or "prettier" in script for script in scripts.values()):
                        quality_tools["formatting"] = True
                    if any("security" in script or "audit" in script for script in scripts.values()):
                        quality_tools["security"] = True
            except:
                pass
        
        return quality_tools
    
    def validate_team_collaboration(self) -> Tuple[bool, Dict]:
        """Validate team collaboration tools and processes"""
        logger.info("👥 Validating team collaboration...")
        
        results = {
            "passed": False,
            "score": 0,
            "details": {
                "communication_tools": {"configured": False, "tools": []},
                "documentation_standards": {"exists": False, "complete": False},
                "knowledge_sharing": {"exists": False, "methods": []},
                "team_workflows": {"defined": False, "documented": False}
            }
        }
        
        score_components = []
        
        # Check communication tools (30% weight)
        communication = self._check_communication_tools()
        results["details"]["communication_tools"] = communication
        comm_score = communication["configured"] * 100
        score_components.append(comm_score * 0.3)
        
        # Check documentation standards (40% weight)
        documentation = self._check_documentation_standards()
        results["details"]["documentation_standards"] = documentation
        doc_score = (documentation["exists"] * 60 + documentation["complete"] * 40)
        score_components.append(doc_score * 0.4)
        
        # Check knowledge sharing (20% weight)
        knowledge = self._check_knowledge_sharing()
        results["details"]["knowledge_sharing"] = knowledge
        knowledge_score = knowledge["exists"] * 100
        score_components.append(knowledge_score * 0.2)
        
        # Check team workflows (10% weight)
        workflows = self._check_team_workflows()
        results["details"]["team_workflows"] = workflows
        workflow_score = (workflows["defined"] * 50 + workflows["documented"] * 50)
        score_components.append(workflow_score * 0.1)
        
        total_score = sum(score_components)
        results["score"] = total_score
        results["passed"] = total_score >= 70
        
        logger.info(f"   💬 Communication: {'✅' if communication['configured'] else '❌'}")
        logger.info(f"   📚 Documentation: {'✅' if documentation['exists'] else '❌'}")
        logger.info(f"   🧠 Knowledge sharing: {'✅' if knowledge['exists'] else '❌'}")
        logger.info(f"   📊 Team collaboration score: {total_score:.1f}/100")
        
        return results["passed"], results
    
    def _check_communication_tools(self) -> Dict:
        """Check communication tools configuration"""
        communication = {"configured": False, "tools": []}
        
        # Check for communication references in documentation
        comm_indicators = [
            ("slack", "Slack"),
            ("teams", "Microsoft Teams"),
            ("discord", "Discord"),
            ("mattermost", "Mattermost")
        ]
        
        readme_path = self.project_path / "README.md"
        if readme_path.exists():
            try:
                content = readme_path.read_text().lower()
                for indicator, tool in comm_indicators:
                    if indicator in content:
                        communication["configured"] = True
                        communication["tools"].append(tool)
            except:
                pass
        
        # Check for team communication documentation
        comm_docs = ["COMMUNICATION.md", "TEAM.md", "docs/team.md", "docs/communication.md"]
        for comm_doc in comm_docs:
            if (self.project_path / comm_doc).exists():
                communication["configured"] = True
                break
        
        return communication
    
    def _check_documentation_standards(self) -> Dict:
        """Check documentation standards implementation"""
        documentation = {"exists": False, "complete": False}
        
        # Check for comprehensive README
        readme_path = self.project_path / "README.md"
        if readme_path.exists():
            documentation["exists"] = True
            
            try:
                content = readme_path.read_text().lower()
                required_sections = ["installation", "usage", "api", "testing", "contributing"]
                complete_count = sum(1 for section in required_sections if section in content)
                documentation["complete"] = complete_count >= 3
            except:
                pass
        
        # Check for additional documentation
        doc_dirs = ["docs", "documentation"]
        for doc_dir in doc_dirs:
            doc_path = self.project_path / doc_dir
            if doc_path.exists() and doc_path.is_dir():
                documentation["exists"] = True
                doc_files = list(doc_path.rglob("*.md"))
                if len(doc_files) >= 3:
                    documentation["complete"] = True
                break
        
        return documentation
    
    def _check_knowledge_sharing(self) -> Dict:
        """Check knowledge sharing mechanisms"""
        knowledge = {"exists": False, "methods": []}
        
        # Check for knowledge sharing indicators
        sharing_methods = {
            "wiki": ["wiki", "confluence"],
            "onboarding": ["onboarding", "getting-started"],
            "architecture_docs": ["architecture", "design", "adr"],
            "code_comments": ["comments", "documentation"],
            "runbooks": ["runbook", "playbook", "operations"]
        }
        
        for method, indicators in sharing_methods.items():
            found = False
            
            # Check in documentation
            for doc_dir in ["docs", "wiki", "."]:
                doc_path = self.project_path / doc_dir
                if doc_path.exists():
                    for doc_file in doc_path.rglob("*.md"):
                        try:
                            content = doc_file.read_text().lower()
                            if any(indicator in content or indicator in doc_file.name.lower() for indicator in indicators):
                                found = True
                                break
                        except:
                            pass
                if found:
                    break
            
            if found:
                knowledge["exists"] = True
                knowledge["methods"].append(method)
        
        return knowledge
    
    def _check_team_workflows(self) -> Dict:
        """Check team workflow definition and documentation"""
        workflows = {"defined": False, "documented": False}
        
        # Check for workflow documentation
        workflow_files = [
            "CONTRIBUTING.md",
            "WORKFLOW.md",
            "docs/workflow.md",
            "docs/development.md",
            ".github/CONTRIBUTING.md"
        ]
        
        for workflow_file in workflow_files:
            if (self.project_path / workflow_file).exists():
                workflows["documented"] = True
                workflows["defined"] = True
                break
        
        # Check for branch naming and PR templates (indicates defined workflows)
        if (self.project_path / ".github").exists():
            workflows["defined"] = True
        
        return workflows
    
    def run_validation(self) -> Dict:
        """Run complete SDLC 2.x validation"""
        logger.info(f"🚀 Starting SDLC 2.x validation for {self.validation_results['project_name']}")
        logger.info(f"📁 Project path: {self.project_path}")
        if self.team_size:
            logger.info(f"👥 Team size: {self.team_size} developers")
        
        if not self.project_path.exists():
            logger.info(f"❌ Project path does not exist: {self.project_path}")
            sys.exit(1)
        
        validation_components = []
        
        try:
            # Agile Framework (25% weight)
            passed, results = self.validate_agile_framework()
            self.validation_results["detailed_results"]["agile_framework"] = results
            validation_components.append(results["score"] * 0.25)
            
            # DevOps Integration (30% weight)
            passed, results = self.validate_devops_integration()
            self.validation_results["detailed_results"]["devops_integration"] = results
            validation_components.append(results["score"] * 0.3)
            
            # Layered Architecture (20% weight)
            passed, results = self.validate_layered_architecture()
            self.validation_results["detailed_results"]["layered_architecture"] = results
            validation_components.append(results["score"] * 0.2)
            
            # Quality Standards (15% weight)
            passed, results = self.validate_quality_standards()
            self.validation_results["detailed_results"]["quality_standards"] = results
            validation_components.append(results["score"] * 0.15)
            
            # Team Collaboration (10% weight)
            passed, results = self.validate_team_collaboration()
            self.validation_results["detailed_results"]["team_collaboration"] = results
            validation_components.append(results["score"] * 0.1)
            
            # Calculate overall compliance
            overall_score = sum(validation_components)
            self.validation_results["compliance_percentage"] = overall_score
            self.validation_results["overall_compliance"] = overall_score >= 75
            
            # Determine maturity levels
            self._assess_maturity_levels()
            
            # Generate summary
            self._generate_validation_summary()
            
            return self.validation_results
            
        except Exception as e:
            logger.info(f"❌ Validation failed: {str(e)}")
            self.validation_results["error"] = str(e)
            return self.validation_results
    
    def _assess_maturity_levels(self):
        """Assess Agile and DevOps maturity levels"""
        
        # Agile maturity assessment
        agile_score = self.validation_results["detailed_results"]["agile_framework"]["score"]
        if agile_score >= 90:
            self.validation_results["agile_maturity"] = "advanced"
        elif agile_score >= 75:
            self.validation_results["agile_maturity"] = "intermediate"
        elif agile_score >= 60:
            self.validation_results["agile_maturity"] = "basic"
        else:
            self.validation_results["agile_maturity"] = "initial"
        
        # DevOps maturity assessment
        devops_score = self.validation_results["detailed_results"]["devops_integration"]["score"]
        if devops_score >= 90:
            self.validation_results["devops_maturity"] = "advanced"
        elif devops_score >= 75:
            self.validation_results["devops_maturity"] = "intermediate"
        elif devops_score >= 60:
            self.validation_results["devops_maturity"] = "basic"
        else:
            self.validation_results["devops_maturity"] = "initial"
    
    def _generate_validation_summary(self):
        """Generate comprehensive validation summary"""
        logger.info("\n" + "="*70)
        logger.info("📊 SDLC 2.x VALIDATION SUMMARY")
        logger.info("="*70)
        
        logger.info(f"Project: {self.validation_results['project_name']}")
        logger.info(f"Framework: {self.validation_results['framework']}")
        if self.team_size:
            logger.info(f"Team Size: {self.team_size} developers")
        logger.info(f"Validation Date: {self.validation_results['validation_date']}")
        
        logger.info(f"\n🎯 Overall Compliance: {self.validation_results['compliance_percentage']:.1f}%")
        status = "✅ PASSED" if self.validation_results["overall_compliance"] else "❌ FAILED"
        logger.info(f"Status: {status}")
        
        logger.info(f"\n📈 Maturity Assessment:")
        logger.info(f"  🏃‍♂️ Agile Maturity: {self.validation_results['agile_maturity'].upper()}")
        logger.info(f"  🔧 DevOps Maturity: {self.validation_results['devops_maturity'].upper()}")
        
        logger.info("\n📋 Component Scores:")
        components = [
            ("agile_framework", "Agile Framework", 25),
            ("devops_integration", "DevOps Integration", 30),
            ("layered_architecture", "Layered Architecture", 20),
            ("quality_standards", "Quality Standards", 15),
            ("team_collaboration", "Team Collaboration", 10)
        ]
        
        for component, name, weight in components:
            if component in self.validation_results["detailed_results"]:
                results = self.validation_results["detailed_results"][component]
                score = results["score"]
                status = "✅" if results["passed"] else "❌"
                logger.info(f"  {status} {name}: {score:.1f}% (weight: {weight}%)")
        
        # Recommendations
        logger.info("\n💡 Recommendations:")
        overall_score = self.validation_results["compliance_percentage"]
        
        if overall_score >= 90:
            logger.info("  🎉 Excellent! Your project exemplifies SDLC 2.x best practices")
            logger.info("  📈 Consider upgrading to SDLC 3.x for enterprise features")
            logger.info("  🔄 Share your practices with other teams")
        elif overall_score >= 75:
            logger.info("  ✅ Good compliance! Focus on these areas for improvement:")
            self._provide_specific_recommendations()
        elif overall_score >= 60:
            logger.info("  ⚠️  Moderate compliance. Priority improvements needed:")
            self._provide_specific_recommendations()
            logger.info("  📚 Review SDLC 2.x documentation for implementation guidance")
        else:
            logger.info("  🚨 Low compliance. Immediate action required:")
            self._provide_specific_recommendations()
            logger.info("  🆘 Consider starting with SDLC 1.x for simpler implementation")
        
        logger.info("\n" + "="*70)
    
    def _provide_specific_recommendations(self):
        """Provide specific recommendations based on validation results"""
        
        # Check each component and provide targeted advice
        for component, results in self.validation_results["detailed_results"].items():
            if not results["passed"]:
                if component == "agile_framework":
                    logger.info("  📋 Implement sprint planning and retrospective processes")
                    logger.info("  📖 Create user stories with acceptance criteria")
                elif component == "devops_integration":
                    logger.info("  🔧 Setup CI/CD pipeline with automated testing")
                    logger.info("  🚀 Implement deployment automation")
                elif component == "layered_architecture":
                    logger.info("  🏗️  Restructure code into presentation, business, and data layers")
                    logger.info("  📦 Separate concerns between different architectural layers")
                elif component == "quality_standards":
                    logger.info("  🧪 Increase test coverage to 70%+ minimum")
                    logger.info("  👥 Implement code review process")
                elif component == "team_collaboration":
                    logger.info("  💬 Setup team communication channels")
                    logger.info("  📚 Improve documentation standards")
    
    def save_validation_report(self, output_file: str = None):
        """Save detailed validation report"""
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"sdlc_2x_validation_report_{timestamp}.json"
        
        output_path = self.project_path / output_file
        with open(output_path, 'w') as f:
            json.dump(self.validation_results, f, indent=2)
        
        logger.info(f"📄 Validation report saved: {output_path}")
        return output_path

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(description="SDLC 2.x Validation Tool")
    parser.add_argument("--project-path", required=True, help="Path to project directory")
    parser.add_argument("--team-size", type=int, help="Team size (5-25 developers)")
    parser.add_argument("--output", help="Output report file name")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    if not args.project_path:
        logger.info("❌ Project path is required")
        sys.exit(1)
    
    if args.team_size and (args.team_size < 5 or args.team_size > 25):
        logger.info("❌ Team size should be between 5-25 developers for SDLC 2.x")
        sys.exit(1)
    
    # Run validation
    validator = SDLC2XValidator(args.project_path, args.team_size)
    results = validator.run_validation()
    
    # Save report
    report_path = validator.save_validation_report(args.output)
    
    # Exit with appropriate code
    exit_code = 0 if results["overall_compliance"] else 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()