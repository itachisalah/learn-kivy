from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
salah = Tk()
salah.title('MCARREFOUR')
salah.iconbitmap('D:\\salah.jfif')
salah.geometry('800x450+280+180')
salah.resizable(True,True)
title = Label(salah,text='Super Market System', fg='gold',bg='black',font=('Tajawal',16,'bold'))
title.pack(fill=X)

u1='https://www.facebook.com'
u2='salaheddinegourtite@gail.com'
u3='0595394559'
def Open1():
    webbrowser.open_new(u1)
def Open2():
    webbrowser.open_new(u2)
def Open3():
    webbrowser.open_new(u3)
def about1():
    messagebox.showinfo('salaheddine','gourtite')
def about2():
    messagebox.showinfo('carrefour','Python')
def log():
    user =En1.get()
    passw=En2.get()
    if user == 'rshs056' and passw =='123456':
        messagebox.showinfo('welcom','Don')
    else:
        messagebox.showerror('Error','Sorry not Don')

F1 = Frame(salah ,width=230 , height =420, bg = '#0B2F3A')
F1.place(x=570,y=30)
Title1 = Label(F1,text='CARREFOUR MAJID AL FUTTIM', bg='#0B2F3A', fg='white',font=('Tajawal',9,'bold'))
Title1.place(x=20,y=20)
Title2 = Label(F1,text='SALAHEDDINE GOURITE', bg='#0B2F3A', fg='white',font=('Tajawal',9,'bold'))
Title2.place(x=40,y=60)
Title3 = Label(F1,text='CONTACT US', bg='#0B2F3A', fg='white',font=('Tajawal',9,'bold'))
Title3.place(x=70,y=100)

B1 = Button(F1,text='our account on facebook',width=26,fg='white',bg='#DBA901',font=('Tajawal',10,'bold'),command=Open1)
B1.place(x=6,y=130)
B2 = Button(F1,text='our account on Gmail',width=26,fg='white',bg='#DBA901',font=('Tajawal',10,'bold'),command=Open2)
B2.place(x=6,y=177)
B3 = Button(F1,text='our account on Namber',width=26,fg='white',bg='#DBA901',font=('Tajawal',10,'bold'),command=Open3)
B3.place(x=6,y=224)
B4 = Button(F1,text='Developer overview',width=26,fg='white',bg='#DBA901',font=('Tajawal',10,'bold'),command=about1)
B4.place(x=6,y=271)
B5 = Button(F1,text='Project overview',width=26,fg='white',bg='#DBA901',font=('Tajawal',10,'bold'),command=about2)
B5.place(x=6,y=318)
B6 = Button(F1,text='EXIT',width=26,fg='white',bg='#DBA901',font=('Tajawal',10,'bold'),command=quit)
B6.place(x=6,y=365)

photo = PhotoImage(file="D:\\carrefour.png")
imo = Label(salah , image=photo)
imo.place(x=120,y=60 , width=350 , height=207)

F2 = Frame(salah , width=570 , height=120 , bg='#0B2F3A')
F2.place(x=0,y=330)
photo1 = PhotoImage(file='D:\\logoo.png')
imo1 = Label(salah, image=photo1)
imo1.place(x=0 ,y=335 ,width=180,height=120)
L1 = Label(F2,text='USER',fg='gold',bg='#0B2F3A',font=('Tajawal',12,'bold'))
L1.place(x=186,y=20)
L2 = Label(F2,text='PASSWORD',fg='gold',bg='#0B2F3A',font=('Tajawal',12,'bold'))
L2.place(x=186,y=70)
En1 = Entry(F2 ,font=('Tajawal',10),justify='center')
En1.place(x=290,y=20)
En2 = Entry(F2 ,font=('Tajawal',10),justify='center')
En2.place(x=290,y=70)

B = Button(F2,text='LOG in',bg='#DBA901',font=('Tajawal',12),width=12,height=3,command=log)
B.place(x=446,y=22)





salah.mainloop()
