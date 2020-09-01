from tkinter import *
from tkinter import messagebox
from datetime import date, timedelta

root = Tk()
root.title("Date Counter")

def get_today(input_y, input_m, input_d):
    
    today=date.today()
    y = str(today.year)
    m = str(today.month)
    d = str(today.day)

    input_y.insert(0, y)
    input_m.set(m)
    input_d.set(d)

def cal_days_between(d1_year, d1_month, d1_day, d2_year, d2_month, d2_day, inc_var):
    
    try:

        y1 = int(d1_year.get())
        m1 = int(d1_month.get())
        d1 = int(d1_day.get())
        y2 = int(d2_year.get())
        m2 = int(d2_month.get())
        d2 = int(d2_day.get())

        date1 = date(y1, m1, d1)
        date2 = date(y2, m2, d2)

        inc = inc_var.get()

        delta = date2 - date1

        if inc == "on":
            delta = str(abs(delta.days) + 1)
        else:
            delta = str(abs(delta.days))
        
        successbox = messagebox.showinfo("Result", "There are " + str(delta) + " days between these two dates.")
    
    except:

        errorbox = messagebox.showerror("Error", "Please input valid date values.")

def cal_days_before_after(d_year, d_month, d_day, days_entry, before_after, inc_var):

    try:

        y = int(d_year.get())
        m = int(d_month.get())
        d = int(d_day.get())

        date_input = date(y, m, d)

        inc = inc_var.get()

        days_to = int(days_entry.get())

        b_c = before_after.get()

        if inc == "on":
            days_to += 1

        if b_c == "Before":
            date_result = date_input - timedelta(days=days_to)
        else:
            date_result = date_input + timedelta(days=days_to)
        
        if inc == "on":
            successbox = messagebox.showinfo("Result", str(days_to-1) + " day(s) " + b_c.lower() + " " + str(date_input) + " is " + str(date_result))
        else:
            successbox = messagebox.showinfo("Result", str(days_to) + " day(s) " + b_c.lower() + " " + str(date_input) + " is " + str(date_result))

    except:

        errorbox = messagebox.showerror("Error", "Please input valid date values.")

# GUI for calculating days between two dates

month1 = StringVar()
day1 = StringVar()
month2 = StringVar()
day2 = StringVar()

months1_options = [str(m) for m in range(1, 13)]
days1_options = [str(d) for d in range(1, 32)]
months2_options = [str(m) for m in range(1, 13)]
days2_options = [str(d) for d in range(1, 32)]

frame_1 = LabelFrame(root, text="Calculate days between two dates.")
frame_1.pack(padx=10, pady=10, ipadx=40)

label_d1 = Label(frame_1, text="Date 1")
label_d1.grid(row=0, column=0)

label_d1_year = Label(frame_1, text="Year")
label_d1_year.grid(row=0, column=1)
d1_year = Entry(frame_1, width=6)
d1_year.grid(row=0, column=2)

label_d1_month = Label(frame_1, text="Month")
label_d1_month.grid(row=0, column=3)
d1_month = OptionMenu(frame_1, month1, *months1_options)
d1_month.grid(row=0, column=4)

label_d1_day = Label(frame_1, text="Day")
label_d1_day.grid(row=0, column=5)
d1_day = OptionMenu(frame_1, day1, *days1_options)
d1_day.grid(row=0, column=6)

button_today1 = Button(frame_1, text="Today", command=lambda: get_today(d1_year, month1, day1))
button_today1.grid(row=0, column=7)

label_d2 = Label(frame_1, text="Date 2")
label_d2.grid(row=1, column=0)

label_d2_year = Label(frame_1, text="Year")
label_d2_year.grid(row=1, column=1)
d2_year = Entry(frame_1, width=6)
d2_year.grid(row=1, column=2)

label_d2_month = Label(frame_1, text="Month")
label_d2_month.grid(row=1, column=3)
d2_month = OptionMenu(frame_1, month2, *months2_options)
d2_month.grid(row=1, column=4)

label_d2_day = Label(frame_1, text="Day")
label_d2_day.grid(row=1, column=5)
d2_day = OptionMenu(frame_1, day2, *days2_options)
d2_day.grid(row=1, column=6)

button_today2 = Button(frame_1, text="Today", command=lambda: get_today(d2_year, month2, day2))
button_today2.grid(row=1, column=7)

inclusive_var = StringVar()
inclusive = Checkbutton(frame_1, text="Dates inclusive", variable=inclusive_var, onvalue="on", offvalue="off")
inclusive.deselect()
inclusive.grid(row=2, column=0)

button_days_between = Button(frame_1, text="Calculate", command=lambda: cal_days_between(d1_year, month1, day1, d2_year, month2, day2, inclusive_var))
button_days_between.grid(row=3, column=0)

# GUI for showing the date of x days before/after a specified date

month = StringVar()
day = StringVar()
before_after = StringVar()

months_options = [str(m) for m in range(1, 13)]
days_options = [str(d) for d in range(1, 32)]

frame_2 = LabelFrame(root, text="Showing the date of a specified number of days before/after a specified date.")
frame_2.pack(padx=10, pady=10)

label_d = Label(frame_2, text="Date")
label_d.grid(row=0, column=0)

label_d_year = Label(frame_2, text="Year")
label_d_year.grid(row=0, column=1)
d_year = Entry(frame_2, width=6)
d_year.grid(row=0, column=2)

label_d_month = Label(frame_2, text="Month")
label_d_month.grid(row=0, column=3)
d_month = OptionMenu(frame_2, month, *months_options)
d_month.grid(row=0, column=4)

label_d_day = Label(frame_2, text="Day")
label_d_day.grid(row=0, column=5)
d_day = OptionMenu(frame_2, day, *days_options)
d_day.grid(row=0, column=6)

button_today = Button(frame_2, text="Today", command=lambda: get_today(d_year, month, day))
button_today.grid(row=0, column=7)

entry_days = Entry(frame_2, width=6)
entry_days.grid(row=1, column=0)

label_days = Label(frame_2, text="days")
label_days.grid(row=1, column=1)

before_after.set("Before")

radiobtn_before = Radiobutton(frame_2, text="Before", variable=before_after, value="Before")
radiobtn_before.grid(row=1, column=2)

radiobtn_after = Radiobutton(frame_2, text="After", variable=before_after, value="After")
radiobtn_after.grid(row=1, column=3)

inclusive_var_2 = StringVar()
inclusive_2 = Checkbutton(frame_2, text="Dates inclusive", variable=inclusive_var_2, onvalue="on", offvalue="off")
inclusive_2.deselect()
inclusive_2.grid(row=1, column=4)

button_days_before_after = Button(frame_2, text="Calculate", command=lambda: cal_days_before_after(d_year, month, day, entry_days, before_after, inclusive_var_2))
button_days_before_after.grid(row=2, column=0)

root.mainloop()