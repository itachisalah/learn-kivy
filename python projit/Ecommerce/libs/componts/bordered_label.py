from kivy.uix.label import Label

class BorderedLabel(Label):
    def __init__(self,**kwargs):
        if 'border_color' in kwargs.keys():
            self.border_color= kwargs.pop('border_color')
        if 'border_width' in kwargs.keys():
            self.border_width = kwargs.pop('border_width')
        super(BorderedLabel, self).__init__(**kwargs)