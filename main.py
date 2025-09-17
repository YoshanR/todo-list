
# Main window creation
import tkinter as tk



root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")



# Add Task Function
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)



# Task entry

root.mainloop()

