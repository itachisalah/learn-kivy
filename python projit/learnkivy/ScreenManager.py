from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import NumericProperty
Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

<CustomScreen>:
    hue: random()
    canvas:
        Color:
            hsv:self.hue, 1,1
        Rectangle:
            size:self.size
    Label:
        font_size: 42
        text:root.name
    Button:
        text:'Next Screen'
        size_hint: None,None
        pos_hint:{'right':1}
        size:150,50
        on_release: root.manager.current = root.manager.next()
    
    Button:
        text:'Previous Screen'
        size_hint: None,None
        size:150,50
        on_release: root.manager.current = root.manager.previous()
    
    BoxLayout:
        size_hint:0.5,None
        height:250
        pos_hint:{'center_x':0.5}
        orientation:'vertical'
        
        Button:
            text:'use SlideTransition with "up"'
            on_release:root.manager.transition =\
            SlideTransition(direction="up")
        
        Button:
            text:'use SlideTransition with "down"'
            on_release:root.manager.transition =\
            SlideTransition(direction="down")
        
        Button:
            text:'use SlideTransition with "left"'
            on_release:root.manager.transition =\
            SlideTransition(direction="left")
        
        Button:
            text:'use SlideTransition with "right"'
            on_release:root.manager.transition =\
            SlideTransition(direction="right")
            
        Button:
            text:'Use SwapTransition'
            on_release:root.manager.transition= SwapTransition()
        
        Button:
            text:'Use WipeTransition'
            on_release:root.manager.transition= WipeTransition()
        
        Button:
            text:'Use RiseInTransition'
            on_release:root.manager.transition= RiseInTransition()
        
        Button:
            text:'Use FallOutTransition'
            on_release:root.manager.transition= FallOutTransition()
        
        Button:
            text:'Use NoTransition'
            on_release:root.manager.transition= NoTransition()
        
        Button:
            text:'Use FadeTransition'
            on_release:root.manager.transition= FadeTransition()


''')

class CustomScreen(Screen):
    hue= NumericProperty(0)

class ScreenManagerApp(App):
    def build(self):
        root = ScreenManager()
        for x in range(10):
            root.add_widget(CustomScreen(name='Screen %d' % x))
        return root

ScreenManagerApp().run()