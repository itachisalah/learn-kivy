from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse,Line
from random import random


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(),random(),random())
        with self.canvas:
            Color(*color)
            d= 30.
            Ellipse(pos=(touch.x -d, touch.y - d),size=(d,d))
            touch.ud['line']= Line(points=(touch.x,touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]


class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

if __name__=='__main__':
    MyPaintApp().run()