from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class salahApp(MDApp):
    def build(self):

        #label1 = MDLabel(text="Facebbok",halign="center", theme_text_color="Error",font_style="Subtitle2"

        #label2= MDLabel(text="Google", halign="center", theme_text_color="Custom",text_color=(0,1,0,1))
                                                                                            # red ,green, blue
        label3 =MDIcon(icon="language-python", halign="center",pos_hint={'center_x':0.8,'center_y':0.9})
        return label3

salahApp().run()