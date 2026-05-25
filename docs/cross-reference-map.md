# خريطة التقاطعات / Cross-Reference Map

**Saudi Legal AI Framework** — دليل الروابط بين مكونات المشروع

هذه الخريطة تُظهر الروابط بين ملفات المشروع المختلفة. الهدف: أن يعرف أي مساهم بالضبط أين يحتاج أن يُحدِّث عند إضافة مكوّن جديد أو تغيير مكوّن موجود.

This map shows the relationships between project files. The goal: every contributor knows exactly what needs updating when a component is added or changed.

---

## كيف تستخدم هذه الخريطة؟ / How to Use This Map

**سيناريو شائع / Common scenario:**

> "غيّرت هيكل تقرير `skills/contract-review.md` — ماذا أُحدِّث أيضًا؟"
> "I changed the report structure in `skills/contract-review.md` — what else needs updating?"

1. ابحث عن الملف الذي غيّرته في الجداول أدناه.
2. اقرأ عمود **"الملفات المرتبطة"** — كل ملف فيه يحتاج مراجعة.
3. تحقق من أن التغيير منسجم في كل الملفات المرتبطة.

1. Find the file you changed in the tables below.
2. Read the **"Related Files"** column — each listed file needs review.
3. Verify the change is consistent across all related files.

---

## 1. Skills ← → Sources / المهارات ← → المصادر

| Skill | المهارة | Related Sources | ملاحظة |
|---|---|---|---|
| `skills/contract-review.md` | مراجعة العقود | `sources/civil-transactions-law.md` · `sources/labor-law.md` · `sources/companies-law.md` · `sources/pdpl.md` · `sources/commercial-courts.md` | المصدر الرئيسي لهيكل التقرير في §8 |
| `skills/labor-law-analysis.md` | تحليل نظام العمل | `sources/labor-law.md` | نظام العمل م/51 هو المرجع الأساسي |
| `skills/commercial-dispute.md` | النزاعات التجارية | `sources/commercial-courts.md` · `sources/saudi-laws.md` | يتقاطع مع نظام التحكيم م/34 |
| `skills/compliance-check.md` | فحص الامتثال | `sources/pdpl.md` · `sources/labor-law.md` · `sources/companies-law.md` | يغطي 3 أنظمة رئيسية |
| `skills/legal-drafting.md` | الصياغة القانونية | `sources/civil-transactions-law.md` · `sources/saudi-laws.md` | يستند لمبادئ نظام المعاملات المدنية |

---

## 1b. Sources → Skills — Reverse Index / المصادر → المهارات (فهرس عكسي)

> هذا الجدول مصدر الحقيقة للـ CI — يُشغِّل `scripts/validate_cross_refs.py` في كل push.
> أي تغيير في §11 لأي skill يستلزم تحديث هذا الجدول.
> This table is the CI source of truth. Any change to a skill's §11 requires updating it.

| Source File | Cited by Skill | Section | طبيعة الاستخدام |
|---|---|---|---|
| `sources/civil-transactions-law.md` | `skills/labor-law-analysis.md` | §11 | مبادئ العقود التكميلية |
| `sources/civil-transactions-law.md` | `skills/commercial-dispute.md` | §11 | العقود والالتزامات — أساس المطالبات |
| `sources/civil-transactions-law.md` | `skills/compliance-check.md` | §11 | التزامات تعاقدية تنظيمية |
| `sources/civil-transactions-law.md` | `skills/legal-drafting.md` | §11 | الإطار العام للعقود والالتزامات |
| `sources/civil-transactions-law.md` | `skills/arbitration.md` | §11 | مبادئ العقود والالتزامات في النزاعات |
| `sources/civil-transactions-law.md` | `skills/real-estate-contracts.md` | §11 | مبادئ العقود والالتزامات العامة |
| `sources/labor-law.md` | `skills/labor-law-analysis.md` | §11 | الإطار الحاكم الأساسي |
| `sources/labor-law.md` | `skills/compliance-check.md` | §11 | السعودة، WPS، GOSI |
| `sources/labor-law.md` | `skills/legal-drafting.md` | §11 | عقود العمل — أحكام آمرة |
| `sources/companies-law.md` | `skills/commercial-dispute.md` | §11 | نزاعات المساهمين والشركاء |
| `sources/companies-law.md` | `skills/compliance-check.md` | §11 | هيكل الملكية ومتطلبات الإفصاح |
| `sources/companies-law.md` | `skills/legal-drafting.md` | §11 | وثائق الشركات والمساهمين |
| `sources/companies-law.md` | `skills/real-estate-contracts.md` | §11 | عقارات الشركات والتصرف فيها |
| `sources/pdpl.md` | `skills/labor-law-analysis.md` | §11 | بنود السرية في عقود العمل |
| `sources/pdpl.md` | `skills/compliance-check.md` | §11 | PDPL — نقل البيانات والخصوصية |
| `sources/pdpl.md` | `skills/legal-drafting.md` | §11 | بنود السرية ومعالجة البيانات |
| `sources/commercial-courts.md` | `skills/commercial-dispute.md` | §11 | الإطار الإجرائي الأساسي |
| `sources/commercial-courts.md` | `skills/compliance-check.md` | §11 | فض النزاعات التنظيمية |
| `sources/commercial-courts.md` | `skills/arbitration.md` | §11 | الرقابة القضائية على التحكيم وتنفيذ الاحكام |

---

## 2. Skills ← → Prompts / المهارات ← → قوالب المطالبات

| Skill | Related Prompts | طبيعة العلاقة |
|---|---|---|
| `skills/contract-review.md` | `prompts/review-contract.md` | الـ prompt يُطبِّق هيكل §8 من الـ skill — أي تغيير في الهيكل يستلزم تحديث الـ prompt |
| `skills/labor-law-analysis.md` | `prompts/review-contract.md` (قالب عقد العمل) | يستخدم الـ prompt نفسه مع سياق العمل |
| `skills/commercial-dispute.md` | `prompts/risk-analysis.md` | تحليل المخاطر يعتمد على منطق النزاعات التجارية |
| `skills/compliance-check.md` | `prompts/risk-analysis.md` | فحص الامتثال يُخرَج كتقرير مخاطر |
| `skills/legal-drafting.md` | `prompts/draft-notice.md` | صياغة الإشعارات تعتمد مبادئ الـ skill |

---

## 3. Skills ← → Examples / المهارات ← → الأمثلة التطبيقية

| Skill | Related Examples | ملاحظة |
|---|---|---|
| `skills/arbitration.md` | `examples/arbitration-example.md` | نزاع توريد عابر للحدود |
| `skills/commercial-dispute.md` | `examples/commercial-dispute-example.md` | تحليل نزاع تجاري |
| `skills/compliance-check.md` | `examples/compliance-example.md` · `examples/pdpl-data-breach-example.md` | فحص امتثال SaaS + اختراق بيانات طبية |
| `skills/contract-review.md` | `examples/contract-review-example.md` · `examples/employment-contract-review.md` · `examples/nda-review.md` · `examples/saudi-contract-review-demo.md` | الـ demo هو التطبيق الكامل لـ §8 |
| `skills/labor-law-analysis.md` | `examples/employment-contract-review.md` · `examples/labor-dispute-job-change-example.md` · `examples/labor-law-example.md` | يتضمن حساب EOSB ونزاع تغيير المسمى |
| `skills/legal-drafting.md` | `examples/legal-drafting-example.md` | صياغة عقد خدمات برمجيات |
| `skills/real-estate-contracts.md` | `examples/commercial-lease-exit-example.md` · `examples/real-estate-example.md` | إيجار تجاري + سكني |

---

## Skill → Example Coverage

> هذا الجدول مُولَّد من `## Related examples` في كل ملف `skills/*.md`.
> يُشغَّل `scripts/validate_example_coverage.py` في كل push للتحقق منه.
> This table is derived from `## Related examples` in each `skills/*.md` file.
> `scripts/validate_example_coverage.py` runs on every push to verify it.

| Skill | Example Count | Example Files | Coverage Status |
|---|---|---|---|
| `skills/arbitration.md` | 1 | `examples/arbitration-example.md` | Partial |
| `skills/commercial-dispute.md` | 1 | `examples/commercial-dispute-example.md` | Partial |
| `skills/compliance-check.md` | 2 | `examples/compliance-example.md` · `examples/pdpl-data-breach-example.md` | Strong |
| `skills/contract-review.md` | 4 | `examples/contract-review-example.md` · `examples/employment-contract-review.md` · `examples/nda-review.md` · `examples/saudi-contract-review-demo.md` | Strong |
| `skills/labor-law-analysis.md` | 3 | `examples/employment-contract-review.md` · `examples/labor-dispute-job-change-example.md` · `examples/labor-law-example.md` · | Strong |
| `skills/legal-drafting.md` | 1 | `examples/legal-drafting-example.md` | Partial |
| `skills/real-estate-contracts.md` | 2 | `examples/commercial-lease-exit-example.md` · `examples/real-estate-example.md` | Strong |

**Coverage rules:** 0 examples → Missing | 1 example → Partial | 2+ examples → Strong

---

## Skill Relationship Graph

> هذا الجدول مُولَّد من `## Related skills` في كل ملف `skills/*.md`.
> يُشغَّل `scripts/validate_skill_graph.py` في كل push للتحقق منه.
> This table is derived from `## Related skills` in each `skills/*.md` file.
> `scripts/validate_skill_graph.py` runs on every push to verify it.

| Skill | Related Skills | Relationship Types | Graph Degree | Connectivity Status |
|---|---|---|---|---|
| `skills/arbitration.md` | `skills/commercial-dispute.md` · `skills/legal-drafting.md` | `alternative_to` · `depends_on` | 4 (2 out, 2 in) | Connected |
| `skills/commercial-dispute.md` | `skills/arbitration.md` · `skills/legal-drafting.md` | `alternative_to` · `precedes` | 4 (2 out, 2 in) | Connected |
| `skills/compliance-check.md` | `skills/labor-law-analysis.md` · `skills/contract-review.md` | `cross_checks` | 5 (2 out, 3 in) | Connected |
| `skills/contract-review.md` | `skills/commercial-dispute.md` · `skills/arbitration.md` · `skills/legal-drafting.md` · `skills/compliance-check.md` | `escalates_to` · `precedes` · `cross_checks` | 8 (4 out, 4 in) | Connected |
| `skills/labor-law-analysis.md` | `skills/compliance-check.md` · `skills/contract-review.md` | `cross_checks` · `depends_on` | 3 (2 out, 1 in) | Connected |
| `skills/legal-drafting.md` | `skills/contract-review.md` | `depends_on` | 4 (1 out, 3 in) | Connected |
| `skills/real-estate-contracts.md` | `skills/contract-review.md` · `skills/compliance-check.md` | `specializes` · `depends_on` | 2 (2 out, 0 in) | Connected |

**Allowed relationship types:** `escalates_to` · `alternative_to` · `cross_checks` · `depends_on` · `specializes` · `precedes` · `shares_sources_with` · `overlaps_with`

---

## 4. Sources ← → Regulations / المصادر ← → الأنظمة

| Source File | Regulation | Royal Decree | صيغة الاستشهاد الرسمية |
|---|---|---|---|
| `sources/civil-transactions-law.md` | نظام المعاملات المدنية | م/191 1443هـ | `Saudi Civil Transactions Law (Royal Decree M/191 1443H)` |
| `sources/labor-law.md` | نظام العمل | م/51 1426هـ | `Saudi Labor Law (Royal Decree M/51 1426H)` |
| `sources/companies-law.md` | نظام الشركات | م/132 1443هـ | `Saudi Companies Law (Royal Decree M/132 1443H)` |
| `sources/commercial-courts.md` | نظام المحاكم التجارية | م/93 1441هـ | `Commercial Courts Law (Royal Decree M/93 1441H)` |
| `sources/pdpl.md` | نظام حماية البيانات الشخصية | م/19 1443هـ | `Personal Data Protection Law PDPL (Royal Decree M/19 1443H)` |
| `sources/saudi-laws.md` | نظرة عامة (جميع الأنظمة) | — | مرجع عام — يُشير لـ `regulation-index.md` |
| `sources/regulation-index.md` | **جميع الأنظمة العشرة** | متعددة | **المصدر الرسمي الوحيد لصيغ الاستشهاد** |

> الأنظمة المسجَّلة في `regulation-index.md` لكن **بدون** ملف `sources/` مخصص بعد:
> - Saudi Arbitration Law (م/34 1433H)
> - Commercial Agency Law (م/11 1382H)
> - Intellectual Property Protection Law (م/41 1424H)
> - Saudi Bankruptcy Law (م/50 1439H)
> - Electronic Transactions Law (م/18 1428H)

---

## 5. Judicial Corpus ← → Indexing ← → Extraction / المجموعة القضائية ← → الفهرسة ← → الاستخراج

هذه الطبقات الثلاث تعمل بتسلسل صارم — لا يبدأ الاستخراج قبل اكتمال الفهرسة.

These three layers work in strict sequence — extraction does not begin before indexing is complete.

| Layer | Directory | Related Files | ملاحظة |
|-------|-----------|---------------|--------|
| **Judicial Corpus** | `sources/judicial-decisions/1435/` | `sources/judicial-decisions/README.md` | 14 ملف PDF مسحوب ضوئيًا — لا يمكن استخراج نصها آليًا |
| **Corpus Index** | `datasets/judicial-index/` | `datasets/judicial-index/schema.md` · `judicial-corpus-index.csv` · `README.md` | الفهرسة اليدوية لأقسام الـ PDF — مدخل الاستخراج |
| **Judicial Extraction** | `datasets/judicial-reasoning/` | `datasets/judicial-reasoning/schema.md` · `example-extraction.md` · `extraction-guidelines.md` | 19 حقلًا — يبدأ بعد اكتمال الفهرسة |

### تبعيات الطبقات / Layer Dependencies

```
sources/judicial-decisions/1435/*.pdf
        │
        ▼  (فهرسة يدوية — read PDF table of contents)
datasets/judicial-index/judicial-corpus-index.csv
        │
        ▼  (اختيار الأقسام ذات extraction_priority = high/medium)
        │
        ▼  (استخراج يدوي — requires human reading of PDF pages)
datasets/judicial-reasoning/{extraction files}
        │
        ▼  (تحقق — reviewed → verified)
skills/ و datasets/ الرئيسية
```

> **ملاحظة OCR / OCR Note:** ملفات الـ PDF مسحوبة ضوئيًا (scanned images) — استخراج النص الآلي غير ممكن بالأدوات الحالية. طبقة OCR مخططة في المستقبل. الاستخراج الحالي يدوي بالكامل.

### عند إضافة قسم جديد للفهرس / When Adding a New Index Section

```
✅ أضف صفًا في:              datasets/judicial-index/judicial-corpus-index.csv
✅ اتبع هيكل الـ index_id:  IDX-{year}-{vol}-{seq}
✅ اقرأ start_page/end_page: من فهرس الـ PDF يدويًا — ضع 0 إذا لم تتحقق
✅ أضف TO VERIFY:            لأي حقل غير مؤكد
✅ لا تضع reasoning هنا:    الاستخراج يتم في datasets/judicial-reasoning/ فقط
```

### عند إضافة استخراج قضائي / When Adding a Judicial Extraction

```
✅ تأكد من وجود صف في الفهرس أولًا:   datasets/judicial-index/judicial-corpus-index.csv
✅ اتبع المخطط:                        datasets/judicial-reasoning/schema.md (19 حقلًا)
✅ اقرأ دليل الاستخراج:                datasets/judicial-reasoning/extraction-guidelines.md
✅ أخفِ جميع البيانات الشخصية:         [صاحب العمل] · [العامل] · [المحكمة X] بدلًا من الأسماء الحقيقية
✅ أضف verification_status = draft:    دائمًا عند الإنشاء
✅ لا تستخرج من حكم غير قابل للقراءة: توقف وأضف ملاحظة في الفهرس
✅ إذا ظهر مرجع فقهي:                 سجّله في sources/fiqh-judicial-references/citation-index.md
```

---

## 5.5 Fiqh References ← → Judicial Reasoning / المراجع الفقهية ← → الاستخراج القضائي

طبقة المراجع الفقهية مساعدة — تُقرَأ أثناء الاستخراج ولا تسبقه ولا تلزمه.

The fiqh reference layer is supplementary — it is consulted during extraction and does not block or precede it.

| From | To | طبيعة العلاقة |
|------|----|---------------|
| `sources/fiqh-judicial-references/citation-index.md` | `datasets/judicial-reasoning/cases/*.md` | كل سجل في الفهرس مرتبط بـ `case_id` — الاستخراج هو المصدر الأساسي |
| `citation-index.md` → حقل `topic` | `judicial_reasoning` + `legal_principle` في ملفات الاستخراج | الموضوع الفقهي يُساعد على تفسير المبادئ المستخلصة |
| `sources/fiqh-judicial-references/usage-guidelines.md` | جميع ملفات `datasets/judicial-reasoning/cases/` | يحكم كيفية توثيق الإحالات الفقهية ومنع الـ hallucination |
| `sources/fiqh-judicial-references/README.md` | `sources/regulation-index.md` | الملفان مستقلان — المراجع الفقهية ليست أنظمة رسمية |

### عند إضافة مرجع فقهي جديد / When Adding a Fiqh Citation

```
✅ تحقق أن المرجع ظهر صراحةً في حكم قضائي في cases/
✅ أضف سجلاً في:     sources/fiqh-judicial-references/citation-index.md
✅ اربط الـ case_id:  related_case_id = JD-{سنة}-{NNN}
✅ استخدم:           verification_status: draft لأي رقم صفحة من OCR
✅ لا تضفه لـ:        sources/regulation-index.md — المراجع الفقهية ليست أنظمة رسمية
```

### تبعية الفقه القضائي / Fiqh Layer Dependencies

```
datasets/judicial-reasoning/cases/*.md   ← المصدر الأساسي دائماً
        │
        │  (إذا ظهر مرجع فقهي في applied_regulations أو judicial_reasoning)
        ▼
sources/fiqh-judicial-references/citation-index.md
        │
        │  (بعد تحقق بشري من المطبوع)
        ▼
verification_status: draft → community-reviewed
```

---

## 6. Contract Datasets ← → Enums / قواعد البيانات ← → القيم المضبوطة

| Dataset / Column | Enum File | القيم المقبولة |
|---|---|---|
| `*` → `risk_level` | `datasets/enums/risk-levels.md` | `critical` · `high` · `medium` · `low` |
| `*` → `contract_type` | `datasets/enums/contract-types.md` | 11 نوعًا — راجع الملف |
| `*` → `clause_category` | `datasets/enums/clause-categories.md` | 14 فئة — راجع الملف |
| `*` → `industry` | `datasets/enums/industries.md` | 12 قطاعًا — راجع الملف |

**ينطبق على جميع ملفات CSV / Applies to all CSV files:**
- `datasets/saudi-contract-risk-dataset.csv`
- `datasets/examples/*.csv`
- `datasets/contributions/**/*.csv`
- `datasets/build/*.generated.csv`

---

## 7. Contract Datasets ← → Scripts / قواعد البيانات ← → السكربتات

| File / Path | Script | الدور |
|---|---|---|
| `datasets/saudi-contract-risk-dataset.csv` | `scripts/validate_dataset.py` | التحقق من صحة الـ master dataset |
| `datasets/examples/*.csv` | `scripts/validate_dataset.py` | التحقق من الأمثلة |
| `datasets/contributions/**/*.csv` | `scripts/validate_dataset.py` | يُشغَّل قبل كل PR |
| `datasets/contributions/**/*.csv` | `scripts/build_dataset.py` | المدخل — يُدمج المساهمات |
| `datasets/build/*.generated.csv` | `scripts/build_dataset.py` | المخرج — يُولِّد هذا الملف |
| `datasets/build/*.generated.csv` | `scripts/validate_dataset.py` | التحقق من الملف المُولَّد بعد البناء |
| `datasets/enums/*.md` + `datasets/schema.md` | `scripts/validate_dataset.py` | المصادر التوثيقية للـ enums — أي تغيير يستلزم تحديث الثوابت في السكربت |

---

## 8. Workflows ← → GitHub Actions / سير العمل ← → الإجراءات الآلية

| Workflow File | Trigger | ما الذي يُشغَّل | الملفات المرتبطة |
|---|---|---|---|
| `.github/workflows/validate-datasets.yml` | `push` · `pull_request` | `scripts/validate_dataset.py` على master + examples | `datasets/saudi-contract-risk-dataset.csv` · `datasets/examples/*.csv` |
| `.github/workflows/auto-label.yml` | `pull_request` (opened/sync/reopened) | `actions/labeler@v5` | `.github/labeler.yml` |

**ملاحظة:** `validate-datasets.yml` **لا** يشغّل الـ validation على `datasets/contributions/` تلقائيًا. المساهمون يُشغّلون الـ validation يدويًا قبل فتح الـ PR.

---

## 9. قواعد الصيانة / Maintenance Rules

> كل تغيير في ملف رئيسي يستلزم تحديث الخريطة وتحديث الملفات المرتبطة به.

Every change to a core file requires updating this map and the files linked to it.

---

### عند إضافة Skill جديد / When Adding a New Skill

```
✅ أضف الـ skill في:             skills/<domain>.md
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جداول 1 و 2 و 3)
✅ افتح Issue لإضافة مصدر:       sources/<regulation>.md (إذا لم يكن موجودًا)
✅ افتح Issue لإضافة prompt:     prompts/<task>.md (إذا لم يكن موجودًا)
✅ افتح Issue لإضافة مثال:       examples/<scenario>.md
✅ تحقق من regulation-index.md:  هل الأنظمة المرتبطة مسجَّلة؟
```

---

### عند إضافة Source جديد / When Adding a New Source

```
✅ أضف الـ source في:            sources/<regulation>.md
✅ سجّل في الـ registry:         sources/regulation-index.md (إلزامي)
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جدول 4)
✅ حدّث الـ skills المرتبطة:     أضف إشارة للـ source في الـ skill المناسب
✅ حدّث CONTRIBUTING.md:         إذا كان النظام الجديد يؤثر على معايير الاستشهاد
```

---

### عند تعديل §11 في Skill / When Editing a Skill's §11

```
✅ حدّث Section 1b في:           docs/cross-reference-map.md
✅ حدّث "See also" في:           كل sources/ file أُضيف أو حُذف من §11
✅ شغّل محليًا:                  python scripts/validate_cross_refs.py
✅ تأكد من خروج 0 قبل الـ commit
```

---

### عند إضافة Enum جديد / When Adding a New Enum Value

```
✅ حدّث ملف الـ enum:            datasets/enums/<type>.md
✅ حدّث validate_dataset.py:     أضف القيمة الجديدة للثابت المناسب (VALID_*)
✅ حدّث datasets/schema.md:      اذكر القيمة الجديدة في وصف العمود
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جدول 5)
```

---

### عند إضافة نوع عقد / When Adding a New Contract Type

```
✅ حدّث:  datasets/enums/contract-types.md
✅ حدّث:  scripts/validate_dataset.py → VALID_CONTRACT_TYPES
✅ حدّث:  datasets/schema.md
✅ أنشئ مجلد مساهمة (إن لزم): datasets/contributions/<domain>/
✅ حدّث هذه الخريطة:  docs/cross-reference-map.md (جداول 5 و 6)
```

---

### عند تغيير Output Format / When Changing the Output Format

هذا التغيير الأكثر تأثيرًا — يجب تحديث سلسلة كاملة:

This is the highest-impact change — requires updating a full chain:

```
skills/<domain>.md §8 (أو القسم المعني بالهيكل)
    ↓  يُعدَّل أولًا — المصدر الأساسي
prompts/<related>.md
    ↓  يُعدَّل ثانيًا — يعكس الهيكل الجديد
examples/<related>.md
    ↓  يُعدَّل ثالثًا — يُطبِّق الهيكل الجديد
docs/cross-reference-map.md
    ↓  يُحدَّث أخيرًا
```

> لا تُغيِّر الـ prompt أو الـ example دون أن تُغيِّر الـ skill أولًا.
> Never change the prompt or example without first changing the skill.

---

### عند إضافة GitHub Workflow جديد / When Adding a New GitHub Workflow

```
✅ أضف الـ workflow في:          .github/workflows/<name>.yml
✅ حدّث .github/labeler.yml:    إذا كان يتعامل مع مسارات ملفات جديدة
✅ حدّث هذه الخريطة:            docs/cross-reference-map.md (جدول 7)
✅ حدّث README.md إذا لزم:      أضف badge أو ذكر للـ workflow
```

---

## ملخص التبعيات الحرجة / Critical Dependency Summary

```
regulation-index.md  ←── مرجع لـ ── sources/*.md ←── مرجع لـ ── skills/*.md
                                                                      ↓
                                                              prompts/*.md
                                                                      ↓
                                                              examples/*.md

datasets/enums/*.md  ←── يُحكم ──── validate_dataset.py ←── يُشغَّل بواسطة ── CI workflow
datasets/schema.md   ←── يوثّق ──── datasets/**/*.csv

sources/judicial-decisions/*.pdf  ──▶  judicial-index/judicial-corpus-index.csv
                                                  │
                                                  ▼  (بعد اكتمال الفهرسة)
                                   datasets/judicial-reasoning/cases/{extractions}
                                                  │        │
                                                  │        ▼  (إذا ظهر مرجع فقهي)
                                                  │  sources/fiqh-judicial-references/
                                                  │  citation-index.md  [draft حتى تحقق]
                                                  │
                                                  ▼  (بعد التحقق)
                                         skills/ و datasets/ الرئيسية

sources/fiqh-judicial-references/  ≠  sources/regulation-index.md
    (مراجع مساعدة — لا تشريعية)           (أنظمة رسمية — المصدر الأساسي دائماً)
```

---

*آخر تحديث / Last updated: 2026-05-25 — إضافة § Skill → Example Coverage + تحديث §3 + validate_example_coverage.py*

*حدّث هذا التاريخ عند كل مراجعة للخريطة. / Update this date on every map revision.*
