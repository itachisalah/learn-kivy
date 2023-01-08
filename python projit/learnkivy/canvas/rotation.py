from kivy.app import App
from kivy.lang import Builder

V='''
FloatLayout:
    Button:
        text:'hi Python'
        size_hint:None,None
        pos_hint:{'center_x':0.5,'center_y':0.5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 45
                origin: self.center
                
        canvas.after:
            PopMatrix
        
    


'''

class RotationApp(App):
    def build(self):
        return Builder.load_string(V)

RotationApp().run()