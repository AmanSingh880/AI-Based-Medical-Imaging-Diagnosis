from tkinter import *
from os import system
from tkinter import ttk
import sqlite3

root = Tk()
def select_all():
    mydb = sqlite3.connect('diagonis.db')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM HISTORY")
    TwoD_list = mycursor.fetchall()
    TwoD_list.reverse()    

    for item in table.get_children():
        table.delete(item)
    for row in TwoD_list:
        table.insert("", "end", values=row)
    
    mydb.commit()
    mydb.close()


root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600") 

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 30, "bold"), fg="black", bg="#ff8600") 
title_label.place(x=450, y=40)


table_frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
table_frame.place(x=800, y=400, anchor="center", width=900, height=600)

scrollbar = Scrollbar(table_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)


columns = ("ID", "Name", "Age", "Predicated", "Result", "Date")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=12, yscrollcommand=scrollbar.set)


scrollbar.config(command=table.yview)


table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Predicated", text="Predicated")
table.heading("Result", text="Result")
table.heading("Date", text="Date")


for col in columns:
    table.column(col, width=125, anchor="center")

table.pack(fill=BOTH, expand=True)

def back():
    root.destroy()
    system("main.py")

refresh_button = Button(root, text="Refresh", bg="green", fg="white", font=("Arial", 18), command=select_all)
refresh_button.place(x=150, y=200, width=150, height=50)

exit_button = Button(root, text="Exit", bg="red", fg="white", font=("Arial", 18), command=back)
exit_button.place(x=150, y=280, width=150, height=50)
select_all()

root.mainloop()
