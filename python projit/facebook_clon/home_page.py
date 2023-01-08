import json

from kivymd.uix.screen import MDScreen

from components.onilne_friends import OnlineAvatarImage
from components.story_widget import StoryWidget
from components.posts import Post


class HomePage(MDScreen):
    profile_pic="https://www.whatspaper.com/wp-content/uploads/2021/12/hd-itachi-uchiha-wallpaper-whatspaper-12-300x536.jpg"

    def on_enter(self):
        self.list_online_friends()
        self.list_stories()
        self.list_post()

    def list_online_friends(self):
        with open("assets/online_friends_data.json") as f:
            data = json.load(f)
            for friend in data:
                self.ids.online_friends.add_widget(OnlineAvatarImage(
                    avatar=data[friend]['avatar']
                ))

    def list_stories(self):
        with open("assets/stories_data.json") as f:
            data = json.load(f)
            for friend_name in data:
                self.ids.stories.add_widget(StoryWidget(
                    name = friend_name,
                    image=data[friend_name]['image'],
                    avatar=data[friend_name]['avatar']
                ))

    def list_post(self):
        with open("assets/posts_data.json") as f:
            data = json.load(f)
            for friend_name in data:
                self.ids.timeline.add_widget(Post(
                    name=friend_name,
                    avatar=data[friend_name]['avatar'],
                    post=data[friend_name]['post'],
                    likes = data[friend_name]['likes'],
                    comments = data[friend_name]['comments'],
                    caption =data[friend_name]['caption'],
                    updated_ago =data[friend_name]['updated_ago'],

                ))