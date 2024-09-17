import tkinter as tk
from tkinter import filedialog, Label, Entry, Button, Toplevel
from PIL import Image, ImageTk
from datetime import datetime

# Function to display the current date
def show_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=current_date)

# Function to handle image browsing
# def browse_image():
#     file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
#     image_entry.delete(0, tk.END)
#     image_entry.insert(0, file_path)

# Function to handle submit button click and open the next window
# def submit_image():
#     image_path = image_entry.get()
#     if image_path:
#         try:
#             open_preview_window(image_path)
#         except Exception as e:
#             print(f"Error loading image: {e}")
#     else:
#         print("No image selected")

# Function to open the new window (Image Preview Page)
def open_preview_window(image_path):
    # Create a new window for preview
    preview_window = Toplevel(root)
    preview_window.title("Image Preview")
    preview_window.geometry("500x400")
    preview_window.config(bg="#ff8600")

    # Title label at the upper center
    title_label = tk.Label(preview_window, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
    title_label.place(relx=0.5, y=50, anchor="center")

    # Present Date label just below the title
    date_label = tk.Label(preview_window, text="Present Date", bg="lightgray", font=("Arial", 16))
    date_label.place(relx=0.5, y=100, anchor="center")
    
    # Show present date
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=current_date)

    # Frame for image preview
    frame = tk.Frame(preview_window, bg="lightgray", bd=2, relief="sunken")
    frame.place(relx=0.5, rely=0.6, anchor="center", width=500, height=400)

    # Load and display the image
    img = Image.open(image_path)
    img.thumbnail((280, 180))  # Resize for display
    img = ImageTk.PhotoImage(img)
    
    image_label = tk.Label(frame, image=img, bg="lightgray")
    image_label.image = img  # Keep a reference to the image
    image_label.place(relx=0.5, rely=0.5, anchor="center")

    # Back button to close the preview window
    back_button = tk.Button(preview_window, text="Back", bg="red", fg="white", font=("Arial", 14), command=preview_window.destroy)
    back_button.place(relx=0.3, rely=0.9, anchor="center")

# Function to handle back button click
def back_clicked():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("500x400")
root.config(bg="#ff8600")

# Title label at the upper center
title_label = tk.Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20), padx=10, pady=10)
title_label.place(relx=0.5, y=50, anchor="center")

# Present Date label just below the title
date_label = tk.Label(root, text="Present Date", bg="lightgray", font=("Arial", 16))
date_label.place(relx=0.5, y=100, anchor="center")

# Show present date
show_date()

# Frame for image input and submit section
frame = tk.Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(relx=0.5, rely=0.55, anchor="center", width=400, height=350)

# Image entry field
# image_entry = tk.Entry(frame, font=("Arial", 13), width=20)
# image_entry.grid(row=5, column=1, padx=20, pady=20)

# Browse button
# browse_button = tk.Button(frame, text="Browse", font=("Arial", 13), command=browse_image)
# browse_button.grid(row=5, column=5, padx=10)

# Submit button
# submit_button = tk.Button(frame, text="Submit", font=("Arial", 12), command=submit_image)
# submit_button.place(relx=0.5, rely=0.5)

# Back button at the bottom left corner
back_button = tk.Button(root, text="Back", bg="red", fg="white", font=("Arial", 14), command=back_clicked)
back_button.place(relx=0.3, rely=0.9, anchor="center")

# Start the main loop
root.mainloop()
