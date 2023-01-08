from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
salah = Tk()
salah.title('GM')
salah.geometry('800x600+280+180')
salah.resizable(True,True)

F1 = Frame(salah ,width=2000 , height =2000, bg = 'black')
F1.place(x=0,y=0)
L = Label(F1,text='Sing On',fg='white',bg='black',font=('Tajawal,12,bold'))
L.place(x=350,y=10)
L1 = Label(F1,text='System   . . . . . . . . . . .  :   CYRUSPR1',fg='green',bg='black',font=('Tajawal',12,'bold'))
L1.place(x=500,y=20)
L1 = Label(F1,text='Subsystem  . . . . . . . .  :   QINTER',fg='green',bg='black',font=('Tajawal',12,'bold'))
L1.place(x=500,y=40)
L1 = Label(F1,text='Display  . . . . . . . . . . . . :   QPADEVO1J4 ',fg='green',bg='black',font=('Tajawal',12,'bold'))
L1.place(x=500,y=60)

L1 = Label(F1,text='User . . . . . . . . . . . . . . . . . .  . .',fg='green',bg='black',font=('Tajawal',12,'bold'))
L1.place(x=200,y=160)
L2 = Label(F1,text='Password . . . . . . .  . . . . . . . . ',fg='green',bg='black',font=('Tajawal',12,'bold'))
L2.place(x=200,y=180)
L3 = Label(F1,text='Program/Procedure  . . . . . .',fg='green',bg='black',font=('Tajawal',12,'bold'))
L3.place(x=200,y=200)
L4 = Label(F1,text='Menu . . . . . . . . . . . . . . . . . . . .',fg='green',bg='black',font=('Tajawal',12,'bold'))
L4.place(x=200,y=220)
L5 = Label(F1,text='Current library. . . . . . . . . . . .  ',fg='green',bg='black',font=('Tajawal',12,'bold'))
L5.place(x=200,y=240)

En1 = Entry(F1,fg='green',bg='black' ,font=('Tajawal',10,'bold'),justify='center')
En1.place(x=420,y=160)
En2 = Entry(F1 ,fg='green',bg='black',font=('Tajawal',10,'bold'),justify='center')
En2.place(x=420,y=180)
En3 = Entry(F1 ,fg='green',bg='black',font=('Tajawal',10,'bold'),justify='center')
En3.place(x=420,y=200)
En4 = Entry(F1 ,fg='green',bg='black',font=('Tajawal',10,'bold'),justify='center')
En4.place(x=420,y=220)
En5 = Entry(F1 ,fg='green',bg='black',font=('Tajawal',10,'bold'),justify='center')
En5.place(x=420,y=240)



salah.mainloop()