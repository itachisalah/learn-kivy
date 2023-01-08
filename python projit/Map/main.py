import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.clock import Clock
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

from kivymd.uix.button import MDFillRoundFlatIconButton


KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import MapView,MapSource kivy_garden.mapview



<ExtendedButton>
    elevation: 3
    -height: "56dp"


<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    unfocus_color: "#fffcf4"


MDScreen:

    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"



                    MDBoxLayout:

                        MDNavigationRail:
                            id: navigation_rail
                            md_bg_color: "#fffcf4"
                            selected_color_background: "#e7e4c0"
                            ripple_color_item: "#e7e4c0"
                            on_item_release: app.switch_screen(*args)

                            MDNavigationRailMenuButton:
                                on_release: nav_drawer.set_state("open")

                            MDNavigationRailItem:
                                #md_bg_color: "#b0f0d6"
                                text: "Distance"
                                icon: "map-marker-distance"


                            MDNavigationRailItem:
                                text: "Itinaire"
                                icon: "open-source-initiative"

                            MDNavigationRailItem:
                                text: "Position"
                                icon: "google-maps"

                            MDNavigationRailItem:
                                text: "Trafic"
                                icon: "bus-marker"

                            MDNavigationRailItem:
                                text: "Coffee"
                                icon: "coffee"
                            MDNavigationRailItem:
                                text: "Direction"
                                icon: "directions-fork"
                            MDNavigationRailItem:
                                text: "Human"
                                icon: "human-male-female"
                            MDNavigationRailItem:
                                text: "Proximité"
                                icon: "map-marker-radius"


                        ScreenManager:
                            id: screen_manager
                            Screen:
                                name: "screen2"
                                BoxLayout:
                                    MapView:
                                        lat:25.530551
                                        lon:42.796291
                                        zoom:14
                                        
                                        
                                        MapMarkerPopup:
                                            source:"images/marker.png"
                                            lat: 25.530551
                                            lon: 42.796291
                                            popup_size: 400,320
                                            
                                        MapMarkerPopup:
                                            source:"images/marker.png"
                                            lat: 19.559795
                                            lon: 46.842077
                                            popup_size: 400,320
                                        
                                        MapMarkerPopup:
                                            source:"images/marker.png"
                                            lat: 33.328695
                                            lon: -8.038293
                                            popup_size: 400,320
                                      


    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        md_bg_color: "#fffcf4"
        elevation: 12
        width: "240dp"

        MDNavigationDrawerMenu:

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "12dp"
                padding: 0, 0, 0, "12dp"

                MDIconButton:
                    icon: "menu"

                ExtendedButton:
                    text: "Compose"
                    icon: "pencil"

            DrawerClickableItem:
                text: "Python"
                icon: "language-python"

            DrawerClickableItem:
                text: "JavaScript"
                icon: "language-javascript"

            DrawerClickableItem:
                text: "Java"
                icon: "language-java"

            DrawerClickableItem:
                text: "Swift"
                icon: "language-swift"
'''


class ExtendedButton(
    RoundedRectangularElevationBehavior, MDFillRoundFlatIconButton
):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4


class Example(MDApp):
    def build(self):
        self.title = "Maps country"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_screen(
            self, instance_navigation_rail, instance_navigation_rail_item
    ):
        '''
        dddd.
        '''




Example().run()