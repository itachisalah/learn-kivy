from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.button import Button
Builder.load_string('''
<Custompopup>:
    size_hint: 0.5,0.5
    title: 'salam alikom'
    auto_dismiss: False
    Button:
        text:'Click and Back'
        on_release: root.dismiss()

''')

class Custompopup(Popup):
    pass

class PopupApp(App):
    def build(self):
        btn = Button(text='show popup', on_release=self.show_popup)
        return btn

    def show_popup(self, btn1):
        btn1 = Custompopup()
        btn1.open()

PopupApp().run()