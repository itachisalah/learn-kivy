from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string(
    """
<ExampleBackdrop>
    MDBackdrop:
        id:backdrop
        left_action_item:[['menu',lambda x: self.open()]]
        title:"itachi python"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Menu"
        
      
    
    
    """
)

class ExampleBackdrop(Screen):
    pass

class BackDrop(MDApp):
    def build(self):
        return ExampleBackdrop()

BackDrop().run()