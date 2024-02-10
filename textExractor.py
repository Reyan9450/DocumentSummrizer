import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    # Open the PDF file
    with fitz.open(pdf_path) as pdf_file:
        # Iterate through each page of the PDF
        for page_num in range(pdf_file.page_count):
            # Get the page
            page = pdf_file.load_page(page_num)
            # Extract text from the page
            text += page.get_text()
    return text

# Example usage
pdf_path = "example.pdf"  # Replace with the path to your PDF file
extracted_text = extract_text_from_pdf(pdf_path)
print("Extracted text:")
print(extracted_text)
