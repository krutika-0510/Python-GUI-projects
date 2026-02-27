import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os
from datetime import datetime

FILENAME = "smart_tasks_gui.json"

# Load tasks
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

# Save tasks
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Refresh task list
def refresh_list():
    task_list.delete(0, tk.END)
    today = datetime.today().date()

    for task in tasks:
        try:
            # Try YYYY-MM-DD format
            due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        except ValueError:
            try:
                # Try DD-MM-YYYY format
                due = datetime.strptime(task["due_date"], "%d-%m-%Y").date()
            except ValueError:
                due = today  # fallback if completely wrong format

        status = task["status"]

        if status != "Completed" and due < today:
            status = "OVERDUE"

        display_text = f"{task['title']} | {task['category']} | {task['priority']} | {task['due_date']} | {status}"
        task_list.insert(tk.END, display_text)

# Add task
def add_task():
    title = title_entry.get()
    category = category_combo.get()
    priority = priority_combo.get()
    due_date = due_entry.get()

    if not title or not due_date:
        messagebox.showerror("Error", "Please fill all required fields")
        return

    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks()
    refresh_list()
    clear_fields()

# Clear input fields
def clear_fields():
    title_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)

# Delete task
def delete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task to delete")
        return
    tasks.pop(selected[0])
    save_tasks()
    refresh_list()

# Mark complete
def mark_complete():
    selected = task_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a task")
        return
    tasks[selected[0]]["status"] = "Completed"
    save_tasks()
    refresh_list()

# Search task
def search_task():
    keyword = search_entry.get().lower()
    task_list.delete(0, tk.END)

    for task in tasks:
        if keyword in task["title"].lower():
            display_text = f"{task['title']} | {task['category']} | {task['priority']} | {task['due_date']} | {task['status']}"
            task_list.insert(tk.END, display_text)

# Productivity score
def show_score():
    if not tasks:
        messagebox.showinfo("Score", "No tasks available")
        return

    completed = sum(1 for t in tasks if t["status"] == "Completed")
    total = len(tasks)
    percent = (completed / total) * 100

    messagebox.showinfo("Productivity Score", f"Completed: {completed}/{total}\nScore: {percent:.2f}%")

# GUI Window
root = tk.Tk()
root.title("SMART PRODUCTIVITY MANAGER")
root.geometry("850x600")
root.config(bg="#f0f4f7")

tasks = load_tasks()

# Title Label
tk.Label(root, text="SMART PRODUCTIVITY MANAGER", font=("Arial", 18, "bold"), bg="#f0f4f7").pack(pady=10)

# Frame for inputs
input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Task Title:", bg="#f0f4f7").grid(row=0, column=0, padx=5)
title_entry = tk.Entry(input_frame, width=25)
title_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Category:", bg="#f0f4f7").grid(row=0, column=2, padx=5)
category_combo = ttk.Combobox(input_frame, values=["Study", "Work", "Personal"], width=15)
category_combo.grid(row=0, column=3, padx=5)
category_combo.current(0)

tk.Label(input_frame, text="Priority:", bg="#f0f4f7").grid(row=1, column=0, padx=5)
priority_combo = ttk.Combobox(input_frame, values=["High", "Medium", "Low"], width=15)
priority_combo.grid(row=1, column=1, padx=5)
priority_combo.current(1)

tk.Label(input_frame, text="Due Date (YYYY-MM-DD):", bg="#f0f4f7").grid(row=1, column=2, padx=5)
due_entry = tk.Entry(input_frame, width=15)
due_entry.grid(row=1, column=3, padx=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", width=15, command=add_task, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Complete", width=15, command=mark_complete, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Task", width=15, command=delete_task, bg="#f44336", fg="white").grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Show Score", width=15, command=show_score, bg="#9C27B0", fg="white").grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root, bg="#f0f4f7")
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search Task:", bg="#f0f4f7").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame, width=25)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_task, bg="#607D8B", fg="white").pack(side=tk.LEFT)

# Task List
task_list = tk.Listbox(root, width=120, height=15)
task_list.pack(pady=15)

refresh_list()

root.mainloop()
