# sore if gubot guys HAHAHAHAHA

import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Expense Tracker")
root.geometry("560x400")

button_frame = ctk.CTkFrame(root, corner_radius=10)
button_frame.pack(side="top")

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# here ang data
expenses = [] 

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

    ctk.CTkEntry(grid_frame, placeholder_text="Enter expense name...").grid(row=1, column=4, padx=10, pady=(10, 5), sticky="ew")
    ctk.CTkEntry(grid_frame, placeholder_text="Enter amount...").grid(row=2, column=4, padx=10, pady=5, sticky="ew")
    DateEntry(grid_frame, width=37, background="darkblue", foreground="white", borderwidth=2).grid(row=3, column=4, padx=10, sticky="ew")

# ---------------------------------------------------------------------------------------
    def addexpfunc():
        # put add expense code here
        pass
# ---------------------------------------------------------------------------------------

    ctk.CTkButton(grid_frame, text="Add", corner_radius=20, command=addexpfunc).grid(row=4, column=3, columnspan=2, pady=5, sticky="ew")

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

    table = ttk.Treeview(tableframe, columns=('Expenses', 'Amount', 'Date'), show='headings', yscrollcommand=vsb.set)
    table.column('Expenses', width=100)
    table.column('Amount', width=100)
    table.column('Date', width=100)
    table.heading('Expenses', text="Expenses")
    table.heading('Amount', text="Amount")  
    table.heading('Date', text="Date")
    table.pack(side="left", expand=True, fill="both")
    vsb.config(command=table.yview)

    # ---------------------------------------------------------------------------------------
    def refreshtable():
        # butangig refresh code para mo refresh and table after adding or deleting expenses
        pass
    # ---------------------------------------------------------------------------------------

    totalframe = ctk.CTkFrame(content_frame)
    totalframe.pack(fill="x", pady=(10, 0))
    ctk.CTkLabel(totalframe, text="Total:", font=("Arial", 12)).pack(side="left", pady=5)
    ctk.CTkLabel(totalframe, text="₱0.00", font=("Arial", 12, "bold"), text_color="green").pack(side="right", padx=10, pady=5)

    # ---------------------------------------------------------------------------------------
    def compute():
        # butangig compute code para mo compute sa total expenses
        pass
    # ---------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------
    def deleteexp():
            # put delete expense code here
            pass
    # ---------------------------------------------------------------------------------------

    ctk.CTkButton(content_frame, text="Compute", corner_radius=20, command=compute, fg_color="green").pack(side="right", padx=(0, 70), pady=10)
    ctk.CTkButton(content_frame, text="Delete", corner_radius=20, command=deleteexp, fg_color="darkred").pack(side="left", padx=(70, 0), pady=10)

    refreshtable()

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
ctk.CTkButton(button_frame, text="Settings", corner_radius=10, command=settings).pack(side="left", padx=2, pady=10)

home()
root.mainloop()
