```
╔═══════════════════════════════════════════════════════════════╗
║         Saudi Legal AI Framework                              ║
║         إطار الذكاء الاصطناعي للقانون السعودي               ║
║                                                               ║
║   Adapting AI assistants to the Saudi legal environment       ║
║   تكييف مساعدات الذكاء الاصطناعي مع البيئة القانونية السعودية ║
╚═══════════════════════════════════════════════════════════════╝
```

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
Phase 1 — Foundation        ████████░░   In Progress   v0.1 published
Phase 2 — Knowledge Base    ██░░░░░░░░   Planned
Phase 3 — AI Workflows      ░░░░░░░░░░   Planned
Phase 4 — MCP Integration   ░░░░░░░░░░   Planned
Phase 5 — Product Layer     ░░░░░░░░░░   Planned
```

See [ROADMAP.md](ROADMAP.md) for the full plan and task breakdown.

---

## Architecture Overview / هيكل المشروع

```
saudi-legal-ai-framework/
│
├── README.md                         # Project overview (this file)
├── CLAUDE.md                         # Guidance for Claude Code users
├── ROADMAP.md                        # Project phases and task tracking
│
├── skills/                           # How AI should reason in each legal domain
│   ├── contract-review.md            # Contract analysis under Saudi law
│   ├── labor-law-analysis.md         # Saudi Labor Law (Royal Decree M/51)
│   ├── commercial-dispute.md         # Commercial court procedures and strategy
│   ├── compliance-check.md           # Regulatory compliance assessment
│   └── legal-drafting.md             # Saudi legal drafting standards
│
├── sources/                          # Reference summaries of key Saudi regulations
│   ├── saudi-laws.md                 # Legislative system overview
│   ├── labor-law.md                  # Labor Law provisions
│   ├── companies-law.md              # Companies Law (Royal Decree M/132, 1443H)
│   ├── commercial-courts.md          # Commercial Courts Law (Royal Decree M/93)
│   └── pdpl.md                       # Personal Data Protection Law
│
├── prompts/                          # Ready-to-use prompt templates
│   ├── review-contract.md            # Contract review prompts
│   ├── draft-notice.md               # Legal notice drafting prompts
│   └── risk-analysis.md              # Legal risk analysis prompts
│
└── examples/                         # Annotated worked examples
    ├── employment-contract-review.md  # Employment contract analysis walkthrough
    └── nda-review.md                  # NDA review walkthrough
```

**Design principle:** Each layer is independent. Use a single prompt template without reading the skills files, or combine all layers for a richer context.

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

### Before you contribute
- Read [CLAUDE.md](CLAUDE.md) for content standards and legal accuracy requirements
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

---

## Project Documentation / وثائق المشروع

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview — start here |
| [ROADMAP.md](ROADMAP.md) | Phase plan, task tracking, versioning |
| [CLAUDE.md](CLAUDE.md) | Standards and guidance for Claude Code users |

---

## License / الترخيص

MIT License — free to use, modify, and distribute with attribution and retention of the legal disclaimer.

This license does not grant any right to represent AI outputs produced using this framework as legal advice.
