# MentorScript (MTS) Template
## SASE Artifact for SE 3.0 SDLC Integration

**Reference:** arXiv:2509.06216v2 - Software Agentic Software Engineering

**Purpose:** Project-specific guidelines, coding standards, and best practices for AI agents
**Author:** SE4H (Software Engineering for Humans - Agent Coach)
**Consumer:** SE4A (Software Engineering for Agents - Agent Executor)

**Version:** 1.0.0
**Framework:** SDLC 5.1.0
**Created:** December 2025

---

## 📋 METADATA

| Field | Value |
|-------|-------|
| **Artifact Type** | MentorScript |
| **Artifact ID** | MTS-YYYY-NNN (e.g., MTS-2026-001) |
| **Project** | [Project Name] |
| **Version** | 1.0.0 |
| **Status** | DRAFT \| ACTIVE \| DEPRECATED |
| **Created Date** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Owner** | [Tech Lead / Architect Name] |

---

## 🎯 PURPOSE

This MentorScript provides project-specific guidance for AI agents (SE4A) working on [Project Name]. It encodes the team's collective wisdom, coding standards, and architectural decisions to ensure consistent, high-quality output.

**Scope:**
- [x] Coding standards and conventions
- [x] Architectural patterns to follow
- [x] Security requirements
- [x] Testing expectations
- [x] Documentation standards
- [x] Common pitfalls to avoid

---

## 🏗️ ARCHITECTURE GUIDELINES

### Technology Stack

```yaml
Backend:
  Language: Python 3.11+
  Framework: FastAPI 0.104+
  Database: PostgreSQL 15.5
  Cache: Redis 7.2
  ORM: SQLAlchemy 2.0 (async)
  Migrations: Alembic 1.12+

Frontend:
  Language: TypeScript 5.0+
  Framework: React 18
  State: Zustand
  UI: shadcn/ui + Tailwind CSS
  Data: TanStack Query v5

DevOps:
  Container: Docker + Docker Compose
  CI/CD: GitHub Actions
  Monitoring: Prometheus + Grafana
```

### Architectural Patterns

#### 1. Service-Repository Pattern (MANDATORY)

```python
# CORRECT: Service depends on Repository
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_user(self, user_id: UUID) -> User:
        return await self.repository.get_by_id(user_id)

# INCORRECT: Direct database access in service
class UserService:
    async def get_user(self, user_id: UUID) -> User:
        # DON'T: Direct DB query in service
        return await db.query(User).filter_by(id=user_id).first()
```

#### 2. Dependency Injection (MANDATORY)

```python
# CORRECT: Using FastAPI Depends
@router.get("/users/{user_id}")
async def get_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service)
) -> UserResponse:
    return await service.get_user(user_id)

# INCORRECT: Hard-coded dependencies
@router.get("/users/{user_id}")
async def get_user(user_id: UUID) -> UserResponse:
    # DON'T: Instantiate service directly
    service = UserService(UserRepository(db))
    return await service.get_user(user_id)
```

#### 3. AGPL Containment (CRITICAL)

```python
# CORRECT: Network-only access to AGPL components
import requests

async def upload_to_minio(file_path: str, bucket: str) -> str:
    """Upload via S3 API (network-only, AGPL-safe)"""
    response = requests.put(
        f"http://minio:9000/{bucket}/{object_name}",
        data=open(file_path, 'rb')
    )
    return f"s3://{bucket}/{object_name}"

# INCORRECT: Importing AGPL library
from minio import Minio  # BANNED - AGPL contamination
client = Minio("localhost:9000")
```

---

## 📝 CODING STANDARDS

### Python Style Guide

#### File Naming
- Use `snake_case` for all Python files
- Maximum 50 characters (excluding `.py`)
- Examples: `user_service.py`, `customer_repository.py`

#### Class Naming
- Use `PascalCase` for classes
- Suffix with type: `Service`, `Repository`, `Model`, `Schema`
- Examples: `UserService`, `ProjectRepository`, `GateModel`

#### Function/Method Naming
- Use `snake_case` for functions
- Use verbs: `get_`, `create_`, `update_`, `delete_`, `validate_`
- Examples: `get_user_by_id`, `create_project`, `validate_gate_status`

#### Type Hints (MANDATORY)

```python
# CORRECT: Full type hints
async def get_user(
    user_id: UUID,
    include_deleted: bool = False
) -> User | None:
    ...

# INCORRECT: Missing type hints
async def get_user(user_id, include_deleted=False):
    ...
```

#### Docstrings (MANDATORY - Google Style)

```python
async def create_gate_evaluation(
    project_id: UUID,
    gate_id: str,
    evidence: list[Evidence]
) -> GateEvaluation:
    """
    Evaluate a project's readiness for a specific gate.

    Args:
        project_id: UUID of the project to evaluate
        gate_id: Gate identifier (e.g., "G0.1", "G1", "G2")
        evidence: List of evidence items to evaluate

    Returns:
        GateEvaluation result with pass/fail status and details

    Raises:
        ProjectNotFoundError: If project does not exist
        InvalidGateError: If gate_id is not recognized
        InsufficientEvidenceError: If required evidence is missing

    Example:
        >>> evaluation = await create_gate_evaluation(
        ...     project_id=UUID("..."),
        ...     gate_id="G1",
        ...     evidence=[legal_doc, market_analysis]
        ... )
        >>> print(evaluation.status)
        GateStatus.PASSED
    """
```

### TypeScript Style Guide

#### File Naming
- Use `camelCase` for regular files: `userService.ts`
- Use `PascalCase` for React components: `UserProfile.tsx`
- Maximum 50 characters

#### Component Structure

```typescript
// CORRECT: Functional component with proper typing
interface UserProfileProps {
  userId: string;
  showDetails?: boolean;
}

export function UserProfile({ userId, showDetails = false }: UserProfileProps) {
  const { data: user, isLoading } = useUser(userId);

  if (isLoading) return <Skeleton />;
  if (!user) return <NotFound />;

  return (
    <div className="p-4">
      <h1>{user.name}</h1>
      {showDetails && <UserDetails user={user} />}
    </div>
  );
}
```

---

## 🔒 SECURITY REQUIREMENTS

### Authentication & Authorization

```python
# MANDATORY: All API endpoints must be protected
@router.get("/projects/{project_id}")
async def get_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),  # Auth required
    project_access: ProjectAccess = Depends(check_project_access)  # Authz
) -> ProjectResponse:
    ...
```

### Input Validation

```python
# MANDATORY: Use Pydantic for all input validation
class CreateProjectRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., max_length=500)
    team_id: UUID

    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip()
```

### SQL Injection Prevention

```python
# CORRECT: Parameterized queries (SQLAlchemy handles this)
result = await db.execute(
    select(User).where(User.email == email)
)

# INCORRECT: String interpolation
result = await db.execute(
    f"SELECT * FROM users WHERE email = '{email}'"  # VULNERABLE
)
```

### Secret Handling

```python
# CORRECT: Use environment variables
import os
api_key = os.environ.get("API_KEY")

# INCORRECT: Hardcoded secrets
api_key = "sk-ant-api03-xxxxx"  # NEVER DO THIS
```

---

## 🧪 TESTING EXPECTATIONS

### Unit Test Requirements

```python
# File: tests/test_user_service.py
import pytest
from unittest.mock import AsyncMock

class TestUserService:
    """Tests for UserService"""

    @pytest.fixture
    def mock_repository(self):
        return AsyncMock(spec=UserRepository)

    @pytest.fixture
    def service(self, mock_repository):
        return UserService(repository=mock_repository)

    # Happy path
    async def test_get_user_success(self, service, mock_repository):
        """Should return user when found"""
        expected_user = User(id=UUID("..."), name="Test")
        mock_repository.get_by_id.return_value = expected_user

        result = await service.get_user(expected_user.id)

        assert result == expected_user
        mock_repository.get_by_id.assert_called_once_with(expected_user.id)

    # Error case
    async def test_get_user_not_found(self, service, mock_repository):
        """Should return None when user not found"""
        mock_repository.get_by_id.return_value = None

        result = await service.get_user(UUID("non-existent"))

        assert result is None

    # Edge case
    async def test_get_user_with_invalid_uuid(self, service):
        """Should raise ValueError for invalid UUID"""
        with pytest.raises(ValueError):
            await service.get_user("not-a-uuid")
```

### Coverage Requirements

| Component | Minimum Coverage |
|-----------|------------------|
| Services | 95% |
| Repositories | 90% |
| API Endpoints | 85% |
| Utilities | 80% |
| **Overall** | **90%** |

---

## 📚 DOCUMENTATION STANDARDS

### Code Comments

```python
# GOOD: Explain WHY, not WHAT
# Use bcrypt with cost=12 to balance security and performance
# Lower cost is faster but less secure, higher cost increases login latency
password_hash = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))

# BAD: Stating the obvious
# Hash the password
password_hash = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
```

### API Documentation

```python
@router.post(
    "/projects",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new project",
    description="""
    Creates a new project with the given details.

    **Required permissions:** `projects:create`

    **Rate limit:** 10 requests per minute
    """,
    responses={
        201: {"description": "Project created successfully"},
        400: {"description": "Invalid input data"},
        403: {"description": "Insufficient permissions"},
        409: {"description": "Project with this name already exists"},
    }
)
async def create_project(...):
    ...
```

---

## ⚠️ COMMON PITFALLS TO AVOID

### 1. Synchronous Blocking Calls

```python
# WRONG: Blocking call in async context
async def fetch_data():
    response = requests.get(url)  # BLOCKS event loop!
    return response.json()

# CORRECT: Use async HTTP client
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
```

### 2. N+1 Query Problem

```python
# WRONG: N+1 queries
users = await db.execute(select(User))
for user in users:
    projects = await db.execute(
        select(Project).where(Project.user_id == user.id)
    )  # Query for each user!

# CORRECT: Eager loading
users = await db.execute(
    select(User).options(selectinload(User.projects))
)
```

### 3. Missing Error Handling

```python
# WRONG: No error handling
async def process_file(file_path: str):
    with open(file_path) as f:
        return f.read()

# CORRECT: Proper error handling
async def process_file(file_path: str) -> str:
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {file_path}")
    except PermissionError:
        raise FileProcessingError(f"Permission denied: {file_path}")
```

### 4. Ignoring Edge Cases

```python
# WRONG: No null check
def get_user_name(user: User) -> str:
    return user.profile.display_name

# CORRECT: Handle null/missing data
def get_user_name(user: User) -> str:
    if not user.profile:
        return user.email  # Fallback
    return user.profile.display_name or user.email
```

---

## 🔄 COMMIT MESSAGE CONVENTIONS

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code refactoring |
| `test` | Adding/updating tests |
| `docs` | Documentation changes |
| `chore` | Maintenance tasks |
| `perf` | Performance improvements |
| `security` | Security fixes |

### Examples

```
feat(gates): Add G2 design ready gate evaluation

- Implement G2 gate checker with design document validation
- Add evidence requirement for design review sign-off
- Include automated architecture diagram verification

Closes #123

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

---

## 📖 REFERENCE DOCUMENTS

| Document | Purpose | Location |
|----------|---------|----------|
| ADR-001 | 4-Layer Architecture | `docs/02-Design-Architecture/03-ADRs/` |
| ADR-007 | AI Context Engine | `docs/02-Design-Architecture/03-ADRs/` |
| OpenAPI Spec | API Contracts | `docs/02-Design-Architecture/openapi.yml` |
| Security Baseline | OWASP ASVS L2 | `docs/02-Design-Architecture/Security-Baseline.md` |
| SDLC-Agentic-Core-Principles | SE4H/SE4A Framework | `02-Core-Methodology/` |

---

## 📝 REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | [Author] | Initial version |

---

## 🏷️ TEMPLATE USAGE NOTES

**MentorScript Maintenance:**
- Update when architectural decisions change
- Review quarterly for accuracy
- Version control all changes

**SE4A Usage:**
- Reference before starting any BRS execution
- Follow patterns exactly unless CRP requests deviation
- Report conflicting guidance via CRP

**SE4H Responsibility:**
- Keep MentorScript current
- Resolve conflicting guidance promptly
- Train new team members on project standards

**Reference:** SDLC-Agentic-Core-Principles.md
