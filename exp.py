# sore if gubot guys HAHAHAHAHA
# ga use kog Custom Tkinter (CTkinter) instead of tkinter lng
# ga use sd kog calendar para sa date sa pag add og expenses HAHAHAHA

import customtkinter as ctk
import tkinter as gui
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Expense Tracker")
root.geometry("730x400")

button_frame = ctk.CTkFrame(root, corner_radius=10)
button_frame.pack(side="top")

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# here ang data
expenses = []

def calculate_total():
    total = 0.0
    for exp in expenses:
        try:
            total += float(exp["amount"])
        except (ValueError, KeyError):
            continue
    return total

def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def home():
    clear_frame()
    ctk.CTkLabel(content_frame, text="--WELCOME--", font=("Arial", 50, "bold")).pack(anchor=ctk.CENTER, pady=(110, 0))
    ctk.CTkLabel(content_frame, text="Start tracking your expenses now!", font=("Arial", 20)).pack(anchor=ctk.CENTER)
    ctk.CTkButton(content_frame, text="Add Expense", corner_radius=20, command=addexp).pack(pady=10)

def addexp():
    clear_frame()
    grid_frame = ctk.CTkFrame(content_frame)
    grid_frame.pack(expand=True)
    grid_frame.place(relx=0.5, rely=0.5, anchor="center")

    ctk.CTkLabel(grid_frame, text="Add Expense", font=("Arial", 15)).grid(row=0, column=3, columnspan=2, pady=10, sticky="ew")
    ctk.CTkLabel(grid_frame, text="Expense name:", justify=ctk.LEFT).grid(row=1, column=3, pady=(10, 5), sticky="ew")
    ctk.CTkLabel(grid_frame, text="Amount:", justify=ctk.LEFT).grid(row=2, column=3, pady=5, sticky="ew")
    ctk.CTkLabel(grid_frame, text="Date:", justify=ctk.LEFT).grid(row=3, column=3, pady=5, sticky="ew")

    # keep ang references para ma access ang mga values later ge add ni nako (cj opaw) para sd mag run ang "name_entry" or values sa addexpfunc
    name_entry = ctk.CTkEntry(grid_frame, placeholder_text="Enter expense name...")
    name_entry.grid(row=1, column=4, padx=10, pady=(10, 5), sticky="ew")

    amount_entry = ctk.CTkEntry(grid_frame, placeholder_text="Enter amount...")
    amount_entry.grid(row=2, column=4, padx=10, pady=5, sticky="ew")

    date_entry = DateEntry(grid_frame, width=37, background="darkblue", foreground="white", borderwidth=2)
    date_entry.grid(row=3, column=4, padx=10, sticky="ew")

    # ---------------------------------------------------------------------------------------
    def addexpfunc(): # declared a function named addexpfunc
        name = name_entry.get().strip() # "get" function to get the current text of entry box, "strip" to remove spaces.
        amount = amount_entry.get().strip() # as well as here for the amount.
        date = date_entry.get().strip() # and here for the date.

        if not name or not amount or not date: # creates a decision control for name, amount, and date.
            messagebox.showerror("Error", "All fields must be filled!") # shows if decision control is true "Error, All Fields must be filled!"
            return # used to stop the function with return.
        try:
            amount = float(amount) # attempt to convert amount string into a number which is the float.
        except ValueError: # used valuerror for invalid type conversion.
            messagebox.showerror("Error", "Amount must be a number!") # shows if ValueError is true: "Error, Amount must be a number!"
            return # used to stop the function with return.

        expense = {"name": name, "amount": amount, "date": date} # creates dictionary (string) for name, amount & date
        expenses.append(expense) # to add the dictionary up to the list.
        messagebox.showinfo("Success", "Expense added successfully!") # shows if "Success, Expense added successfully!"

        # clear entries
        name_entry.delete(0, "end") # .delete(0, end) index 0 to end.
        amount_entry.delete(0, "end")
        date_entry.delete(0, "end")
    # ---------------------------------------------------------------------------------------

    ctk.CTkButton(grid_frame, text="Add", corner_radius=20, command=addexpfunc).grid(row=4, column=3, columnspan=2, pady=5, sticky="ew")
# aron ma view mga expense nga gi add sa "add expense" no shii
def viewsum():
    clear_frame()
    ctk.CTkLabel(content_frame, text="Expense Summary", font=("Arial", 15)).pack(pady=10)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="white", background="#797979")

    tableframe = ctk.CTkFrame(content_frame)
    tableframe.pack(fill="both", expand=True)
    vsb = ttk.Scrollbar(tableframe, orient="vertical")
    vsb.pack(side="right", fill="y")

    table = ttk.Treeview(tableframe, columns=('Expenses', 'Amount', 'Date'), show='headings',
                         yscrollcommand=vsb.set, selectmode="extended")
    table.column('Expenses', width=100)
    table.column('Amount', width=100)
    table.column('Date', width=100)
    table.heading('Expenses', text="Expenses")
    table.heading('Amount', text="Amount")
    table.heading('Date', text="Date")
    table.pack(side="left", expand=True, fill="both")
    vsb.config(command=table.yview)

    # single click to select/deselect — no Ctrl needed aron di lisod 
    def toggle_select(event):
        row = table.identify_row(event.y)
        if not row:
            return
        if row in table.selection():
            table.selection_remove(row)
        else:
            table.selection_add(row)
        return "break"

    table.bind("<Button-1>", toggle_select)

    # ---------------------------------------------------------------------------------------
    def refreshtable():
        table.delete(*table.get_children())
        for exp in expenses:
            table.insert("", "end", values=(exp["name"], exp["amount"], exp["date"]))
    # ---------------------------------------------------------------------------------------

    totalframe = ctk.CTkFrame(content_frame)
    totalframe.pack(fill="x", pady=(10, 0))
    ctk.CTkLabel(totalframe, text="Total:", font=("Arial", 12)).pack(side="left", pady=5)
    total_label = ctk.CTkLabel(totalframe, text="₱0.00", font=("Arial", 12, "bold"), text_color="green")
    total_label.pack(side="right", padx=10, pady=5)

    # ---------------------------------------------------------------------------------------
    #to compute the total expensis 
    def compute():
        selected = table.selection()
        if selected:
            total = 0.0
            for sel in selected:
                values = table.item(sel, "values")
                try:
                    total += float(values[1])
                except (ValueError, KeyError):
                    continue
            total_label.configure(text=f"₱{total:,.2f} (selected)")
        else:
            if len(expenses) == 0:
                total_label.configure(text="₱0.00")
            else:
                total = calculate_total()
                total_label.configure(text=f"₱{total:,.2f} (all)")
    # ---------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------
    def deleteexp():
        pass
    # ---------------------------------------------------------------------------------------

    ctk.CTkButton(content_frame, text="Compute", corner_radius=20, command=compute, fg_color="green").pack(pady=10)

    refreshtable()

def manage_expenses():

    clear_frame()

    ctk.CTkLabel(
        content_frame,
        text="Manage Expenses",
        font=("Arial", 22, "bold")
    ).pack(pady=10)

    scroll_frame = ctk.CTkScrollableFrame(content_frame, width=600, height=250)
    scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # if no expenses = way makita means wala
    if len(expenses) == 0:

        ctk.CTkLabel(
            scroll_frame,
            text="No expenses found.",
            font=("Arial", 14)
        ).pack(pady=20)

    # display all expenses
    for index, expense in enumerate(expenses):

        expense_frame = ctk.CTkFrame(scroll_frame, corner_radius=15)
        expense_frame.pack(fill="x", pady=5, padx=5)

        info_text = f"""
Expense: {expense['name']}
Amount: ₱{expense['amount']}
Date: {expense['date']}
"""

        ctk.CTkLabel(
            expense_frame,
            text=info_text,
            justify="left",
            font=("Arial", 13)
        ).pack(side="left", padx=15, pady=10)

        # delete button for each expense
        def delete_selected(i=index):
 
            expenses.pop(i)
 
            messagebox.showinfo("Success", "Expense deleted successfully!")
 
            manage_expenses()
 
        ctk.CTkButton(
            expense_frame,
            text="Delete",
            width=80,
            fg_color="darkred",
            hover_color="red",
            command=delete_selected
        ).pack(side="right", padx=15)


def settings():
    clear_frame()
    ctk.CTkLabel(content_frame, text="Settings", font=("Arial", 18)).pack(pady=10)
    ctk.CTkLabel(content_frame, text="Customize your preferences here.", font=("Arial", 14, "bold")).pack()

    switch = ctk.CTkSwitch(content_frame, text="Dark Mode", onvalue="dark", offvalue="light", command=lambda: ctk.set_appearance_mode(switch.get()))
    switch.pack(pady=10)

    ctk.CTkLabel(content_frame, text="About", font=("Arial", 14, "bold")).pack(pady=10)
    ctk.CTkLabel(content_frame, text="Expense Tracker made by:\nCelesios, Avril Satu\nKilat, Sean\nLucabgo, John Paul\nMainit, Christian Jay\nMagpatoc, Sunday Dawn", font=("Arial", 12, "italic")).pack()

ctk.CTkButton(button_frame, text="Home", corner_radius=10, command=home).pack(side="left", padx=2, pady=10)
ctk.CTkButton(button_frame, text="Add Expense", corner_radius=10, command=addexp).pack(side="left", padx=2, pady=10)
ctk.CTkButton(button_frame, text="View Summary", corner_radius=10, command=viewsum).pack(side="left", padx=2, pady=10)
ctk.CTkButton(button_frame, text="Manage Expenses", corner_radius=10, command=manage_expenses).pack(side="left", padx=2, pady=10)
ctk.CTkButton(button_frame, text="Settings", corner_radius=10, command=settings).pack(side="left", padx=2, pady=10)

home()
root.mainloop()