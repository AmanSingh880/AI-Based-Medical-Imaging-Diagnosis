import tkinter as tk
from tkinter import Label
from datetime import datetime

# Function to display the current date
def show_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=current_date)

# Function to handle start button click
def start_clicked():
    print("Start button clicked")

# Function to handle exit button click
def exit_clicked():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("AI-Based Medical Imaging Diagnosis")
root.geometry("500x400")
root.config(bg="#ff8600")

# Title label at the upper center
title_label = tk.Label(root, text="AI-Based Medical Imaging Diagnosis", font=("Arial", 20), padx=10, pady=10)
title_label.place(relx=0.5, y=50, anchor="center")

# Present Date label just below the title
date_label = tk.Label(root, text="Present Date", bg="lightgray", font=("Arial", 15))
date_label.place(relx=0.5, y=100, anchor="center")

# Show present date
show_date()

# Start button in the center
start_button = tk.Button(root, text="START", bg="blue", fg="white", font=("Arial", 24), command=start_clicked)
start_button.place(relx=0.5, rely=0.5, anchor="center")

# Exit button at the bottom left corner
exit_button = tk.Button(root, text="Exit", bg="red", fg="white", font=("Arial", 24), command=exit_clicked)
exit_button.place(relx=0.2, rely=0.9, anchor="center")

# Start the main loop
root.mainloop()
