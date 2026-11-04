# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Saudi Legal AI Framework** is an open-source documentation framework for adapting AI assistants to the Saudi Arabian legal environment. Most of the repository is Markdown (skills, sources, prompts, examples, datasets). It also contains Python validators in `scripts/`, a test suite in `tests/` (run `python3 -m pytest -q`), an eval harness in `evals/`, and a FastMCP server in `mcp-server/`. Run the validators and tests before opening a PR.

## Repository Structure

```
skills/      → Guidance on how AI should approach specific legal domains under Saudi law
sources/     → Reference summaries of key Saudi regulations (not legal text substitutes)
prompts/     → Ready-to-use prompt templates for Claude, ChatGPT, and Gemini
examples/    → Worked analysis examples demonstrating the framework in practice
datasets/    → Structured risk data and judicial reasoning extractions
scripts/     → Dataset builders and cross-reference validators
tests/       → pytest suite for scripts and MCP tools
evals/       → Eval harness (cases, schema, source registry)
mcp-server/  → FastMCP server exposing 3 legal tools
```

Judicial decision PDFs are not stored in git. Run `scripts/fetch_judicial_pdfs.sh` to download them from the `judicial-decisions-1435` release into `sources/judicial-decisions/1435/`.

## Core Principles (must be followed in all interactions)

1. **No legal advice** — All AI output is preliminary analysis only. Always include the disclaimer that a licensed Saudi attorney must review any conclusions.
2. **No Western law defaults** — Do not apply U.S., EU, or common-law assumptions. The Saudi legal system is grounded in Islamic Sharia combined with Royal Decrees and ministerial regulations.
3. **Cite Saudi sources** — Reference specific Saudi regulations by their official Arabic names and decree numbers when available.
4. **Bilingual output** — Legal analysis and documentation in this project should be written in both Arabic and English.
5. **Jurisdiction awareness** — Saudi Arabia has specialized courts (Labor Courts, Commercial Courts, Administrative Courts). Always identify the competent court or authority.

## Working With This Framework

- When editing a `skills/` file: describe *how* an AI should reason, not *what the law says*. Point to `sources/` for legal specifics.
- When editing a `sources/` file: summarize the regulation's scope, key provisions, and official reference. Do not reproduce full legal text.
- When editing a `prompts/` file: write prompts that work across Claude, ChatGPT, and Gemini. Use clear variable placeholders like `[CONTRACT_TEXT]`.
- When editing an `examples/` file: show realistic scenarios with annotated reasoning — not definitive legal rulings.

## Key Saudi Legal Context

- The primary legislative instrument is the **Royal Decree (مرسوم ملكي)**
- Regulations are published officially via **هيئة الخبراء بمجلس الوزراء** (boe.gov.sa) and the **Official Gazette / الجريدة الرسمية (أم القرى)** (uqn.gov.sa)
- Saudi labor law has specific mandatory provisions: Saudization (نطاقات/Nitaqat), end-of-service benefits (مكافأة نهاية الخدمة), and mandatory written contracts
- The **PDPL (نظام حماية البيانات الشخصية)** became effective September 2023
- Commercial disputes are handled by **Commercial Courts (المحاكم التجارية)** established under Royal Decree M/93 (2020)

## Disclaimer Enforcement

Every file in `prompts/` and `examples/` must include the following warning in both languages:

> **تحذير:** هذا تحليل أولي بمساعدة الذكاء الاصطناعي ولا يُعدّ استشارة قانونية. يجب مراجعة مختص قانوني مرخّص في المملكة العربية السعودية قبل اتخاذ أي إجراء.
>
> **Warning:** This is a preliminary AI-assisted analysis and does not constitute legal advice. A licensed legal professional in the Kingdom of Saudi Arabia must be consulted before taking any action.
