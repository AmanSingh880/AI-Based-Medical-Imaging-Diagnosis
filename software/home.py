from tkinter import *
from os import system
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def open():
    root.destroy()
    system("main.py")
def exit():
    root.destroy()

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

date_label = Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(x=600,y=150)

start_button =Button(root, text="START", bg="blue", fg="white", font=("Arial", 24),command=open)
start_button.place(x=600,y=300)

exit_button =Button(root, text="Exit", bg="red", fg="white", font=("Arial", 24),command=exit)
exit_button.place(x=100,y=700)



root.mainloop()
