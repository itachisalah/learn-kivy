import os
from kivymd.app import MDApp
from kivy import platform
from kivy.metrics import dp
from pathlib import Path

from View.Managers.manager_screen import ManagerScreen

os.environ['CURRENCY_CONVERTER_ROOT']= str(Path(__file__).parent)

class ConverterApp(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style= 'Light'
        self.theme_cls.primary_palette = 'DeepOrange'
        self.manager_screen = ManagerScreen()
        if platform != 'android':
            self.button_size = dp(28)
            self.font_size= 'H3'
        else:
            self.button_size = dp(16)
            self.font_size = 'H5'

    def __int__(self):
        return 'ConverterApp'

    def build(self):
        self.manager_screen.add_widget(self.manager_screen.create_screen('main'))
        return self.manager_screen


ConverterApp().run()