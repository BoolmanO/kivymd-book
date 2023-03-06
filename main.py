from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition, NoTransition

from py_screens import *
import utils
import kv_annotations
from utils.path import FileExtension
from utils.text_loader import text_manager


from kivy.core.window import Window
#Window.size = (300, 600) # ONLY FOR DEVvv


class BookApp(MDApp):

    window = Window

    path_to = utils.path_to
    func_wrap = kv_annotations.func_wrap

    text_manager = text_manager
    like = kv_annotations.like # usage: app.like.function

    metadata = utils.get_metadata()
    formatted_metadata = ""
    for key, value in metadata.items():
        formatted_metadata += f"{key} - {value}\n"

    no_transition = NoTransition
    transition = NoTransition
    transition_duration = 0.4

    def path_to(self, *args, ext: FileExtension):
        return utils.path_to(*args, ext=ext)

    def switch_to_main(self, icon):
        self.sm.current="main_screen"

    def change_theme(app: MDApp, mode: bool):
        if mode:
            app.theme_cls.theme_style = "Dark"
        else:
            app.theme_cls.theme_style = "Light"
            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()

        for screen in all_screens:
            self.sm.add_widget(screen())

        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = False
        self.theme_cls.colors["Light"]["Background"] = "#ebebeb"

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
    #print(app.sm.screen_names)
    app.run()