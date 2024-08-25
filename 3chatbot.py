import tkinter as tk
from tkinter import messagebox

def chatbot():
    user_response = entry.get().strip().lower()
    entry.delete(0, tk.END)  # Clear the input field after getting the response
    
    if user_response in ["good", "great", "nice", "happy", "fine", "fantastic", "wonderful", "amazing"]:
        response = "That's great! Enjoy your day."
    elif user_response in ["bad", "sad", "unhappy", "terrible", "awful", "not good", "depressed", "down"]:
        response = "That's okay! Don't be sad, things will get better!"
    elif user_response in ["okay", "so-so", "not bad", "meh", "alright", "fine, but could be better"]:
        response = "I see, just take it one step at a time."
    elif user_response in ["tired", "exhausted", "sleepy", "drained"]:
        response = "You should get some rest! Your body needs it."
    elif user_response in ["excited", "pumped", "thrilled", "energetic"]:
        response = "That's awesome! Keep that energy going!"
    elif user_response in ["anxious", "nervous", "worried", "stressed"]:
        response = "Try to take deep breaths and relax. You've got this!"
    else:
        response = "I didn't quite understand that. Sorry, next time!"
    
    messagebox.showinfo("CHATBOT", response)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create and place the label, entry, and button widgets
label = tk.Label(root, text="How are you?")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=chatbot)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()