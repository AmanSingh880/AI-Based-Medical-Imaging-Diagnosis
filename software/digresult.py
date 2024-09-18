from tkinter import *

# Create the main window
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")

# Create and place the title label
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", bg="lightgray", font=("Arial", 14), relief="solid", width=40)
title_label.pack(pady=20)

# Functionality for buttons
def get_result():
    pass

def go_back():
    pass

# Create and place the entry fields
frame = Frame(root, bg="orange")
frame.pack(pady=20)

name_entry = Entry(frame, font=("Arial", 12), justify="center")
name_entry.insert(0, "Enter Name")
name_entry.grid(row=0, column=0, padx=20, pady=10, ipadx=20, ipady=5)

age_entry = Entry(frame, font=("Arial", 12), justify="center")
age_entry.insert(0, "Enter Age")
age_entry.grid(row=0, column=1, padx=20, pady=10, ipadx=20, ipady=5)

# Create and place the "Result" button
result_button = Button(root, text="Result", bg="lightgray", font=("Arial", 14), command=get_result)
result_button.pack(pady=20, ipadx=60, ipady=10)

# Create and place the "Back" button
back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 12), command=go_back)
back_button.place(x=20, y=340, width=100, height=40)

# Run the application
root.mainloop()
