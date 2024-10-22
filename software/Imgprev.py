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
frame = Frame(root, bg="#ff8600", bd=6, relief="sunken")
frame.place(relx=0.49, rely=0.5, anchor="center", width=600, height=500)
img = Image.open(image_path)
img.thumbnail((280, 180))  # Resize for display
img = ImageTk.PhotoImage(img)    
image_label = Label(frame, image=img, bg="#ff8850",bd=6)
image_label.image = img
image_label.place(relx=0.5, rely=0.5, anchor="center",width=450, height=350)

def showimg():
    img_path = os.path.join('uploads', 'image.jpeg')
    

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 36, "bold"), fg="black", bg="#ff8600") 
title_label.place(x=330,y=50)
def get_current_date():
    a= datetime.now().strftime("%Y-%m-%d")
    date_label.configure(text=a)

date_label = Label(root, text="Present Date", font=("Arial", 25,"bold"),  bg="#ff8600")
date_label.place(x=600,y=130)
get_current_date()

img_label=Label()
img_label.place(x=600,y=400)
showimg()

back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24),command=openmain)
back_button.place(x=100,y=700)

root.mainloop()
