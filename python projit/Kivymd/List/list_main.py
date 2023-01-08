from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.lang import Builder
Window.size= 350, 600
list_it="""
ScrollView:
    MDList:
        OneLineListItem:
            text: 'Item1'
        OneLineListItem:
            text: 'Item2'
        OneLineListItem:
            text: 'Item3'
            

"""




class ListApp(MDApp):
    def build(self):
        screen = Screen()
        list_item = Builder.load_string(list_it)
        screen.add_widget(list_item)
        return screen

ListApp().run()