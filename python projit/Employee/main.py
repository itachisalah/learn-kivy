import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import ttk
from tkcalender import Calender, DateEntry
from datetime import datetime
import pymysql

conn = pymysql.connect()

app = tk.Tk()
app.geometry('850x655+350+150')
app.title('Employee Management System')
app.configure(background='#6A6A6A')
app.resizable(width=False, height=False)

icon = tk.PhotoImage(file='')
app.call('wm','iconphoto',app._w,icon)

emp_id = tk.StringVar()
emp_name = tk.StringVar()
emp_age = tk.StringVar()
emp_email = tk.StringVar()
emp_phone = tk.StringVar()
emp_salary = tk.StringVar()

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS emp_data(
    ID TEXT NOT NULL PRIMARY KEY,NAme TEXT NOT NULL,
    Age TEXT NOT NULL,Email TEXT NOT NULL,
    Phone TEXT NOT NULL, Salary TEXT NOT NULL,
    Date_save TEXT NOT NULL""")
cur.close()
App_title_frame = tk.Frame(app,width=830, height=60,bg='#4F5A60')
App_title_frame.place(x=10,y=10)

app_date = datetime.now()
x_date =app_date.strftime('%Y-%m-%d')

def|
date_label = tk.Label(app,text=x_date,bg='#4F5A60',fg='#E8EFF',font=('Arial Greek',
                      10,'bold'),)
date_label.place(x=70,y=22)

my_app_title = tk.Label(App_title_frame)



app.mainloop()




