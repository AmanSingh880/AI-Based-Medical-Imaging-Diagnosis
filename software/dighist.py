from tkinter import *
from os import system
from tkinter import ttk
import sqlite3

root = Tk()

# Function to fetch and display data
def select_all():
    mydb = sqlite3.connect('diagonis.db')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM HISTORY")
    TwoD_list = mycursor.fetchall()
    TwoD_list.reverse()    
    # Clear the table before inserting new data
    for item in table.get_children():
        table.delete(item)
    
    # Insert data into the Treeview
    for row in TwoD_list:
        table.insert("", "end", values=row)
    
    mydb.commit()
    mydb.close()

# GUI setup
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")  # Same background color

# Title Label
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 28, "bold"), fg="black", bg="#ff8600")  # Same color for title
title_label.place(x=450, y=40)

# Frame for the table
table_frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
table_frame.place(x=750, y=450, anchor="center", width=800, height=300)

# Scrollbar for the table
scrollbar = Scrollbar(table_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# Define the columns for the Treeview
columns = ("ID", "Name", "Age", "Predicated", "Result", "Date")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10, yscrollcommand=scrollbar.set)

# Link scrollbar with the Treeview
scrollbar.config(command=table.yview)

# Define the headings and column properties
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Predicated", text="Predicated")
table.heading("Result", text="Result")
table.heading("Date", text="Date")

# Set column width and alignment
for col in columns:
    table.column(col, width=125, anchor="center")

table.pack(fill=BOTH, expand=True)

# Back button functionality
def back():
    root.destroy()
    system("main.py")

# Add a "Refresh" button to reload the data dynamically
refresh_button = Button(root, text="Refresh", bg="green", fg="white", font=("Arial", 18), command=select_all)
refresh_button.place(x=150, y=200, width=150, height=50)

# Add an "Exit" button to close the window
exit_button = Button(root, text="Exit", bg="red", fg="white", font=("Arial", 18), command=back)
exit_button.place(x=150, y=280, width=150, height=50)

# Fetch and display data on startup
select_all()

root.mainloop()
