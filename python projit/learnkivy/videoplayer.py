from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from sys import argv
from os.path import dirname, join
from kivy.core.window import Window
Window.size= 350,600

class VideoPlayerApp(App):
    def build(self):
        if len(argv) >1:
            filename= argv[1]
        else:
            curdir = dirname(__file__)
            filename= join(curdir,'tiwtiw.mp4')

        return VideoPlayer(source= filename, state='play')

VideoPlayerApp().run()