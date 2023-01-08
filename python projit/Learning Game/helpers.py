from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
<InfoPopup>:
    auto_dismiss:True
    size_hint: None ,None
    size : 400, 200
    on_open : root.dismiss_trigger()
    title:root.title
    Label:
        text: root.text
    
    


''')


class InfoPopup(Popup):
    title = StringProperty('information')
    text = StringProperty('')

    def __init__(self, time= 2 , **kwargs):
        super(InfoPopup, self).__init__(**kwargs)
        self.dismiss_trigger = Clock.create_trigger(self.dismiss, time)