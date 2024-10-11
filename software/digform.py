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
    entry_name()
    root.destroy()
    system("main.py")

def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False
    
def entry_name():
    val=name.get() 
    print(val)   
    print(validate_name(val))

def validate_age(age):
    age = float(age) 
    if 0 <= age <= 100: 
        return True
    return False

def entry_age():
    val=age.get()
    print(validate_age(val))

name=StringVar
age=StringVar
l1=Label(text="Enter name : ").place(x=500,y=85,height=40,width=100)
l2=Label(text="Enter age  : ").place(x=500,y=155,height=40,width=100)

e1=Entry(root,text=name).place(x=650,y=85,width=340,height=40)
e2=Entry(root,text=age).place(x=650,y=155,width=340,height=40)
bt=Button(root,text="Back",bg="red",fg="white",font=("Arial",15),width=15,command=to_exit).place(x=200,y=650)

bt1=Button(root,text="submit",bg="lightgreen",fg="red",font=("Arial",15),width=15,command=to_submit).place(x=1100,y=650)
root.mainloop()