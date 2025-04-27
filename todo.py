import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import datetime

# Save and Load tasks from file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            loaded = f.readlines()
            for task in loaded:
                tasks.append(task.strip())
            update_listbox()
    except FileNotFoundError:
        pass  # No tasks file yet

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    date = cal.get_date()
    time = time_var.get()
    if task != "":
        full_task = f"{task} | 📅 {date} ⏰ {time}"
        tasks.append(full_task)
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task_name = tasks[selected]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete '{task_name}'?")
        if confirm:
            del tasks[selected]
            update_listbox()
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected]
        if not task.startswith("✔️ "):
            tasks[selected] = "✔️ " + task
        else:
            tasks[selected] = task.replace("✔️ ", "")
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

def clear_tasks():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete ALL tasks?")
    if confirm:
        tasks.clear()
        update_listbox()
        save_tasks()

# Main window setup
root = tk.Tk()
root.title("📝 To-Do List with Date & Time")
root.geometry("400x600")
root.configure(bg="#2c3e50")

tasks = []

# Entry widget
entry = tk.Entry(root, width=28, font=("Helvetica", 14), bg="#34495e", fg="white", bd=0, insertbackground="white")
entry.pack(pady=10)

# Calendar Widget
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd", background="#34495e", foreground="white", headersbackground="#2c3e50", normalbackground="#34495e", weekendbackground="#34495e", selectbackground="#1abc9c")
cal.pack(pady=10)

# Time Picker
time_var = tk.StringVar()
time_combo = ttk.Combobox(root, textvariable=time_var, values=[f"{h:02d}:{m:02d}" for h in range(24) for m in (0, 30)], font=("Helvetica", 12))
time_combo.set(datetime.datetime.now().strftime("%H:00"))  # Default current hour
time_combo.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", width=12, font=("Helvetica", 11), bg="#27ae60", fg="white", bd=0, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=12, font=("Helvetica", 11), bg="#e74c3c", fg="white", bd=0, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

done_btn = tk.Button(button_frame, text="Mark Done", width=26, font=("Helvetica", 11), bg="#3498db", fg="white", bd=0, command=mark_done)
done_btn.grid(row=1, column=0, columnspan=2, pady=5)

clear_btn = tk.Button(root, text="Clear All Tasks", width=30, font=("Helvetica", 11), bg="#f39c12", fg="white", bd=0, command=clear_tasks)
clear_btn.pack(pady=10)

# Listbox
listbox = tk.Listbox(root, width=50, height=12, font=("Helvetica", 11), bg="#34495e", fg="white", selectbackground="#1abc9c", bd=0)
listbox.pack(pady=10)

# Load existing tasks
load_tasks()

# Hover Effects
def on_enter(e):
    e.widget['bg'] = '#1abc9c'

def on_leave(e):
    e.widget['bg'] = button_original_colors[e.widget]

button_original_colors = {
    add_btn: "#27ae60",
    delete_btn: "#e74c3c",
    done_btn: "#3498db",
    clear_btn: "#f39c12"
}

for button in button_original_colors:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Start mainloop
root.mainloop()
