
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.animation import Animation

Window.size= 350,600

class TestApp(App):

    def animate(self,instance):

        animation = Animation(pos=(100,100), t='out_bounce')
        animation += Animation(pos=(200,100),t= 'out_bounce')
        animation &= Animation(pos=(250,500))
        animation +=Animation(pos=(100,50))
        animation +=Animation(pos=(250,0))

        animation.start(instance)


    def build(self):
        b1 = Button(text= 'animation',size_hint=(None,None),
                    on_press= self.animate)

        return b1

if __name__=='__main__':
    TestApp().run()
