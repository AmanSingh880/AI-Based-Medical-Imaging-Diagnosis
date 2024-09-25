# date function
from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
current_date = get_current_date()
print(current_date)


# save function
import tkinter as tk
from tkinter import filedialog

def save_image_path():
    image_path = filedialog.askopenfilename(title="Select an Image", 
                                            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    
    if image_path:
        with open("image_path.txt", "w") as file:
            file.write(image_path)
        print(f"Image path saved to 'image_path.txt': {image_path}")
    else:
        print("No image selected")

root = tk.Tk()
root.withdraw()  

save_image_path()

# read function
def read_image_path():
    try:

        with open("image_path.txt", "r") as file:
            image_path = file.read()
        print(f"Image path read from 'image_path.txt': {image_path}")
        return image_path
    except FileNotFoundError:
        print("File 'image_path.txt' not found.")
        return None

read_image_path()
