import math

from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
import json

from libs.componts.circular_item import CircularItem

class HomePage(MDScreen):
    def on_enter(self, ):
        self.list_of_shoes()

    def closest(self, lst, K):
        return lst[min(range(len(lst)), key=lambda  i: abs(lst[i]-K))]

    def list_of_shoes(self):
        ratings = []
        stars = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
        with open('assets/data/images.json') as f_obj:
            data = json.load(f_obj)
            for shoe in data:
                try:
                    if data[shoe]['discount']:
                        self.ids.shoe_cards.add_widget(CircularItem(
                            avatar_card= data[shoe]['avatar_card'],
                            name = data[shoe]['name'],
                            price=f"{ data[shoe]['price']} \N{euro sign}",
                            discount = data[shoe]['discount']

                        ))
                except:
                    self.ids.shoe_cards.add_widget(CircularItem(
                        avatar_card=data[shoe]['avatar_card'],
                        name=data[shoe]['name'],
                        price=f"{data[shoe]['price']} \N{euro sign}",
                        discount="Be happy"
                    ))
                ratings.append(data[shoe]['rating'])

            j = 0
            for circular_item in self.ids.shoe_cards.children:
                rating = ratings[j]
                n_stars= self.closest(stars, float(rating))

                int_n_stars = math.trunc(n_stars)

                for i in range(int_n_stars):

                    circular_item.ids.shoe_star.add_widget(Image(
                        source="assets/images/star.png",
                        size_hint = (None,None),
                        pos_hint={"center_x":0.7, "center_y":0.7},
                        size=(20,20)

                    ))
                if n_stars % 1 !=0:
                    circular_item.ids.shoe_star.add_widget(Image(
                        source="assets/images/half_star.png",
                        size_hint=(None, None),
                        pos_hint={"center_x": 0.7, "center_y": 0.7},
                        size=(20, 20)
                    ))
                circular_item.ids.shoe_star.add_widget(MDLabel(
                    text= f'({rating})',
                    size_hint=(1,0.6),
                    pos_hint={"center_x": 0.7, "center_y": 0.7},
                    font_size=10
                ))
                j +=1
