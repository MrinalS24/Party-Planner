import tkinter as tk
from guestlist import show_guests




window = tk.Tk()
window.geometry("600x500")
window.config(bg = "#ffd1f4")
window.title("Party Planner")




planner_label = tk.Label(window, text = "PARTY PLANNER", fg = "black", bg = "#ffd1f4", font = ("Times New Roman", 20))
planner_label.place(x = 230, y = 230)

guest_list_button = tk.Button(window, text = "GUEST LIST", fg = "black", bg = "white", font = ("Times New Roman", 20))
guest_list_button.place(x = 235, y = 80)

checklist_button = tk.Button(window, text = "CHECKLIST", fg = "black", bg = "white", font = ("Times New Roman", 20))
checklist_button.place(x = 230, y = 380)

budget_button = tk.Button(window, text = "BUDGETING", fg = "black", bg = "white", font = ("Times New Roman", 20))
budget_button.place(x = 15, y = 230)

food_button = tk.Button(window, text = "FOOD", fg = "black", bg = "white", font = ("Times New Roman", 20))
food_button.place(x = 480, y = 230)




window.mainloop()
