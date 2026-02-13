#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""
SDLC 1.x Implementation Script
=============================

This script sets up a new project using SDLC 1.x Framework for:
- Small projects ($10K - $100K budget)
- Teams of 2-10 developers
- MVP and rapid prototyping
- Development time: 1-6 months

Usage:
    python setup_sdlc_1x.py --project-name "MyProject" --stack "react-node"

Supported Stacks:
- react-node: React + Node.js + PostgreSQL
- vue-python: Vue.js + Django/FastAPI + PostgreSQL  
- simple-php: HTML/CSS/JS + Laravel/CI + MySQL
"""

import argparse
import os
import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime

class SDLC1XSetup:
    """SDLC 1.x Project Setup Implementation"""
    
    def __init__(self, project_name: str, stack: str, database: str = "postgresql"):
        self.project_name = project_name
        self.stack = stack
        self.database = database
        self.project_root = Path.cwd() / project_name
        
        # SDLC 1.x Configuration
        self.config = {
            "version": "1.0",
            "target_team_size": "2-10 developers",
            "project_scale": "$10K-$100K",
            "development_time": "1-6 months",
            "architecture": "monolithic",
            "deployment": "single-server",
            "testing_coverage": "60%"
        }
    
    def create_project_structure(self):
        """Create SDLC 1.x compliant directory structure"""
        logger.info(f"📁 Creating SDLC 1.x project structure for {self.project_name}...")
        
        # Core directories
        directories = [
            "src",
            "src/backend",
            "src/frontend", 
            "src/database",
            "tests",
            "tests/unit",
            "tests/integration",
            "docs",
            "config",
            "scripts",
            ".github/workflows"  # Basic CI/CD
        ]
        
        for directory in directories:
            (self.project_root / directory).mkdir(parents=True, exist_ok=True)
            
        logger.info("✅ Project structure created")
    
    def setup_stack(self):
        """Setup technology stack based on selection"""
        if self.stack == "react-node":
            self._setup_react_node_stack()
        elif self.stack == "vue-python":
            self._setup_vue_python_stack()
        elif self.stack == "simple-php":
            self._setup_simple_php_stack()
        else:
            raise ValueError(f"Unsupported stack: {self.stack}")
    
    def _setup_react_node_stack(self):
        """Setup React + Node.js + PostgreSQL stack"""
        logger.info("🚀 Setting up React + Node.js stack...")
        
        # Backend package.json
        backend_package = {
            "name": f"{self.project_name}-backend",
            "version": "1.0.0",
            "description": "SDLC 1.x Backend API",
            "main": "server.js",
            "scripts": {
                "start": "node server.js",
                "dev": "nodemon server.js",
                "test": "jest",
                "test:coverage": "jest --coverage"
            },
            "dependencies": {
                "express": "^4.18.2",
                "cors": "^2.8.5",
                "helmet": "^7.0.0",
                "dotenv": "^16.3.1",
                "pg": "^8.11.3",
                "jsonwebtoken": "^9.0.2",
                "bcrypt": "^5.1.0",
                "joi": "^17.9.2"
            },
            "devDependencies": {
                "nodemon": "^3.0.1",
                "jest": "^29.6.2",
                "supertest": "^6.3.3"
            }
        }
        
        # Frontend package.json
        frontend_package = {
            "name": f"{self.project_name}-frontend",
            "version": "1.0.0",
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test",
                "eject": "react-scripts eject"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-router-dom": "^6.15.0",
                "axios": "^1.5.0",
                "@mui/material": "^5.14.5",
                "@emotion/react": "^11.11.1",
                "@emotion/styled": "^11.11.0"
            },
            "devDependencies": {
                "react-scripts": "5.0.1",
                "@testing-library/react": "^13.4.0",
                "@testing-library/jest-dom": "^5.17.0"
            },
            "proxy": "http://localhost:5000"
        }
        
        # Write package.json files
        with open(self.project_root / "src/backend/package.json", "w") as f:
            json.dump(backend_package, f, indent=2)
            
        with open(self.project_root / "src/frontend/package.json", "w") as f:
            json.dump(frontend_package, f, indent=2)
        
        # Create basic server.js
        server_js = '''const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ 
    status: 'OK', 
    version: '1.0.0',
    framework: 'SDLC 1.x'
  });
});

// API routes
app.use('/api/auth', require('./routes/auth'));
app.use('/api/users', require('./routes/users'));

app.listen(PORT, () => {
  console.log(`🚀 SDLC 1.x Server running on port ${PORT}`);
});

module.exports = app;
'''
        
        with open(self.project_root / "src/backend/server.js", "w") as f:
            f.write(server_js)
        
        logger.info("✅ React + Node.js stack setup complete")
    
    def _setup_vue_python_stack(self):
        """Setup Vue.js + Python (Django/FastAPI) stack"""
        logger.info("🐍 Setting up Vue.js + Python stack...")
        
        # requirements.txt for Python backend
        requirements = '''# SDLC 1.x Python Backend Dependencies
fastapi==0.103.1
uvicorn[standard]==0.23.2
sqlalchemy==2.0.20
psycopg2-binary==2.9.7
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
python-dotenv==1.0.0
pydantic==2.3.0

# Development
pytest==7.4.0
pytest-asyncio==0.21.1
black==23.7.0
flake8==6.0.0
'''
        
        with open(self.project_root / "src/backend/requirements.txt", "w") as f:
            f.write(requirements)
        
        # Vue.js package.json
        vue_package = {
            "name": f"{self.project_name}-frontend",
            "version": "1.0.0",
            "scripts": {
                "serve": "vue-cli-service serve",
                "build": "vue-cli-service build",
                "test:unit": "vue-cli-service test:unit",
                "lint": "vue-cli-service lint"
            },
            "dependencies": {
                "vue": "^3.3.4",
                "vue-router": "^4.2.4",
                "vuex": "^4.1.0",
                "axios": "^1.5.0",
                "vuetify": "^3.3.15"
            },
            "devDependencies": {
                "@vue/cli-service": "^5.0.8",
                "@vue/test-utils": "^2.4.1",
                "jest": "^29.6.2"
            }
        }
        
        with open(self.project_root / "src/frontend/package.json", "w") as f:
            json.dump(vue_package, f, indent=2)
        
        logger.info("✅ Vue.js + Python stack setup complete")
    
    def _setup_simple_php_stack(self):
        """Setup HTML/CSS/JS + PHP stack"""
        logger.info("🌐 Setting up Simple PHP stack...")
        
        # composer.json for PHP
        composer_json = {
            "name": f"{self.project_name.lower()}/app",
            "description": "SDLC 1.x PHP Application",
            "type": "project",
            "require": {
                "php": ">=8.1",
                "laravel/framework": "^10.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "autoload": {
                "psr-4": {
                    "App\\": "src/"
                }
            }
        }
        
        with open(self.project_root / "src/backend/composer.json", "w") as f:
            json.dump(composer_json, f, indent=2)
        
        logger.info("✅ Simple PHP stack setup complete")
    
    def create_database_schema(self):
        """Create basic database schema for SDLC 1.x"""
        logger.info("🗄️  Creating database schema...")
        
        if self.database == "postgresql":
            schema_sql = '''-- SDLC 1.x Database Schema
-- Created: {timestamp}

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Basic audit trigger
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();

-- Create indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
'''.format(timestamp=datetime.now().isoformat())
        
        elif self.database == "mysql":
            schema_sql = '''-- SDLC 1.x MySQL Schema
-- Created: {timestamp}

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
'''.format(timestamp=datetime.now().isoformat())
        
        with open(self.project_root / "src/database/schema.sql", "w") as f:
            f.write(schema_sql)
        
        logger.info("✅ Database schema created")
    
    def create_configuration_files(self):
        """Create SDLC 1.x configuration files"""
        logger.info("⚙️  Creating configuration files...")
        
        # Environment file
        env_content = f'''# SDLC 1.x Environment Configuration
# Project: {self.project_name}
# Created: {datetime.now().isoformat()}

NODE_ENV=development
PORT=5000

# Database
DATABASE_URL=postgresql://username:password@localhost:5432/{self.project_name.lower()}
DB_HOST=localhost
DB_PORT=5432
DB_NAME={self.project_name.lower()}
DB_USER=username
DB_PASSWORD=password

# JWT
JWT_SECRET=your-super-secret-jwt-key-change-this
JWT_EXPIRE=7d

# API Settings
API_VERSION=v1
API_BASE_URL=http://localhost:5000/api

# Frontend
REACT_APP_API_URL=http://localhost:5000/api
'''
        
        with open(self.project_root / ".env.example", "w") as f:
            f.write(env_content)
        
        # Docker configuration for development
        dockerfile = '''FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:5000/api/health || exit 1

# Start application
CMD ["npm", "start"]
'''
        
        with open(self.project_root / "Dockerfile", "w") as f:
            f.write(dockerfile)
        
        # Basic CI/CD workflow
        github_workflow = '''name: SDLC 1.x CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
        cache-dependency-path: src/backend/package-lock.json
    
    - name: Install backend dependencies
      run: |
        cd src/backend
        npm ci
    
    - name: Run backend tests
      run: |
        cd src/backend
        npm run test:coverage
    
    - name: Install frontend dependencies
      run: |
        cd src/frontend
        npm ci
    
    - name: Run frontend tests
      run: |
        cd src/frontend
        npm test -- --coverage --watchAll=false
    
    - name: Build application
      run: |
        cd src/frontend
        npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - name: Deploy to staging
      run: echo "Deploy to staging server"
'''
        
        with open(self.project_root / ".github/workflows/ci-cd.yml", "w") as f:
            f.write(github_workflow)
        
        logger.info("✅ Configuration files created")
    
    def create_documentation(self):
        """Create SDLC 1.x documentation"""
        logger.info("📚 Creating project documentation...")
        
        readme_content = f'''# {self.project_name}

SDLC 1.x Framework Implementation

## Project Overview

- **Framework**: SDLC 1.x (Foundational Development)
- **Team Size**: {self.config["target_team_size"]}
- **Project Scale**: {self.config["project_scale"]}
- **Development Time**: {self.config["development_time"]}
- **Architecture**: {self.config["architecture"].title()}
- **Stack**: {self.stack}

## Quick Start

### Prerequisites
- Node.js 18+ (for React/Node stack)
- PostgreSQL 15+ (database)
- Git

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd {self.project_name}
```

2. Setup environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Install dependencies
```bash
# Backend
cd src/backend
npm install

# Frontend
cd ../frontend
npm install
```

4. Setup database
```bash
# Create database
createdb {self.project_name.lower()}

# Run migrations
psql -d {self.project_name.lower()} -f src/database/schema.sql
```

5. Start development servers
```bash
# Backend (Terminal 1)
cd src/backend
npm run dev

# Frontend (Terminal 2)
cd src/frontend
npm start
```

## Project Structure

```
{self.project_name}/
├── src/
│   ├── backend/          # Backend API
│   ├── frontend/         # Frontend UI
│   └── database/         # Database schemas
├── tests/
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
├── docs/                # Documentation
├── config/              # Configuration files
└── scripts/             # Utility scripts
```

## Development Workflow

### Daily Workflow
1. Morning standup (15 min)
2. Development work (6-7 hours)
3. End of day commit and update

### Testing
```bash
# Backend tests
cd src/backend
npm test

# Frontend tests  
cd src/frontend
npm test
```

### Quality Gates

- **QG1**: Requirements documented ✅
- **QG2**: Technical foundation established ✅
- **QG3**: Core functionality implemented ⏳
- **QG4**: Production ready ⏳

## Deployment

### Development
```bash
docker build -t {self.project_name.lower()}:dev .
docker run -p 5000:5000 {self.project_name.lower()}:dev
```

### Production
See deployment guide in `docs/deployment.md`

## Contributing

1. Create feature branch from `develop`
2. Implement changes with tests
3. Submit pull request
4. Code review and merge

## License

Copyright © {datetime.now().year} {self.project_name}. All rights reserved.

---
Generated by SDLC 1.x Implementation Script
Framework Version: {self.config["version"]}
Created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
'''
        
        with open(self.project_root / "README.md", "w") as f:
            f.write(readme_content)
        
        logger.info("✅ Documentation created")
    
    def create_test_files(self):
        """Create basic test structure for SDLC 1.x"""
        logger.info("🧪 Creating test files...")
        
        # Backend test example
        backend_test = '''const request = require('supertest');
const app = require('../server');

describe('SDLC 1.x Backend Tests', () => {
  test('Health check endpoint', async () => {
    const response = await request(app)
      .get('/api/health')
      .expect(200);
    
    expect(response.body.status).toBe('OK');
    expect(response.body.framework).toBe('SDLC 1.x');
  });
  
  test('API versioning', async () => {
    const response = await request(app)
      .get('/api/health')
      .expect(200);
    
    expect(response.body.version).toBe('1.0.0');
  });
});
'''
        
        with open(self.project_root / "tests/unit/backend_test.js", "w") as f:
            f.write(backend_test)
        
        # Jest configuration
        jest_config = {
            "testEnvironment": "node",
            "collectCoverageFrom": [
                "src/**/*.js",
                "!src/**/*.test.js"
            ],
            "coverageThreshold": {
                "global": {
                    "branches": 60,
                    "functions": 60,
                    "lines": 60,
                    "statements": 60
                }
            }
        }
        
        with open(self.project_root / "jest.config.json", "w") as f:
            json.dump(jest_config, f, indent=2)
        
        logger.info("✅ Test files created")
    
    def run_setup(self):
        """Execute complete SDLC 1.x setup"""
        logger.info(f"🚀 Starting SDLC 1.x setup for {self.project_name}")
        logger.info(f"📊 Configuration: {json.dumps(self.config, indent=2)}")
        
        try:
            self.create_project_structure()
            self.setup_stack()
            self.create_database_schema()
            self.create_configuration_files()
            self.create_documentation()
            self.create_test_files()
            
            logger.info(f"\n🎉 SDLC 1.x project '{self.project_name}' setup complete!")
            logger.info(f"📁 Project location: {self.project_root}")
            logger.info("\n📋 Next steps:")
            logger.info("1. Edit .env file with your configuration")
            logger.info("2. Setup database and run migrations")
            logger.info("3. Install dependencies: npm install")
            logger.info("4. Start development: npm run dev")
            logger.info("5. Begin implementing your MVP features")
            
            # Create setup summary
            summary = {
                "project_name": self.project_name,
                "stack": self.stack,
                "database": self.database,
                "framework": "SDLC 1.x",
                "created_at": datetime.now().isoformat(),
                "configuration": self.config
            }
            
            with open(self.project_root / "sdlc_setup.json", "w") as f:
                json.dump(summary, f, indent=2)
            
        except Exception as e:
            logger.info(f"❌ Setup failed: {str(e)}")
            sys.exit(1)

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(description="SDLC 1.x Implementation Script")
    parser.add_argument("--project-name", required=True, help="Project name")
    parser.add_argument("--stack", choices=["react-node", "vue-python", "simple-php"], 
                       default="react-node", help="Technology stack")
    parser.add_argument("--database", choices=["postgresql", "mysql"], 
                       default="postgresql", help="Database system")
    
    args = parser.parse_args()
    
    if not args.project_name:
        logger.info("❌ Project name is required")
        sys.exit(1)
    
    # Initialize and run setup
    setup = SDLC1XSetup(args.project_name, args.stack, args.database)
    setup.run_setup()

if __name__ == "__main__":
    main()