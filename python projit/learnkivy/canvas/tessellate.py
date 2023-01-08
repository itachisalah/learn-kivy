from kivy.app import App
from kivy.graphics import Mesh ,Color
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.graphics.tesselator import Tesselator, WINDING_ODD, TYPE_POLYGONS
from kivy.logger import Logger

Builder.load_string('''
<ShipBuilder>:
    BoxLayout:
        size_hint_y: None
        height: 48
        spacing: 2
        padding: 2
        
        ToggleButton:
            text: "debug"
            id: debug
            on_release: root.build()
        
        Button:
            text:'new shape'
            on_release:root.push_shape()
        Button:
            text:'Build'
            on_release:root.build()
        Button:
            text:'rest'
            on_release:root.rest()
    BoxLayout:
        size_hint_y:None
        height:48
        top: root.top
        spacing : 2
        padding:2    
        Label:
            id :status
            text:'Status'
 
''')

class ShipBuilder(FloatLayout):
    def __init__(self, **kwargs):
        super(ShipBuilder, self).__init__(**kwargs)
        self.shapes=[
            [100,100,300,100,300,300,100,300],
            [150,150,250,150,250,250,150,250]
        ]
        self.shape=[]
        self.build()
    def on_touch_down(self, touch):
        if super(ShipBuilder, self).on_touch_down(touch):
            return True
        Logger.info('tesselate: on_touch_down(%5.2f, %5.2f)'%touch.pos)
        self.shape.extend(touch.pos)
        self.build()
        return True

    def on_touch_move(self, touch):
        if super(ShipBuilder, self).on_touch_move(touch):
            return True
        Logger.info('tesselate: on_touch_move(%5.2f, %5.2f)' % touch.pos)
        self.shape.extend(touch.pos)
        self.build()
        return True

    def on_touch_up(self, touch):
        if super(ShipBuilder, self).on_touch_up(touch):
            return True
        Logger.info('tesselate: on_touch_up(%5.2f, %5.2f)' % touch.pos)
        self.push_shape()
        self.build()


    def push_shape(self):
        self.shapes.append(self.shape)
        self.shape=[]



    def build(self):
        tess= Tesselator()
        count =0
        for shape in self.shapes:
            if len(shape) >=3:
                tess.add_contour(shape)
                count += 1
        if self.shape and len(self.shape) >=3:
            tess.add_contour(self.shape)
            count +=1
        if not count:
            return
        ret = tess.tesselate(WINDING_ODD, TYPE_POLYGONS)
        Logger.info('tesselate:build: tess.tesselate retures{}'.format(ret))
        self.canvas.after.clear()

        debug= self.ids.debug.state == "down"
        if debug:
            with self.canvas.after:
                c =0
                for vertices, indices in tess.meshes:
                    Color(c, 1,1, mode="hsv")
                    c += 0.3
                    indices= [0]
                    for i in range(1, len(vertices) //4):
                        if i >0:
                            indices.append(i)
                        indices.append(i)
                        indices.append(0)
                        indices.append(i)
                    indices.pop(-1)
                    Mesh(vertices=vertices,indices=indices,mode="lines")
        else:
            with self.canvas.after:
                Color(1,1,1,1)
                for vertices , indices in tess.meshes:
                    Mesh(vertices=vertices,indices=indices,mode="triangle_fan")
        self.ids.status.text= "Shapes:{} - Vertex:{} - Elements: {}".format(
            count, tess.vertex_count, tess.element_count
        )
    def rest(self):
        self.shapes=[]
        self.shape=[]
        self.ids.status.text="Shapes:{} - Vertex:{} - Elements: {}".format(
            0,0,0)
        self.canvas.after.clear()





class TessApp(App):
    def build(self):
        return ShipBuilder()

if __name__=='__main__':
    TessApp().run()