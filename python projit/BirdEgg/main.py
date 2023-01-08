from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.core.window import Window




class LancaTartaruga(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    pontos = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class MoveUrubu(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class MoveCesto(Widget):
    pontos = NumericProperty(0)
    itachi = NumericProperty(0)

class TartarugaGame(Widget):
    tartaruga = ObjectProperty(None)
    urubu = ObjectProperty(None)
    cesto = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    imageBotao = "icon/sonButton1.png"
    loop = ObjectProperty(None)
    estado = "ON"
    SomFundo = ObjectProperty(None)

    popup = None
    def serve_tartaruga(self):
        self.tartaruga.center = self.center
        self.tartaruga.velocity = -Vector(0,4).rotate(0)
        self.btn1.bind(on_press=self.LigaDesLiga)

    def serve_urubu(self):
        self.urubu.center= self.center
        self.urubu.velocity = Vector(4,0).rotate(0)

    def StopGame(self):
        self.tartaruga.velocity = Vector(0,0 ).rotate(0)
        self.urubu.velocity = Vector(0,0).rotate(0)
        self.urubu.center =self.width /2 , self.top-100
        self.tartaruga.center = self.width / 2 ,self.top - 170

    def Yxit(self, instance):
        import sys
        sys.exit()

    def RestartGame(self, instance):
        self.popup.dismiss()
        self.cesto.pontos = 0
        self.cesto.iatchi =0
        self.urubu.center = self.width / 2 , self.top - 100
        self.tartaruga.center = self.width / 2, self.top - 170
        self.urubu.velocity = Vector(4, 0).rotate(0)
        self.tartaruga.velocity = -Vector(0,4).rotate(0)

    def GameOver(self):
        content = BoxLayout(orientation = 'horizontal', size_hint_y= 0.7)
        if (self.cesto.pontos>= 100):
            texto= """
            You made %s Points.
            This is the maximum score.
            if you want to play again, press the button : Restart!
            Or click Exit to end the Game\n
            Credits: itachi python
            email: salaheddinegourtite@gmail.com\n
            """ % self.cesto.pontos
        else:
            texto = """
            You made %s Points.
            This is the maximum score.
            if you want to play again, press the button : Restart!
            Or click Exit to end the Game\n
            Credits: itachi python
            email: salaheddinegourtite@gmail.com\n
            """ % self.cesto.pontos
        replay = Button(text ='Restart')
        yxit = Button(text = 'Go out')
        label = Label(text = texto)
        info = BoxLayout(spacing = 10, orientation = 'horizontal')
        action = BoxLayout(spacing=10,orientation = 'horizontal',size_hint_y = 0.3)
        content = BoxLayout(spacing = 10, orientation = 'vertical')
        info.add_widget(label)
        action.add_widget(replay)
        action.add_widget(yxit)
        content.add_widget(info)
        content.add_widget(action)

        replay.bind(on_press = self.RestartGame)
        yxit.bind(on_press= self.Yxit)

        self.StopGame()

        self.popup = Popup(title= 'Fim',
                           content= content,
                           size_hint= (None,None),
                           size = (400,400),
                           auto_dismiss= False)

        self.popup.open()
    def update(self,dt):
        self.tartaruga.move()
        self.urubu.move()

        if ((self.tartaruga.y <= 55) and (self.tartaruga.y >=50 )):
            if ((self.tartaruga.center_x <= self.cesto.center_x + 20 ) \
                    and (self.tartaruga.center_x >= self.cesto.center_x - 20)):
                self.cesto.pontos += 1

                if(self.cesto.pontos >=100):
                    self.GameOver()
            else:
                self.cesto.itachi += 1

                if(self.cesto.itachi <= 3):
                    self.Loop()
                if(self.cesto.itachi >=3):
                    self.GameOver()

        if (self.tartaruga.y < 50):
            self.tartaruga.center = self.urubu.pos[0], self.top - 170
            self.tartaruga.velocity_y *= 1.1

            if(self.tartaruga.velocity_y < -15.0):
                self.tartaruga.velocity_y = 4 * abs(self.tartaruga.velocity_y)\
                                           / self.tartaruga.velocity_y
        if (self.urubu.x < 25) or (self.urubu.x > self.width - 150):
            self.urubu.velocity_x *= -1.0

    def on_touch_move(self, touch):
        self.cesto.center_x = touch.x

    def LigaDesLiga(self, value):
        if(self.estado):
            if(self.estado == "ON"):
                self.estado = "OFF"

            elif(self.estado == "OFF"):
                self.estado = "ON"

    def MusicaFundo(self,dt):
        if(self.SomFundo):
            if(self.estado =="ON"):
                if(self.SomFundo.status == "stop"):
                    self.SomFundo.play()
            if(self.SomFundo.status == "play"):
                if (self.estado == "OFF"):
                    self.SomFundo.stop()

    def Loop(self):
        if (self.estado):
            if(self.estado =="ON"):
                def paraLoop(dt):
                    self.loop.stop()
                    self.loop.play()
                    Clock.schedule_once(paraLoop, 1.0)

Factory.register("MoveCesto", MoveCesto)
Factory.register("MoveUrubu", MoveUrubu)
Factory.register("LancaTartaruga", LancaTartaruga)


class TartarugaApp(App):
    title = "Bird Egg"
    icon = "icon/UrubuRei.png"

    def build(self):
        game = TartarugaGame()
        game.serve_tartaruga()
        game.serve_urubu()
        game.SomFundo = SoundLoader.load('icon/loop.wav')
        Clock.schedule_interval(game.update, 1.0 / 60)
        return game

if __name__=='__main__':
    TartarugaApp().run()