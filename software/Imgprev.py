from tkinter import *
from os import system

root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def openmain():
    root.destroy()
    system("main.py")
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

date_label = Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(x=600,y=150)

frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(x=700, y=500, anchor="center", width=300, height=250)


back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24),command=openmain)
back_button.place(x=100,y=700)

root.mainloop()
