from tkinter import *
from os import system 

root=Tk()
root.title("AI-Based-Medical-Imaging-Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
Label(root,text="AI-Based-Medical-Imaging-Diagnosis" , font=("Arial",20), relief="solid",width=35).pack(pady=30)

def to_exit():
    root.destroy()
    system("main.py")
def to_submit():
    root.destroy()
    system("main.py")
    pass
def entry_name():
    pass
def entry_age():
    pass
l1=Label(text="Enter name : ").place(x=400,y=85,height=20)
e1=Entry(root).place(x=550,y=85,width=340,height=40)
e2=Entry(root).place(x=550,y=155,width=340,height=40)
bt=Button(root,text="Back",bg="red",fg="white",font=("Arial",15),width=15,command=to_exit).place(x=200,y=650)

bt1=Button(root,text="submit",bg="lightgreen",fg="red",font=("Arial",15),width=15,command=to_submit).place(x=1100,y=650)
root.mainloop()