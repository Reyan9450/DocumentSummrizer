import easyocr

def extract_text_from_image(image_path, language='en'):
    # Initialize EasyOCR reader
    reader = easyocr.Reader([language])

    # Read text from the image
    result = reader.readtext(image_path)

    # Extract and concatenate text from the result
    text = ' '.join([entry[1] for entry in result])

    return text

# Example usage
image_path = "example.png"  # Replace with the path to your image file
extracted_text = extract_text_from_image(image_path)
print("Extracted text:")
print(extracted_text)
