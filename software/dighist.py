from tkinter import *
from os import system
from tkinter import ttk
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

name_label = Label(root, text="Enter Name", bg="lightgray", font=("Arial", 12), width=15)
name_label.place(x=600, y=150, anchor="center")

age_label = Label(root, text="Enter Age", bg="lightgray", font=("Arial", 12), width=15)
age_label.place(x=900, y=150, anchor="center")

table_frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
table_frame.place(x=700, y=500, anchor="center", width=400, height=150)

columns = ("Name", "Age", "Result", "Date", "ID")

table = ttk.Treeview(table_frame, columns=columns, show="headings", height=5)

table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Result", text="Result")
table.heading("Date", text="Date")
table.heading("ID", text="ID")

for col in columns:
    table.column(col, width=75, anchor="center")

table.place(x=0,y=0)
def back():
    system("main.py")
exit_button = Button(root, text="Exit", bg="red", fg="white", font=("Arial", 24))
exit_button.place(x=100,y=700)

root.mainloop()
