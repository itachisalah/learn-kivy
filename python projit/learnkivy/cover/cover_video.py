from kivy.app import App
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.video import Video

class CoverVideo(CoverBehavior,Video):
    def _on_video_frame(self, *largs):
        video = self._video
        if not video:
            return
        texture = video.texture
        self.reference_size = texture.size
        self.calculate_cover()
        self.duration = video.duration
        self.position = video.position
        self.texture= texture
        self.canvas.ask_update()


class MainApp(App):
    def build(self):
        return CoverVideo(source='cityCC0.mpg',play= True)

MainApp().run()