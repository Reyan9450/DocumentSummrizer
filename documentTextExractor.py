import fitz  # PyMuPDF

class PdfTextExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        text = ""
        # Open the PDF file
        with fitz.open(self.pdf_path) as pdf_file:
            # Iterate through each page of the PDF
            for page_num in range(pdf_file.page_count):
                # Get the page
                page = pdf_file.load_page(page_num)
                # Extract text from the page
                text += page.get_text()
        
        return text
