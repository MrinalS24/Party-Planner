import tkinter as tk
from tkinter import ttk
from budgeting import budgeting_window
from menu import menu_window
from check_list import checklist_window



total_people = 0
guest_list = {}

status_var = None
name_entry = None
no_people_spinbox = None
guest_listbox = None
total_people_label = None
guest_window = None

no_people = 0




def add_people():
    global status_var, name_entry, no_people_spinbox, total_people, guest_list, guest_listbox, no_people_var, total_people_label, no_people

    name = name_entry.get()
    rsvp_status = status_var.get()
    no_people = no_people_var.get()

    if name not in guest_list:
        guest_listbox.insert(tk.END, name)
    
    if name in guest_list:
        total_people -= guest_list[name][1]

    total_people += no_people    

    guest_list[name] = [rsvp_status, no_people]
    print(guest_list)

    name_entry.delete(0, tk.END)
    no_people_var.set(1)

    total_people_label.config(text = f"Total No. of People: {total_people}")

    


def delete_people():
    global no_people_spinbox, guest_list, total_people, total_people_label, guest_listbox, no_people

    selected_index = guest_listbox.curselection()
    guest_listbox.delete(selected_index)
    
    total_people -= no_people
    total_people_label.config(text = f"Total No. of People: {total_people}")


def show_details(event):
    global guest_list, guest_listbox, guest_window

    show_details_window = tk.Toplevel(guest_window)
    show_details_window.geometry("100x100")
    show_details_window.config(bg = "white")

    index = guest_listbox.curselection()[0]

    name = guest_listbox.get(index)
    no_of_people = guest_list[name][1]
    status = guest_list[name][0]

    name_label = tk.Label(show_details_window, text = f"Name: {name}", font = ("Times New Roman", 13), fg = "black", bg = "white")
    name_label.place(x = 5, y = 5)

    no_people_label = tk.Label(show_details_window, text = f"No. of People: {no_of_people}", font = ("Times New Roman", 13), fg = "black", bg = "white")
    no_people_label.place(x = 5, y = 30)

    status_label = tk.Label(show_details_window, text = f"Status: {status}", font = ("Times New Roman", 13), fg = "black", bg = "white")
    status_label.place(x = 5, y = 55)

    show_details_window.mainloop()


















def open_guest_window():
    global status_var, name_entry, no_people_spinbox, total_people, guest_listbox, total_people_label, guest_window

    guest_window = tk.Toplevel(window)
    guest_window.title("Guest List Window")
    guest_window.geometry("500x500")
    guest_window.config(bg = "#FDFD96")

    guest_listbox = tk.Listbox(guest_window, width = 30, height = 20, font = ("Times New Roman", 15), fg = "black", bg = "white")
    guest_listbox.place(x = 20, y = 20)

    guest_listbox.bind("<<ListboxSelect>>", show_details)

    for i in guest_list.keys():
        guest_listbox.insert(tk.END, i)

    name_label = tk.Label(guest_window, text = "Enter Guest Name:", fg = "black", bg = "#FDFD96", font = ("Times New Roman", 18))
    name_label.place(x = 280, y = 30)

    name_entry = tk.Entry(guest_window, width = 20, fg = "black", bg = "white", font = ("Times New Roman", 18), bd = 4, relief = tk.SUNKEN)
    name_entry.place(x = 280, y = 65)

    rsvp_label = tk.Label(guest_window, text = "Choose invite status:", fg = "black", bg = "#FDFD96", font = ("Times New Roman", 18))
    rsvp_label.place(x = 280, y = 125)

    status_var = tk.StringVar(value = "Unconfirmed")

    accepted_button = tk.Radiobutton(guest_window, text = "Confirmed", fg = "black", bg = "#FDFD96", variable = status_var, value = "Confirmed", font = ("Times New Roman", 18))
    accepted_button.place(x = 280, y = 155)

    unconfirmed_button = tk.Radiobutton(guest_window, text = "Unconfirmed", fg = "black", bg = "#FDFD96", variable = status_var, value = "Unconfirmed", font = ("Times New Roman", 18))
    unconfirmed_button.place(x = 280, y = 190)

    no_people_label = tk.Label(guest_window, text = "No. of People:", fg = "black", bg = "#FDFD96", font = ("Times New Roman", 18))
    no_people_label.place(x = 280, y = 265)

    no_people_spinbox = tk.Spinbox(guest_window, from_ = 1, to = 10, fg = "black", bg = "white", font = ("Times New Roman", 18), width = 15, textvariable = no_people_var)
    no_people_spinbox.place(x = 280, y = 295)

    add_button = tk.Button(guest_window, text = "Add", fg = "black", bg = "white", bd = 4, relief = tk.GROOVE, font = ("Times New Roman", 18), command = add_people)
    add_button.place(x = 280, y = 360)

    delete_button = tk.Button(guest_window, text = "Delete", fg = "black", bg = "white", bd = 4, relief = tk.GROOVE, font = ("Times New Roman", 18), command = delete_people)
    delete_button.place(x = 380, y = 360)

    total_people_label = tk.Label(guest_window, text = f"Total No. of People: {total_people}", fg = "black", bg = "#FDFD96", bd = 2, relief = tk.SUNKEN, font = ("Times New Roman", 20), width = 22)
    total_people_label.place(x = 28, y = 420)








    





window = tk.Tk()
window.geometry("600x500")
window.config(bg = "#ffd1f4")
window.title("Party Planner")

no_people_var = tk.IntVar(value = 1)

streamer_img = tk.PhotoImage(file = "streamers.png") #loading images
money_img = tk.PhotoImage(file = "money.png")

streamer_img_label = tk.Label(window, image = streamer_img, bg = "#ffd1f4")
streamer_img_label.pack()




planner_label = tk.Label(window, text = "PARTY PLANNER", fg = "black", bg = "#ffd1f4", font = ("Times New Roman", 20))
planner_label.place(x = 230, y = 230)

guest_list_button = tk.Button(window, text = "GUEST LIST", fg = "black", bg = "white", font = ("Times New Roman", 20), command = open_guest_window)
guest_list_button.place(x = 235, y = 80)

checklist_button = tk.Button(window, text = "CHECKLIST", fg = "black", bg = "white", font = ("Times New Roman", 20), command = checklist_window)
checklist_button.place(x = 230, y = 380)

budget_button = tk.Button(window, text = "BUDGETING", fg = "black", bg = "white", font = ("Times New Roman", 20), command = budgeting_window)
budget_button.place(x = 15, y = 230)

food_button = tk.Button(window, text = "MENU", fg = "black", bg = "white", font = ("Times New Roman", 20), command = menu_window)
food_button.place(x = 480, y = 230)

# to add an image in a button, add a property "image" and put in the image variable as loaded onto the file. 




window.mainloop()

