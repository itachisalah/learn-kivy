from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList,IconLeftWidget, OneLineListItem, OneLineIconListItem

Window.size= 350,600

class ItachiApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()

        list_item = MDList()
        for i in range(25):
            icons = IconLeftWidget(icon="android")
            items= OneLineIconListItem(text=str(i)+ 'item')
            items.add_widget(icons)
            list_item.add_widget(items)

        scroll.add_widget(list_item)
        screen.add_widget(scroll)

        return screen

ItachiApp().run()