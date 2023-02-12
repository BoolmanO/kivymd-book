from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from os.path import join
from glob import glob
from screens import MainScreen
from frontend.widgets.widgets_py import *

from kivy.core.window import Window # ONLY FOR DEV
Window.size = (300, 600)

def builder_load():
    "loads all files from /frontend, use join for run this code on win and unix"
    for file in glob(join("frontend","widgets","*.kv")):
        Builder.load_file(file)
    for file in glob(join("frontend","*.kv")):
        Builder.load_file(file)

class BookApp(MDApp):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()
        
    def setup_theme(self):
        self.theme_cls.theme_style = "Dark" # TODO: make in future more themes
        self.theme_cls.primary_palette = "Indigo"
         
    def setup_sm(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen()) # see names in screens.screens
         
    def build(self): # kivy requires a build function
        return self.sm
    
if __name__ == '__main__':
    builder_load()
    BookApp().run()