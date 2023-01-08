from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_string('''
<Test>:
    size_hint:0.5,0.5
    pos_hint:{'center_x':0.5,'center_y':0.5}
    do_default_tab: False
    
    TabbedPanelItem:
        text:'first tab'
        Label:
            text:'First Tab content area'
    TabbedPanelItem:
        text:'tab2'
        BoxLayout:
            Label:
                text:'Second tab content area'
            Button:
                text:'Button'
    TabbedPanelItem:
        text:'tab3'
        RstDocument:
            text:
                '\\n'.join(("Hello Itachi","----------",
                "You are in the third tab...."))
''')

class Test(TabbedPanel):
    pass

class TabbedPanelApp(App):
    def build(self):
        return Test()

if __name__=='__main__':
    TabbedPanelApp().run()