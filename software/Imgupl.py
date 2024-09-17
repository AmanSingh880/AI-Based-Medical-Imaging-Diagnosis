import tkinter as tk
from tkinter import filedialog, Label, Entry, Button
from PIL import Image, ImageTk  # For handling image files

# Function to display the current date
from datetime import datetime
def show_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=current_date)

# Function to handle image browsing
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    image_entry.delete(0, tk.END)
    image_entry.insert(0, file_path)

# Function to handle submit button click
def submit_image():
    image_path = image_entry.get()
    if image_path:
        try:
            # Open and display the image
            img = Image.open(image_path)
            img.thumbnail((200, 200))  # Resize for display
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img  # Keep a reference to the image
        except Exception as e:
            print(f"Error loading image: {e}")
    else:
        print("No image selected")

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
date_label = tk.Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(relx=0.5, y=100, anchor="center")

# Show present date
show_date()

# Frame for image input and submit section
frame = tk.Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(relx=0.5, rely=0.55, anchor="center", width=300, height=150)

# Image entry field
image_entry = tk.Entry(frame, font=("Arial", 12), width=20)
image_entry.grid(row=0, column=0, padx=10, pady=10)

# Browse button
browse_button = tk.Button(frame, text="Browse", font=("Arial", 10), command=browse_image)
browse_button.grid(row=0, column=1, padx=10)

# Submit button
submit_button = tk.Button(frame, text="Submit", font=("Arial", 12), command=submit_image)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

# Image display label
image_label = tk.Label(root, bg="lightgray")
image_label.place(relx=0.5, y=350, anchor="center")

# Back button at the bottom left corner
back_button = tk.Button(root, text="Back", bg="red", fg="white", font=("Arial", 24), command=back_clicked)
back_button.place(relx=0.2, rely=0.9, anchor="center")

# Start the main loop
root.mainloop()
