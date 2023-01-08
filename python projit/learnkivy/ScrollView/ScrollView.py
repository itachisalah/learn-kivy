from kivy.app import App
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
Window.size=350,600

class ScrollViewApp(App):
    def build(self):
        layout= GridLayout(cols=1 , padding=10, spacing=10,
                           size_hint=(None,None),width=300)
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(50):
            btn = Button(text=str(i),size=(280,40),size_hint=(None,None))

            layout.add_widget(btn)

        root = ScrollView(size_hint=(None,None),size=(300,520),
                          pos_hint={'center_x':0.5,'center_y':0.5},
                          do_scroll_x= True)
        root.add_widget(layout)
        return root


ScrollViewApp().run()