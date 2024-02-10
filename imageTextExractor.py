import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)
    return text

# Example usage
image_path = "example.png"  # Replace with the path to your image file
extracted_text = extract_text_from_image(image_path)
print("Extracted text:")
print(extracted_text)
