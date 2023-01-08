from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.lang import Builder

list_it="""
Screen:
    ScrollView:
        MDList:
            id : salah
            
"""

class ListSalahApp(MDApp):
    def build(self):
        screen =Builder.load_string(list_it)
        return screen
    def on_start(self):
        for i in range(30):
            item = OneLineListItem(text='Item'+ str(i))
            self.root.ids.salah.add_widget(item)

ListSalahApp().run()