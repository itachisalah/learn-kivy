from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
Window.size = 350,600

class RootWidget(BoxLayout):

    container= ObjectProperty(None)

class MainApp(App):
    def build(self):
        self.root= Builder.load_file('kv/root.kv')

    def next_screen(self, screen):
        filename =screen + '.kv'
        Builder.unload_file('kv/'+filename)
        self.root.container.clear_widgets()
        screen = Builder.load_file('kv/'+filename)
        self.root.container.add_widget(screen)

MainApp().run()