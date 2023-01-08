from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_age = StringProperty()



