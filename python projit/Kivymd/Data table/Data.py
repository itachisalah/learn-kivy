from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
Window.size=320,600

class DataApp(MDApp):
    def build(self):
        screen = Screen()
        data_table = MDDataTable(pos_hint={'center_x':.5,'center_y':.5},
                                 size_hint= (0.9,0.6),
                                 check = True,
                                 rows_num=10,
                                 column_data=[
                                     ("No.", dp(18)),
                                     ("Food", dp(20)),
                                     ("price",dp(20))
                                 ],
                                 row_data=[
                                     ("1", "Tomato", "3dh"),
                                     ("2", "Banana", "7dh"),
                                     ("3", "Apple", "5dh"),
                                     ("4", "Onion", "2.5dh"),
                                     ("5", "Cauliflower", "3dh"),
                                     ("6", "Water melon", "1dh"),
                                     ("7", "Potato", "2dh"),
                                     ("8", "PineApple", "4dh"),
                                     ("9", "Strawberry", "5dh"),
                                     ("10", "Lettuce", "1dh"),
                                 ])


        screen.add_widget(data_table)
        return screen



DataApp().run()