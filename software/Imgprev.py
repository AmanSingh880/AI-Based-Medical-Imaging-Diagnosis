from tkinter import *
from os import system
import os
from PIL import Image, ImageTk
from datetime import datetime
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def openmain():
    root.destroy()
    system("main.py")

image_path = os.path.join('uploads', 'image.jpeg')
frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(relx=0.5, rely=0.6, anchor="center", width=500, height=400)
img = Image.open(image_path)
img.thumbnail((280, 180))  # Resize for display
img = ImageTk.PhotoImage(img)    
image_label = Label(frame, image=img, bg="lightgray")
image_label.image = img  # Keep a reference to the image
image_label.place(relx=0.5, rely=0.5, anchor="center")

def showimg():
    img_path = os.path.join('uploads', 'image.jpeg')
    


title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)
def get_current_date():
    a= datetime.now().strftime("%Y-%m-%d")
    date_label.configure(text=a)

date_label = Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(x=600,y=150)
get_current_date()

img_label=Label()
img_label.place(x=600,y=400)
showimg()

back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24),command=openmain)
back_button.place(x=100,y=700)

root.mainloop()
