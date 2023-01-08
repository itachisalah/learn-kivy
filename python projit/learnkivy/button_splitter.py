from kivy.base import runTouchApp
from kivy.lang import Builder

salah = Builder.load_string('''
BoxLayout:
    orientation:'vertical'
    BoxLayout:
        size_hint_y : None
        height: 60
        Label:
            text: 'keep_within_parent?'
        CheckBox:
            id :in_parent_box
            active: False
    
        Label:
            text: 'rescale_within_parent?'
        CheckBox:
            id :rescale_box
            active: False   
    BoxLayout:
        orientation:'horizontal'
        Button:
            text:'left btn'
            size_hint_x: 0.3 
        BoxLayout:
            orientation:'vertical'
            Button:
                text:' btn0'
            BoxLayout:
                Splitter:
                    sizable_from: 'right'
                    keep_within_parent: in_parent_box.active
                    rescale_within_parent: rescale_box.active
                    Button:
                        text: 'btn5'
                Button:
                    text:'btn6'
            BoxLayout:
                sizable_from:'top'
                BoxLayout:
                    orientation:'horizontal'
                    BoxLayout:
                        orientation:'vertical'
                        Button:
                            text:' btn1'
                        Splitter:
                            sizable_from:'top'
                            keep_within_parent: in_parent_box.active
                            rescale_within_parent: rescale_box.active
                            Button:
                                text: 'btn2'
                Splitter:
                    sizable_from:'left'
                    keep_within_parent: in_parent_box.active
                    rescale_within_parent: rescale_box.active
                    Button:
                        text: 'btn3'            
        BoxLayout:
            orientation:'vertical'
            size_hint_x: 0.3
            Button:
                text:'right btn'
            Splitter:
                sizable_from:'bottom'
                keep_within_parent: in_parent_box.active
                rescale_within_parent: rescale_box.active
                Button:
                    text: 'btn7'      
            Button:
                text: 'right btn'                
                        
            
                   






''')


runTouchApp(salah)