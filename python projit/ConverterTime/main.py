from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.size= 360,640

class Container(GridLayout):
    def convert(self):
        try:
            number= int(self.text_input.text)
        except Exception:
            number = 0
        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number *24 *60)
        self.label_seconds.text= str(number * 24 * 60 * 60)



class ConverterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Container()

if __name__=='__main__':
    ConverterApp().run()