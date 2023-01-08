from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
import salah
Window.size= 350,600


class Text_inputApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()
        self.username = Builder.load_string(salah.username_input)
        button= MDRectangleFlatButton(text='show',
                                      pos_hint={'center_x':0.8,'center_y':0.4},
                                      on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        if self.username.text is not "":
            user_error = self.username.text + " user does not exist."
        else:
            user_error = "Please Enter a Username"
        self.dialog = MDDialog(title='check Username',
                               text=user_error,size_hint=(0.8,1),
                               buttons=[MDFlatButton(text='Close',
                                                     on_release=self.close_dialog),
                                        MDFlatButton(text='More')])
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()

Text_inputApp().run()
