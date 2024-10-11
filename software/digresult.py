from tkinter import *
from os import system
root=Tk()
root.title("AI-Based-Medical-Imaging-Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
Label(root,text="AI-Based-Medical-Imaging-Diagnosis",font=("Arial",20),relief="solid",width=40).pack(pady=30)
Label(root,text="Enter Name",font=("Arial",20),fg="skyblue").place(x=450,y=105,width=200,height=50)
Label(root,text="Enter Age",font=("Arial",20),fg="skyblue").place(x=850,y=105,width=200,height=50)
Label(root,text="Result",font=("Arial",25),fg="blue").place(x=500,y=300,width=500,height=60)
def to_exit():
    root.destroy()
    system("main.py")
# here no need of name and age functon 
def result():
    pass
Button(root,text="back",font=("Arial",15),bg="red",fg="white",width=15,command=to_exit).place(x=100,y=650)
root.mainloop()