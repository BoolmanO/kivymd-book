from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition
from screens import all
from utils import *

from kivy.core.window import Window
Window.size = (300, 600) # ONLY FOR DEV


class BookApp(MDApp, ColorManager, FunctionAnnotationInKv, KvPathUtils):

    window = Window
    like = Like() # usage: app.like.function
    transition = SwapTransition
    transition_duration = 0.4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()
        for screen in all:
            self.sm.add_widget(screen())
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.6
        

    def setup_theme(self) -> None:
        self.theme_cls.theme_style = "Light" # TODO: make in future more themes
        self.theme_cls.primary_palette = "Indigo"
         
         
    def setup_sm(self) -> None:
        self.sm = ScreenManager(transition=self.transition(duration=self.transition_duration))


    def build(self) -> ScreenManager: # kivy requires a build function
        return self.sm
    
    
if __name__ == '__main__':
    builder_load()
    BookApp().run()