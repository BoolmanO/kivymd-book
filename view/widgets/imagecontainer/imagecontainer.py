from __future__ import annotations
import os

from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp, Clock

from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.uix.scatter import Scatter

from py_screens import BaseScreen


class ZoomingImageScreenAppBar(MDTopAppBar):
    pass


class ScatterImage(Scatter):
    do_rotation=False
    size_hint_y=None
    source=StringProperty()
    

class ZoomingImageScreen(MDScreen):
    def __init__(self, image_obj: ZoomingImage):
        self.image_obj = image_obj
        self.name=f"{image_obj.name}_screen"
        super().__init__()

    def get_img_source(self):
        return self.image_obj.source

    def back_to_root_screen(self, touch):
        self.image_obj.back_to_root_screen()


class ZoomingImage(Image):
    source=StringProperty()
    name=os.path.split(str(source))[1]
    root_screen=None
    image_screen=None
    
    
    def on_touch_down(self, touch):
        if self.image_screen is None:
            """
            This expression corrects the error when the user does not click, 
            but swipes across the screen, lingering on the image, 
            at the moment the on_touch_down method is called, 
            the list of clicks has not yet been formed and we get an IndexError
            """
            try:
                root = touch.grab_list[0].__call__()
            except IndexError: return

            while not isinstance(root, BaseScreen):
                root = root.parent # !WARNING!
            
            self.root_screen=root
            self.image_screen=ZoomingImageScreen(self)
            MDApp.get_running_app().sm.add_widget(self.image_screen)

        MDApp.get_running_app().sm.current=self.image_screen.name


    def back_to_root_screen(self):

        app = MDApp.get_running_app()
        app.sm.transition.direction="right"
        app.sm.current=self.root_screen.name

        def change_direction_to_left(time):
            """
            It's rather sad that you have to make such a crutch, 
            but the kivy architecture is to blame for this, 
            please use switch_to in your projects
            https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html?highlight=screenmanage#kivy.uix.screenmanager.ScreenManager.switch_to
            """
            app.sm.transition.direction = "left"

        Clock.schedule_once(change_direction_to_left, 1)
        #app.sm.transition.direction="left"
        # kivy do transition after executing my code