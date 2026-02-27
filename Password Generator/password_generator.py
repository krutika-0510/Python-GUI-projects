import tkinter as tk
from tkinter import messagebox
import random
import string

# ==============================
# SMART PERSONALIZED PASSWORD GENERATOR
# ==============================

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Length must be at least 4")
            return

        base_text = ""

        # Add name if provided
        if name_entry.get():
            base_text += name_entry.get()

        # Add date if provided
        if date_entry.get():
            base_text += date_entry.get()

        characters = ""

        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type")
            return

        # Generate random part
        remaining_length = length - len(base_text)

        if remaining_length < 0:
            messagebox.showerror("Error", "Length too short for given inputs")
            return

        random_part = ''.join(random.choice(characters) for _ in range(remaining_length))

        # Combine and shuffle
        final_password = list(base_text + random_part)
        random.shuffle(final_password)
        final_password = ''.join(final_password)

        result_entry.delete(0, tk.END)
        result_entry.insert(0, final_password)

    except:
        messagebox.showerror("Error", "Invalid Input")


def copy_password():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied!")


# ---------- WINDOW ----------
root = tk.Tk()
root.title("Smart Personalized Password Generator")
root.geometry("500x520")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 Smart Password Generator",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f", fg="cyan").pack(pady=15)

# Name Input
tk.Label(root, text="Enter Name (Optional)",
         bg="#1e1e2f", fg="white").pack()

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

# Date Input
tk.Label(root, text="Enter Important Date (Optional)",
         bg="#1e1e2f", fg="white").pack()

date_entry = tk.Entry(root, font=("Arial", 12))
date_entry.pack(pady=5)

# Length Input
tk.Label(root, text="Password Length",
         bg="#1e1e2f", fg="white").pack()

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar()

options_frame = tk.Frame(root, bg="#1e1e2f")
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Uppercase",
               variable=var_upper,
               bg="#1e1e2f", fg="white").grid(row=0, column=0, padx=10)

tk.Checkbutton(options_frame, text="Lowercase",
               variable=var_lower,
               bg="#1e1e2f", fg="white").grid(row=0, column=1, padx=10)

tk.Checkbutton(options_frame, text="Numbers",
               variable=var_digits,
               bg="#1e1e2f", fg="white").grid(row=1, column=0, padx=10)

tk.Checkbutton(options_frame, text="Symbols",
               variable=var_symbols,
               bg="#1e1e2f", fg="white").grid(row=1, column=1, padx=10)

# Generate Button
tk.Button(root, text="Generate Password",
          command=generate_password,
          bg="cyan", fg="black",
          font=("Arial", 12, "bold")).pack(pady=15)

# Result
result_entry = tk.Entry(root, font=("Consolas", 14), justify="center")
result_entry.pack(pady=10, fill="x", padx=40)

# Copy Button
tk.Button(root, text="Copy to Clipboard",
          command=copy_password).pack(pady=5)

root.mainloop()
