import tkinter as tk
from tkinter import messagebox


def show_message():
    text = textbox.get("1.0", "end-1c")
    messagebox.showinfo("textbox.text=", text)


root = tk.Tk()
root.title("First GUI APP")
textbox = tk.Text(root, height=5, width=30)
button = tk.Button(root, text="Show text", command=show_message)
textbox.pack(pady=10)
button.pack(pady=5)
root.mainloop()
