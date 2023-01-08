from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from math import sin,cos,pi
from kivy.core.window import Window

KV='''
BoxLayout:
    Widget:
        canvas:
            Color:
                rgba:1,1,1,1
            Mesh: 
                vertices: app.mesh_points
                indices: range(len(app.mesh_points))
                texture:app.mesh_texture
                mode :'tringle_fan'
    BoxLayout:
        orientation:'vertical'
        size_hint_x: None
        width:100
        Slider:
            value: app.offset_x       
            on_value: app.offset_x = args[1]
            min: -1
            max:1 
        Slider:
            value: app.offset_y      
            on_value: app.offset_y = args[1]
            min: -1
            max:1 
        Slider:
            value: app.radius       
            on_value: app.radius = args[1]
            min: -1
            max:1 
        Slider:
            value: app.radius       
            on_value: app.radius = args[1]
            min: 10
            max:1000
        Slider:
            value: app.sin_wobble      
            on_value: app.sin_wobble = args[1]
            min: -50
            max:50
        Slider:
            value: app.sin_wobble_speed      
            on_value: app.sin_wobble_speed = args[1]
            min: 0
            max:50
            step:1


'''


class MeshBallApp(App):
    mesh_points= ListProperty([])
    mesh_texture= ObjectProperty(None)
    offset_x= NumericProperty(0.5)
    offset_y = NumericProperty(0.5)
    radius = NumericProperty(900)
    sin_wobble_speed= NumericProperty(0)
    sin_wobble= NumericProperty(0)

    def build(self):
        self.mesh_texture= CoreImage('xman.jpg').texture
        Clock.schedule_interval(self.update_points, 0)

        return Builder.load_string(KV)
    def update_points(self, *args):
        points= [Window.width /2, Window.height /2, 0.5,0.5]
        i =0
        while i < 2 *pi :
            i += 0.01 *pi
            points.extend([
                Window.width/2 +cos(i) * (self.radius+self.sin_wobble *
                                          sin(i*self.sin_wobble_speed)),
                Window.height / 2 + sin(i) * (self.radius + self.sin_wobble *
                                             sin(i * self.sin_wobble_speed)),

                self.offset_x +sin(i),
                self.offset_y + cos(i)


            ])
        self.mesh_points=points

if __name__=='__main__':
    MeshBallApp().run()