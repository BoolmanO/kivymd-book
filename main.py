from kivymd.app import MDApp
from kivy.lang.builder import Builder
#from kivymd.theming import ThemeManager

class HelloWorldApp(MDApp):
    
    def setup_theme(self):
         self.theme_cls.theme_style = "Dark"
         
    def build(self):
        self.setup_theme()
        return Builder.load_file("frontend/main.kv")
    
if __name__ == '__main__':
    HelloWorldApp().run()