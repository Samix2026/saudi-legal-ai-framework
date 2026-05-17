# Architecture Audit — v1
# تدقيق المعمارية — الإصدار الأول

**تاريخ التدقيق / Audit Date:** 2026-05-17
**المراجع / Reviewer:** Claude Code — استنادًا إلى قراءة كاملة لجميع ملفات المشروع
**الإصدار / Project Version:** v0.3 قيد العمل
**ملاحظة / Note:** graphify-out/GRAPH_REPORT.md غير موجود — التدقيق بني على قراءة مباشرة للملفات

---

## ⚠️ إخلاء مسؤولية / Disclaimer

> هذا التدقيق تحليل معماري — لا استشارة قانونية. الملاحظات تتعلق بهيكل المشروع وقابليته للتوسع، لا بدقة المحتوى القانوني.

---

## 1. تحليل الطبقات الحالية / Current Layer Analysis

### 1.1 جدول حالة الطبقات / Layer State Table

| الطبقة | المجلد | عدد الملفات | حالة التنفيذ | مستوى النضج |
|--------|--------|------------|-------------|------------|
| Legislative Sources | `sources/` | 8 md + 14 pdf | نشط | متوسط — محتوى موثق، تحقق قانوني مفقود |
| Judicial Corpus | `sources/judicial-decisions/1435/` | 14 pdf | موجود — غير قابل للاستخراج | قشرة بدون لب |
| Corpus Index | `datasets/judicial-index/` | 1 csv (5 صفوف) | بداية — 5/14 فقط | ضعيف جدًا |
| Judicial Extraction | `datasets/judicial-reasoning/` | 1 example.md | إطار جاهز — محتوى شبه معدوم | إطار بدون بيانات |
| Contract Dataset | `datasets/` | 1 csv (3 صفوف) | نشط — قيم حقيقية | ضعيف — 3 صفوف فقط |
| Enums | `datasets/enums/` | 5 md | كامل | عالٍ — محدد ومُنفَّذ |
| Validation Scripts | `scripts/` | 2 py | يعمل — 43 اختبارًا | عالٍ |
| Skills | `skills/` | 5 md | نشط | متوسط — هيكل موحد، تحقق مفقود |
| Prompts | `prompts/` | 3 md | نشط | متوسط |
| Examples | `examples/` | 3 md | نشط — ناقص للبعض | متوسط |
| OCR | `experiments/ocr-benchmark/` | benchmark فقط | تجريبي | لا pipeline حقيقي |
| MCP Planning | `docs/mcp-integration-notes.md` | 1 md | توثيق نظري | مبكر جدًا |
| CI/CD | `.github/workflows/` | 2 yml | يعمل | عالٍ |

---

### 1.2 الملاحظات الجوهرية لكل طبقة / Key Layer Observations

**Legislative Sources (sources/):**
- `regulation-index.md` يسجل 10 أنظمة، لكن 5 منها بدون ملف `sources/` مخصص (نظام التحكيم، الوكالة التجارية، الملكية الفكرية، الإفلاس، التعاملات الإلكترونية)
- جميع ملفات المصادر بحالة `educational-reference` — لا يوجد ملف واحد بحالة `verified`
- `civil-transactions-law.md` هو الأكثر تفصيلًا وتوثيقًا، لكنه يحتوي ~9 `TO VERIFY` items في أرقام المواد

**Judicial Corpus:**
- 14 ملف PDF — لا يوجد text extraction لأي منها
- الـ OCR benchmark كشف: دقة 65-75% لنصوص الفقرات، فشل كامل في الجداول
- الفهرس `judicial-corpus-index.csv` يحتوي 5 صفوف فقط من مجلد 1 فقط (من أصل 14 مجلد)
- جميع صفوف الفهرس بـ `start_page = 0` و `end_page = 0` — لم تُقرأ الصفحات بعد

**Judicial Extraction:**
- مثال واحد حقيقي: `property-sale-proof-1435-example.md` — بحالة `ocr_draft`
- الإطار (schema 19 حقل) جاهز تمامًا
- البيانات شبه معدومة: 1 extraction من 14 مجلد

**Contract Dataset:**
- الملف الرئيسي: 3 صفوف فقط — جميعها `hypothetical`, `draft`
- `datasets/build/saudi-contract-risk-dataset.generated.csv` مُولَّد آليًا
- `datasets/contributions/saas/example-saas-risk-patterns.csv` موجود — لم يُتحقق منه

---

## 2. اكتشافات المشاكل المعمارية / Architectural Issues Discovered

### 2.1 Duplicated Concepts / مفاهيم مكررة

| المفهوم | أين يظهر | المشكلة |
|---------|---------|---------|
| `verification_status` enum | `datasets/enums/verification-status.md` + `docs/legal-verification-lifecycle.md` + `datasets/schema.md` + `datasets/judicial-reasoning/schema.md` + `datasets/judicial-index/schema.md` | 5 أماكن تُعرِّف/تصف نفس الـ enum — لا single source of truth لقيم الـ enum نفسها؛ `validate_dataset.py` يحمل القيم hardcoded |
| disclaimer | في كل ملف `skills/`, `prompts/`, `examples/`, `sources/` بصياغات متفاوتة | لا template file واحد — المرحلة 1 وحَّدت الصياغة يدويًا لكن الأصل لا يزال مكررًا |
| `court_type` enum | `datasets/judicial-reasoning/schema.md §4` + `datasets/judicial-index/schema.md §10` | معرَّف في ملفين — لا ملف enum مستقل مثل `datasets/enums/` |
| `source_type` | قيم مختلفة في `datasets/schema.md` (`hypothetical`, `abstracted`...) مقابل قيمة `source_type: official_regulation_summary` في `sources/` files | نفس الاسم، قيم مختلفة، سياقات مختلفة — خطر terminology drift |

### 2.2 Inconsistent Schemas / عدم اتساق المخططات

| المخطط | الإشكالية |
|--------|----------|
| judicial-reasoning schema (19 حقل) | يستخدم `case_id` بصيغة `JD-{year}-{seq}` |
| judicial-index schema (13 حقل) | يستخدم `index_id` بصيغة `IDX-{year}-{vol}-{seq}` |
| الربط بين الاثنين | لا `foreign key` صريح — `source_pdf` مشترك لكن لا `index_id` في ملفات الـ extraction |
| main dataset | يستخدم `id` عدد صحيح بسيط |
| النتيجة | 3 أنظمة معرِّفات مختلفة في نفس المشروع — لا اتساق |

### 2.3 Weak Boundaries / حدود ضعيفة

| الحد | المشكلة |
|------|---------|
| `skills/` vs `sources/` | `skills/` تحتوي على معلومات نظامية (مثل "المادة 84 EOSB") وليس فقط "كيفية التفكير" — CLAUDE.md يقول skills تصف "how to reason" لكن المحتوى الفعلي يصف "what the law says" أيضًا |
| `sources/` vs `docs/` | `docs/mcp-integration-notes.md` أُنشئ حديثًا لكن لا يوجد `docs/sources-guide.md` — خطر أن تمتد ملفات `docs/` لتحل محل `sources/` |
| `examples/` vs `prompts/` | ثلاثة ملفات في `examples/` — اثنان منها توضيحيان، والثالث (`saudi-contract-review-demo.md`) يحتوي على prompt templates كاملة — يجب أن يكون في `prompts/` |
| `experiments/` vs production | مجلد `experiments/` موجود مع OCR benchmark — لكن لا CONTRIBUTING.md يذكره ولا CI يتحقق منه |

### 2.4 Tightly Coupled Files / ملفات مترابطة بإحكام

| الزوج | طبيعة الترابط | المخاطرة |
|-------|--------------|---------|
| `prompts/review-contract.md` ← `skills/contract-review.md §8` | الـ prompt يشير صراحةً لـ §8 بوصفه المرجع للهيكل | أي إعادة ترقيم لأقسام skill تكسر الـ prompt |
| `scripts/validate_dataset.py` ← `datasets/enums/*.md` | الـ enums محفوظة hardcoded في السكربت — قيم مكررة في 2 أماكن | تغيير enum value يستلزم تعديل ملفين يدويًا |
| `datasets/build/` ← `scripts/build_dataset.py` | الـ build output محفوظ في الـ repo | خطر: بيانات مُولَّدة vs مصدر في نفس الـ repo |

### 2.5 Missing Registries / سجلات مفقودة

| ما ينقص | الأثر |
|---------|-------|
| **Court Type Registry** | `court_type` enum معرَّف في ملفين schema بدون ملف enum مستقل في `datasets/enums/` |
| **Case Domain Registry** | `case_domain` في schema الاستخراج بدون ملف enum |
| **Extraction Priority Registry** | `extraction_priority` في schema الفهرس بدون ملف enum |
| **OCR Status Registry** | `ocr_draft` حالة مُستخدَمة في benchmark وفي ملف الاستخراج الأول — لكنها غير معرَّفة رسميًا في أي enum file؛ `verification-status.md` لا يذكرها |
| **Source Tier Registry** | `mcp-integration-notes.md` يعرِّف Tier 1-4 غير رسميًا — لا سجل مركزي |
| **Skill Registry** | لا index لملفات skills — CLAUDE.md يذكر 5 skills لكن لا ملف يعددها رسميًا بخصائصها |

### 2.6 Missing Abstractions / تجريدات مفقودة

| التجريد المفقود | لماذا ضروري |
|----------------|------------|
| **Regulation Abstraction Layer** | `regulation-index.md` يسجل أسماء وأرقام فقط — لا schema موحد لتمثيل كل نظام (articles count, effective date, amendment history) |
| **Pipeline State Machine** | دورة `ocr_draft → draft → pending-review → reviewed → verified` موثقة نثرًا — لا state machine رسمي يمنع الانتقالات غير الصحيحة |
| **Extraction Job Tracker** | لا نظام لتتبع أي أقسام من الـ PDFs قيد الاستخراج، أي انتهت، أي معطلة |
| **Contributor Interface** | ملف `CONTRIBUTING.md` يصف العملية نثرًا — لا template رسمي للمساهمة في `sources/` |

### 2.7 Terminology Drift / انجراف المصطلحات

| المصطلح | الاستخدام الحالي | التعارض |
|---------|----------------|--------|
| `source_type` | في datasets: قيم `hypothetical/abstracted/published_case` | في sources/ files: يُستخدم في metadata بمعنى `official_regulation_summary` — معنيان مختلفان لنفس المصطلح |
| `draft` | في dataset: `verification_status = draft` | في civil-transactions-law.md: `status: draft-educational-reference` (YAML frontmatter) — 2 نظامين مختلفين لنفس الكلمة |
| "Mandatory provision" | في sources/ files: `Mandatory Non-Waivable Provisions` (المرحلة 2) | في skills/ files: "الأحكام الآمرة" | في datasets: `requires_escalation` — 3 تمثيلات لمفهوم واحد بدون ربط |
| "Verification" | تعني: مراجعة الجودة القانونية في datasets | تعني: التحقق من أرقام المواد في sources/ `to_verify` | لا فرق واضح بين النوعين |
| "Source" | `sources/` directory | `source_type` column | `source_pdf` field | `official_reference` في metadata — 4 استخدامات |

### 2.8 Naming Inconsistencies / تعارضات التسمية

| المشكلة | التفصيل |
|---------|---------|
| `judicial-decisions` vs `judicial-reasoning` vs `judicial-index` | المجلدات الثلاثة تبدأ بـ `judicial-` لكن موضوعاتها مختلفة — لا وحدة مفاهيمية |
| `cross-reference-map.md` يذكر `civil-transactions-law.md` بينما النظام الأساسي في ROADMAP/README يُسمى المعاملات المدنية | ليس خطأً لكن التناوب بين التسمية الإنجليزية والعربية في أسماء الملفات غير متسق |
| `saudi-laws.md` اسم عام جدًا لملف نظرة عامة — يمكن الخلط مع "all saudi laws" | يُوهم بأنه يغطي كل الأنظمة |
| الملفات في `datasets/examples/` تُسمى `employment-contracts.csv`، `saas-agreements.csv`، `construction-contracts.csv` — بينما `datasets/contributions/saas/` يحتوي `example-saas-risk-patterns.csv` | تسميتان مختلفتان لمحتوى متشابه |

---

## 3. تحليل خاص للـ Pipelines الحرجة / Critical Pipeline Analysis

### 3.1 Judicial Reasoning Pipeline

```
الحالة الفعلية (Current State):

sources/judicial-decisions/1435/*.pdf [14 ملف]
        │
        ▼ [يدوي — بطيء جدًا]
datasets/judicial-index/judicial-corpus-index.csv [5 صفوف — مجلد 1 فقط]
        │
        │ BLOCKED: start_page/end_page = 0 لجميع الصفوف
        ▼
datasets/judicial-reasoning/ [مثال واحد — ocr_draft]

التقدير الحقيقي: 5/14 مجلدات مفهرسة (جزئيًا)، 1/5 قسم مستخرج
```

**المشاكل الجوهرية:**
1. الـ pipeline يدوي بالكامل — لا أتمتة في أي مرحلة حتى OCR
2. `judicial-corpus-index.csv` بـ 5 صفوف كلها `start_page = 0` — لم يُقرأ فهرس أي PDF فعليًا
3. لا ربط بين `index_id` في الفهرس و `case_id` في الاستخراج — ربط ضمني فقط عبر `source_pdf`
4. `ocr_draft` حالة غير معرَّفة في نظام التحقق الرسمي — تعيش خارج النظام
5. لا نظام لتتبع أي صفحات قُرئت وأيها لم تُقرأ

### 3.2 OCR Lifecycle

```
الحالة الفعلية:

experiments/ocr-benchmark/ [3 صفحات مختبرة من 502 صفحة في مجلد 1 فقط]
        │
        │ Go/No-Go Decision: ⚠️ مشروط
        ▼
[لا pipeline إنتاجي] [لا preprocessing] [لا post-processing]
[لا معيار quality control] [لا حد أدنى للدقة]
```

**الفجوات:**
- لا تعريف رسمي لـ "ما مستوى الدقة المقبول للترقية من `ocr_draft`"
- لا اختبار لـ PaddleOCR (المقترح كبديل في README)
- لا معالجة مسبقة للصورة (deskew, contrast, binarization)
- الـ benchmark يغطي مجلد 1 فقط — PDF المولود بـ InDesign — المجلدات الأخرى قد تكون مسحًا ورقيًا حقيقيًا (أصعب)

### 3.3 Verification Lifecycle

```
الحالة الفعلية:

draft → pending-review → reviewed → verified
  │
  │ المشكلة: 0 صفوف verified في أي ملف في المشروع
  │ جميع المحتوى = draft أو to_verify
  │
  │ السبب: لا محامٍ مرخَّص راجع المحتوى بعد
  │
  ▼
bottleneck حرج: SINGLE HUMAN BOTTLENECK
الترقية لـ verified تتطلب محامٍ سعودي مرخَّص —
لا آلية للعثور عليه، لا workflow واضح لكيفية التعاون،
لا incentive structure في CONTRIBUTING.md
```

**المخاطر:**
- المشروع بأكمله في حالة `draft` — لا محتوى `verified` في أي طبقة
- لا تمييز بين "draft بسبب عدم المراجعة" و "draft بسبب عدم اليقين بالمحتوى"
- `ocr_draft` حالة خارج النظام الرسمي — من يرقيها؟ بأي معيار؟

### 3.4 Source Hierarchy

```
TIER 1 (رسمي إلزامي):  boe.gov.sa + uqn.gov.sa
        ↓  (يُلخَّص في)
TIER 1.5 (ملفات sources/ — غير رسمي):  sources/*.md  [UNLABELED TIER]
        ↓  (يُشار إليه في)
TIER 2 (مهارات AI):  skills/*.md
        ↓  (يُطبَّق في)
TIER 3 (prompts/examples):  prompts/*.md + examples/*.md

المشكلة: sources/*.md تُسوَّق كـ "summaries of official sources"
لكنها في الواقع طبقة بينية غير رسمية لم يُتحقق منها.
يوجد خطر يستشهد به المستخدم بـ sources/labor-law.md
كأنه النص الرسمي.
```

### 3.5 MCP Future Integration

```
التوثيق الحالي:
  - docs/official-api-sources.md  [توثيق نظري — Phase 4]
  - docs/mcp-integration-notes.md [جديد — توثيق نظري]
  - ROADMAP.md §Phase 4

المشاكل المعمارية لـ MCP مستقبلًا:
  1. لا data model يحدد ما "الوحدة القابلة للاسترجاع" — مادة؟ مجموعة مواد؟ ملف source كامل؟
  2. لا caching strategy للنصوص المسترجَعة
  3. لا versioning للمحتوى الخارجي (تتبع متى تغير النص الرسمي)
  4. لا conflict resolution عند تعارض النص المسترجَع مع sources/*.md
  5. Tier system في mcp-integration-notes.md غير مرتبط رسميًا بـ regulation-index.md
```

---

## 4. الـ Source-of-Truth غير المقصودة / Unintended Sources of Truth

| الملف | الدور المقصود | الدور الفعلي / المشكلة |
|-------|--------------|----------------------|
| `sources/regulation-index.md` | سجل صيغ الاستشهاد | أصبح أيضًا مرجع الـ Tier system، وقائمة المصادر المفتوحة، وأداة التوثيق — ثقيل جدًا |
| `scripts/validate_dataset.py` | أداة تحقق | يحتوي hardcoded enums — أصبح source-of-truth للقيم المقبولة بدلًا من `datasets/enums/*.md` |
| `docs/cross-reference-map.md` | خريطة تبعيات | أصبح يحتوي قواعد الصيانة والإجراءات — دور CONTRIBUTING.md |
| `CLAUDE.md` | توجيهات للـ AI | يحتوي قواعد disclaimer إلزامية لـ prompts/examples — لا يُشير إلى ملف disclaimer موحد |
| `examples/saudi-contract-review-demo.md` | مثال تطبيقي | يحتوي prompt templates كاملة — دور prompts/ |

---

## 5. Top 10 Architectural Risks / أعلى 10 مخاطر معمارية

| الرقم | الخطر | الاحتمالية | الأثر | المستوى |
|-------|-------|-----------|-------|---------|
| 1 | **صفر محتوى verified** — المشروع بأكمله في حالة draft؛ لا آلية عملية لإشراك محامٍ مرخَّص | عالية | كارثي | 🔴 حرج |
| 2 | **OCR pipeline غير موجود** — 14 مجلد PDF لا يمكن استخراج نصها؛ الفهرس شبه فارغ؛ الاستخراج شبه معدوم | عالية | عالٍ | 🔴 حرج |
| 3 | **Enums مكررة hardcoded** في validate_dataset.py — تغيير enum value دون تحديث السكربت يُفشل CI بصمت أو يقبل قيمًا خاطئة | متوسطة | متوسط | 🟠 مرتفع |
| 4 | **`ocr_draft` خارج نظام التحقق** — لا تعريف رسمي، لا معيار ترقية، لا من يرقيها؛ محتوى في منطقة رمادية | عالية | متوسط | 🟠 مرتفع |
| 5 | **Judicial index فارغة فعليًا** — 5 صفوف كلها `start_page = 0`؛ الـ pipeline يبدأ من لا شيء | عالية | عالٍ | 🟠 مرتفع |
| 6 | **terminology drift لـ `source_type`** — معنيان مختلفان في طبقتين — خطر حدوث confusion عند توسيع المشروع | متوسطة | متوسط | 🟡 متوسط |
| 7 | **تضخم regulation-index.md** — يحمل أدوارًا متعددة؛ سيصعب صيانته عند وصول الأنظمة لـ 20+ | منخفضة | متوسط | 🟡 متوسط |
| 8 | **missing court_type/case_domain enums** — معرَّفة في schemas لكن بدون validation؛ لا CI يتحقق من قيمها | متوسطة | منخفض | 🟡 متوسط |
| 9 | **لا foreign key بين judicial-index وjudicial-reasoning** — ربط ضمني عبر `source_pdf` فقط؛ يصعب الإحصاء والتحقق | منخفضة | متوسط | 🟡 متوسط |
| 10 | **MCP Tier system غير مرتبط بـ regulation-index** — تعريفات متوازية؛ خطر تعارضها عند التوسع | منخفضة | منخفض | 🟢 منخفض |

---

## 6. Top 10 Structural Improvements / أفضل 10 تحسينات هيكلية

| الأولوية | التحسين | الجهد | الأثر |
|---------|---------|-------|-------|
| 1 | **إنشاء `datasets/enums/court-type.md` + `case-domain.md` + `extraction-priority.md`** — استخراج الـ enums من schemas إلى ملفات مستقلة وإضافة validation | صغير | عالٍ |
| 2 | **تعريف `ocr_draft` رسميًا في `datasets/enums/verification-status.md`** وتوثيق شروط الترقية منها | صغير | عالٍ |
| 3 | **فصل الـ enums من validate_dataset.py** إلى قراءة ديناميكية من ملفات `datasets/enums/` — قضاء على التكرار | متوسط | عالٍ |
| 4 | **إضافة `index_id` كـ foreign key في schema الاستخراج** — تمكين الربط الصريح بين الفهرس والاستخراج | صغير | متوسط |
| 5 | **إنشاء `sources/SOURCES_GUIDE.md`** يشرح طبيعة ملفات sources/ (educational summaries, not official text) — مرجع صريح يقلل خطر الاستشهاد الخاطئ | صغير | عالٍ |
| 6 | **نقل prompt templates من `examples/saudi-contract-review-demo.md` إلى `prompts/`** أو توثيق الفرق صراحةً | صغير | متوسط |
| 7 | **إضافة disclaimer template file** يُشار إليه من CLAUDE.md بدلًا من نسخه في كل ملف | صغير | متوسط |
| 8 | **إنشاء `datasets/judicial-index/INDEXING_PROGRESS.md`** لتتبع أي الـ PDFs فُهرست وأيها لم تُفهرس | صغير | عالٍ |
| 9 | **إضافة `article_id` field** في المستقبل لربط provisions في `sources/` بـ `related_regulation` في datasets | كبير | عالٍ (مستقبلًا) |
| 10 | **توحيد الـ Source Tier system** في `regulation-index.md` بدلًا من تعريفه في `mcp-integration-notes.md` فقط | صغير | متوسط |

---

## 7. ما يجب تجميده الآن / What to Freeze Now

> لا تُضف إليها ولا تعدِّلها إلا لإصلاح خطأ موثق:

| الملف / الطبقة | سبب التجميد |
|----------------|------------|
| `scripts/validate_dataset.py` و `scripts/build_dataset.py` | تعمل بشكل صحيح — أي تغيير يخاطر بكسر CI؛ لا تُعدِّل إلا لإضافة enum جديد مدروس |
| `datasets/enums/risk-levels.md` | تعريف ناضج ومُنفَّذ — تغيير القيم يكسر datasets موجودة |
| `datasets/enums/verification-status.md` | نفس السبب — لكن يحتاج إضافة `ocr_draft` بالعملية الصحيحة |
| `.github/workflows/` | CI يعمل — لا تُعدِّله دون اختبار محلي كامل |
| `sources/judicial-decisions/1435/` | الـ PDFs source-of-truth لكل الاستخراج — لا تحذف ولا تُعيد تسمية |
| `datasets/judicial-reasoning/schema.md` | الإطار مكتمل — لا تُضف حقولًا قبل أن تكون هناك 10+ extractions تُبرر التغيير |

---

## 8. ما يجب Refactor له مبكرًا / What Needs Early Refactoring

| الهدف | الأولوية | الخطوات |
|-------|---------|---------|
| **إنشاء enum files للـ judicial schemas** | عالية | أنشئ `datasets/enums/court-type.md`, `case-domain.md`, `extraction-priority.md` من القيم الموثقة في schemas |
| **تعريف `ocr_draft` رسميًا** | عالية | أضفها في `datasets/enums/verification-status.md` + وثِّق شروط الترقية في `docs/legal-verification-lifecycle.md` |
| **إنشاء progress tracker للـ judicial pipeline** | عالية | ملف `datasets/judicial-index/INDEXING_PROGRESS.md` أو عمود إضافي في الـ CSV |
| **توحيد `source_type`** | متوسطة | غيِّر اسم metadata field في sources/ files من `source_type` إلى `sources_tier` لتجنب الالتباس |
| **استخراج disclaimer لملف مرجعي** | منخفضة | ملف `templates/legal-disclaimer.md` يُشار إليه من CLAUDE.md |

---

## 9. ما لا يجب لمسه الآن / What Not to Touch Now

| الطبقة / الملف | السبب |
|----------------|-------|
| `docs/legal-verification-lifecycle.md` | مستوفٍ وناضج — لا تُعدِّله إلا عند إضافة `ocr_draft` رسميًا |
| `docs/cross-reference-map.md` | دقيق ومفصَّل — أي تعديل يتطلب مراجعة شاملة لجميع التبعيات |
| `sources/civil-transactions-law.md` | أكثر الملفات تفصيلًا وتوثيقًا — التعديلات تستلزم تحقق أرقام مواد من النص الرسمي |
| `datasets/judicial-reasoning/extraction-guidelines.md` | الدليل مكتمل — لا تُعدِّله قبل وجود 5+ extractions تكشف احتياج تعديل حقيقي |
| `prompts/*.md` | تعمل بشكل صحيح — أي تعديل يتطلب اختبار على نماذج متعددة |
| `CONTRIBUTING.md` | يُنظِّم عملية المساهمة — تعديله يؤثر على توقعات المساهمين الخارجيين |

---

## 10. تصنيف المشروع / Project Classification

### ما هو المشروع الآن؟

```
╔══════════════════════════════════════════════════════════════════╗
║  Documentation Repo                                              ║
║  ████████████████████████████████████░░░░░░  85%               ║
║                                                                  ║
║  Knowledge Base (draft)                                          ║
║  ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░  40%               ║
║                                                                  ║
║  Legal Infrastructure                                            ║
║  ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  20%               ║
║                                                                  ║
║  Legal Intelligence Platform                                     ║
║  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  10%               ║
║                                                                  ║
║  Research Architecture                                           ║
║  █████████████████████████░░░░░░░░░░░░░░░░  60%               ║
╚══════════════════════════════════════════════════════════════════╝
```

**التصنيف الأدق / Most Accurate Classification:**

> **Research Architecture في طور بناء Knowledge Base**

المشروع يمتلك بنية تحتية وثائقية ناضجة (governance, CI/CD, schemas, verification lifecycle) — لكن المحتوى الذي يملأ تلك البنية لا يزال في مراحل أولى جدًا. الـ infrastructure جاهزة لاستقبال محتوى حقيقي؛ المحتوى نفسه لم يصل بعد.

**ما ليس المشروع عليه بعد:**
- ليس Legal Infrastructure بالمعنى الكامل: لا محتوى verified قابل للاستشهاد به في عمل قانوني
- ليس Legal Intelligence Platform: لا retrieval, لا reasoning engine, لا agent workflows
- ليس Knowledge Base كاملة: 3 صفوف في main dataset, 1 judicial extraction

---

## 11. تقييم Readiness لكل مرحلة / Readiness Assessment

### 11.1 OCR Scaling Readiness

| المعيار | الحالة | التفاصيل |
|---------|-------|---------|
| أداة OCR مختارة | ⚠️ جزئي | Tesseract مُقيَّم؛ PaddleOCR لم يُختبر بعد |
| معيار جودة محدد | ❌ غائب | لا حد أدنى للدقة قبل الترقية من ocr_draft |
| preprocessing pipeline | ❌ غائب | لا deskew, binarization, contrast |
| human review workflow | ❌ غائب | لا تقدير لوقت مراجعة صفحة واحدة |
| storage strategy | ⚠️ جزئي | الصور في experiments/ — لا strategy للإنتاج |
| **الحكم / Verdict** | ❌ **غير جاهز** | يحتاج: اختبار PaddleOCR + تحديد معيار جودة + preprocessing |

### 11.2 Judicial Extraction Scaling Readiness

| المعيار | الحالة | التفاصيل |
|---------|-------|---------|
| schema جاهز | ✅ مكتمل | 19 حقل موثق ومُصمَّم |
| extraction guidelines | ✅ مكتملة | دليل شامل للاستخراج والتجريد |
| corpus index | ❌ شبه فارغ | 5 صفوف، جميعها start_page = 0 |
| OCR text | ❌ معدوم | لا نص مستخرَج من أي PDF |
| reviewer pool | ❌ غائب | لا مراجعون قانونيون محددون |
| **الحكم / Verdict** | ❌ **غير جاهز** | BLOCKED على: إكمال الفهرس + OCR pipeline |

### 11.3 Contributor Scaling Readiness

| المعيار | الحالة | التفاصيل |
|---------|-------|---------|
| CONTRIBUTING.md | ✅ موجود | شامل |
| CI validation | ✅ يعمل | 43 اختبار |
| contribution templates | ⚠️ جزئي | .github/ISSUE_TEMPLATE موجود، لكن لا PR template لـ sources/ |
| enum validation للـ judicial | ❌ غائب | court_type/case_domain لا تُتحقق آليًا |
| staging workflow | ✅ موجود | datasets/contributions/ |
| **الحكم / Verdict** | ⚠️ **جاهز للـ dataset contributions** — غير جاهز للـ sources أو judicial contributions |

### 11.4 Legal Review Scaling Readiness

| المعيار | الحالة | التفاصيل |
|---------|-------|---------|
| workflow لإشراك محامٍ | ❌ غائب | CONTRIBUTING.md يذكره لكن لا آلية عملية |
| incentive structure | ❌ غائب | لا ذكر لكيفية التعرف على المراجع أو تحفيزه |
| review interface | ❌ غائب | لا template رسمي "للمراجع القانوني" |
| audit trail | ⚠️ جزئي | reviewed_by_lawyer field موجود — لكن لا مكان لبيانات المراجع |
| **الحكم / Verdict** | ❌ **غير جاهز** | Single bottleneck بدون حل |

### 11.5 MCP Integration Readiness

| المعيار | الحالة | التفاصيل |
|---------|-------|---------|
| data model للوحدة القابلة للاسترجاع | ❌ غائب | لا تعريف لما يُسترجَع |
| regulation versioning | ❌ غائب | لا تتبع تاريخ تغيير النص الرسمي |
| conflict resolution | ❌ غائب | لا آلية عند تعارض المسترجَع مع sources/ |
| rate limiting / caching | ❌ غائب | لا strategy |
| **الحكم / Verdict** | ❌ **غير جاهز** — مبكر جدًا؛ يتطلب إكمال المحتوى أولًا |

### 11.6 Future Retrieval/RAG Readiness

| المعيار | الحالة | التفاصيل |
|---------|-------|---------|
| محتوى verified قابل للـ chunking | ❌ معدوم | 0 صفوف verified |
| embedding strategy | ❌ غائب | لم تُحدَّد |
| retrieval unit | ❌ غائب | مادة؟ قسم؟ ملف؟ |
| Arabic embedding model | ❌ غائب | لم يُقيَّم |
| **الحكم / Verdict** | ❌ **غير جاهز** — يحتاج محتوى verified أولًا |

### ملخص Readiness / Readiness Summary

| المرحلة | الجاهزية |
|---------|---------|
| Dataset Contributions | ✅ جاهز — الـ pipeline يعمل |
| Sources Documentation | ⚠️ جزئي — infrastructure جاهزة، محتوى يحتاج تحقق |
| OCR Scaling | ❌ يحتاج عمل |
| Judicial Extraction Scaling | ❌ BLOCKED على OCR + فهرسة |
| Legal Review Scaling | ❌ يحتاج workflow جديد |
| MCP Integration | ❌ مبكر جدًا |
| RAG / Retrieval | ❌ يحتاج محتوى verified أولًا |

---

## 12. ملخص تنفيذي / Executive Summary

### نقاط القوة / Strengths

1. **بنية تحتية ناضجة** — CI/CD, validation, schemas, verification lifecycle: كلها مُصمَّمة جيدًا
2. **Judicial schema ممتاز** — 19 حقل لـ reasoning extraction مدروس ومفصَّل
3. **regulation-index.md** نقطة تحكم مركزية فعَّالة
4. **cross-reference-map.md** يوثِّق التبعيات بشكل مرجعي نادر
5. **OCR benchmark موثَّق** — القرار التقني (Go/No-Go) مُبرَّر بدليل عملي
6. **Separation of concerns** بين skills/prompts/examples واضح نسبيًا

### نقاط الضعف الجوهرية / Core Weaknesses

1. **صفر محتوى verified** — المشروع يبني بنية تحتية لمحتوى لم يصل بعد
2. **Judicial pipeline شبه معدوم** — 5 صفوف فهرس فارغة، 1 extraction
3. **Single reviewer bottleneck** بلا حل — كيف يصل المحتوى لـ verified؟
4. **OCR بلا pipeline** — الـ benchmark يُثبت إمكانية العمل لكن لا pipeline إنتاجي
5. **Terminology drift** في `source_type` و `draft` و `verification` بين الطبقات

### التوصية الاستراتيجية / Strategic Recommendation

> المشروع وصل إلى نقطة تحول: البنية التحتية جاهزة، لكن استمرار بناء البنية التحتية دون ملء المحتوى أصبح يُقلِّل العائد.
>
> **الأولوية القصوى:** إيجاد مراجع قانوني مرخَّص ولو لمراجعة ملف واحد — `sources/labor-law.md` — وترقيته لـ `verified`. هذا الصف الأول `verified` سيثبت أن دورة حياة التحقق قابلة للتشغيل الفعلي.
>
> **الأولوية الثانية:** إكمال فهرسة PDF واحد من 14 — `1.pdf` — بأرقام صفحات حقيقية. هذا وحده يُمكِّن extraction حقيقية.

---

*هذا تدقيق معماري — لا استشارة قانونية. جميع الملاحظات تتعلق بهيكل المشروع وقابليته للتوسع.*
*This is an architectural audit — not legal advice. All observations concern project structure and scalability.*
