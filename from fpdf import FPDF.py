from fpdf import FPDF
import shutil

# Copy font
font_src_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_dest_path = "/mnt/data/DejaVuSans.ttf"
shutil.copy(font_src_path, font_dest_path)

class PDF(FPDF):
    def header(self):
        # No header for slides
        pass

    def add_slide_title(self, title):
        self.set_font("Vazir", 'B', 16)
        self.cell(0, 10, title, ln=True, align='C')
        self.ln(5)

    def add_paragraph(self, text):
        self.set_font("Vazir", '', 12)
        self.multi_cell(0, 8, text, align='R')
        self.ln(3)

pdf = PDF('P', 'mm', 'A4')
pdf.add_font('Vazir', '', font_dest_path, uni=True)
pdf.add_font('Vazir', 'B', font_dest_path, uni=True)

# Slide: Title
pdf.add_page()
pdf.set_font("Vazir", 'B', 20)
pdf.cell(0, 15, "معرفی پروژه: سیستم تشخیص رفتار خودرو با هوش مصنوعی", ln=True, align='C')
pdf.ln(10)
pdf.set_font("Vazir", '', 14)
pdf.cell(0, 10, "توسط تیم تحقیق و توسعه AI-Car", ln=True, align='C')

# Slide: Introduction
pdf.add_page()
pdf.add_slide_title("معرفی پروژه")
pdf.add_paragraph(
    "در این پروژه، یک سامانه هوشمند مبتنی بر بینایی ماشین و یادگیری عمیق توسعه می‌دهیم که قابلیت تشخیص رفتارهای "
    "خودرو و راننده را در زمان واقعی دارد. این سیستم با هدف افزایش ایمنی، بهینه‌سازی مصرف سوخت و ارائه گزارش‌های "
    "تحلیلی طراحی شده است."
)
pdf.add_paragraph("[تصویر 1: دیاگرام معماری کلی سیستم]")

# Slide: Team
pdf.add_page()
pdf.add_slide_title("اعضای تیم و نقش‌ها")
pdf.add_paragraph("• محمد: مدیریت پروژه، برنامه‌ریزی، هماهنگی فنی و تضمین کیفیت\n"
                  "• عرفانه: کارشناس داده و بینایی ماشین، جمع‌آوری و آنالیز Telemetry\n"
                  "• آرشام: سناریو‌نویسی، دیجیتال مارکتینگ، معرفی و جذب سرمایه‌گذار")
pdf.add_paragraph("[تصویر 2: عکس اعضای تیم یا آواتار]")

# Slide: Problem Statement
pdf.add_page()
pdf.add_slide_title("بیان مسئله")
pdf.add_paragraph(
    "حوادث رانندگی ناشی از عدم توجه راننده و نقص در سامانه‌های هشداردهنده، چالش مهمی در صنعت خودرو محسوب می‌شود. "
    "نیاز به یک راه‌حل هوشمند برای تشخیص خستگی، عدم تمرکز و رفتارهای خطرناک راننده احساس می‌شود."
)
pdf.add_paragraph("[تصویر 3: نمودار آمار حوادث و علت‌ها]")

# Slide: Solution
pdf.add_page()
pdf.add_slide_title("راه‌حل پیشنهادی")
pdf.add_paragraph(
    "- تحلیل ویدئوی کابین و محیط با استفاده از شبکه‌های عصبی\n"
    "- تشخیص وضعیت راننده (خستگی، حواس‌پرتی)\n"
    "- مانیتورینگ Telemetry خودرو و پیش‌بینی خطاها\n"
    "- ارائه داشبورد تعاملی و هشدارهای لحظه‌ای"
)
pdf.add_paragraph("[تصویر 4: نمونه داشبورد یا نمودارها]")

# Slide: Tech Stack
pdf.add_page()
pdf.add_slide_title("فناوری‌ها و ابزارها")
pdf.add_paragraph(
    "• بینایی ماشین: OpenCV, TensorFlow\n"
    "• یادگیری عمیق: PyTorch, Keras\n"
    "• پردازش داده: Python, Pandas\n"
    "• وب و داشبورد: FastAPI, React, D3.js\n"
    "• DevOps: Docker, GitHub Actions\n"
    "• ابزارهای AI: GitHub Copilot, ChatGPT"
)

# Slide: Roadmap
pdf.add_page()
pdf.add_slide_title("نقشه راه پروژه")
pdf.add_paragraph(
    "Sprint 0 (هفته 1): راه‌اندازی محیط و زیرساخت\n"
    "Sprint 1 (هفته 2-3): MVP و مستندسازی API\n"
    "Sprint 2 (هفته 4-5): ماژول شبیه‌سازی و کنترل اولیه\n"
    "Sprint 3 (هفته 6-7): بهینه‌سازی و داشبورد تحلیلی\n"
    "Sprint 4 (هفته 8-9): ادغام و تست استرس\n"
    "Sprint 5 (هفته 10): استقرار نهایی و UAT"
)
pdf.add_paragraph("[تصویر 5: نمودار گانت یا جدول زمانی]")

# Slide: Next Steps
pdf.add_page()
pdf.add_slide_title("گام‌های بعدی")
pdf.add_paragraph(
    "1. جمع‌آوری بازخورد از کاربران اولیه\n"
    "2. بهبود مدل‌های AI و افزایش دقت\n"
    "3. آماده‌سازی نسخه صنعتی و ارتباط با تولیدکنندگان\n"
    "4. جذب سرمایه برای گسترش محصول"
)

# Save PDF
# output_path = "/mnt/data/AI_Car_Project_Presentation.pdf"
# pdf.output(output_path)
# output_path
