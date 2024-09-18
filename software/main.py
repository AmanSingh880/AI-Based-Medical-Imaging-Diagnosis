from tkinter import *

root=Tk()
root.title("AI-Based-Medical-Imaging-Diagnosis")
root.geometry("500x900")
root.config(bg="#ff8600")
Label( root,text="AI-Based-Medical-Imaging-Diagnosis", font=("Arial", 20),relief="solid",width=35).pack(pady=25)
def to_upload():
    pass
def to_preview():
    pass
def to_diagnosis():
    pass
def to_result():
    pass
def to_exit():
    pass
bt=Button(root,text="Image Upload",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_upload)
bt.place(x=530,y=85)

bt1=Button(root,text="Image Preview",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_preview)
bt1.place(x=780,y=85)

bt2=Button(root,text="Diagnosis",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_diagnosis)
bt2.place(x=530,y=155)

bt3=Button(root,text="Diagnosis Result",font=("Arial", 15),bg="yellow" ,fg="green" ,width=20,command=to_result)
bt3.place(x=780,y=155)

bt4=Button(root,text="Exit",font=("Arial", 15),bg="red" ,fg="green" ,width=20,command=to_exit)
bt4.place(x=100,y=650)

root.mainloop()