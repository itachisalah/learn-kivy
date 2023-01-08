from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
import datetime
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView

#                    red,green,blue
Window.clearcolor = '#7FFF00'
Window.size=(400,600)


class Myapp(ScrollView):
    text=StringProperty('')
runTouchApp(Myapp())

