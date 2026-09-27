# Revised version for better performance and error handling
from fpdf import FPDF
class PDF(FPDF):
    def __init__(self, font_path="DejaVuSans.ttf"):
        super().__init__()
        self.font_path = font_path
        self.add_page()
        self.setup_font()
    def setup_font(self):
        try:
            # Adding font with UTF-8 support (e.g., Persian font)
            self.add_font("DejaVu", "", self.font_path, uni=True)
            self.set_font("DejaVu", size=14)
        except Exception as e:
            print(f"Error loading font: {e}")
    def add_title(self, title):
        self.set_font("DejaVu", 'B', 16)
        self.cell(0, 10, title, ln=True, align='C')
    def add_content(self, content):
        self.set_font("DejaVu", size=14)
        self.multi_cell(0, 10, content)
# Create PDF file with support for Persian text
pdf = PDF()
pdf.add_title("تشخیص خرابی خودرو با هوش مصنوعی")
content = "این پروژه با استفاده از یادگیری ماشین و بینایی ماشین، خرابی‌های احتمالی خودرو را تشخیص می‌دهد."
pdf.add_content(content)
# Save the file in the current directory with error handling
try:
    pdf.output("diagnosis_ai.pdf")
except Exception as e:
    print(f"Error saving PDF: {e}")