from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class LabelApp(MDApp):
    def build(self):
        #label = MDLabel(text= "hello salah", halign="center", theme_text_color="Error")

        #label = MDLabel(text="hellow itachi", halign= "center", theme_text_color= "Custom", text_color =(0,1,0,1))

        lab = MDIcon(icon= "language-python",)

        return lab

LabelApp().run()