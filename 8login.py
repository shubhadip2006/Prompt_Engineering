import tkinter as tk
from tkinter import messagebox

# Function to handle sign-in
def sign_in():
    global username, password
    username = entry_username_signin.get()
    password = entry_password_signin.get()
    if username and password:
        messagebox.showinfo("Sign-In", "Sign-in SUCCESSFUL!")
    else:
        messagebox.showwarning("Sign-In", "Please enter both username and password.")

# Function to handle login
def login():
    u = entry_username_login.get()
    p = entry_password_login.get()
    if u == username and p == password:
        messagebox.showinfo("Login", "Login SUCCESSFUL!")
    else:
        messagebox.showerror("Login", "Login NOT Successful")

# Create the main window
root = tk.Tk()
root.title("Sign-In & Login Page")

# Sign-In Section
tk.Label(root, text="Welcome to Sign-In Page:", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Username:").pack()
entry_username_signin = tk.Entry(root)
entry_username_signin.pack()

tk.Label(root, text="Password:").pack()
entry_password_signin = tk.Entry(root, show="*")
entry_password_signin.pack()

tk.Button(root, text="Sign-In", command=sign_in).pack(pady=10)

# Separator
tk.Label(root, text="").pack()  # Empty label for spacing

# Login Section
tk.Label(root, text="Welcome to Login Page:", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Username:").pack()
entry_username_login = tk.Entry(root)
entry_username_login.pack()

tk.Label(root, text="Password:").pack()
entry_password_login = tk.Entry(root, show="*")
entry_password_login.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

# Start the main loop
root.mainloop()
