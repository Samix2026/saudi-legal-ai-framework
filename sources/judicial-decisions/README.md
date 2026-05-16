# مجموعات الأحكام القضائية السعودية
# Saudi Judicial Decisions Collection

---

## ⚠️ تحذير / Warning

> الأحكام القضائية الواردة في هذا المجلد **مصادر تكميلية** لدراسة أنماط الاستدلال القضائي **فقط**.
> لا تُعدَّل ولا تُفسَّر النصوص التشريعية الرسمية، ولا تُغني عن الرجوع إلى هيئة الخبراء بمجلس الوزراء (boe.gov.sa) أو الجريدة الرسمية (أم القرى) للحصول على النص الرسمي الساري لأي نظام.
>
> Judicial decisions in this directory are **supplementary sources** for studying judicial reasoning patterns **only**.
> They do not amend or interpret official legislative texts and do not replace consulting the Bureau of Experts (boe.gov.sa) or the Official Gazette (Umm Al-Qura) for the authoritative current text of any regulation.

---

## 1. ما هي مجموعات الأحكام القضائية / What Are Judicial Decision Collections

مجموعات الأحكام القضائية هي وثائق تحتوي على نصوص أو ملخصات لأحكام صادرة عن المحاكم السعودية (تجارية، عمالية، مدنية، إدارية). قد تكون:

Judicial decision collections are documents containing texts or summaries of rulings issued by Saudi courts (commercial, labor, civil, administrative). They may be:

| النوع | الوصف |
|-------|-------|
| **أحكام منشورة** | أحكام نُشرت رسميًا أو في مجلات قانونية محكَّمة |
| **ملخصات وصفية** | ملخصات مجمَّعة لأحكام مع إخفاء البيانات المعرِّفة |
| **بيانات إحصائية** | إحصاءات مجمَّعة عن نتائج قضايا دون نص الحكم |
| **مراجع أكاديمية** | تحليلات فقهية وقانونية تستشهد بأحكام موثَّقة |

**هيكل المجلدات / Directory structure:**
المجلدات مرتَّبة بالسنة الهجرية لتسهيل التتبع الزمني للتطور القضائي.
Directories are organized by Hijri year to facilitate tracking judicial evolution over time.

```
sources/judicial-decisions/
├── README.md          ← هذا الملف
├── 1435/              ← أحكام السنة 1435هـ
├── 1436/              ← أحكام السنة 1436هـ
└── ...
```

---

## 2. لماذا هي مهمة للمشروع / Why They Matter to This Project

معظم نماذج الذكاء الاصطناعي تُفسِّر القانون السعودي استنادًا إلى نصوص الأنظمة فقط — دون فهم كيف تُطبِّقها المحاكم فعليًا. الفجوة بين النص والتطبيق مصدر خطأ جوهري في التحليل القانوني بالذكاء الاصطناعي.

Most AI models interpret Saudi law based solely on regulatory texts — without understanding how courts actually apply them. The gap between text and application is a fundamental source of error in AI-driven legal analysis.

الأحكام القضائية تُسهم في سد هذه الفجوة بـ:

Judicial decisions help bridge this gap by:

- **كشف التفسير القضائي الفعلي** للمواد النظامية الغامضة
- **تحديد البنود التعاقدية** التي رفضتها المحاكم أو أقرّتها تاريخيًا
- **بناء توقعات واقعية** حول نتائج النزاعات في سياقات محددة
- **توجيه الذكاء الاصطناعي** نحو لغة قانونية تعكس الممارسة لا النظرية فقط

Revealing the actual judicial interpretation of ambiguous regulatory articles, identifying contractual clauses historically rejected or upheld by courts, building realistic expectations about dispute outcomes in specific contexts, and guiding AI toward legal language that reflects practice not just theory.

---

## 3. المصادر كـ Supplementary Judicial Reasoning Sources

هذه الملفات **مكمِّلة** — لا أساسية. الهرم المرجعي في المشروع:

These files are **supplementary** — not primary. The reference hierarchy in the project:

```
① النصوص الرسمية (boe.gov.sa، uqn.gov.sa)   ← المصدر الأعلى دائمًا
        │
② ملفات sources/ (labor-law.md، pdpl.md...)  ← ملخصات الأنظمة
        │
③ sources/judicial-decisions/                ← أنماط التطبيق القضائي
        │
④ datasets/ و skills/ و prompts/             ← المحتوى التطبيقي
```

لا يُستشهَد بحكم قضائي في هذا المشروع إلا إذا:
A judicial decision is cited in this project only if:

- كان مُنشورًا رسميًا أو موثَّقًا في مصدر أكاديمي معتمد
- تمت إزالة جميع البيانات المعرِّفة (أسماء أطراف، أرقام ملفات)
- خضع لـ verification من مراجع مختص

---

## 4. ليست بديلًا للنصوص النظامية / Not a Replacement for Legislative Texts

| ما تفعله الأحكام | ما لا تفعله |
|-----------------|------------|
| تُفسِّر مادة نظامية في سياق واقعة بعينها | تُعدِّل نص النظام |
| تكشف كيف طبَّقت محكمة بعينها حكمًا ما | تُنشئ سابقة ملزِمة عامة |
| تُضيء الغموض في صياغة نظامية | تحلّ محل النظام |
| تُشير إلى أولويات تطبيقية | تُقرِّر ما هو القانون |

**ملاحظة جوهرية:** النظام القانوني السعودي لا يعتمد مبدأ السابقة القضائية الملزمة (Stare Decisis) بالمفهوم الكومن لوي. كل حكم هو تطبيق لمبادئ الشريعة والأنظمة في واقعة محددة.

**Critical note:** The Saudi legal system does not apply binding precedent (Stare Decisis) in the common law sense. Each ruling is an application of Sharia principles and regulations to a specific set of facts.

---

## 5. متطلبات التحقق / Verification Requirements

أي محتوى مُستخلَص من أحكام قضائية قبل إدراجه في المشروع يجب أن يستوفي:

Any content extracted from judicial decisions before inclusion in the project must satisfy:

| المتطلب | التفصيل |
|---------|---------|
| **`verification_status = draft`** | الحالة الافتراضية لأي استخلاص جديد |
| **إزالة البيانات المعرِّفة** | لا أسماء أطراف، لا أرقام ملفات، لا تفاصيل شخصية |
| **توثيق المصدر** | اسم المحكمة، السنة، نوع القضية — دون بيانات تعريفية |
| **مراجعة مختص** | يجب مراجعة الاستخلاص قبل الترقية إلى `reviewed` |
| **تأكيد محامٍ** | الترقية إلى `verified` تستلزم تأكيدًا مكتوبًا من محامٍ مرخَّص |

راجع [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md) للتفصيل الكامل.

---

## 6. الهدف: دراسة Judicial Reasoning Patterns

الغاية الأساسية من هذه المجموعة هي فهم **كيف تستدلّ المحاكم السعودية** — لا حفظ نصوص الأحكام.

The primary purpose of this collection is to understand **how Saudi courts reason** — not to archive decision texts.

أنماط الاستدلال القضائي المستهدفة:

Targeted judicial reasoning patterns:

- **التحقق من الأركان** — كيف تُثبت المحاكم صحة العقد أو بطلانه
- **تفسير البنود الغامضة** — المنهجية القضائية في ملء الفراغات التعاقدية
- **تقدير التعويض** — الأسس التي تعتمدها المحاكم لحساب التعويض
- **التطبيق التدريجي للأنظمة الجديدة** — كيف تعاملت المحاكم مع الأنظمة حديثة الصدور
- **الموازنة بين النص والعرف التجاري** — متى يأخذ القاضي بالعرف التجاري السعودي

---

## 7. إضافة ملفات / Adding Files

عند إضافة ملف جديد لأي مجلد سنة:

When adding a new file to any year directory:

1. تأكد من إزالة جميع البيانات المعرِّفة
2. أضف في رأس الملف: المحكمة، السنة الهجرية، نوع القضية، نوع المحتوى (نص / ملخص / إحصاء)
3. عيّن `verification_status = draft` في كل صف dataset مرتبط
4. افتح Issue لمناقشة الاستخلاص قبل دمجه في `skills/` أو `datasets/`

Remove all identifying data, add a file header with: court name, Hijri year, case type, content type (text / summary / statistics), assign `verification_status = draft` to all linked dataset rows, and open an Issue to discuss the extraction before merging it into `skills/` or `datasets/`.

---

## الملفات المرتبطة / Related Files

| الملف | العلاقة |
|-------|---------|
| [`sources/regulation-index.md`](../regulation-index.md) | الأنظمة المُطبَّقة في الأحكام — المرجع الأول |
| [`sources/open-data-judicial-sources.md`](../open-data-judicial-sources.md) | مصدر البيانات المفتوحة التكميلي |
| [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md) | معيار `verification_status` |
| [`docs/official-api-sources.md`](../../docs/official-api-sources.md) | التصور المعماري لاستيعاب البيانات مستقبلًا |
| [`datasets/judicial-reasoning/schema.md`](../../datasets/judicial-reasoning/schema.md) | مخطط الاستخراج المنظَّم (19 حقلاً) |
| [`datasets/judicial-reasoning/extraction-guidelines.md`](../../datasets/judicial-reasoning/extraction-guidelines.md) | دليل الاستخراج والإخفاء |
| [`datasets/judicial-reasoning/example-extraction.md`](../../datasets/judicial-reasoning/example-extraction.md) | مثال تعليمي افتراضي |
