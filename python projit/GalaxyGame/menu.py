from kivy.uix.relativelayout import RelativeLayout


class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.on_opacity == 0:
            return False
        return super(RelativeLayout, self).on_touch_down(touch)