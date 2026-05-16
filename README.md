```
╔═══════════════════════════════════════════════════════════════╗
║         Saudi Legal AI Framework                              ║
║         إطار الذكاء الاصطناعي للقانون السعودي               ║
║                                                               ║
║   Adapting AI assistants to the Saudi legal environment       ║
║   تكييف مساعدات الذكاء الاصطناعي مع البيئة القانونية السعودية ║
╚═══════════════════════════════════════════════════════════════╝
```
<p align="center">
  <img src="assets/cover.png" alt="Saudi Legal AI Framework" width="100%">
</p>

[![Validate Datasets](https://github.com/Samix2026/saudi-legal-ai-framework/actions/workflows/validate-datasets.yml/badge.svg)](https://github.com/Samix2026/saudi-legal-ai-framework/actions/workflows/validate-datasets.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)](ROADMAP.md)
[![Language: AR | EN](https://img.shields.io/badge/Language-Arabic%20%7C%20English-orange.svg)]()
[![AI: Claude | ChatGPT | Gemini](https://img.shields.io/badge/AI-Claude%20%7C%20ChatGPT%20%7C%20Gemini-purple.svg)]()

---

## ⚠️ Legal Disclaimer / إخلاء مسؤولية قانوني

> **بالعربية:** هذا الإطار أداة مساعدة للبحث والتحليل الأولي **فقط**. لا يُعدّ أي مخرج ينتج عنه استشارةً قانونية، ولا يُغني عن الرجوع إلى محامٍ مرخّص في المملكة العربية السعودية. **استخدم هذا الإطار تحت إشراف مختص قانوني مؤهل دائمًا.**

> **In English:** This framework is a research and preliminary analysis tool **only**. No AI output produced using this framework constitutes legal advice or replaces consultation with a licensed attorney in the Kingdom of Saudi Arabia. **Always use this framework under the supervision of a qualified legal professional.**

---

## Overview / نظرة عامة

Most large AI models are trained predominantly on Western (U.S. and European) legal material. When applied to the Saudi context, they produce errors that range from misleading to harmful — citing inapplicable legal concepts, ignoring mandatory local regulations, and misidentifying competent courts.

This project addresses that gap. It is a structured, open-source collection of **skills**, **prompt templates**, **legal source references**, and **worked examples** that give AI assistants the context they need to reason correctly about Saudi law — while making clear what AI can and cannot do in a legal setting.

معظم نماذج الذكاء الاصطناعي الكبرى مُدرَّبة على مواد قانونية غربية بالدرجة الأولى. عند تطبيقها في السياق السعودي، تُنتج أخطاءً تتراوح بين المضلِّل والضار. هذا المشروع يُعالج تلك الفجوة بتوفير إطار منظَّم ومفتوح المصدر من المهارات وقوالب المطالبات والمصادر التشريعية والأمثلة التطبيقية.

---

## Why Saudi Legal AI Matters / لماذا هذا المشروع مهم

The Saudi legal system has a distinct foundation that most AI models handle poorly:

- **Islamic Sharia** is the primary source of law — not civil codes or common law
- **Royal Decrees** are the main legislative instrument, not parliamentary statutes
- **Specialized courts** (Labor, Commercial, Administrative) have exclusive jurisdiction over distinct dispute types
- **Mandatory provisions** in labor, data protection, and company law cannot be contracted out of
- **Arabic is the authoritative language** for official legal texts — English translations are unofficial

When an AI assistant defaults to Western legal reasoning in a Saudi context, it can lead professionals to draw wrong conclusions about their rights, obligations, and legal exposure.

---

## Features / المميزات

| Feature | Description |
|---------|-------------|
| **Saudi-first reasoning** | Skills and prompts are grounded in Saudi law — not adapted from Western templates |
| **Bilingual (AR / EN)** | All content is structured in both Arabic and English |
| **Multi-model compatible** | Works with Claude, ChatGPT, Gemini, and any instruction-following LLM |
| **Modular structure** | Use only the components relevant to your task |
| **Source-referenced** | Every legal claim points to an official Saudi source |
| **Disclaimer-enforced** | Every output template includes mandatory legal disclaimer language |
| **No code required** | Pure documentation — usable without any technical setup |

---

## Project Status / حالة المشروع

```
Phase 1 — Foundation        ██████████   Complete
Phase 2 — Knowledge Base    ███████░░░   Advanced In Progress
Phase 3 — AI Workflows      ████░░░░░░   Foundation Established
Phase 4 — MCP Integration   █░░░░░░░░░   Research / Early Planning
Phase 5 — Product Layer     ░░░░░░░░░░   Planned
```

**Phase 1 includes:** repository architecture · governance · validation pipeline · CI/CD · contributor workflows · automated testing · verification lifecycle · scalable dataset structure

**Phase 2 includes:** regulation registry · datasets · enums · legal references · Saudi legal sources · example scenarios · judicial corpus · judicial indexing framework · reasoning extraction framework · verification lifecycle · open-data sources
**Phase 2 remaining:** broader coverage · verified references · larger datasets

**Phase 3 includes:** standardized legal skills · unified output formats · workflow templates · reasoning-oriented data structures · system architecture documentation
**Phase 3 remaining:** orchestration · evaluations · reasoning chains · agent workflows

**Phase 4 early planning includes:** OCR strategy · future ingestion pipelines · future API integrations · future retrieval architecture

See [ROADMAP.md](ROADMAP.md) for the full plan and task breakdown.

---

## Architecture Overview / هيكل المشروع

```
saudi-legal-ai-framework/
│
├── README.md                              # Project overview (this file)
├── CLAUDE.md                              # Guidance for Claude Code users
├── ROADMAP.md                             # Project phases and task tracking
│
├── skills/                                # How AI should reason in each legal domain
│   ├── contract-review.md
│   ├── labor-law-analysis.md
│   ├── commercial-dispute.md
│   ├── compliance-check.md
│   └── legal-drafting.md
│
├── sources/                               # Reference summaries of key Saudi regulations
│   ├── saudi-laws.md
│   ├── labor-law.md
│   ├── companies-law.md
│   ├── commercial-courts.md
│   ├── pdpl.md
│   ├── regulation-index.md                # Authoritative citation registry for all regulations
│   ├── open-data-judicial-sources.md      # Saudi open data — supplementary statistics only
│   └── judicial-decisions/                # Scanned PDF volumes of Saudi court decisions
│       └── 1435/                          # Hijri year — 14 PDF volumes
│
├── datasets/                              # Structured legal datasets
│   ├── saudi-contract-risk-dataset.csv    # Master dataset
│   ├── schema.md                          # 16-column schema definition
│   ├── enums/                             # Controlled vocabularies (risk, contract, clause, industry)
│   ├── examples/                          # Sector-specific example CSVs
│   ├── contributions/                     # One-file-per-contributor staging area
│   ├── build/                             # Generated merged output (CI-produced)
│   ├── judicial-reasoning/                # Structured extraction from court decisions
│   │   ├── schema.md                      # 19-field extraction schema
│   │   ├── example-extraction.md          # Teaching example with walkthrough
│   │   └── extraction-guidelines.md       # Redaction, anonymization, extraction rules
│   └── judicial-index/                    # PDF section index — before extraction
│       ├── schema.md                      # 13-field indexing schema
│       ├── judicial-corpus-index.csv      # Section-level map of PDF volumes
│       └── README.md
│
├── prompts/                               # Ready-to-use prompt templates
│   ├── review-contract.md
│   ├── draft-notice.md
│   └── risk-analysis.md
│
├── examples/                              # Annotated worked examples
│   ├── employment-contract-review.md
│   └── nda-review.md
│
├── docs/                                  # Architecture, governance, and planning documents
│   ├── system-architecture.md             # Full system layer map and data lifecycle
│   ├── cross-reference-map.md             # File dependency map — what to update when
│   ├── legal-verification-lifecycle.md    # Verification states and transition rules
│   └── official-api-sources.md            # Saudi government Real-Time APIs — future integration
│
└── scripts/                               # Validation and build automation
    ├── validate_dataset.py
    └── build_dataset.py
```

**Design principle:** Each layer is independent. Use a single prompt template without reading the skills files, or combine all layers for a richer context.

For a complete description of each layer, the data lifecycle, and the planned future architecture, see [docs/system-architecture.md](docs/system-architecture.md).

---

## Current Architecture Layers / طبقات المعمارية الحالية

| Layer | Directory | Status | Description |
|-------|-----------|--------|-------------|
| **Legislative Sources** | `sources/` | Active | Reference summaries of Saudi regulations with official citations |
| **Judicial Corpus** | `sources/judicial-decisions/` | Active — Indexing | Scanned PDF volumes of Saudi court decisions (14 files, 1435H) |
| **Corpus Index** | `datasets/judicial-index/` | Active — In Progress | Section-level map of PDF volumes before extraction |
| **Judicial Extraction** | `datasets/judicial-reasoning/` | Framework Ready | Structured 19-field extraction schema — awaiting indexed sections |
| **Contract Datasets** | `datasets/` | Active | 16-column CSV schema with verification lifecycle |
| **AI Skills** | `skills/` | Active | Domain-specific reasoning guides for AI assistants |
| **Prompt Templates** | `prompts/` | Active | Self-contained, model-neutral prompt templates |
| **Worked Examples** | `examples/` | Active | Annotated walkthroughs for reference |
| **Future: OCR Layer** | — | Planned | Text extraction from scanned judicial PDFs |
| **Future: RAG Layer** | — | Planned | Retrieval-augmented generation over verified content |
| **Future: Agent Layer** | — | Planned | Orchestrated multi-step legal analysis workflows |

See [docs/system-architecture.md](docs/system-architecture.md) for the full layer map, [datasets/judicial-index/](datasets/judicial-index/) for corpus indexing progress, and [datasets/judicial-reasoning/](datasets/judicial-reasoning/) for the extraction framework.

---

## Supported AI Assistants / نماذج الذكاء الاصطناعي المدعومة

This framework is model-agnostic. It has been designed to work with:

| Model | How to Use |
|-------|------------|
| **Claude** (Anthropic) | Open project in Claude Code, or paste skill file content at the start of a conversation |
| **ChatGPT** (OpenAI) | Paste skill file as a System Prompt or at the top of the conversation |
| **Gemini** (Google) | Include skill file content in the initial context window |
| **Any instruction-following LLM** | Same approach — paste the relevant skill and prompt template |

The prompts in `prompts/` are written to be self-contained and model-neutral.

---

## Quick Start / البدء السريع

**No installation required.** This is a documentation framework.

### Option 1 — Use a single prompt template
1. Open any file in `prompts/`
2. Copy the template that matches your task
3. Paste it into your AI assistant of choice
4. Replace the placeholder variables (e.g. `[CONTRACT_TEXT]`)

### Option 2 — Full context (recommended for complex tasks)
1. Open the relevant `skills/` file and paste its content as system context
2. Add the relevant `sources/` file for deeper regulatory grounding
3. Use the matching `prompts/` template as your user message
4. Review any AI output with a licensed Saudi legal professional

### Option 3 — Claude Code users
```bash
git clone https://github.com/Samix2026/saudi-legal-ai-framework.git
cd saudi-legal-ai-framework
# Open in Claude Code — CLAUDE.md loads automatically as project context
```

---

## Example Workflows / أمثلة على سير العمل

### مراجعة عقد عمل / Reviewing an Employment Contract
```
1. context  → skills/labor-law-analysis.md
2. source   → sources/labor-law.md
3. prompt   → prompts/review-contract.md (employment contract template)
4. example  → examples/employment-contract-review.md
```
The AI will check mandatory clauses, flag non-compliant provisions (e.g. annual leave below the 21-day minimum), and identify clauses that Saudi courts would override regardless of what the contract says.

---

### فحص الامتثال لـ PDPL / PDPL Compliance Check
```
1. context  → skills/compliance-check.md
2. source   → sources/pdpl.md
3. prompt   → prompts/risk-analysis.md (operational risk template)
```
The AI will assess data processing activities against PDPL requirements, flag gaps in privacy policy, cross-border transfer compliance, and breach notification procedures.

---

### تحليل مخاطر نزاع تجاري / Commercial Dispute Risk Analysis
```
1. context  → skills/commercial-dispute.md
2. source   → sources/commercial-courts.md
3. prompt   → prompts/risk-analysis.md (M&A or general dispute template)
```
The AI will identify the competent court, assess the strength of each party's position, and outline resolution options from negotiated settlement to Commercial Court litigation.

---

## Guiding Principles / المبادئ التوجيهية

| Principle | What it means in practice |
|-----------|--------------------------|
| **Saudi law first** | Islamic Sharia + Royal Decrees are the baseline — never Western civil law defaults |
| **No false confidence** | AI output uses hedged language ("may be", "could raise") — never categorical legal rulings |
| **Human oversight required** | Every output template mandates review by a licensed Saudi attorney |
| **Source transparency** | Legal claims reference specific regulations by decree number and article |
| **Arabic is authoritative** | Where Arabic and English conflict in any document, Arabic governs |
| **Jurisdiction awareness** | Competent court or authority is always identified (Labor, Commercial, Administrative) |

---

## Future Vision / الرؤية المستقبلية

This project is built in phases toward a practical tool that legal professionals in Saudi Arabia can rely on for preliminary research and analysis.

**Near-term (v0.2 — v1.0):**
Completing the knowledge base for the five major regulatory areas, adding worked examples across more sectors (real estate, technology, healthcare), and having the content reviewed by licensed Saudi legal professionals.

**Medium-term (v2.0):**
MCP server integrations that connect AI assistants directly to official Saudi legal sources — retrieving current regulatory text, flagging recent amendments, and grounding analysis in verified, up-to-date content.

**Long-term (v3.0):**
A web interface that allows legal professionals and organizations to upload documents, run structured analyses, and generate formatted review reports — without requiring any technical knowledge.

The project will not pursue automated legal advice at any stage. The goal is to make preliminary legal research faster and more accurate, not to replace legal judgment.

---

## Contribution Guide / دليل المساهمة

Contributions are welcome from legal professionals, researchers, and developers.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide, including dataset standards, citation formats, anonymization requirements, and the pre-submission checklist.

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing. To report a security issue (e.g. non-anonymized client data), see [SECURITY.md](SECURITY.md).

### Before you contribute
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for content standards, enum rules, and legal accuracy requirements
- Review [ROADMAP.md](ROADMAP.md) to see what is planned and what is in progress
- Open an **Issue** to discuss any significant addition before submitting a Pull Request

### What we need most
**Legal accuracy review** — If you are a licensed Saudi attorney, reviewing and correcting the content in `sources/` and `skills/` is the highest-value contribution this project can receive.

**Regulatory updates** — Saudi regulations change frequently. If a regulation has been amended and a file in `sources/` is outdated, please open an Issue or submit a correction with the official reference.

**Additional examples** — Realistic worked examples in `examples/` across different sectors (real estate, technology, healthcare, construction).

### Contribution standards
- Every legal claim must cite an official Saudi source (decree number, article, issuing authority)
- New content must include the bilingual legal disclaimer in both Arabic and English
- Do not introduce Western legal assumptions — if uncertain, note the uncertainty explicitly
- Pull Request descriptions must explain what changed and why, with source references

### What we are not looking for
- AI-generated legal text presented as authoritative
- Content adapted from Western legal templates without Saudi-specific grounding
- Speculative interpretations not supported by official sources

---

## Official Sources / المصادر الرسمية

| Source | URL | Content |
|--------|-----|---------|
| هيئة الخبراء بمجلس الوزراء | [boe.gov.sa](https://boe.gov.sa) | Official regulations and laws |
| الجريدة الرسمية (أم القرى) | [uqn.gov.sa](https://uqn.gov.sa) | Official Gazette — authoritative text |
| منصة استطلاع | [istitlaa.ncc.gov.sa](https://istitlaa.ncc.gov.sa) | Draft regulations under public consultation |
| وزارة العدل | [moj.gov.sa](https://www.moj.gov.sa) | Ministry of Justice |
| منصة ناجز | [najiz.sa](https://www.najiz.sa) | Electronic judicial services |
| وزارة الموارد البشرية والتنمية الاجتماعية | [hrsd.gov.sa](https://www.hrsd.gov.sa) | Labor and HR regulations |
| هيئة السوق المالية | [cma.org.sa](https://www.cma.org.sa) | Capital Markets Authority |
| سدايا | [sdaia.gov.sa](https://sdaia.gov.sa) | Data and AI authority — PDPL regulator |
| منصة البيانات المفتوحة السعودية | [open.data.gov.sa](https://open.data.gov.sa) | Judicial & government open datasets — statistics, patterns, metadata (supplementary only) |

---

## Project Documentation / وثائق المشروع

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview — start here |
| [ROADMAP.md](ROADMAP.md) | Phase plan, task tracking, versioning |
| [CLAUDE.md](CLAUDE.md) | Standards and guidance for Claude Code users |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guide — datasets, citations, PRs |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community standards and expected behaviour |
| [SECURITY.md](SECURITY.md) | How to report security issues and data incidents |
| [docs/cross-reference-map.md](docs/cross-reference-map.md) | File dependency map — what to update when you change something |
| [sources/open-data-judicial-sources.md](sources/open-data-judicial-sources.md) | Saudi open data sources — judicial statistics and practice signals |
| [docs/official-api-sources.md](docs/official-api-sources.md) | Saudi government Real-Time APIs — future architecture and governance |
| [datasets/judicial-reasoning/schema.md](datasets/judicial-reasoning/schema.md) | Judicial reasoning extraction schema — 19-field structured format |
| [datasets/judicial-reasoning/extraction-guidelines.md](datasets/judicial-reasoning/extraction-guidelines.md) | Extraction and redaction guidelines for judicial decisions |
| [datasets/judicial-index/judicial-corpus-index.csv](datasets/judicial-index/judicial-corpus-index.csv) | Judicial corpus index — section-level map of PDF volumes before extraction |

---

## License / الترخيص

MIT License — free to use, modify, and distribute with attribution and retention of the legal disclaimer.

This license does not grant any right to represent AI outputs produced using this framework as legal advice.
