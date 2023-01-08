from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

s = Spinner(
    text= 'Python',
    values= ('Python','java','C#','PHP','C++'),
    size_hint=(None,None),size=(100,44),
    pos_hint={'center_x':0.5,'center_y':0.5}
)



runTouchApp(s)