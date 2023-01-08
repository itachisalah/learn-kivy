from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation
from kivy.properties import NumericProperty


Window.size= (350,600)

class DribbleUi(MDScreen):
    animation_constant= NumericProperty(40)

    def __init__(self, **kw):
        super().__init__(**kw)
        anim = Animation(animation_constant=10, duration=0.6 , t='in_out_quad') + Animation(animation_constant=40,
                                                                                            duration=0.6, t='in_out_quad')
        anim.repeat = True
        anim.start(self)


class Iatchi(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    Iatchi().run()
