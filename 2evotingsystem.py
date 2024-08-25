import tkinter as tk
from tkinter import messagebox

# Function to handle the voting process
def vote():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone = entry_phone.get()
    age = entry_age.get()

    if not first_name or not last_name or not phone or not age:
        messagebox.showwarning("Input Error", "Please fill all the fields")
        return

    try:
        age = int(age)
        phone = int(phone)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid numbers for Phone No. and Age")
        return

    if age < 18:
        messagebox.showinfo("Not Eligible", "NOT ELIGIBLE TO VOTE. Go Away...")
        return

    choice = selected_party.get()

    if choice == 1:
        messagebox.showinfo("Vote", "Vote sent to BJP...")
    elif choice == 2:
        messagebox.showinfo("Vote", "Vote sent to Cong...")
    elif choice == 3:
        messagebox.showinfo("Vote", "Vote sent to CPM...")
    else:
        messagebox.showwarning("Invalid Choice", "INVALID Choice...")

# Create the main window
root = tk.Tk()
root.title("Voting Page")
root.geometry("400x300")

# Create Labels and Entry widgets for user details
tk.Label(root, text="Welcome to the Voting Page", font=("Helvetica", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(frame)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(frame)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Phone No.:").grid(row=2, column=0, padx=10, pady=5)
entry_phone = tk.Entry(frame)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Age:").grid(row=3, column=0, padx=10, pady=5)
entry_age = tk.Entry(frame)
entry_age.grid(row=3, column=1, padx=10, pady=5)

# Voting Options
tk.Label(root, text="Please Select whom you want to Vote:", font=("Helvetica", 12)).pack(pady=10)

selected_party = tk.IntVar()
tk.Radiobutton(root, text="BJP", variable=selected_party, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="Cong", variable=selected_party, value=2).pack(anchor=tk.W)
tk.Radiobutton(root, text="CPM", variable=selected_party, value=3).pack(anchor=tk.W)

# Submit Button
tk.Button(root, text="Submit Vote", command=vote).pack(pady=20)

# Run the application
root.mainloop()