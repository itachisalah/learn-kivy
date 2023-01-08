import json

from kivy.app import App
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.graphics import Mesh
from kivy.uix.widget import Widget
from kivy.graphics.instructions import RenderContext
import math
from random import random
from kivy.base import EventLoop

def load_atlas(atlas_name):
    with open(atlas_name, 'rb') as f:
        atlas = json.load(f.read().decode('utf-8'))
        tex_name,



class Particle:
    x= 0
    y= 0
    size = 1

    def __init__(self, parent, i):
        self.parent =parent
        self.vsize= parent.vsize
        self.reset(creted = True)

    def reset(self,creted = True):
        raise NotImplementedError()

    def advance(self):
        raise NotImplementedError()

    def update(self):
        for i in range(self.base_i,
                       self.base_i + 4 * self.vsize,
                       self.vsize):
            self.parent.vertices[i:i + 3]= (
                self.x , self.y , self.size
            )


class PSWidget(Widget):
    indices = []
    vertices= []
    particles = []

    def __init__(self, **kwargs):
        Widget.__init__(self,**kwargs)
        self.canvas = RenderContext(use_parent_projection= True)
        self.canvas.shader.source= self.glsl

        self.vfmt = (
            (b'vCenter',    2, 'float'),
            (b'vScale', 1, 'float'),
            (b'vPosition', 2, 'float'),
            (b'vTexCoords0', 2, 'float'),
        )
        self.vsize= sum(attr[1] for attr in self.vfmt)

        self.texture,self.uvmap = load_atlas(self.atlas)
        self.indices= []
        for i in range(0, 4 * NSTARS, 4 ):
            self.indices.extend((
                i,i+1,i+2,i+2,i+3,i
            ))

        self.vertices =[]
        for i in range(NSTARS):
            self.vertices.extend((
                0,0,1,-24,-24,0,1,
                0,0,1,24,-24,1,1,
                0,0,1,24,24,1,0,
                0,0,1,-24,24,0,0,
            ))

        self.texture= Image('star.png').texture
        self.stars = [Star(self, i) for i in range (NSTARS)]

    def update_glsl(self,nap):
        x0 , y0 = self.center
        max_distance = 1.1 * max(x0, y0)

        for star in self.stars:
            star.distance *= 2 * nap +1
            star.size += 0.25 *nap

            if (star.distance > max_distance):
                star.reset()
            else:
                star.update(x0, y0)
        self.canvas.clear()

        with self.canvas:
            Mesh(fmt=self.vfmt, mode='triangles',
                 indices = self.indices,
                 vertices= self.vertices,
                 texture = self.texture)

class StarApp(App):
    def build(self):
        EventLoop.ensure_window()
        return Starfield()

    def on_start(self):
        Clock.schedule_interval(self.root.update_glsl, 60 ** -1)

if __name__=='__main__':
    StarApp().run()