from time import strftime
from kivy import Config

# a fixed size is set for the app's display when executed
Config.set("graphics", "height", "323")
Config.set("graphics", "width", "444")

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock


class ClockApp(MDApp):
    # Clock object for the clock(in the app) event
    event_clock = None

    def build(self):
        return MainScreen()

    def on_start(self):

        self.event_clock = Clock.schedule_interval(self.root.clock_update, 1)


class MainScreen(MDScreen):
    # Clock object for the Chrono event
    event_chrono = None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.chrono_mins = 0
        self.chrono_secs = 0
        self.total_seconds = 0

    def clock_update(self, dt):

        self.time_label.text = strftime('[b] %H [/b]: %M : %S %p')

    def chrono_update(self, dt):

        self.total_seconds += dt
        self.chrono_mins, self.chrono_secs = divmod(self.total_seconds, 60)


        self.ids.chrono_label.text = f"[b] {str(int(self.chrono_mins)).zfill(2)} [/b]: " \
                                     f"{str(int(self.chrono_secs)).zfill(2)}.[size=30sp]" \
                                     f"{str(int((self.chrono_secs * 100) % 100)).zfill(2)}[/size]"

    def reset_chrono(self):

        self.event_chrono.cancel()
        self.ids.chrono_label.text = "[b] 00 [/b]: 00.[size=30sp]00[/size]"
        self.total_seconds = 0
        self.ids.start_stop_btn.text = "Start"

    def start_stop_chrono(self):

        if self.ids.start_stop_btn.text == "Start":
            self.event_chrono = Clock.schedule_interval(self.chrono_update, 0.042)
            self.ids.start_stop_btn.text = "Stop"
        else:
            self.event_chrono.cancel()
            self.ids.start_stop_btn.text = "Start"


if __name__ == "__main__":
    from kivy.core.text import LabelBase

    LabelBase.register(
        name="Roboto",
        fn_regular="fonts/Roboto-Thin.ttf",
        fn_bold="fonts/Roboto-Medium.ttf"
    )

    ClockApp().run()
