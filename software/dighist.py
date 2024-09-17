import tkinter as tk
from tkinter import ttk

# Function to exit the application
def exit_app():
    root.quit()

# Main Tkinter window
root = tk.Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("500x400")
root.config(bg="#ff8600")

# Title label at the upper center
title_label = tk.Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(relx=0.5, y=50, anchor="center")

# Name input button
name_label = tk.Label(root, text="Name", bg="lightgray", font=("Arial", 15), width=15)
name_label.place(relx=0.25, y=120, anchor="center")

# Age input button
age_label = tk.Label(root, text="Age", bg="lightgray", font=("Arial", 15), width=15)
age_label.place(relx=0.75, y=120, anchor="center")

# Frame for the table
table_frame = tk.Frame(root, bg="lightgray", bd=2, relief="sunken")
table_frame.place(relx=0.5, rely=0.55, anchor="center", width=400, height=150)

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
exit_button = tk.Button(root, text="Exit", bg="red", fg="white", font=("Arial", 20), command=exit_app)
exit_button.place(relx=0.3, rely=0.9, anchor="center")

# Start the Tkinter event loop
root.mainloop()
