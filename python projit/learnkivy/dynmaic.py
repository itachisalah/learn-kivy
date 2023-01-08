from kivy.base import runTouchApp
from kivy.lang import Builder

root = Builder.load_string("""
<ImageButton@Button>:
    source: None
    Image:
        source:root.source
        center:root.center

ImageButton:
    source: 'itachii.png'
""")


runTouchApp(root)