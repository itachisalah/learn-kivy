from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

Window.size= 350,600


class ThemeApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_salah = MDRectangleFlatButton(text='Salah Eddine',
                                          pos_hint={'center_x':0.5,'center_y':0.5})

        screen.add_widget(btn_salah)
        return screen
ThemeApp().run()

