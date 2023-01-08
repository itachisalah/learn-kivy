from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size=350,600

screen_itachi="""
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    
<MenuScreen>:
    name : 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint:{'center_x':.5,'center_y':.6}
        on_press:root.manager.current ='profile'
        
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint:{'center_x':.5,'center_y':.5}
        on_press:root.manager.current ='upload'
        
<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:'profile salah hello my dear'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint:{'center_x':0.5,'center_y':.2}
        on_press:root.manager.current ='menu'
        
<UploadScreen>:
    name:'upload'
    MDLabel:
        text:'Upload 123 '
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint:{'center_x':0.5,'center_y':.2}
        on_press:root.manager.current='menu'                      
        
"""
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

screenm = ScreenManager()
screenm.add_widget(MenuScreen(name='menu'))
screenm.add_widget(ProfileScreen(name='profile'))
screenm.add_widget(UploadScreen(name='upload'))


class SwitchingApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_itachi)
        return screen

SwitchingApp().run()