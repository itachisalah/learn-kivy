from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string("""
<text>:
    text_size:  self.size
    valign : "middle"
    font_name : app.fonts.subheading
    shoten_from :"right"
    shorten : True
    color :[0,0,0,1]
    markup: True

""")

class Text(Label):
    def __init__(self, **kw):
        super().__init__(**kw)