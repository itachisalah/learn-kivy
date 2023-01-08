from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.list import ThreeLineListItem
from datetime import date
import csv

from kivy.core.window import Window

Window.size = (415, 600)


class WindowSignin(Screen):
    pass


class WindowSignup(Screen):
    pass


class WindowMain(Screen):
    pass


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu = None
        self.screen = Builder.load_file("string.kv")

    def build(self):
        self.title = 'I.T Maintance'
        self.icon = "./assets/lamp.ico"

        return self.screen

    def on_start(self):
        self.issues()

    def message_login(self):
        self.root.get_screen('signin').add_widget((MDLabel(
            text='Email is invalid.',
            pos_hint={'center_y': 0.4, 'center_x': 0.5},
            size_hint=(.5, .5),
            halign='center',
            font_style="Caption"
        )))

    def database_login(self):
        email_user = self.root.get_screen("signin").ids.user_email.text

        with open("database.csv", "r", newline="") as f:
            reader = csv.reader(f, delimiter=";")
            for log in reader:
                if log[1] == email_user:
                    # fazer a janela correr para direita
                    self.root.current = "main"
                    self.root.get_screen('main').ids.label_welcome.text = f"Hi {log[0]}, Welcome!"
                    self.root.get_screen('main').ids.label_welcome.font_size = "23dp"
                    return log

                else:
                    self.message_login()

    def signup_register(self):
        with open("database.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter=";")

            name = self.root.get_screen("signup").ids.name_register.text
            email = self.root.get_screen("signup").ids.email_register.text
            sector = self.root.get_screen("signup").ids.password_register.text

            writer.writerow([name, email, sector])

    def issues(self):
        with open("issues.csv", "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader, None)
            menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f'{i[0]}',
                    "on_release": lambda x=f"{i[0]}": self.set_item(x),
                } for i in reader]

            self.menu = MDDropdownMenu(
                caller=self.root.get_screen('main').ids.field_issue,
                items=menu_items,
                position="auto",
                width_mult=3,
            )

    def set_item(self, text__item):
        self.root.get_screen('main').ids.field_issue.text = text__item
        self.menu.dismiss()

    def requests(self):
        with open("request.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter=";")

            name = self.database_login()[0]
            issue = self.root.get_screen("main").ids.field_issue.text
            describe = self.root.get_screen("main").ids.field_describe.text
            time = date.today().strftime("%m/%d/%Y")
            department = self.database_login()[2]

            writer.writerow([name, issue, describe, time, department])

    def queue(self):
        # clean the widgets to update de view
        if self.root.get_screen('main').ids.container.children:
            self.root.get_screen('main').ids.container.clear_widgets()

        count = 0
        with open("request.csv", "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader:
                self.root.get_screen("main").ids.container.add_widget(
                    ThreeLineListItem(
                        text=f"{i[0]}- {i[3]} ",
                        secondary_text=f"Issue: {i[1]} ({i[4]})",
                        tertiary_text=f"Describe Issue: {i[2]}"

                    ))
                count += 1


if __name__ == '__main__':
    MyApp().run()
