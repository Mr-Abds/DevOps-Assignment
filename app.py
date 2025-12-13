from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحتي التعريفية</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }
        body { background: #f5f5f5; color: #333; line-height: 1.6; }
        header { background: linear-gradient(to right, #4f46e5, #8b5cf6, #ec4899); color: white; padding: 2rem; text-align: center; }
        header h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
        header p { font-size: 1rem; opacity: 0.9; }
        nav { margin-top: 1rem; }
        nav a { color: white; text-decoration: none; margin: 0 0.5rem; padding: 0.5rem 1rem; border-radius: 10px; transition: 0.3s; }
        nav a:hover { background: rgba(255,255,255,0.2); }
        main { max-width: 1000px; margin: 2rem auto; padding: 0 1rem; display: grid; grid-template-columns: 2fr 1fr; gap: 2rem; }
        section, aside { background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        h2, h3 { margin-bottom: 1rem; color: #1f2937; }
        ul { list-style: none; }
        ul li { margin-bottom: 0.5rem; }
        footer { background: white; text-align: center; padding: 1rem; margin-top: 2rem; border-top: 1px solid #ddd; font-size: 0.9rem; }
        @media(max-width: 768px){ main { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <header>
<h1>عبدالله سالم بارفعه</h1>   
        <p>مطور |مهتم بـ Python و Flask — صفحة تعريفية احترافية</p>
        <nav>
            <a href="#projects">مشاريعي</a>
            <a href="#contact">تواصل معي</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>مرحباً — عنّي</h2>
            <p> أنا عبدالله، أخصائي/ـة أمن سيبراني أعمل على تأمين التطبيقات والبنية التحتية الرقمية. أهتم بتحليل الثغرات، اختبار الاختراق، وبناء أنظمة آمنة. أحبأنا عبدالله، أخصائي/ـة أمن سيبراني أعمل على تأمين التطبيقات والبنية التحتية الرقمية. أهتم بتحليل الثغرات، اختبار الاختراق، وبناء أنظمة آمنة. أحب استكشاف تقنيات الحماية، فحص الشبكات والتطبيقات، وتطبيق أفضل ممارسات الأمن لضمان سلامة البيانات والأنظمة. استكشاف تقنيات الحماية، فحص الشبكات والتطبيقات، وتطبيق أفضل ممارسات الأمن لضمان سلامة البيانات والأنظمة.</p>

            <h3>المهارات</h3>
            <ul>
                <li>Python - متقدم</li>
                <li>Flask - ممتاز</li>
                <li>HTML / CSS - جيد</li>
                <li>Git - جيد</li>
            </ul>
        </section>

        <aside>
            <h3>روابط سريعة</h3>
            <ul>
                <li><a href="#projects">مشاريعي</a></li>
                <li><a href="#contact">التواصل</a></li>
                <li><a href="#">حساب GitHub</a></li>
            </ul>
        </aside>
    </main>

    <section id="projects" style="max-width:1000px;margin:2rem auto;padding:0 1rem;">
        <h3>مشاريعي</h3>
        <p>أمثلة على مشاريع: تطبيق Flask بسيط، واجهة React، ونشر على خادم محلي أو سحابي.</p>
    </section>

    <section id="contact" style="max-width:1000px;margin:2rem auto;padding:0 1rem;">
        <h3>تواصل معي</h3>
        <p>البريد الإلكتروني: abdullahsalemahmed1@gmail.com</p>
        <p>الهاتف: +96772084811   </p>

    </section>

    <footer>
        © 2025 صفحتك الشخصية — تم تصميم الواجهة لتكون قابلة للتعديل بسهولة
    </footer>

    <script>
        console.log('صفحة التعريف جاهزة');
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8030, debug=True)
