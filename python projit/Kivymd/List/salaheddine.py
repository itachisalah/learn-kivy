from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string(

    '''
#:import images_path kivymd.images_path

<CustomOneLineIconListItem>

    IconLeftWidget:
        icon: root.icon
            
            
<PreviousMDIcons>
    MDBoxLayout:
        orientation:  'vertical'
        spacing: 10
        padding: 20
        MDBoxLayout:
            adaptive_height: True
            
            MDIconButton:
                icon: 'magnify'
            MDTextField:
                id : search_field
                hint_text:'Search icon'
                on_text:root.set_list_md_icons(self.text, True)
                
        RecycleView:
            id : rv
            key_viewclass:'viewclass'
            key_size: 'height'
            
            RecycleBoxLayout:
                padding :10
                default_size : None , 48
                default_size_hint : 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation:'vertical'
    
    '''
)

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class PreviousMDIcons(Screen):
    def set_list_md_icons(self, text="", search=False):

        def add_icon_item(name_icon):
            self.ids.rv.data.append({
                "viewclass":"CustomOneLineIconListItem",
                "icon":name_icon,
                "text":name_icon,
                "callback":lambda x: x,

            })
        self.ids.rv.data=[]
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

class ItachiApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen= PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()
ItachiApp().run()