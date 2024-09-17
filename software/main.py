from tkinter import *

root = Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("500x400")
root.configure(bg="orange")

# Create and place the title label
title_label = Label(root, text="AI-Based Medical Imaging Diagnosis", bg="lightgray", font=("Arial", 14), relief="solid", width=40)
title_label.pack(pady=10)

# Functionality for buttons
def upload_image():
    pass

def preview_image():
    pass

def diagnose():
    pass
def show_diagnosis_result():
    pass

def exit_program():
    pass

# Create a frame to center the buttons
frame = Frame(root, bg="orange")
frame.pack(pady=40)

# Create and place buttons inside the frame for central alignment
button1 = Button(frame, text="Image Upload", bg="yellow",fg="green" ,font=("Arial", 12), command=upload_image)
button1.grid(row=0, column=0, padx=20, pady=10)

button2 = Button(frame, text="Image Preview", bg="yellow",fg="green" , font=("Arial", 12), command=preview_image)
button2.grid(row=0, column=1, padx=20, pady=10)

button3 = Button(frame, text="Diagnosis", bg="yellow", fg="green" ,font=("Arial", 12), command=diagnose)
button3.grid(row=1, column=0, padx=20, pady=10)

button4 = Button(frame, text="Diagnosis Result", bg="yellow", fg="green" ,font=("Arial", 12), command=show_diagnosis_result)
button4.grid(row=1, column=1, padx=20, pady=10)

# Exit button placed in the bottom left corner
exit_button =Button(root, text="Exit", bg="red", fg="white", font=("Arial", 12), command=exit_program)
exit_button.place(x=20, y=340, width=100, height=40)

# Run the application
root.mainloop()
