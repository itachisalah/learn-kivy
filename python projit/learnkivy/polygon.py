from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.lang import Builder
from kivy.properties import ListProperty

Builder.load_string('''
<Triangle>:
    p1: 0,0
    p2:self.width, 0
    p3 : self.width/2, self.height
    
    canvas:
        Color:
            rgb:0,1,0
        Triangle:
            points: self.p1 +self.p2 +self.p3

''')

def point_inside_polygon(x ,y , poly):
    n = len(poly)
    inside = False
    p1x = poly[0]
    p1y = poly[1]
    for i in range(0, n+ 2 ,2):
        p2x= poly[i % n]
        p2y = poly[(i +1) % n]
        if y > min(p1y , p2y):
            if y <= max(p1y , p2y):
                if x <= max(p1x , p2x):
                    if p1y != p2y:
                        xinters= (y - p1y)* (p2x - p1x) / (p2y - p1y) +p1x
                    if p1x == p2x or x<= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside




class Triangle(Scatter):
    p1 = ListProperty([0,0])
    p2 = ListProperty([0,0])
    p3 = ListProperty([0, 0])

    def collide_point(self, x, y):
        x , y = self.to_local(x ,y)
        return point_inside_polygon(x ,y, self.p1+self.p2+self.p3)

class TriangleApp(App):
    def build(self):
        return Triangle(size_hint=(None,None))

TriangleApp().run()