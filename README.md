![Stars](https://img.shields.io/github/stars/Samix2026/saudi-legal-ai-framework?style=flat) ![Forks](https://img.shields.io/github/forks/Samix2026/saudi-legal-ai-framework?style=flat) ![Contributors](https://img.shields.io/github/contributors/Samix2026/saudi-legal-ai-framework?style=flat) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Version](https://img.shields.io/badge/version-0.2-orange.svg)

> ⚠️ للبحث الأولي فقط — ليس استشارة قانونية. For preliminary research only — not legal advice.

# إطار الذكاء الاصطناعي القانوني السعودي

مجموعة مفتوحة المصدر من المهارات والمصادر القانونية تمنح الذكاء الاصطناعي السياق الصحيح للتعامل مع القانون السعودي.

Open-source collection of legal skills, source references, and datasets that give AI assistants the context they need to reason correctly about Saudi law.

الموقع: [samix2026.github.io/saudi-legal-ai-framework](https://samix2026.github.io/saudi-legal-ai-framework/)

---

## قبل وبعد

**السؤال:** "ما مدة التقادم في دعاوى المطالبة التجارية في السعودية؟"

**بدون الإطار**
> "تتراوح مدة التقادم عادة بين 3 و10 سنوات وفقا للقانون التجاري المعمول به."

❌ مبني على مبادئ غربية عامة — لا يستند إلى أي نظام سعودي.

**مع الإطار** (بعد تحميل `skills/commercial-dispute.md`)
> "وفقا لنظام المحاكم التجارية الصادر بالمرسوم الملكي م/93 لعام 1441ه:
> الدعاوى التجارية العامة: 5 سنوات (المادة 24). الأوراق التجارية: 3 سنوات (نظام الأوراق التجارية م/84).
> حقوق التجار عن سلع لغير التجار: سنة واحدة (المادة 297 نظام المعاملات المدنية م/191).
> الاختصاص: المحاكم التجارية المتخصصة وليس المحاكم العامة."

✅ جواب مستند للنظام السعودي الفعلي مع رقم المرسوم ورقم المادة.

---

## البدء السريع

1. اختر ملف المهارة المناسب من `skills/`
2. انسخ محتواه والصقه مع سؤالك في Claude أو ChatGPT أو Gemini
3. راجع المخرجات مع محامٍ مرخص في المملكة العربية السعودية

> 📖 [دليل الاستخدام الكامل](docs/USAGE_GUIDE.ar.md) · [ابدأ هنا إذا كنت جديدا على GitHub](https://samix2026.github.io/saudi-legal-ai-framework/start.html)

---

## خادم MCP / MCP Server

يتضمن المشروع خادم MCP (Model Context Protocol) مبني على Docker
يتيح لمساعدات الذكاء الاصطناعي استدعاء أدوات التحليل القانوني مباشرة.

### الأدوات المتاحة / Available Tools

| الأداة | الوظيفة |
|--------|---------|
| `analyze_contract_clause` | تحليل بند عقدي وإرجاع JSON بمستوى الخطر والمواد القانونية |
| `get_regulation_summary` | ملخص منظم لأي نظام سعودي من 20 مصدرا |
| `search_contract_risks` | البحث في قاعدة بيانات مخاطر العقود (30 بندا) |

راجع [mcp-server/README.md](mcp-server/README.md) للتفاصيل الكاملة.

---

## نظام تقييم الجودة / Eval Harness

**Saudi Legal AI Eval Harness** نظام تقييم داخلي يقيس دقة وموثوقية أدوات ونماذج
الذكاء الاصطناعي القانوني ضمن السياق المحدود للمصادر السعودية الرسمية.
لا يقدّم استشارة قانونية مباشرة — هدفه قياس جودة الاسترجاع والاستدلال فقط.
جميع الحالات الحالية بحالة `draft` إلى حين مراجعتها من مختص قانوني مرخّص.

An internal evaluation harness that benchmarks the accuracy and legal reliability
of the framework's AI tools and prompts against official Saudi sources. It does
**not** provide direct legal advice; all cases remain in `draft` status pending
review by a licensed Saudi legal professional.

```bash
pip install -r requirements-dev.txt
python3 evals/validate_cases.py
python3 -m pytest tests/test_eval_validator.py -q
```

راجع [evals/README.md](evals/README.md) للتفاصيل الكاملة.

---

## فهرس الملفات

| المجلد | المحتوى | العدد |
|--------|---------|-------|
| `skills/` | ملفات مهارة قانونية موجهة للذكاء الاصطناعي | 9 |
| `sources/` | ملخصات مرجعية للأنظمة السعودية الرسمية | 20 |
| `datasets/` | مجموعات بيانات قانونية منظمة وملفات مخاطر | 11 |
| `examples/` | أمثلة تطبيقية موثقة عبر المجالات القانونية | 14 |
| `prompts/` | قوالب مطالبات جاهزة للاستخدام | 3 |
| `docs/` | موقع Pages + وثائق تقنية | 8 |
| `scripts/` | سكريبتات التحقق والبناء | 8 |
| `tests/` | اختبارات آلية لسكريبتات التحقق | 8 |
| `evals/` | نظام تقييم جودة أدوات الذكاء الاصطناعي القانوني — 5 حالات تقييم أولية (`draft`) | — |
| `mcp-server/` | Docker-based MCP server with 3 legal analysis tools | 6 |

---

## هيكل المستودع

```
saudi-legal-ai-framework/
├── skills/                        # مهارات قانونية موجهة للذكاء الاصطناعي
│   ├── contract-review.md
│   ├── commercial-dispute.md
│   ├── compliance-check.md
│   ├── labor-law-analysis.md
│   ├── legal-drafting.md
│   ├── arbitration.md
│   ├── real-estate-contracts.md
│   ├── intellectual-property-law.md
│   └── sports-dispute.md
├── sources/                       # ملخصات مرجعية للأنظمة السعودية
│   ├── commercial-courts.md
│   ├── companies-law.md
│   ├── labor-law.md
│   ├── pdpl.md
│   ├── arbitration-law.md
│   ├── bankruptcy-law.md
│   ├── evidence-law.md
│   ├── e-commerce-law.md
│   ├── zatca-e-invoicing.md
│   ├── competition-law.md
│   ├── intellectual-property-law.md
│   ├── civil-transactions-law.md
│   ├── whistleblower-protection.md
│   ├── legal-profession-law.md
│   ├── sports-law-saff.md
│   ├── fifa-rstp.md
│   ├── real-estate-arbitration-reac.md
│   ├── regulation-index.md
│   ├── saudi-laws.md
│   ├── open-data-judicial-sources.md
│   └── judicial-decisions/        # ملفات PDF لأحكام 1435هـ
├── datasets/                      # مجموعات بيانات قانونية منظمة
├── examples/                      # أمثلة تطبيقية
├── prompts/                       # قوالب مطالبات
├── docs/                          # موقع GitHub Pages
├── scripts/                       # سكريبتات التحقق والبناء
├── evals/                         # نظام تقييم جودة الذكاء الاصطناعي القانوني
│   ├── schema.json
│   ├── source-registry.json
│   ├── validate_cases.py
│   └── cases/                     # حالات تقييم حسب المجال (draft)
└── mcp-server/                    # Docker MCP server
    ├── Dockerfile
    ├── docker-compose.yml
    ├── server.py
    └── tools/                     # 3 legal analysis tools
        ├── analyzer.py            # analyze_contract_clause
        ├── summarizer.py          # get_regulation_summary
        └── search.py              # search_contract_risks
```

---

## حالة المشروع

| Phase | Status | الحالة |
|-------|--------|--------|
| Phase 1: Foundation | Complete | مكتملة |
| Phase 2: Knowledge Base | In Progress | جارية |
| Phase 3: AI Workflows | Foundation Established | مرحلة أولية |
| Phase 4: MCP Integration | Foundation Established | مرحلة أولية |
| Phase 5: Product Layer | Planned | مخطط لها |

راجع [ROADMAP.md](ROADMAP.md) للخطة الكاملة.

**الرؤية المستقبلية:** استكمال التغطية لخمسة مجالات تشريعية رئيسية، وإضافة أمثلة في قطاعات العقار والتقنية والرعاية الصحية.
مراجعة المحتوى من محامين سعوديين مرخصين، ثم واجهة ويب تتيح رفع المستندات وتشغيل التحليل مباشرة.
المدى البعيد: MCP server يربط النماذج بقواعد البيانات القضائية ونصوص الأنظمة مباشرة.

---

## مساعدات الذكاء الاصطناعي المدعومة

| النموذج | طريقة الاستخدام |
|---------|----------------|
| Claude (claude.ai) | الصق محتوى ملف المهارة مباشرة في المحادثة قبل سؤالك |
| ChatGPT (chatgpt.com) | افتح محادثة جديدة، الصق الملف، ثم اكتب سؤالك |
| Gemini (gemini.google.com) | الصق محتوى الملف في بداية المحادثة ثم سؤالك |
| أي نموذج يتبع التعليمات | نفس الأسلوب — الملفات تعمل مع أي LLM |

---

## المساهمة

**3 مسارات للمساهمة:**

**⚖️ محامٍ أو مستشار قانوني**
راجع ملفات `skills/` أو `sources/` وأضف تصحيحات مستندة إلى مراسيم رسمية.
كل تعديل يجب أن يشير إلى رقم المرسوم أو رقم المادة.

**📋 باحث أو محلل**
أضف أمثلة تطبيقية في `examples/` أو وسّع مجموعات البيانات في `datasets/`.
المحتوى يجب أن يشير إلى مصادر رسمية سعودية.

**📝 مطور أو كاتب**
حسّن وثائق `docs/` أو سكريبتات التحقق في `scripts/`.
افتح Issue أولا لمناقشة الإضافات الجوهرية قبل فتح PR.

اقرأ [CONTRIBUTING.md](CONTRIBUTING.md) للتفاصيل الكاملة.

### Good First Issues

| المهمة | الملف | الجهد |
|--------|-------|-------|
| إضافة مثال تطبيقي لعقد إيجار تجاري | `examples/` | منخفض |
| مراجعة labor-law.md والإشارة إلى أي أحكام قديمة | `sources/labor-law.md` | منخفض |
| إضافة روابط المصادر الرسمية الناقصة | `sources/` | منخفض |
| تحسين جودة الترجمة الإنجليزية في أي ملف مهارة | `skills/` | منخفض |
| اقتراح قالب مطالبة جديد لقطاع غير مغطى | `prompts/` | متوسط |

---

## المصادر الرسمية

| المحتوى | الرابط | الجهة |
|---------|--------|-------|
| الأنظمة والتشريعات الرسمية | [boe.gov.sa](https://boe.gov.sa) | هيئة الخبراء بمجلس الوزراء |
| الجريدة الرسمية | [uqn.gov.sa](https://uqn.gov.sa) | أم القرى |
| الأنظمة المقترحة للاستشارة العامة | [istitlaa.ncc.gov.sa](https://istitlaa.ncc.gov.sa) | منصة استطلاع |
| وزارة العدل | [moj.gov.sa](https://www.moj.gov.sa) | وزارة العدل |
| الخدمات القضائية الإلكترونية | [najiz.sa](https://www.najiz.sa) | منصة ناجز |
| أنظمة العمل والموارد البشرية | [hrsd.gov.sa](https://www.hrsd.gov.sa) | وزارة الموارد البشرية |
| الاتحاد السعودي لكرة القدم | [saff.com.sa](https://www.saff.com.sa) | لوائح اللاعبين والانتقالات والتأديب |
| FIFA Legal | [inside.fifa.com/legal](https://inside.fifa.com/legal) | RSTP — لوائح الانتقالات الدولية |
| المركز السعودي للتحكيم العقاري | [reac.rega.gov.sa](https://reac.rega.gov.sa) | تحكيم وصلح النزاعات العقارية |
| المركز السعودي للتحكيم التجاري | [sadr.org](https://www.sadr.org) | التحكيم التجاري العام |
| اللجنة الدائمة لمراكز التحكيم | [scsac.org.sa](https://www.scsac.org.sa) | ترخيص وحوكمة مراكز التحكيم |

---

## المساهمون

| المساهم | المساهمة |
|---------|---------|
| [@Majedmhm](https://github.com/Majedmhm) | تصحيح مدد التقادم في نظام المحاكم التجارية |
| [@al3obdi](https://github.com/al3obdi) | نظام الإثبات، نظام التجارة الإلكترونية، نظام المعاملات المدنية |

---

## الترخيص

[MIT License](LICENSE) — للاستخدام الحر مع نسب المصدر والاحتفاظ بإخلاء المسؤولية القانوني.
