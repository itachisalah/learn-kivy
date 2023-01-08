import sqlite3

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable

Window.size= 300,500

KV=""" 
MDFloatLayout:
    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active:"lightgrey"
        
        MDBottomNavigationItem:
            name:"calculatirce"
            text:"calculatirce"
            icon:"calculator"
            
            MDCard:
                size_hint: 0.9, 0.2
                pos_hint:{"center_x":0.5,"center_y":0.87}
                md_bg_color: "white"
            MDLabel:
                id: label
                text:""
                pos_hint:{"center_y":0.87}
                halign: "center"
                bold: True
                font_style:"H5"                
                
            MDTextButton:
                text:"AC"
                size_hint_x: 0.1
                pos_hint:{"center_x":0.12,"center_y":0.7}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.ac()
            MDTextButton:
                text:"π"
                size_hint_x: 0.1
                pos_hint:{"center_x":0.37,"center_y":0.7}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.pi()
                
            MDRectangleFlatButton:
                id: parenthese
                text:"()"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.62,"center_y":0.7}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.parenthese()
                
            MDRectangleFlatButton:
                id: diviser
                text:"/"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.87,"center_y":0.7}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.diviser()
                
            MDRectangleFlatButton:
                id: sept
                text:"7"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.12,"center_y":0.6}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.sept()
            
            MDRectangleFlatButton:
                id: huit
                text:"8"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.37,"center_y":0.6}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.huit()
            
            MDRectangleFlatButton:
                id: neuf
                text:"9"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.62,"center_y":0.6}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.neuf()
            
            MDRectangleFlatButton:
                id: quatre
                text:"4"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.12,"center_y":0.5}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.quatre()
            
            MDRectangleFlatButton:
                id: cinq
                text:"5"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.37,"center_y":0.5}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.cinq()
            
            MDRectangleFlatButton:
                id: six
                text:"6"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.62,"center_y":0.5}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.six()
            
            MDRectangleFlatButton:
                id: un
                text:"1"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.12,"center_y":0.4}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.un()
            
            MDRectangleFlatButton:
                id: deux
                text:"2"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.37,"center_y":0.4}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.deux()

            
            MDRectangleFlatButton:
                id: trois
                text:"3"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.62,"center_y":0.4}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.trois()
                
            MDRaisedButton:
                text:"x"
                pos_hint:{"center_x":0.87,"center_y":0.6}
                size_hint_x: 0.05
                elevation: 0
                theme_text_color:"Custom"
                md_bg_color:app.theme_cls.primary_color
                on_press: app.fois()
                
            MDRaisedButton:
                text:"-"
                pos_hint:{"center_x":0.87,"center_y":0.5}
                size_hint_x: 0.05
                elevation: 0
                theme_text_color:"Custom"
                md_bg_color:app.theme_cls.primary_color
                on_press: app.moins()
                
            MDRaisedButton:
                text:"+"
                pos_hint:{"center_x":0.87,"center_y":0.4}
                size_hint_x: 0.05
                elevation: 0
                theme_text_color:"Custom"
                md_bg_color:app.theme_cls.primary_color
                on_press: app.plus()
                
            MDRectangleFlatButton:
                id: ziro
                text:"0"
                size_hint_x: 0.05
                pos_hint:{"center_x":0.37,"center_y":0.3}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.ziro()
            
            MDRectangleFlatButton:
                id: virgule
                text:","
                size_hint_x: 0.05
                pos_hint:{"center_x":0.62,"center_y":0.3}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.virgule()
                
            MDFillRoundFlatButton:
                text:"="
                pos_hint:{"center_x":0.87,"center_y":0.3}
                size_hoint_x: 0.5
                theme_text_color:"Custom"
                md_bg_color: app.theme_cls.primary_color
                on_press: app.egale()
                
            MDFillRoundFlatButton:
                text:"²"
                pos_hint:{"center_x":0.12,"center_y":0.3}
                size_hoint_x: 0.5
                theme_text_color:"Custom"
                md_bg_color: app.theme_cls.primary_color
                on_press: app.carre()
                
            MDIconButton:
                icon:"delete-variant"
                pos_hint:{"center_x":0.5,"center_y":0.15}
                theme_text_color:"Custom"
                md_bg_color: app.theme_cls.primary_color
                on_press: app.delete()
       
        MDBottomNavigationItem:
            name:"historique"
            text:"History"
            icon:"database-edit" 
            
            AnchorLayout:
                id: historique        
        
        MDBottomNavigationItem:
            name:"parametre"
            text:"Parametre" 
            icon:"menu"
            
            MDLabel:
                id:label_siwtch_theme
                text:"Theme Style:"
                halign:"center"
                pos_hint:{"center_x":0.2,"center_y":0.9}
                bold: True
                theme_text_color:"Custom"   
                
            MDSwitch:
                on_active :app.switch_theme()
                pos_hint:{"center_x":0.6,"center_y":0.9}
                
            MDLabel:
                id:label_switch_color
                text:"Theme Color"
                halign: "center"
                pos_hint:{"center_x":0.2,"center_y":0.8}
                bold: True
                theme_text_color:"Custom"
            
            MDRectangleFlatButton:
                id: red_button
                text:"Red"
                pos_hint:{"center_x":0.55,"center_y":0.8}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.switch_color("red")
            
            MDRectangleFlatButton:
                id: blue_button
                text:"Blue"
                pos_hint:{"center_x":0.8,"center_y":0.8}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.switch_color("blue")
            
            MDRectangleFlatButton:
                id: green_button
                text:"Green"
                pos_hint:{"center_x":0.55,"center_y":0.7}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.switch_color("green")
            
            MDRectangleFlatButton:
                id: purple_button
                text:"Purple"
                pos_hint:{"center_x":0.8,"center_y":0.7}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.switch_color("purple")
                
            MDRectangleFlatButton:
                id: reset_historique_button
                text:"Delete all History"
                pos_hint:{"center_x":0.3,"center_y":0.6}
                theme_text_color:"Custom"
                text_color:app.theme_cls.primary_color
                on_press:app.delete_historique()

"""

class calculatirApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette= "Green"
        self.theme_cls.theme_style = "Light"
        self.result = ""
        self.x = True
        self.data_tables_values = []
        self.connection = connection
        self.cursor = cursor
        self.init_table = True

        self.button = Builder.load_string(KV)
        self.screen.add_widget(self.button)


        self.creat_db()
        self.creat_table_data()

        return self.screen

    def creat_db(self):
        self.cursor.execute("""create table if not exists Data(
        cacul text,
        resultat text)
        """)
        self.connection.commit()

    def creat_table_data(self):
        self.cursor.execute("select * from Data")
        if len(self.cursor.fetchall()) == 0:
            self.data_tables = MDDataTable(
                size_hint=(0.9,0.85),
                elevation = 0,
                rows_num= 300,
                column_data=[
                    ("Calcul", 30),
                    ("Resultat", 30),
                ],
                row_data= self.data_tables_values
            )
        else:
            self.data_tables= MDDataTable(
                size_hint=(0.9, 0.85),
                elevation=0,
                rows_num=300,
                column_data=[
                    ("Calcul", 30),
                    ("Resultat", 30),
                ],
                row_data=self.data_tables_values

            )
            self.cursor.execute("select * from Data")
            if self.init_table:
                for values in self.cursor.fetchall():
                    self.data_tables.add_row(values)
                self.cursor.execute("select * from Data")
                self.data_tables_values = self.cursor.fetchall()

        self.button.ids.historique.add_widget(self.data_tables)
        self.init_table = False
        print(self.data_tables_values)


    def ac(self):
        self.result= ""
        self.button.ids.label.text= ""

    def pi(self):
        self.result+= "3.14"
        self.button.ids.label.text= self.result

    def parenthese(self):
        if self.x:
            self.result +=("(")
            self.x =False
        else:
            self.result += (")")
            self.x= True
        self.button.ids.label.text = self.result

    def diviser(self):
        self.result+=("/")
        self.button.ids.label.text = self.result

    def plus(self):
        self.result+=("+")
        self.button.ids.label.text = self.result

    def moins(self):
        self.result+=("-")
        self.button.ids.label.text = self.result

    def fois(self):
        self.result+=("*")
        self.button.ids.label.text = self.result

    def un(self):
        self.result+=("1")
        self.button.ids.label.text = self.result

    def deux(self):
        self.result+=("2")
        self.button.ids.label.text = self.result

    def trois(self):
        self.result+=("3")
        self.button.ids.label.text = self.result

    def quatre(self):
        self.result+=("4")
        self.button.ids.label.text = self.result

    def cinq(self):
        self.result+=("5")
        self.button.ids.label.text = self.result

    def six(self):
        self.result+=("6")
        self.button.ids.label.text = self.result

    def sept(self):
        self.result+=("7")
        self.button.ids.label.text = self.result

    def huit(self):
        self.result+=("8")
        self.button.ids.label.text = self.result

    def neuf(self):
        self.result+=("9")
        self.button.ids.label.text = self.result

    def ziro(self):
        self.result+=("0")
        self.button.ids.label.text = self.result

    def virgule(self):
        self.result+=(".")
        self.button.ids.label.text = self.result

    def carre(self):
        self.result+=("**2")
        self.button.ids.label.text = self.result

    def delete(self):
        self.result = self.result[:-1]
        self.button.ids.label.text = self.result

    def egale(self):
        if self.result == "":
            self.button.ids.label.text = "ERROR"
            self.result_final = "ERROR"
            return
        try:
            self.result_final= eval(self.result)
            self.button.ids.label.text= str(self.result_final)
        except:
            self.button.ids.label.text = "ERROR"
            self.result_final= "ERROR"
        self.data_tables.add_row((self.result, self.result_final))
        self.data_tables_values = self.data_tables.row_data
        self.cursor.execute("insert into Data values(?,?)",(self.result,self.result_final))
        self.connection.commit()

    def switch_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.button.ids.label_switch_theme_color =(1,1,1,1)
            self.button.ids.label_switch_color_color = (1, 1, 1, 1)
            self.creat_table_data()

        else:
            self.theme_cls.theme_style= "Light"
            self.button.ids.label_switch_theme_color = (0,0,0, 1)
            self.button.ids.label_switch_color_color = (0,0,0, 1)
            self.creat_table_data()

    def switch_color(self, instance):
        if instance== "blue":
            self.theme_cls.primary_palette= "Blue"
        elif instance== "green":
            self.theme_cls.primary_palette= "Green"
        elif instance== "purple":
            self.theme_cls.primary_palette= "Purple"
        elif instance== "red":
            self.theme_cls.primary_palette= "Red"

        self.button.ids.blue_button.line_color= self.theme_cls.primary_color
        self.button.ids.red_button.line_color = self.theme_cls.primary_color
        self.button.ids.green_button.line_color = self.theme_cls.primary_color
        self.button.ids.purple_button.line_color = self.theme_cls.primary_color

        self.button.ids.ziro.line_color = self.theme_cls.primary_color
        self.button.ids.un.line_color = self.theme_cls.primary_color
        self.button.ids.deux.line_color = self.theme_cls.primary_color
        self.button.ids.trois.line_color = self.theme_cls.primary_color
        self.button.ids.quatre.line_color = self.theme_cls.primary_color
        self.button.ids.cinq.line_color = self.theme_cls.primary_color
        self.button.ids.six.line_color = self.theme_cls.primary_color
        self.button.ids.sept.line_color = self.theme_cls.primary_color
        self.button.ids.huit.line_color = self.theme_cls.primary_color
        self.button.ids.neuf.line_color = self.theme_cls.primary_color
        self.button.ids.virgule.line_color = self.theme_cls.primary_color
        self.button.ids.parenthese.line_color = self.theme_cls.primary_color
        self.button.ids.diviser.line_color = self.theme_cls.primary_color
        self.button.ids.reset_historique_button.line_color = self.theme_cls.primary_color

    def delete_historique(self):
        if len(self.data_tables.row_data) >=1:
            for i in range(len(self.data_tables.row_data)):
                self.data_tables.remove_row(self.data_tables.row_data[-1])

        self.data_tables_values = []
        self.cursor.execute("delete from Data")
        self.connection.commit()




connection = sqlite3.connect("data.db")
cursor = connection.cursor()

if __name__=='__main__':
    calculatirApp().run()


connection.close()