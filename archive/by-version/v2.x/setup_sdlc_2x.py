#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""
SDLC 2.x Implementation Script
=============================

This script sets up a new project using SDLC 2.x Framework for:
- Medium projects ($50K - $500K budget)
- Teams of 5-25 developers  
- Agile & DevOps Integration
- Development time: 6-18 months

Usage:
    python setup_sdlc_2x.py --project-name "MyProject" --team-size 12 --agile-framework "scrum"

Supported Frameworks:
- scrum: Scrum methodology with 2-4 week sprints
- kanban: Kanban workflow with continuous delivery
- hybrid: Hybrid Scrum-Kanban approach
"""

import argparse
import os
import subprocess
import json
import sys
import yaml
from pathlib import Path
from datetime import datetime, timedelta

class SDLC2XSetup:
    """SDLC 2.x Agile & DevOps Integration Setup"""
    
    def __init__(self, project_name: str, team_size: int, agile_framework: str = "scrum"):
        self.project_name = project_name
        self.team_size = team_size
        self.agile_framework = agile_framework
        self.project_root = Path.cwd() / project_name
        
        # SDLC 2.x Configuration
        self.config = {
            "version": "2.5",
            "target_team_size": f"{team_size} developers (5-25 range)",
            "project_scale": "$50K-$500K", 
            "development_time": "6-18 months",
            "architecture": "layered_architecture",
            "deployment": "ci_cd_automated",
            "testing_coverage": "70%",
            "agile_framework": agile_framework,
            "sprint_length": "2-4 weeks" if agile_framework == "scrum" else "continuous"
        }
    
    def create_project_structure(self):
        """Create SDLC 2.x agile-compliant directory structure"""
        logger.info(f"📁 Creating SDLC 2.x project structure for {self.project_name}...")
        
        # Agile & DevOps directories
        directories = [
            # Core development
            "src/presentation",      # Presentation layer
            "src/business-logic",    # Business logic layer  
            "src/data-access",       # Data access layer
            "src/infrastructure",    # Infrastructure layer
            
            # Testing
            "tests/unit",
            "tests/integration", 
            "tests/performance",
            "tests/acceptance",
            
            # Agile documentation
            "docs/sprints",
            "docs/user-stories", 
            "docs/acceptance-criteria",
            "docs/retrospectives",
            "docs/architecture",
            
            # DevOps
            "devops/ci-cd",
            "devops/monitoring",
            "devops/deployment",
            "devops/scripts",
            
            # Agile artifacts  
            "agile/sprint-planning",
            "agile/daily-standups",
            "agile/sprint-reviews",
            "agile/retrospectives",
            "agile/backlog",
            
            # Configuration
            "config/environments",
            "config/docker",
            "config/kubernetes"
        ]
        
        for directory in directories:
            (self.project_root / directory).mkdir(parents=True, exist_ok=True)
            
        logger.info("✅ SDLC 2.x agile structure created")
    
    def setup_agile_framework(self):
        """Setup agile framework artifacts"""
        logger.info(f"🏃‍♂️ Setting up {self.agile_framework} framework...")
        
        if self.agile_framework == "scrum":
            self._setup_scrum_framework()
        elif self.agile_framework == "kanban":
            self._setup_kanban_framework()
        elif self.agile_framework == "hybrid":
            self._setup_hybrid_framework()
    
    def _setup_scrum_framework(self):
        """Setup Scrum methodology artifacts"""
        
        # Sprint planning template
        sprint_planning = f'''# Sprint Planning Template - SDLC 2.x

## Sprint Information
- **Sprint Number**: #__
- **Sprint Goal**: ________________
- **Sprint Duration**: {self.config["sprint_length"]}
- **Team Capacity**: {self.team_size} developers
- **Start Date**: ___________
- **End Date**: ___________

## Team Roles
- **Product Owner**: ________________
- **Scrum Master**: ________________ 
- **Development Team**: {self.team_size} members

## Sprint Backlog

### High Priority Stories
| Story ID | User Story | Story Points | Acceptance Criteria | Assigned To |
|----------|------------|--------------|-------------------|-------------|
| US-001   | As a ___   | ___ pts      | - [ ] Criteria 1  | Developer   |

### Medium Priority Stories  
| Story ID | User Story | Story Points | Acceptance Criteria | Assigned To |
|----------|------------|--------------|-------------------|-------------|
| US-002   | As a ___   | ___ pts      | - [ ] Criteria 1  | Developer   |

## Definition of Done
- [ ] Code written and reviewed
- [ ] Unit tests written (>70% coverage)
- [ ] Integration tests pass
- [ ] Documentation updated
- [ ] Acceptance criteria met
- [ ] Deployed to staging environment
- [ ] Product Owner approval

## Sprint Risks & Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| ___  | Low/Med/High| Low/Med/High| _______ |

## Notes
- Sprint planning meeting: _____ (Date/Time)
- Daily standups: _____ (Time)
- Sprint review: _____ (Date/Time)
- Sprint retrospective: _____ (Date/Time)

---
Generated by SDLC 2.x Implementation Script
Framework: Scrum | Created: {datetime.now().strftime("%Y-%m-%d")}
'''
        
        with open(self.project_root / "agile/sprint-planning/sprint-template.md", "w") as f:
            f.write(sprint_planning)
        
        # Daily standup template
        daily_standup = '''# Daily Standup Template - SDLC 2.x Scrum

**Date**: ___________
**Sprint**: #___  
**Scrum Master**: ________________

## Team Updates

### [Developer Name 1]
- **Yesterday**: ________________
- **Today**: ________________  
- **Blockers**: ________________

### [Developer Name 2]  
- **Yesterday**: ________________
- **Today**: ________________
- **Blockers**: ________________

## Sprint Progress
- **Stories Completed**: ___ / ___
- **Story Points Burned**: ___ / ___
- **Days Remaining**: ___

## Action Items
- [ ] Action item 1 - Assigned to: ___
- [ ] Action item 2 - Assigned to: ___

## Notes
___________________________________________

---
Next Standup: ___________
'''
        
        with open(self.project_root / "agile/daily-standups/standup-template.md", "w") as f:
            f.write(daily_standup)
    
    def _setup_kanban_framework(self):
        """Setup Kanban methodology artifacts"""
        
        kanban_board = '''# Kanban Board Configuration - SDLC 2.x

## Board Columns
1. **Backlog** - New stories and requirements
2. **Ready** - Stories ready for development (max 3)  
3. **In Progress** - Active development (max 5)
4. **Code Review** - Peer review phase (max 2)
5. **Testing** - QA and testing phase (max 3)
6. **Done** - Completed and deployed

## Work in Progress (WIP) Limits
- Ready: 3 items
- In Progress: 5 items  
- Code Review: 2 items
- Testing: 3 items

## Kanban Metrics
- **Lead Time**: Time from request to delivery
- **Cycle Time**: Time from start to completion
- **Throughput**: Stories completed per week
- **Flow Efficiency**: Value-added time / Total lead time

## Continuous Improvement
- Weekly team review
- Monthly process optimization
- Quarterly retrospectives

---
Generated by SDLC 2.x Implementation Script
Framework: Kanban | Created: {datetime.now().strftime("%Y-%m-%d")}
'''
        
        with open(self.project_root / "agile/backlog/kanban-board.md", "w") as f:
            f.write(kanban_board)
    
    def _setup_hybrid_framework(self):
        """Setup Hybrid Scrum-Kanban framework"""
        
        hybrid_process = '''# Hybrid Scrum-Kanban Process - SDLC 2.x

## Framework Overview
Combines Scrum ceremonies with Kanban flow management for optimal team productivity.

## Scrum Elements
- **2-week Sprints**: Short iterations for planning
- **Sprint Planning**: Commitment to sprint goals
- **Daily Standups**: Team synchronization  
- **Sprint Reviews**: Stakeholder feedback
- **Retrospectives**: Continuous improvement

## Kanban Elements  
- **Continuous Flow**: No sprint boundaries for delivery
- **WIP Limits**: Prevent overloading team members
- **Visual Management**: Real-time progress tracking
- **Pull System**: Team pulls work when ready

## Hybrid Workflow
1. Sprint Planning (Every 2 weeks)
   - Plan upcoming work
   - Set sprint goal
   - No hard commitment to all planned work

2. Continuous Delivery
   - Deploy features as soon as ready
   - No waiting for sprint end
   - Immediate value delivery

3. Sprint Reviews & Retrospectives
   - Review work completed in past 2 weeks  
   - Gather stakeholder feedback
   - Improve team processes

## Metrics
- Sprint goal achievement
- Lead time and cycle time
- Throughput per sprint
- Team velocity trends

---
Generated by SDLC 2.x Implementation Script  
Framework: Hybrid | Created: {datetime.now().strftime("%Y-%m-%d")}
'''
        
        with open(self.project_root / "agile/backlog/hybrid-process.md", "w") as f:
            f.write(hybrid_process)
    
    def setup_devops_pipeline(self):
        """Setup CI/CD pipeline for SDLC 2.x"""
        logger.info("🔧 Setting up DevOps CI/CD pipeline...")
        
        # Jenkins pipeline
        jenkinsfile = '''pipeline {
    agent any
    
    environment {
        PROJECT_NAME = '${params.PROJECT_NAME}'
        ENVIRONMENT = '${params.ENVIRONMENT}'
        DOCKER_REGISTRY = 'your-registry.com'
    }
    
    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['development', 'staging', 'production'],
            description: 'Deployment environment'
        )
        string(
            name: 'PROJECT_NAME', 
            defaultValue: '%s',
            description: 'Project name'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "🚀 SDLC 2.x Pipeline Started"
            }
        }
        
        stage('Install Dependencies') {
            parallel {
                stage('Backend Dependencies') {
                    steps {
                        dir('src/business-logic') {
                            sh 'npm ci'
                        }
                    }
                }
                stage('Frontend Dependencies') {
                    steps {
                        dir('src/presentation') {
                            sh 'npm ci'
                        }
                    }
                }
            }
        }
        
        stage('Code Quality') {
            parallel {
                stage('Linting') {
                    steps {
                        sh 'npm run lint'
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'npm audit'
                    }
                }
            }
        }
        
        stage('Testing') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        dir('tests/unit') {
                            sh 'npm test -- --coverage'
                        }
                    }
                    post {
                        always {
                            publishTestResults testResultsPattern: 'tests/unit/coverage/junit.xml'
                            publishCoverage adapters: [coberturaAdapter('tests/unit/coverage/cobertura.xml')]
                        }
                    }
                }
                stage('Integration Tests') {
                    steps {
                        dir('tests/integration') {
                            sh 'npm run test:integration'
                        }
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t $DOCKER_REGISTRY/$PROJECT_NAME:$BUILD_NUMBER .'
                sh 'docker tag $DOCKER_REGISTRY/$PROJECT_NAME:$BUILD_NUMBER $DOCKER_REGISTRY/$PROJECT_NAME:latest'
            }
        }
        
        stage('Deploy') {
            when {
                anyOf {
                    branch 'main'
                    branch 'develop'
                }
            }
            steps {
                script {
                    if (params.ENVIRONMENT == 'staging') {
                        sh 'kubectl apply -f config/kubernetes/staging/'
                    } else if (params.ENVIRONMENT == 'production') {
                        input 'Deploy to production?'
                        sh 'kubectl apply -f config/kubernetes/production/'
                    }
                }
            }
        }
        
        stage('Monitoring Setup') {
            steps {
                sh 'kubectl apply -f devops/monitoring/'
                echo "📊 Monitoring dashboards deployed"
            }
        }
    }
    
    post {
        success {
            echo "🎉 SDLC 2.x Pipeline Completed Successfully"
            slackSend(
                channel: '#deployments',
                message: "✅ $PROJECT_NAME deployed to $ENVIRONMENT successfully"
            )
        }
        failure {
            echo "❌ SDLC 2.x Pipeline Failed"
            slackSend(
                channel: '#deployments', 
                message: "🚨 $PROJECT_NAME deployment to $ENVIRONMENT failed"
            )
        }
        always {
            cleanWs()
        }
    }
}
''' % self.project_name
        
        with open(self.project_root / "devops/ci-cd/Jenkinsfile", "w") as f:
            f.write(jenkinsfile)
        
        # Docker Compose for development
        docker_compose = f'''version: '3.8'

services:
  # Application
  app:
    build: 
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
      - "5000:5000"
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:password@db:5432/{self.project_name.lower()}
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - ./src:/app/src
      - /app/node_modules
    command: npm run dev

  # Database
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: {self.project_name.lower()}
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./src/data-access/migrations:/docker-entrypoint-initdb.d

  # Redis for caching and sessions
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Monitoring
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./devops/monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
      - ./devops/monitoring/grafana:/etc/grafana/provisioning

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
'''
        
        with open(self.project_root / "docker-compose.dev.yml", "w") as f:
            f.write(docker_compose)
        
        logger.info("✅ DevOps pipeline setup complete")
    
    def create_layered_architecture(self):
        """Create SDLC 2.x layered architecture structure"""
        logger.info("🏗️ Creating layered architecture...")
        
        # Presentation Layer (React + Express API)
        presentation_config = {
            "name": f"{self.project_name}-presentation",
            "version": "1.0.0", 
            "description": "SDLC 2.x Presentation Layer",
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test --coverage",
                "dev:api": "nodemon api-server.js"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-router-dom": "^6.15.0",
                "axios": "^1.5.0",
                "@mui/material": "^5.14.5",
                "express": "^4.18.2",
                "cors": "^2.8.5"
            },
            "proxy": "http://localhost:5000"
        }
        
        with open(self.project_root / "src/presentation/package.json", "w") as f:
            json.dump(presentation_config, f, indent=2)
        
        # Business Logic Layer
        business_logic_config = {
            "name": f"{self.project_name}-business-logic",
            "version": "1.0.0",
            "description": "SDLC 2.x Business Logic Layer",
            "main": "index.js",
            "scripts": {
                "start": "node index.js",
                "dev": "nodemon index.js", 
                "test": "jest --coverage"
            },
            "dependencies": {
                "express": "^4.18.2",
                "joi": "^17.9.2",
                "lodash": "^4.17.21",
                "moment": "^2.29.4"
            },
            "devDependencies": {
                "jest": "^29.6.2",
                "nodemon": "^3.0.1"
            }
        }
        
        with open(self.project_root / "src/business-logic/package.json", "w") as f:
            json.dump(business_logic_config, f, indent=2)
        
        # Data Access Layer
        data_access_config = {
            "name": f"{self.project_name}-data-access",
            "version": "1.0.0",
            "description": "SDLC 2.x Data Access Layer", 
            "main": "index.js",
            "scripts": {
                "migrate": "knex migrate:latest",
                "seed": "knex seed:run",
                "test": "jest"
            },
            "dependencies": {
                "knex": "^2.5.1",
                "pg": "^8.11.3",
                "redis": "^4.6.7"
            }
        }
        
        with open(self.project_root / "src/data-access/package.json", "w") as f:
            json.dump(data_access_config, f, indent=2)
        
        logger.info("✅ Layered architecture created")
    
    def setup_monitoring(self):
        """Setup monitoring and observability"""
        logger.info("📊 Setting up monitoring stack...")
        
        # Prometheus configuration
        prometheus_config = {
            "global": {
                "scrape_interval": "15s"
            },
            "scrape_configs": [
                {
                    "job_name": f"{self.project_name}-app",
                    "static_configs": [
                        {
                            "targets": ["app:3000", "app:5000"]
                        }
                    ]
                },
                {
                    "job_name": "postgres",
                    "static_configs": [
                        {
                            "targets": ["db:5432"]
                        }
                    ]
                }
            ]
        }
        
        with open(self.project_root / "devops/monitoring/prometheus.yml", "w") as f:
            yaml.dump(prometheus_config, f, default_flow_style=False)
        
        # Grafana dashboard
        grafana_dashboard = {
            "dashboard": {
                "id": None,
                "title": f"{self.project_name} - SDLC 2.x Dashboard",
                "tags": ["sdlc-2x", "agile", "devops"],
                "timezone": "browser",
                "panels": [
                    {
                        "id": 1,
                        "title": "Application Requests",
                        "type": "graph",
                        "targets": [
                            {
                                "expr": "rate(http_requests_total[1m])",
                                "legendFormat": "RPS"
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "title": "Sprint Progress",
                        "type": "stat",
                        "targets": [
                            {
                                "expr": "sprint_story_points_completed / sprint_story_points_planned * 100",
                                "legendFormat": "Sprint Progress %"
                            }
                        ]
                    }
                ],
                "time": {
                    "from": "now-1h",
                    "to": "now"
                },
                "refresh": "30s"
            }
        }
        
        with open(self.project_root / "devops/monitoring/grafana/dashboards/main.json", "w") as f:
            json.dump(grafana_dashboard, f, indent=2)
        
        logger.info("✅ Monitoring stack configured")
    
    def create_documentation(self):
        """Create comprehensive SDLC 2.x documentation"""
        logger.info("📚 Creating SDLC 2.x documentation...")
        
        main_readme = f'''# {self.project_name}

SDLC 2.x - Agile & DevOps Integration Framework

## Project Overview

- **Framework**: SDLC 2.x ({self.config["version"]})
- **Team Size**: {self.config["target_team_size"]}
- **Project Scale**: {self.config["project_scale"]}
- **Development Time**: {self.config["development_time"]}
- **Architecture**: {self.config["architecture"].replace("_", " ").title()}
- **Agile Framework**: {self.config["agile_framework"].title()}
- **Sprint Length**: {self.config["sprint_length"]}

## Architecture Overview

### Layered Architecture
```
┌─────────────────────────────────────┐
│        Presentation Layer           │
│     (React UI + Express API)        │
├─────────────────────────────────────┤
│       Business Logic Layer          │
│    (Core Domain & Use Cases)        │
├─────────────────────────────────────┤
│       Data Access Layer             │
│   (Database & External APIs)        │
├─────────────────────────────────────┤
│      Infrastructure Layer           │
│  (Docker, K8s, CI/CD, Monitoring)   │
└─────────────────────────────────────┘
```

## Agile Methodology

### {self.config["agile_framework"].title()} Framework
- **Sprint Duration**: {self.config["sprint_length"]}
- **Team Capacity**: {self.team_size} developers
- **Definition of Done**: >70% test coverage, code review, acceptance criteria met
- **Ceremonies**: Planning, Daily standups, Reviews, Retrospectives

### Team Roles
- **Product Owner**: Requirements and priorities
- **Scrum Master**: Process facilitation (if using Scrum)
- **Development Team**: {self.team_size} cross-functional developers

## Development Workflow

### Sprint Cycle ({self.config["agile_framework"].title()})
1. **Sprint Planning** - Plan upcoming work and set goals
2. **Daily Standups** - Team synchronization (15 min)
3. **Development** - Feature implementation with TDD
4. **Sprint Review** - Demo completed work to stakeholders  
5. **Sprint Retrospective** - Process improvement discussion

### CI/CD Pipeline
```
Code → Build → Test → Deploy → Monitor
  ↓      ↓       ↓       ↓       ↓
 Git   Docker   Jest  K8s/Docker Grafana
```

## Quick Start

### Prerequisites
- Node.js 16+
- Docker & Docker Compose
- Kubernetes (optional)
- Git

### Installation
```bash
# Clone repository
git clone <repository-url>
cd {self.project_name}

# Start development environment
docker-compose -f docker-compose.dev.yml up -d

# Install dependencies
npm run install:all

# Setup database
npm run migrate:dev

# Start development
npm run dev
```

### Development Commands
```bash
# Start all services
npm run dev

# Run tests
npm run test              # All tests
npm run test:unit         # Unit tests only
npm run test:integration  # Integration tests only
npm run test:coverage     # Coverage report

# Code quality
npm run lint             # ESLint
npm run format           # Prettier
npm run audit            # Security audit

# Database
npm run migrate:dev      # Run migrations
npm run seed:dev         # Seed test data

# Deployment
npm run build            # Production build
npm run deploy:staging   # Deploy to staging
npm run deploy:prod      # Deploy to production
```

## Project Structure

```
{self.project_name}/
├── src/
│   ├── presentation/         # UI components & API routes
│   ├── business-logic/       # Domain models & use cases
│   ├── data-access/         # Database & external integrations
│   └── infrastructure/      # DevOps & deployment configs
├── tests/
│   ├── unit/               # Unit tests (70%+ coverage)
│   ├── integration/        # API & service integration tests
│   ├── performance/        # Load & performance tests
│   └── acceptance/         # User acceptance tests
├── agile/
│   ├── sprint-planning/    # Sprint planning artifacts
│   ├── daily-standups/     # Daily standup notes
│   ├── sprint-reviews/     # Sprint review materials
│   ├── retrospectives/     # Retrospective outcomes
│   └── backlog/           # Product backlog management
├── devops/
│   ├── ci-cd/             # Jenkins, GitHub Actions
│   ├── monitoring/        # Prometheus, Grafana
│   ├── deployment/        # Kubernetes manifests
│   └── scripts/           # Automation scripts
└── docs/
    ├── sprints/           # Sprint documentation
    ├── user-stories/      # User story details
    ├── architecture/      # Technical documentation
    └── retrospectives/    # Process improvements
```

## Quality Gates

### QG1: Sprint Planning Approval ✅
- Sprint backlog defined and estimated
- Team commitment to sprint goals
- Acceptance criteria documented

### QG2: Development Standards ⏳
- Code quality standards met (ESLint)
- Minimum 70% test coverage achieved
- All tests passing

### QG3: Sprint Review ⏳
- Sprint goals achieved and demonstrated
- Working software increment delivered
- Stakeholder feedback collected

### QG4: Release Readiness ⏳
- All acceptance criteria met
- Production deployment successful
- Monitoring and alerting active

## Monitoring & Observability

### Metrics Dashboards
- **Application**: Request rates, response times, errors
- **Infrastructure**: CPU, memory, disk, network usage
- **Business**: Sprint progress, velocity, burndown
- **Quality**: Test coverage, bug rates, deployment frequency

### Access URLs
- Application: http://localhost:3000
- API: http://localhost:5000
- Grafana: http://localhost:3001 (admin/admin)
- Prometheus: http://localhost:9090

## Team Collaboration

### Communication Channels
- Daily standups: Every morning 9:00 AM
- Sprint planning: Every {self.config["sprint_length"]} 
- Sprint reviews: End of each sprint
- Retrospectives: After sprint reviews
- Slack/Teams: Async communication

### Code Review Process
1. Create feature branch from `develop`
2. Implement feature with tests
3. Submit pull request with description
4. Code review by 2+ team members
5. Merge after approval and CI pass

## Deployment

### Environments
- **Development**: Local Docker Compose
- **Staging**: Kubernetes cluster (auto-deploy from develop)
- **Production**: Kubernetes cluster (manual approval required)

### Deployment Process
1. Code merged to main branch
2. CI/CD pipeline triggered
3. Automated tests run
4. Docker image built and tagged
5. Deployment to staging (automatic)
6. Manual approval for production
7. Blue-green deployment to production
8. Post-deployment monitoring

## Troubleshooting

### Common Issues
- **Tests failing**: Check test database connection
- **Build errors**: Verify Node.js version compatibility  
- **Docker issues**: Ensure Docker daemon is running
- **Database errors**: Check PostgreSQL service status

### Support
- Documentation: `/docs` directory
- Team lead: [Contact Information]
- DevOps support: [Contact Information]
- Product Owner: [Contact Information]

---
Generated by SDLC 2.x Implementation Script
Framework Version: {self.config["version"]} | Created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Agile Framework: {self.config["agile_framework"].title()} | Team Size: {self.team_size} developers
'''
        
        with open(self.project_root / "README.md", "w") as f:
            f.write(main_readme)
        
        logger.info("✅ SDLC 2.x documentation created")
    
    def run_setup(self):
        """Execute complete SDLC 2.x setup"""
        logger.info(f"🚀 Starting SDLC 2.x setup for {self.project_name}")
        logger.info(f"📊 Configuration: {json.dumps(self.config, indent=2)}")
        
        try:
            self.create_project_structure()
            self.setup_agile_framework()  
            self.setup_devops_pipeline()
            self.create_layered_architecture()
            self.setup_monitoring()
            self.create_documentation()
            
            logger.info(f"\n🎉 SDLC 2.x project '{self.project_name}' setup complete!")
            logger.info(f"📁 Project location: {self.project_root}")
            logger.info(f"👥 Configured for {self.team_size} developers using {self.agile_framework}")
            logger.info("\n📋 Next steps:")
            logger.info("1. Start development environment: docker-compose -f docker-compose.dev.yml up")
            logger.info("2. Access application: http://localhost:3000")
            logger.info("3. Access monitoring: http://localhost:3001 (Grafana)")
            logger.info("4. Begin first sprint planning session")
            logger.info("5. Setup team communication channels")
            logger.info("6. Configure CI/CD pipeline with your repository")
            
            # Create setup summary
            summary = {
                "project_name": self.project_name,
                "team_size": self.team_size,
                "agile_framework": self.agile_framework,
                "framework": "SDLC 2.x",
                "created_at": datetime.now().isoformat(),
                "configuration": self.config,
                "next_sprint_planning": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            }
            
            with open(self.project_root / "sdlc_setup.json", "w") as f:
                json.dump(summary, f, indent=2)
                
        except Exception as e:
            logger.info(f"❌ Setup failed: {str(e)}")
            sys.exit(1)

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(description="SDLC 2.x Implementation Script")
    parser.add_argument("--project-name", required=True, help="Project name")
    parser.add_argument("--team-size", type=int, required=True, help="Team size (5-25 developers)")
    parser.add_argument("--agile-framework", choices=["scrum", "kanban", "hybrid"],
                       default="scrum", help="Agile methodology framework")
    
    args = parser.parse_args()
    
    # Validation
    if not args.project_name:
        logger.info("❌ Project name is required")
        sys.exit(1)
        
    if args.team_size < 5 or args.team_size > 25:
        logger.info("❌ Team size must be between 5-25 developers for SDLC 2.x")
        sys.exit(1)
    
    # Initialize and run setup
    setup = SDLC2XSetup(args.project_name, args.team_size, args.agile_framework)
    setup.run_setup()

if __name__ == "__main__":
    main()