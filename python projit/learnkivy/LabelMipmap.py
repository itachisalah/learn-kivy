from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import ScatterPlane

class LabelMipmapApp(App):
    def build(self):
        s = ScatterPlane(scale=0.5)
        l = Label(text='Iatchi Python', font_size=95, pos= (400,100),mipmap= True)
        l1 = Label(text= 'salaheddine', font_size=95, pos= (400,328))
        s.add_widget(l)
        s.add_widget(l1)
        return s

LabelMipmapApp().run()