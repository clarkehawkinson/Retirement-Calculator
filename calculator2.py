import tkinter as tk
from tkinter import *
from datetime import date, datetime

today = date.today()

base = Tk()
base.geometry("400x300")
base.config(bg="Blue")
base.resizable(width=False,height=False)
base.title('Retirement Calculator!')

def retire():

    m = int(month_r.get())
    d = int(day_r.get())
    y = int(year_r.get())
    v = int(vacation.get())
    ret = date(year = y, month = m, day = d)
    total_days = ret - today
    message = total_days
    print(total_days)
    msg = Message(base, text = total_days)
    total_label = msg
    total_label.pack()
    # weeks = total_days%7
    # message = weeks


Label(base, text = "Month").pack()
month_r=Entry(base, width = 7)
month_r.pack()

Label(base, text = "Day").pack()
day_r= Entry(base, width = 7)
day_r.pack()

Label(base, text = "Year").pack()
year_r = Entry(base, width = 7)
year_r.pack()

Label(base, text = "Vacation Days").pack()
vacation = Entry(base, width = 5)
vacation.pack()

Button(base, text = "Calculate", command = retire).pack()

total_label=Label(base, text = "total is: ")
total_label.pack()


base.mainloop()
