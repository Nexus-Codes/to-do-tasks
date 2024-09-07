from tkinter import *

root = Tk()

#functionality of delete btn
def on_delete_btn(frame):
    frame.destroy()

def on_btn_click():
    task = task_input.get()

    if task.strip() == "":
        return
    tasks_frame = Frame(root, bg="#e8e8e8")
    tasks_frame.pack(pady=5, padx=80, fill=X)

    #checkbox
    checkbox_var = IntVar()
    checkbox = Checkbutton(tasks_frame, variable=checkbox_var, bg="#e8e8e8", relief="flat", \
                            highlightbackground="black", highlightthickness=2)
    checkbox.pack(side=LEFT)
    checkbox.config(font=("verdana", 14), )

    task1 = Label(tasks_frame, text=task, bg="#e8e8e8")
    task1.pack(anchor='w', padx=(12), pady=(10), side=LEFT)
    task1.config(font=("verdana", 12))
    task_input.delete(0, END)

    #delete btn
    delete_1 = Button(tasks_frame, text="Delete", fg="white", command=lambda: on_delete_btn(tasks_frame))
    delete_1.pack(side=RIGHT, padx=(0, 10))
    delete_1.config(background="red", font=("verdana", 10))



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



root.mainloop()
