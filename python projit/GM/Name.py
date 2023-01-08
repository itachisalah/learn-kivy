from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
class gm1:
    #----------now windows aplction--------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x780+1+1')
        self.root.title('Applction colleg')
        self.root.configure(background="black")
        self.root.resizable(False,False)
        title =Label(self.root,
        text='[GM]',
        bg='#1AAECB',
        font=('monspace',14,'bold'),
        fg='green' )
        title.pack(fill=X)


root =Tk()
ob = gm1(root)
root.mainloop()
