from tkinter import *

salah = Tk()
salah.geometry('500x400')
salah.title('salaheddine Gourtite [System]')
salah.resizable(False,False)

#==========[Buttons + photos]===========

login = PhotoImage(file='photo/login.png')
logo = PhotoImage(file='photo/logo.png')
signup = PhotoImage(file='photo/signup.png')
close = PhotoImage(file='photo/close.png')

logo_lab = Label(salah,image=logo)
logo_lab.place(x=1,y=1)

#============[Button]===========

login_btn= Button(salah,
                  text='Login',
                  fg='black',
                  width='125',
                  bg='white',
                  cursor='hand2',
                  bd=1,
                  relief=SOLID,
                  image=login,
                  compound=TOP
                  )
login_btn.place(x=70,y=233)



salah.mainloop()