# Импортируем модули
import ttkbootstrap as ttk
import json
from tkinter import Listbox


with open("tasks.json", 'r', encoding="utf-8") as json_file:
    tasks = json.load(json_file)

def add_task(event):
    text = add_entry.get()
    if text:
        tasks["To do"].append(text)
        to_do.insert("end", text)
        add_entry.delete(0, "end")
    save()

def move_task(evente, source_list, target_list=None):
    selected = source_list.curselection()
    if target_list:
        target_list.insert("end", source_list.get(selected))
    source_list.delete(selected)
    save()

def save():
    tasks = {
        "To do": to_do.get(0, "end"),
        "In progress": in_progres.get(0, "end"),
        "Done": done.get(0, "end")
    }
    with open("tasks.json", 'w', encoding="utf-8") as json_file:
        json.dump(tasks, json_file, ensure_ascii=False)

root = ttk.Window(themename="superhero")
root.resizable(0, 0)
root.configure(padx=10, pady=10)
root.title("Менеджер задач.")

to_do = Listbox(root, width=30)
to_do.grid(column=0, row=1, padx=(0, 30))

label_to_do = ttk.Label(root, text="To do", style="danger")
label_to_do.grid(column=0, row=0)


in_progres = Listbox(root, width=30)
in_progres.grid(column=1, row=1, padx=(0, 30))

label_in_progres = ttk.Label(root, text="In progress", style="warning")
label_in_progres.grid(column=1, row=0)

done = Listbox(root, width=30)
done.grid(column=2, row=1)

label_done = ttk.Label(root, text="Done", style="success")
label_done.grid(column=2, row=0)

add_label = ttk.Label(root, text="Add task: ", style="primary")
add_label.grid(column=0, row=2, pady=(20, 0))

add_entry = ttk.Entry(root, textvariable="Enter text to add a task")
add_entry.grid(column=1, row=2, pady=(20, 0))

add_button = ttk.Button(root, text="Press Enter or this button to add task.", style="primary")
add_button.grid(column=2, row=2, pady=(20, 0))

add_entry.bind("<Return>", add_task)
add_button.bind("<Button-1>", add_task)
to_do.bind("<Double-Button-1>", lambda event: move_task(event, to_do, in_progres))
in_progres.bind("<Double-Button-1>", lambda event: move_task(event, in_progres, done))
done.bind("<Double-Button-1>", lambda event: move_task(event, done))


for task in tasks["To do"]:
    to_do.insert("end", task)


for task in tasks["In progress"]:
    in_progres.insert("end", task)


for task in tasks["Done"]:
    done.insert("end", task)

"""Сохраняем в файл записи при закрытии окна
root.protovol("WM_DELETE_WINDOW", save())
Обязательно пишем так:
def save():
  . . . . . . . 
  . . . . . . . 
  root.destroy()        !!!!!!!!!!!!!!!"""
root.mainloop()