from kivy.base import runTouchApp
from kivy.lang import Builder

KV='''
PageLayout:
    BoxLayout:
        canvas:
            Color:
                rgba: 216/255, 195/255,88/255, 1
            Rectangle:
                size:self.size
        orientation:'vertical'
        Label:
            size_hint_y:None
            height: 1.5*self.texture_size[1]
            text:'page1'
            
        Button:
            text:'test'
            on_press:print('test')
    
    BoxLayout:
        canvas:
            Color:
                rgba: 199/255, 8/255,50/255, 1
            Rectangle:
                pos:self.pos
                size:self.size
        
        Label:

            text:'page2'
        AsyncImage:
            source:'http://kivy.org/logos/kivy-logo-black-64.png'
            
    GridLayout:
        canvas:
            Color:
                rgba: 35/255, 38/255,30/255, 1
            Rectangle:
                pos:self.pos
                size:self.size
        cols:2
        Label:

            text:'page3'
        AsyncImage:
            source:'http://kivy.org/slides/kivyandroid-thumb.jpg' 
        Button:
            text:'test'
        AsyncImage:
            source:'http://kivy.org/slides/kivypictures-thumb.jpg'
            
        Widget
        AsyncImage:
            source:'http://kivy.org/slides/particlepanda-thumb.jpg'
                      
            

'''


if __name__=='__main__':
    runTouchApp(Builder.load_string(KV))