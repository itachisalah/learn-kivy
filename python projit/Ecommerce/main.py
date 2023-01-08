from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screens.homepage import HomePage



class EcommerceShoeApp(MDApp):
    def build(self):
        self.load_all_kv_files()
        Window.size = 330, 600
        return HomePage()


    def load_all_kv_files(self):
        Builder.load_file("libs/screens/homepage.kv")
        Builder.load_file("libs/componts/appbar.kv")
        Builder.load_file("libs/componts/product_dropdown.kv")
        Builder.load_file("libs/componts/categories.kv")
        Builder.load_file("libs/componts/circular_item.kv")

    def on_start(self):
        self.root.dispatch('on_enter')

if __name__ == '__main__':
    EcommerceShoeApp().run()