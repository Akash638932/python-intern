import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        # Create GUI elements
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.RIGHT, padx=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'description': task, 'completed': False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
        
    def complete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = True
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to complete.")
        
    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")
        
    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = 'Done' if task['completed'] else 'Pending'
            self.tasks_listbox.insert(tk.END, f"{task['description']} - {status}")

if __name__ == "__main__":
    root = tk.Tk(23)
    app = ToDoApp(root)
    root.mainloop(20)
