from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.taptargetview import MDTapTargetView
KV="""
Screen :
    MDFloatingActionButton:
        id: button
        icon: "language-python"
        pos :10 ,10
        on_release: app.tap_target_start()

"""
class TapTargetView(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget= screen.ids.button,
            title_text= "This is button Python",
            description_text= "your Description here",
            widget_position= "left_bottom",
        )
        return screen

    def tap_target_start(self):
        if self.tap_target_view.state== "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

TapTargetView().run()