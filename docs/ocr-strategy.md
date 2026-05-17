# استراتيجية التعرف الضوئي على النص
# OCR Strategy

**Saudi Legal AI Framework** — استراتيجية استخراج النص من ملفات PDF القضائية المُحوَّلة ضوئياً

**الحالة / Status:** 🔧 سكربت الإنتاج متاح — `scripts/ocr_pdf_pages.py` / Production script available — `scripts/ocr_pdf_pages.py`
**آخر تحديث / Last updated:** 2026-05-17

---

## ⚠️ تحذير جوهري / Critical Warning

> **بالعربية:** مخرجات OCR من ملفات قضائية **ليست نصوصًا قانونية موثوقة**. أي نص مستخرَج آليًا يخضع لأخطاء التعرف، وتشويه الأرقام، وفقدان التشكيل، ولا يُستخدم مباشرةً في أي تحليل قانوني قبل التحقق البشري الكامل.
>
> **In English:** OCR output from judicial PDF files is **not authoritative legal text**. Any automatically extracted text is subject to recognition errors, number distortion, diacritic loss, and must not be used directly in any legal analysis without complete human verification.

---

## جدول المحتويات / Table of Contents

- [سكربت الإنتاج](#0-سكربت-الإنتاج--production-script)
- [لماذا نحتاج OCR](#1-لماذا-نحتاج-ocr--why-we-need-ocr)
- [طبيعة ملفات PDF القضائية](#2-طبيعة-ملفات-pdf-القضائية--nature-of-judicial-pdf-files)
- [مخاطر OCR في السياق القانوني](#3-مخاطر-ocr-في-السياق-القانوني--ocr-risks-in-legal-context)
- [لماذا لا يُستخدم OCR كحقيقة قانونية مباشرة](#4-لماذا-لا-يُستخدم-ocr-كحقيقة-قانونية-مباشرة--why-ocr-output-is-not-direct-legal-fact)
- [مقارنة الأدوات](#5-مقارنة-الأدوات--tool-comparison)
- [خطة الاختبار الصغيرة](#6-خطة-الاختبار-الصغيرة--small-test-plan)
- [حالة مخرجات OCR](#7-حالة-مخرجات-ocr--ocr-output-status)
- [الملفات المرتبطة](#8-الملفات-المرتبطة--related-files)

---

## 0. سكربت الإنتاج / Production Script

**الملف / File:** [`scripts/ocr_pdf_pages.py`](../scripts/ocr_pdf_pages.py)

### المتطلبات / Requirements

```bash
# macOS (Homebrew)
brew install poppler tesseract tesseract-lang
```

تحقق من التثبيت:

```bash
pdftoppm -v   # Poppler pdftoppm
tesseract --version
tesseract --list-langs   # يجب أن يظهر 'ara'
```

### صيغة الأمر / Command Syntax

```bash
python3 scripts/ocr_pdf_pages.py \
    --pdf   <مسار ملف PDF> \
    --pages <نطاق الصفحات> \
    --out   <مجلد المخرجات> \
    --lang  ara \
    --dpi   300
```

### أمثلة / Examples

```bash
# صفحات متتالية / Consecutive pages
python3 scripts/ocr_pdf_pages.py \
    --pdf sources/judicial-decisions/1435/1.pdf \
    --pages 18-20 \
    --out experiments/ocr-production-test/1pdf-pages-18-20/

# صفحات غير متتالية / Non-consecutive pages
python3 scripts/ocr_pdf_pages.py \
    --pdf sources/judicial-decisions/1435/3.pdf \
    --pages 5,12,17 \
    --out experiments/ocr-production-test/3pdf-pages-5-12-17/

# صيغة مختلطة / Mixed format
python3 scripts/ocr_pdf_pages.py \
    --pdf sources/judicial-decisions/1435/1.pdf \
    --pages 18-19,22 \
    --out experiments/ocr-production-test/1pdf-mixed/ \
    --dpi 400
```

### هيكل المخرجات / Output Structure

```
<out>/
├── images/
│   ├── page-018.png        ← صورة الصفحة بالدقة المحددة
│   └── page-019.png
├── text/
│   ├── page-018.txt        ← نص OCR خام (ocr_draft)
│   └── page-019.txt
└── metadata.json           ← المصدر، الصفحات، الأدوات، الحالة
```

### محتوى metadata.json

```json
{
  "source_pdf": "sources/judicial-decisions/1435/1.pdf",
  "pages": [18, 19],
  "lang": "ara",
  "dpi": 300,
  "tool_versions": {
    "pdftoppm": "pdftoppm version 26.04.0",
    "tesseract": "tesseract 5.5.2"
  },
  "output_status": "ocr_draft",
  "timestamp_utc": "2026-05-17T...",
  "output_files": [...]
}
```

### تحذيرات الاستخدام / Usage Warnings

```
⚠️  المخرج خام (ocr_draft) — لا تنظيف، لا تعديل
⚠️  لا تُضمِّن النص مباشرةً في dataset أو skill أو prompt
⚠️  راجع كل صفحة بشريًا مقابل الصورة الأصلية قبل الاستخراج
⚠️  لا تعتمد على OCR وحده لإخفاء أسماء الأطراف
```

---

## 1. لماذا نحتاج OCR / Why We Need OCR

الاستخراج اليدوي الحالي للأحكام القضائية بطيء ومحدود النطاق. 14 ملف PDF تمثّل مئات الصفحات — استخراجها يدويًا بالكامل يستغرق وقتًا طويلًا ويُقيِّد المساهمة.

The current manual extraction of judicial decisions is slow and limited in scope. 14 PDF files represent hundreds of pages — fully manual extraction is time-consuming and restricts contribution.

**OCR يُمكِّن من:**

| الإمكانية | التفصيل |
|-----------|---------|
| **اكتشاف المحتوى** | معرفة ما يوجد في كل صفحة دون قراءة بشرية كاملة |
| **الفهرسة السريعة** | البحث النصي في الأحكام بعد التحقق |
| **مدخل الاستخراج** | توفير نص خام يُراجَع بشريًا بدلًا من البدء من الصفر |
| **قياس التغطية** | تحديد نسبة ما تمت فهرسته من المجموعة الكاملة |

**OCR لا يُلغي الاستخراج البشري** — يُعجِّله فقط بتوفير مسودة أولى.

OCR does not replace human extraction — it only accelerates it by providing a first draft.

---

## 2. طبيعة ملفات PDF القضائية / Nature of Judicial PDF Files

ملفات `sources/judicial-decisions/1435/*.pdf` **ليست PDF نصية** — هي صور رقمية لصفحات مطبوعة أو مكتوبة، مُدرَجة داخل حاوية PDF.

The files in `sources/judicial-decisions/1435/*.pdf` are **not text PDFs** — they are digital images of printed or written pages embedded inside a PDF container.

### الأدلة التقنية / Technical Evidence

```
حجم متوسط الملف:  ~12MB لكل PDF
الإصدار:          PDF 1.4
pdftotext output:  فارغ — لا نص قابل للاستخراج
النوع:            صور مُمسوحة ضوئياً (scanned images)
الدقة:            غير معروفة — تؤثر على جودة OCR
```

### ما يعنيه ذلك / What This Means

```
PDF نصي (text-based):        OCR غير مطلوب ← استخراج مباشر
PDF صوري (image-based):  ←── هذه ملفاتنا — OCR مطلوب
```

---

## 3. مخاطر OCR في السياق القانوني / OCR Risks in Legal Context

السياق القانوني يُضاعف تأثير أخطاء OCR — خطأ في رقم مادة أو اسم طرف يُنتج تحليلًا خاطئًا.

The legal context amplifies OCR errors — an error in an article number or party name produces incorrect analysis.

### 3.1 أخطاء التعرف العامة / General Recognition Errors

| نوع الخطأ | مثال | الأثر القانوني |
|-----------|------|----------------|
| تشابه الأحرف | `و` ↔ `ر` · `ن` ↔ `ت` | تغيير معنى النص |
| دمج الكلمات | `نظام العمل` → `نظامالعمل` | فشل البحث النصي |
| فصل الكلمات | `الإعسار` → `الإ عسار` | خطأ في التصنيف |
| أحرف غير مقروءة | `■` أو `?` بدل حرف | ثغرات في النص |

### 3.2 التشكيل / Diacritics

التشكيل (الحركات: فَتحة، ضَمّة، كَسرة...) نادر في OCR العربي لكنه حاسم في النصوص القانونية:

Diacritics (vowel marks: fatha, damma, kasra...) are rare in Arabic OCR output but critical in legal texts:

```
يَجِب (يجب) ← معنى مختلف تمامًا ← يُجِب (يجيب)
مُدَّعٍ ← يختلف عن ← مُدَّعى عليه
```

**OCR عادةً يتجاهل التشكيل.** هذا مقبول في النصوص العادية — غير مقبول في نصوص الأحكام.

### 3.3 أرقام المواد النظامية / Regulatory Article Numbers

```
خطأ OCR:   المادة (٨١) → المادة (٨١) ← قد تُقرأ كـ (٨ ١) أو (٨١.) أو (٨١,)
الأثر:     إسناد حكم لمادة خاطئة ← خطأ قانوني جوهري
```

الأرقام العربية (٠١٢٣...) والأرقام الإنجليزية (0123...) قد يخلط بينهما OCR.

### 3.4 أسماء الأطراف / Party Names

```
خطأ OCR في اسم:   يُصعِّب إخفاء الهوية — قد يتغير الاسم بشكل يبدو اسمًا آخر
الأثر:            خطر الكشف عن هوية طرف حقيقي بشكل غير مقصود
```

كل استخراج يجب أن يُعيد فحص الأسماء من النص الأصلي (الصورة) — لا يعتمد على OCR وحده للإخفاء.

### 3.5 الصفحات والمراجع / Pages and References

```
رقم صفحة مشوَّه:   يُخطئ في تحديد نطاق القسم (start_page / end_page)
مرجع حكم:          رقم الحكم أو التاريخ قد يتغير بخطأ OCR
```

---

## 4. لماذا لا يُستخدم OCR كحقيقة قانونية مباشرة / Why OCR Output Is Not Direct Legal Fact

### المبدأ / The Principle

```
النص القانوني الأصلي (الصورة في PDF) ← هو المرجع الوحيد الموثوق
مخرج OCR                              ← مسودة مساعِدة للقراءة البشرية فقط
```

### الأسباب التفصيلية / Detailed Reasons

**أولًا: معدلات الخطأ / Error Rates**
حتى أفضل أدوات OCR تُخطئ في 1-5% من الأحرف في النصوص العربية المُمسوحة. في نص قانوني من 500 كلمة، هذا يعني 5-25 خطأ محتملًا.

Even the best OCR tools make errors in 1-5% of characters in scanned Arabic text. In a 500-word legal text, that is 5-25 potential errors.

**ثانيًا: غياب السياق الدلالي / No Semantic Context**
OCR يحوِّل بكسلات إلى أحرف — لا يفهم المعنى. جملة مشوَّهة تبدو صحيحة نحويًا لكنها تحمل معنى مختلفًا تمامًا.

OCR converts pixels to characters — it does not understand meaning. A garbled sentence may appear grammatically valid while carrying a completely different meaning.

**ثالثًا: المسؤولية القانونية / Legal Responsibility**
الاستشهاد بحكم قضائي معتمدًا على OCR غير مُتحقَّق منه — مع احتمال خطأ في رقم المادة أو اسم المحكمة — هو خطأ منهجي في التحليل القانوني.

Citing a judicial ruling based on unverified OCR — with a possible error in an article number or court name — is a methodological error in legal analysis.

**الاستنتاج / Conclusion:**
```
OCR output + مراجعة بشرية كاملة = مدخل موثوق
OCR output بلا مراجعة           = لا يُستخدم في هذا المشروع
```

---

## 5. مقارنة الأدوات / Tool Comparison

### جدول المقارنة / Comparison Table

| الأداة | الدعم العربي | الدقة (تقديرية) | التكلفة | الخصوصية | الصعوبة التقنية | الملاحظات |
|--------|-------------|----------------|---------|----------|----------------|-----------|
| **Tesseract** | ✅ (نموذج ara) | متوسط | مجاني | ✅ محلي | منخفضة–متوسطة | الأقدم، يحتاج preprocessing جيد |
| **PaddleOCR** | ✅ (متنامي) | جيد–متوسط | مجاني | ✅ محلي | متوسطة | أفضل layout analysis من Tesseract |
| **Cloud OCR** | ✅ ممتاز | عالية | مدفوع | ⚠️ تحميل خارجي | منخفضة | مشكلة رفع وثائق قضائية لطرف ثالث |
| **Manual Extraction** | ✅ مثالي | 100% | وقت بشري | ✅ كامل | — | الأسلوب الحالي — المعيار المرجعي |
| **AI-assisted OCR** | ✅ ممتاز | عالية–جيدة | مدفوع/محدود | ⚠️ تحميل خارجي | منخفضة | خطر الهلوسة (hallucination) — خطر إضافي |

### تفصيل كل أداة / Tool Details

---

#### Tesseract

```
النوع:        مفتوح المصدر (Apache 2.0)
المطوِّر:      Google (مُصدَر للمجتمع)
نموذج عربي:   ara.traineddata
المتطلبات:    tesseract-ocr + arabic language pack
```

**المزايا / Advantages:**
- مجاني ومحلي — لا رفع بيانات
- دعم عربي مستقر
- قابل للتخصيص والتدريب

**العيوب / Disadvantages:**
- ضعيف في التشكيل
- يحتاج preprocessing للصور منخفضة الجودة
- layout analysis محدود (يحتاج pytesseract + OpenCV)
- ضعيف في النصوص ذات الاتجاهين (عربي + إنجليزي)

**مناسب لـ:** اختبار أولي منخفض التكلفة على صور جودتها مقبولة.

---

#### PaddleOCR

```
النوع:        مفتوح المصدر (Apache 2.0)
المطوِّر:      Baidu PaddlePaddle
الدعم العربي: متاح في الإصدارات الحديثة
المتطلبات:    paddlepaddle + paddleocr Python package
```

**المزايا / Advantages:**
- layout analysis أفضل من Tesseract
- نماذج متعددة الإصدار (fast / accurate)
- دعم RTL في تطور مستمر

**العيوب / Disadvantages:**
- تثبيت ثقيل (PaddlePaddle كبير الحجم)
- الدعم العربي أحدث — أقل اختبارًا
- وثائق أقل مقارنةً بـ Tesseract

**مناسب لـ:** مقارنة مع Tesseract في خطة الاختبار.

---

#### Cloud OCR (Google Vision / Azure / AWS Textract)

```
الأمثلة:     Google Cloud Vision API · Azure AI Vision · AWS Textract
التسعير:     يبدأ من $1-3 لكل 1000 صفحة (يتفاوت)
```

**المزايا / Advantages:**
- دقة عربية عالية جداً
- يتعامل مع التشكيل بشكل أفضل
- لا يحتاج تثبيتًا محلياً

**العيوب / Disadvantages:**
- **مشكلة الخصوصية الجوهرية:** رفع وثائق قضائية — حتى مُخفاة الهوية — لخادم طرف ثالث
- تكلفة متراكمة عند المقياس الكبير
- يتطلب اتصال إنترنت مستمر

**الحكم في سياق هذا المشروع:** غير مفضَّل للمرحلة الأولى بسبب إشكالية الخصوصية. يُعاد النظر فيه بعد استشارة قانونية حول متطلبات حماية البيانات القضائية.

---

#### Manual Extraction — الاستخراج اليدوي

```
الحالة:  الأسلوب الحالي في المشروع
الأدوات: قارئ PDF + نموذج استخراج (datasets/judicial-reasoning/schema.md)
```

**المزايا / Advantages:**
- دقة 100% في قراءة النص
- يفهم السياق والغموض
- يُطبِّق anonymization صحيحًا
- المعيار المرجعي لتقييم OCR

**العيوب / Disadvantages:**
- بطيء جدًا — يُقيِّد التوسع
- غير قابل للمقياس الكبير

**الدور:** المعيار الذهبي (ground truth) — يُستخدم للتحقق من أي مخرج OCR.

---

#### AI-assisted OCR — المساعدة بالذكاء الاصطناعي

```
الأمثلة:  GPT-4 Vision · Claude vision · Gemini Vision
الأسلوب: إرسال صورة الصفحة → طلب استخراج النص
```

**المزايا / Advantages:**
- يفهم السياق — يُصحِّح أخطاء OCR بالسياق
- يتعامل مع التشكيل أفضل
- يمكن طلب الاستخراج بتنسيق محدد مباشرةً

**العيوب / Disadvantages:**
- **خطر الهلوسة (hallucination):** النموذج قد يُضيف كلمات لم تكن في الصفحة
- تكلفة مرتفعة لكل صفحة
- إشكالية الخصوصية (رفع صور وثائق قضائية)
- المخرج يبدو دقيقًا لكن قد يكون مُولَّدًا لا مُستخرَجًا

**الحكم:** يُستخدم بحذر شديد للتحقق المتقاطع فقط — لا كمصدر أولي.

---

## 6. خطة الاختبار الصغيرة / Small Test Plan

قبل اتخاذ قرار الأداة، نُجري اختبارًا على 3 صفحات فقط من `sources/judicial-decisions/1435/1.pdf`.

Before deciding on a tool, we run a test on 3 pages only from `1.pdf`.

### الهدف / Objective

> تقييم جودة OCR على نص قضائي عربي مُمسوح ضوئياً — وتحديد ما إذا كانت الجودة كافية للاستخدام كمسودة مساعِدة.

> Evaluate OCR quality on scanned Arabic judicial text — and determine whether quality is sufficient for use as an assistive draft.

---

### الخطوة 1: اختيار الصفحات / Step 1 — Page Selection

اختر 3 صفحات تُمثِّل حالات مختلفة:

Choose 3 pages representing different cases:

| الصفحة | المعيار |
|--------|---------|
| صفحة من منتصف حكم | نص كثيف، أرقام مواد، تعداد |
| صفحة بها جدول أو قائمة | تحدي layout |
| صفحة بها عنوان + متن | تحقق من التعرف على الهيكل |

لا تختر الصفحة الأولى (غلاف) ولا الأخيرة (مؤشر).

Do not choose the first page (cover) or the last (index).

---

### الخطوة 2: تشغيل الأداة / Step 2 — Run the Tool

**للـ Tesseract:**
```bash
# تحويل صفحة PDF إلى صورة أولًا
pdftoppm -r 300 -png sources/judicial-decisions/1435/1.pdf /tmp/ocr-test -f <start> -l <end>

# تشغيل Tesseract على الصورة
tesseract /tmp/ocr-test-<n>.png /tmp/ocr-output-<n> -l ara

# مراجعة النتيجة
cat /tmp/ocr-output-<n>.txt
```

**ملاحظة:** لا تُشغِّل OCR على الملف كاملًا في هذه المرحلة — 3 صفحات فقط.

**Note:** Do not run OCR on the full file at this stage — 3 pages only.

---

### الخطوة 3: تقييم الجودة / Step 3 — Quality Assessment

لكل صفحة مُختبَرة، سجِّل التقييم في جدول:

For each tested page, record the evaluation in a table:

| المعيار | الوصف | الدرجة (1-5) |
|---------|-------|-------------|
| **دقة الأحرف** | هل الأحرف الأساسية صحيحة؟ | |
| **التشكيل** | هل حُفظ التشكيل (جزئيًا أو كليًا)؟ | |
| **أرقام المواد** | هل أرقام كـ (م/51) دقيقة؟ | |
| **التنسيق** | هل الفقرات والأسطر منظَّمة؟ | |
| **الكلمات غير المقروءة** | كم كلمة ظهرت كـ `?` أو فارغة؟ | |

---

### الخطوة 4: المقارنة اليدوية / Step 4 — Manual Comparison

افتح الصورة الأصلية (PDF viewer) جنبًا إلى جنب مع النص المُستخرَج:

Open the original image (PDF viewer) side by side with the extracted text:

```
PDF viewer (الصورة)          ←──── قارن ────►    النص المُستخرَج (txt)

- اقرأ الصفحة يدويًا
- حدد أول 10 جمل
- قارن جملة بجملة مع OCR output
- سجِّل الأخطاء التي وجدتها
```

---

### الخطوة 5: قرار الاستمرار / Step 5 — Go / No-Go Decision

بعد التقييم، اتخذ قرارًا بناءً على المعايير:

After evaluation, make a decision based on criteria:

| النتيجة | المعيار | القرار |
|---------|---------|--------|
| ✅ جودة عالية | < 3% أخطاء في الأحرف · أرقام مواد صحيحة | **استمرار — نُشغِّل على القسم كاملًا** |
| ⚠️ جودة متوسطة | 3-8% أخطاء · أرقام مواد غالبًا صحيحة | **مشروط — نُشغِّل + مراجعة بشرية مكثَّفة** |
| ❌ جودة ضعيفة | > 8% أخطاء · أرقام مواد غير موثوقة | **توقف — نغيِّر الأداة أو نواصل يدويًا** |

**إذا كانت النتيجة "توقف":** أعِد الاختبار بأداة مختلفة (PaddleOCR) أو بمعالجة مسبقة للصورة (deskew + contrast).

---

### سجل نتائج الاختبار / Test Results Log

```
التاريخ:         [ لم يُنفَّذ بعد ]
الأداة:          [ ]
الصفحات:         [ ]
متوسط الدقة:     [ ]
أخطاء المواد:    [ ]
القرار:          [ ]
الملاحظات:       [ ]
```

سيُحدَّث هذا السجل بعد تنفيذ الاختبار.
This log will be updated after the test is executed.

---

## 7. حالة مخرجات OCR / OCR Output Status

### القاعدة الأساسية / The Core Rule

```
كل نص مُستخرَج بـ OCR يبدأ كـ:   ocr_draft / unverified
ولا ينتقل إلى مرحلة أعلى إلا بعد:  مراجعة بشرية كاملة للنص مقابل الصورة الأصلية
```

Every OCR-extracted text starts as: `ocr_draft / unverified`
It does not advance to a higher stage without: complete human review of the text against the original image.

### مستويات حالة OCR / OCR Status Levels

| الحالة | المعنى | من يُعيِّنها | هل تُستخدم في تحليل؟ |
|--------|--------|-------------|---------------------|
| `ocr_draft` | نص مُستخرَج آليًا — لم يُراجَع | النظام/الأداة | ❌ لا |
| `ocr_reviewed` | راجعه إنسان وأصلح الأخطاء | مساهم بشري | ⚠️ بتحفظ |
| `draft` | استخراج قضائي يدوي — لم يُتحقق منه | مساهم بشري | ⚠️ بتحفظ |
| `reviewed` | راجعه مختص (باحث / أكاديمي) | مراجع مختص | ✅ مع إشارة |
| `verified` | أكده محامٍ مرخَّص سعودي | محامٍ مرخَّص | ✅ |

### تدفق الحالة / Status Flow

```
[أداة OCR]
    │
    ▼
ocr_draft
(النص الخام — لا يُستخدم)
    │
    ▼ (مراجعة بشرية للنص مقابل الصورة)
ocr_reviewed
(مُصحَّح — يُستخدم كمسودة استخراج)
    │
    ▼ (يُنقَل إلى datasets/judicial-reasoning/ كاستخراج رسمي)
draft
    │
    ▼ (مراجعة مختص)
reviewed
    │
    ▼ (تأكيد محامٍ مرخَّص)
verified
```

### قواعد الإخراج / Output Rules

```
❌ لا تُضمِّن نص ocr_draft في أي skill أو prompt أو dataset مباشرةً
❌ لا تعتمد على OCR وحده لإخفاء أسماء الأطراف — راجع الصورة الأصلية دائمًا
❌ لا تُسنِد نتيجة قانونية لنص لم تتحقق منه بشريًا
✅ استخدم OCR كمسودة — ابدأ المراجعة منها، لا تنهِ بها
```

---

## 8. الملفات المرتبطة / Related Files

| الملف | العلاقة |
|-------|---------|
| [`sources/judicial-decisions/README.md`](../sources/judicial-decisions/README.md) | سياق مجموعة الأحكام المُمسوحة |
| [`datasets/judicial-index/README.md`](../datasets/judicial-index/README.md) | الفهرسة اليدوية الحالية — قبل OCR |
| [`datasets/judicial-index/judicial-corpus-index.csv`](../datasets/judicial-index/judicial-corpus-index.csv) | الفهرس الحالي — يُحدَّث بعد OCR |
| [`datasets/judicial-reasoning/schema.md`](../datasets/judicial-reasoning/schema.md) | مخطط الاستخراج — 19 حقلاً |
| [`datasets/judicial-reasoning/extraction-guidelines.md`](../datasets/judicial-reasoning/extraction-guidelines.md) | دليل الاستخراج والإخفاء |
| [`docs/system-architecture.md`](system-architecture.md) | موضع OCR في المعمارية الكاملة |
| [`docs/legal-verification-lifecycle.md`](legal-verification-lifecycle.md) | دورة حياة التحقق بعد OCR |
