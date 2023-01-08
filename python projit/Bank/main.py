from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Window.size= 370,660

class Application(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = '700'
        return Application()

Builder.load_file('application.kv')

if __name__=="__main__":
    MainApp().run()