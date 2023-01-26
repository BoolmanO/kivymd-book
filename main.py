from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from os.path import join
from glob import glob
from screens import MainScreen

def builder_load():
    # loads all files from /frontend, use join for run this code on win and unix
    for file in glob(join("frontend","*.kv")):
        Builder.load_file(file)

class BookApp(MDApp):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # MDApp create self.theme_cls in __init__
        self.setup_theme() # If swapped it won't work
        self.setup_sm()
        
    def setup_theme(self):
        self.theme_cls.theme_style = "Dark"
         
    def setup_sm(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
         
    def build(self): # kivy requires a build function
        return self.sm
    
if __name__ == '__main__':
    builder_load()
    BookApp().run()