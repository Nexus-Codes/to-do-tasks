from tkinter import *

root = Tk()

# Restore previous tasks from a file and display them
def load_tasks():
    try:
        with open("tasks.txt", "r") as tasks_file:
            for line in tasks_file:
                add_task_to_ui(line.strip())
    except FileNotFoundError:
        # No tasks file found, so nothing to load
        pass

# Save the current task to the file
def tasks_save(task):
    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(task +"\n")  # Add newline for each task

# Add a task to the UI
def add_task_to_ui(task):
    if task.strip() == "":
        return

    tasks_frame = Frame(root, bg="#e8e8e8")
    tasks_frame.pack(pady=5, padx=80, fill=X)

    # Checkbox
    checkbox_var = IntVar()
    checkbox = Checkbutton(tasks_frame, variable=checkbox_var, bg="#e8e8e8", relief="flat",
                            highlightbackground="black", highlightthickness=2)
    checkbox.pack(side=LEFT)
    checkbox.config(font=("verdana", 14))

    task_label = Label(tasks_frame, text=task, bg="#e8e8e8")
    task_label.pack(anchor='w', padx=(12), pady=(10), side=LEFT)
    task_label.config(font=("verdana", 12))

    # Delete button
    delete_btn = Button(tasks_frame, text="Delete", fg="white", command=lambda: on_delete_btn(tasks_frame, task))
    delete_btn.pack(side=RIGHT, padx=(0, 10))
    delete_btn.config(background="red", font=("verdana", 10))

# Delete the task frame and remove from the file
def on_delete_btn(frame, task):
    frame.destroy()
    # Remove the task from the file
    remove_task_from_file(task)

# Remove the task from the file
def remove_task_from_file(task):
    try:
        with open("tasks.txt", "r") as tasks_file:
            lines = tasks_file.readlines()
        with open("tasks.txt", "w") as tasks_file:
            for line in lines:
                if line.strip() != task:
                    tasks_file.write(line)
    except FileNotFoundError:
        pass

# Button click handler
def on_btn_click():
    task = task_input.get()
    if task.strip() == "":
        return

    tasks_save(task)
    add_task_to_ui(task)
    task_input.delete(0, END)

# Initialize the main window
root.title("To Do Lists")
root.geometry('730x470')
root.configure(background="#f3f3f3")
root.resizable(0, 0)

to_do_tasks = Label(root, text="To Do Tasks", fg="black", bg="#f3f3f3")
to_do_tasks.pack(pady=(20, 1), padx=(86, 10), anchor="w")
to_do_tasks.config(font=("verdana", 18))

input_frame = Frame(root, background="#f3f3f3")
input_frame.pack(pady=(10, 30), padx=(86, 10), fill=X)

task_input = Entry(input_frame)
task_input.pack(side=LEFT, padx=(0, 40), ipadx=120, ipady=7)
task_input.config(font=("verdana", 12), relief="flat", highlightbackground="black", highlightthickness=2)

add_btn = Button(input_frame, text="Add", bg="#73f255", relief="flat", command=on_btn_click, highlightcolor="black", highlightthickness=2)
add_btn.pack(side=LEFT, ipadx=13, ipady=3)
add_btn.config(font=("verdana", 14))

root.bind('<Return>', lambda event: on_btn_click())

# Load existing tasks when the application starts
load_tasks()

root.mainloop()
