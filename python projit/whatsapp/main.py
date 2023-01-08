from kivy.lang import Builder
from kivy.properties import StringProperty ,DictProperty , OptionProperty, BooleanProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

from demo.demo import profiles


Window.size =(320,600)

Builder.load_file('story.kv')
Builder.load_file('chat_list_item.kv')
Builder.load_file('chat_screen.kv')
Builder.load_file('text_field.kv')
Builder.load_file('chat_bubble.kv')


class WindowManager(ScreenManager):
    '''A window manager switching between screen.'''

class MessageScreen(Screen):
    '''A screen that display the stories and all message histories'''

class StoryWithImage(MDBoxLayout):
    text= StringProperty()
    source= StringProperty()

class ChatListItem(MDCard):
    friend_avatar = StringProperty()
    mssg = StringProperty()
    timestamp = StringProperty()
    profile = DictProperty()
    isReed = OptionProperty( None , options =['delivery', 'read', 'new','waiting'])
    friend_name= StringProperty()

class ChatScreen(Screen):
    text = StringProperty()
    image = StringProperty()
    active = BooleanProperty()

class ChatBubble(MDBoxLayout):
    msg= StringProperty()
    time = StringProperty()
    sender= StringProperty()
    isRead= OptionProperty('waiting', options= ['read','delivery', 'waiting'])

class Message(MDLabel):
    ''' '''

class MainApp(MDApp):
    def build(self):
        '''Initialize the application
        and return the root widget.'''

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette= 'Teal'
        self.theme_cls_accent_hue = '400'
        self.title =' WhatsApp'

        screens = [
            MessageScreen(name ='message'),
            ChatScreen(name='chat-screen')
        ]

        self.wm = WindowManager(transition =FadeTransition())
        for screen in screens:
            self.wm.add_widget(screen)

        self.story_builder()
        self.chat_list_builder()



        return self.wm


    def story_builder(self):
        for profile in profiles:
            self.story = StoryWithImage()
            self.story.text = profile['name']
            self.story.source= profile['image']
            self.wm.screens[0].ids['story_layout'].add_widget(self.story)

    def chat_list_builder(self):
        for profile in profiles:
            for message in profile['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = profile
                self.chatitem.friend_name = profile ['name']
                self.chatitem.friend_avatar= profile['image']

                lastMessage,time ,isRead ,sender = message.split(';')
                self.chatitem.mssg=lastMessage
                self.chatitem.timestamp= time
                self.chatitem.isRead=isRead
            self.wm.screens[0].ids['chatTimeLine'].add_widget(self.chatitem)

    def change_screen(self, screen):
        self.wm.current = screen

    def create_chat(self,profile):
        self.chat_screen = ChatScreen()
        self.chat_screen.text= profile['name']
        self.chat_screen.image = profile['image']
        self.chat_screen.active = profile['active']
        self.msg_builder(profile , self.chat_screen)
        self.wm.switch_to(self.chat_screen)

    def msg_builder(self, profiles , screen):
        for messages in profiles['msg']:
            if messages != "":
                message , time , isRead, sender = messages.split(";")
                self.chatmsg= ChatBubble()
                self.chatmsg.msg= message
                self.chatmsg.time= time
                self.chatmsg.isRead = isRead
                self.chatmsg.sender= sender
                screen.ids['msglist'].add_widget(self.chatmsg)




if __name__=="__main__":
    MainApp().run()
