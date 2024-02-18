import tkinter as tk
from tkinter import filedialog

def select_document():
    document_path = filedialog.askopenfilename(title="Select Document", filetypes=(("PDF files", "*.pdf"), ("Text files", "*.txt")))
    if document_path:
        document_label.config(text="Selected Document: " + document_path)

def select_image():
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.jpg *.png *.jpeg"), ("All files", "*.*")))
    if image_path:
        image_label.config(text="Selected Image: " + image_path)

# Create the main window
root = tk.Tk()
root.title("File Selector")

# Create buttons to select document and image
document_button = tk.Button(root, text="Select Document", command=select_document)
document_button.pack(pady=10)

image_button = tk.Button(root, text="Select Image", command=select_image)
image_button.pack(pady=10)

# Labels to display selected document and image paths
document_label = tk.Label(root, text="")
document_label.pack()

image_label = tk.Label(root, text="")
image_label.pack()

# Run the Tkinter event loop
root.mainloop()
