from tkinter import *
from os import system
from datetime import datetime
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")
def get_current_date():
    a= datetime.now().strftime("%Y-%m-%d")
    date_label.configure(text=a)
def open():
    root.destroy()
    system("main.py")
def exit():
    root.destroy()

title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 36, "bold"), fg="black", bg="#ff8600") 
title_label.place(x=350,y=80)

date_label = Label(root, text="Present Date", font=("Arial", 25,"bold"), bg="#ff8600")
date_label.place(x=600,y=150)
get_current_date()

start_button =Button(root, text="START", bg="blue", fg="white", font=("Arial", 24),command=open)
start_button.place(x=600,y=300)

exit_button =Button(root, text="Exit", bg="red", fg="white", font=("Arial", 24),command=exit)
exit_button.place(x=100,y=700)



root.mainloop()
