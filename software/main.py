from tkinter import *
import os
from datetime import datetime
root=Tk()
root.title("AI-Based-Medical-Imaging-Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def get_current_date():
    a= datetime.now().strftime("%Y-%m-%d")
    date_label.configure(text=a)
def to_upload():
    root.destroy()
    os.system("Imgupl.py")
def to_exit():
    os.system("home.py")
    root.destroy()
def to_preview():
    root.destroy()
    os.system("Imgprev.py")
def to_diagnosis():
    root.destroy()
    os.system("digform.py")
def to_result():
    root.destroy()
    os.system("dighist.py")
def to_exit():
    root.destroy()
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 36, "bold"), fg="black", bg="#ff8600") 
title_label.place(x=320,y=60)

date_label = Label(root, text="Present Date", font=("Arial", 25,"bold"), bg="#ff8600")
date_label.place(x=650,y=130)
get_current_date()

bt=Button(root,text="Image Upload",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_upload)
bt.place(x=530,y=200)

bt1=Button(root,text="Image Preview",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_preview)
bt1.place(x=800,y=200)

bt2=Button(root,text="Diagnosis",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_diagnosis)
bt2.place(x=530,y=300)

bt3=Button(root,text="Diagnosis Result",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_result)
bt3.place(x=800,y=300)

bt4=Button(root,text="Exit",font=("Arial", 15),bg="red" ,fg="white" ,width=20,command=to_exit)
bt4.place(x=100,y=650)

root.mainloop()