import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
# from tkcalendar import DateEntry

root = tk.Tk()
root.geometry('300x200')
root.resizable(False,False)
root.title("Retirement Calculator")

date = tk.StringVar()
vacation = tk.StringVar()


def login_clicked():
    res.config(text="result"+str(eval(entry.get)))
    showinfo(
        title='Information',
        message = msg
    )
calc = ttk.Frame(root)
calc.pack(padx=10,pady=10, fill='x', expand=True)

# Retirement date
date_label = ttk.Label(calc, text = "Retirement Date")
date_label.pack(fill='x', expand=True)

date_entry=ttk.Entry(calc, textvariable=date)
date_entry.pack(fill='x', expand=True)
date_entry.focus()

vacation_label = ttk.Label(calc, text="Vacation days")
vacation_label.pack(fill='x', expand=True)

vacation_entry = ttk.Entry(calc, textvariable=vacation)
vacation_entry.pack(fill='x', expand=True)
#
res.pack()

calculate_button = ttk.Button(calc, text="Calculate", command = login_clicked)
calculate_button.pack(fill='x', expand = True, pady = 10)
#
root.mainloop()
