import tkinter as tk
from tkinter import ttk


to_do_listbox = None
done_listbox = None
task_enter_button = None
task_entry = None
tasks_list = []
done_task = ""
done_tasks_list = []





def add_task():
    global to_do_listbox, done_listbox, task_enter_button, task_entry

    task = task_entry.get()

    tasks_list.append(task)
    final_of_task_list = len(tasks_list) - 1

    to_do_listbox.insert(tk.END, tasks_list[final_of_task_list])

    task_entry.delete(0, tk.END)


def change_task_status(event):
    global tasks_list, done_tasks_list, done_task, done_listbox, to_do_listbox
    index = to_do_listbox.curselection()

    to_do_listbox.delete(index[0])

    done_task = tasks_list.pop(index[0])

    done_tasks_list.append(done_task)
    final_of_done_task_list = len(done_tasks_list) -1

    done_listbox.insert(tk.END, done_tasks_list[final_of_done_task_list])









def checklist_window():
    global to_do_listbox, done_listbox, task_enter_button, task_entry, tasks_list, done_tasks_list

    checklist_window = tk.Toplevel()
    checklist_window.geometry("500x500")
    checklist_window.config(bg = "#D1C1F2")
    checklist_window.title("Checklist Window")

    to_do_listbox = tk.Listbox(checklist_window, width = 25, height = 15, font = ("Times New Roman", 15), fg = "black", bg = "white")
    to_do_listbox.place(x = 50, y = 20)

    to_do_listbox.bind("<Double-Button-1>", change_task_status)
    
    for i in tasks_list:
        to_do_listbox.insert(tk.END, i)


    done_listbox = tk.Listbox(checklist_window, width = 25, height = 15, font = ("Times New Roman", 15), fg = "black", bg = "white")
    done_listbox.place(x = 280, y = 20)

    for i in done_tasks_list:
        done_listbox.insert(tk.END, i)

    to_do_label = tk.Label(checklist_window, text = "Still To-Do", bg = "#D1C1F2", fg = "black", font = ("Times New Roman", 18))
    to_do_label.place(x = 100, y = 300)

    done_label = tk.Label(checklist_window, text = "Done", bg = "#D1C1F2", fg = "black", font = ("Times New Roman", 18))
    done_label.place(x = 360, y = 300)

    task_entry = tk.Entry(checklist_window, font = ("Times New Roman", 18), fg = "black", bg = "white", bd = 3, relief = tk.GROOVE)
    task_entry.place(x = 80, y = 350)

    task_enter_button = tk.Button(checklist_window, text = "Enter Task", font = ("Times New Roman", 18), fg = "black", bg = "#D1C1F2", bd = 3, relief = tk.SUNKEN, command = add_task)
    task_enter_button.place(x = 290, y = 350)

    helping_label = tk.Label(checklist_window, text = "*To change the status of the task from to-do to done, simply double-click on the task", font = ("Times New Roman", 13), fg = "black", bg = "#D1C1F2")
    helping_label.place(x = 30, y = 450)

