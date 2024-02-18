import cv2

def capture_and_save_image(output_path):
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the camera.")
        return

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Unable to capture frame.")
        return

    # Save the captured frame as an image
    cv2.imwrite(output_path, frame)

    # Release the camera
    cap.release()

    print("Image captured and saved successfully.")

# Example usage
output_path = "captured_image.jpg"  # Specify the path to save the captured image
capture_and_save_image(output_path)
