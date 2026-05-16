# معمارية النظام
# System Architecture

**Saudi Legal AI Framework** — التوثيق المعماري الكامل

**الإصدار / Version:** 2.1
**يعكس / Reflects:** v0.3 قيد العمل — Phase 2 متقدمة · Phase 3 أساس مُنشأ · Phase 4 بحث وتخطيط مبكر

---

## 1. نظرة عامة على المعمارية / Architecture Overview

هذا المشروع **إطار توثيقي** — لا تطبيق قابل للتشغيل. الهدف هو بناء طبقات معرفية متراكبة تُعلّم مساعدات الذكاء الاصطناعي كيف تُفكّر في السياق القانوني السعودي.

This project is a **documentation framework** — not a runnable application. The goal is to build layered knowledge strata that teach AI assistants how to reason within the Saudi legal context.

### مبدأ التصميم الجوهري / Core Design Principle

```
كل طبقة مستقلة — تستفيد من الطبقة التي تسبقها ولا تستبدلها.
Each layer is independent — it draws from the layer below without replacing it.
```

---

## 2. مستوى نضج المشروع الحالي / Current Project Maturity

هذا المشروع انتقل من مستودع منظَّم إلى بنية تحتية معرفية قانونية مُصانة.

This project has evolved from a structured repository into a maintained legal knowledge infrastructure.

### من / From → إلى / To

```
مستودع منظَّم (Structured Repository)       بنية تحتية معرفية (Knowledge Infrastructure)
──────────────────────────────────────  →   ──────────────────────────────────────────────
· هيكل ملفات + governance                   · 8 طبقات معمارية متكاملة
· 5 مهارات · 5 مصادر · 3 قوالب              · مجموعة أحكام قضائية (14 PDF مُحوَّل ضوئياً)
· dataset أساسي                             · إطار فهرسة + إطار استخراج (13 + 19 حقلًا)
                                            · دورة حياة تحقق كاملة (6 حالات)
                                            · CI/CD + 43 اختباراً آلياً
                                            · توثيق معماري + خرائط مرجعية
                                            · خطة تكامل MCP/RAG موثَّقة
```

### مؤشرات النضج / Maturity Indicators

| المؤشر | الوضع |
|--------|-------|
| هيكل المشروع وحوكمته | ✅ مكتمل — Phase 1 |
| المصادر التشريعية (sources/) | ✅ 5 أنظمة موثَّقة بمراجع رسمية |
| المجموعة القضائية | ✅ 14 PDF مُحوَّل ضوئياً، فهرسة جزئية |
| إطار الاستخراج القضائي | ✅ جاهز — 19 حقلًا + دليل + مثال |
| مجموعات البيانات | ✅ 16 عموداً · تحقق آلي · بناء آلي |
| دورة حياة التحقق | ✅ 6 حالات · انتقالات موثَّقة |
| مهارات الذكاء الاصطناعي | ✅ 5 مهارات · هيكل 11 قسماً موحَّداً |
| تكاملات MCP/RAG المستقبلية | 🔍 خطة موثَّقة — لا تطبيق بعد |
| واجهة المستخدم (Product) | ⬜ مخطَّط — Phase 5 |

### ما لم يتغيَّر / What Has Not Changed

المشروع لا يزال:
- **إطارًا توثيقيًا** — لا تطبيقًا قابلًا للتشغيل
- **مساعدًا** — لا بديلًا عن المختص القانوني
- **في التطوير المستمر** — المحتوى يحتاج مراجعة قانونية متخصصة قبل الاعتماد عليه

---

## 3. خريطة طبقات النظام الكاملة / Full System Layer Map

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   LAYER 8 — Future Agents          [مخطَّط / Planned]           │
│   Multi-step legal reasoning · orchestrated workflows           │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 7 — Future RAG             [مخطَّط / Planned]           │
│   Retrieval-Augmented Generation from verified sources          │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 6 — Future MCP / Retrieval [بحث مبكر / Early Research] │
│   MCP servers · official source APIs · semantic search          │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 5 — AI Workflows           [أساس مُنشأ / Found. Est.]  │
│   skills/ · prompts/ · examples/                                │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 4 — Structured Datasets    [متقدم / Advanced]          │
│   datasets/saudi-contract-risk-dataset.csv                      │
│   datasets/examples/ · datasets/contributions/                  │
│   datasets/judicial-reasoning/                                  │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 3 — Indexing & Extraction  [قيد العمل / In Progress]   │
│   datasets/judicial-index/ · datasets/judicial-reasoning/       │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 2 — Judicial Corpus        [مكتملة / Complete]         │
│   sources/judicial-decisions/1435/ (14 PDF)                     │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   LAYER 1 — Official Sources       [مكتملة / Complete]         │
│   sources/ · sources/regulation-index.md                        │
│   boe.gov.sa · uqn.gov.sa (external)                           │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 4. دورة حياة البيانات الكاملة / Full Data Lifecycle

```
┌─────────────────────┐
│   Raw PDFs          │  ← sources/judicial-decisions/1435/*.pdf
│   (Scanned, 14 vol) │     12MB average, image-based, not text-extractable
└────────┬────────────┘
         │
         ▼ [Future: OCR Layer]
┌─────────────────────┐
│   OCR               │  ← مخطَّط — Phase 4 / Planned — Phase 4
│   Text extraction   │     Arabic OCR · layout analysis · page detection
└────────┬────────────┘
         │ (حالياً: يدوي / Currently: manual)
         ▼
┌─────────────────────┐
│   Indexing          │  ← datasets/judicial-index/judicial-corpus-index.csv
│   Section mapping   │     13 حقلاً · العنوان + نطاق الصفحات + الأولوية
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Extraction        │  ← datasets/judicial-reasoning/
│   Reasoning capture │     19 حقلاً · judicial_reasoning + legal_principle
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Verification      │  ← verification_status: draft → reviewed → verified
│   Human review      │     docs/legal-verification-lifecycle.md
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Structured        │  ← datasets/saudi-contract-risk-dataset.csv
│   Datasets          │     16 عموداً · validate_dataset.py · build_dataset.py
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Skills            │  ← skills/*.md (5 ملفات · هيكل 11 قسماً)
│   Reasoning guides  │     contract-review · labor · commercial · compliance · drafting
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   AI Workflows      │  ← prompts/*.md · examples/*.md
│   Ready-to-use      │     3 قوالب مطالبات · أمثلة تطبيقية
└────────┬────────────┘
         │
         ▼ [Future: MCP / Retrieval Layer — Phase 4]
┌─────────────────────┐
│   MCP / Retrieval   │  ← Phase 4
│   Live data access  │     MCP servers · official APIs · semantic search
└────────┬────────────┘
         │
         ▼ [Future: RAG Layer — Phase 4]
┌─────────────────────┐
│   Future RAG        │  ← Phase 4
│   Grounded answers  │     vector search · verified sources · citations
└────────┬────────────┘
         │
         ▼ [Future: Agent Layer — Phase 5]
┌─────────────────────┐
│   Future Agents     │  ← Phase 5
│   Orchestrated LLM  │     multi-step reasoning · document workflows
└─────────────────────┘
```

---

## 5. الفرق بين الطبقات / Layer Distinctions

### Sources — المصادر التشريعية
**ما هي:** ملخصات مرجعية للأنظمة السعودية الرسمية.
**What:** Reference summaries of official Saudi regulations.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `sources/*.md` |
| المحتوى | ملخصات الأنظمة + الاستشهادات الرسمية |
| المصدر الأصلي | boe.gov.sa · uqn.gov.sa |
| الاستخدام | مرجع للـ skills والـ datasets |
| يُعوَّض بـ | لا — هذه الطبقة الأساسية دائماً |

---

### Judicial Corpus — المجموعة القضائية
**ما هي:** ملفات PDF للأحكام القضائية السعودية الصادرة عن المحاكم.
**What:** PDF files of Saudi judicial rulings issued by courts.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `sources/judicial-decisions/{سنة هجرية}/` |
| المحتوى | ملفات PDF — مُحوَّلة بالمسح الضوئي |
| الاستخدام | المادة الخام للفهرسة والاستخراج |
| القيد | لا يمكن استخراج النص آلياً — يحتاج OCR |

---

### Indexing — الفهرسة
**ما هي:** فهرس محتوى الـ PDFs — ماذا يوجد في كل ملف.
**What:** Content index of the PDFs — what exists in each file.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `datasets/judicial-index/` |
| المحتوى | 13 حقلاً: section · pages · domain · priority |
| الغرض | تحديد ما يُستخرَج قبل البدء بالاستخراج |
| يحتوي reasoning? | لا — فهرسة فقط |

---

### Extraction — الاستخراج
**ما هي:** استخلاص منظَّم للاستدلال القضائي من الأحكام.
**What:** Structured extraction of judicial reasoning from rulings.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `datasets/judicial-reasoning/` |
| المحتوى | 19 حقلاً: facts · reasoning · principle · outcome |
| الغرض | بناء قاعدة أنماط الاستدلال القضائي |
| شرط أساسي | يجب أن يسبقه indexing للقسم المُستخرَج |

---

### Datasets — مجموعات البيانات
**ما هي:** بيانات منظَّمة حول بنود العقود وأنماط مخاطرها.
**What:** Structured data about contract clauses and their risk patterns.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `datasets/*.csv` · `datasets/examples/` · `datasets/contributions/` |
| المحتوى | 16 عموداً: clause · risk · regulation · verification_status |
| التحقق | `scripts/validate_dataset.py` (43 اختباراً) |
| البناء | `scripts/build_dataset.py` |

---

### Skills — المهارات
**ما هي:** توجيهات لكيفية تفكير الذكاء الاصطناعي في مجال قانوني.
**What:** Guidance on how AI should reason in a legal domain.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `skills/*.md` (5 ملفات) |
| الهيكل | 11 قسماً موحَّداً لكل ملف |
| يستند إلى | `sources/` للمراجع التشريعية |
| يُطبَّق عبر | `prompts/` و`examples/` |

---

### AI Workflows — سير عمل الذكاء الاصطناعي
**ما هي:** قوالب جاهزة للاستخدام المباشر مع أي نموذج لغوي.
**What:** Ready-to-use templates for direct use with any language model.

| الخاصية | القيمة |
|---------|--------|
| الموقع | `prompts/*.md` · `examples/*.md` |
| النماذج المدعومة | Claude · ChatGPT · Gemini · أي LLM |
| يستند إلى | `skills/` للسياق القانوني |

---

## 6. تدفق التحقق / Verification Flow

```
مساهم يُضيف محتوى
        │
        ▼
verification_status = draft  (الافتراضي دائماً)
        │
        ▼
مراجعة بشرية من مختص (باحث / أكاديمي)
        │
        ├─ يجتاز ──► verification_status = reviewed
        │                     │
        │                     ▼
        │            مراجعة من محامٍ مرخَّص سعودي
        │                     │
        │                     ├─ يجتاز ──► verification_status = verified
        │                     │                  (reviewed_by_lawyer = yes)
        │                     └─ تغيير تشريعي ──► deprecated / superseded
        │
        └─ تغيير تشريعي لاحق ──► deprecated / superseded
```

**المرجع الكامل:** [`docs/legal-verification-lifecycle.md`](legal-verification-lifecycle.md)

---

## 7. تدفق المساهمة / Contribution Flow

```
مساهم يفتح Issue لمناقشة الإضافة
        │
        ▼
موافقة المشرف
        │
        ├─ إضافة تشريعية ──► sources/ + regulation-index.md
        │
        ├─ إضافة dataset ──► datasets/contributions/{domain}/
        │                          │
        │                          ▼
        │                    validate_dataset.py
        │                          │
        │                          ▼
        │                    build_dataset.py
        │                          │
        │                          ▼
        │                    GitHub Actions CI
        │
        ├─ إضافة استخراج ──► datasets/judicial-index/ (أولاً)
        │                          │
        │                          ▼
        │                    datasets/judicial-reasoning/
        │                          │
        │                          ▼
        │                    verification_status = draft
        │
        └─ إضافة skill ──► skills/{domain}.md
                                 │
                                 ▼
                           prompts/ + examples/ (تُحدَّث لاحقاً)
```

---

## 8. الطبقات المستقبلية / Future Layers

### Future OCR Layer — طبقة التعرف الضوئي على النص

**الهدف:** استخراج النص العربي تلقائياً من الـ PDFs المُحوَّلة بالمسح الضوئي.

**التحدي:** الـ PDFs الحالية مُحوَّلة بالمسح الضوئي (image-based) — يحتاج OCR متخصص باللغة العربية وتنسيق المستندات القضائية.

**المكونات المقترحة:**
```
PDF المسح الضوئي
        │
        ▼
Arabic OCR Engine (مثل Tesseract + Arabic model)
        │
        ▼
Layout Analysis (تمييز رأس الصفحة · المتن · التذييل)
        │
        ▼
Page Segmentation (تحديد حدود كل حكم)
        │
        ▼
نص عربي منظَّم → مدخل لـ Indexing Layer
```

**المرحلة:** Phase 4 — لا تطبيق حالياً.

---

### Future RAG Layer — طبقة الاسترجاع المعزَّز

**الهدف:** ربط نماذج اللغة مباشرةً بالمصادر الموثَّقة في المشروع عبر الاسترجاع الدلالي.

**المكونات المقترحة:**
```
استعلام المستخدم
        │
        ▼
Embedding Model (تحويل الاستعلام لمتجه دلالي)
        │
        ▼
Vector Search على:
  · sources/*.md (الأنظمة)
  · datasets/*.csv (البنود)
  · datasets/judicial-reasoning/ (الأحكام)
        │
        ▼
Top-K Results → سياق للـ LLM
        │
        ▼
LLM + Context → إجابة مستندة ومُستشهَد بها
```

**المرحلة:** Phase 4 — لا تطبيق حالياً.

---

### Future Agent Layer — طبقة العوامل

**الهدف:** سير عمل متعددة الخطوات تُنجَز آلياً بتوجيه بشري.

**المكونات المقترحة:**
```
طلب مراجعة عقد
        │
        ▼
Agent: Document Parser (استخراج البنود)
        │
        ▼
Agent: Risk Classifier (تصنيف المخاطر)
        │
        ▼
Agent: Regulation Matcher (ربط بالأنظمة)
        │
        ▼
Agent: Report Generator (توليد التقرير)
        │
        ▼
Human Review Gate (مراجعة بشرية إلزامية)
        │
        ▼
تقرير نهائي مع إخلاء مسؤولية
```

**المرحلة:** Phase 5 — لا تطبيق حالياً.

---

## 9. هيكل الملفات الحالي / Current File Structure

```
saudi-legal-ai-framework/
│
├── README.md                              # نقطة البداية
├── CLAUDE.md                             # توجيهات Claude Code
├── ROADMAP.md                            # خارطة الطريق
├── CONTRIBUTING.md                       # دليل المساهمة
├── CODE_OF_CONDUCT.md                    # قواعد السلوك
├── SECURITY.md                           # سياسة الأمان
│
├── skills/                               # LAYER 5 — توجيهات الاستدلال
│   ├── contract-review.md
│   ├── labor-law-analysis.md
│   ├── commercial-dispute.md
│   ├── compliance-check.md
│   └── legal-drafting.md
│
├── sources/                              # LAYER 1 — المصادر التشريعية
│   ├── regulation-index.md              # ← سجل الاستشهادات الرسمي
│   ├── saudi-laws.md
│   ├── labor-law.md
│   ├── companies-law.md
│   ├── commercial-courts.md
│   ├── civil-transactions-law.md
│   ├── pdpl.md
│   ├── open-data-judicial-sources.md    # ← مصدر تكميلي
│   └── judicial-decisions/              # LAYER 2 — المجموعة القضائية
│       ├── README.md
│       └── 1435/                        # ← 14 PDF مُحوَّل بالمسح
│           ├── 1.pdf … 14.pdf
│
├── prompts/                              # LAYER 5 — قوالب المطالبات
│   ├── review-contract.md
│   ├── draft-notice.md
│   └── risk-analysis.md
│
├── examples/                             # LAYER 5 — أمثلة تطبيقية
│   ├── employment-contract-review.md
│   ├── nda-review.md
│   └── saudi-contract-review-demo.md
│
├── datasets/                             # LAYER 4 — مجموعات البيانات
│   ├── saudi-contract-risk-dataset.csv  # ← الملف الرئيسي (3 صفوف)
│   ├── schema.md                        # ← 16 عموداً
│   ├── risk-taxonomy.md
│   ├── severity-standards.md
│   ├── enums/                           # ← 5 ملفات enum
│   ├── examples/                        # ← 3 ملفات CSV تطبيقية
│   ├── contributions/                   # ← مساهمات خارجية
│   ├── judicial-index/                  # LAYER 3 — فهرس الأحكام
│   │   ├── schema.md
│   │   ├── judicial-corpus-index.csv
│   │   └── README.md
│   └── judicial-reasoning/              # LAYER 3 — استخراج الاستدلال
│       ├── schema.md
│       ├── example-extraction.md
│       └── extraction-guidelines.md
│
├── scripts/                              # CI/CD & Validation
│   ├── validate_dataset.py
│   └── build_dataset.py
│
├── tests/                                # 43 اختباراً آلياً
│   ├── test_validate_dataset.py
│   └── test_build_dataset.py
│
├── docs/                                 # التوثيق المعماري
│   ├── system-architecture.md           # ← هذا الملف
│   ├── legal-verification-lifecycle.md
│   ├── cross-reference-map.md
│   └── official-api-sources.md
│
└── .github/                              # CI/CD & Governance
    ├── workflows/
    │   ├── validate-datasets.yml
    │   └── auto-label.yml
    └── labeler.yml
```

---

## 10. الروابط المرجعية / Reference Links

| الملف | الدور المعماري |
|-------|---------------|
| [`docs/legal-verification-lifecycle.md`](legal-verification-lifecycle.md) | تفصيل تدفق التحقق |
| [`docs/cross-reference-map.md`](cross-reference-map.md) | خريطة التبعيات بين الملفات |
| [`docs/official-api-sources.md`](official-api-sources.md) | تصور طبقة API المستقبلية |
| [`sources/regulation-index.md`](../sources/regulation-index.md) | سجل الاستشهادات الرسمي |
| [`datasets/judicial-index/README.md`](../datasets/judicial-index/README.md) | دليل طبقة الفهرسة |
| [`datasets/judicial-reasoning/extraction-guidelines.md`](../datasets/judicial-reasoning/extraction-guidelines.md) | دليل طبقة الاستخراج |
| [`ROADMAP.md`](../ROADMAP.md) | السياق الزمني للطبقات المستقبلية |
