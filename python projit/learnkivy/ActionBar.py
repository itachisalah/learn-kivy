from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top':1}
    ActionView:
        use_separator: True
        ActionPrevious:
            title: 'File'
            with_previous:False
        ActionOverflow:
        ActionButton:
            icon:'atlas://data/images/defaulttheme/audio-volume-high'
        ActionButton:
            important: True
            text:'Edit'
        ActionButton:
            text:'View'
        ActionButton:
            text:'Navigate'
        ActionButton:
            text:'Code'
        ActionGroup:
            text:'Group1'
            ActionButton:
                text:'Window'
            ActionButton:
                text:'VCs'
        ActionGroup:
            text:'Help'
            ActionButton:
                text:'Window1'
            ActionButton:
                text:'VCs2'
            



'''))