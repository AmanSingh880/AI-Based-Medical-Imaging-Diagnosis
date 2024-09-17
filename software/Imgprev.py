from tkinter import *


# Create the main window
root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("1500x900")
root.config(bg="#ff8600")

# Title label at the upper center
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20))
title_label.place(x=500,y=80)

# Present Date label just below the title
date_label = Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(x=600,y=150)

# Frame for image input and submit section
frame = Frame(root, bg="lightgray", bd=2, relief="sunken")
frame.place(x=700, y=500, anchor="center", width=300, height=250)

# Back button at the bottom left corner
back_button = Button(root, text="Back", bg="red", fg="white", font=("Arial", 24))
back_button.place(x=100,y=700)

# Start the main loop
root.mainloop()
