from tkinter import *
from os import system
import sqlite3
root=Tk()
root.title("AI-Based-Medical-Imaging-Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def en(name,age,result,p_p):
    name_l.configure(text=name)
    age_l.configure(text=age)
    result_l.configure(text=f"Prediction Ratio = {p_p}, result = {result}")

def select_all():
    mydb=sqlite3.connect('diagonis.db')
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM HISTORY")
    TwoD_list=mycursor.fetchall()
    TwoD_list.reverse()
    return TwoD_list
    mydb.commit()
a=select_all()[0]
name=a[1]
age=a[2]
p_p=a[3]
result=a[4]







Label(root,text="AI-Based-Medical-Imaging-Diagnosis",font=("Arial",20),relief="solid",width=40).pack(pady=30)
name_l=Label(root,text="Enter Name",font=("Arial",20),fg="skyblue")
name_l.place(x=450,y=105,width=200,height=50)
age_l=Label(root,text="Enter Age",font=("Arial",20),fg="skyblue")
age_l.place(x=850,y=105,width=200,height=50)
result_l=Label(root,text="Result",font=("Arial",25),fg="blue")
result_l.place(x=400,y=300,width=700,height=70)
en(name,age,result,p_p)
def to_exit():
    root.destroy()
    system("main.py")
# here no need of name and age functon 

Button(root,text="back",font=("Arial",15),bg="red",fg="white",width=15,command=to_exit).place(x=100,y=650)
root.mainloop()