import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Create a basic GUI window
root = tk.Tk()
root.title("To-Do List")

# Create and pack the task entry field with a default placeholder text
default_text = "Add Task..."
entry = tk.Entry(root, width=40)
entry.insert(0, default_text)
entry.bind("<FocusIn>", lambda event: entry.delete(0, "end"))  # Clear the default text when focused
entry.pack(pady=10)

# Create and pack the task list
task_list = tk.Listbox(root, width=40)
task_list.pack()

# Create "Add" and "Delete" buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
add_button.pack()
delete_button.pack()

# Start the main event loop
root.mainloop()
