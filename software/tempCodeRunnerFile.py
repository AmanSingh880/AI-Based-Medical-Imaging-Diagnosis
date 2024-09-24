import tkinter as tk
from tkinter import filedialog, Label, Entry, Button
from PIL import Image, ImageTk  # For handling image files
# Function to display the current date
from datetime import datetime
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")])
    image_entry.delete(0, tk.END)
    image_entry.insert(0, file_path)
# Function to handle submit button click
def submit_image():
    image_path = image_entry.get()
    if image_path:
        try:
            img = Image.open(image_path)
            img.thumbnail((200, 200))  
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img  
        except Exception as e:
            print(f"Error loading image: {e}")
    else:
        print("No image selected")
root = tk.Tk()
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
root.mainloop()