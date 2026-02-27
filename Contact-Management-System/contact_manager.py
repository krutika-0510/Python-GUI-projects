import tkinter as tk
from tkinter import messagebox
import uuid

# ==============================
# PROFESSIONAL CONTACT MANAGER
# ==============================

contacts = []
selected_contact_id = None


# ---------- FUNCTIONS ----------

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required")
        return

    contact = {
        "id": str(uuid.uuid4()),  # unique ID
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    refresh_list()
    clear_fields()


def refresh_list(filtered=None):
    contact_list.delete(0, tk.END)

    data = filtered if filtered else contacts

    for contact in data:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def search_contact():
    query = search_entry.get().lower()

    filtered = [
        contact for contact in contacts
        if query in contact["name"].lower()
        or query in contact["phone"]
    ]

    refresh_list(filtered)


def select_contact(event):
    global selected_contact_id

    selected = contact_list.curselection()
    if not selected:
        return

    index = selected[0]
    selected_text = contact_list.get(index)

    name, phone = selected_text.split(" - ")

    for contact in contacts:
        if contact["name"] == name and contact["phone"] == phone:
            selected_contact_id = contact["id"]

            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)

            name_entry.insert(0, contact["name"])
            phone_entry.insert(0, contact["phone"])
            email_entry.insert(0, contact["email"])
            address_entry.insert(0, contact["address"])
            break


def update_contact():
    global selected_contact_id

    if not selected_contact_id:
        messagebox.showerror("Error", "Select a contact first")
        return

    for contact in contacts:
        if contact["id"] == selected_contact_id:
            contact["name"] = name_entry.get()
            contact["phone"] = phone_entry.get()
            contact["email"] = email_entry.get()
            contact["address"] = address_entry.get()
            break

    refresh_list()
    clear_fields()
    selected_contact_id = None


def delete_contact():
    global selected_contact_id

    if not selected_contact_id:
        messagebox.showerror("Error", "Select a contact first")
        return

    contacts[:] = [
        contact for contact in contacts
        if contact["id"] != selected_contact_id
    ]

    refresh_list()
    clear_fields()
    selected_contact_id = None


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# ---------- UI ----------

root = tk.Tk()
root.title("Smart Contact Manager")
root.geometry("750x500")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

tk.Label(root, text="📇 Smart Contact Manager",
         font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="cyan").pack(pady=15)

main_frame = tk.Frame(root, bg="#1e1e2f")
main_frame.pack()

# Left Form
form_frame = tk.Frame(main_frame, bg="#1e1e2f")
form_frame.grid(row=0, column=0, padx=30)

def create_label(text):
    return tk.Label(form_frame, text=text, bg="#1e1e2f", fg="white")

create_label("Name").pack()
name_entry = tk.Entry(form_frame, width=30)
name_entry.pack(pady=5)

create_label("Phone").pack()
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.pack(pady=5)

create_label("Email").pack()
email_entry = tk.Entry(form_frame, width=30)
email_entry.pack(pady=5)

create_label("Address").pack()
address_entry = tk.Entry(form_frame, width=30)
address_entry.pack(pady=5)

tk.Button(form_frame, text="Add", width=20, command=add_contact).pack(pady=5)
tk.Button(form_frame, text="Update", width=20, command=update_contact).pack(pady=5)
tk.Button(form_frame, text="Delete", width=20, command=delete_contact).pack(pady=5)

# Right List
list_frame = tk.Frame(main_frame, bg="#1e1e2f")
list_frame.grid(row=0, column=1, padx=30)

tk.Label(list_frame, text="Search",
         bg="#1e1e2f", fg="white").pack()

search_entry = tk.Entry(list_frame, width=30)
search_entry.pack(pady=5)

tk.Button(list_frame, text="Search", command=search_contact).pack(pady=5)
tk.Button(list_frame, text="Show All", command=lambda: refresh_list()).pack(pady=5)

contact_list = tk.Listbox(list_frame, width=40, height=15)
contact_list.pack(pady=10)

contact_list.bind("<<ListboxSelect>>", select_contact)

root.mainloop()
