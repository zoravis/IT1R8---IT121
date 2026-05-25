import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry # ga download kog tkcalendar kay para sa datepicker

# sore guys gi mano mano ko ni AHHAHAHAHA
root = tk.Tk()
root.title("Expense Tracker kase mga nijer sila")
root.geometry("420x400")

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

content_frame = tk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True)

# maoni mga coloristeristics (di pa final)
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F0F0F0"
DARK_GRAY = "#A9A9A9"
BUTTON_COLOR = "#4CAF50"


def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

# needs color n design
def home(): # diri ang home page
    clear_frame()
    tk.Label(content_frame, text="WELCOME", font=("Arial", 30, "bold")).pack(anchor=tk.CENTER, pady=(120, 0))
    tk.Label(content_frame, text="Start tracking your expenses now!", font=("Arial", 10)).pack(anchor=tk.CENTER)
    tk.Button(content_frame, text="Add Expense", command=addexp).pack(anchor=tk.CENTER, pady=10)

def addexp(): # tas diri ang add expense page
    clear_frame()
    grid_frame = tk.Frame(content_frame)
    grid_frame.pack()
    
    tk.Label(grid_frame, text="Add Expense", font=("Arial", 15)).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(grid_frame, text="Expense name:").grid(row=1, column=0, sticky=tk.W, pady=(70, 5))
    tk.Label(grid_frame, text="Amount:").grid(row=2, column=0, sticky=tk.W, pady=5)
    tk.Label(grid_frame, text="Date:").grid(row=3, column=0, sticky=tk.W, pady=5)
    
    tk.Entry(grid_frame).grid(row=1, column=1, padx=10, pady=(70, 5))
    spinbox = ttk.Spinbox(grid_frame, from_=0, to=999999999).grid(row=2, column=1, padx=50, pady=5)
    DateEntry(grid_frame, width=12, background='darkblue', foreground='white', borderwidth=2).grid(row=3, column=1, padx=10)

# ---------------------------------------------------------------------------------------
    def addexpfunc():
        # put add expense code here
        pass
# ---------------------------------------------------------------------------------------

    tk.Button(grid_frame, text="Add", command=addexpfunc).grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.EW)


def viewsum(): # diri ang view summary page
    clear_frame()
    tk.Label(content_frame, text="Expense Summary", font=("Arial", 15)).pack(pady=10)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10))
    style.configure("Treeview", foreground=BUTTON_COLOR, background=BUTTON_COLOR, fieldbackground=BUTTON_COLOR)
    
    tableframe = tk.Frame(content_frame)
    tableframe.pack(fill=tk.BOTH, padx=10, pady=5)
    vsb = ttk.Scrollbar(tableframe, orient="vertical")
    vsb.pack(side=tk.RIGHT, fill=tk.Y)

    table = ttk.Treeview(tableframe, columns=('Expenses', 'Amount', 'Date'), show='headings', yscrollcommand=vsb.set)
    table.column('Expenses', width=100)
    table.column('Amount', width=100)
    table.column('Date', width=100)
    table.heading('Expenses', text="Expenses")
    table.heading('Amount', text="Amount")  
    table.heading('Date', text="Date")
    
    table.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    vsb.config(command=table.yview)

# ---------------------------------------------------------------------------------------
    def deleteexp():
        # put delete code here
        pass
# ---------------------------------------------------------------------------------------

    total = tk.Frame(content_frame)
    total.pack(fill=tk.X, pady=(10, 0), padx=10)
    tk.Label(total, text="Total:", font=("Arial", 12)).pack(side=tk.LEFT)
    tk.Label(total, text="$0.00", font=("Arial", 12,), fg="green").pack(side=tk.RIGHT, padx=5)
    buttonframe = tk.Frame(content_frame)
    buttonframe.pack(fill=tk.X, side=tk.BOTTOM, pady=10, padx=10)
    tk.Button(buttonframe, text="Delete", command=deleteexp, bg="dark red", fg="white", padx=10).pack(side=tk.BOTTOM, pady=(0, 5))

def settings(): # diri ang settings page
    clear_frame()
    var = tk.IntVar()
    tk.Label(content_frame, text="Settings", font=("Arial", 15)).pack(pady=10)
    tk.Label(content_frame, text="\nCustomize your preferences here.", font=("Arial", 12)).pack()
    tk.Radiobutton(content_frame, text="Light Mode (Default)", variable=var, value=1, font=("Arial", 9)).pack(padx=10, anchor=tk.W)
    tk.Radiobutton(content_frame, text="Dark Mode", variable=var, value=2, font=("Arial", 9)).pack(padx=10, anchor=tk.W) 
    tk.Label(content_frame, text="About", font=("Arial", 12)).pack(pady=10)
    tk.Label(content_frame, text="Expense Tracker made by:", font=("Arial", 11)).pack()
    tk.Label(content_frame, text=(
        "Celesios, Avril Satu"
        "\nKilat, Sean"
        "\nLucabgo, John Paul"
        "\nMainit, Christian Jay"
        "\nMagpatoc, Sunday Dawn"
    ), font=("Arial", 10, "italic")).pack()

# diri ang menu buttonizations
button1 = tk.Button(button_frame, text="Home", command=home)
button2 = tk.Button(button_frame, text="Add Expense", command=addexp)
button3 = tk.Button(button_frame, text="View Summary", command=viewsum)
button4 = tk.Button(button_frame, text="Settings", command=settings)

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)

home()
root.mainloop()