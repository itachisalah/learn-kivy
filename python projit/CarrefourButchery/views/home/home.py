from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty

Window.size = 400,600


Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    def __init__(self, **kw) ->None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, 0.1)

    def render(self, _):
        plants =[
            {
                'name': 'Meat Strip',
                'station': 'Egpyt',
                'source':'assets/imgs/1.png',
                'price': 25.95,
            },
            {
                'name': 'Ground Meat',
                'station': 'PAKISTAN',
                'source': 'assets/imgs/2.png',
                'price': 19.95,
            },

            {
                'name': 'Meat Thigh',
                'station': 'Maroc',
                'source': 'assets/imgs/3.png',
                'price': 30.95,
            },
            {
                'name': 'Camel Meat ',
                'station': 'KSA',
                'source': 'assets/imgs/4.png',
                'price': 26.95,
            },
            {
                'name': 'Meat ',
                'station': 'algrie',
                'source': 'assets/imgs/5.png',
                'price': 23.95,
            },
            {
                'name': 'His Liver',
                'station': 'Local',
                'source': 'assets/imgs/6.png',
                'price': 27.95,
            },
            {
                'name': 'Meat with Bones',
                'station': 'Local',
                'source': 'assets/imgs/7.png',
                'price': 19.95,
            },
            {
                'name': 'half Lamb',
                'station': 'Ksa',
                'source': 'assets/imgs/8.png',
                'price': 190,
            },
        ]

        self.ids.plants.clear_widgets()
        for p in plants:
            pl = Plant()
            pl.name =p['name']
            pl.source = p['source']
            pl.price = p['price']
            pl.station =p['station']
            pl.bind(on_release = self.view_plant)

            self.ids.plants.add_widget(pl)


    def view_plant(self, inst):
        pv = App.get_running_app().root.ids.plant
        mngr = App.get_running_app().root.ids.scrn_mngr

        pv.name = inst.name
        pv.price = inst.price
        pv.source = inst.source
        pv.station = inst.station
        mngr.current = 'scrn_plant'

class Plant(ButtonBehavior, BoxLayout):
    name = StringProperty("")
    station = StringProperty("")
    source = StringProperty("")
    price = NumericProperty(0)
    radius = NumericProperty(dp(24))
    def __init__(self, **kw) ->None:
        super().__init__(**kw)