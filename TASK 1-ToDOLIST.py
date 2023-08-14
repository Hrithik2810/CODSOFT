import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(todo, root):
        todo.root = root
        todo.root.title("To-Do List App")
        todo.root.config(background="#353935")

        todo.tasks = []

        todo.title=tk.Label(root,text="ToDo List",font=("Ink Free",40,"bold"),background="#097969",width=30)
        todo.title.pack()

        todo.task_entry = tk.Entry(root, font=("Lucida Console",15), width=40,highlightbackground="Black",highlightcolor="Aqua",fg="White",background="#36454F",)
        todo.task_entry.pack(pady=10)
        
        todo.add_button = tk.Button(root, text="Add Task", font=("Comic Sans MS",15), command=todo.add_task,background="#28282B",highlightbackground="Black",fg="White")
        todo.add_button.pack()

        todo.task_listbox = tk.Listbox(root, font=("Lucida Console",15), width=50, height=10,highlightbackground="Black",highlightcolor="#1F51FF",background="#36454F",fg="White")
        todo.task_listbox.pack(pady=10)

        button_frame = tk.Frame(root, background="#353935")
        button_frame.pack()

        todo.complete_button = tk.Button(button_frame, text="Mark as Completed", font=("Comic Sans MS",15), command=todo.mark_completed,background="#28282B",fg="White")
        todo.complete_button.pack(side=tk.LEFT, padx=5, pady=5)

        todo.edit_button = tk.Button(button_frame, text="Edit Task", font=("Comic Sans MS",15), command=todo.edit_task,background="#28282B",fg="White")
        todo.edit_button.pack(side=tk.LEFT, padx=5,pady=5)
        
        todo.delete_button = tk.Button(button_frame, text="Delete Task", font=("Comic Sans MS",15), command=todo.delete_task,background="#28282B",fg="White")
        todo.delete_button.pack(side=tk.LEFT, padx=5,pady=9)
        
        
        
    def add_task(todo):
        task = todo.task_entry.get()
        if task:
            todo.tasks.append(task)
            todo.update_listbox()
            todo.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def update_listbox(todo):
        todo.task_listbox.delete(0, tk.END)
        for task in todo.tasks:
            todo.task_listbox.insert(tk.END, task)
            
    def edit_task(todo):
        selected_task = todo.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=todo.tasks[index],)
            if new_task:
                todo.tasks[index] = new_task
                todo.update_listbox()
            
    def mark_completed(todo):
        selected_task = todo.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            todo.tasks[index] = "✔ " + todo.tasks[index]
            todo.update_listbox()
            
    def delete_task(todo):
        selected_task = todo.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            del todo.tasks[index]
            todo.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
