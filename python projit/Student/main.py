from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo

import pymysql


class Student:
    #----------now windows aplction--------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1520x780+1+1')
        self.root.title('Applction colleg')
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title =Label(self.root,
        text='[Systme save Student]',
        bg='#1AAECB',
        font=('monspace',14,'bold'),
        fg='white' )
        title.pack(fill=X)
        #---------variable---------
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.phone_var=StringVar()
        self.email_var=StringVar()
        self.certi_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.delet_var=StringVar()
        self.se_by=StringVar()
        self.se_txt=StringVar()

        #------------Stating control applction-------
        Manage_Frame = Frame(self.root, bg='white')
        Manage_Frame.place(x=1205,y=34,width=310,height=400)
        lbl_ID =Label(Manage_Frame, text='Namber ID', bg='white' )
        lbl_ID.pack()
        ID_Entry = Entry(Manage_Frame,textvariable=self.id_var,bd=2,justify='center')
        ID_Entry.pack()
        lbl_name = Label(Manage_Frame, bg='white',text='Name')
        lbl_name.pack()
        name_Entry = Entry(Manage_Frame,textvariable=self.name_var, bd=2, justify='center')
        name_Entry.pack()
        lbl_email = Label(Manage_Frame, bg='white',text='Email')
        lbl_email.pack()
        email_Entry = Entry(Manage_Frame,textvariable=self.email_var, bd=2, justify='center')
        email_Entry.pack()
        lbl_phone = Label(Manage_Frame, bg='white', text='Phone')
        lbl_phone.pack()
        phone_Entry = Entry(Manage_Frame,textvariable=self.phone_var, bd=2, justify='center')
        phone_Entry.pack()
        lbl_certi = Label(Manage_Frame, bg='white', text='Certi')
        lbl_certi.pack()
        certi_Entry = Entry(Manage_Frame,textvariable=self.certi_var, bd=2, justify='center')
        certi_Entry.pack()
        lbl_gender = Label(Manage_Frame, bg='white', text='Gender')
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,)
        combo_gender['value']=('male','fale')
        combo_gender.pack()
        lbl_address = Label(Manage_Frame, bg='white', text='Address')
        lbl_address.pack()
        address_Entry = Entry(Manage_Frame,textvariable=self.address_var, bd=2, justify='center')
        address_Entry.pack()
        lbl_delete = Label(Manage_Frame, fg='red',bg='white', text='Delete Name')
        lbl_delete.pack()
        delete_Entry = Entry(Manage_Frame,textvariable=self.delet_var, bd='3',justify='center')
        delete_Entry.pack()

        #-----------buttons---------
        Manage_Frame1 = Frame(self.root, bg='white')
        Manage_Frame1.place(x=1205, y=438, width=310, height=338)
        title1=Label(Manage_Frame1, text='System Controle', font=('Deco',14),fg='white',bg='#2980B9')
        title1.pack(fill=X)

        add_btn=Button(Manage_Frame1,text='Add Student',bg='#85929E',fg='white',command=self.add_student)
        add_btn.place(x=60,y=33,width=200,height=30)

        del_btn=Button(Manage_Frame1,text='Delate Student',bg='#85929E',fg='white',command=self.delete)
        del_btn.place(x=60,y=70,width=200,height=30)

        update_btn=Button(Manage_Frame1,text='Edite Date Student',bg='#85929E',fg='white',command=self.update)
        update_btn.place(x=60,y=107,width=200,height=30)

        clear_btn=Button(Manage_Frame1,text='Empty Fields',bg='#85929E',fg='white',command=self.clear)
        clear_btn.place(x=60,y=144,width=200,height=30)

        about_btn=Button(Manage_Frame1,text='Who Are We',bg='#85929E',fg='white',command=self.about)
        about_btn.place(x=60,y=181,width=200,height=30)

        exit_btn=Button(Manage_Frame1,text='Close the Program',bg='#85929E',fg='white',command=root.quit)
        exit_btn.place(x=60,y=218,width=200,height=30)

        #---------Search manage -------
        search_Frame= Frame(self.root, bg='white')
        search_Frame.place(x=3,y=35,width=1200,height=70)
        lbl_search= Label(search_Frame, text='Search Student',bg='white')
        lbl_search.place(x=1100,y=20)
        combo_search =ttk.Combobox(search_Frame,justify="center",textvariable=self.se_by)
        combo_search['value']=('id','name','email','phone')
        combo_search.place(x=940,y=20)

        search_Entry= Entry(search_Frame,textvariable=self.se_txt, bd=2)
        search_Entry.place(x=800,y=20 ,width=120,height=25)

        search_btn =Button(search_Frame, text='search',font='blod', bg ='#3498DB',fg='white',command=self.search)
        search_btn.place(x=660,y=20, width=120,height=25)

        #--------- dietals--------
        Dietals_Frame = Frame(self.root,bg='#F2F4F4')
        Dietals_Frame.place(x=3,y=106,width=1200,height=670 )
        #=------scroll----------
        scroll_x= Scrollbar(Dietals_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Dietals_Frame, orient=VERTICAL)
        #-------treeveiw------

        self.student_table= ttk.Treeview(Dietals_Frame,
        columns=('id','name','email','phone','certi','gender','address'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=1,width=1182,height=652)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show']='headings'
        self.student_table.heading('address',text='address student')
        self.student_table.heading('gender', text='Gender student')
        self.student_table.heading('certi', text='Certi student')
        self.student_table.heading('phone', text='Phone student')
        self.student_table.heading('email', text='Email student')
        self.student_table.heading('name', text='Name student')
        self.student_table.heading('id', text='Id student')

        self.student_table.column('address',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('certi',width=100)
        self.student_table.column('phone',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('id',width=100)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)


        #-----------con + add-------
        self.fetch_all()
    def add_student(self):
        con=pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='stud')
        cur=con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                                                         self.id_var.get(),
                                                         self.name_var.get(),
                                                         self.email_var.get(),
                                                         self.phone_var.get(),
                                                         self.certi_var.get(),
                                                         self.gender_var.get(),
                                                         self.address_var.get()
                                                           ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def fetch_all(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud')
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        if len(rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()

    def delete(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud')
        cur = con.cursor()
        cur.execute('delete from student where id=%s',self.delet_var.get())
        con.commit()
        self.fetch_all()
        con.close()

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.certi_var.set('')
        self.gender_var.set('')
        self.address_var.set('')

    def get_cursor(self,ev):
        cursor_row= self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.address_var.set(row[6])
        self.gender_var.set(row[5])
        self.certi_var.set(row[4])
        self.phone_var.set(row[3])
        self.email_var.set(row[2])
        self.name_var.set(row[1])
        self.id_var.set(row[0])

    def update(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud')
        cur = con.cursor()
        cur.execute("update student set address=%s,gender=%s,certi=%s,phone=%s,email=%s,name=%s where id=%s", (
                                                            self.address_var.get(),
                                                            self.gender_var.get(),
                                                            self.certi_var.get(),
                                                            self.phone_var.get(),
                                                            self.email_var.get(),
                                                            self.name_var.get(),
                                                            self.id_var.get(),
                                                             ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def search(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud')
        cur = con.cursor()
        cur.execute("select * from student where " +
        str(self.se_by.get()) + " LIKE '%" + str(self.se_txt.get()) +"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            con.commit()
        con.close()
    def about(self):
        messagebox,showinfo("deloper salaheddine ","welcome to our first projict")
        messagebox, showinfo("0595394559")

root =Tk()
ob = Student(root)
root.mainloop()