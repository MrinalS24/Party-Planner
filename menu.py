import tkinter as tk
from tkinter import ttk



food_entry = None
food_type_var = None
v_nv_type_var = None




def add_food_item():
    global food_entry, food_type_var, v_nv_type_var

    food_name = food_entry.get()
    food_type = food_type_var.get()
    v_nv = v_nv_type_var









def menu_window():
    global food_entry, food_type_var, v_nv_type_var

    menu_window = tk.Tk()
    menu_window.title("Menu WIndow")
    menu_window.geometry("500x500")
    menu_window.config(bg = "#ACE1AF")


    food_listbox = tk.Listbox(menu_window, width = 30, height = 20, font = ("Times New Roman", 15), fg = "black", bg = "white")
    food_listbox.place(x = 20, y = 20)

    food_label = tk.Label(menu_window, text = "Enter Food Item:", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    food_label.place(x = 270, y = 30)

    food_entry = tk.Entry(menu_window, bg = "white", fg = "black", bd = 3, relief = tk.GROOVE, font = ("Times New Roman", 18))
    food_entry.place(x = 270, y = 60)

    food_type_var = tk.StringVar(value = "Mains")

    drink_button = tk.Radiobutton(menu_window, text = "Drinks", variable = food_type_var, value = "Drinks", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    drink_button.place(x = 270, y = 100)

    mains_button = tk.Radiobutton(menu_window, text = "Mains", variable = food_type_var, value = "Mains", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    mains_button.place(x = 270, y = 130)

    snacks_button = tk.Radiobutton(menu_window, text = "Snacks", variable = food_type_var, value = "Snacks", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    snacks_button.place(x = 270, y = 160)

    dessert_button = tk.Radiobutton(menu_window, text = "Dessert", variable = food_type_var, value = "Dessert", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    dessert_button.place(x = 270, y = 190)

    v_nv_type_var = tk.StringVar(value = "Veg")

    veg_button = tk.Radiobutton(menu_window, text = "Vegetarian", variable = v_nv_type_var, value = "Veg", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    veg_button.place(x = 270, y = 250)

    non_veg_button = tk.Radiobutton(menu_window, text = "Non-Veg", variable = v_nv_type_var, value = "Non-Veg", bg = "#ACE1AF", fg = "black", font = ("Times New Roman", 18))
    non_veg_button.place(x = 270, y = 280)

    add_button = tk.Button(menu_window, text = "Add Food Item", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18))
    add_button.place(x = 270, y = 350)

    remove_button = tk.Button(menu_window, text = "Remove Food Item", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18))
    remove_button.place(x = 270, y = 400)

    



