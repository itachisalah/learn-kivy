from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion, AccordionItem

Window.size=350,600

class AccordionApp(App):
    def build(self):

        root = Accordion()
        for x in range(3):
            item = AccordionItem(title='Title %d' % x)
            item.add_widget(Label(text='Itachi Python\n' *5))
            root.add_widget(item)
        return root

if __name__=='__main__':
    AccordionApp().run()
