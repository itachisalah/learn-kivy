from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''
<SizeHint>:
    cols:1
    BoxLayout:
        Button:
            size_hint_y: 0.4
            pos_hint:{'y':0}
            text: 'pos_hint: y=0'
        Button:
            size_hint_y: 0.2
            pos_hint:{'center_y':0.5}
            text: 'pos_hint: center_y=0.5'
        Button:
            size_hint_y: 0.3
            pos_hint:{'top':1}
            text: 'pos_hint: top=1'
            
    BoxLayout:
        orientation:'vertical'
        Button:
            size_hint_x: 0.4
            pos_hint:{'x':0}
            text: 'pos_hint: x=0'
        Button:
            size_hint_x: 0.2
            pos_hint:{'center_x':0.5}
            text: 'pos_hint: center_x=0.5'
        Button:
            size_hint_x: 0.3
            pos_hint:{'right':1}
            text: 'pos_hint: right=1'
    
            

''')

class SizeHint(GridLayout):
    pass

class PosHint(App):
    def build(self):
        return SizeHint()

PosHint().run()