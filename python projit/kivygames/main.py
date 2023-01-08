from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
import win32com.client as win


from os import listdir
Window.size = 350,600

PATH ='./kv/'
for kv in listdir(PATH):
    Builder.load_file(PATH+ kv)

class HomeScreen(GridLayout):
    def hello_Salah(self):
        speaker = win.Dispatch("SAPI.SPvoice")
        speaker.Speak("Hello Salah ,would you like to play a game?")

    def hello_Mohamed(self):
        speaker = win.Dispatch("SAPI.SPvoice")
        speaker.Speak("Hello Mohamed ,would you like to play a game?")

    speaker = win.Dispatch("SAPI.SPvoice")
    speaker.Speak("Hello , is this salah or mohamed? Please press you name.?")

class MyApp(App):
    title = 'VoiceGame'

    def build(self):
        return HomeScreen()

if __name__=='__main__':
    MyApp().run()