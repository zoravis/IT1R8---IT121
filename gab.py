import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ===== Theme =====
BG_DARK    = "#000000"
BG_MENU    = "#000000"
TEXT_LIGHT = "#e2e2e2"
TEXT_HOVER = "#ff0000"
HOVER_BG   = "#ffffff"

# ===== Database Init =====
def init_all_dbs():
    conn = sqlite3.connect("main_users.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY, password TEXT NOT NULL)""")
    conn.commit(); conn.close()

    conn = sqlite3.connect("payroll.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS payroll (
        emp_no TEXT PRIMARY KEY, name TEXT, position TEXT,
        rate REAL, days REAL, gross REAL, sss REAL,
        philhealth REAL, cash_adv REAL, deductions REAL, net REAL)""")
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    conn.commit(); conn.close()

    conn = sqlite3.connect("grading_system.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT, name TEXT, course TEXT, subject TEXT,
        prelim REAL, midterm REAL, final REAL,
        average REAL, num_val TEXT, remark TEXT)""")
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    conn.commit(); conn.close()

# ===== Grade Computation =====
def compute_grade(p, m, f):
    try:
        p, m, f = float(p), float(m), float(f)
        if not all(0 <= x <= 100 for x in [p, m, f]):
            return None, None, None
        avg = (p * 0.3) + (m * 0.3) + (f * 0.4)
        r = round(avg)
        if r >= 95:   grade, rem = "1.00", "Excellent"
        elif r >= 90: grade, rem = "1.25", "Very Good"
        elif r >= 85: grade, rem = "1.50", "Above Average"
        elif r >= 80: grade, rem = "1.75", "Average"
        elif r >= 75: grade, rem = "2.00", "Passing"
        elif r >= 70: grade, rem = "2.25", "Conditional"
        else:         grade, rem = "5.00", "Failed"
        return avg, grade, rem
    except:
        return None, None, None

# ===== ACT 1: Student Information =====
def act1():
    win = tk.Toplevel(window)
    win.title("Student Information")
    win.geometry("400x250")
    win.configure(bg="#121212")
    info = (
        "STUDENT INFORMATION\n"
        "=========================\n"
        "Student ID : 2025301731\n"
        "Name       : Gabriel L. Cajandab\n"
        "Course     : BS INFORMATION TECHNOLOGY\n"
        "Year Level : 1st Year"
    )
    tk.Label(win, text=info, font=("Consolas", 11), bg="#121212",
             fg="#00ffaa", justify="left").pack(expand=True, padx=20, pady=20)

# ===== ACT 2: Sales Program =====
def act2():
    win = tk.Toplevel(window)
    win.title("Sales Program")
    win.geometry("380x380")
    win.configure(bg="#121212")
    ls = {"bg": "#121212", "fg": "white", "font": ("Segoe UI", 10)}
    es = {"bg": "#1e1e1e", "fg": "white", "insertbackground": "white", "relief": "flat"}
    tk.Label(win, text="Sales Program", font=("Segoe UI", 14, "bold"),
             bg="#121212", fg="#ffffff").pack(pady=15)
    frame = tk.Frame(win, bg="#121212"); frame.pack(padx=20)
    fields = ["Customer Number", "Customer Name", "Item Description", "Price", "Quantity"]
    entries = {}
    for i, f in enumerate(fields):
        tk.Label(frame, text=f, **ls).grid(row=i, column=0, sticky="w", pady=5)
        e = tk.Entry(frame, **es, width=22); e.grid(row=i, column=1, pady=5)
        entries[f] = e
    result_var = tk.StringVar()
    tk.Label(win, textvariable=result_var, font=("Consolas", 11),
             bg="#121212", fg="#ffffff").pack(pady=10)
    def compute():
        try:
            total = float(entries["Price"].get()) * float(entries["Quantity"].get())
            result_var.set(f"TOTAL SALES AMOUNT: {total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Enter valid numeric Price and Quantity.", parent=win)
    tk.Button(win, text="Compute", command=compute, bg="#00ffaa", fg="black",
              font=("Segoe UI", 10, "bold"), relief="flat", width=15).pack(pady=5)

# ===== ACT 3: Grade Calculator =====
def act3():
    win = tk.Toplevel(window)
    win.title("Grade Calculator")
    win.geometry("450x580")
    win.configure(bg="#121212")

    ls = {"bg": "#121212", "fg": "white", "font": ("Segoe UI", 10)}
    es = {"bg": "#1e1e1e", "fg": "white", "insertbackground": "white", "relief": "flat"}

    tk.Label(win, text="Grade Calculator", font=("Segoe UI", 14, "bold"),
             bg="#121212", fg="#00ffaa").pack(pady=15)

    frame = tk.Frame(win, bg="#121212")
    frame.pack(padx=20)

    labels = ["Name", "Course", "ID Number", "Subject", "Prelim", "Midterm", "Finals"]
    entries = {}

    for i, lbl in enumerate(labels):
        tk.Label(frame, text=lbl, **ls).grid(row=i, column=0, sticky="w", pady=4)
        e = tk.Entry(frame, **es, width=28)
        e.grid(row=i, column=1, pady=4)
        entries[lbl] = e

    # Result output
    result_var = tk.StringVar()
    result_label = tk.Label(win, textvariable=result_var,
                            font=("Consolas", 10),
                            bg="#121212", fg="#00ffaa",
                            justify="left")
    result_label.pack(pady=15)

    def calc():
        name    = entries["Name"].get().strip()
        course  = entries["Course"].get().strip()
        sid     = entries["ID Number"].get().strip()
        subject = entries["Subject"].get().strip()

        if not all([name, course, sid, subject]):
            messagebox.showerror("Error", "Fill all fields.", parent=win)
            return

        if not sid.isdigit():
            messagebox.showerror("Error", "ID must be numeric.", parent=win)
            return

        try:
            prelim  = float(entries["Prelim"].get())
            midterm = float(entries["Midterm"].get())
            finals  = float(entries["Finals"].get())
        except ValueError:
            messagebox.showerror("Error", "Grades must be numbers.", parent=win)
            return

        if any(q < 0 or q > 100 for q in [prelim, midterm, finals]):
            messagebox.showerror("Error", "Scores must be 0-100.", parent=win)
            return

        avg    = (prelim * 0.3) + (midterm * 0.3) + (finals * 0.4)
        remark = "Passed" if avg >= 75 else "Failed"

        # Color based on remark
        color = "#00ffaa" if remark == "Passed" else "#ff4444"
        result_label.config(fg=color)

        result_var.set(
            f"{'='*35}\n"
            f" Student Number : {sid}\n"
            f" Student Name   : {name}\n"
            f" Course         : {course}\n"
            f" Subject        : {subject}\n"
            f"{'='*35}\n"
            f" Final Grade    : {avg:.2f}\n"
            f" Remarks        : {remark}\n"
            f"{'='*35}"
        )

    def clr():
        for e in entries.values():
            e.delete(0, tk.END)
        result_var.set("")
        result_label.config(fg="#00ffaa")

    tk.Button(win, text="Calculate", command=calc,
              bg="#00ffaa", fg="black",
              font=("Segoe UI", 10, "bold"),
              relief="flat", width=15).pack(pady=5)
    tk.Button(win, text="Clear", command=clr,
              bg="#333333", fg="white",
              font=("Segoe UI", 10, "bold"),
              relief="flat", width=15).pack(pady=5)
    tk.Button(win, text="Close", command=win.destroy,
              bg="#cc0000", fg="white",
              font=("Segoe UI", 10, "bold"),
              relief="flat", width=15).pack(pady=5)

# ===== ACT 4: Simple Payroll =====
def act4():
    win = tk.Toplevel(window)
    win.title("Simple Payroll System")
    win.geometry("480x750")
    win.configure(bg="#121212")

    ls = {"bg": "#121212", "fg": "white", "font": ("Segoe UI", 10)}
    es = {"bg": "#1e1e1e", "fg": "white", "insertbackground": "white", "relief": "flat"}
    bs = {"font": ("Segoe UI", 10, "bold"), "relief": "flat", "width": 20}

    tk.Label(win, text="Employee Payroll System", font=("Segoe UI", 16, "bold"),
             bg="#121212", fg="#00ffaa").pack(pady=20)

    frame = tk.Frame(win, bg="#121212")
    frame.pack()

    tk.Label(frame, text="Employee Number",  **ls).grid(row=0, column=0, sticky="w", pady=5)
    e_num  = tk.Entry(frame, **es); e_num.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Employee Name",    **ls).grid(row=1, column=0, sticky="w", pady=5)
    e_name = tk.Entry(frame, **es); e_name.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Rate Per Day",     **ls).grid(row=2, column=0, sticky="w", pady=5)
    e_rate = tk.Entry(frame, **es); e_rate.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Days Worked",      **ls).grid(row=3, column=0, sticky="w", pady=5)
    e_days = tk.Entry(frame, **es); e_days.grid(row=3, column=1, pady=5)

    # Deductions section
    tk.Label(win, text="Deductions", font=("Segoe UI", 13, "bold"),
             bg="#121212", fg="#00ffaa").pack(pady=10)

    frame2 = tk.Frame(win, bg="#121212")
    frame2.pack()

    tk.Label(frame2, text="SSS",          **ls).grid(row=0, column=0, sticky="w", pady=5)
    e_sss  = tk.Entry(frame2, **es); e_sss.grid(row=0, column=1, pady=5)

    tk.Label(frame2, text="PhilHealth",   **ls).grid(row=1, column=0, sticky="w", pady=5)
    e_phil = tk.Entry(frame2, **es); e_phil.grid(row=1, column=1, pady=5)

    tk.Label(frame2, text="Cash Advance", **ls).grid(row=2, column=0, sticky="w", pady=5)
    e_cash = tk.Entry(frame2, **es); e_cash.grid(row=2, column=1, pady=5)

    # Result output
    result_var = tk.StringVar()
    result_label = tk.Label(win, textvariable=result_var,
                            font=("Consolas", 10),
                            bg="#121212", fg="#00ffaa",
                            justify="left")
    result_label.pack(pady=15)

    def payroll():
        num  = e_num.get().strip()
        name = e_name.get().strip()

        if not num or not name or not e_rate.get() or not e_days.get():
            messagebox.showerror("Error", "Fill all required fields.", parent=win)
            return

        if any(c.isdigit() for c in name):
            messagebox.showerror("Error", "Name must not contain numbers.", parent=win)
            return

        try:
            rate = float(e_rate.get())
            days = float(e_days.get())
            sss  = float(e_sss.get())  if e_sss.get()  else 0
            phil = float(e_phil.get()) if e_phil.get() else 0
            cash = float(e_cash.get()) if e_cash.get() else 0

            if rate <= 0 or days <= 0:
                messagebox.showerror("Error", "Rate and Days must be positive.", parent=win)
                return

            if any(x < 0 for x in [sss, phil, cash]):
                messagebox.showerror("Error", "Deductions cannot be negative.", parent=win)
                return

        except ValueError:
            messagebox.showerror("Error", "Enter valid numeric values.", parent=win)
            return

        gross     = rate * days
        total_ded = sss + phil + cash
        net       = gross - total_ded

        if total_ded > gross:
            messagebox.showerror("Error", "Deductions exceed Gross Pay.", parent=win)
            return

        result_var.set(
            f"{'='*38}\n"
            f" Employee Number   : {num}\n"
            f" Employee Name     : {name}\n"
            f" Rate Per Day      : {rate:.2f}\n"
            f" No. of Work Days  : {days}\n"
            f"{'='*38}\n"
            f" SSS               : {sss:.2f}\n"
            f" PhilHealth        : {phil:.2f}\n"
            f" Cash Advance      : {cash:.2f}\n"
            f" Total Deduction   : {total_ded:.2f}\n"
            f"{'='*38}\n"
            f" Gross Pay         : {gross:.2f}\n"
            f" Net Pay           : {net:.2f}\n"
            f"{'='*38}"
        )

    def clear():
        for e in [e_num, e_name, e_rate, e_days, e_sss, e_phil, e_cash]:
            e.delete(0, tk.END)
        result_var.set("")

    tk.Button(win, text="Compute Payroll", command=payroll,
              bg="#00ffaa", fg="black", **bs).pack(pady=10)
    tk.Button(win, text="Clear All", command=clear,
              bg="#333333", fg="white", **bs).pack(pady=5)

# ===== ACT 5: Grading System with Combobox =====
def act5():
    win = tk.Toplevel(window)
    win.title("Grading System")
    win.geometry("400x680")
    win.configure(bg="#000000")
    LS = {"bg": "#000000", "fg": "white",   "font": ("Arial", 10)}
    ES = {"bg": "#222222", "fg": "white",   "insertbackground": "white", "relief": "flat"}
    RS = {"bg": "#222222", "fg": "white",   "relief": "flat"}
    GS = {"bg": "#000000", "fg": "#ffffff", "font": ("Arial", 12, "bold")}
    tk.Label(win, text="Student Grading System", **GS).pack(pady=20)
    f = tk.Frame(win, bg="#000000"); f.pack(padx=20)
    tk.Label(f, text="Student Number", **LS).grid(row=0, column=0, sticky="w", pady=5)
    stNum  = tk.Entry(f, **ES, width=25); stNum.grid(row=0, column=1)
    tk.Label(f, text="Student Name",   **LS).grid(row=1, column=0, sticky="w", pady=5)
    stName = tk.Entry(f, **ES, width=25); stName.grid(row=1, column=1)
    tk.Label(f, text="Course",         **LS).grid(row=2, column=0, sticky="w", pady=5)
    cbC = ttk.Combobox(f, values=["BSIT","BSCS","BSEMC"], state="readonly", width=22)
    cbC.current(0); cbC.grid(row=2, column=1)
    tk.Label(f, text="Subject",        **LS).grid(row=3, column=0, sticky="w", pady=5)
    stSub  = tk.Entry(f, **ES, width=25); stSub.grid(row=3, column=1)
    tk.Label(f, text="Grades", **GS).grid(row=4, column=0, sticky="w", pady=(15,0))
    tk.Frame(f, bg="#ffffff", height=1).grid(row=5, column=0, columnspan=2, sticky="we", pady=5)
    tk.Label(f, text="Prelim Grade",   **LS).grid(row=6, column=0, sticky="w", pady=2)
    pre = tk.Entry(f, **ES, width=12); pre.grid(row=6, column=1, sticky="w")
    tk.Label(f, text="Midterm Grade",  **LS).grid(row=7, column=0, sticky="w", pady=2)
    mid = tk.Entry(f, **ES, width=12); mid.grid(row=7, column=1, sticky="w")
    tk.Label(f, text="Final Grade",    **LS).grid(row=8, column=0, sticky="w", pady=2)
    fin = tk.Entry(f, **ES, width=12); fin.grid(row=8, column=1, sticky="w")
    tk.Label(f, text="Result", **GS).grid(row=9, column=0, sticky="w", pady=(15,0))
    tk.Frame(f, bg="#ffffff", height=1).grid(row=10, column=0, columnspan=2, sticky="we", pady=(0,10))
    tk.Label(f, text="Average Grade",   **LS).grid(row=11, column=0, sticky="w", pady=2)
    res_avg = tk.Label(f, text="", **RS, width=15, anchor="w"); res_avg.grid(row=11, column=1, sticky="w")
    tk.Label(f, text="Numerical Value", **LS).grid(row=12, column=0, sticky="w", pady=2)
    res_num = tk.Label(f, text="", **RS, width=15, anchor="w"); res_num.grid(row=12, column=1, sticky="w")
    tk.Label(f, text="Remarks",         **LS).grid(row=13, column=0, sticky="w", pady=2)
    res_rem = tk.Label(f, text="", **RS, width=15, anchor="w"); res_rem.grid(row=13, column=1, sticky="w")
    def calc():
        if not stNum.get().strip() or not stName.get().strip() or not stSub.get().strip():
            messagebox.showerror("Error", "Fill all student details.", parent=win); return
        if any(c.isdigit() for c in stName.get()):
            messagebox.showerror("Error", "Name cannot contain numbers.", parent=win); return
        try:
            p_v = float(pre.get().strip() or 0)
            m_v = float(mid.get().strip() or 0)
            f_v = float(fin.get().strip() or 0)
            if any(g < 0 or g > 100 for g in [p_v, m_v, f_v]):
                messagebox.showerror("Error", "Grades must be 0-100.", parent=win); return
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers.", parent=win); return
        avg = (p_v * 0.30) + (m_v * 0.30) + (f_v * 0.40)
        if avg >= 95:   num, rem = 1.00, "Excellent"
        elif avg >= 90: num, rem = 1.50, "Very Good"
        elif avg >= 85: num, rem = 2.00, "Above Average"
        elif avg >= 80: num, rem = 2.50, "Average"
        elif avg == 75: num, rem = 3.00, "Passing"
        elif avg >= 70: num, rem = 3.25, "Conditional"
        else:           num, rem = 5.00, "Failed"
        res_avg.config(text=f"{avg:.2f}")
        res_num.config(text=f"{num:.2f}")
        color = ("#00ffaa" if rem in ["Excellent","Very Good"]
                 else "#00ccff" if rem in ["Above Average","Average"]
                 else "yellow"  if rem == "Passing"
                 else "orange"  if rem == "Conditional"
                 else "#ff4444")
        res_rem.config(text=rem, fg=color)
    def clr():
        for e in [stNum, stName, stSub, pre, mid, fin]: e.delete(0, tk.END)
        cbC.current(0)
        for lbl in [res_avg, res_num, res_rem]: lbl.config(text="", fg="white")
    bf = tk.Frame(win, bg="#000000"); bf.pack(pady=20)
    tk.Button(bf, text="Calculate", command=calc,    bg="#FF0000", fg="white",
              width=10, relief="flat").grid(row=0, column=0, padx=5)
    tk.Button(bf, text="Clear",     command=clr,     bg="#FF0000", fg="white",
              width=10, relief="flat").grid(row=0, column=1, padx=5)
    tk.Button(bf, text="Close", command=win.destroy, bg="#cc0000", fg="white",
              width=10, relief="flat").grid(row=0, column=2, padx=5)

# ===== ACT 6: Simple CRUD App =====
def act6():
    class SimpleCRUDApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Simple CRUD App with ID")
            self.root.geometry("520x420")
            self.users = []
            self.selected_index = None
            self.user_id_counter = 1
            self.build_ui()

        def build_ui(self):
            tk.Label(self.root, text="First Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            self.entry_fname = tk.Entry(self.root)
            self.entry_fname.grid(row=0, column=1, pady=5)
            tk.Label(self.root, text="Last Name").grid(row=1, column=0, padx=10, sticky="w")
            self.entry_lname = tk.Entry(self.root)
            self.entry_lname.grid(row=1, column=1, pady=5)
            tk.Label(self.root, text="Gender").grid(row=2, column=0, padx=10, sticky="w")
            self.gender_var = tk.StringVar()
            tk.Radiobutton(self.root, text="Male",   variable=self.gender_var,
                           value="Male").grid(row=2, column=1, sticky="w")
            tk.Radiobutton(self.root, text="Female", variable=self.gender_var,
                           value="Female").grid(row=2, column=2, sticky="w")
            tk.Label(self.root, text="Address").grid(row=3, column=0, padx=10, sticky="w")
            self.entry_address = tk.Entry(self.root)
            self.entry_address.grid(row=3, column=1, pady=5)
            tk.Label(self.root, text="Username").grid(row=4, column=0, padx=10, sticky="w")
            self.entry_username = tk.Entry(self.root)
            self.entry_username.grid(row=4, column=1, pady=5)
            tk.Label(self.root, text="Password").grid(row=5, column=0, padx=10, sticky="w")
            self.entry_password = tk.Entry(self.root, show="*")
            self.entry_password.grid(row=5, column=1, pady=5)
            tk.Button(self.root, text="Create", command=self.create_user,
                      bg="#28a745", fg="white", width=10).grid(row=6, column=0, padx=5, pady=10)
            tk.Button(self.root, text="Update", command=self.update_user,
                      bg="#007bff", fg="white", width=10).grid(row=6, column=1, padx=5, pady=10)
            tk.Button(self.root, text="Delete", command=self.delete_user,
                      bg="#dc3545", fg="white", width=10).grid(row=6, column=2, padx=5, pady=10)
            tk.Button(self.root, text="Clear",  command=self.clear_fields,
                      bg="#6c757d", fg="white", width=10).grid(row=6, column=3, padx=5, pady=10)
            self.listbox = tk.Listbox(self.root, width=70, height=10)
            self.listbox.grid(row=7, column=0, columnspan=4, padx=10, pady=5)
            self.listbox.bind("<<ListboxSelect>>", self.select_user)

        def create_user(self):
            fname    = self.entry_fname.get().strip()
            lname    = self.entry_lname.get().strip()
            gender   = self.gender_var.get()
            address  = self.entry_address.get().strip()
            username = self.entry_username.get().strip()
            password = self.entry_password.get().strip()
            if not all([fname, lname, gender, address, username, password]):
                messagebox.showwarning("Input Error", "Please fill all fields",
                                       parent=self.root); return
            self.users.append([self.user_id_counter, fname, lname,
                                gender, address, username, password])
            self.user_id_counter += 1
            self.update_listbox()
            self.clear_fields()

        def update_user(self):
            if self.selected_index is None:
                messagebox.showwarning("Select", "Select a user first",
                                       parent=self.root); return
            uid = self.users[self.selected_index][0]
            self.users[self.selected_index] = [
                uid,
                self.entry_fname.get().strip(),
                self.entry_lname.get().strip(),
                self.gender_var.get(),
                self.entry_address.get().strip(),
                self.entry_username.get().strip(),
                self.entry_password.get().strip()
            ]
            self.update_listbox()
            self.clear_fields()
            messagebox.showinfo("Success", "User updated!", parent=self.root)

        def delete_user(self):
            if self.selected_index is None:
                messagebox.showwarning("Select", "Select a user first",
                                       parent=self.root); return
            if messagebox.askyesno("Confirm", "Delete this user?", parent=self.root):
                self.users.pop(self.selected_index)
                self.update_listbox()
                self.clear_fields()

        def update_listbox(self):
            self.listbox.delete(0, tk.END)
            for u in self.users:
                self.listbox.insert(tk.END,
                    f"ID:{u[0]}  |  {u[1]} {u[2]}  |  {u[3]}  |  {u[4]}")

        def select_user(self, event):
            try:
                self.selected_index = self.listbox.curselection()[0]
                u = self.users[self.selected_index]
                self.clear_fields(keep_index=True)
                self.entry_fname.insert(0, u[1])
                self.entry_lname.insert(0, u[2])
                self.gender_var.set(u[3])
                self.entry_address.insert(0, u[4])
                self.entry_username.insert(0, u[5])
                self.entry_password.insert(0, u[6])
            except: pass

        def clear_fields(self, keep_index=False):
            if not keep_index:
                self.selected_index = None
            for e in [self.entry_fname, self.entry_lname,
                      self.entry_address, self.entry_username, self.entry_password]:
                e.delete(0, tk.END)
            self.gender_var.set("")

    win = tk.Toplevel(window)
    app = SimpleCRUDApp(win)
    window.app6 = app

# ===== ACT 7: Payroll Database =====
def act7():
    class PayrollSystem:
        def __init__(self, root):
            self.root = root
            self.root.title("Payroll System")
            self.conn = sqlite3.connect("payroll.db")
            self.cursor = self.conn.cursor()
            self.init_db()
            self.show_login()

        def init_db(self):
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS payroll (
                emp_no TEXT PRIMARY KEY, name TEXT, position TEXT,
                rate REAL, days REAL, gross REAL, sss REAL,
                philhealth REAL, cash_adv REAL, deductions REAL, net REAL)""")
            self.cursor.execute("""CREATE TABLE IF             NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)""")
            self.conn.commit()

        def show_login(self):
            self.clear_screen()
            self.root.geometry("300x300")
            frame = tk.Frame(self.root, padx=20, pady=20)
            frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(frame, text="Payroll System Login",
                     font=("Arial", 13, "bold")).grid(row=0, columnspan=2, pady=15)
            tk.Label(frame, text="Username:").grid(row=1, column=0, sticky="w")
            self.user_ent = tk.Entry(frame, width=22)
            self.user_ent.grid(row=1, column=1, pady=5)
            tk.Label(frame, text="Password:").grid(row=2, column=0, sticky="w")
            self.pass_ent = tk.Entry(frame, show="*", width=22)
            self.pass_ent.grid(row=2, column=1, pady=5)
            tk.Button(frame, text="Login", width=20, bg="blue", fg="white",
                      command=self.login_user).grid(row=3, columnspan=2, pady=10)
            tk.Button(frame, text="Register New Account", width=20,
                      command=self.open_register).grid(row=4, columnspan=2)
            self.root.bind('<Return>', lambda e: self.login_user())

        def login_user(self):
            u = self.user_ent.get()
            p = self.pass_ent.get()
            self.cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?", (u, p))
            if self.cursor.fetchone():
                self.show_main_app()
            else:
                messagebox.showerror("Error", "Invalid Username or Password",
                                     parent=self.root)

        def open_register(self):
            reg = tk.Toplevel(self.root)
            reg.title("Create Account")
            reg.geometry("250x220")
            reg.grab_set()
            tk.Label(reg, text="New Username").pack(pady=5)
            reg_user = tk.Entry(reg); reg_user.pack()
            tk.Label(reg, text="New Password").pack(pady=5)
            reg_pwd = tk.Entry(reg, show="*"); reg_pwd.pack()
            def save_account():
                u = reg_user.get().strip()
                p = reg_pwd.get().strip()
                if not u or not p:
                    messagebox.showerror("Error", "All fields required", parent=reg); return
                try:
                    self.cursor.execute("INSERT INTO users VALUES (?, ?)", (u, p))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Account Created!", parent=reg)
                    reg.destroy()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Username already taken", parent=reg)
            tk.Button(reg, text="Save Account", command=save_account,
                      bg="green", fg="white").pack(pady=15)

        def show_main_app(self):
            self.clear_screen()
            self.root.geometry("1100x600")
            frame = tk.Frame(self.root, padx=20, pady=20)
            frame.pack()
            tk.Label(frame, text="Emp No:").grid(row=0, column=0)
            self.entry_emp = tk.Entry(frame); self.entry_emp.grid(row=0, column=1)
            tk.Label(frame, text="Name:").grid(row=1, column=0)
            self.entry_name = tk.Entry(frame); self.entry_name.grid(row=1, column=1)
            tk.Label(frame, text="Position:").grid(row=2, column=0)
            self.combo_pos = ttk.Combobox(frame,
                values=["Manager","Staff","Dev","HR"], state="readonly")
            self.combo_pos.grid(row=2, column=1)
            tk.Label(frame, text="Rate:").grid(row=3, column=0)
            self.entry_rate = tk.Entry(frame); self.entry_rate.grid(row=3, column=1)
            tk.Label(frame, text="Days:").grid(row=4, column=0)
            self.entry_days = tk.Entry(frame); self.entry_days.grid(row=4, column=1)
            tk.Label(frame, text="SSS:").grid(row=0, column=2, padx=10)
            self.entry_sss = tk.Entry(frame); self.entry_sss.grid(row=0, column=3)
            tk.Label(frame, text="PhilHealth:").grid(row=1, column=2, padx=10)
            self.entry_phil = tk.Entry(frame); self.entry_phil.grid(row=1, column=3)
            tk.Label(frame, text="Cash Adv:").grid(row=2, column=2, padx=10)
            self.entry_cash = tk.Entry(frame); self.entry_cash.grid(row=2, column=3)
            btn_frame = tk.Frame(self.root); btn_frame.pack(pady=10)
            tk.Button(btn_frame, text="Add",    width=10,
                      command=self.add_record).grid(row=0, column=0, padx=5)
            tk.Button(btn_frame, text="Update", width=10,
                      command=self.update_record).grid(row=0, column=1, padx=5)
            tk.Button(btn_frame, text="Delete", width=10,
                      command=self.delete_record).grid(row=0, column=2, padx=5)
            tk.Button(btn_frame, text="Logout", width=10,
                      command=self.show_login).grid(row=0, column=3, padx=5)
            columns = ("ID","Name","Position","Rate","Days",
                       "Gross","SSS","PH","Cash","Ded","Net")
            self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=90, anchor="center")
            self.tree.pack(fill="both", expand=True, padx=10, pady=10)
            self.tree.bind("<ButtonRelease-1>", self.select_record)
            self.load_data()

        def compute_values(self):
            try:
                rate  = float(self.entry_rate.get())
                days  = float(self.entry_days.get())
                sss   = float(self.entry_sss.get())
                phil  = float(self.entry_phil.get())
                cash  = float(self.entry_cash.get())
                gross      = rate * days
                deductions = sss + phil + cash
                net        = gross - deductions
                return gross, deductions, net
            except ValueError:
                messagebox.showerror("Error", "Invalid numeric input", parent=self.root)
                return None

        def add_record(self):
            if not self.entry_emp.get() or not self.entry_name.get():
                messagebox.showerror("Error", "Required fields missing", parent=self.root); return
            result = self.compute_values()
            if result:
                gross, deductions, net = result
                try:
                    self.cursor.execute(
                        "INSERT INTO payroll VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                        (self.entry_emp.get(), self.entry_name.get(),
                         self.combo_pos.get(), self.entry_rate.get(),
                         self.entry_days.get(), gross, self.entry_sss.get(),
                         self.entry_phil.get(), self.entry_cash.get(),
                         deductions, net))
                    self.conn.commit()
                    self.load_data()
                    self.clear_fields()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Employee Number already exists",
                                         parent=self.root)

        def update_record(self):
            selected = self.tree.focus()
            if not selected:
                messagebox.showerror("Error", "Select a record", parent=self.root); return
            result = self.compute_values()
            if result:
                gross, deductions, net = result
                self.cursor.execute("""UPDATE payroll SET
                    name=?, position=?, rate=?, days=?, gross=?,
                    sss=?, philhealth=?, cash_adv=?, deductions=?, net=?
                    WHERE emp_no=?""",
                    (self.entry_name.get(), self.combo_pos.get(),
                     self.entry_rate.get(), self.entry_days.get(), gross,
                     self.entry_sss.get(), self.entry_phil.get(),
                     self.entry_cash.get(), deductions, net,
                     self.entry_emp.get()))
                self.conn.commit()
                self.load_data()

        def delete_record(self):
            selected = self.tree.focus()
            if not selected: return
            emp_no = self.tree.item(selected)['values'][0]
            if messagebox.askyesno("Confirm", "Delete this record?", parent=self.root):
                self.cursor.execute("DELETE FROM payroll WHERE emp_no=?", (emp_no,))
                self.conn.commit()
                self.load_data()

        def load_data(self):
            for row in self.tree.get_children():
                self.tree.delete(row)
            self.cursor.execute("SELECT * FROM payroll")
            for row in self.cursor.fetchall():
                self.tree.insert("", tk.END, values=row)

        def select_record(self, event):
            selected = self.tree.focus()
            data = self.tree.item(selected, "values")
            if data:
                self.clear_fields()
                self.entry_emp.insert(0, data[0])
                self.entry_name.insert(0, data[1])
                self.combo_pos.set(data[2])
                self.entry_rate.insert(0, data[3])
                self.entry_days.insert(0, data[4])
                self.entry_sss.insert(0, data[6])
                self.entry_phil.insert(0, data[7])
                self.entry_cash.insert(0, data[8])

        def clear_fields(self):
            self.entry_emp.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
            self.combo_pos.set("")
            self.entry_rate.delete(0, tk.END)
            self.entry_days.delete(0, tk.END)
            self.entry_sss.delete(0, tk.END)
            self.entry_phil.delete(0, tk.END)
            self.entry_cash.delete(0, tk.END)

        def clear_screen(self):
            for widget in self.root.winfo_children():
                widget.destroy()

    win = tk.Toplevel(window)
    app = PayrollSystem(win)
    window.app7 = app

# ===== ACT 8: Student Grading Management System =====
def act8():
    class GradingSystemPro:
        def __init__(self, root):
            self.root = root
            self.root.title("Student Grading System Pro")
            self.root.geometry("400x300")
            self.init_db()
            self.show_login()

        def get_connection(self):
            return sqlite3.connect("grading_system.db")

        def init_db(self):
            with self.get_connection() as conn:
                conn.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id TEXT, name TEXT, course TEXT, subject TEXT,
                    prelim REAL, midterm REAL, final REAL,
                    average REAL, num_val TEXT, remark TEXT)""")
                conn.execute("""CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY, password TEXT)""")

        def calculate_grade_details(self, p, m, f):
            avg = (p * 0.30) + (m * 0.30) + (f * 0.40)
            if avg >= 95:   return round(avg,2), "1.0",  "Excellent"
            elif avg >= 90: return round(avg,2), "1.25", "Very Good"
            elif avg >= 85: return round(avg,2), "1.5",  "Above Average"
            elif avg >= 80: return round(avg,2), "1.75", "Average"
            elif avg >= 75: return round(avg,2), "2.0",  "Passing"
            elif avg >= 70: return round(avg,2), "3.0",  "Conditional"
            else:           return round(avg,2), "5.0",  "Failed"

        def show_login(self):
            self.clear_screen()
            self.root.geometry("400x300")
            frame = tk.Frame(self.root, padx=20, pady=20)
            frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(frame, text="Grading System Login",
                     font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=15)
            tk.Label(frame, text="Username:").grid(row=1, column=0, sticky="w")
            self.user_ent = tk.Entry(frame, width=25)
            self.user_ent.grid(row=1, column=1, pady=5)
            tk.Label(frame, text="Password:").grid(row=2, column=0, sticky="w")
            self.pass_ent = tk.Entry(frame, show="*", width=25)
            self.pass_ent.grid(row=2, column=1, pady=5)
            tk.Button(frame, text="Login", width=20, bg="#28a745", fg="white",
                      command=self.login_user).grid(row=3, columnspan=2, pady=10)
            tk.Button(frame, text="Create Account", width=20, bg="#17a2b8", fg="white",
                      command=self.register_user).grid(row=4, columnspan=2)
            self.root.bind('<Return>', lambda e: self.login_user())

        def login_user(self):
            u = self.user_ent.get()
            p = self.pass_ent.get()
            with self.get_connection() as conn:
                row = conn.execute(
                    "SELECT * FROM users WHERE username=? AND password=?",
                    (u, p)).fetchone()
            if row:
                self.show_main_app()
            else:
                messagebox.showerror("Error", "Invalid credentials.", parent=self.root)

        def register_user(self):
            u = self.user_ent.get().strip()
            p = self.pass_ent.get().strip()
            if not u or not p:
                messagebox.showwarning("Warning", "Fill all fields", parent=self.root); return
            try:
                with self.get_connection() as conn:
                    conn.execute("INSERT INTO users VALUES (?, ?)", (u, p))
                messagebox.showinfo("Success", "Account created!", parent=self.root)
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already taken.", parent=self.root)

        def show_main_app(self):
            self.clear_screen()
            self.root.geometry("1100x600")
            self.left_frame = tk.LabelFrame(self.root, text="Entry Form", padx=10, pady=10)
            self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
            self.right_frame = tk.Frame(self.root, padx=10, pady=10)
            self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            self.inputs = {}
            fields = [("Student ID","sid"),("Full Name","name"),("Subject","subj"),
                      ("Prelim","p"),("Midterm","m"),("Final","f")]
            for label, key in fields:
                tk.Label(self.left_frame, text=label).pack(anchor="w")
                entry = tk.Entry(self.left_frame)
                entry.pack(fill=tk.X, pady=(0,5))
                self.inputs[key] = entry
            tk.Label(self.left_frame, text="Course").pack(anchor="w")
            self.combo_course = ttk.Combobox(self.left_frame,
                values=["BSIT","BSCS","BSIS","BSDS"], state="readonly")
            self.combo_course.pack(fill=tk.X, pady=(0,15))
            actions = [
                ("Add Student",     self.add_record,    "#28a745"),
                ("Update Selected", self.update_record, "#007bff"),
                ("Delete Selected", self.delete_record, "#dc3545"),
                ("Clear Fields",    self.clear_fields,  "#6c757d"),
                ("Logout",          self.show_login,    "#343a40"),
            ]
            for txt, cmd, clr in actions:
                tk.Button(self.left_frame, text=txt, command=cmd,
                          bg=clr, fg="white", font=("Arial",9,"bold")).pack(fill=tk.X, pady=3)
            cols = ("Student ID","Name","Course","Subject","P","M","F","Avg","Grade","Remark")
            self.tree = ttk.Treeview(self.right_frame, columns=cols, show="headings")
            for col in cols:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=95, anchor="center")
            self.tree.pack(fill=tk.BOTH, expand=True)
            self.tree.bind("<<TreeviewSelect>>", self.load_selection)
            self.refresh_table()

        def add_record(self):
            try:
                p = float(self.inputs['p'].get())
                m = float(self.inputs['m'].get())
                f = float(self.inputs['f'].get())
                avg, nv, rem = self.calculate_grade_details(p, m, f)
                with self.get_connection() as conn:
                    conn.execute("""INSERT INTO students
                        (student_id,name,course,subject,prelim,midterm,final,average,num_val,remark)
                        VALUES (?,?,?,?,?,?,?,?,?,?)""",
                        (self.inputs['sid'].get(), self.inputs['name'].get(),
                         self.combo_course.get(),  self.inputs['subj'].get(),
                         p, m, f, avg, nv, rem))
                self.refresh_table()
                self.clear_fields()
            except:
                messagebox.showerror("Error", "Check numeric inputs.", parent=self.root)

        def update_record(self):
            selected = self.tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Select a record first.", parent=self.root); return
            current_sid = self.tree.item(selected)['values'][0]
            try:
                p = float(self.inputs['p'].get())
                m = float(self.inputs['m'].get())
                f = float(self.inputs['f'].get())
                avg, nv, rem = self.calculate_grade_details(p, m, f)
                with self.get_connection() as conn:
                    conn.execute("""UPDATE students SET
                        student_id=?, name=?, course=?, subject=?,
                        prelim=?, midterm=?, final=?, average=?, num_val=?, remark=?
                        WHERE student_id=?""",
                        (self.inputs['sid'].get(), self.inputs['name'].get(),
                         self.combo_course.get(),  self.inputs['subj'].get(),
                         p, m, f, avg, nv, rem, current_sid))
                self.refresh_table()
                messagebox.showinfo("Success", "Record updated!", parent=self.root)
            except:
                messagebox.showerror("Error", "Update failed.", parent=self.root)

        def delete_record(self):
            selected = self.tree.selection()
            if not selected:
                messagebox.showwarning("Warning", "Select a record first.", parent=self.root); return
            sid = self.tree.item(selected)['values'][0]
            if messagebox.askyesno("Confirm", "Delete this student?", parent=self.root):
                with self.get_connection() as conn:
                    conn.execute("DELETE FROM students WHERE student_id=?", (sid,))
                self.refresh_table()

        def refresh_table(self):
            self.tree.delete(*self.tree.get_children())
            with self.get_connection() as conn:
                cursor = conn.execute("""SELECT student_id, name, course, subject,
                    prelim, midterm, final, average, num_val, remark FROM students""")
                for row in cursor.fetchall():
                    self.tree.insert("", tk.END, values=row)

        def load_selection(self, event):
            sel = self.tree.selection()
            if not sel: return
            v = self.tree.item(sel)['values']
            self.clear_fields()
            self.inputs['sid'].insert(0, v[0])
            self.inputs['name'].insert(0, v[1])
            self.combo_course.set(v[2])
            self.inputs['subj'].insert(0, v[3])
            self.inputs['p'].insert(0, v[4])
            self.inputs['m'].insert(0, v[5])
            self.inputs['f'].insert(0, v[6])

        def clear_fields(self):
            for e in self.inputs.values():
                e.delete(0, tk.END)
            self.combo_course.set("")

        def clear_screen(self):
            for widget in self.root.winfo_children():
                widget.destroy()

    win = tk.Toplevel(window)
    app = GradingSystemPro(win)
    window.app8 = app

# ===== Main Window =====
def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.quit()

def about():
    messagebox.showinfo("About",
        "Integrated Programs System\n\n"
        "Activities:\n"
        "1. Student Information\n"
        "2. Sales Program\n"
        "3. Grade Calculator\n"
        "4. Simple Payroll System\n"
        "5. Grading System (Combobox)\n"
        "6. Simple CRUD App\n"
        "7. Payroll Database\n"
        "8. Student Grading Management\n\n"
        "Acts 7 & 8 require login.\n"
        "First time? Use 'Register' on the login screen."
    )

init_all_dbs()

window = tk.Tk()
window.title("Integrated Programs System")
window.geometry("800x500")
window.configure(bg=BG_DARK)

# ===== Menu Bar =====
menubar = tk.Frame(window, bg=BG_MENU, height=35)
menubar.pack(fill=tk.X)
menubar.pack_propagate(False)

menu_style = {
    "bg": BG_MENU, "fg": TEXT_LIGHT, "font": ("Segoe UI", 10),
    "relief": "flat", "padx": 15, "pady": 5, "cursor": "hand2"
}

file_btn = tk.Button(menubar, text="Activities", **menu_style)
file_btn.pack(side=tk.LEFT, padx=2)
help_btn = tk.Button(menubar, text="Help", **menu_style)
help_btn.pack(side=tk.LEFT, padx=2)

file_menu = tk.Menu(window, tearoff=0, bg=BG_MENU, fg=TEXT_LIGHT, font=("Segoe UI", 10))
file_menu.add_command(label="── Midterm Activities ──", state="disabled")
file_menu.add_separator()
file_menu.add_command(label="1. Student Information",          command=act1)
file_menu.add_command(label="2. Sales Program",                command=act2)
file_menu.add_command(label="3. Grade Calculator",             command=act3)
file_menu.add_command(label="4. Simple Payroll System",        command=act4)
file_menu.add_command(label="5. Grading System (Combobox)",    command=act5)
file_menu.add_separator()
file_menu.add_command(label="── Final Activities ──", state="disabled")
file_menu.add_separator()
file_menu.add_command(label="6. Simple CRUD App",                   command=act6)
file_menu.add_command(label="7. Payroll Database",                  command=act7)
file_menu.add_command(label="8. Student Grading Management System", command=act8)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)

help_menu = tk.Menu(window, tearoff=0, bg=BG_MENU, fg=TEXT_LIGHT, font=("Segoe UI", 10))
help_menu.add_command(label="About", command=about)

def show_file_menu(event):
    file_menu.post(event.widget.winfo_rootx(), event.widget.winfo_rooty() + 30)

def show_help_menu(event):
    help_menu.post(event.widget.winfo_rootx(), event.widget.winfo_rooty() + 30)

file_btn.bind("<Button-1>", show_file_menu)
help_btn.bind("<Button-1>", show_help_menu)

def on_enter(btn): btn.config(bg=HOVER_BG, fg=TEXT_HOVER)
def on_leave(btn): btn.config(bg=BG_MENU,  fg=TEXT_LIGHT)

for btn in [file_btn, help_btn]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(b))

# ===== Welcome Screen =====
tk.Label(window,
    text=(
        "Welcome to Integrated Programs System\n\n"
        "Click Activities menu to select a program:\n\n"
        "  Midterm:\n"
        "  • Student Information\n"
        "  • Sales Program\n"
        "  • Grade Calculator\n"
        "  • Simple Payroll System\n"
        "  • Grading System (Combobox)\n\n"
        "  Final:\n"
        "  • Simple CRUD App\n"
        "  • Payroll Database           ← requires login\n"
        "  • Student Grading Management ← requires login\n\n"
        "First time? Use 'Register' on the login screen."
    ),
    font=("Segoe UI", 11), bg=BG_DARK, fg=TEXT_LIGHT,
    justify="left", anchor="center"
).pack(expand=True)

window.mainloop()