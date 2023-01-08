from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import*
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.togglebutton import ToggleButton
Window.size= 380,600


class Chip(ToggleButton):
    dc= ListProperty([0,0,0,1])
    def __init__(self, **k):
        super().__init__(**k)

    def call(self):
        print("a")

        if self.state =='down':
            self.dc=[1,1,1,1]
            self.color:[0,0,0,1]

        else:
            self.color=[1,1,1,1]
            self.dc:[0,0,0,1]

class Plate(MDCard):
    _image = StringProperty('')
    menu = None
    _video_title = StringProperty('')
    _channel_name = StringProperty('')
    _rimage = StringProperty('')
    _time = StringProperty('0:00:00')
    def on_kv_post(self,obj):
        pass
    def open_menu(self,obj):
        if not self.menu:
            _items= ["Save to WatchLater", 'Save to playlist','Share', 'Report']
            menu_items =[
                {
                    "text": f"{i}",
                    "viewclass":"OneLineListItem",
                    "on_releaese":lambda x = f"{i}":self.menu_callback(x),
                }for i in _items
            ]
            self.menu = MDDropdownMenu(
                caller = obj,
                items = menu_items,
                width_mult = 4,
            )
        self.menu.open()
    def menu_callback(self,text_item):
        print(text_item)

class MainScreen(Screen):
    pass



class Youtube(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return MainScreen()

Youtube().run()