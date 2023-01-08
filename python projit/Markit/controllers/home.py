from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp as App
from kivy.lang import Builder


class HomeMainScreen(MDScreen):
    pass


with open('views/home.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class HomeScreenApp(App):
    def build(self):
        return HomeMainScreen


def main():
    HomeScreenApp().run()


if __name__=='__main__':
    main()