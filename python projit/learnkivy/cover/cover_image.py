from kivy.app import App
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
Window.size = 350,600

class CoverImage(CoverBehavior,Image):
    def __init__(self,**kwargs):
        super(CoverImage, self).__init__(**kwargs)
        texture = self._coreimage.texture
        self.reference_size = texture.size
        self.texture = texture

class MainApp(App):
    def build(self):
        return CoverImage(source='cityCC0.png')

MainApp().run()
