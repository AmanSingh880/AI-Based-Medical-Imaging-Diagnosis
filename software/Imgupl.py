from tkinter import*
from os import system
# Create the main window
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def mainopen():
    root.destroy()
    system("main.py")

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

date_label = Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(x=600,y=150)

frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(x=700, y=500, anchor="center", width=300, height=150)
image_entry = Entry(frame, font=("Arial", 12), width=20)
image_entry.grid(row=0, column=0, padx=10, pady=10)
browse_button = Button(frame, text="Browse", font=("Arial", 10))
browse_button.grid(row=0, column=1, padx=10)
submit_button = Button(frame, text="Submit", font=("Arial", 12),command=mainopen)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)
image_label = Label(root, bg="lightgray")
image_label.place(relx=0.5, y=350, anchor="center")
back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24),command=mainopen)
back_button.place(x=100,y=700)
root.mainloop()
