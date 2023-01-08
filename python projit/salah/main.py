
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
Window.size=(300,500)

KV = '''


<ContentNavigationDrawer>



    MDNavigationDrawerMenu:
        MDNavigationDrawerHeader:
            title: "Project"
            text: "Calculator"





        MDNavigationDrawerDivider:

        MDNavigationDrawerLabel:
            text: 'Apps'

        MDNavigationDrawerItem:
            icon: 'calculator'
            text: 'Calculator'
            on_press:
                root.nav_drawer.set_state('close')
                root.screen_manager.current= 'calculator'

        MDNavigationDrawerDivider:

        MDNavigationDrawerLabel:
            text: 'Other'

        MDNavigationDrawerItem:
            text: 'Settings'
            icon: 'cog'
            on_press:
                root.nav_drawer.set_state('close')
                root.screen_manager.current= 'settings'


MDScreen:


    MDTopAppBar:
        title: 'Application'
        pos_hint: {'top':1}
        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]


    MDNavigationLayout:


        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: 'calculator'
                MDLabel:
                    text: 'Welcome to calculator'
                    halign: 'center'

            MDScreen:
                name: 'settings'

                MDRectangleFlatButton:
                    text: 'Change Palette' 
                    pos_hint: {'center_x':0.7,'center_y':0.8}
                    on_press: app.switch_accent_palette()

                MDLabel:
                    text: 'Change theme'
                    pos_hint: {'center_x': 0.55, 'center_y': 0.8}



        MDNavigationDrawer:
            id:nav_drawer
            radius: (0,16,16,0)
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer:nav_drawer


'''


# Making a class for adding NavigationContents
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


# Main App Class
class IatchiApp(MDApp):
    def build(self):
        sc = Screen()

        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Light'

        sc.add_widget(Builder.load_string(KV))

        return sc

    def switch_accent_palette(self):
        self.theme_cls.primary_palette=('Red' if self.theme_cls.primary_palette == 'Blue' else 'Blue')

if __name__=='__main__':
    IatchiApp().run()