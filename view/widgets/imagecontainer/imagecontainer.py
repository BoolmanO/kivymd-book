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
    scale_max = 7.5
    scale_min = 0.75
    

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
    name=source
    root_screen=None
    image_screen=None

    def on_touch_down(self, touch):
        """Open new screen with image on click"""

        # I LITERALLY FORKED THIS CODE FROM kivymd.uix.button.button.py BaseButton on_touch_down (i mean if-elif tree)
        # Explanation of this code for beginners: when you click on the widget, 
        # the on_touch_down event literally fires for all instances of the class
        if touch.is_mouse_scrolling:
            return False
        elif not self.collide_point(touch.x, touch.y):
            return False
        elif self in touch.ud:
            return False
        elif self.disabled:
            return False

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
        app.sm.current=self.root_screen.name
        app.change_transition_direction_to_left()