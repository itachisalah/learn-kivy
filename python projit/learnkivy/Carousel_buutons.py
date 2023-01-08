from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window

Window.size= 350,600

Builder.load_string('''
<Page>:
    cols: 3
    Label:
        text:str(id(root))
    Button
    Button
    Button
    Button
        text:'load(page1)'
        on_release:
            carousel = root.parent.parent
            carousel.load_slide(carousel.slides[2])
    Button
    Button
        text: 'prev'
        on_release:
            root.parent.parent.load_previous()
    Button
    Button
        text: 'Next'
        on_release:
            root.parent.parent.load_next()
        
''')

class Page(GridLayout):
    pass

class TestApp(App):
    def build(self):
        root = Carousel()
        for x in range(3):
            root.add_widget(Page())

        return root

TestApp().run()