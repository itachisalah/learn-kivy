from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class CircularItem(MDCard):
    avatar_card= StringProperty()
    name = StringProperty()
    price = StringProperty()
    discount = StringProperty()