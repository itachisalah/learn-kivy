
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.lang import Builder

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    
    Camera:
        id: camera
        resolution:(640,480)
        play: False
    ToggleButton:
        text:'Play'
        size_hint_y:None
        height: 48
        on_press: camera.play = not camera.play
    Button:
        text:'Capture'
        size_hint_y: None
        height: 48
        on_press:root.capture()

''')

class CameraClick(BoxLayout):
    def capture(self):

        camera= self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("caputre")

class CameraApp(App):
    def build(self):
        b1 = CameraClick()
        return b1

if __name__=='__main__':
    CameraApp().run()
