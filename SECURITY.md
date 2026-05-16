# الإبلاغ عن ثغرات أمنية / Security Policy

**Saudi Legal AI Framework** — سياسة الإبلاغ عن المشكلات الأمنية وحماية البيانات

---

## نطاق هذه السياسة / Scope

تُعالج هذه السياسة المشكلات ذات الطابع الحساس التي لا تصلح للإبلاغ العلني عبر Issues العادية، وتشمل:

This policy covers sensitive issues not suitable for public Issue reporting, including:

### ما يُعدّ حادثة أمنية / What Counts as a Security Incident

| المشكلة / Issue | المثال / Example |
|---|---|
| **تسريب بيانات عملاء** | أسماء حقيقية أو أرقام عقود أو بيانات موكّلين وُجدت في أي ملف بالمشروع |
| **بيانات غير مُخفاة (Non-anonymized)** | ملفات CSV تحتوي على بيانات حقيقية يمكن تمييزها |
| **معلومات قانونية حساسة** | محادثات حقيقية بين محامٍ وموكّل أو وثائق سرية |
| **ثغرة في سكربتات المشروع** | `validate_dataset.py` أو أي سكربت آخر يقبل مدخلات خطيرة |
| **ثغرة في GitHub Actions** | workflow يسمح بتنفيذ كود خارجي أو تسريب متغيرات بيئة |
| **Real client data** | Real names, contract numbers, or attorney-client data found in any project file |
| **Non-anonymized data** | CSV files containing identifiable real-world data |
| **Sensitive legal information** | Real attorney-client communications or confidential documents |
| **Script vulnerability** | `validate_dataset.py` or any script accepting dangerous input |
| **GitHub Actions vulnerability** | Workflow allowing external code execution or leaking environment variables |

---

## كيفية الإبلاغ / How to Report

### الخيار الأول — GitHub Security Advisories (مُفضَّل / Preferred)

استخدم **GitHub Security Advisories** للإبلاغ الخاص:

1. اذهب إلى تبويب **Security** في هذا المستودع
2. اضغط **Report a vulnerability**
3. اشرح المشكلة بوضوح: الملف المتأثر، طبيعة البيانات، حجم التأثير
4. لا تُرفق بيانات حساسة في نص التقرير — اكتفِ بالوصف

Use **GitHub Security Advisories** for private reporting:

1. Go to the **Security** tab of this repository
2. Click **Report a vulnerability**
3. Describe the issue clearly: affected file, nature of data, impact scope
4. Do not attach sensitive data in the report body — description only

---

### الخيار الثاني — Issue خاص (إذا لم تكن Security Advisories متاحة)

إذا لم تجد زر "Report a vulnerability":

1. افتح Issue عادي بعنوان يبدأ بـ `[SECURITY]` **دون** تفاصيل حساسة في العنوان
2. اكتب في نص الـ Issue: "يوجد بلاغ أمني يحتاج قناة خاصة — أرجو التواصل"
3. سيتواصل معك المشرف عبر قناة آمنة

If "Report a vulnerability" is not available:

1. Open a regular Issue with a title starting with `[SECURITY]` **without** sensitive details in the title
2. Write in the body: "There is a security report requiring a private channel — please reach out"
3. A maintainer will contact you via a secure channel

---

## ما يجب تضمينه في البلاغ / What to Include

```
1. الملف أو المسار المتأثر / Affected file or path
2. وصف المشكلة / Description of the issue
3. هل يوجد بيانات حقيقية؟ نعم / لا / Does real data exist? Yes / No
4. حجم التأثير المقدَّر / Estimated impact scope
5. خطوات إعادة الإنتاج إن أمكن / Reproduction steps if applicable
```

---

## ما لا يُعدّ حادثة أمنية / What Is NOT a Security Incident

الأمور التالية تُبلَّغ عبر Issues العادية:

Report the following via regular Issues instead:

- ❌ خطأ في معلومة قانونية أو استشهاد → **[Bug] Issue**
- ❌ مشكلة في تشغيل `validate_dataset.py` → **[Bug] Issue**
- ❌ رابط معطوب أو ملف مفقود → **[Bug] Issue**
- ❌ اقتراح لتحسين قالب أو skill → **[Skill] Issue**

---

## الاستجابة المتوقعة / Expected Response

| الخطوة / Step | التوقيت / Timeline |
|---|---|
| تأكيد استلام البلاغ / Acknowledgment | خلال 5 أيام عمل / Within 5 business days |
| تقييم أولي / Initial assessment | خلال 10 أيام عمل / Within 10 business days |
| الحل أو الخطة / Resolution or plan | يعتمد على التعقيد / Depends on complexity |

---

## مبادئ التعامل مع البيانات في هذا المشروع / Data Principles

هذا المشروع **لا يُجمع** أي بيانات مستخدمين ولا يتضمن أي نظام مصادقة. المشروع وثائق ونصوص فقط.

This project **does not collect** any user data and includes no authentication system. It is documentation only.

الحادثة الأمنية الأكثر احتمالًا هي **بيانات عملاء غير مُخفاة** مضافة عن غير قصد في ملفات `datasets/`. إذا وجدت ذلك، أبلغ فورًا بالطريقة الموضحة أعلاه.

The most likely security incident is **non-anonymized client data** accidentally added to `datasets/` files. If you find this, report immediately using the method described above.

---

## بعد حل المشكلة / After Resolution

- سيُذكر المُبلِّغ في ملف CHANGELOG أو commit ذي الصلة (إن رغب)
- لن تُنشر تفاصيل الحادثة إلا بعد التحقق من إزالة البيانات الحساسة بالكامل

- The reporter will be credited in the relevant CHANGELOG or commit (if desired)
- Incident details will not be published until sensitive data has been fully removed and verified

---

*سياسة أمان مُصمَّمة لمشروع توثيق قانوني مفتوح المصدر — لا بنية تحتية تشغيلية أو نظام مصادقة.*

*Security policy designed for an open-source legal documentation project — no operational infrastructure or authentication system.*
