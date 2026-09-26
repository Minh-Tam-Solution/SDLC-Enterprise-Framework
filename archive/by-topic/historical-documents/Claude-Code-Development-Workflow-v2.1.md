# Hướng dẫn Quy trình Phát triển với Claude Code

## Tổng quan

**Claude Code** là một công cụ dòng lệnh (CLI) cho phép bạn ủy thác các tác vụ lập trình phức tạp trực tiếp từ terminal. Quy trình làm việc này tận dụng Claude Code như một **AI codex agent** (tác tử mã hóa AI) trong suốt các giai đoạn của vòng đời phát triển phần mềm, từ chiến lược đến vận hành.

### Các điểm khác biệt chính: Claude Code vs. IDE-based AI

| Tiêu chí | Claude Code | Cursor (và các IDE tương tự) |
| :--- | :--- | :--- |
| **Nền tảng** | Dòng lệnh (terminal) | Tích hợp trong IDE |
| **Phương pháp** | Ủy thác tác vụ, thực thi tự động | Phát triển tương tác, hỗ trợ thời gian thực |
| **Phạm vi** | Hoàn thành các tính năng phức tạp, xử lý hàng loạt | Sửa lỗi, viết các đoạn code nhỏ, hỗ trợ tức thời |

-----

## 5 Giai Đoạn Của Quy Trình Làm Việc

Quy trình được chia thành 5 giai đoạn chính, trong đó Claude Code đóng các vai trò khác nhau để tự động hóa công việc.

### **Giai đoạn 1: Chiến lược Sản phẩm & Phân tích Kinh doanh**

**Vai trò của Claude Code**: Product Manager + Business Analyst

Claude Code giúp tự động hóa việc tạo ra các tài liệu nền tảng, đảm bảo tầm nhìn sản phẩm rõ ràng và nhất quán.

  * **Tài liệu Yêu cầu Kinh doanh (BRD)**:
    ```bash
    # Tạo BRD toàn diện
    claude-code "Act as Senior Business Analyst for [PROJECT_NAME]. Create comprehensive BRD with:
    - Business objectives and success metrics  
    - Stakeholder analysis with RACI matrix
    - High-level system requirements
    - Risk assessment using SWOT analysis
    - Implementation timeline with Gantt chart format
    - ROI and cost-benefit analysis
    Output as markdown in docs/BRD.md"
    ```
  * **Lộ trình Sản phẩm (Product Roadmap)**:
    ```bash
    # Tạo lộ trình sản phẩm dựa trên BRD
    claude-code "Act as Product Manager. Based on BRD in docs/BRD.md, create:
    - Product vision statement
    - Feature prioritization (MoSCoW method)
    - Release roadmap with 3-month sprints
    - Success metrics per release
    - Go-to-market strategy
    Save as docs/PRODUCT_ROADMAP.md"
    ```

### **Giai đoạn 2: Kiến trúc Kỹ thuật**

**Vai trò của Claude Code**: Technical Architect + DevOps

AI đảm nhận việc thiết kế kiến trúc và khởi tạo toàn bộ cấu trúc dự án.

  * **Thiết kế Kiến trúc Hệ thống**:
    ```bash
    # Thiết kế kiến trúc full-stack và tạo sơ đồ Mermaid
    claude-code "Act as Full-Stack Technical Architect. Design a full-stack architecture for a web & mobile app using our tech stack. Create detailed architecture diagrams using Mermaid and save in docs/ARCHITECTURE.md"
    ```
  * **Thiết lập Cấu trúc Dự án**:
    ```bash
    # Khởi tạo cấu trúc dự án full-stack
    claude-code "Create a full-stack project structure with /backend, /frontend, /mobile, /shared, /docs, /infrastructure. Include Dockerfiles, docker-compose.yml, GitHub Actions workflows, and pre-commit hooks."
    ```
  * **Định nghĩa Ngữ cảnh với `CLAUDE.md`**: Đây là tệp quan trọng nhất, đóng vai trò là "bộ não" của dự án cho AI.
    ```markdown
    # Project Overview
    - **Project Name**: [Tên dự án]
    - **Description**: [Mô tả ngắn gọn về dự án]

    ## Directory Structure
    - **/backend**: Python FastAPI application
    - **/frontend**: React (TypeScript) web application
    - ...

    ## Tech Stack
    ### Backend
    - **Framework**: Python 3.11+ with FastAPI
    - **Database**: PostgreSQL, Redis
    - ...

    ## Coding Standards & Conventions
    - **Commit Messages**: Conventional Commits
    - **API Design**: RESTful principles
    - **Branching Strategy**: GitFlow
    ```

### **Giai đoạn 3: Triển khai Phát triển**

**Vai trò của Claude Code**: Full-Stack Developer

Đây là giai đoạn Claude Code tỏa sáng nhất, tự động viết code cho toàn bộ ứng dụng bằng cách sử dụng phương pháp **Chain of Thought**.

  * **Phát triển Backend (Chain of Thought)**:
    ```bash
    claude-code "Act as a Senior Backend Developer. Your task is to implement core features for our Python FastAPI backend.

    **Context:** Refer to the project definition in `CLAUDE.md`.

    **Instructions (Chain of Thought):**
    1.  **Think Step-by-Step**: First, outline the key components and modules needed.
    2.  **Define Requirements**: Based on your outline and modern best practices, list the detailed requirements (authentication, authorization, models, schemas, etc.).
    3.  **Implement**: Generate the code based on the requirements.
    4.  **Organize Output**: Place the generated code into the `/backend` directory."
    ```
  * **Phát triển Frontend & Mobile**: Áp dụng prompt theo phương pháp Chain of Thought tương tự.

### **Giai đoạn 4: Kiểm thử & Đảm bảo Chất lượng**

**Vai trò của Claude Code**: QA Engineer + Security Auditor

AI tự động tạo ra chiến lược kiểm thử và thực hiện kiểm toán bảo mật.

  * **Kiểm thử Toàn diện**:
    ```bash
    # Tạo chiến lược và kịch bản kiểm thử
    claude-code "Create a comprehensive test strategy including a test plan, API test automation with pytest, Web E2E tests with Playwright, and Mobile E2E tests with Detox. Output reports to /tests/reports/."
    ```
  * **Kiểm toán Bảo mật**:
    ```bash
    # Thực hiện kiểm toán bảo mật
    claude-code "Perform a security audit covering SAST with bandit, dependency scanning, API penetration test cases (OWASP Top 10), and generate a report in docs/SECURITY_AUDIT.md."
    ```

### **Giai đoạn 5: Triển khai & Vận hành**

**Vai trò của Claude Code**: DevOps Engineer + SRE

Tự động hóa việc tạo hạ tầng (IaC) và sinh ra các tài liệu vận hành.

  * **Hạ tầng dưới dạng Mã (IaC)**:
    ```bash
    # Tạo hạ tầng sản xuất
    claude-code "Create production infrastructure using Terraform modules for AWS/GCP, Kubernetes manifests with Helm, and CI/CD pipelines with GitHub Actions. Include monitoring with Prometheus/Grafana."
    ```
  * **Sổ tay Vận hành (Runbooks)**:
    ```bash
    # Tạo sổ tay vận hành
    claude-code "Create operational runbooks including deployment procedures, rollback strategies, and incident response playbooks. Format as actionable checklists."
    ```

-----

## Nghệ thuật Prompt Engineering

Chất lượng đầu ra phụ thuộc trực tiếp vào chất lượng của prompt. Một prompt hiệu quả cần có cấu trúc rõ ràng.

### "Giải phẫu" một Prompt Hiệu quả

```bash
claude-code "
# 1. Vai trò (Role)
Role: Senior Python Developer

# 2. Ngữ cảnh (Context)
Context: E-commerce platform. Schema in `docs/schema.sql`. Use DDD pattern from `backend/services/`.

# 3. Nhiệm vụ (Task)
Task: Implement the 'Shopping Cart' feature.

# 4. Yêu cầu (Requirements)
Requirements:
- API for add, view, update, remove items.
- Use Pydantic models for validation.
- Test coverage > 95%.
- Update OpenAPI docs.

# 5. Ràng buộc (Constraints)
Constraints:
- Use PostgreSQL and Redis.
- Response time < 150ms.
"
```

1.  **Role**: Đặt AI vào một vai trò cụ thể để nó hành xử và áp dụng kiến thức phù hợp.
2.  **Context**: Cung cấp bối cảnh, tài liệu tham chiếu, và các mẫu code để AI làm việc một cách nhất quán.
3.  **Task**: Nêu rõ nhiệm vụ cần thực hiện, tránh sự mơ hồ.
4.  **Requirements**: Liệt kê các yêu cầu chi tiết, có thể định lượng.
5.  **Constraints**: Đặt ra các ràng buộc về công nghệ hoặc hiệu năng mà AI phải tuân thủ.

-----

## Hợp tác & Tối ưu hóa

  * **Thư viện Tác vụ Chung**: Tạo các tệp script (`.sh`) chứa các prompt thường dùng để toàn đội tái sử dụng.
  * **Chia sẻ Kiến thức**: Dùng Claude Code để tự động tạo tài liệu về các quyết định kiến trúc (ADRs), quy ước code (coding conventions).
  * **Tự động hóa Code Review**: Tích hợp Claude Code vào quy trình CI/CD để tự động review Pull Request, kiểm tra tiêu chuẩn và lỗ hổng bảo mật.

## NQH-BOT Specific Guidelines

### Project Context
- **MVP Focus**: Clock in/out, Smart chat, Task management
- **Architecture**: Multi-tenant with facility-based isolation
- **Tech Stack**: FastAPI + PostgreSQL + Redis + React PWA
- **Deployment**: Single VPS, Docker Compose

### Development Workflow
1. Always check `CLAUDE.md` for project-specific guidelines
2. Use TodoWrite tool for task planning and tracking
3. Run tests and linting before committing
4. Follow the 5-phase workflow described above

### Quality Gates
- Test coverage ≥ 70%
- All linting checks pass (black, flake8, mypy)
- Security scan with bandit
- API documentation updated

## Python Development Best Practices

### Coding Standards
- **C-1**: Use type hints for all functions
- **C-2**: Follow existing naming conventions
- **C-3**: Prefer functions over classes when simple
- **C-4**: Use environment variables for config
- **C-5**: No hardcoded secrets

### Testing
- **T-1**: Write tests before implementation (TDD)
- **T-2**: Separate unit tests from integration tests
- **T-3**: Use pytest fixtures
- **T-4**: Include security test cases

### Security
- **S-1**: Run Bandit scanner: `bandit -r src/`
- **S-2**: Validate all inputs
- **S-3**: Use encryption service for sensitive data
- **S-4**: Implement proper authentication
- **S-5**: Never commit .env files

### Git Workflow
- Use Conventional Commits format
- Types: feat, fix, docs, style, refactor, test, chore
- Example: `feat(auth): add OAuth2 support`

## Shortcuts Reference

### QNEW
Follow all best practices including security guidelines.

### QPLAN
Analyze codebase for consistency before implementing.

### QCODE
Implement with tests, run black, flake8, and bandit.

### QCHECK
Review as skeptical senior developer:
1. Check best practices
2. Verify Python idioms
3. Run linting tools

### QSEC
Security review:
1. OWASP Top 10
2. Bandit scanner
3. Auth logic
4. Input validation

### QGIT
Prepare and commit:
1. Clean artifacts
2. Format code
3. Run checks
4. Commit with conventional format

## Kết luận

Bằng cách tích hợp **Claude Code** vào cả 5 giai đoạn của quy trình phát triển, các doanh nghiệp có thể:

  * 🚀 **Tăng tốc độ** phát triển lên nhiều lần.
  * 🛡️ **Nâng cao chất lượng** và tính nhất quán của mã nguồn.
  * 💰 **Tối ưu hóa chi phí** và giải phóng nguồn lực developer cho các công việc sáng tạo.