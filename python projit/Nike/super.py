from tkinter import*
import math
import os
import random
from tkinter import messagebox
class Super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x760+10+10')
        self.root.title('Super Market : Carrefour')
        self.root.resizable(False,False)
        self.root.iconbitmap('D:\\salah.ico')
        title =Label(self.root,text='Project Management : Marekt Carrefour',fg='white',bg='#0B2F3A', font=('Tajawal',15))
        title.pack(fill=X)
        #========={Total Account}===========
        #=========vigatable q1==> q20=========
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()
        self.q19=IntVar()
        self.q20=IntVar()
        # =========fruit qq1==> qq20=========
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()
        self.qq19=IntVar()
        self.qq20=IntVar()
        # =========Name qqq1==> qqq20=========
        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()
        self.qqq16=IntVar()
        self.qqq17=IntVar()
        self.qqq18=IntVar()
        self.qqq19=IntVar()
        self.qqq20=IntVar()
        # =========Care q1==> q20=========
        #========chinage date customer======
        self.name=StringVar()
        self.phono=StringVar()
        self.fatora=StringVar()
        x=random.randint(1000,9999)
        self.fatora.set(str(x))

        #==========varibele total accont======
        self.vegatbale=StringVar()
        self.fruit=StringVar()
        self.name1=StringVar()




        #==> Customer Date.
        F1 = Frame(root,bd=2, width=338,height=170, bg='#0b4C5f')
        F1.place(x=1160,y=30)
        tit = Label(F1,text='Data :',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='tomato')
        tit.place(x=0,y=10)
        his_name =Label(F1,text='Name Customer',font=('tajawal',10,),bg='#0B4c5F',fg='white')
        his_name.place(x=0,y=40)
        his_phone = Label(F1, text='Phone Customer', font=('tajawal', 10,), bg='#0B4c5F', fg='white')
        his_phone.place(x=0, y=70)
        bill_num = Label(F1, text='Namber invince' ,font=('tajawal', 10,), bg='#0B4c5F', fg='white')
        bill_num.place(x=0, y=100)

        Ent_name = Entry(F1,textvariable=self.name, justify='center')
        Ent_name.place(x=120,y=42)
        Ent_phone = Entry(F1,textvariable=self.phono, justify='center')
        Ent_phone.place(x=120, y=72)
        Ent_bill = Entry(F1 ,textvariable=self.fatora, justify='center')
        Ent_bill .place(x=120, y=102)

        btn_customer = Button(F1 , text='Serch', font=('tajawal,10'),width=8,height=4,bg='white')
        btn_customer.place(x=250,y=40)
        #==========Fatora or bill=========
        tibill = Label(F1 , text='[bill]',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        tibill.place(x=125,y=135)
        F3 = Frame(root, bd=2, width=338, height=399, bg='white')
        F3.place(x=1160,y=205)
        scrol_y =Scrollbar(F3,orient=VERTICAL)
        self.textarea=Text(F3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=======Price=======
        F4 = Frame(root,bd=2,width=560,height=112, bg='#0B4C5F')
        F4.place(x=938,y=582)
        hesab = Button(F4,text='Account',width=13,height=2,font=('tajawal'),bg='#DBA901',command=self.total)
        hesab.place(x=424,y=3)
        fatora = Button(F4,text='Export Invoice',width=13,height=2,font='tajawal',bg='#DBA901')
        fatora.place(x=424,y=55)
        clear = Button(F4 ,text='Empty Fields',width=13,height=2,font='tajawal',bg='#DBA901')
        clear.place(x=295,y=3)
        exite =Button(F4 ,text='Exit Appliction',width=13,height=2,font='tajawal',bg='#DBA901')
        exite.place(x=295,y=55)
        lblo1=Label(F4, text='Total Vigatabel',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo1.place(x=100,y=10)
        lblo2 = Label(F4, text='Total Fruit', font=('tajawal', 10, 'bold'), bg='#0B4C5F', fg='gold')
        lblo2.place(x=100, y=40)
        lblo3 = Label(F4, text='Total Name', font=('tajawal', 10, 'bold'), bg='#0B4C5F', fg='gold')
        lblo3.place(x=100, y=70)
        ento1 = Entry(F4,textvariable=self.vegatbale,width=12)
        ento1.place(x=10,y=10)
        ento2 = Entry(F4,textvariable=self.fruit, width=12)
        ento2.place(x=10, y=40)
        ento3 = Entry(F4,textvariable=self.name1, width=12)
        ento3.place(x=10, y=70)
        #=========items{1}========
        FF1=Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')
        FF1.place(x=1,y=30)
        t =Label(FF1,text=' Vegatabel',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        t.place(x=100,y=0)
        leg1=Label(FF1,text='Tomato',font=('tajawal',14,'bold'),bg='#0B4C5F',fg='white')
        leg1.place(x=190,y=50)
        leg2 = Label(FF1, text='Cucumber', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg2.place(x=190, y=80)
        leg3 = Label(FF1, text='onion', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg3.place(x=190, y=110)
        leg4 = Label(FF1, text='Ginger', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg4.place(x=190, y=140)
        leg5 = Label(FF1, text='Garlic', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg5.place(x=190, y=170)
        leg6 = Label(FF1, text='Zucchini', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg6.place(x=190, y=200)
        leg7 = Label(FF1, text='Eggplant', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg7.place(x=190, y=230)
        leg8 = Label(FF1, text='Beetrot', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg8.place(x=190, y=260)
        leg9 = Label(FF1, text='Turnip', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg9.place(x=190, y=290)
        leg10 = Label(FF1, text='Green beans', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg10.place(x=190, y=320)
        leg11 = Label(FF1, text='Brods beans', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg11.place(x=190, y=350)
        leg12 = Label(FF1, text='Cabbge', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg12.place(x=190, y=380)
        leg13 = Label(FF1, text='capsicum', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg13.place(x=190, y=410)
        leg14 = Label(FF1, text='potato', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg14.place(x=190, y=440)
        leg15 = Label(FF1, text='Potato Sweet', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg15.place(x=190, y=470)
        leg16 = Label(FF1, text='Sweet Corn', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg16.place(x=190, y=500)
        leg17 = Label(FF1, text='Celery Stick', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg17.place(x=190, y=530)
        leg18 = Label(FF1, text='Lettuce', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg18.place(x=190, y=560)
        leg19 = Label(FF1, text='Carrot', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg19.place(x=190, y=590)
        leg20 = Label(FF1, text='Herbs', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg20.place(x=190, y=620)

        fruit1= Entry(FF1,textvariable=self.q1,width=18)
        fruit1.place(x=10,y=52)
        fruit2 = Entry(FF1,textvariable=self.q2, width=18)
        fruit2.place(x=10, y=80)
        fruit3 = Entry(FF1,textvariable=self.q3, width=18)
        fruit3.place(x=10, y=110)
        fruit4 = Entry(FF1,textvariable=self.q4, width=18)
        fruit4.place(x=10, y=140)
        fruit5 = Entry(FF1,textvariable=self.q5, width=18)
        fruit5.place(x=10, y=170)
        fruit6 = Entry(FF1,textvariable=self.q6, width=18)
        fruit6.place(x=10, y=200)
        fruit7 = Entry(FF1,textvariable=self.q7, width=18)
        fruit7.place(x=10, y=230)
        fruit8 = Entry(FF1,textvariable=self.q8, width=18)
        fruit8.place(x=10, y=260)
        fruit9 = Entry(FF1,textvariable=self.q9, width=18)
        fruit9.place(x=10, y=290)
        fruit10 = Entry(FF1,textvariable=self.q10, width=18)
        fruit10.place(x=10, y=320)
        fruit11 = Entry(FF1,textvariable=self.q11, width=18)
        fruit11.place(x=10, y=350)
        fruit12 = Entry(FF1,textvariable=self.q12, width=18)
        fruit12.place(x=10, y=380)
        fruit13 = Entry(FF1,textvariable=self.q13, width=18)
        fruit13.place(x=10, y=410)
        fruit14 = Entry(FF1,textvariable=self.q14, width=18)
        fruit14.place(x=10, y=440)
        fruit15 = Entry(FF1,textvariable=self.q15, width=18)
        fruit15.place(x=10, y=470)
        fruit16 = Entry(FF1,textvariable=self.q16, width=18)
        fruit16.place(x=10, y=500)
        fruit17 = Entry(FF1,textvariable=self.q17, width=18)
        fruit17.place(x=10, y=530)
        fruit18 = Entry(FF1,textvariable=self.q18, width=18)
        fruit18.place(x=10, y=560)
        fruit19 = Entry(FF1,textvariable=self.q19, width=18)
        fruit19.place(x=10, y=590)
        fruit20= Entry(FF1,textvariable=self.q20, width=18)
        fruit20.place(x=10, y=620)

        #=========itam[2]==========
        FF2 =Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')
        FF2.place(x=321,y=30)
        t = Label(FF2, text='Fruit', font=('tajawal', 15, 'bold'), bg='#0B4C5F', fg='gold')
        t.place(x=140, y=0)
        leg1 = Label(FF2, text='Orange A', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg1.place(x=190, y=50)
        leg2 = Label(FF2, text='Starwberry', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg2.place(x=190, y=80)
        leg3 = Label(FF2, text='Mandarin', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg3.place(x=190, y=110)
        leg4 = Label(FF2, text='Clmentine', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg4.place(x=190, y=140)
        leg5 = Label(FF2, text='Nectarin', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg5.place(x=190, y=170)
        leg6 = Label(FF2, text='Lemone', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg6.place(x=190, y=200)
        leg7 = Label(FF2, text='pomogrante', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg7.place(x=190, y=230)
        leg8 = Label(FF2, text='Banana', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg8.place(x=190, y=260)
        leg9 = Label(FF2, text='Apple red', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg9.place(x=190, y=290)
        leg10 = Label(FF2, text='Apple gala', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg10.place(x=190, y=320)
        leg11 = Label(FF2, text='Apple green', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg11.place(x=190, y=350)
        leg12 = Label(FF2, text='Pinapple', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg12.place(x=190, y=380)
        leg13 = Label(FF2, text='Pear cosia', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg13.place(x=190, y=410)
        leg14 = Label(FF2, text='Kaki', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg14.place(x=190, y=440)
        leg15 = Label(FF2, text='Garpfruite', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg15.place(x=190, y=470)
        leg16 = Label(FF2, text='lime', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg16.place(x=190, y=500)
        leg17 = Label(FF2, text='peach', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg17.place(x=190, y=530)
        leg18 = Label(FF2, text='apricot', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg18.place(x=190, y=560)
        leg19 = Label(FF2, text='Jujubi', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg19.place(x=190, y=590)
        leg20 = Label(FF2, text='Kiwi', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg20.place(x=190, y=620)

        fruit1 = Entry(FF2,textvariable=self.qq1, width=18)
        fruit1.place(x=10, y=52)
        fruit2 = Entry(FF2,textvariable=self.qq2, width=18)
        fruit2.place(x=10, y=80)
        fruit3 = Entry(FF2,textvariable=self.qq3, width=18)
        fruit3.place(x=10, y=110)
        fruit4 = Entry(FF2,textvariable=self.qq4, width=18)
        fruit4.place(x=10, y=140)
        fruit5 = Entry(FF2,textvariable=self.qq5, width=18)
        fruit5.place(x=10, y=170)
        fruit6 = Entry(FF2,textvariable=self.qq6, width=18)
        fruit6.place(x=10, y=200)
        fruit7 = Entry(FF2,textvariable=self.qq7, width=18)
        fruit7.place(x=10, y=230)
        fruit8 = Entry(FF2,textvariable=self.qq8, width=18)
        fruit8.place(x=10, y=260)
        fruit9 = Entry(FF2,textvariable=self.qq9, width=18)
        fruit9.place(x=10, y=290)
        fruit10 = Entry(FF2,textvariable=self.qq10, width=18)
        fruit10.place(x=10, y=320)
        fruit11 = Entry(FF2,textvariable=self.qq11, width=18)
        fruit11.place(x=10, y=350)
        fruit12 = Entry(FF2,textvariable=self.qq12, width=18)
        fruit12.place(x=10, y=380)
        fruit13 = Entry(FF2,textvariable=self.qq13, width=18)
        fruit13.place(x=10, y=410)
        fruit14 = Entry(FF2,textvariable=self.qq14, width=18)
        fruit14.place(x=10, y=440)
        fruit15 = Entry(FF2,textvariable=self.qq15, width=18)
        fruit15.place(x=10, y=470)
        fruit16 = Entry(FF2,textvariable=self.qq16, width=18)
        fruit16.place(x=10, y=500)
        fruit17 = Entry(FF2,textvariable=self.qq17, width=18)
        fruit17.place(x=10, y=530)
        fruit18 = Entry(FF2,textvariable=self.qq18, width=18)
        fruit18.place(x=10, y=560)
        fruit19 = Entry(FF2,textvariable=self.qq19, width=18)
        fruit19.place(x=10, y=590)
        fruit20 = Entry(FF2,textvariable=self.qq20, width=18)
        fruit20.place(x=10, y=620)

        FF3 = Frame(root, bd=2, width=295, height=664, bg='#0B4C5F')
        FF3.place(x=641, y=30)
        t = Label(FF3, text='Name', font=('tajawal', 15, 'bold'), bg='#0B4C5F', fg='gold')
        t.place(x=140, y=0)
        leg1 = Label(FF3, text='Salah', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg1.place(x=160, y=50)
        leg2 = Label(FF3, text='Hossam', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg2.place(x=160, y=80)
        leg3 = Label(FF3, text='Mohamed', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg3.place(x=160, y=110)
        leg4 = Label(FF3, text='Otmane', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg4.place(x=160, y=140)
        leg5 = Label(FF3, text='Zakaria', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg5.place(x=160, y=170)
        leg6 = Label(FF3, text='Rachid', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg6.place(x=160, y=200)
        leg7 = Label(FF3, text='Hassan', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg7.place(x=160, y=230)
        leg8 = Label(FF3, text='Omar', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg8.place(x=160, y=260)
        leg9 = Label(FF3, text='Jihad', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg9.place(x=160, y=290)
        leg10 = Label(FF3, text='Souhil', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg10.place(x=160, y=320)
        leg11 = Label(FF3, text='Ahmed', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg11.place(x=160, y=350)
        leg12 = Label(FF3, text='Amine', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg12.place(x=160, y=380)
        leg13 = Label(FF3, text='Samir', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg13.place(x=160, y=410)
        leg14 = Label(FF3, text='Noor', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg14.place(x=160, y=440)
        leg15 = Label(FF3, text='Kamal', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg15.place(x=160, y=470)
        leg16 = Label(FF3, text='Simo', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg16.place(x=160, y=500)
        leg17 = Label(FF3, text='Lofi', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg17.place(x=160, y=530)
        leg18 = Label(FF3, text='Zoro', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg18.place(x=160, y=560)
        leg19 = Label(FF3, text='Sanji', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg19.place(x=160, y=590)
        leg20 = Label(FF3, text='Usope', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg20.place(x=160, y=620)

        fruit1 = Entry(FF3,textvariable=self.qqq1, width=18)
        fruit1.place(x=10, y=52)
        fruit2 = Entry(FF3,textvariable=self.qqq2, width=18)
        fruit2.place(x=10, y=80)
        fruit3 = Entry(FF3,textvariable=self.qqq3, width=18)
        fruit3.place(x=10, y=110)
        fruit4 = Entry(FF3,textvariable=self.qqq4, width=18)
        fruit4.place(x=10, y=140)
        fruit5 = Entry(FF3,textvariable=self.qqq5, width=18)
        fruit5.place(x=10, y=170)
        fruit6 = Entry(FF3,textvariable=self.qqq6, width=18)
        fruit6.place(x=10, y=200)
        fruit7 = Entry(FF3,textvariable=self.qqq7, width=18)
        fruit7.place(x=10, y=230)
        fruit8 = Entry(FF3,textvariable=self.qqq8, width=18)
        fruit8.place(x=10, y=260)
        fruit9 = Entry(FF3,textvariable=self.qqq9, width=18)
        fruit9.place(x=10, y=290)
        fruit10 = Entry(FF3,textvariable=self.qqq10, width=18)
        fruit10.place(x=10, y=320)
        fruit11 = Entry(FF3,textvariable=self.qqq11, width=18)
        fruit11.place(x=10, y=350)
        fruit12 = Entry(FF3,textvariable=self.qqq12, width=18)
        fruit12.place(x=10, y=380)
        fruit13 = Entry(FF3,textvariable=self.qqq13, width=18)
        fruit13.place(x=10, y=410)
        fruit14 = Entry(FF3,textvariable=self.qqq14, width=18)
        fruit14.place(x=10, y=440)
        fruit15 = Entry(FF3,textvariable=self.qqq15, width=18)
        fruit15.place(x=10, y=470)
        fruit16 = Entry(FF3,textvariable=self.qqq16, width=18)
        fruit16.place(x=10, y=500)
        fruit17 = Entry(FF3,textvariable=self.qqq17, width=18)
        fruit17.place(x=10, y=530)
        fruit18 = Entry(FF3,textvariable=self.qqq18, width=18)
        fruit18.place(x=10, y=560)
        fruit19 = Entry(FF3, textvariable=self.qqq19,width=18)
        fruit19.place(x=10, y=590)
        fruit20 = Entry(FF3,textvariable=self.qqq20, width=18)
        fruit20.place(x=10, y=620)


        FF4 = Frame(root, bd=2, width=220, height=550, bg='#0B4C5F')
        FF4.place(x=938, y=30)

        t = Label(FF4, text='Care', font=('tajawal', 15, 'bold'), bg='#0B4C5F', fg='gold')
        t.place(x=90, y=0)
        leg1 = Label(FF4, text='BMW', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg1.place(x=90, y=50)
        leg2 = Label(FF4, text='Marsides', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg2.place(x=90, y=80)
        leg3 = Label(FF4, text='Aoudi', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg3.place(x=90, y=110)
        leg4 = Label(FF4, text='Tyota', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg4.place(x=90, y=140)
        leg5 = Label(FF4, text='Fiata', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg5.place(x=90, y=170)
        leg6 = Label(FF4, text='Dasia', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg6.place(x=90, y=200)
        leg7 = Label(FF4, text='Golf', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg7.place(x=90, y=230)
        leg8 = Label(FF4, text='Ford', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg8.place(x=90, y=260)
        leg9 = Label(FF4, text='Firar', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg9.place(x=90, y=290)
        leg10 = Label(FF4, text='Nisan', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg10.place(x=90, y=320)
        leg11 = Label(FF4, text='4X4', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg11.place(x=90, y=350)
        leg12 = Label(FF4, text='Citrwin', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg12.place(x=90, y=380)
        leg13 = Label(FF4, text='Saqoda', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg13.place(x=90, y=410)
        leg14 = Label(FF4, text='Kia', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg14.place(x=90, y=440)
        leg15 = Label(FF4, text='Rouno', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg15.place(x=90, y=470)
        leg16 = Label(FF4, text='Alfa Romo', font=('tajawal', 14, 'bold'), bg='#0B4C5F', fg='white')
        leg16.place(x=90, y=500)

        fruit1 = Entry(FF4, width=12)
        fruit1.place(x=10, y=52)
        fruit2 = Entry(FF4, width=12)
        fruit2.place(x=10, y=80)
        fruit3 = Entry(FF4, width=12)
        fruit3.place(x=10, y=110)
        fruit4 = Entry(FF4, width=12)
        fruit4.place(x=10, y=140)
        fruit5 = Entry(FF4, width=12)
        fruit5.place(x=10, y=170)
        fruit6 = Entry(FF4, width=12)
        fruit6.place(x=10, y=200)
        fruit7 = Entry(FF4, width=12)
        fruit7.place(x=10, y=230)
        fruit8 = Entry(FF4, width=12)
        fruit8.place(x=10, y=260)
        fruit9 = Entry(FF4, width=12)
        fruit9.place(x=10, y=290)
        fruit10 = Entry(FF4, width=12)
        fruit10.place(x=10, y=320)
        fruit11 = Entry(FF4, width=12)
        fruit11.place(x=10, y=350)
        fruit12 = Entry(FF4, width=12)
        fruit12.place(x=10, y=380)
        fruit13 = Entry(FF4, width=12)
        fruit13.place(x=10, y=410)
        fruit14 = Entry(FF4, width=12)
        fruit14.place(x=10, y=440)
        fruit15 = Entry(FF4, width=12)
        fruit15.place(x=10, y=470)
        fruit16 = Entry(FF4, width=12)
        fruit16.place(x=10, y=500)

    def total(self):
        self.Tomato=self.q1.get()*4.95
        self.Cucmber=self.q2.get()*5.95
        self.onion = self.q3.get() * 1.95
        self.ginger = self.q4.get() * 5.95
        self.garlic = self.q5.get() * 4.95
        self.zuchini = self.q6.get() * 5.95
        self.eggplant = self.q7.get() * 4.95
        self.turnip = self.q8.get() * 5.95
        self.greenbeans = self.q9.get() * 4.95
        self.brodsbeans = self.q10.get() * 5.95
        self.cabbge = self.q11.get() * 4.95
        self.capsicum = self.q12.get() * 5.95
        self.potato = self.q13.get() * 4.95
        self.potatosweet = self.q14.get() * 5.95
        self.sweetcorn = self.q15.get() * 4.95
        self.celerystick = self.q16.get() * 4.95
        self.lettuce = self.q17.get() * 5.95
        self.carrot = self.q18.get() * 4.95
        self.herbs = self.q19.get() * 0.95
        self.beetrot = self.q20.get() * 4.95
        self.totalito=float(
            self.Tomato+
            self.Cucmber+
            self.sweetcorn+
            self.greenbeans+
            self.beetrot+
            self.celerystick+
            self.carrot+
            self.cabbge+
            self.capsicum+
            self.eggplant+
            self.onion+
            self.potatosweet+
            self.potato+
            self.turnip+
            self.garlic+
            self.ginger+
            self.zuchini+
            self.herbs+
            self.brodsbeans+
            self.lettuce
        )
        self.vegatbale.set(str(self.totalito)+ "  $  ")







    def welcome(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Market Carrefour Your welcome")
        self.textarea.insert(END,"\n====================================")
        self.textarea.insert(END,f"\n\t B.NUM  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t NAME   :{self.name.get()}")
        self.textarea.insert(END,f"\n\t PHONE  :{self.phono.get()}")
        self.textarea.insert(END,"\n====================================")
        self.textarea.insert(END,f"\nprice\t  the number\t     purchases")
        self.textarea.insert(END,"\n=====================================")






root=Tk()
ob = Super(root)
root.mainloop()