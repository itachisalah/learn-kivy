from os.path import dirname, join
from random import randint

import kivy
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from glob import glob
from kivy.logger import Logger



class Picture(Scatter):
    source= StringProperty(None)

class PicturesApp(App):
    def build(self):
        root = self.root
        curdir = dirname(__file__)
        for filename in glob(join(curdir,'images', '*')):
            try:
                picture= Picture(source=filename,rotation= randint(-30,30))
                root.add_widget(picture)
            except Exception as e:
                Logger.exception('images: unable to load <%s>'% filename)

    def on_pause(self):
        return True



if __name__=='__main__':
    PicturesApp().run()

