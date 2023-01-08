from kivy.app import App
from kivy.lang import Builder

KV='''
BoxLayout:
    orientation:'vertical'
    
    Camera:
        id: camera
        resolution: 499,399
    
    BoxLayout:
        orientation:'horizontal'
        size_hint_y: None
        height: '48dp'
        Button:
            text: 'Start'
            on_release: camera.play = True
        Button:
            text: 'Stop'
            on_release: camera.play = False
    
'''


class CameraApp(App):
    def build(self):
        return Builder.load_string(KV)

CameraApp().run()