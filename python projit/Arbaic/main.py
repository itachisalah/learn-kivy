from kivmob import KivMob, TestIds, RewardedListenerInterface

from kivy.app import App
from kivy.uix.button import Button

class RewardedVideoTest(App):
    """ Display a rewarded video ad on button release.
    """

    def build(self):
        self.ads = KivMob( 'ca-app-pub-3940256099942544~3347511713')
        self.ads.load_rewarded_ad( 'ca-app-pub-3940256099942544/8691691433')
        # Add any callback functionality to this class.
        self.ads.set_rewarded_ad_listener(RewardedListenerInterface())
        return Button(text='Show Rewarded Ad',
                      on_release=lambda a:self.ads.show_rewarded_ad())

    def on_resume(self):
        self.ads.load_rewarded_ad(TestIds.REWARDED_VIDEO)

if __name__ == "__main__":
    RewardedVideoTest().run()