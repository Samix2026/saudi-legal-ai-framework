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
[![Arabic Support](https://img.shields.io/badge/Language-Arabic%20%7C%20English-orange.svg)]()
[![Open Source](https://img.shields.io/badge/open%20source-yes-green.svg)](LICENSE)
[![AI Compatible](https://img.shields.io/badge/AI-compatible-blueviolet.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

> ⚠️ **تنبيه / Notice:** مخرجات هذا الاطار للبحث الاولي فقط وليست استشارة قانونية. استخدمه دائما تحت اشراف محام مرخص في المملكة العربية السعودية. Outputs are for preliminary research only and do not constitute legal advice. Always use under supervision of a licensed Saudi attorney.

---

## نظرة عامة / Overview

تعاني معظم نماذج الذكاء الاصطناعي الكبرى من قصور واضح في التعامل مع البيئة القانونية السعودية، لانها مدربة في معظمها على مواد قانونية غربية. النتيجة اخطاء متعددة: الاستشهاد بمبادئ غير قابلة للتطبيق، وتجاهل الانظمة المحلية الالزامية، والخلط في صلاحيات المحاكم المتخصصة.

هذا المشروع يعالج تلك الفجوة. انه مجموعة منظمة ومفتوحة المصدر من المهارات وقوالب المطالبات والمصادر التشريعية والامثلة التطبيقية، تمنح مساعدات الذكاء الاصطناعي السياق الضروري للتعامل الصحيح مع القانون السعودي.

Most large AI models are trained predominantly on Western legal material. When applied to the Saudi context, they produce errors: citing inapplicable legal concepts, ignoring mandatory local regulations, and misidentifying competent courts. This project addresses that gap with a structured, open-source collection of skills, prompt templates, legal source references, and worked examples that give AI assistants the context they need to reason correctly about Saudi law.

---

## كيف تستخدم هذا الاطار

1. **اختر المجال القانوني** المناسب وافتح ملف المهارة المقابل في مجلد `skills/`
2. **اضف السياق التشريعي** من مجلد `sources/`، ثم استخدم قالب المطالبة المناسب من `prompts/`
3. **راجع المخرجات** مع محام مرخص في المملكة العربية السعودية قبل اتخاذ اي قرار

---

## 🔍 مثال عملي - قبل وبعد

### بدون هذا الاطار

اسأل اي نموذج ذكاء اصطناعي:

> "ما هي مدة التقادم في دعاوى المطالبة التجارية في السعودية؟"

**الجواب النموذجي:**
> "تتراوح مدة التقادم عادة بين 3 و10 سنوات وفقا للقانون التجاري المعمول به."

❌ المشكلة: الجواب مبني على مبادئ قانون تجاري غربي عام. لا يشير الى نظام المحاكم التجارية السعودية، ولا الى المرسوم الملكي رقم م/93، ولا الى الفروق بين انواع الدعاوى.

---

### مع هذا الاطار

بعد تحميل ملف `skills/commercial-dispute.md` في سياق النموذج، يصبح الجواب:

> "وفقا لنظام المحاكم التجارية السعودية الصادر بالمرسوم الملكي رقم م/93 لعام 1441هـ:
> - الدعاوى التجارية العامة (بما فيها الديون وعقود التوريد): 5 سنوات من تاريخ نشوء الحق (المادة 24)
> - الاوراق التجارية (شيك، كمبيالة): 3 سنوات من تاريخ الاستحقاق (نظام الاوراق التجارية، المادة 84)
> - حقوق التجار عن سلع وخدمات لغير التجار: سنة واحدة (نظام المعاملات المدنية م/191 لعام 1444هـ، المادة 297)
>
> الاختصاص القضائي: المحاكم التجارية المتخصصة، وليس المحاكم العامة."

✅ النتيجة: جواب مبني على النظام السعودي الفعلي، مع مرجع نظامي محدد وتمييز واضح بين انواع الدعاوى.

---

> 💡 هذا الفرق هو سبب وجود هذا المشروع.

---

## لماذا هذا المشروع مهم / Why Saudi Legal AI Matters

البيئة القانونية السعودية تختلف جوهريا عن البيئات التي دربت عليها نماذج الذكاء الاصطناعي الكبرى. المصدر الاساسي للتشريع هو الشريعة الاسلامية، والمرسوم الملكي هو اداة التشريع الرئيسية وليس القانون البرلماني. المحاكم المتخصصة كالعمالية والتجارية والادارية تختص بانواع محددة من النزاعات. واللغة العربية هي اللغة المعتمدة للنصوص الرسمية، والترجمات الانجليزية غير ملزمة. حين يتجاهل نموذج الذكاء الاصطناعي هذه الخصائص، تتحول مخرجاته من مفيدة الى مضللة.

The Saudi legal system has a distinct foundation that most AI models handle poorly: Islamic Sharia is the primary source of law, Royal Decrees are the main legislative instrument, specialized courts (Labor, Commercial, Administrative) have exclusive jurisdiction over distinct dispute types, and Arabic is the authoritative language for all official legal texts. When AI defaults to Western legal reasoning in this context, it can lead professionals to draw wrong conclusions about their rights, obligations, and legal exposure.

---

## المميزات / Features

| المميزة | الوصف بالعربية | Description in English |
|---------|----------------|------------------------|
| **تاسيس سعودي** | المهارات والقوالب مبنية على القانون السعودي، لا مقتبسة من نماذج غربية | Skills and prompts grounded in Saudi law, not adapted from Western templates |
| **ثنائي اللغة** | جميع المحتوى منظم بالعربية والانجليزية | All content structured in Arabic and English |
| **متوافق مع عدة نماذج** | يعمل مع Claude وChatGPT وGemini واي نموذج يتبع التعليمات | Works with Claude, ChatGPT, Gemini, and any instruction-following LLM |
| **هيكل معياري** | استخدم المكونات ذات الصلة بمهمتك فقط | Use only the components relevant to your task |
| **مصادر موثقة** | كل ادعاء قانوني يشير الى مصدر سعودي رسمي | Every legal claim points to an official Saudi source |
| **اخلاء مسؤولية دائم** | كل قالب مخرجات يتضمن نص اخلاء المسؤولية القانوني | Every output template includes mandatory legal disclaimer language |
| **لا يحتاج برمجة** | توثيق خالص، قابل للاستخدام دون اي اعداد تقني | Pure documentation, usable without any technical setup |
| **التحكيم التجاري** | تحليل اتفاقيات التحكيم وإجراءات SCCA ومدد الطعن في الأحكام وفق نظام التحكيم م/34 | Arbitration agreement analysis, SCCA procedures, and award challenge timelines under Saudi law |
| **عقود العقارات والإيجار** | مراجعة عقود الإيجار التجاري والسكني والتحقق من الالتزامات النظامية ومنصة إيجار | Commercial and residential lease review, statutory obligations, and Ejar platform compliance |
| **حماية المبلغين والشهود** | اطار تشريعي متكامل لحماية المبلغين والشهود والخبراء والضحايا وفق نظام م/148 لعام 1445هـ واللائحة التنفيذية 2026م | Comprehensive protection framework for whistleblowers, witnesses, experts and victims under Royal Decree M/148 1445H and 2026 implementing regulations |

---

## حالة المشروع / Project Status

| المرحلة | الحالة | Phase | Status |
|---------|--------|-------|--------|
| المرحلة 1: الاساس | مكتملة — 90% (skills/ 7 ملفات) | Phase 1: Foundation | Complete — 90% (skills/ 7 files) |
| المرحلة 2: قاعدة المعرفة | جارية، متقدمة | Phase 2: Knowledge Base | Advanced, In Progress |
| المرحلة 3: سير عمل الذكاء الاصطناعي | جارية، مرحلة اولية | Phase 3: AI Workflows | Foundation Established |
| المرحلة 4: تكامل MCP | تخطيط مبكر | Phase 4: MCP Integration | Research / Early Planning |
| المرحلة 5: طبقة المنتج | مخطط لها | Phase 5: Product Layer | Planned |

**المرحلة 1 تشمل:** هيكل المستودع، الحوكمة، pipeline التحقق، CI/CD، سير عمل المساهمين، الاختبار الآلي، دورة حياة التحقق، هيكل مجموعات البيانات القابل للتوسع.

**المرحلة 2 تشمل:** سجل الانظمة، مجموعات البيانات، القيم المعيارية، المراجع القانونية، المصادر التشريعية السعودية، الامثلة التطبيقية، المجموعة القضائية، اطار الفهرسة القضائية، اطار استخراج التفكير، دورة حياة التحقق، المصادر المفتوحة البيانات.
**ما تبقى من المرحلة 2:** تغطية اشمل، مراجع موثقة، مجموعات بيانات اكبر.

**المرحلة 3 تشمل:** مهارات قانونية موحدة، صيغ مخرجات موحدة، قوالب سير عمل، هياكل بيانات موجهة للتفكير، وثائق هندسة النظام.
**ما تبقى من المرحلة 3:** التنسيق، التقييمات، سلاسل التفكير، سير عمل الوكلاء.

**المرحلة 4 - التخطيط المبكر يشمل:** استراتيجية OCR، خطوط استيعاب مستقبلية، تكاملات API مستقبلية، هيكل استرجاع مستقبلي.

راجع [ROADMAP.md](ROADMAP.md) للخطة الكاملة وتفاصيل المهام.

---

## هيكل المشروع / Architecture Overview

```
saudi-legal-ai-framework/
│
├── README.md                              # نظرة عامة بالمشروع (هذا الملف)
├── CLAUDE.md                              # توجيهات لمستخدمي Claude Code
├── ROADMAP.md                             # مراحل المشروع وتتبع المهام
├── CONTRIBUTING.md                        # دليل المساهمة
├── CODE_OF_CONDUCT.md                     # معايير السلوك المجتمعي
├── SECURITY.md                            # الابلاغ عن مشكلات امنية
├── requirements-dev.txt                   # متطلبات بيئة التطوير
│
├── skills/                                # كيف يستدل الذكاء الاصطناعي في كل مجال قانوني
│   ├── contract-review.md
│   ├── labor-law-analysis.md
│   ├── commercial-dispute.md
│   ├── compliance-check.md
│   └── legal-drafting.md
│
├── sources/                               # ملخصات مرجعية للانظمة السعودية الرئيسية (8 ملفات)
│   ├── regulation-index.md                # سجل الاستشهادات المعتمد لجميع الانظمة
│   ├── saudi-laws.md
│   ├── labor-law.md
│   ├── companies-law.md
│   ├── civil-transactions-law.md
│   ├── commercial-courts.md
│   ├── pdpl.md
│   ├── e-commerce-law.md
│   ├── whistleblower-protection.md        # م/148 1445هـ — نظام حماية المبلغين والشهود والخبراء والضحايا
│   ├── open-data-judicial-sources.md      # بيانات مفتوحة سعودية، احصاءات تكميلية فقط
│   ├── fiqh-judicial-references/          # المراجع الفقهية الكلاسيكية المستشهد بها في الاحكام
│   │   ├── README.md                      # حدود الطبقة وقواعد الاضافة
│   │   ├── citation-index.md              # الاستشهادات الفقهية مرتبطة بمعرفات الحالات
│   │   └── usage-guidelines.md            # متى وكيف تستخدم، قواعد منع الهلوسة
│   └── judicial-decisions/                # مجلدات PDF الممسوحة لقرارات المحاكم السعودية
│       ├── README.md
│       └── 1435/                          # السنة الهجرية، 14 مجلد PDF
│
├── datasets/                              # مجموعات البيانات القانونية المنظمة
│   ├── README.md
│   ├── saudi-contract-risk-dataset.csv    # مجموعة البيانات الرئيسية
│   ├── schema.md                          # تعريف المخطط، 16 عمودا
│   ├── risk-taxonomy.md
│   ├── severity-standards.md
│   ├── enums/                             # قواميس المصطلحات المضبوطة
│   ├── examples/                          # ملفات CSV تطبيقية حسب القطاع
│   ├── contributions/                     # منطقة تجميع مساهمات المساهمين
│   ├── build/                             # مخرجات مدمجة يولدها CI
│   ├── judicial-reasoning/                # استخراج منظم من قرارات المحاكم
│   │   ├── schema.md                      # مخطط استخراج 19 حقلا
│   │   ├── example-extraction.md
│   │   ├── extraction-guidelines.md
│   │   └── cases/                         # الاستخراجات المكتملة (5 حالات، 1435ه)
│   │       ├── README.md
│   │       ├── JD-1435-001.md
│   │       ├── JD-1435-002.md
│   │       ├── JD-1435-003.md
│   │       ├── JD-1435-004.md
│   │       └── JD-1435-005.md
│   └── judicial-index/                    # فهرس اقسام PDF قبل الاستخراج
│       ├── README.md
│       ├── schema.md
│       └── judicial-corpus-index.csv
│
├── prompts/                               # قوالب مطالبات جاهزة للاستخدام
│   ├── review-contract.md
│   ├── draft-notice.md
│   └── risk-analysis.md
│
├── examples/                              # امثلة تطبيقية مشروحة
│   ├── employment-contract-review.md
│   ├── nda-review.md
│   └── saudi-contract-review-demo.md
│
├── docs/                                  # وثائق الهندسة والحوكمة والتخطيط
│   ├── system-architecture.md             # خريطة طبقات النظام الكاملة ودورة حياة البيانات
│   ├── cross-reference-map.md             # خريطة تبعية الملفات، ما تحدّثه عند تغيير شيء
│   ├── legal-verification-lifecycle.md    # حالات التحقق وقواعد الانتقال
│   ├── official-api-sources.md            # واجهات برمجية حكومية سعودية، هندسة مستقبلية
│   ├── ocr-strategy.md                    # استراتيجية OCR لملفات PDF القضائية الممسوحة
│   ├── architecture-audit-v1.md
│   └── mcp-integration-notes.md
│
├── scripts/                               # التحقق وأتمتة البناء
│   ├── validate_dataset.py
│   ├── build_dataset.py
│   └── ocr_pdf_pages.py                   # سكريبت OCR القابل للتكرار لملفات PDF القضائية
│
├── tests/                                 # اختبارات وحدة التحقق والبناء
│   ├── test_validate_dataset.py
│   └── test_build_dataset.py
│
├── experiments/                           # تجارب OCR واعمال استخراج استكشافية
│   ├── ocr-production-test/               # مخرجات OCR على مستوى الصفحة
│   └── ocr-benchmark/                     # نتائج المقارنة بين ادوات OCR
│
└── .github/                               # قوالب المشكلات وسير عمل CI
    ├── ISSUE_TEMPLATE/                    # 3 قوالب: خطا قانوني، تحديث محتوى، مثال جديد
    ├── pull_request_template.md
    └── workflows/                         # validate-datasets.yml · label-check.yml
```

### تدفق المعمارية / Architectural Flow

```
القوانين الرسمية والمراسيم الملكية     sources/*.md · sources/regulation-index.md
        │
        ▼
قرارات قضائية (PDFs ممسوحة)           sources/judicial-decisions/1435/
        │
        ▼
استشهادات فقهية داخل الاحكام          sources/fiqh-judicial-references/citation-index.md
        │  (cited by judges, supplementary, not legislative)
        ▼
استخراج OCR والفهرسة                  scripts/ocr_pdf_pages.py
        │                              datasets/judicial-index/
        ▼
استخراج التفكير القضائي               datasets/judicial-reasoning/cases/
        │
        ▼
دورة حياة التحقق                      draft → community-reviewed → verified
        │                              docs/legal-verification-lifecycle.md
        ▼
مجموعات البيانات المنظمة              datasets/saudi-contract-risk-dataset.csv
        │
        ▼
المهارات وسير عمل الذكاء الاصطناعي    skills/ · prompts/ · examples/
```

**Design principle:** Each layer is independent. Use a single prompt template without reading the skills files, or combine all layers for a richer context.

For a complete description of each layer, the data lifecycle, and the planned future architecture, see [docs/system-architecture.md](docs/system-architecture.md).

---

## طبقات المعمارية الحالية / Current Architecture Layers

| Layer | Directory | Status | Description |
|-------|-----------|--------|-------------|
| **Legislative Sources** | `sources/` | Active | Reference summaries of Saudi regulations with official citations |
| **Judicial Corpus** | `sources/judicial-decisions/` | Active, Indexing | Scanned PDF volumes of Saudi court decisions (14 files, 1435H) |
| **Corpus Index** | `datasets/judicial-index/` | Active, In Progress | Section-level map of PDF volumes before extraction |
| **Judicial Extraction** | `datasets/judicial-reasoning/` | Active: 5 cases extracted | Structured 19-field extraction schema, 5 cases from 1435H decisions |
| **Fiqh Reference Layer** | `sources/fiqh-judicial-references/` | Active | Classical fiqh works cited in judicial rulings, supplementary, not legislative |
| **Contract Datasets** | `datasets/` | Active | 16-column CSV schema with verification lifecycle |
| **AI Skills** | `skills/` | Active | Domain-specific reasoning guides for AI assistants |
| **Prompt Templates** | `prompts/` | Active | Self-contained, model-neutral prompt templates |
| **Worked Examples** | `examples/` | Active | Annotated walkthroughs for reference |
| **Future: OCR Layer** | — | Planned | Text extraction from scanned judicial PDFs |
| **Future: RAG Layer** | — | Planned | Retrieval-augmented generation over verified content |
| **Future: Agent Layer** | — | Planned | Orchestrated multi-step legal analysis workflows |

See [docs/system-architecture.md](docs/system-architecture.md) for the full layer map, [datasets/judicial-index/](datasets/judicial-index/) for corpus indexing progress, and [datasets/judicial-reasoning/](datasets/judicial-reasoning/) for the extraction framework.

---

## نماذج الذكاء الاصطناعي المدعومة / Supported AI Assistants

This framework is model-agnostic. It has been designed to work with:

| Model | How to Use |
|-------|------------|
| **Claude** (Anthropic) | Open project in Claude Code, or paste skill file content at the start of a conversation |
| **ChatGPT** (OpenAI) | Paste skill file as a System Prompt or at the top of the conversation |
| **Gemini** (Google) | Include skill file content in the initial context window |
| **Any instruction-following LLM** | Same approach: paste the relevant skill and prompt template |

The prompts in `prompts/` are written to be self-contained and model-neutral.

---

## البدء السريع / Quick Start

**No installation required.** This is a documentation framework.

### الخيار 1: قالب مطالبة واحد / Option 1: Single Prompt Template
1. Open any file in `prompts/`
2. Copy the template that matches your task
3. Paste it into your AI assistant of choice
4. Replace the placeholder variables (e.g. `[CONTRACT_TEXT]`)

### الخيار 2: السياق الكامل (موصى به للمهام المعقدة) / Option 2: Full Context
1. Open the relevant `skills/` file and paste its content as system context
2. Add the relevant `sources/` file for deeper regulatory grounding
3. Use the matching `prompts/` template as your user message
4. Review any AI output with a licensed Saudi legal professional

### الخيار 3: مستخدمو Claude Code / Option 3: Claude Code Users
```bash
git clone https://github.com/Samix2026/saudi-legal-ai-framework.git
cd saudi-legal-ai-framework
# Open in Claude Code — CLAUDE.md loads automatically as project context
```

---

## أمثلة على سير العمل / Example Workflows

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

## المبادئ التوجيهية / Guiding Principles

| Principle | What it means in practice |
|-----------|--------------------------|
| **Saudi law first** | Islamic Sharia + Royal Decrees are the baseline: never Western civil law defaults |
| **No false confidence** | AI output uses hedged language ("may be", "could raise"): never categorical legal rulings |
| **Human oversight required** | Every output template mandates review by a licensed Saudi attorney |
| **Source transparency** | Legal claims reference specific regulations by decree number and article |
| **Arabic is authoritative** | Where Arabic and English conflict in any document, Arabic governs |
| **Jurisdiction awareness** | Competent court or authority is always identified (Labor, Commercial, Administrative) |

---

## الرؤية المستقبلية / Future Vision

هذا المشروع يتطور عبر مراحل نحو اداة فعلية يعتمد عليها المختصون القانونيون في المملكة للبحث الاولي والتحليل.

**المرحلة القريبة (v0.2 - v1.0):**
استكمال قاعدة المعرفة للمجالات التشريعية الخمسة الرئيسية، واضافة امثلة تطبيقية في قطاعات جديدة (العقار، التقنية، الرعاية الصحية)، ومراجعة المحتوى من قبل محامين سعوديين مرخصين.

**المرحلة المتوسطة (v2.0):**
تكاملات MCP تربط مساعدات الذكاء الاصطناعي مباشرة بالمصادر القانونية السعودية الرسمية، لاسترجاع النص التشريعي الحالي والاشارة الى التعديلات الاخيرة وتاسيس التحليل على محتوى موثق ومحدث.

**المرحلة البعيدة (v3.0):**
واجهة ويب تتيح للمختصين القانونيين والمنظمات رفع وثائقهم وتشغيل تحليلات منظمة وانتاج تقارير مراجعة منسقة دون الحاجة الى خلفية تقنية.

لن يسعى المشروع في اي مرحلة الى تقديم مشورة قانونية آلية. الهدف تسريع البحث القانوني الاولي وتحسين دقته، لا استبدال الحكم القانوني البشري.

Near-term (v0.2 to v1.0): completing the knowledge base for the five major regulatory areas, adding worked examples across more sectors (real estate, technology, healthcare), and having content reviewed by licensed Saudi legal professionals.

Medium-term (v2.0): MCP server integrations connecting AI assistants directly to official Saudi legal sources, retrieving current regulatory text, flagging recent amendments, and grounding analysis in verified content.

Long-term (v3.0): a web interface for legal professionals and organizations to upload documents, run structured analyses, and generate formatted review reports without technical knowledge.

---

## دليل المساهمة / Contribution Guide

نرحب بمساهمات المختصين القانونيين والباحثين والمطورين على حد سواء. كل مساهمة، كبيرة كانت ام صغيرة، تضيف قيمة حقيقية للمشروع.

راجع [CONTRIBUTING.md](CONTRIBUTING.md) للدليل الكامل بما يشمل معايير مجموعات البيانات وصيغ الاستشهاد ومتطلبات اخفاء الهوية وقائمة التحقق قبل التقديم.

اقرأ [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) قبل المساهمة. للابلاغ عن مشكلة امنية (مثل بيانات غير معماة)، راجع [SECURITY.md](SECURITY.md).

### مسارات المساهمة

⚖️ **مختص قانوني:** مراجعة محتوى `sources/` و`skills/` للدقة القانونية هي اعلى قيمة يمكن تقديمها. تصحيح خطأ واحد يستحق عشر اضافات. الانظمة السعودية تتغير باستمرار، وتحديث ملف قديم في `sources/` مع المرجع الرسمي مساهمة لا تقدر بثمن.

📋 **باحث او محلل:** اذا لاحظت نظاما تم تعديله وملف في `sources/` غير محدث، افتح مشكلة او قدم تصحيحا مع رقم المرسوم والمصدر الرسمي. ايضا: فهرسة الاحكام القضائية واستخراجها في `datasets/judicial-reasoning/` مجال خصب للمساهمة.

📝 **مطور او كاتب:** امثلة عملية في `examples/` لقطاعات متعددة (العقار، التقنية، الانشاءات)، وقوالب مطالبات جديدة في `prompts/`، وتحسين جودة الترجمة في اي ملف.

### من اين تبدا؟

1. اقرأ [CONTRIBUTING.md](CONTRIBUTING.md) لتعرف معايير المحتوى ومتطلبات الاستشهاد.
2. راجع [ROADMAP.md](ROADMAP.md) لتعرف ما هو مخطط وما هو جار.
3. افتح مشكلة (Issue) لمناقشة اي اضافة جوهرية قبل تقديم Pull Request.
4. ابدأ بمهمة من قائمة "Good First Issues" اذا كنت جديدا على المشروع.

### كيفية تقديم Pull Request

1. انشئ fork للمستودع وتفرع منه لعملك.
2. قدم تغيير واحد او موضوع واحد في كل Pull Request.
3. اذكر في وصف الـ PR ما الذي تغير ولماذا، مع الاشارة الى المصادر الرسمية عند الاقتضاء.
4. انتظر المراجعة. ردود الفعل البناءة جزء من العملية.

### نقطة البداية للمساهمين الجدد / Good First Issues

اذا كنت جديدا على المشروع، هذه افضل نقاط للبداية:

| المهمة | الملف | الجهد |
|--------|-------|-------|
| اضافة مثال تطبيقي لعقد ايجار تجاري | `examples/` | منخفض |
| مراجعة labor-law.md والاشارة الى اي احكام قديمة | `sources/labor-law.md` | منخفض |
| اضافة روابط المصادر الرسمية الناقصة | `sources/` | منخفض |
| تحسين جودة الترجمة الانجليزية في اي ملف مهارة | `skills/` | منخفض |
| اقتراح قالب مطالبة جديد لقطاع غير مغطى | `prompts/` | متوسط |

جميع هذه المهام موسومة `good first issue` في تبويب المشكلات.

### معايير المساهمة / Contribution Standards

- Every legal claim must cite an official Saudi source (decree number, article, issuing authority)
- New content must include the bilingual legal disclaimer in both Arabic and English
- Do not introduce Western legal assumptions: if uncertain, note the uncertainty explicitly
- Pull Request descriptions must explain what changed and why, with source references

### ما لا نبحث عنه

- نص قانوني مُولَّد بالذكاء الاصطناعي يُقدَّم على انه موثوق
- محتوى مقتبس من قوالب قانونية غربية دون تاسيس سعودي
- تفسيرات تخمينية غير مستندة الى مصادر رسمية

---

## المصادر الرسمية / Official Sources

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
| البوابة القانونية — وزارة العدل | [laws.moj.gov.sa](https://laws.moj.gov.sa) | أنظمة تشريعية + أحكام المحاكم + سوابق قضائية — Ministry of Justice legal portal — legislation and judicial decisions |

---

## وثائق المشروع / Project Documentation

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
| [docs/ocr-strategy.md](docs/ocr-strategy.md) | OCR strategy for scanned judicial PDFs — tool comparison, risks, test plan |
| [datasets/judicial-reasoning/schema.md](datasets/judicial-reasoning/schema.md) | Judicial reasoning extraction schema — 19-field structured format |
| [datasets/judicial-reasoning/extraction-guidelines.md](datasets/judicial-reasoning/extraction-guidelines.md) | Extraction and redaction guidelines for judicial decisions |
| [datasets/judicial-index/judicial-corpus-index.csv](datasets/judicial-index/judicial-corpus-index.csv) | Judicial corpus index — section-level map of PDF volumes before extraction |
| [sources/fiqh-judicial-references/citation-index.md](sources/fiqh-judicial-references/citation-index.md) | Fiqh citation index — classical works cited in judicial rulings, linked to case IDs |
| [sources/fiqh-judicial-references/usage-guidelines.md](sources/fiqh-judicial-references/usage-guidelines.md) | When and how to use fiqh references — hallucination prevention rules |

---

## المساهمون / Contributors

هذا المشروع في بداياته. نرحب بك ان تكون من اوائل المساهمين.

This project is in its early stages. We welcome you to be among its first contributors.

<!-- All contributors will be listed here. To add yourself, open a Pull Request adding your name or GitHub handle. -->

---

## الترخيص / License

MIT License — free to use, modify, and distribute with attribution and retention of the legal disclaimer.

This license does not grant any right to represent AI outputs produced using this framework as legal advice.
