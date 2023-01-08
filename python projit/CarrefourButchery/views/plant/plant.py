from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty,NumericProperty

Builder.load_file('views/plant/plant.kv')

class PlantView(BoxLayout):
    name = StringProperty("")
    station = StringProperty("")
    source = StringProperty("")
    price = NumericProperty(0)
    def __init__(self, **kw):
        super().__init__(**kw)