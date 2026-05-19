# datasets/judicial-decisions / قرارات المحاكم السعودية

هذا المجلد يحتوي على فهارس ومراجع للأحكام القضائية السعودية المتاحة للعموم عبر البوابة القانونية لوزارة العدل.

This directory contains indexes and references to Saudi judicial decisions publicly available through the Ministry of Justice Legal Portal.

**المصدر الرسمي / Official Source:** [laws.moj.gov.sa/ar](https://laws.moj.gov.sa/ar)

---

## الهيكل / Structure

```
datasets/judicial-decisions/
├── README.md               # هذا الملف
├── commercial/             # أحكام المحاكم التجارية
├── labor/                  # أحكام المحاكم العمالية
└── civil/                  # أحكام المحاكم العامة (المدنية)
```

---

## معايير الإضافة / Contribution Standards

- المصدر يجب أن يكون `laws.moj.gov.sa` أو مصدر رسمي موثق
- لا يُنسخ نص الحكم كاملاً — يُشار إلى رقم القضية والمحكمة والمبدأ القانوني فقط
- كل ملف يحتوي على حكم واحد أو مجموعة أحكام في نفس المسألة
- يُذكر تاريخ الحكم بالهجري والميلادي

Sources must be `laws.moj.gov.sa` or another verified official source. Do not reproduce full decision text — reference the case number, court, and legal principle only. Each file covers one decision or a set of decisions on the same legal issue. Dates must include both Hijri and Gregorian.

---

## كيف تساهم / How to Contribute

إذا وجدت حكماً قضائياً متاحاً للعموم على البوابة القانونية يتعلق بمسألة قانونية مهمة:

1. افتح Issue بعنوان: `"حكم قضائي: [موضوع الحكم]"`
2. أضف رابط الحكم من `laws.moj.gov.sa`
3. اذكر المبدأ القانوني الذي يرسيه الحكم

If you find a publicly available judicial decision on the Legal Portal that establishes an important legal principle:

1. Open an Issue titled: `"حكم قضائي: [decision topic]"`
2. Add the decision link from `laws.moj.gov.sa`
3. State the legal principle the decision establishes

---

## العلاقة بالطبقات الأخرى / Relationship to Other Layers

| الطبقة | الملف | الصلة |
|--------|-------|-------|
| الفهرس القضائي | `datasets/judicial-index/` | فهرسة مجلدات PDF على مستوى الأقسام |
| استخراج التفكير | `datasets/judicial-reasoning/cases/` | استخراج منظم بـ 19 حقلاً من الأحكام |
| المصادر الأولية (PDF) | `sources/judicial-decisions/` | ملفات PDF الممسوحة (1435هـ) |

---

## إخلاء المسؤولية / Disclaimer

هذه المراجع لأغراض بحثية وتعليمية فقط. لا تمثل استشارة قانونية.

> **تحذير:** هذا تحليل أولي بمساعدة الذكاء الاصطناعي ولا يُعدّ استشارة قانونية. يجب مراجعة مختص قانوني مرخّص في المملكة العربية السعودية قبل اتخاذ أي إجراء.
>
> **Warning:** This is a preliminary AI-assisted analysis and does not constitute legal advice. A licensed legal professional in the Kingdom of Saudi Arabia must be consulted before taking any action.
