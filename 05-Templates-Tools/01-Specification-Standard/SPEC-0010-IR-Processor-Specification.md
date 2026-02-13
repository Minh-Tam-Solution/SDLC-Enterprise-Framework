# SPEC-0010: IR Processor Specification

## Frontmatter

```yaml
spec_id: SPEC-0010
title: IR Processor Technical Specification - EP-06 Backend Scaffold Generation
version: 1.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 4 - Build & Implementation
owner: Backend Lead + CTO
last_updated: 2026-02-03
tags:
  - ir-processor
  - ep-06
  - backend-scaffold
  - blueprint
related_specs:
  - SPEC-0006  # Multi-Provider Codegen
  - SPEC-0020  # Quality Gates Codegen
epic: EP-06 IR-Based Codegen Engine
sprint: Sprint 46
```

---

## 1. Overview

### 1.1 Purpose

This specification defines the IR (Intermediate Representation) Processor system that transforms validated IR schemas into deterministic backend code scaffolds for Vietnamese SME applications.

**Target Domains**: F&B (restaurants, cafes), E-commerce (retail), HRM (human resources)

### 1.2 Scope

| In Scope | Out of Scope |
|----------|--------------|
| IR validation against JSON schemas | Frontend/React generation |
| Backend scaffold generation (FastAPI) | One-click deployment |
| SQLAlchemy model generation | DeepCode integration (Sprint 50) |
| Pydantic schema generation | Complex business logic |
| Alembic migration generation | Authentication/Authorization |
| Minimal CRUD endpoint generation | Production optimization |

### 1.3 Context

**Dependency Chain**:
```
Sprint 45: CodegenProvider + Multi-Provider Gateway
    ↓
Sprint 46: IR Processor (THIS SPEC)
    ↓
Sprint 47: Vietnamese Domain Templates
    ↓
Sprint 48: 4-Gate Quality Pipeline
```

**Integration Points**:
- Input: AppBlueprint JSON from `/codegen/generate` API
- Output: GeneratedBundle with 10-15 files (models, schemas, routes, migrations)
- Provider: Deterministic (no AI, pure template instantiation)

---

## 2. Functional Requirements

### FR-001: IR Validation Against JSON Schemas

**Description**: Validate AppBlueprint JSON against structured schemas before code generation.

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-001.1 | AppBlueprint JSON validated against `app_blueprint.schema.json` | Unit test with valid/invalid blueprints | ALL |
| AC-001.2 | ModuleSpec validated (name pattern: `^[a-z][a-z0-9_]*$`) | Schema validation test | ALL |
| AC-001.3 | DataModelSpec validated (entity name PascalCase) | Schema validation test | ALL |
| AC-001.4 | FieldSpec validated (type enum: string/text/integer/float/boolean/datetime/date/uuid/json) | Schema validation test | ALL |
| AC-001.5 | Validation errors returned with JSON path + error message | Integration test | ALL |
| AC-001.6 | Normalized IR returned with defaults applied | Unit test | ALL |

**BDD Scenario**:
```gherkin
GIVEN an AppBlueprint JSON with name "Restaurant Order System"
  AND modules containing entity "Order" with fields
WHEN IRValidator.validate_app_blueprint() is called
THEN validation.valid returns True
  AND normalized_ir contains default database config
  AND all entities have generated table_name (snake_case + plural)
```

---

### FR-002: Project Scaffold Generation

**Description**: Generate FastAPI project structure (main.py, config.py, requirements.txt, docker-compose.yml).

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-002.1 | `app/main.py` generated with FastAPI app + CORS middleware | Code generation test | ALL |
| AC-002.2 | `app/core/config.py` generated with database connection settings | Code generation test | ALL |
| AC-002.3 | `requirements.txt` generated with FastAPI 0.104.1, SQLAlchemy 2.0.23, asyncpg | File content test | ALL |
| AC-002.4 | `docker-compose.yml` generated with PostgreSQL service | YAML validation test | PRO, ENT |
| AC-002.5 | `Dockerfile` generated with Python 3.11+ base image | Dockerfile syntax test | PRO, ENT |
| AC-002.6 | Health check endpoint `/health` included in main.py | Integration test | ALL |

**BDD Scenario**:
```gherkin
GIVEN an IR with app_name "Restaurant Order System"
  AND database config {"type": "postgresql", "name": "restaurant_db"}
WHEN ProjectProcessor.process() is called
THEN 5 files generated (main.py, config.py, requirements.txt, docker-compose.yml, Dockerfile)
  AND main.py contains FastAPI app with title "Restaurant Order System"
  AND docker-compose.yml contains PostgreSQL service with POSTGRES_DB=restaurant_db
```

---

### FR-003: SQLAlchemy Model Generation

**Description**: Generate SQLAlchemy ORM models from DataModelSpec entities.

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-003.1 | One model file generated per entity (`app/models/{entity}.py`) | File count test | ALL |
| AC-003.2 | Base model generated with `TimestampMixin` (created_at, updated_at) | Code inspection test | ALL |
| AC-003.3 | UUID primary key generated for all entities | Model attribute test | ALL |
| AC-003.4 | IR type mapping applied (string → String, integer → Integer, etc.) | Type mapping test | ALL |
| AC-003.5 | Field constraints applied (nullable, unique, indexed, max_length) | SQLAlchemy column test | ALL |
| AC-003.6 | `__init__.py` generated with all model imports | Import test | ALL |

**Type Mapping Table**:

| IR Type | SQLAlchemy Type | Python Type | Constraints |
|---------|-----------------|-------------|-------------|
| string | String | str | max_length optional |
| text | Text | str | No length limit |
| integer | Integer | int | - |
| float | Float | float | - |
| boolean | Boolean | bool | - |
| datetime | DateTime | datetime | - |
| date | Date | date | - |
| uuid | UUID | UUID | PostgreSQL dialect |
| json | JSON | dict | - |

**BDD Scenario**:
```gherkin
GIVEN an entity "Order" with fields:
  | name         | type     | required | unique |
  | table_number | integer  | true     | false  |
  | status       | string   | true     | false  |
  | total        | float    | false    | false  |
WHEN ModelProcessor.process() is called
THEN `app/models/order.py` generated with class Order(Base, TimestampMixin)
  AND table_number mapped to Integer(nullable=False)
  AND status mapped to String(nullable=False)
  AND total mapped to Float(nullable=True)
```

---

### FR-004: Pydantic Schema Generation

**Description**: Generate Pydantic schemas for request/response validation.

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-004.1 | Three schemas generated per entity (Create, Read, Update) | File content test | ALL |
| AC-004.2 | `{Entity}Base` schema with shared fields | Pydantic model test | ALL |
| AC-004.3 | `{Entity}Create` inherits from Base | Inheritance test | ALL |
| AC-004.4 | `{Entity}Update` has all fields Optional | Field type test | ALL |
| AC-004.5 | `{Entity}Read` includes id, created_at, updated_at | Read schema test | ALL |
| AC-004.6 | `Config.from_attributes = True` for ORM compatibility | Config test | ALL |

**BDD Scenario**:
```gherkin
GIVEN an entity "Order" with fields table_number (integer), status (string)
WHEN ModelProcessor.process() is called
THEN `app/schemas/order.py` generated
  AND OrderBase has table_number: int, status: str
  AND OrderCreate inherits OrderBase
  AND OrderUpdate has table_number: Optional[int], status: Optional[str]
  AND OrderRead has id: UUID, created_at: datetime, updated_at: datetime
```

---

### FR-005: CRUD Endpoint Generation

**Description**: Generate FastAPI CRUD routes for each module with configurable operations.

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-005.1 | One route file per module (`app/api/routes/{module}.py`) | File count test | ALL |
| AC-005.2 | Operations filtered by module.operations array | Endpoint count test | ALL |
| AC-005.3 | POST /{entities} endpoint if "create" in operations | Route test | ALL |
| AC-005.4 | GET /{entities} endpoint if "list" in operations | Route test | ALL |
| AC-005.5 | GET /{entities}/{id} endpoint if "read" in operations | Route test | ALL |
| AC-005.6 | PATCH /{entities}/{id} endpoint if "update" in operations | Route test | ALL |
| AC-005.7 | DELETE /{entities}/{id} endpoint if "delete" in operations | Route test | ALL |
| AC-005.8 | 404 error handling for GET/PATCH/DELETE by ID | Error handling test | ALL |

**Operations Matrix**:

| Operation | HTTP Method | Endpoint | Response Code |
|-----------|-------------|----------|---------------|
| create | POST | `/{entities}` | 201 |
| list | GET | `/{entities}` | 200 |
| read | GET | `/{entities}/{id}` | 200 |
| update | PATCH | `/{entities}/{id}` | 200 |
| delete | DELETE | `/{entities}/{id}` | 204 |

**BDD Scenario**:
```gherkin
GIVEN a module "orders" with operations ["create", "read", "list"]
  AND entity "Order"
WHEN EndpointProcessor.process() is called
THEN `app/api/routes/orders.py` generated
  AND POST /orders endpoint exists
  AND GET /orders endpoint exists (list)
  AND GET /orders/{id} endpoint exists
  AND PATCH /orders/{id} endpoint does NOT exist
  AND DELETE /orders/{id} endpoint does NOT exist
```

---

### FR-006: CRUD Service Generation

**Description**: Generate service layer with database operations for each entity.

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-006.1 | One service file per entity (`app/services/{entity}_service.py`) | File count test | ALL |
| AC-006.2 | `{Entity}Service` class with `__init__(db: AsyncSession)` | Constructor test | ALL |
| AC-006.3 | `create(data)` method if "create" in operations | Method test | ALL |
| AC-006.4 | `get(id)` method if "read" in operations | Method test | ALL |
| AC-006.5 | `list(skip, limit)` method if "list" in operations | Method test | ALL |
| AC-006.6 | `update(id, data)` method if "update" in operations | Method test | ALL |
| AC-006.7 | `delete(id)` method if "delete" in operations | Method test | ALL |

**BDD Scenario**:
```gherkin
GIVEN an entity "Order" with operations ["create", "read", "list", "delete"]
WHEN EndpointProcessor.process() is called
THEN `app/services/order_service.py` generated
  AND OrderService class has create(data: OrderCreate) method
  AND OrderService class has get(id: UUID) method
  AND OrderService class has list(skip: int, limit: int) method
  AND OrderService class has delete(id: UUID) method
  AND OrderService class does NOT have update() method
```

---

### FR-007: Bundle Assembly & Output

**Description**: Orchestrate all processors and assemble complete output bundle.

**Acceptance Criteria**:

| ID | Criterion | Test Method | Tier |
|----|-----------|-------------|------|
| AC-007.1 | BundleBuilder validates IR before processing | Validation test | ALL |
| AC-007.2 | All processors run in sequence (Project → Model → Endpoint) | Orchestration test | ALL |
| AC-007.3 | GeneratedBundle includes success status, files, file_count, total_lines | Response structure test | ALL |
| AC-007.4 | Validation errors returned before processing starts | Error handling test | ALL |
| AC-007.5 | Bundle contains 10-15 files for typical restaurant app | Integration test | PRO, ENT |
| AC-007.6 | Total lines calculated from all generated files | Calculation test | ALL |

**BDD Scenario**:
```gherkin
GIVEN a valid AppBlueprint for "Restaurant Order System" with 1 module, 1 entity
WHEN BundleBuilder.build(blueprint) is called
THEN bundle.success returns True
  AND bundle.files contains 12-15 files
  AND bundle.file_count >= 10
  AND bundle.total_lines >= 200
  AND bundle.errors is empty array
  AND bundle.app_name equals "Restaurant Order System"
```

---

## 3. Technical Requirements

### TR-001: Jinja2 Template Engine

**Requirements**:
- Jinja2 3.1.2+ for template rendering
- Templates stored in `backend/app/services/codegen/templates/fastapi/`
- Template categories: models, schemas, routes, config, docker
- Auto-escaping enabled for security
- `trim_blocks` and `lstrip_blocks` enabled for clean output

**Template Files**:

| Template | Purpose | Output |
|----------|---------|--------|
| `main.py.j2` | FastAPI app entry point | `app/main.py` |
| `config.py.j2` | Application config | `app/core/config.py` |
| `model.py.j2` | SQLAlchemy model | `app/models/{entity}.py` |
| `schema.py.j2` | Pydantic schemas | `app/schemas/{entity}.py` |
| `route.py.j2` | FastAPI routes | `app/api/routes/{module}.py` |
| `crud.py.j2` | CRUD service | `app/services/{entity}_service.py` |
| `docker-compose.yml.j2` | Docker services | `docker-compose.yml` |
| `Dockerfile.j2` | Python container | `Dockerfile` |

### TR-002: JSON Schema Validation

**Requirements**:
- JSON Schema Draft 7 for IR validation
- Schemas stored in `backend/app/schemas/codegen/`
- `jsonschema` library 4.17+ with `Draft7Validator`
- Validation error reporting with JSON path + message
- Normalization with default value application

**Schema Files**:

| Schema | Validates | Required Fields |
|--------|-----------|-----------------|
| `app_blueprint.schema.json` | AppBlueprint root | name, version, modules |
| `module_spec.schema.json` | ModuleSpec | name, entities |
| `data_model.schema.json` | DataModelSpec | name, fields |
| `field_spec.schema.json` | FieldSpec | name, type |

### TR-003: Processor Architecture

**Requirements**:
- Abstract base class `IRProcessor` for all processors
- Concrete processors: `ProjectProcessor`, `ModelProcessor`, `EndpointProcessor`
- Each processor returns `ProcessorResult` with success status + files + errors
- Template rendering via `render_template(template_name, context)`
- Error handling: catch exceptions, return errors in result

**Processor Interface**:
```python
class IRProcessor(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Processor name for logging."""
        pass

    @abstractmethod
    def process(self, ir: Dict[str, Any]) -> ProcessorResult:
        """Process IR and generate files."""
        pass

    def render_template(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render Jinja2 template."""
        pass
```

### TR-004: Package Structure

**Requirements**:
```
backend/app/services/codegen/
├── ir/
│   ├── __init__.py
│   ├── validator.py              # IRValidator class
│   ├── processor_base.py         # IRProcessor base
│   ├── project_processor.py      # ProjectProcessor
│   ├── model_processor.py        # ModelProcessor
│   ├── endpoint_processor.py     # EndpointProcessor
│   └── bundle_builder.py         # BundleBuilder orchestrator
├── templates/fastapi/
│   ├── main.py.j2
│   ├── config.py.j2
│   ├── model.py.j2
│   ├── schema.py.j2
│   ├── route.py.j2
│   └── crud.py.j2
└── templates/docker/
    ├── Dockerfile.j2
    └── docker-compose.yml.j2
```

### TR-005: API Integration

**Requirements**:
- Integrate `BundleBuilder` into `/codegen/generate` endpoint
- Return `GeneratedBundle` in API response
- Provider type: `"ir_processor"` (deterministic, no AI)
- Include metadata: app_name, file_count, total_lines, generator

**API Response Structure**:
```json
{
  "success": true,
  "result": {
    "success": true,
    "files": [
      {"path": "app/main.py", "content": "...", "language": "python"},
      {"path": "app/models/order.py", "content": "...", "language": "python"}
    ],
    "provider": "ir_processor",
    "file_count": 12,
    "total_lines": 450,
    "metadata": {
      "app_name": "Restaurant Order System",
      "generator": "SDLC Orchestrator EP-06"
    }
  }
}
```

---

## 4. Quality Requirements

### QR-001: Code Generation Quality

**Requirements**:
- Generated code must be valid Python 3.11+ syntax
- All generated files must pass `ruff` linting (0 errors)
- Generated models must follow SQLAlchemy 2.0 best practices
- Generated routes must follow FastAPI conventions
- Code must be production-ready (no TODOs, no placeholders)

**Validation**:
- AST parsing test: `ast.parse(generated_code)` must succeed
- Linting test: `ruff check` must return 0 errors
- Type checking: `mypy` in strict mode must pass

### QR-002: Template Coverage

**Requirements**:
- 100% coverage of IR schema types (all field types supported)
- Templates support all CRUD operations (create, read, update, delete, list)
- Templates handle edge cases (optional fields, unique constraints, indexes)
- Templates include error handling (404, validation errors)

**Test Coverage**:
- Unit tests: 95%+ for all processors
- Integration tests: 90%+ for BundleBuilder
- Template tests: 100% for all Jinja2 templates

### QR-003: Performance

**Requirements**:
- IR validation: <100ms for typical blueprint (1 module, 3 entities)
- Code generation: <500ms for typical restaurant app (10-15 files)
- Total bundle build time: <1s (p95)
- Memory usage: <100MB during generation

**Benchmark Targets**:

| Metric | Target | Test Method |
|--------|--------|-------------|
| Validation time | <100ms | pytest-benchmark |
| Generation time | <500ms | pytest-benchmark |
| Total time | <1s (p95) | Load test (100 concurrent) |
| Memory usage | <100MB | Memory profiler |

---

## 5. Tier-Specific Requirements

### TSR-001: LITE Tier Requirements

**Scope**: Basic scaffold generation without Docker or deployment

| Requirement | Implementation |
|-------------|----------------|
| Generate main.py, config.py, requirements.txt | ProjectProcessor |
| Generate SQLAlchemy models | ModelProcessor |
| Generate CRUD endpoints (create, read, list only) | EndpointProcessor |
| Skip Docker files | ProjectProcessor skips docker templates |
| Skip Alembic migrations | No MigrationProcessor |

**Rationale**: LITE tier (1-2 developers) needs minimal setup, no containerization.

### TSR-002: PROFESSIONAL/ENTERPRISE Tier Requirements

**Scope**: Full scaffold with Docker, Alembic, and production optimizations

| Requirement | Implementation | Tier |
|-------------|----------------|------|
| Generate Dockerfile + docker-compose.yml | ProjectProcessor | PRO, ENT |
| Generate Alembic migration files | MigrationProcessor (future) | PRO, ENT |
| Generate health check endpoints | ProjectProcessor | PRO, ENT |
| Generate pytest test scaffolds | TestProcessor (future) | ENT |
| Generate OpenAPI documentation | FastAPI auto-docs | PRO, ENT |

**Rationale**: PRO/ENT tiers (10-50+ developers) need production-ready infrastructure.

---

## 6. Testing Strategy

### 6.1 Unit Tests

**Coverage**: 95%+ for all IR processors

**Test Cases**:
```python
# backend/tests/unit/services/codegen/ir/test_validator.py
def test_valid_blueprint_passes_validation()
def test_invalid_entity_name_fails_validation()
def test_missing_required_field_fails_validation()
def test_normalization_applies_defaults()

# backend/tests/unit/services/codegen/ir/test_project_processor.py
def test_generate_main_py()
def test_generate_config_py()
def test_generate_requirements_txt()
def test_generate_docker_compose_yml()

# backend/tests/unit/services/codegen/ir/test_model_processor.py
def test_generate_sqlalchemy_model()
def test_type_mapping_string_to_sqlalchemy()
def test_field_constraints_applied()
def test_base_model_generation()

# backend/tests/unit/services/codegen/ir/test_endpoint_processor.py
def test_generate_crud_endpoints()
def test_operations_filter_applied()
def test_404_error_handling()
```

### 6.2 Integration Tests

**Coverage**: 90%+ for end-to-end bundle generation

**Test Cases**:
```python
# backend/tests/integration/test_ir_bundle.py
def test_generate_restaurant_app_bundle()
def test_generated_code_is_valid_python()
def test_generated_models_import_successfully()
def test_generated_routes_start_fastapi_app()
def test_bundle_with_multiple_modules()
```

### 6.3 Acceptance Tests

**Coverage**: All acceptance criteria from FR-001 to FR-007

**Example**:
```python
def test_ac_001_1_app_blueprint_validation():
    """AC-001.1: AppBlueprint JSON validated against schema"""
    validator = IRValidator(schema_dir)
    blueprint = {"name": "Test", "version": "1.0.0", "modules": [...]}

    result = validator.validate_app_blueprint(blueprint)

    assert result.valid is True
    assert len(result.issues) == 0
```

---

## 7. Dependencies

### Internal Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| Sprint 45: CodegenProvider | 1.0.0 | Multi-provider gateway API |
| SDLC-Orchestrator API | 1.0.0 | `/codegen/generate` endpoint |

### External Dependencies

| Dependency | Version | License | Purpose |
|------------|---------|---------|---------|
| Jinja2 | 3.1.2+ | BSD-3-Clause | Template rendering |
| jsonschema | 4.17+ | MIT | IR validation |
| FastAPI | 0.104.1 | MIT | Generated app framework |
| SQLAlchemy | 2.0.23 | MIT | Generated ORM models |
| Pydantic | 2.5.2 | MIT | Generated schemas |

---

## 8. Migration & Rollback

### Migration from Sprint 45

**Changes**:
- Add `ir/` package to `backend/app/services/codegen/`
- Add `templates/` directory with Jinja2 templates
- Update `/codegen/generate` endpoint to use `BundleBuilder`
- Add JSON schemas to `backend/app/schemas/codegen/`

**Migration Steps**:
1. Create `ir/` package structure
2. Implement `IRValidator`, `IRProcessor` classes
3. Create Jinja2 templates
4. Update API endpoint
5. Add unit + integration tests
6. Deploy with backward compatibility (old API still works)

### Rollback Plan

**Rollback Trigger**: >10% failure rate in bundle generation

**Rollback Steps**:
1. Revert API endpoint to Sprint 45 version
2. Remove `ir/` package from imports
3. Keep templates (no side effects)
4. Monitor error rate for 24h
5. Root cause analysis + fix

---

## 9. Success Criteria

### Sprint 46 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Unit test coverage | ≥95% | pytest-cov |
| Integration test coverage | ≥90% | pytest-cov |
| IR validation accuracy | ≥99% | Test suite pass rate |
| Code generation success rate | ≥95% | API response metrics |
| Generated code validity | 100% | AST parsing + linting |
| Bundle generation time | <1s (p95) | pytest-benchmark |

### Demo Success Criteria

**Demo Scenario**: Generate Restaurant Order System from IR

**Success Criteria**:
1. IR blueprint validated (0 errors)
2. 12-15 files generated
3. Generated code passes `ruff` linting
4. FastAPI app starts successfully
5. CRUD endpoints return 200 OK
6. Swagger UI accessible at `/docs`

---

## 10. Related Documents

### Framework Documents

- SDLC 6.0.5 Specification Standard
- Section 7: Quality Assurance System
- Pillar 4: Build & Implementation

### Architecture Documents

- ADR-022: EP-06 IR-Based Codegen Architecture
- System Architecture Document v3.0.0 (5-Layer Architecture)

### Sprint Documents

- Sprint 45: Multi-Provider Codegen Gateway
- Sprint 46: IR Processor Implementation (THIS SPEC)
- Sprint 47: Vietnamese Domain Templates
- Sprint 48: 4-Gate Quality Pipeline

---

## 11. Glossary

| Term | Definition |
|------|------------|
| **IR** | Intermediate Representation - structured JSON schema for app definition |
| **AppBlueprint** | Root IR schema defining app name, version, modules, database |
| **ModuleSpec** | IR schema defining a module (e.g., "orders") with entities and operations |
| **DataModelSpec** | IR schema defining an entity (e.g., "Order") with fields and relationships |
| **FieldSpec** | IR schema defining a field (e.g., "status" string field) |
| **BundleBuilder** | Orchestrator class that runs all processors and assembles output |
| **GeneratedBundle** | Output structure with success status, files, and metadata |
| **Processor** | Component that transforms IR into code files (Project/Model/Endpoint) |
| **Jinja2** | Template engine for rendering Python/YAML/Dockerfile templates |
| **JSON Schema** | Schema language for validating JSON structures (Draft 7) |

---

**Document Status**: ✅ APPROVED
**Last Review**: January 30, 2026
**Next Review**: February 28, 2026 (Post Sprint 46 completion)

**Approval Chain**:
- Backend Lead: ✅ APPROVED (Dec 23, 2025)
- Architect: ✅ APPROVED (Dec 23, 2025)
- CTO: ✅ APPROVED (Dec 23, 2025)

---

*SDLC Framework 6.0.2 - Specification Standard Compliance*
*Sprint 46 (Jan 20-31, 2026) - EP-06 IR-Based Backend Scaffold Generation*
