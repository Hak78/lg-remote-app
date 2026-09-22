[app]
# اسم التطبيق
title = Lg Remote

# اسم الحزمة المعرف للتطبيق
package.name = lg_remote_app
package.domain = com.hak78

# مسار مجلد السورس كود (موقع ملف main.py)
source.dir = .

# امتدادات الملفات المراد تضمينها
source.include_exts = py,png,jpg,kv,atlas,txt

# المتطلبات والمكتبات الأساسية (flet مهمة جداً هنا)
requirements = python3,flet,requests

# أذونات التطبيق (الإنترنت لتطبيق التحكم عبر الواي فاي)
android.permissions = INTERNET

# التوجيه الافتراضي للشاشة (أفقي، عمودي، أو تلقائي)
orientation = portrait

# (خياري) إصدار التطبيق
version = 0.1

[buildozer]
# درجة تفصيل الأخطاء أثناء البناء
log_level = 2
warn_on_root = 1
