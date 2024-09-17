from tkinter import *
from tkinter import ttk


# Main Tkinter window
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")

# Title label at the upper center
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

# Name input button
name_label = Label(root, text="Enter Name", bg="lightgray", font=("Arial", 12), width=15)
name_label.place(x=600, y=150, anchor="center")

# Age input button
age_label = Label(root, text="Enter Age", bg="lightgray", font=("Arial", 12), width=15)
age_label.place(x=900, y=150, anchor="center")

# Frame for the table
table_frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
table_frame.place(x=700, y=500, anchor="center", width=400, height=150)

# Defining columns for the table
columns = ("Name", "Age", "Result", "Date", "ID")

# Creating a treeview widget (table)
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=5)

# Defining each column
table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Result", text="Result")
table.heading("Date", text="Date")
table.heading("ID", text="ID")

# Set column width
for col in columns:
    table.column(col, width=75, anchor="center")

# Place the table
table.pack(fill="both", expand=True)

# Exit button in the bottom left corner
exit_button = Button(root, text="Exit", bg="red", fg="white", font=("Arial", 24))
exit_button.place(x=100,y=700)

# Start the Tkinter event loop
root.mainloop()
