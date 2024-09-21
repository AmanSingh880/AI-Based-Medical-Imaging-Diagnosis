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
