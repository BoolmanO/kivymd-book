from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition

from py_screens import *
from utils import FileExtension, KvPathUtils, builder_load
from kv_annotations import FunctionAnnotationInKv, Like


from kivy.core.window import Window
Window.size = (300, 600) # ONLY FOR DEV


class temporary_plug:
    def get_active_icon_color(self): return (0.4, 0.4, 0.4, 1)
    def get_inactive_git_color(self): return (0.2, 0.2, 0.2, 1)


class BookApp(MDApp, FunctionAnnotationInKv, KvPathUtils, temporary_plug):

    window = Window
    like = Like() # usage: app.like.function
    transition = SwapTransition
    transition_duration = 0.4

    def change_theme(self, mode: bool): # TODO FIXME: ASAP
        if mode:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def set_transition(self, transition):
        self.sm.transition = transition()
        self.sm.screens[0].ids["nav"].transition = transition
        self.transition = transition

    @property
    def get_transition_class(self):
        return self.sm.transition.__class__
    
    @property
    def get_transition(self):
        return self.sm.transition

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()

        for screen in all_screens:
            self.sm.add_widget(screen())

        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.4
        

    def setup_theme(self) -> None:
        self.theme_cls.theme_style = "Dark" # TODO: make in future more themes
        self.theme_cls.primary_palette = "Indigo"
         
         
    def setup_sm(self) -> None:
        self.sm = ScreenManager(transition=self.transition(duration=self.transition_duration))


    def build(self) -> ScreenManager: # kivy requires a build function
        return self.sm
    
    
if __name__ == '__main__':
    builder_load()
    app = BookApp()
    print(app.sm.screen_names)
    app.run()