from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor=(0,0,128)
Window.size=(400,600)

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Python(Screen):
    pass

class Java(Screen):
    pass

class Php(Screen):
    pass

class Chh(Screen):
    pass

class Cn(Screen):
    pass

class Css(Screen):
    pass

class Error(Screen):
    pass


kv = Builder.load_file('my.kv')
class Myitachi(App):
    def build(self):
        self.title='WElCOME'
        return kv

if __name__=='__main__':
    Myitachi().run()

