import tkinter as tk
from tkinter import ttk


def checklist_window():
    checklist_window = tk.Tk()
    checklist_window.geometry("500x500")
    checklist_window.config(bg = "#D1C1F2")
    checklist_window.title("Checklist Window")

    to_do_listbox = tk.Listbox(checklist_window, width = 30, height = 15, font = ("Times New Roman", 15), fg = "black", bg = "white")
    to_do_listbox.place(x = 20, y = 20)

    done_listbox = tk.Listbox(checklist_window, width = 30, height = 15, font = ("Times New Roman", 15), fg = "black", bg = "white")
    done_listbox.place(x = 270, y = 20)

    to_do_label = tk.Label(checklist_window, text = "Still To-Do", bg = "#D1C1F2", fg = "black", font = ("Times New Roman", 18))
    to_do_label.place(x = 50, y = 300)