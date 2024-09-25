<<<<<<< HEAD
from tkinter import *
from tkinter import filedialog, Label, Entry, Button
from PIL import Image, ImageTk
=======
from tkinter import*
from os import system
>>>>>>> 1df899b817846b5957916cab8985d2068f0d897e
# Create the main window
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def mainopen():
    root.destroy()
    system("main.py")

<<<<<<< HEAD
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")])
    image_entry.delete(0, END)
    image_entry.insert(0, file_path)

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


# Title label at the upper center
=======
>>>>>>> 1df899b817846b5957916cab8985d2068f0d897e
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

date_label = Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(x=600,y=150)

frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(x=700, y=500, anchor="center", width=300, height=150)
image_entry = Entry(frame, font=("Arial", 12), width=20)
image_entry.grid(row=0, column=0, padx=10, pady=10)
<<<<<<< HEAD

# Browse button
browse_button = Button(frame, text="Browse", font=("Arial", 10),command=browse_image)
browse_button.grid(row=0, column=1, padx=10)

# Submit button
submit_button = Button(frame, text="Submit", font=("Arial", 12) , command=submit_image)
=======
browse_button = Button(frame, text="Browse", font=("Arial", 10))
browse_button.grid(row=0, column=1, padx=10)
submit_button = Button(frame, text="Submit", font=("Arial", 12),command=mainopen)
>>>>>>> 1df899b817846b5957916cab8985d2068f0d897e
submit_button.grid(row=1, column=0, columnspan=2, pady=10)
image_label = Label(root, bg="lightgray")
image_label.place(relx=0.5, y=350, anchor="center")
back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24),command=mainopen)
back_button.place(x=100,y=700)
root.mainloop()
