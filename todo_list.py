from tkinter import *

root = Tk()
root.geometry("445x525")
root.resizable(False, False)
root.config(bg="#030B1B")
root.title("TODO LIST APP")


# ================= TITLE BAR =================

title_bar = Frame(root, bg="#061426", height=40)
title_bar.pack(fill="x")

app_title = Label(
    title_bar,
    text="▣  TODO LIST APP",
    font=("Arial", 10, "bold"),
    bg="#061426",
    fg="#EFF2FC"
)
app_title.pack(side="left", padx=0, pady=0)


# ================= HEADER =================

header = Frame(root, bg="#030B1B")
header.pack(pady=25)

logo = Label(
    header,
    text="☑",
    font=("Arial", 45, "bold"),
    bg="#030B1B",
    fg="#00D9FF"
)
logo.pack(side="left", padx=10)

header_text = Frame(header, bg="#030B1B")
header_text.pack(side="left")

title = Label(
    header_text,
    text="TODO LIST",
    font=("Arial", 30, "bold"),
    bg="#030B1B",
    fg="#EFF2FC"
)
title.pack(anchor="w")

subtitle = Label(
    header_text,
    text="Small Tasks  •  Big Goals",
    font=("Arial", 11),
    bg="#030B1B",
    fg="#92CFFE"
)
subtitle.pack(anchor="w")


task_items = []

task_text = ""

selected_task = ""

def add_task():
    task_text = task_entry.get()

    if task_text.strip()== " ":
        return
    task_items.append(task_text)
    task_list.insert(END,task_items)
    print(task_items)

def delete_task():
    selected_indexes = task_list.curselection()

    if  not selected_indexes :
        return
    selected_index = selected_indexes[0]
    selected_task = task_list.get(selected_index)

    for selected_task in task_items:
      task_items.remove(selected_task)
      task_list.delete(selected_index)





# ================= INPUT AREA =================

task_entry = Entry(
    root,
    font=("Arial", 13),
    bg="#061A3A",
    fg="white",
    insertbackground="white",
    bd=0
)

task_entry.place(
    x=35,
    y=130,
    width=380,
    height=42
)


# ================= ADD BUTTON =================

add_task_button = Button(
    root,
    text="+  Add Task",
    font=("Arial", 12, "bold"),
    bg="#168CFF",
    fg="white",
    bd=0,
    activebackground="#00BFFF",
    activeforeground="white",
    command=add_task

)

add_task_button.place(
    x=35,
    y=185,
    width=380,
    height=42
)


# ================= TASK HEADING =================

task_heading = Label(
    root,
    text="☷  Your Tasks:",
    font=("Arial", 15, "bold"),
    bg="#030B1B",
    fg="#EFF2FC"
)

task_heading.place(
    x=35,
    y=245
)


# ================= LISTBOX FRAME =================

task_frame = Frame(
    root,
    bg="#061A3A",
    highlightbackground="#00AFFF",
    highlightthickness=1
)

task_frame.place(
    x=35,
    y=280,
    width=380,
    height=170
)


# ================= LISTBOX =================

task_list = Listbox(
    task_frame,
    font=("Consolas", 12, "bold"),
    bg="#061A3A",
    fg="#EFF2FC",
    selectbackground="#168CFF",
    selectforeground="white",
    bd=0,
    highlightthickness=0
)

task_list.pack(
    fill="both",
    expand=True,
    padx=0,
    pady=0
)


# Sample tasks — layout testing ke liye
task_list.insert(END, task_items)


# ================= DELETE BUTTON =================

delete_button = Button(
    root,
    text="🗑  Delete Selected",
    font=("Arial", 11, "bold"),
    bg="#061A3A",
    fg="#00D9FF",
    bd=0,
    activebackground="#168CFF",
    activeforeground="white",
    command=delete_task
)

delete_button.place(
    x=270,
    y=480,
    width=145,
    height=38
)


root.mainloop()