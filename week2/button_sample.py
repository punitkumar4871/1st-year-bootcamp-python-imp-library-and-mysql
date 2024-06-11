import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

# Main window
root = tk.Tk()
root.title("Tkinter Button Example")

# Button widget
button = tk.Button(root, text="Click Me!", command=on_button_click, bg="lightgreen", fg="black", font=("Arial", 12), padx=10, pady=5)
button.pack(pady=20)

# Run application
root.mainloop()
