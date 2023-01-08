from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.lang import Builder
import itachi
Window.size= 360,600

class TextApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen =Screen()

        username = Builder.load_string(itachi.username_input)
        screen.add_widget(username)

        return screen

TextApp().run()