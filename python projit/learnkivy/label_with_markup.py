from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
Label:
    text:
        ('[b]Itachi[/b][color=1b2dd1] Python[/color]\\n'
        '[color=f7cf07]Itachi[/color][b] Python[/b]')
    
    markup: True
    font_size: 64



''')

class LabelWithMarkup(App):
    def build(self):
        return root

LabelWithMarkup().run()