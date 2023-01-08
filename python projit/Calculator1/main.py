from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'width', 300)
Config.set('graphics','height', 600)


class Calc(BoxLayout):

    def clicarBotao(self,xx):
        sss = '/*-+'

        try:
            if self.output.text == '0' or self.result:
                assert xx not in sss
                self.output.text = xx
                self.result = False
            else:
                if xx in sss:
                    for x in sss:
                        assert x not in self.output.text
                    self.output.text += xx
                else:
                    self.output.text += xx
        except:
            pass

    def apagar(self):
        if self.result == False:

            if len(self.output.text) == 1:
                self.output.text = '0'
            else:
                self.output.text = self.output.text[:-1]

    def resultado(self):
        try:
            result = float(eval(self.output.text))
            if result.is_integer():
                result = int(result)
            self.output.text = str(result)
            self.result = True
        except:
            pass

class MyApp(App):

    def build(self):
        self.title = 'Calculator'
        self.icon = 'calc.png'
        return Calc()

if __name__=='__main__':
    MyApp().run()
