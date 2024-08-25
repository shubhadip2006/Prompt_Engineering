import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator != 0:
            result = float(entry1.get()) / denominator
            label_result.config(text=f"Result: {result}")
        else:
            messagebox.showerror("Math error", "Division by zero is not allowed")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button_add = tk.Button(root, text="Add", command=add)
button_add.pack()

button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.pack()

button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Start the Tkinter event loop
root.mainloop()
