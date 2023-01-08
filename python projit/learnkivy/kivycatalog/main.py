
import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder, Parser,ParserException
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window
Window.size= 350,600



CATALOG_ROOT = os.path.dirname(__file__)


CONTAINER_KVS = os.path.join(CATALOG_ROOT,'container_kvs')
CONTAINER_CLASSES =[c[:-3]for c in os.listdir(CONTAINER_KVS)
                    if c.endswith('.kv')]

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.previous_text = open(self.kv_file).read()
        parser = Parser(content=self.previous_text)
        widget= Factory.get(parser.root.name)()
        Builder._apply_rule(widget, parser.root, parser.root)
        self.add_widget(widget)


    @property
    def kv_file(self):
        return os.path.join(CONTAINER_KVS, self.__class__.__name__+'.kv')


for class_name in CONTAINER_CLASSES:
    globals()[class_name]= type(class_name,(Container,),{})



class KivyRenderTextInput(CodeInput):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        is_osx = sys.platform == 'darwin'

        ctrl , cmd = 64, 1024
        key, key_str= keycode
        if text and key not in (list(self.interesting_keys.keys())+[27]):
            if modifiers ==['ctrl']or (is_osx and modifiers== ['meta']):
                if key == ord('s'):
                    self.catalog.change_kv(True)
                    return
        return  super(KivyRenderTextInput, self).keyboard_on_key_down(
            window, keycode, text, modifiers
        )




class Catalog(BoxLayout):
    language_box= ObjectProperty()
    screen_manager= ObjectProperty()
    _change_kv_ev= None

    def __init__(self,**kwargs):
        self._previously_parsed_text=''
        super(Catalog, self).__init__(**kwargs)
        self.show_kv(None,'Welcome')
        self.carousel = None

    def show_kv(self, instance, value):
        self.screen_manager.current = value
        child = self.screen_manager.current_screen.children[0]
        with open(child.kv_file, 'rb') as file:
            self.language_box.text = file.read().decode('utf8')
        if self._change_kv_ev is not None:
            self._change_kv_ev.cancel()
        self.change_kv()
        self.language_box.reset_undo()

    def schedule_reload(self):
        if self.auto_reload:
            txt= self.language_box.text
            child = self.screen_manager.current_screen.children[0]
            if txt== child.previous_text:
                return
            child.previous_text=txt
            if self._change_kv_ev is not None:
                self._change_kv_ev.cancel()
            if self._change_kv_ev is None:
                self._change_kv_ev = Clock.create_trigger(self.change_kv,2)
            self._change_kv_ev()


    def change_kv(self, *largs):
        txt= self.language_box.text
        kv_container = self.screen_manager.current_screen.children[0]
        try:
            parser= Parser(content=txt)
            kv_container.clear_widgets()
            widget=Factory.get(parser.root.name)()
            Builder._apply_rule(widget, parser.root, parser.root)
            kv_container.add_widget(widget)
        except (SyntaxError,ParserException) as e:
            self.show_error()
        except Exception as e:
            self.show_error(e)
    def show_error(self, e):
        self.info_label.text = str(e).encode('utf-8')
        self.anim = Animation(top= 190.0, opacity = 1, d =2, t='in_back') +\
                    Animation(top= 190.0, d= 3)+\
                    Animation(top= 0 , opacity = 0, d=2)
        self.anim.start(self.info_label)

class KivyCatalogApp(App):
    def build(self):
        return Catalog()

if __name__=='__main__':
    KivyCatalogApp().run()