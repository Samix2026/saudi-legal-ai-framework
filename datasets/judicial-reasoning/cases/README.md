# datasets/judicial-reasoning/cases/
# مجلد استخراجات القضايا القضائية الفردية

**الغرض / Purpose:** استخراجات منظَّمة لقضايا فردية من المجموعة القضائية لعام 1435هـ.

---

## اصطلاح التسمية / Naming Convention

```
JD-{سنة هجرية}-{رقم تسلسلي بثلاثة أرقام}.md
```

| مثال | المعنى |
|------|--------|
| `JD-1435-001.md` | أول قضية مُستخرَجة من مجموعة 1435هـ |
| `JD-1435-002.md` | ثاني قضية من نفس المجموعة |

**القاعدة:** الترقيم تسلسلي داخل كل سنة هجرية — لا علاقة له برقم القضية الأصلية في الملف.

---

## دورة حياة التحقق / Verification Lifecycle

كل ملف استخراج يبدأ بـ `verification_status: draft` ولا يرتفع إلى حالة أعلى إلا بالمسار التالي:

```
draft
  │
  ▼  (مراجعة باحث أو ممارس موثوق)
community-reviewed
  │
  ▼  (تأكيد مكتوب من محامٍ مرخَّص في المملكة)
verified
```

**لا يُستشهَد بأي استخراج ولا يُدمَج في skills أو prompts قبل الوصول إلى `community-reviewed` على الأقل.**

---

## حالة مخرجات OCR / OCR Status

كل نص مُستخرَج من ملفات PDF يمر بمسار منفصل قبل الاستخراج القضائي:

```
[pdftoppm + tesseract]
       │
       ▼
   ocr_draft
(نص خام — لا تنظيف)
       │
       ▼  (مراجعة بشرية مقابل الصورة الأصلية)
   ocr_reviewed
       │
       ▼  (يُنقَل للاستخراج القضائي المنظَّم)
     draft
```

**الرمز `[OCR_UNCERTAIN]` في أي ملف استخراج:** يعني أن هذا الجزء من النص كان غير واضح في مخرج OCR ويحتاج مراجعة مقابل صورة PDF الأصلية.

---

## مسار عمل الاستخراج / Extraction Workflow

```
1. OCR → experiments/ocr-production-test/ (أو ocr-scan/)
2. مراجعة OCR text مقابل صورة PDF
3. كتابة ملف استخراج هنا بـ verification_status: draft
4. مراجعة مجتمعية → community-reviewed
5. تأكيد محامٍ → verified
6. دمج في datasets/ و skills/ (فقط بعد verified)
```

---

## سياسة المراجعة المجتمعية / Community-Reviewed Policy

**ما يُشترَط للانتقال إلى `community-reviewed`:**
- مراجعة النص الكامل مقابل ملف PDF الأصلي (ليس الـ OCR فقط)
- التحقق من أن جميع البيانات المعرِّفة أُزيلت
- التحقق من صحة الأنظمة المُستشهَد بها عبر `sources/regulation-index.md`
- وصف طبيعة المراجع في PR description: (باحث قانوني / ممارس / مساهم موثوق)

**ما لا يكفي للانتقال إلى `community-reviewed`:**
- مراجعة الـ OCR text فقط بدون مقارنة بالصورة الأصلية
- مراجعة آلية أو بالذكاء الاصطناعي فقط
- مراجعة من شخص خارج مجال القانون أو الدراسات القانونية

---

## المجموعات الحالية / Current Collections

| المجموعة | عدد الملفات | المصدر | الحالة |
|---------|------------|--------|--------|
| 1435هـ | 5 | sources/judicial-decisions/1435/1.pdf | draft |

---

## توثيق الإحالات الفقهية / Documenting Fiqh Citations

**قاعدة إلزامية:** أي مرجع فقهي يظهر في حقل `applied_regulations` أو `judicial_reasoning` داخل أي ملف استخراج **يجب تسجيله** في:

```
sources/fiqh-judicial-references/citation-index.md
```

**خطوات التسجيل:**
1. تحقق أولاً من أن المرجع غير مُدرَج بالفعل في `citation-index.md`
2. إذا غير مُدرَج: أضف سجلاً جديداً بـ `verification_status: draft`
3. أشر إلى الـ `reference_id` (مثل `FQR-1435-001`) داخل ملف الاستخراج إذا أردت الربط الصريح
4. راجع [`sources/fiqh-judicial-references/usage-guidelines.md`](../../../sources/fiqh-judicial-references/usage-guidelines.md) للقواعد الكاملة

**لا تستشهد بمرجع فقهي داخل ملف استخراج إذا لم يكن القاضي أحال إليه صراحةً في الحكم.**

---

## الملفات المرتبطة / Related Files

| الملف | العلاقة |
|-------|---------|
| [`../schema.md`](../schema.md) | تعريف الحقول الـ 19 |
| [`../extraction-guidelines.md`](../extraction-guidelines.md) | قواعد الاستخراج والإخفاء |
| [`../example-extraction.md`](../example-extraction.md) | مثال تعليمي |
| [`../../docs/legal-verification-lifecycle.md`](../../../docs/legal-verification-lifecycle.md) | تفصيل دورة حياة التحقق |
| [`../../docs/ocr-strategy.md`](../../../docs/ocr-strategy.md) | استراتيجية OCR |
| [`../../scripts/ocr_pdf_pages.py`](../../../scripts/ocr_pdf_pages.py) | سكربت توليد OCR |
| [`../../../sources/fiqh-judicial-references/citation-index.md`](../../../sources/fiqh-judicial-references/citation-index.md) | فهرس المراجع الفقهية المُحال إليها في الأحكام |
