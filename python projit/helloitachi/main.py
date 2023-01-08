from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = '#8B4513'

class Hello(App):
    def build(self):

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(0.6, 0.7)
        self.window.pos_hint={"x":0.2,"y":0.2}
        self.window.add_widget(Image(source="pngegg.png"))

        self.greeting = Label(
                        text="What`s Your Name ?",
                        font_size =18,
                        color= 'FFFF00')
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline = False,
                    padding_y=(20,20),
                    size_hint=(1,0.5) )
        self.window.add_widget(self.user)

        self.button= Button(
                    text="GREET",
                    size_hint=(1, 0.5),
                    bold = True,
                    background_color ='#00FF00' )

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "hello " + self.user.text + " ! "

if __name__=="__main__":
    Hello().run()
