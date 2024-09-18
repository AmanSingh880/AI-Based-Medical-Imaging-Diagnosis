from tkinter import *
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", bg="lightgray", font=("Arial", 14), relief="solid", width=40)
title_label.pack(pady=20)


name_entry = Entry(root, font=("Arial", 12), justify="center")
name_entry.insert(0, "Enter Name")
name_entry.pack(pady=10, ipadx=40, ipady=5)

age_entry = Entry(root, font=("Arial", 12), justify="center")
age_entry.insert(0, "Enter Age")
age_entry.pack(pady=10, ipadx=40, ipady=5)


def submit():
    pass

def go_back():
    pass

back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 12), command=go_back)
back_button.place(x=50, y=300, width=100, height=50)

submit_button = Button(root, text="Submit", bg="lightgreen", fg="red", font=("Arial", 12), command=submit)
submit_button.place(x=350, y=300, width=100, height=50)

root.mainloop()
