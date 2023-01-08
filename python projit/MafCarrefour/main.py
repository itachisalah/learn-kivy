import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import ttk
#from tkcalender import Calendar, DateEntry
from datetime import datetime
import sqlite3

conn = sqlite3.connect('employee.db')

app=tk.Tk()
app.geometry('850x655+350+150')
app.title('Employee Management System MAF Carrefour')
app.configure(background='#6A6A6A')
app.resizable(width=False,height=False)

icon = tk.PhotoImage(file='carrefour.png')
app.call('wm','iconphoto',app._w,icon)




app.mainloop()
