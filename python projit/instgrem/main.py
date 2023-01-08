from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
import json

class CircularAvatarImage(MDCard):
    avatar= StringProperty()
    name= StringProperty()

class StoryCreator(MDCard):
    avatar = StringProperty()

class PostCard(MDCard):
    profile_pic= StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_ago = StringProperty()



class HomePage(MDScreen):
    profile_picture='https://costumesheaven.b-cdn.net/wp-content/uploads/2022/08/itachi-uchiha-naruto-pozadina-86192_w635.jpg'


    def on_enter(self):
        self.list_stories()
        self.list_posts()

    def list_stories(self):
        with open('itachi/stories.json') as f_obj:
            data= json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(avatar=data[name]['avatar'],name=name))

    def list_posts(self):
        with open('itachi/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(username=username,
                                                      avatar=data[username]['avatar'],
                                                      profile_pic=self.profile_picture,
                                                      post=data[username]['post'],
                                                      caption= data[username]['caption'],
                                                      likes=data[username]['likes'],
                                                      comments= data[username]['comments'],
                                                      posted_ago= data[username]['posted_ago']


                ))






class MainApp(MDApp):

    def build(self):
        Window.size =300, 600
        Builder.load_file('home_page.kv')
        return HomePage()

    def on_start(self):
        self.root.dispatch('on_enter')

if __name__=='__main__':
    MainApp().run()
