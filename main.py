from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition

from py_screens import *
import utils
import kv_annotations
from utils.path import FileExtension
from utils.text_loader import text_manager


from kivy.core.window import Window
#Window.size = (300, 600) # ONLY FOR DEVvv


class temporary_plug:
    def get_active_icon_color(self): return (0.4, 0.4, 0.4, 1)
    def get_inactive_icon_color(self): return (0.2, 0.2, 0.2, 1)
    def switch_to_main(self, icon):
        self.sm.current="main_screen"


class BookApp(MDApp, temporary_plug):

    window = Window
    path_to = utils.path_to
    text_manager = text_manager
    like = kv_annotations.like # usage: app.like.function
    func_wrap = kv_annotations.func_wrap

    transition = SwapTransition # TODO create memory package # TODO Check kivymd transitions
    transition_duration = 0.4

    def path_to(self, *args, ext: FileExtension):
        return utils.path_to(*args, ext=ext)

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
    

    def change_theme(app: MDApp, mode: bool):
        if mode:
            app.theme_cls.theme_style = "Dark"
        else:
            app.theme_cls.theme_style = "Light"

    def change_theme_animation(app: MDApp, mode: bool):
        if mode:
            app.theme_cls.theme_style_switch_animation = True
        else:
            app.theme_cls.theme_style_switch_animation = False
            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()

        for screen in all_screens:
            self.sm.add_widget(screen())

        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = False
        self.theme_cls.theme_style_switch_animation_duration = 0.4
        

    def setup_theme(self) -> None:
        self.theme_cls.theme_style = "Dark" # TODO: make in future more themes
        self.theme_cls.primary_palette = "Indigo"
         
         
    def setup_sm(self) -> None:
        self.sm = ScreenManager(transition=self.transition(duration=self.transition_duration))


    def build(self) -> ScreenManager: # kivy requires a build function
        return self.sm
    
    
if __name__ == '__main__':
    utils.builder_load()
    app = BookApp()
    print(app.sm.screen_names)
    app.run()
