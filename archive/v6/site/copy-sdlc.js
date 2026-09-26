/* ============================================================
   SDLC Framework — copy strings (EN/VI bilingual)
   ============================================================ */
const sdlcCopy = {
  en: {
    nav: { framework: "Framework", endiorbot: "Endiorbot", orchestrator: "Orchestrator", lang: "EN" },
    hero: {
      eyebrow: "v6.3.1 · April 2026 · MIT Licensed",
      headline_a: "A 7-pillar methodology for",
      headline_em: "AI + Human teams",
      headline_b: "that actually ship.",
      sub: "Tool-agnostic. Battle-tested in production. 503 documents, 39h of training, 18 SOUL roles, 10 stages, 5 quality gates — all open source.",
      ctaPrimary: "Read the Executive Summary",
      ctaSecondary: "See live reference: Endiorbot →",
      stat1: { n: "11", l: "training modules" },
      stat2: { n: "39h", l: "curriculum" },
      stat3: { n: "18", l: "SOUL roles" },
      stat4: { n: "10", l: "lifecycle stages" },
      stat5: { n: "503+", l: "framework docs" },
    },
    promise: {
      eyebrow: "The promise",
      title: "Built BY AI+Human teams. FOR AI+Human teams.",
      body: "Most SDLC frameworks were written before LLMs existed. They treat AI as a tool you bolt on. SDLC 6.3.1 starts from a different premise: humans guide, agents execute, humans verify — at every stage, with evidence, with gates, with accountability. The framework is what's left when you remove every assumption that AI doesn't exist.",
    },
    pillars: {
      eyebrow: "Pillar 0 → 6 + Section 7 + 8",
      title: "Seven pillars, two extensions.",
      sub: "Every pillar is independent. Adopt one or all seven — the framework scales from solo developer to enterprise.",
      items: [
        { n: "P0", t: "Design Thinking", d: "Empathize → Define → Ideate → Prototype → Test. Validate problems before building solutions. Cuts the 70% feature-waste rate the industry quietly lives with." },
        { n: "P1", t: "10-Stage Lifecycle", d: "Foundation → Govern. Every stage has explicit prerequisites, exit criteria, and tier-aware requirements. Skip with eyes open, not by accident." },
        { n: "P2", t: "Sprint Governance", d: "Three-phase sprint model with TDD baked in. G-Sprint and G-Sprint-Close gates. 24-hour documentation rule. Ten golden rules for sprint integrity." },
        { n: "P3", t: "4-Tier Classification", d: "LITE (1-2 devs) → STANDARD → PROFESSIONAL → ENTERPRISE (50+). Tier dictates required stages, documentation depth, and tooling — not the other way around." },
        { n: "P4", t: "Quality Gates", d: "Dual-track gates: feature (G0–G4) and sprint (G-Sprint). Evidence-based passes. No green-light without artifacts. Vibecoding Index quantifies risk." },
        { n: "P5", t: "SASE Integration", d: "Software Agent Software Engineering 3.0. SE4H (humans coach) vs SE4A (agents execute). AGENTS.md + CRP + MRP + VCR. 13 roles in the canonical model." },
        { n: "P6", t: "Documentation Permanence", d: "AI-parseable formats. YAML frontmatter mandatory. BDD requirements (GIVEN-WHEN-THEN). Specs are the single source of truth — not Slack threads." },
      ],
      sec7: { n: "§7", t: "Quality Assurance System", d: "Anti-Vibecoding controls. Vibecoding Index (0–100). Progressive routing: green auto-merge → red CTO override. Auto-generation reduces compliance friction from 30 min to <5 min per PR." },
      sec8: { n: "§8", t: "Unified Specification Standard", d: "Mandatory YAML frontmatter, BDD requirements, lightweight ADRs (DESIGN_DECISIONS), version tracking (SPEC_DELTA). Format-agnostic SpecIR converts OpenSpec ↔ SDLC bidirectionally." },
    },
    stages: {
      eyebrow: "Pillar 1",
      title: "Ten stages. Two questions per stage.",
      sub: "Click any stage to inspect prerequisites, exit gate, and key deliverables.",
      data: [
        { id: "00", name: "Foundation", q: "WHY?", gate: "G0.1 / G0.2", reqs: "—", parallel: "No",
          deliverables: [
            ["Question", "Why are we building this?"],
            ["Output", "Business case · Problem statement · 3 evidence-based personas"],
            ["Gate", "G0.1 (problem validated, 5+ users) → G0.2 (solution diversity, 100+ ideas)"],
            ["Skip risk", "Critical — skipping causes 70% feature waste"],
          ]
        },
        { id: "01", name: "Planning", q: "WHAT?", gate: "G1", reqs: "00 + G0.2", parallel: "No",
          deliverables: [
            ["Question", "What are we building?"],
            ["Output", "Requirements · User stories · API specs · Acceptance criteria"],
            ["Format", "BDD (GIVEN-WHEN-THEN) mandatory at STANDARD+"],
            ["Gate", "G1 — stakeholders approve, requirements complete"],
          ]
        },
        { id: "02", name: "Design", q: "HOW?", gate: "G2", reqs: "01 + G1", parallel: "No",
          deliverables: [
            ["Question", "How will we build it?"],
            ["Output", "Architecture · ADRs · Threat model · Security design"],
            ["Templates", "ADR-NNN, SPEC-NNNN with YAML frontmatter"],
            ["Gate", "G2 — CTO/Tech Lead approval"],
          ]
        },
        { id: "03", name: "Integrate", q: "Connect?", gate: "G2", reqs: "02 + G2", parallel: "Yes (with 04)",
          deliverables: [
            ["Question", "How does it connect to the world?"],
            ["Output", "API contracts · Integration tests · OpenAPI SSOT"],
            ["Cross-ref", "Stage 03 ↔ Stage 05 traceability matrix"],
            ["Pattern", "Parallel with Build via API-first development"],
          ]
        },
        { id: "04", name: "Build", q: "Right?", gate: "G3", reqs: "02 + G2", parallel: "Yes (with 03)",
          deliverables: [
            ["Question", "Are we building it right?"],
            ["Output", "Working code · Unit tests · Coverage at tier target"],
            ["TDD", "RED → GREEN → REFACTOR per feature"],
            ["Coverage", "LITE 70% · STD 85% · PRO/ENT 95%"],
          ]
        },
        { id: "05", name: "Test", q: "Works?", gate: "G3", reqs: "04 + G3", parallel: "No",
          deliverables: [
            ["Question", "Does it work correctly?"],
            ["Output", "Test reports · UAT sign-off · OWASP API Top-10 checked"],
            ["Workflow", "6-phase E2E: Discovery → Config → Execution → Security → Reporting → Integration"],
            ["Saves", "~83% setup time vs ad-hoc testing"],
          ]
        },
        { id: "06", name: "Deploy", q: "Ship?", gate: "G4", reqs: "05 + G3", parallel: "No",
          deliverables: [
            ["Question", "How do we ship safely?"],
            ["Output", "Release notes · Rollback procedures · Deployment evidence"],
            ["Checklist", "100-item Go-Live Readiness (tier-aware)"],
            ["Gate", "G4 — production stability confirmed"],
          ]
        },
        { id: "07", name: "Operate", q: "Running?", gate: "Continuous", reqs: "06 + G4", parallel: "Yes",
          deliverables: [
            ["Question", "Is it running reliably?"],
            ["Output", "Runbooks · Monitoring dashboards · SLO definitions"],
            ["Metrics", "DORA: deployment frequency, lead time, MTTR, CFR"],
            ["Target", "99.9%+ uptime at PRO/ENT tier"],
          ]
        },
        { id: "08", name: "Collaborate", q: "Effective?", gate: "Continuous", reqs: "01+", parallel: "Yes",
          deliverables: [
            ["Question", "Is the team effective?"],
            ["Output", "Team charter · AGENTS.md · Training materials"],
            ["Roles", "13-role SASE model + 10 TEAM charters"],
            ["Pattern", "Runs throughout — never blocks delivery"],
          ]
        },
        { id: "09", name: "Govern", q: "Compliant?", gate: "Continuous", reqs: "06 + G4", parallel: "Yes",
          deliverables: [
            ["Question", "Are we compliant?"],
            ["Output", "Compliance reports · Audit logs · Risk register"],
            ["Standards", "SOC 2 · HIPAA · GDPR · NIST SSDF mappings"],
            ["Early start", "Can begin at Stage 01 if regulated industry"],
          ]
        },
      ]
    },
    tiers: {
      eyebrow: "Pillar 3",
      title: "One framework. Four tiers.",
      sub: "Pick the tier that fits your team — don't pick a tier above it. The framework scales down as gracefully as it scales up.",
      items: [
        { lvl: "T1", name: "LITE", who: "1–2 developers · Solo · Indie", stages: "00, 01, 02, 04",
          features: ["3 SOUL roles", "README + .env.example", "70% test coverage", "AGENTS.md <60 lines"], rec: false },
        { lvl: "T2", name: "STANDARD", who: "3–10 developers · Startups · Small agencies", stages: "00–02, 04–06",
          features: ["6 SOUL roles", "+ CLAUDE.md + /docs", "85% test coverage", "BDD requirements"], rec: true },
        { lvl: "T3", name: "PROFESSIONAL", who: "10–50 developers · Growth-stage", stages: "All 10 stages",
          features: ["11 SOUL roles", "+ Full ADRs + Compliance", "95% test coverage", "Senior review board"], rec: false },
        { lvl: "T4", name: "ENTERPRISE", who: "50+ developers · Regulated · Public", stages: "All 10 stages",
          features: ["14 SOUL roles", "+ Executive reports + Audit", "95%+ with security tests", "All sections active"], rec: false },
      ]
    },
    gates: {
      eyebrow: "Pillar 4",
      title: "Five gates. Evidence or no pass.",
      sub: "Quality gates are not approvals — they are evidence checkpoints. If artifacts don't exist, the gate doesn't pass.",
      items: [
        { id: "G0", phase: "Foundation", title: "Problem & Solution Validated",
          ev: ["5+ user interviews documented", "100+ ideas generated, top 3 selected", "Personas evidence-based"] },
        { id: "G1", phase: "Planning", title: "Requirements Complete",
          ev: ["BDD requirements written", "Stakeholders signed off", "Acceptance criteria measurable"] },
        { id: "G2", phase: "Design", title: "Architecture Approved",
          ev: ["ADRs reviewed by CTO/Tech Lead", "Threat model complete", "API contracts in version control"] },
        { id: "G3", phase: "Build · Test", title: "Ship-Ready",
          ev: ["Tier coverage met (70/85/95%)", "OWASP API Top-10 checked", "MRP submitted for >100 LOC"] },
        { id: "G4", phase: "Deploy · Operate", title: "Production Stable",
          ev: ["Rollback procedure tested", "Monitoring dashboards live", "SLOs defined and tracked"] },
      ]
    },
    vibe: {
      eyebrow: "Section 7",
      title: "The Vibecoding Index.",
      body: "Vibecoded code is fast to write, expensive to maintain. The Index quantifies risk on a 0–100 scale across five weighted signals, then routes each PR to the right reviewer.",
      signals: [
        { l: "Intent Clarity", w: "30%" },
        { l: "Code Ownership Confidence", w: "25%" },
        { l: "Context Completeness", w: "20%" },
        { l: "AI Attestation Rate", w: "15%" },
        { l: "Historical Rejection Rate", w: "10%" },
      ],
      routing: [
        { range: "0–19", label: "Green", action: "Auto-merge · 1+ approvals" },
        { range: "20–39", label: "Yellow", action: "Tech Lead spot-check" },
        { range: "40–59", label: "Orange", action: "CEO optional · Senior eng review" },
        { range: "60–100", label: "Red", action: "Senior Review Board · CTO override" },
      ]
    },
    souls: {
      eyebrow: "Pillar 5 · SASE 13-Role Model",
      title: "Eighteen role templates. Pre-tuned, battle-tested.",
      sub: "Each SOUL specifies identity, stage coverage, gate responsibilities, and tier availability. Plug-and-play across projects.",
      tiers: [
        { l: "Advisor (SE4H)", c: "advisor" },
        { l: "Executor (SE4A)", c: "executor" },
        { l: "Support / Optional", c: "support" },
      ],
      items: [
        { role: "Router", name: "assistant", c: "support" },
        { role: "Advisor", name: "ceo", c: "advisor" },
        { role: "Advisor", name: "cto", c: "advisor" },
        { role: "Advisor", name: "cpo", c: "advisor" },
        { role: "Advisor", name: "cso", c: "advisor" },
        { role: "Executor", name: "coder", c: "executor" },
        { role: "Executor", name: "fullstack", c: "executor" },
        { role: "Executor", name: "architect", c: "executor" },
        { role: "Executor", name: "tester", c: "executor" },
        { role: "Executor", name: "reviewer", c: "executor" },
        { role: "Executor", name: "devops", c: "executor" },
        { role: "Executor", name: "pm", c: "executor" },
        { role: "Executor", name: "pjm", c: "executor" },
        { role: "Researcher", name: "researcher", c: "executor" },
        { role: "Optional", name: "writer", c: "support" },
        { role: "Optional", name: "sales", c: "support" },
        { role: "Optional", name: "cs", c: "support" },
        { role: "Optional", name: "itadmin", c: "support" },
      ],
    },
    training: {
      eyebrow: "11 Modules · 39 hours",
      title: "Train your whole team in one curriculum.",
      sub: "Real-incident-driven content. Each module ends with quiz + practical exercises. 80-question final assessment, 70% to pass.",
      items: [
        { i: "01", t: "SDLC Overview", sub: "10-Stage Lifecycle · 7 Pillars · 4-Tier Classification", h: "4h", tier: "ALL" },
        { i: "02", t: "Six Pillars Deep Dive", sub: "Design Thinking · Zero Mock · QA · Documentation", h: "6h", tier: "ALL" },
        { i: "03", t: "Zero Mock Policy", sub: "The 679 Mock Crisis · Real-services testing", h: "4h", tier: "STD+" },
        { i: "04", t: "Code Quality Standards", sub: "Coverage · Naming · OWASP · Performance", h: "4h", tier: "STD+" },
        { i: "05", t: "Development Workflow", sub: "Git · Conventional commits · 3-tier review · CI/CD", h: "4h", tier: "STD+" },
        { i: "06", t: "AI Tools in Practice", sub: "Claude Code · Local models · Design-to-code", h: "4h", tier: "ALL" },
        { i: "07", t: "SASE & Agentic SDLC", sub: "SE4H vs SE4A · 6 artifacts · L0–L3 maturity", h: "4h", tier: "PRO+" },
        { i: "08", t: "Authority & Decision Governance", sub: "Role boundaries · 13 decision types · Escalation", h: "2h", tier: "PRO+" },
        { i: "09", t: "Quality Gate Workshop", sub: "G0–G4 hands-on · Evidence upload · Common failures", h: "2h", tier: "STD+" },
        { i: "10", t: "ADR & Sprint Plan Workflow", sub: "When ADR is mandatory · Document-first culture", h: "2h", tier: "STD+" },
        { i: "11", t: "Remote Team Governance", sub: "Collaborator vs Fork · Remote escalation patterns", h: "1h", tier: "PRO+" },
      ]
    },
    refs: {
      eyebrow: "Reference implementations",
      title: "Methodology + Platforms. Each in its lane.",
      sub: "The Framework is tool-agnostic. Platforms implement the Framework. One Framework, many possible platforms.",
      endior: {
        badge: "LIVE · OPEN SOURCE",
        title: "Endiorbot",
        body: "Personal AI orchestration for solo developers. 14 SOUL agents across 5 channels. The first reference implementation of SDLC 6.3.1 — battle-tested, MIT-licensed, free forever.",
        stats: [["NEW", "just launched"], ["14", "SOUL agents"], ["5", "channels"], ["Sprint 145", "current"]],
        ctas: [["Visit endior.net", "https://endior.net"], ["GitHub →", "https://github.com/Minh-Tam-Solution/EndiorBot"]],
      },
      orch: {
        badge: "COMING Q3 2026 · COMMERCIAL",
        title: "SDLC Orchestrator",
        body: "Enterprise platform that automates Framework enforcement. Dynamic AGENTS.md, gate automation, evidence collection, audit trails. Built for regulated teams that need governance at scale.",
        stats: [["Q3", "2026 launch"], ["Enterprise", "tier focus"], ["Auto", "gate enforcement"], ["Pilot", "joining now"]],
        ctas: [["Joining pilot — contact taidt@mtsolution.com.vn", "mailto:taidt@mtsolution.com.vn"]],
      }
    },
    adopt: {
      eyebrow: "Adoption",
      title: "Three weeks from zero to compliant.",
      sub: "Don't try to adopt all 7 pillars in one sprint. The framework is designed to be adopted incrementally — start small, prove value, expand.",
      steps: [
        { day: "Day 1", num: "01", t: "Read the Executive Summary",
          d: "30 minutes. Understand 7 pillars, pick your tier, identify 1 stage to pilot." },
        { day: "Week 1", num: "02", t: "Pilot one feature",
          d: "Run a single feature through your chosen tier. Use templates verbatim. Don't customize yet." },
        { day: "Week 2", num: "03", t: "Add quality gates",
          d: "Wire G0–G4 into your CI/CD. Set Vibecoding Index to WARNING mode. Establish baseline." },
        { day: "Week 3", num: "04", t: "Train the team",
          d: "Run Modules 01 + 02 (10h). Switch governance to SOFT mode. Plan Module 06 for next month." },
      ]
    },
    standards: {
      eyebrow: "Standards alignment",
      title: "Plays nicely with what you already have.",
      sub: "SDLC 6.3.1 is a methodology, not a religion. It maps cleanly to industry standards your auditors already accept.",
      items: [
        ["CMMI v3.0", "Maturity levels (LITE = L1–2, ENTERPRISE = L4–5)"],
        ["SAFe 6.0", "Lean Governance concepts"],
        ["DORA Metrics", "Deployment Frequency · Lead Time · MTTR · CFR"],
        ["OWASP ASVS", "Security Verification Levels 1–3"],
        ["NIST SSDF", "Secure Development Framework"],
        ["ISO/IEC 12207", "Process group alignment"],
        ["Team Topologies", "4 fundamental team types"],
        ["Singapore AI Gov", "Model AI Governance Framework (Jan 2026)"],
      ]
    },
    faq: {
      eyebrow: "FAQ",
      title: "Honest answers.",
      items: [
        { q: "Is this another AI hype framework?",
          a: "No. SDLC 6.3.1 has been battle-tested in production across 14 platforms in the NQH Technology Ecosystem. Every pillar is derived from real incidents, not hypotheticals. The case studies (BFlow 4.2→4.3, MTEP, NQH-Bot) are documented in /06-Case-Studies/." },
        { q: "Do I need an AI tool to use this?",
          a: "No. The framework is tool-agnostic. You can run all 10 stages manually with your existing tools. Platforms (like SDLC Orchestrator) automate enforcement, but humans following this framework on paper still get the benefit." },
        { q: "How is this different from SAFe or CMMI?",
          a: "SAFe was written for human-only teams. CMMI predates LLMs. SDLC 6.3.1 was built BY AI+Human teams, FOR AI+Human teams. It treats AI as a first-class citizen with explicit governance (SE4H/SE4A, AGENTS.md, CRP/MRP/VCR) — not as a productivity hack." },
        { q: "Why MIT license?",
          a: "Methodologies improve through adoption and adversarial review. Locking SDLC behind a license would slow the feedback loop. The Framework is free; only platforms that automate it (Orchestrator) are commercial." },
        { q: "What's the relationship to Endiorbot?",
          a: "Endiorbot is the first reference implementation of this Framework. When you read about Pillar 5 (SASE) here, Endiorbot's 14 agents are exactly what that looks like in practice. The two projects are co-developed, dual-launched." },
        { q: "Will SDLC Orchestrator replace this Framework?",
          a: "Never. The Framework is the policy. The Orchestrator is one platform that automates the policy. Other platforms (custom CI/CD, future tools) can implement the same Framework. 1 Framework : N platforms." },
      ]
    },
    footer: {
      tag: "SDLC Enterprise Framework v6.3.1",
      sub: "Built BY AI+Human teams. FOR AI+Human teams. MIT licensed.",
      cols: [
        { t: "Framework", links: [["Executive Summary", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/01-Overview/SDLC-Executive-Summary.md"], ["Quick Reference", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/01-Overview/SDLC-Quick-Reference.md"], ["Core Methodology", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/02-Core-Methodology/SDLC-Core-Methodology.md"], ["Changelog", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/CHANGELOG.md"]] },
        { t: "Pillars", links: [["10-Stage Lifecycle", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md"], ["Quality Gates", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md"], ["SASE", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md"], ["Specifications", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md"]] },
        { t: "Resources", links: [["18 SOUL templates", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/tree/main/05-Templates-Tools/04-SASE-Artifacts/souls"], ["Case studies", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/tree/main/06-Case-Studies"], ["Training (39h)", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/tree/main/08-Training-Materials"], ["GitHub", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework"]] },
        { t: "Family", links: [["Endiorbot (live)", "https://endior.net"], ["SDLC Orchestrator (Q3 2026)", "mailto:taidt@mtsolution.com.vn?subject=SDLC%20Orchestrator%20Pilot"], ["MTS-SDLC-Lite", "https://github.com/Minh-Tam-Solution/MTS-SDLC-Lite"], ["TinySDLC", "https://github.com/Minh-Tam-Solution/tinysdlc"], ["AncestorTree", "https://github.com/Minh-Tam-Solution/AncestorTree"]] },
      ],
      auth: "CPO Office · taidt@mtsolution.com.vn · CTO Approved",
    }
  },
  vi: {
    nav: { framework: "Framework", endiorbot: "Endiorbot", orchestrator: "Orchestrator", lang: "VI" },
    hero: {
      eyebrow: "v6.3.1 · Tháng 4, 2026 · Giấy phép MIT",
      headline_a: "Phương pháp 7-trụ-cột cho",
      headline_em: "đội AI + Người",
      headline_b: "thực sự ship được sản phẩm.",
      sub: "Tool-agnostic. Đã kiểm chứng production. 503 tài liệu, 39 giờ đào tạo, 18 SOUL roles, 10 stages, 5 quality gates — tất cả mã nguồn mở.",
      ctaPrimary: "Đọc Executive Summary",
      ctaSecondary: "Xem reference: Endiorbot →",
      stat1: { n: "11", l: "modules đào tạo" },
      stat2: { n: "39h", l: "chương trình" },
      stat3: { n: "18", l: "SOUL roles" },
      stat4: { n: "10", l: "lifecycle stages" },
      stat5: { n: "503+", l: "tài liệu" },
    },
    promise: {
      eyebrow: "Lời cam kết",
      title: "Xây dựng BỞI đội AI+Người. CHO đội AI+Người.",
      body: "Hầu hết SDLC framework được viết trước khi LLM tồn tại. Chúng coi AI như công cụ gắn thêm. SDLC 6.3.1 bắt đầu từ tiền đề khác: con người định hướng, agent thực thi, con người xác minh — ở mọi giai đoạn, có bằng chứng, có gate, có trách nhiệm. Framework là phần còn lại sau khi loại bỏ mọi giả định rằng AI không tồn tại.",
    },
    pillars: {
      eyebrow: "Pillar 0 → 6 + Section 7 + 8",
      title: "Bảy trụ cột, hai mở rộng.",
      sub: "Mỗi trụ cột độc lập. Áp dụng một hay cả bảy — framework scale từ solo developer tới enterprise.",
      items: [
        { n: "P0", t: "Design Thinking", d: "Empathize → Define → Ideate → Prototype → Test. Xác minh vấn đề trước khi xây giải pháp. Cắt tỷ lệ lãng phí 70% mà ngành công nghệ vẫn âm thầm chấp nhận." },
        { n: "P1", t: "10-Stage Lifecycle", d: "Foundation → Govern. Mỗi stage có prerequisites, exit criteria và yêu cầu theo tier rõ ràng. Skip stage có chủ đích, không phải vô tình." },
        { n: "P2", t: "Sprint Governance", d: "Sprint 3-pha với TDD tích hợp sẵn. G-Sprint và G-Sprint-Close. Quy tắc tài liệu trong 24h. Mười nguyên tắc vàng cho sprint." },
        { n: "P3", t: "4-Tier Classification", d: "LITE (1-2 dev) → STANDARD → PROFESSIONAL → ENTERPRISE (50+). Tier quyết định stages bắt buộc, độ sâu tài liệu, tooling — không ngược lại." },
        { n: "P4", t: "Quality Gates", d: "Dual-track: feature (G0–G4) và sprint (G-Sprint). Pass dựa trên bằng chứng. Không có artifact, không pass. Vibecoding Index lượng hoá rủi ro." },
        { n: "P5", t: "SASE Integration", d: "Software Agent Software Engineering 3.0. SE4H (người hướng dẫn) vs SE4A (agent thực thi). AGENTS.md + CRP + MRP + VCR. Mô hình 13 vai trò chuẩn." },
        { n: "P6", t: "Documentation Permanence", d: "Định dạng AI-parseable. Bắt buộc YAML frontmatter. BDD (GIVEN-WHEN-THEN). Spec là nguồn sự thật duy nhất — không phải Slack." },
      ],
      sec7: { n: "§7", t: "Quality Assurance System", d: "Anti-Vibecoding controls. Vibecoding Index (0–100). Routing tiến triển: green tự động merge → red CTO duyệt. Auto-generation giảm friction từ 30 phút xuống dưới 5 phút mỗi PR." },
      sec8: { n: "§8", t: "Unified Specification Standard", d: "YAML frontmatter bắt buộc, BDD requirements, ADR nhẹ (DESIGN_DECISIONS), version tracking (SPEC_DELTA). SpecIR format-agnostic chuyển đổi OpenSpec ↔ SDLC hai chiều." },
    },
    stages: {
      eyebrow: "Pillar 1",
      title: "Mười stages. Mỗi stage hai câu hỏi.",
      sub: "Click vào bất kỳ stage để xem prerequisites, exit gate và deliverables chính.",
      data: [
        { id: "00", name: "Foundation", q: "TẠI SAO?", gate: "G0.1 / G0.2", reqs: "—", parallel: "Không",
          deliverables: [
            ["Câu hỏi", "Tại sao chúng ta xây cái này?"],
            ["Output", "Business case · Problem statement · 3 personas có bằng chứng"],
            ["Gate", "G0.1 (vấn đề được xác minh, 5+ users) → G0.2 (đa dạng giải pháp, 100+ ý tưởng)"],
            ["Rủi ro skip", "Critical — bỏ qua dẫn tới 70% lãng phí feature"],
          ]
        },
        { id: "01", name: "Planning", q: "CÁI GÌ?", gate: "G1", reqs: "00 + G0.2", parallel: "Không",
          deliverables: [
            ["Câu hỏi", "Chúng ta xây cái gì?"],
            ["Output", "Requirements · User stories · API specs · Acceptance criteria"],
            ["Định dạng", "BDD (GIVEN-WHEN-THEN) bắt buộc từ STANDARD trở lên"],
            ["Gate", "G1 — stakeholders duyệt, requirements đủ"],
          ]
        },
        { id: "02", name: "Design", q: "BẰNG CÁCH NÀO?", gate: "G2", reqs: "01 + G1", parallel: "Không",
          deliverables: [
            ["Câu hỏi", "Chúng ta xây bằng cách nào?"],
            ["Output", "Architecture · ADRs · Threat model · Security design"],
            ["Templates", "ADR-NNN, SPEC-NNNN với YAML frontmatter"],
            ["Gate", "G2 — CTO/Tech Lead duyệt"],
          ]
        },
        { id: "03", name: "Integrate", q: "Kết nối?", gate: "G2", reqs: "02 + G2", parallel: "Có (với 04)",
          deliverables: [
            ["Câu hỏi", "Hệ thống kết nối thế nào?"],
            ["Output", "API contracts · Integration tests · OpenAPI SSOT"],
            ["Cross-ref", "Stage 03 ↔ Stage 05 traceability matrix"],
            ["Pattern", "Song song với Build qua API-first development"],
          ]
        },
        { id: "04", name: "Build", q: "Đúng chưa?", gate: "G3", reqs: "02 + G2", parallel: "Có (với 03)",
          deliverables: [
            ["Câu hỏi", "Chúng ta đang xây đúng không?"],
            ["Output", "Code chạy được · Unit tests · Coverage đạt tier target"],
            ["TDD", "RED → GREEN → REFACTOR mỗi feature"],
            ["Coverage", "LITE 70% · STD 85% · PRO/ENT 95%"],
          ]
        },
        { id: "05", name: "Test", q: "Chạy đúng?", gate: "G3", reqs: "04 + G3", parallel: "Không",
          deliverables: [
            ["Câu hỏi", "Hệ thống chạy đúng không?"],
            ["Output", "Test reports · UAT sign-off · OWASP API Top-10"],
            ["Workflow", "6-pha E2E: Discovery → Config → Execution → Security → Reporting → Integration"],
            ["Tiết kiệm", "~83% thời gian setup so với test ad-hoc"],
          ]
        },
        { id: "06", name: "Deploy", q: "Ship?", gate: "G4", reqs: "05 + G3", parallel: "Không",
          deliverables: [
            ["Câu hỏi", "Ship sao cho an toàn?"],
            ["Output", "Release notes · Rollback procedures · Deployment evidence"],
            ["Checklist", "100-mục Go-Live Readiness (theo tier)"],
            ["Gate", "G4 — production ổn định"],
          ]
        },
        { id: "07", name: "Operate", q: "Đang chạy?", gate: "Continuous", reqs: "06 + G4", parallel: "Có",
          deliverables: [
            ["Câu hỏi", "Hệ thống chạy ổn không?"],
            ["Output", "Runbooks · Monitoring dashboards · SLO definitions"],
            ["Metrics", "DORA: deployment frequency, lead time, MTTR, CFR"],
            ["Mục tiêu", "99.9%+ uptime ở tier PRO/ENT"],
          ]
        },
        { id: "08", name: "Collaborate", q: "Hiệu quả?", gate: "Continuous", reqs: "01+", parallel: "Có",
          deliverables: [
            ["Câu hỏi", "Đội nhóm có hiệu quả không?"],
            ["Output", "Team charter · AGENTS.md · Tài liệu đào tạo"],
            ["Roles", "Mô hình SASE 13 vai trò + 10 TEAM charters"],
            ["Pattern", "Chạy xuyên suốt — không bao giờ block delivery"],
          ]
        },
        { id: "09", name: "Govern", q: "Tuân thủ?", gate: "Continuous", reqs: "06 + G4", parallel: "Có",
          deliverables: [
            ["Câu hỏi", "Có tuân thủ không?"],
            ["Output", "Compliance reports · Audit logs · Risk register"],
            ["Standards", "SOC 2 · HIPAA · GDPR · NIST SSDF"],
            ["Bắt đầu sớm", "Có thể bắt đầu từ Stage 01 nếu là ngành quản lý chặt"],
          ]
        },
      ]
    },
    tiers: {
      eyebrow: "Pillar 3",
      title: "Một framework. Bốn tier.",
      sub: "Chọn tier phù hợp với đội — đừng chọn tier cao hơn năng lực hiện tại. Framework scale xuống cũng nhẹ nhàng như scale lên.",
      items: [
        { lvl: "T1", name: "LITE", who: "1–2 dev · Solo · Indie", stages: "00, 01, 02, 04",
          features: ["3 SOUL roles", "README + .env.example", "70% test coverage", "AGENTS.md <60 dòng"], rec: false },
        { lvl: "T2", name: "STANDARD", who: "3–10 dev · Startup · Agency nhỏ", stages: "00–02, 04–06",
          features: ["6 SOUL roles", "+ CLAUDE.md + /docs", "85% test coverage", "BDD requirements"], rec: true },
        { lvl: "T3", name: "PROFESSIONAL", who: "10–50 dev · Growth-stage", stages: "Cả 10 stages",
          features: ["11 SOUL roles", "+ Full ADRs + Compliance", "95% test coverage", "Senior review board"], rec: false },
        { lvl: "T4", name: "ENTERPRISE", who: "50+ dev · Quản lý chặt · Đại chúng", stages: "Cả 10 stages",
          features: ["14 SOUL roles", "+ Executive reports + Audit", "95%+ + security tests", "Tất cả sections"], rec: false },
      ]
    },
    gates: {
      eyebrow: "Pillar 4",
      title: "Năm gates. Có bằng chứng mới qua.",
      sub: "Quality gate không phải sự đồng ý — là điểm kiểm tra bằng chứng. Không có artifact, gate không pass.",
      items: [
        { id: "G0", phase: "Foundation", title: "Vấn đề & Giải pháp được xác minh",
          ev: ["5+ user interviews có tài liệu", "100+ ý tưởng, chọn top 3", "Personas có bằng chứng"] },
        { id: "G1", phase: "Planning", title: "Requirements đầy đủ",
          ev: ["BDD requirements đã viết", "Stakeholders duyệt", "Acceptance criteria đo được"] },
        { id: "G2", phase: "Design", title: "Architecture được duyệt",
          ev: ["ADR được CTO/Tech Lead duyệt", "Threat model đầy đủ", "API contracts trong version control"] },
        { id: "G3", phase: "Build · Test", title: "Sẵn sàng ship",
          ev: ["Đạt coverage theo tier (70/85/95%)", "OWASP API Top-10 đã check", "MRP submit cho >100 LOC"] },
        { id: "G4", phase: "Deploy · Operate", title: "Production ổn định",
          ev: ["Rollback đã test", "Monitoring dashboards live", "SLO định nghĩa và theo dõi"] },
      ]
    },
    vibe: {
      eyebrow: "Section 7",
      title: "Vibecoding Index.",
      body: "Code 'vibe' viết nhanh, bảo trì tốn kém. Index lượng hoá rủi ro trên thang 0–100 qua năm signal có trọng số, sau đó route mỗi PR đến đúng người review.",
      signals: [
        { l: "Intent Clarity", w: "30%" },
        { l: "Code Ownership Confidence", w: "25%" },
        { l: "Context Completeness", w: "20%" },
        { l: "AI Attestation Rate", w: "15%" },
        { l: "Historical Rejection Rate", w: "10%" },
      ],
      routing: [
        { range: "0–19", label: "Green", action: "Auto-merge · 1+ approvals" },
        { range: "20–39", label: "Yellow", action: "Tech Lead spot-check" },
        { range: "40–59", label: "Orange", action: "CEO optional · Senior review" },
        { range: "60–100", label: "Red", action: "Senior Review Board · CTO override" },
      ]
    },
    souls: {
      eyebrow: "Pillar 5 · SASE 13-Role Model",
      title: "Mười tám role templates. Pre-tuned, đã chinh chiến.",
      sub: "Mỗi SOUL chỉ định identity, stage coverage, gate responsibilities và tier availability. Plug-and-play giữa các project.",
      tiers: [
        { l: "Advisor (SE4H)", c: "advisor" },
        { l: "Executor (SE4A)", c: "executor" },
        { l: "Support / Optional", c: "support" },
      ],
      items: [
        { role: "Router", name: "assistant", c: "support" },
        { role: "Advisor", name: "ceo", c: "advisor" },
        { role: "Advisor", name: "cto", c: "advisor" },
        { role: "Advisor", name: "cpo", c: "advisor" },
        { role: "Advisor", name: "cso", c: "advisor" },
        { role: "Executor", name: "coder", c: "executor" },
        { role: "Executor", name: "fullstack", c: "executor" },
        { role: "Executor", name: "architect", c: "executor" },
        { role: "Executor", name: "tester", c: "executor" },
        { role: "Executor", name: "reviewer", c: "executor" },
        { role: "Executor", name: "devops", c: "executor" },
        { role: "Executor", name: "pm", c: "executor" },
        { role: "Executor", name: "pjm", c: "executor" },
        { role: "Researcher", name: "researcher", c: "executor" },
        { role: "Optional", name: "writer", c: "support" },
        { role: "Optional", name: "sales", c: "support" },
        { role: "Optional", name: "cs", c: "support" },
        { role: "Optional", name: "itadmin", c: "support" },
      ],
    },
    training: {
      eyebrow: "11 Modules · 39 giờ",
      title: "Đào tạo cả đội bằng một chương trình.",
      sub: "Nội dung từ sự cố thật. Mỗi module có quiz + bài tập thực hành. Đánh giá cuối 80 câu, đạt 70% là pass.",
      items: [
        { i: "01", t: "SDLC Overview", sub: "10-Stage Lifecycle · 7 Pillars · 4-Tier Classification", h: "4h", tier: "ALL" },
        { i: "02", t: "Six Pillars Deep Dive", sub: "Design Thinking · Zero Mock · QA · Documentation", h: "6h", tier: "ALL" },
        { i: "03", t: "Zero Mock Policy", sub: "Khủng hoảng 679 Mock · Test với real services", h: "4h", tier: "STD+" },
        { i: "04", t: "Code Quality Standards", sub: "Coverage · Naming · OWASP · Performance", h: "4h", tier: "STD+" },
        { i: "05", t: "Development Workflow", sub: "Git · Conventional commits · 3-tier review · CI/CD", h: "4h", tier: "STD+" },
        { i: "06", t: "AI Tools trong thực tế", sub: "Claude Code · Local models · Design-to-code", h: "4h", tier: "ALL" },
        { i: "07", t: "SASE & Agentic SDLC", sub: "SE4H vs SE4A · 6 artifacts · L0–L3 maturity", h: "4h", tier: "PRO+" },
        { i: "08", t: "Authority & Decision Governance", sub: "Role boundaries · 13 decision types · Escalation", h: "2h", tier: "PRO+" },
        { i: "09", t: "Quality Gate Workshop", sub: "G0–G4 hands-on · Upload bằng chứng · Lỗi phổ biến", h: "2h", tier: "STD+" },
        { i: "10", t: "ADR & Sprint Plan Workflow", sub: "Khi nào ADR bắt buộc · Document-first culture", h: "2h", tier: "STD+" },
        { i: "11", t: "Remote Team Governance", sub: "Collaborator vs Fork · Escalation pattern remote", h: "1h", tier: "PRO+" },
      ]
    },
    refs: {
      eyebrow: "Reference implementations",
      title: "Methodology + Platforms. Mỗi cái một làn.",
      sub: "Framework tool-agnostic. Platform thực thi Framework. Một Framework, nhiều platform khả thi.",
      endior: {
        badge: "LIVE · MÃ NGUỒN MỞ",
        title: "Endiorbot",
        body: "AI orchestration cá nhân cho lập trình viên solo. 14 SOUL agents qua 5 kênh. Reference implementation đầu tiên của SDLC 6.3.1 — đã chinh chiến, MIT, miễn phí mãi mãi.",
        stats: [["MỚI", "vừa launched"], ["14", "SOUL agents"], ["5", "kênh"], ["Sprint 145", "hiện tại"]],
        ctas: [["Vào endior.net", "https://endior.net"], ["GitHub →", "https://github.com/Minh-Tam-Solution/EndiorBot"]],
      },
      orch: {
        badge: "RA MẮT Q3 2026 · THƯƠNG MẠI",
        title: "SDLC Orchestrator",
        body: "Nền tảng enterprise tự động hoá Framework. Dynamic AGENTS.md, gate automation, thu thập bằng chứng, audit trails. Dành cho team quản lý chặt cần governance ở quy mô lớn.",
        stats: [["Q3", "ra mắt 2026"], ["Enterprise", "tier focus"], ["Auto", "gate enforcement"], ["Pilot", "đang mở"]],
        ctas: [["Tham gia pilot — liên hệ taidt@mtsolution.com.vn", "mailto:taidt@mtsolution.com.vn"]],
      }
    },
    adopt: {
      eyebrow: "Áp dụng",
      title: "Ba tuần từ zero tới compliant.",
      sub: "Đừng cố áp dụng cả 7 trụ cột trong một sprint. Framework thiết kế để adopt từng phần — bắt đầu nhỏ, chứng minh giá trị, mở rộng.",
      steps: [
        { day: "Ngày 1", num: "01", t: "Đọc Executive Summary",
          d: "30 phút. Hiểu 7 trụ cột, chọn tier, xác định 1 stage để pilot." },
        { day: "Tuần 1", num: "02", t: "Pilot một feature",
          d: "Chạy một feature qua tier đã chọn. Dùng template y nguyên. Chưa customize." },
        { day: "Tuần 2", num: "03", t: "Thêm quality gates",
          d: "Wire G0–G4 vào CI/CD. Set Vibecoding Index ở chế độ WARNING. Lập baseline." },
        { day: "Tuần 3", num: "04", t: "Đào tạo đội",
          d: "Chạy Module 01 + 02 (10h). Chuyển governance sang chế độ SOFT. Lên kế hoạch Module 06 cho tháng sau." },
      ]
    },
    standards: {
      eyebrow: "Chuẩn ngành",
      title: "Tương thích với mọi thứ bạn đã có.",
      sub: "SDLC 6.3.1 là phương pháp, không phải tôn giáo. Map sạch sẽ với các chuẩn ngành mà auditor đã chấp nhận.",
      items: [
        ["CMMI v3.0", "Maturity levels (LITE = L1–2, ENTERPRISE = L4–5)"],
        ["SAFe 6.0", "Lean Governance concepts"],
        ["DORA Metrics", "Deployment Frequency · Lead Time · MTTR · CFR"],
        ["OWASP ASVS", "Security Verification Levels 1–3"],
        ["NIST SSDF", "Secure Development Framework"],
        ["ISO/IEC 12207", "Process group alignment"],
        ["Team Topologies", "4 loại team cơ bản"],
        ["Singapore AI Gov", "Model AI Governance Framework (1/2026)"],
      ]
    },
    faq: {
      eyebrow: "FAQ",
      title: "Trả lời thẳng thắn.",
      items: [
        { q: "Đây có phải framework AI hype nữa không?",
          a: "Không. SDLC 6.3.1 đã được battle-test ở production qua 14 platform trong NQH Technology Ecosystem. Mỗi trụ cột bắt nguồn từ sự cố thật, không phải giả định. Case studies (BFlow 4.2→4.3, MTEP, NQH-Bot) có tài liệu trong /06-Case-Studies/." },
        { q: "Có cần AI tool để dùng framework này không?",
          a: "Không. Framework tool-agnostic. Có thể chạy thủ công cả 10 stages với công cụ hiện có. Platform (như SDLC Orchestrator) tự động hoá enforcement, nhưng người làm theo framework trên giấy vẫn được hưởng lợi." },
        { q: "Khác gì SAFe hoặc CMMI?",
          a: "SAFe viết cho team chỉ có người. CMMI có trước LLM. SDLC 6.3.1 được xây BỞI đội AI+Người, CHO đội AI+Người. Coi AI là công dân hạng nhất với governance rõ ràng (SE4H/SE4A, AGENTS.md, CRP/MRP/VCR) — không phải mẹo tăng productivity." },
        { q: "Vì sao MIT?",
          a: "Methodology cải thiện qua adoption và phản biện. Khoá SDLC sau license sẽ làm chậm feedback loop. Framework miễn phí; chỉ platform tự động hoá nó (Orchestrator) là thương mại." },
        { q: "Quan hệ với Endiorbot là gì?",
          a: "Endiorbot là reference implementation đầu tiên của Framework. Khi đọc về Pillar 5 (SASE) ở đây, 14 agents của Endiorbot chính là hình hài thực tế. Hai project co-developed, dual-launch." },
        { q: "SDLC Orchestrator có thay thế Framework này không?",
          a: "Không bao giờ. Framework là chính sách. Orchestrator là một platform tự động hoá chính sách đó. Platform khác (custom CI/CD, công cụ tương lai) có thể implement cùng Framework. 1 Framework : N platforms." },
      ]
    },
    footer: {
      tag: "SDLC Enterprise Framework v6.3.1",
      sub: "Xây BỞI đội AI+Người. CHO đội AI+Người. MIT licensed.",
      cols: [
        { t: "Framework", links: [["Executive Summary", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/01-Overview/SDLC-Executive-Summary.md"], ["Quick Reference", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/01-Overview/SDLC-Quick-Reference.md"], ["Core Methodology", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/02-Core-Methodology/SDLC-Core-Methodology.md"], ["Changelog", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/CHANGELOG.md"]] },
        { t: "Pillars", links: [["10-Stage Lifecycle", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md"], ["Quality Gates", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md"], ["SASE", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md"], ["Specifications", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/blob/main/05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md"]] },
        { t: "Resources", links: [["18 SOUL templates", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/tree/main/05-Templates-Tools/04-SASE-Artifacts/souls"], ["Case studies", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/tree/main/06-Case-Studies"], ["Training (39h)", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/tree/main/08-Training-Materials"], ["GitHub", "https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework"]] },
        { t: "Family", links: [["Endiorbot (live)", "https://endior.net"], ["SDLC Orchestrator (Q3 2026)", "mailto:taidt@mtsolution.com.vn?subject=SDLC%20Orchestrator%20Pilot"], ["MTS-SDLC-Lite", "https://github.com/Minh-Tam-Solution/MTS-SDLC-Lite"], ["TinySDLC", "https://github.com/Minh-Tam-Solution/tinysdlc"], ["AncestorTree", "https://github.com/Minh-Tam-Solution/AncestorTree"]] },
      ],
      auth: "CPO Office · taidt@mtsolution.com.vn · CTO Approved",
    }
  }
};
window.sdlcCopy = sdlcCopy;
