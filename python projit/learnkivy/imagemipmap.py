from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.scatter import ScatterPlane
from os.path import join

class ImageMipmapApp(App):
    def build(self):
        s= ScatterPlane(scale= 0.5)
        filename= join('itachii.png')
        imag= Image(source=filename,pos=(400,100),size=(256,256))
        imag1 = Image(source=filename, pos=(400, 365), size=(256, 256),
                      mipmap= True)
        s.add_widget(imag)
        s.add_widget(imag1)

        return s

ImageMipmapApp().run()