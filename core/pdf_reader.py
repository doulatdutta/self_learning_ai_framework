# core/pdf_reader.py

import fitz  # PyMuPDF

class PDFReader:
    def read_pdf(self, pdf_path):
        text = ""
        try:
            with fitz.open(pdf_path) as doc:
                for page in doc:
                    text += page.get_text()
        except Exception as e:
            print(f"Error reading PDF: {e}")
        return text
