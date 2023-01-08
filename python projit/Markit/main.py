from kivymd.app import MDApp
from kivy.lang import Builder
from manager.navigation import NavigationManager
from kivy import properties as p


class MainScreenManager(NavigationManager):
    pass


with open('main.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class MarkitApp(MDApp):
    manager =p.ObjectProperty(None)

    def build(self):
        self.theme_cls.primary_palette ="Indigo"
        self.theme_cls.primary_hue = "900"

        self.manager = MainScreenManager()
        return self.manager

if __name__ == "__main__":
    MarkitApp().run()
