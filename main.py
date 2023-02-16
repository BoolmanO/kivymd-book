from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from os.path import join
from glob import glob
from screens import *

from kivy.core.window import Window
Window.size = (300, 600) # ONLY FOR DEV


def builder_load() -> None:
    "loads all files from /frontend, use join for run this code on win and unix"
    for file in glob(join("frontend","widgets","*.kv")):
        Builder.load_file(file)

    for file in glob(join("frontend","*.kv")):
        Builder.load_file(file)


class FunctionWrapper:
    '''This class is used to create a "delayed" function,
    during initialization, the function itself and its arguments are passed'''
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def do(self):
        self.func(*self.args, **self.kwargs)


class FunctionAnnotationInKv:
    def func_wrap(self, func, *args, **kwargs):
        return FunctionWrapper(func, *args, **kwargs)

    def function(self, *args, **kwargs):
        pass


class ColorManager:
    def change_theme(self, mode: bool):
        if mode:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


class BookApp(MDApp, ColorManager, FunctionAnnotationInKv):

    window = Window

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.6
        

    def setup_theme(self) -> None:
        self.theme_cls.theme_style = "Dark" # TODO: make in future more themes
        self.theme_cls.primary_palette = "Indigo"
         
         
    def setup_sm(self) -> None:
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen()) # see names in screens.screens
         

    def build(self) -> ScreenManager: # kivy requires a build function
        return self.sm
    
if __name__ == '__main__':
    builder_load()
    BookApp().run()