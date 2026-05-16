# مخطط بيانات الاستخراج القضائي المنظَّم
# Judicial Reasoning Extraction Schema

**المجلد / Directory:** `datasets/judicial-reasoning/`
**الغرض / Purpose:** استخراج أنماط الاستدلال القضائي من الأحكام السعودية — لا أرشفة النصوص
**Purpose:** Extract judicial reasoning patterns from Saudi decisions — not archive texts
**عدد الحقول / Field count:** 19

---

## ⚠️ تحذير / Warning

> هذا المخطط أداة لدراسة **أنماط الاستدلال** — لا لأرشفة نصوص الأحكام.
> كل صف مستخلَص يبدأ بـ `verification_status = draft` ولا يُستخدم في أي تطبيق قبل المراجعة.
>
> This schema is a tool for studying **reasoning patterns** — not archiving decision texts.
> Every extracted row starts at `verification_status = draft` and must not be used in any application before review.

---

## الحقول / Fields

---

### 1. `case_id`
**النوع / Type:** نص — معرّف فريد (String — unique identifier)
**الوصف / Description:**
معرّف فريد يُنشئه المساهم لهذا الصف — لا علاقة له برقم الملف القضائي الأصلي.
Unique identifier created by the contributor for this row — unrelated to the original case file number.

**الصيغة / Format:** `JD-{سنة هجرية}-{رقم تسلسلي}` — مثال: `JD-1435-001`

| صحيح ✅ | خطأ ❌ |
|--------|-------|
| `JD-1435-001` | رقم الملف القضائي الأصلي |
| `JD-1441-012` | اسم القضية |

---

### 2. `source_pdf`
**النوع / Type:** نص (String)
**الوصف / Description:**
اسم ملف PDF المصدر داخل `sources/judicial-decisions/{سنة}/`.
Name of the source PDF file within `sources/judicial-decisions/{year}/`.

**الصيغة / Format:** `{رقم}.pdf` — مثال: `3.pdf`

---

### 3. `source_page`
**النوع / Type:** عدد صحيح أو نطاق (Integer or range)
**الوصف / Description:**
رقم الصفحة أو نطاق الصفحات التي استُخلص منها هذا الصف.
Page number or range from which this row was extracted.

**الصيغة / Format:** `5` أو `5-8`

---

### 4. `court_type`
**النوع / Type:** نص محدود القيم (Enum)
**الوصف / Description:**
نوع المحكمة التي أصدرت الحكم.
Type of court that issued the ruling.

| القيمة | المعنى |
|--------|-------|
| `commercial` | محكمة تجارية |
| `labor` | محكمة عمالية |
| `administrative` | محكمة إدارية (ديوان المظالم) |
| `civil` | محكمة مدنية عامة |
| `appellate` | محكمة استئناف |
| `supreme` | المحكمة العليا |
| `unknown` | غير محدد في الوثيقة |

---

### 5. `case_domain`
**النوع / Type:** نص محدود القيم (Enum)
**الوصف / Description:**
المجال القانوني الرئيسي للقضية.
Primary legal domain of the case.

**القيم / Values:** `labor` · `commercial` · `civil` · `administrative` · `ip` · `data_protection` · `construction` · `mixed`

---

### 6. `dispute_type`
**النوع / Type:** نص (String)
**الوصف / Description:**
وصف موجز لنوع النزاع — بدون بيانات معرِّفة.
Brief description of the dispute type — without identifying data.

**أمثلة / Examples:**
`إنهاء عقد العمل بدون سبب مشروع` · `نزاع على ملكية فكرية في برنامج مُخصَّص` · `رفض دفع مستحقات مقاول`

---

### 7. `legal_issue`
**النوع / Type:** نص (String)
**الوصف / Description:**
المسألة القانونية الجوهرية التي فصلت فيها المحكمة — مستخلَصة من الحكم لا مُستنتَجة.
The core legal issue the court adjudicated — extracted from the ruling, not inferred.

**ملاحظة / Note:** جملة أو جملتان — تُجيب: "ما السؤال القانوني الذي حسم الحكم؟"
One or two sentences answering: "What legal question did the ruling settle?"

---

### 8. `facts_summary`
**النوع / Type:** نص (String) — مُجرَّد بالكامل
**الوصف / Description:**
ملخص وقائع القضية بعد إزالة جميع البيانات المعرِّفة (أسماء، تواريخ دقيقة، مبالغ محددة).
Summary of case facts after removing all identifying data (names, precise dates, specific amounts).

**القاعدة / Rule:** استبدل الأسماء بـ [الطرف الأول] / [الطرف الثاني] / [صاحب العمل] / [العامل].
Replace names with [Party A] / [Party B] / [Employer] / [Employee].

---

### 9. `claims`
**النوع / Type:** نص (String)
**الوصف / Description:**
ملخص مطالبات المدّعي الرئيسية كما وردت في الحكم — مُجرَّدة.
Summary of the claimant's main claims as stated in the ruling — abstracted.

---

### 10. `defenses`
**النوع / Type:** نص (String)
**الوصف / Description:**
ملخص دفوع المدّعى عليه الرئيسية كما وردت في الحكم — مُجرَّدة.
Summary of the respondent's main defenses as stated in the ruling — abstracted.

---

### 11. `evidence_considered`
**النوع / Type:** نص (String)
**الوصف / Description:**
أنواع الأدلة التي أخذتها المحكمة بعين الاعتبار — لا نصوصها الكاملة.
Types of evidence the court took into account — not their full texts.

**أمثلة / Examples:** `عقد العمل المكتوب` · `شهادة شهود` · `خبرة محاسبية` · `مراسلات إلكترونية`

---

### 12. `applied_regulations`
**النوع / Type:** نص (String) — صيغة الاستشهاد الموحَّدة
**الوصف / Description:**
الأنظمة والمواد التي استند إليها الحكم — بالصيغة الموحَّدة من `regulation-index.md`.
Regulations and articles cited in the ruling — using the standard format from `regulation-index.md`.

**الصيغة / Format:** مثل `related_regulation` في الـ dataset الرئيسي.
**مثال / Example:** `Saudi Labor Law (Royal Decree M/51 1426H) Arts. 80 & 84`

---

### 13. `judicial_reasoning`
**النوع / Type:** نص (String) — الحقل الأهم
**الوصف / Description:**
**الحقل الجوهري.** منهجية استدلال المحكمة: كيف ربطت الوقائع بالنصوص النظامية وتوصّلت للنتيجة.
**The core field.** The court's reasoning methodology: how it linked facts to regulatory texts to reach its conclusion.

**ما يُكتب / What to write:**
- خطوات الاستدلال بالتسلسل
- المبادئ التي طبّقتها المحكمة
- كيف وازنت بين الحجج المتعارضة
- ما رفضته وما قبلته من دفوع

**ما لا يُكتب / What not to write:**
- نسخ نص الحكم حرفيًا
- الاستنتاجات الشخصية للمستخلِص

---

### 14. `legal_principle`
**النوع / Type:** نص (String)
**الوصف / Description:**
المبدأ القانوني المُستخلَص القابل للتعميم — ما يمكن تطبيقه في حالات مماثلة.
The extracted generalizable legal principle — what can be applied in similar cases.

**ملاحظة / Note:** يجب أن يكون مبدأً يُستخلَص من الحكم لا مُستنتَجًا من التفسير الشخصي.
Must be a principle extracted from the ruling, not derived from personal interpretation.

**مثال / Example:** `المحاكم العمالية تُلزم صاحب العمل بإثبات المبرر المشروع للإنهاء — عبء الإثبات يقع عليه لا على العامل`

---

### 15. `outcome`
**النوع / Type:** نص محدود القيم + تفصيل (Enum + detail)
**الوصف / Description:**
نتيجة الحكم ومضمونه الموجز — مُجرَّد من المبالغ الدقيقة والبيانات المعرِّفة.
The ruling's outcome and brief content — abstracted from precise amounts and identifying data.

| القيمة | المعنى |
|--------|-------|
| `claimant_prevailed` | حُكم لصالح المدّعي |
| `respondent_prevailed` | حُكم لصالح المدّعى عليه |
| `partial` | حُكم جزئي لكلا الطرفين |
| `settlement` | انتهت بتسوية |
| `dismissed` | رُدّت الدعوى شكلاً |
| `remanded` | أُحيلت لمحكمة أدنى |

---

### 16. `risk_pattern`
**النوع / Type:** نص (String)
**الوصف / Description:**
نمط المخاطر الذي يُمثّله هذا الحكم لأغراض مراجعة العقود — الربط بالـ dataset الرئيسي.
The risk pattern this ruling represents for contract review purposes — linking to the main dataset.

**مثال / Example:** `بند إنهاء العقد دون سبب مشروع — خطر critical في عقود العمل`

---

### 17. `confidence_level`
**النوع / Type:** نص محدود القيم (Enum)
**الوصف / Description:**
مستوى ثقة المستخلِص في دقة الاستخلاص.
The extractor's confidence level in the accuracy of this extraction.

| القيمة | المعنى |
|--------|-------|
| `high` | النص صريح — الاستخلاص مباشر |
| `medium` | يتطلب تفسيرًا معقولًا للنص |
| `low` | الحكم غامض أو ناقص — يحتاج تحقق إضافي |

---

### 18. `verification_status`
**النوع / Type:** نص محدود القيم (Enum)
**الوصف / Description:**
حالة دورة حياة التحقق القانوني — نفس قيم الـ dataset الرئيسي.
Legal verification lifecycle status — same values as the main dataset.

**القيم / Values:** `draft` · `pending-review` · `reviewed` · `verified` · `deprecated` · `superseded`
**الافتراضي / Default:** `draft` — دائمًا عند الإضافة الأولى

**المرجع / Reference:** [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md)

---

### 19. `notes`
**النوع / Type:** نص (String) — اختياري
**الوصف / Description:**
أي ملاحظات إضافية: غموض في النص، تناقض مع حكم آخر، حاجة لمراجعة متخصصة.
Any additional notes: textual ambiguity, conflict with another ruling, need for specialist review.

**استخدام TO VERIFY:** إذا كان الاستخلاص غير مؤكد في جزء منه، أضف في هذا الحقل: `TO VERIFY — [وصف موجز للجزء غير المؤكد]`

---

## الترتيب الموحَّد للحقول / Standard Field Order

```
case_id, source_pdf, source_page, court_type, case_domain, dispute_type,
legal_issue, facts_summary, claims, defenses, evidence_considered,
applied_regulations, judicial_reasoning, legal_principle, outcome,
risk_pattern, confidence_level, verification_status, notes
```

---

## الملفات المرتبطة / Related Files

| الملف | العلاقة |
|-------|---------|
| [`extraction-guidelines.md`](extraction-guidelines.md) | دليل تطبيق هذا المخطط |
| [`example-extraction.md`](example-extraction.md) | مثال تعليمي افتراضي |
| [`sources/regulation-index.md`](../../sources/regulation-index.md) | صيغ الاستشهاد لـ `applied_regulations` |
| [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md) | تفصيل `verification_status` |
