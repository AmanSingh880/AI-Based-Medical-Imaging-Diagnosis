from tkinter import *
from os import system 
from tkinter import messagebox


root=Tk()
root.title("AI-Based-Medical-Imaging-Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
Label(root,text="AI-Based-Medical-Imaging-Diagnosis" , font=("Arial",20), relief="solid",width=35).pack(pady=30)

def to_exit():
    root.destroy()
    system("main.py")

def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False
    
def entry_name():
    val=e1.get() 
    return validate_name(val)

def validate_age(age):
    age = float(age) 
    if 0 <= age <= 100: 
        return True
    return False

def entry_age():
    val=e2.get()
    return validate_age(val)

def txt_saver(name, age, filename="data.txt"):
    try:
        with open(filename, "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def to_submit():
    a=entry_name()
    if(a==False):
        messagebox.showwarning("Warning Medical-Imaging-Diagnosis","""Invalid Name
It should contain only alpha""")
        return False
    b=entry_age()
    if(b==False):
        messagebox.showwarning("Warning Medical-Imaging-Diagnosis","""Invalid Age
It should contain only number""")
        return False
    a=e1.get()
    b=e2.get()
    c=txt_saver(a,b)
    if(c==False):
        messagebox.showwarning("Medical-Imaging-Diagnosis","""Please Try Again
Internal Server Error""")
    if(a and b and c):
        root.destroy()
        system("backend.py")


l1=Label(text="Enter name : ").place(x=500,y=85,height=40,width=100)
l2=Label(text="Enter age  : ").place(x=500,y=155,height=40,width=100)

e1=Entry(root)
e1.place(x=650,y=85,width=340,height=40)
e2=Entry(root)
e2.place(x=650,y=155,width=340,height=40)
bt=Button(root,text="Back",bg="red",fg="white",font=("Arial",15),width=15,command=to_exit).place(x=200,y=650)

bt1=Button(root,text="submit",bg="lightgreen",fg="red",font=("Arial",15),width=15,command=to_submit).place(x=1100,y=650)
root.mainloop()