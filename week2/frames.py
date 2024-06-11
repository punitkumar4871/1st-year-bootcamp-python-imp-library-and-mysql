import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Nested Frames Example")

# Create the main frame
main_frame = tk.Frame(root, bg="lightgray", bd=5, relief="groove")
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the top frame
top_frame = tk.Frame(main_frame, bg="lightblue", bd=2, relief="raised")
top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

label1 = tk.Label(top_frame, text="Top Frame", bg="lightblue")
label1.pack(padx=10, pady=10)
# Create the bottom frame
bottom_frame = tk.Frame(main_frame, bg="lightgreen", bd=2, relief="sunken")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)


label2 = tk.Label(bottom_frame, text="Bottom Frame", bg="lightgreen")
label2.pack(padx=10, pady=10)
root.mainloop()
