import tkinter as tk
from tkinter import messagebox

# ==============================
# ENHANCED BASIC CALCULATOR
# ==============================

dark_mode = True

# ---------- FUNCTIONS ----------

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        history.insert(tk.END, f"{expression} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Expression")

# ---------- THEME ----------

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        bg = "#1e1e2f"
        btn = "#2c2c3c"
        fg = "white"
    else:
        bg = "#f0f0f0"
        btn = "#dddddd"
        fg = "black"

    root.config(bg=bg)
    entry.config(bg=btn, fg=fg)

    for b in all_buttons:
        b.config(bg=btn, fg=fg, activebackground="#555")

# ---------- WINDOW ----------

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("400x550")
root.resizable(False, False)

# Display
entry = tk.Entry(root, font=("Arial", 28), bd=8, relief="ridge", justify="right")
entry.pack(fill="x", padx=10, pady=15)

# Theme Button
tk.Button(root, text="🌗 Toggle Theme", command=toggle_theme).pack(pady=5)

# Main Frame
frame = tk.Frame(root)
frame.pack()

# Button Layout (Only Basic Operations)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "←", "+"],
    ["C", "="]
]

all_buttons = []

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = calculate
        elif text == "C":
            cmd = clear
        elif text == "←":
            cmd = backspace
        else:
            cmd = lambda t=text: click(t)

        btn = tk.Button(
            frame,
            text=text,
            width=6,
            height=2,
            font=("Arial", 16),
            command=cmd
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
        all_buttons.append(btn)

# History Panel
tk.Label(root, text="History", font=("Arial", 12)).pack(pady=5)

history = tk.Listbox(root, height=6)
history.pack(fill="both", padx=10)

# Keyboard Support
def key_input(event):
    if event.char in "0123456789+-*/.":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()

root.bind("<Key>", key_input)

apply_theme()

root.mainloop()
