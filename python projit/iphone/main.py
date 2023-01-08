from kivy.app import App
from kivy.coreass import Window
Window.clearcolor = (100/255.0,0,0,0)
Window.size = (400,600)
class Myapp(App):
     def build(self):
         self.title = 'salah [First App]'
         pass
if __name__== '__main__':
     Myapp().run()