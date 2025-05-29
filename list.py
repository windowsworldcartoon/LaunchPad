import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import time
__version__ = "1.0.0"


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create text entry field
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack()

        # Create add task button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        # Create listbox to display tasks
        self.task_list = tk.Listbox(self.root, width=40)
        self.task_list.pack()

        # Create delete task button
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        # Create save tasks button
        self.save_tasks_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_button.pack()

    def check_for_updates(self):
        # Coming soon
        pass

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except:
            pass

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            tasks = [self.task_list.get(i) for i in range(self.task_list.size())]
            with open(file_path, "w") as file:
                for task in tasks:
                    file.write(task + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()