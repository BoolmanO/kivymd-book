from typing import Callable

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SlideTransition, NoTransition

import kv_annotations
import utils
from py_screens import *
from view import *

from kivy.core.window import Window
#Window.size = (300, 600)

# TODO fix transitions.
# TODO icons, add light theme support, outlined / filled
class BookApp(MDApp):
    window = Window

    like = kv_annotations.like # usage: app.like.function
    text_manager = utils.text_manager
    metadata = utils.get_metadata()

    formatted_metadata = ""
    for key, value in metadata.items():
        formatted_metadata += f"{key} - {value}\n"

    nav_transition = SlideTransition
    nav_transition_duration = 0.4
    
    transition = SlideTransition
    transition_duration = 0.4


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()

        for screen in all_screens:
            self.sm.add_widget(screen())

        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = False
        self.theme_cls.colors["Light"]["Background"] = "#ebebeb"


    """Micro functions"""
    def path_to(self, *args, ext: utils.FileExtension):
        return utils.path_to(*args, ext=ext)

    def func_wrap(self, func: Callable, *args, **kwargs):
        kv_annotations.func_wrap(func, *args, **kwargs)

    def switch_to_main(self, icon):
        self.sm.current="main_screen"

    def change_theme(app: MDApp, mode: bool):
        if mode:
            app.theme_cls.theme_style = "Dark"
        else:
            app.theme_cls.theme_style = "Light"


    """Functions that determine the behavior of components when changing the theme"""
    def get_active_icon_color(self):
        return "#e1e1fc"
    
    def change_to_outlined(self, MDTab_instance):
        MDTab_instance.icon=MDTab_instance.icon+"-outline"

    def change_to_filled(self, MDTab_instance):
        MDTab_instance.icon=MDTab_instance.icon.split("-")[0]

    """Functions for build"""
    def setup_theme(self) -> None:
        self.theme_cls.theme_style = "Light" # TODO: make in future more themes
        self.theme_cls.primary_palette = "Indigo"
         
    def setup_sm(self) -> None:
        self.sm = ScreenManager(transition=self.transition(duration=self.transition_duration))

    def build(self) -> ScreenManager: # kivy requires a build function
        return self.sm
    
    
if __name__ == '__main__':
    utils.builder_load()
    BookApp().run()