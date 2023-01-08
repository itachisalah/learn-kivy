from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import random
import webbrowser

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty, NumericProperty
from kivy.utils import get_color_from_hex

from json_settings import json_settings
from arithmetic import Arithmetic


Window.clearcolor = get_color_from_hex("#16203B")

LabelBase.register(
    name = "Roboto",
    fn_regular= "fonts/Roboto-Thin.ttf",
    fn_bold="fonts/Roboto-Medium.ttf"
)

class KivyTutorRoot(BoxLayout):
    math_screen = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(KivyTutorRoot, self).__init__(**kwargs)
        self.screen_list = []
        self.is_mix = False
        self.math_popup = MathPopup()

    def changeScreen(self, next_screen):
        operations = "addition subtraction multiplication division".split()
        question = None

        if self.ids.kivy_screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.kivy_screen_manager.current)

        if next_screen == "about this app":
            self.ids.kivy_screen_manager.current = "about_screen"

        else:
            if next_screen == "mix!":
                self.is_mix = True
                index = random.randint(0, len(operations) - 1)
                next_screen = operations[index]
            else:
                self.is_mix = False
            for operation in operations:
                if next_screen == operation:
                    question= "self.math_screen.get_{}_question()".format(
                        operation)

            self.math_screen.question_text.text = KivyTutorRoot.prepQuestion(
                eval(question) if question is not None else None
            )
            self.ids.kivy_screen_manager.current = "math_screen"

    @staticmethod
    def prepQuestion(question):

        if question is None:
            return "ERROR"
        text_list = question.split()
        text_list.insert(2 , "[b]")
        text_list.insert(len(text_list), "[/b]")
        return " ".join(text_list)

    def onBackBtn(self):
        if self.screen_list:
            self.ids.kivy_screen_manager.current = self.screen_list.pop()
            return True
        return False

class MathScreen(Screen, Arithmetic):

    def __init__(self, *args, **kwargs):
        super(MathScreen, self).__init__(*args, **kwargs)


class MathPopup(Popup):
    GOOD = "{} :D"
    BAD = "{}, Correct answer is [b]{}[/b]"
    GOOD_LIST = "Awesome! Amaing! Excellent! Coorect!".split()
    BAD_LIST = ["Almost!", "Close!", "Sorry", "Don`t Worry"]

    message = ObjectProperty()
    wrapped_button = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(MathPopup, self).__init__(*args, **kwargs)


    def open(self, correct=True):
        if correct:
            if self.wrapped_button in self.content.children:
                self.content.remove_widget(self.wrapped_button)
        else:
            if self.wrapped_button not in self.content.children:
                self.content.add_widget(self.wrapped_button)

        self.message.text = self._prep_text(correct)

        super(MathPopup, self).open()
        if correct:
            Clock.schedule_once(self.dismiss, 1)

    def _prep_text(self, correct):
        if correct:
            index = random.randint(0, len(self.GOOD_LIST) - 1)
            return self.GOOD.format(self.GOOD_LIST[index])
        else:
            index = random.randint(0, len(self.BAD_LIST)- 1)
            math_screen = App.get_running_app().root.math_screen
            answer = math_screen.get_answer()
            return self.BAD.format(self.BAD_LIST[index], answer)


class KeyPad(GridLayout):

    def __init__(self, *args, **kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)
        self.cols = 3
        self.spacing = 10
        self.createButtons()

    def createButtons(self):
        _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "", "GO!"]
        for num in _list:
            self.add_widget(Button(text=str(num), on_release=self.onBtnPress))

    # --------------------------------------------------------------------------
    def onBtnPress(self, btn):
        math_screen = App.get_running_app().root.ids.math_screen
        answer_text = math_screen.answer_text

        if btn.text.isdigit():
            answer_text.text += btn.text
        if btn.text == "GO!" and answer_text.text != "":
            answer = math_screen.get_answer()
            root = App.get_running_app().root
            if int(answer_text.text) == answer:
                root.math_popup.open(True)
            else:
                root.math_popup.open(False)
            # Clear the answer text
            answer_text.text = ""
            # Prepare to get new question
            question = math_screen.question_text
            question.text = root.prepQuestion(
                math_screen.get_next_question(True if root.is_mix else False)
            )


class KivyTutorApp(App):

    def __init__(self, **kwargs):
        super(KivyTutorApp, self).__init__(**kwargs)
        self.use_kivy_settings = False
        Window.bind(on_keboard = self.onBackBtn)

    def onBackBtn(self, window, key , *args):
        if key == 27:
            return self.root.onBackBtn()

    def build(self):
        return KivyTutorRoot()

    def getText(self):
        return ("Hey There!\n My name salaheddine\n"
                "My chnnale :[b][ref=website]youtube[/ref][/b]")

    def on_ref_press(self, instance, ref):
        _dict= {
            "website": "https://www.youtube.com/channel/UCOoYJv5SfcQiS0F-JrsAKCQ"

        }
        webbrowser.open(_dict[ref])

    def build_config(self, config):
        config.setdefaults("General", {"lower_num": 0, "upper_num": 10})

    def build_settings(self, settings):
        settings.add_json_panel("MAth from Itachi python", self.config,data=json_settings)

    def on_config_change(self, config, section, key, value):
        if key == "upper_num":
            self.root.math_screen.max_num = int(value)
        elif key == "lower_num":
            self.root.math_screen.min_num = int(value)


if __name__ == '__main__':
    KivyTutorApp().run()

