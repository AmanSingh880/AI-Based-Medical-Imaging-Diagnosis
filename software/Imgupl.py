from tkinter import *
from tkinter import filedialog, Label, Entry, Button
from PIL import Image, ImageTk
from tkinter import*
from os import system
import shutil
import os

# Create the main window
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")

import os
import shutil

def submit_image(source_path, destination_dir):
    try:
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"The source file at {source_path} does not exist.")

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        destination_path = os.path.join(destination_dir, "image.jpeg")
        
        shutil.copy(source_path, destination_path)
        
        print(f"Image copied and saved as: {destination_path}")
    
    except Exception as e:
        print(f"Error: {e}")


def mainopen():
    root.destroy()
    system("main.py")

def save_image_path():
    print("Aman")
    image_path = filedialog.askopenfilename(title="Select an Image", 
                                            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if image_path:
        print(f"Image path saved to 'image_path.txt': {image_path}")
        submit_image(image_path,"uploads")
    else:
        print("No image selected")



# Title label at the upper center

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

image_entry = Entry(font=("Arial", 12), width=20)
image_entry.place(x=500,y=180)
browse_button = Button(text="Browse", font=("Arial", 10),command=save_image_path)
browse_button.place(x=700,y=180)

submit_button = Button( text="Submit", font=("Arial", 12),command=mainopen)
submit_button.place(x=550,y=230)

back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24),command=mainopen)
back_button.place(x=100,y=700)
root.mainloop()
