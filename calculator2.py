import tkinter as tk
from tkinter import *
from datetime import date, datetime
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# import math
today = date.today()
base = Tk()
base.geometry("400x300")
base.config(bg="#F7DC6F")
base.resizable(width=False,height=False)
base.title('Retirement Calculator!')
# l1 = tk.Label(window,text="The Age Calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
# l2 = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")
#
# l_d=tk.Label(window,text="Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
# l_m=tk.Label(window,text="Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
# l_y=tk.Label(window,text="Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
# e1=tk.Entry(window,width=5)
# e2=tk.Entry(window,width=5)
# e3=tk.Entry(window,width=5)
#
# b1=tk.Button(window,text="Calculate Age!",font=("Arial",13),command=get_age)
#
# l3 = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
# t1=tk.Text(window,width=5,height=0,state="disabled")
#
# b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)
# l1.place(x=70,y=5)
# l2.place(x=10,y=40)
# l_d.place(x=100,y=70)
# l_m.place(x=100,y=95)
# l_y.place(x=100,y=120)
# e1.place(x=180,y=70)
# e2.place(x=180,y=95)
# e3.place(x=180,y=120)
# b1.place(x=100,y=150)
# l3.place(x=50,y=200)
# t1.place(x=240,y=203)

# base.geometry('300x200')
# base.resizable(False,False)
# base.title("Retirement Calculator")

# date = tk.Entry()


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
