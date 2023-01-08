from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_string("""
<Text>:
    text_size: self.size
    valign: "middle"
    font_name: app. fonts.subheading
    color: [0,0,0, 1]
    shorten_from :"right"
    shorten : True
    markup : True


""")

class Text(Label):
    def __int__(self, **kw):
        super().__int__(**kw)
