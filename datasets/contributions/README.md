# مجلد المساهمات / Contributions Directory

هذا المجلد يستقبل ملفات CSV المُساهَم بها من المجتمع. كل ملف يمثّل مساهمة مستقلة قبل دمجها في قاعدة البيانات الرسمية عبر سكربت البناء.

This directory receives community-contributed CSV files. Each file represents an independent contribution before being merged into the official dataset via the build script.

---

## لماذا ملف واحد لكل مساهمة؟ / Why One File Per Contribution?

**المشكلة مع ملف مركزي واحد:**
- كل مساهمَين يعدّلان نفس الملف → تعارضات Git يصعب حلّها
- يستحيل مراجعة مساهمة واحدة بمعزل عن غيرها
- تراكم الأخطاء وصعوبة تتبع مصدر كل صف

**مزايا هيكل one file per contribution:**
- كل Pull Request يُضيف ملفًا جديدًا فقط — لا تعارضات تقريبًا
- المراجع يرى بوضوح ما أضافه المساهم تحديدًا
- يمكن قبول مساهمة أو رفضها أو تعديلها دون التأثير على الباقي
- سهولة التتبع: من أضاف أي صف ولماذا

**The problem with a single central file:**
- Two contributors editing the same file → hard-to-resolve Git conflicts
- Impossible to review one contribution in isolation
- Errors accumulate and source tracing becomes difficult

**Advantages of one-file-per-contribution:**
- Each Pull Request adds only a new file — almost zero conflicts
- Reviewers see exactly what each contributor added
- A contribution can be accepted, rejected, or revised without affecting others
- Full traceability: who added what and why

---

## هيكل المجلدات / Directory Structure

```
datasets/contributions/
├── employment/       # عقود العمل / Employment contracts
├── saas/             # اتفاقيات SaaS والبرمجيات / SaaS and software agreements
├── construction/     # عقود الإنشاء والمقاولات / Construction contracts
├── commercial/       # العقود التجارية العامة / General commercial contracts
├── pdpl/             # بنود حماية البيانات / Data protection clauses
└── general/          # بنود متعددة الفئات / Multi-category clauses
```

اختر المجلد الذي يتطابق مع نوع العقد الغالب في ملفك. إذا كانت الصفوف تغطي أنواعًا متعددة، استخدم `general/`.

Choose the folder that matches the dominant contract type in your file. If rows cover multiple types, use `general/`.

---

## كيف تُضيف مساهمة جديدة؟ / How to Add a Contribution

```bash
# 1. Fork المستودع وأنشئ branch جديد
git checkout -b add-saas-liability-clauses

# 2. أنشئ ملف CSV جديد في المجلد المناسب
# Create a new CSV in the appropriate folder
# انسخ الـ header من أحد ملفات datasets/examples/ كنقطة بداية
# Copy the header from any file in datasets/examples/ as a starting point

# 3. تحقق من صحة ملفك قبل الإرسال
python3 scripts/validate_dataset.py --file datasets/contributions/saas/your-file.csv

# 4. افتح Pull Request — استخدم قالب dataset-contribution
```

**قواعد أساسية / Core rules:**
- لا تُعدّل ملفات موجودة — أضف ملفًا جديدًا فقط
- لا تُضف أكثر من 20 صفًا في مساهمة واحدة (أبقِ المراجعة قابلة للإدارة)
- تأكد أن الملف يجتاز الـ validation قبل فتح الـ PR
- Do not edit existing files — add a new file only
- Keep contributions to ≤ 20 rows (keep reviews manageable)
- Ensure the file passes validation before opening a PR

---

## اصطلاح التسمية / Naming Convention

```
<domain>/<descriptive-slug>.csv
```

| صحيح / Correct | خاطئ / Incorrect |
|---|---|
| `saas/pdpl-data-transfer-clauses.csv` | `saas/my_file.csv` |
| `employment/probation-period-risks.csv` | `employment/new 1.csv` |
| `construction/force-majeure-clauses.csv` | `construction/ForceMajeure.csv` |
| `general/arbitration-clause-patterns.csv` | `general/dataset.csv` |

**القواعد / Rules:**
- أحرف صغيرة فقط / Lowercase only
- فصل الكلمات بـ `-` / Hyphen-separated words
- اسم وصفي يعكس محتوى الملف / Descriptive name reflecting file content
- لا مسافات أو أحرف خاصة / No spaces or special characters

---

## IDs في ملفات المساهمة / IDs in Contribution Files

IDs في ملفات المساهمة هي **محلية** — لا تمثّل الـ ID النهائي في قاعدة البيانات.

سكربت البناء (`build_dataset.py`) يُعيد تعيين IDs تسلسلية في الملف المُولَّد. لذلك:
- يمكنك البدء من 1 في كل ملف مساهمة
- لا حاجة للتنسيق مع مساهمين آخرين بشأن الأرقام
- المهم هو التفرّد داخل ملفك فقط

IDs in contribution files are **local** — they do not represent the final ID in the dataset.

The build script (`build_dataset.py`) reassigns sequential IDs in the generated output. Therefore:
- You can start from 1 in every contribution file
- No need to coordinate with other contributors on ID numbers
- Uniqueness within your own file is what matters

---

## متى تُدمَج البيانات؟ / When Is Data Merged into the Master Dataset?

البناء **لا يعدّل** `datasets/saudi-contract-risk-dataset.csv` — هذا الملف الأساسي يُحدَّث يدويًا فقط من قِبَل المشرفين بعد مراجعة متأنية.

The build **does not modify** `datasets/saudi-contract-risk-dataset.csv` — this master file is updated manually by maintainers only after careful review.

**دورة حياة المساهمة / Contribution lifecycle:**

```
مساهمة → validate → PR → مراجعة قانونية → قبول → build → ترقية للـ master
Contribution → validate → PR → legal review → approval → build → promote to master
```

يُولَّد `datasets/build/saudi-contract-risk-dataset.generated.csv` لأغراض الاختبار فقط ولا يُرفع للـ repo (مُدرَج في .gitignore).

`datasets/build/saudi-contract-risk-dataset.generated.csv` is generated for testing only and is not committed to the repo (listed in .gitignore).

---

## كيف تُشغّل الـ Validation والبناء / How to Run Validation and Build

```bash
# تحقق من ملف مساهمتك / Validate your contribution file
python3 scripts/validate_dataset.py --file datasets/contributions/saas/your-file.csv

# ابنِ قاعدة البيانات المدمجة / Build the merged dataset
python3 scripts/build_dataset.py

# تحقق من الملف المُولَّد / Validate the generated file
python3 scripts/validate_dataset.py --file datasets/build/saudi-contract-risk-dataset.generated.csv

# تحقق من ملفات examples/ / Validate examples
for f in datasets/examples/*.csv; do
  python3 scripts/validate_dataset.py --file "$f"
done
```

---

## الملف المرجعي / Reference

راجع هذه الملفات قبل كتابة مساهمتك / Review these before writing your contribution:

| الملف / File | الغرض / Purpose |
|---|---|
| [`datasets/schema.md`](../schema.md) | الـ schema الكامل بجميع الأعمدة |
| [`datasets/enums/risk-levels.md`](../enums/risk-levels.md) | قيم `risk_level` المقبولة |
| [`datasets/enums/contract-types.md`](../enums/contract-types.md) | قيم `contract_type` المقبولة |
| [`datasets/enums/clause-categories.md`](../enums/clause-categories.md) | قيم `clause_category` المقبولة |
| [`datasets/enums/industries.md`](../enums/industries.md) | قيم `industry` المقبولة |
| [`datasets/examples/saas-agreements.csv`](../examples/saas-agreements.csv) | مثال تطبيقي كامل |
| [`sources/regulation-index.md`](../../sources/regulation-index.md) | صيغ الاستشهاد بالأنظمة السعودية |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md) | دليل المساهمة الشامل |
