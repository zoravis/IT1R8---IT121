from tkinter import Tk,Button
from tkcalendar import DateEntry
def get_date():
    selected_date = cal.get()
    print(f"Selected date: {selected_date}")
root = Tk()
cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack()
btn = Button(root, text="Click Here To Return a Date ", command=get_date)
btn.pack()
root.mainloop()