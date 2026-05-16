# دليل الاستخراج القضائي المنظَّم
# Structured Judicial Extraction Guidelines

**ينطبق على / Applies to:** جميع ملفات `datasets/judicial-reasoning/`
**يُكمِّل / Complements:** [`schema.md`](schema.md) · [`example-extraction.md`](example-extraction.md)

---

## ⚠️ تحذير أساسي / Fundamental Warning

> الهدف من الاستخراج هو **فهم كيف تستدلّ المحاكم** — لا نسخ نصوص الأحكام ولا بناء قاعدة بيانات قانونية.
> كل صف يبدأ بـ `verification_status = draft` ولا يُستخدم في أي سياق قبل المراجعة.
>
> The goal of extraction is to **understand how courts reason** — not to copy decision texts or build a legal database.
> Every row starts at `verification_status = draft` and must not be used in any context before review.

---

## 1. كيف نستخرج Reasoning من حكم / How to Extract Reasoning

الاستخراج الجيد يمر بأربع مراحل:

Good extraction follows four stages:

### المرحلة 1: القراءة الكاملة أولاً
اقرأ الحكم من البداية للنهاية قبل الكتابة. لا تبدأ الاستخراج من أول صفحة — الحكم بنية متكاملة.

Read the ruling from start to finish before writing. Do not begin extraction from page one — a ruling is an integrated structure.

### المرحلة 2: تحديد العناصر الأربعة
ابحث في النص عن:

| العنصر | السؤال المرشد |
|--------|--------------|
| **المسألة القانونية** | ما الخلاف الجوهري الذي حسم الحكم؟ |
| **الوقائع الجوهرية** | ما الأحداث التي اعتمدتها المحكمة لا ما ادّعاه الأطراف؟ |
| **منهجية الاستدلال** | كيف ربطت المحكمة الوقائع بالنصوص النظامية؟ |
| **المبدأ القابل للتعميم** | ما الذي تقوله هذه القضية لحالة مشابهة؟ |

### المرحلة 3: الكتابة بلغتك أنت
لا تنسخ نص الحكم. اكتب بلغتك الخاصة ما فهمته من استدلال المحكمة. إذا لم تستطع إعادة الصياغة بلغتك، فأنت لم تفهم الاستدلال بعد.

Do not copy the ruling text. Write in your own words what you understood of the court's reasoning. If you cannot rephrase it in your own words, you have not understood the reasoning yet.

### المرحلة 4: التحقق الذاتي
قبل الحفظ اسأل نفسك:
- هل يمكن تطبيق `legal_principle` على قضية مماثلة لم تحدث بعد؟
- هل أزلت كل البيانات المعرِّفة؟
- هل `judicial_reasoning` يصف منهجية المحكمة لا رأيك أنت؟

---

## 2. الفرق بين Facts و Reasoning و Outcome

هذا التمييز أساسي — الخلط بينها يُفسد الاستخراج كاملاً.

This distinction is fundamental — confusing them invalidates the extraction entirely.

### Facts — الوقائع

**ما هي:** الأحداث التي حدثت فعلاً وأثبتتها المحكمة.
**What they are:** Events that actually occurred and were established by the court.

**السؤال المرشد:** "ماذا حدث؟"

**أمثلة:**
- ✅ `أبرم [الطرف الأول] عقد عمل مع [الطرف الثاني] لمدة غير محددة`
- ✅ `أنهى [صاحب العمل] العقد فورًا دون إشعار مسبق موثق`
- ❌ `[صاحب العمل] تصرف بسوء نية` — هذا تقييم، ليس واقعة

### Reasoning — الاستدلال

**ما هو:** منهجية المحكمة في الربط بين الوقائع والنصوص للوصول للنتيجة.
**What it is:** The court's methodology in linking facts to texts to reach a conclusion.

**السؤال المرشد:** "كيف توصّلت المحكمة للنتيجة؟"

**أمثلة:**
- ✅ `رأت المحكمة أن عبء إثبات المبرر يقع على صاحب العمل استناداً للمادة 80 — إذ لم يُقدِّم توثيقًا، سقط دفعه`
- ❌ `الحكم صحيح لأن القانون واضح` — هذا رأي المستخلِص، ليس استدلال المحكمة

### Outcome — النتيجة

**ما هي:** منطوق الحكم — ماذا قضت المحكمة؟
**What it is:** The ruling's operative part — what did the court decide?

**السؤال المرشد:** "ماذا أصدرت المحكمة؟"

**أمثلة:**
- ✅ `حُكم لصالح [العامل] بمكافأة نهاية الخدمة كاملة`
- ❌ `انتصر العامل` — غير دقيق، لا يصف المنطوق

### جدول المقارنة / Comparison Table

| العنصر | السؤال | يُكتب في حقل |
|--------|--------|-------------|
| Facts | ماذا حدث؟ | `facts_summary` |
| Claims / Defenses | ماذا ادّعى كل طرف؟ | `claims` · `defenses` |
| Evidence | ما الذي نظرت إليه المحكمة؟ | `evidence_considered` |
| Reasoning | كيف استدلّت المحكمة؟ | `judicial_reasoning` |
| Principle | ما المبدأ العام؟ | `legal_principle` |
| Outcome | ماذا قضت؟ | `outcome` |

---

## 3. كيف نتعامل مع أسماء الأطراف / Handling Party Names

**القاعدة الصارمة:** لا يُذكر اسم أي طرف طبيعي أو اعتباري في أي حقل.
**Strict rule:** No natural or legal person's name may appear in any field.

### جدول الاستبدال / Replacement Table

| بدلاً من | استخدم |
|---------|--------|
| اسم صاحب العمل | `[صاحب العمل]` أو `[الطرف الأول]` |
| اسم العامل | `[العامل]` أو `[الطرف الثاني]` |
| اسم الشركة المدّعية | `[الشركة المدّعية]` |
| اسم الشركة المدّعى عليها | `[الشركة المدّعى عليها]` |
| اسم المقاول | `[المقاول]` |
| اسم الجهة الحكومية | `[الجهة الحكومية]` |
| اسم الشاهد | `[الشاهد]` أو `[المشرف]` |

### بيانات أخرى تُحذف / Other Data to Remove

| البيانات | القاعدة |
|---------|---------|
| رقم الملف القضائي | يُحذف كاملاً |
| تاريخ الحكم الدقيق | يُستبدل بالسنة الهجرية فقط: `1435هـ` |
| المبالغ الدقيقة | يُستبدل بوصف نسبي: `مبلغ يمثّل أجر سنتين` |
| أسماء الأماكن | يُستبدل بـ `[المدينة]` إذا كانت مُعرِّفة |
| أسماء المحامين | تُحذف كاملاً |

---

## 4. كيف نُخفي البيانات / How to Redact Data

### مبدأ الإخفاء / Redaction Principle

الإخفاء الجيد يحافظ على **معنى الواقعة** مع حذف **هوية أصحابها**.
Good redaction preserves the **meaning of the fact** while removing **the identities of those involved**.

### اختبار الإخفاء / Redaction Test

بعد الاستخراج، اسأل: هل يستطيع شخص يقرأ هذا الصف تحديد القضية الأصلية أو أطرافها؟
After extraction, ask: Can someone reading this row identify the original case or its parties?

- إذا كانت الإجابة **نعم** → الإخفاء غير كافٍ، أعد المراجعة
- إذا كانت الإجابة **لا** → الإخفاء مقبول

### مستويات الحساسية / Sensitivity Levels

| المستوى | أمثلة | الإجراء |
|---------|--------|---------|
| **عالي** | قضايا تتعلق بأفراد، عمال، بيانات شخصية | لا استخراج إلا بموافقة مشرف |
| **متوسط** | نزاعات تجارية بين شركات | إخفاء الأسماء والمبالغ الدقيقة |
| **منخفض** | مبادئ قانونية عامة من أحكام منشورة | إخفاء الأسماء فقط |

---

## 5. متى نستخدم TO VERIFY

استخدم `TO VERIFY` في حقل `notes` عند أي من الحالات التالية:

Use `TO VERIFY` in the `notes` field in any of these situations:

| الحالة | مثال |
|--------|------|
| نص الحكم غامض في موضع بعينه | `TO VERIFY — غير واضح إذا كانت المادة المُستند إليها 80 أم 81` |
| الاستخراج يتضمن تفسيرًا شخصيًا لا نصًا صريحًا | `TO VERIFY — legal_principle مُستنتَج لا مصرَّح به في الحكم` |
| الحكم يتعارض مع حكم آخر في المجموعة | `TO VERIFY — يتعارض مع JD-1435-003 في نقطة عبء الإثبات` |
| المرجع النظامي غير مؤكد | `TO VERIFY — المادة المُشار إليها تحتاج تأكيد من regulation-index.md` |
| الحكم صادر قبل تعديل تشريعي لاحق | `TO VERIFY — النظام المُطبَّق عُدِّل لاحقًا، قد يكون المبدأ تغيّر` |

**القاعدة:** الشك يُوجب `TO VERIFY` — لا تُكمل بدونه.
**Rule:** When in doubt, use `TO VERIFY` — never proceed without it.

---

## 6. كيف نربط الحكم بالأنظمة / Linking Rulings to Regulations

### الخطوات / Steps

**أولاً:** حدّد الأنظمة التي ذكرها الحكم صراحةً — لا تُضيف أنظمة من عندك.
First: identify regulations explicitly mentioned in the ruling — do not add regulations on your own.

**ثانياً:** طابق الصياغة مع `sources/regulation-index.md` للصيغة الموحَّدة.
Second: match the wording against `sources/regulation-index.md` for the standard citation format.

**ثالثاً:** إذا ذكر الحكم مادة بعينها، أضفها: `Saudi Labor Law (Royal Decree M/51 1426H) Art. 80`
Third: if the ruling cites a specific article, add it: `Saudi Labor Law (Royal Decree M/51 1426H) Art. 80`

**رابعاً:** إذا لم يُحدِّد الحكم المادة، اكتب النظام فقط وأضف في `notes`: `TO VERIFY — المادة المحددة غير مذكورة في الحكم`
Fourth: if the ruling does not specify the article, write the regulation only and add in `notes`: `TO VERIFY — specific article not stated in ruling`

### لا تفعل / Do Not

- ❌ تُضيف نظامًا لم يذكره الحكم صراحةً
- ❌ تُحيل لمادة بناءً على تقديرك الشخصي
- ❌ تختلق صياغة استشهاد غير واردة في `regulation-index.md`

---

## 7. متى لا نستخرج الحكم / When NOT to Extract

### حالات منع الاستخراج / Extraction Prohibited Cases

| الحالة | السبب |
|--------|-------|
| الحكم يُعرِّف أطرافه بشكل يصعب إخفاؤه | خطر الإضرار بخصوصية الأفراد |
| الحكم يتضمن تفاصيل شخصية حساسة (طبية، عائلية، جنائية) | خارج نطاق المشروع |
| مصدر الحكم غير موثوق أو غير رسمي | لا يمكن التحقق من صحته |
| الحكم صادر في قضية لا تزال منظورة | التعليق على قضايا منظورة غير مناسب |
| الحكم لا يتضمن أي استدلال قابل للتعميم | لا قيمة استخراجية |
| النص غير مكتمل بما يمنع فهم الاستدلال | الاستخراج الجزئي يُضلّل |
| الحكم يتعلق بمسائل شخصية أو أسرية | خارج نطاق المشروع (العقود التجارية والعمالية فقط) |

### إجراء عند الشك / Procedure When Unsure

إذا لم تكن متأكدًا من إمكانية الاستخراج:
1. لا تستخرج
2. افتح Issue في المشروع وصف الحالة
3. انتظر مراجعة المشرف قبل المتابعة

If unsure whether extraction is appropriate:
1. Do not extract
2. Open a project Issue describing the situation
3. Await maintainer review before proceeding

---

## 8. قائمة تحقق ما قبل الحفظ / Pre-Save Checklist

قبل إضافة أي صف استخراج، تحقق من كل النقاط:

Before adding any extraction row, verify every point:

- [ ] `case_id` فريد ولا يحتوي معلومات معرِّفة
- [ ] جميع أسماء الأطراف أُزيلت واستُبدلت
- [ ] `source_pdf` و`source_page` موثَّقان بدقة
- [ ] `applied_regulations` بالصيغة الموحَّدة من `regulation-index.md`
- [ ] `judicial_reasoning` مكتوب بلغة المستخلِص لا بنسخ من الحكم
- [ ] `legal_principle` مُستخلَص من الحكم لا من التفسير الشخصي
- [ ] `verification_status = draft`
- [ ] `TO VERIFY` مُضاف في `notes` عند كل غموض
- [ ] المبالغ الدقيقة أُزيلت أو استُبدلت بأوصاف نسبية
- [ ] الحكم لا يقع في أي من حالات منع الاستخراج

---

## الملفات المرتبطة / Related Files

| الملف | العلاقة |
|-------|---------|
| [`schema.md`](schema.md) | تعريف الحقول الكاملة |
| [`example-extraction.md`](example-extraction.md) | مثال تطبيقي |
| [`sources/judicial-decisions/README.md`](../../sources/judicial-decisions/README.md) | سياق مجموعة الأحكام |
| [`docs/legal-verification-lifecycle.md`](../../docs/legal-verification-lifecycle.md) | تفصيل `verification_status` |
| [`sources/regulation-index.md`](../../sources/regulation-index.md) | صيغ الاستشهاد الموحَّدة |
