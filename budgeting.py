import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


total_budget_label = None
total_budget_entry = None
expenses_listbox = None
expense_name_entry = None
expense_cost_entry = None
total_spenditure_label = None
total_remaining_label = None


total_spent = 0
remaining_budget = 0
total_budget = 0
expenses_list = []






def enter_budget():
    global total_budget, total_spent, remaining_budget, total_budget_entry, total_budget_label


    total_budget = int(total_budget_entry.get())

    total_budget_label.config(text = f"Total Budget: {total_budget}")

    remaining_budget = total_budget
    total_remaining_label.config(text = f"Remaining budget: {remaining_budget}")

    total_budget_entry.delete(0, tk.END)
    



def add_expense():
    global expenses_listbox, total_budget, total_spent, remaining_budget, expense_cost_entry, expense_name_entry, total_spenditure_label, total_remaining_label, expenses_list

    expense_cost = int(expense_cost_entry.get())
    expense_name = expense_name_entry.get()

    expense = (expense_name, expense_cost)

    expenses_list.append(expense)

    last_item_index = len(expenses_list) -1
    expenses_listbox.insert(tk.END, expenses_list[last_item_index])

    total_spent += expense_cost
    total_spenditure_label.config(text = f"Total Amount Spent: {total_spent}")

    remaining_budget -= expense_cost
    total_remaining_label.config(text = f"Remaining budget: {remaining_budget}")

    expense_name_entry.delete(0, tk.END)
    expense_cost_entry.delete(0, tk.END)






    



    









def budgeting_window():
    global total_budget_label, total_budget_entry, expenses_listbox, expense_name_entry, expense_cost_entry, total_spenditure_label, total_remaining_label, expenses_list


    budgeting_window = tk.Tk()
    budgeting_window.title("Budgeting Window")
    budgeting_window.geometry("500x500")
    budgeting_window.config(bg = "#A7C7E7")

    total_budget_var  = tk.IntVar(value = 0)
    

    expenses_listbox = tk.Listbox(budgeting_window, bg = "white", fg = "black", font = ("Times New Roman", 18), width = 30, height = 15)
    expenses_listbox.place(x = 20, y = 20)
    for i in expenses_list:
        expenses_listbox.insert(tk.END, i)

    total_budget_question = tk.Label(budgeting_window, text = "Total Budget:", bg = "#A7C7E7", fg = "black", font = ("Times New Roman", 18))
    total_budget_question.place(x = 300, y = 30)

    total_budget_entry = tk.Entry(budgeting_window, bg = "white", fg = "black", bd = 4, relief = tk.GROOVE, font = ("Times New Roman", 18))
    total_budget_entry.place(x = 300, y = 70)

    enter_button = tk.Button(budgeting_window, text = "Enter", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18), command = enter_budget)
    enter_button.place(x = 300, y = 110)

    expense_name_label = tk.Label(budgeting_window, text = "Expense Name:", bg = "#A7C7E7", fg = "black", font = ("Times New Roman", 18))
    expense_name_label.place(x = 300, y = 160)

    expense_name_entry = tk.Entry(budgeting_window, bg = "white", fg = "black", bd = 4, relief = tk.GROOVE, font = ("Times New Roman", 18))
    expense_name_entry.place(x = 300, y =200)

    expense_cost_label = tk.Label(budgeting_window, text = "Expense Cost:", bg = "#A7C7E7", fg = "black", font = ("Times New Roman", 18))
    expense_cost_label.place(x = 300, y = 240)

    expense_cost_entry = tk.Entry(budgeting_window, bg = "white", fg = "black", bd = 4, relief = tk.GROOVE, font = ("Times New Roman", 18))
    expense_cost_entry.place(x = 300, y = 290)

    add_button = tk.Button(budgeting_window, text = "Add Expense", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18), command = add_expense)
    add_button.place(x = 325, y = 350)

    total_budget_label = tk.Label(budgeting_window, text = f"Total Budget: {total_budget}", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18))
    total_budget_label.place(x = 40, y = 375)

    total_spenditure_label = tk.Label(budgeting_window, text = f"Total Amount Spent: {total_spent}", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18))
    total_spenditure_label.place(x = 40, y = 415)

    total_remaining_label = tk.Label(budgeting_window, text = f"Remaining budget: {remaining_budget}", bg = "white", fg = "black", bd = 4, relief = tk.SUNKEN, font = ("Times New Roman", 18))
    total_remaining_label.place(x = 40, y = 455)





