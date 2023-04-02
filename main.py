from typing import Callable

from kivymd.app import MDApp, Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SlideTransition, NoTransition, SwapTransition
from kivy.core.window import Window

import kv_annotations
import utils
from py_screens import all_screens
from view import *

#Window.size = (300, 600)


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
    
    transition = SwapTransition
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


    def change_transition_direction_to_left(self):
        """
        Change ScreenManager.transition.direction to left for app.transition_duration + 0.1 seconds.
        """

        """
        It's rather sad that you have to make such a crutch, 
        but the kivy architecture is to blame for this, 
        please use switch_to in your projects
        https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html?highlight=screenmanage#kivy.uix.screenmanager.ScreenManager.switch_to
        """

        self.sm.transition.direction = "right"

        def change(dtime: float):
            self.sm.transition.direction = "left"

        Clock.schedule_once(change, self.transition_duration+0.1)


    def switch_to_main(self, icon):
        self.change_transition_direction_to_left()
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

    def get_icon_color(self):
        return self.theme_cls.primary_color # FIXME


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