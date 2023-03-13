from __future__ import annotations

import os

from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.properties import StringProperty

from py_screens import BaseScreen


class ZoomingImageScreen(MDScreen):
    def __init__(self, image_obj: ZoomingImage):
        super().__init__()
        self.image_obj = image_obj
        self.name=f"{image_obj.name}_screen"

    def back_to_root_screen(self, touch):
        self.image_obj.back_to_root_screen()


class ZoomingImageScreenAppBar(MDTopAppBar):
    pass

class ZoomingImage(Image):
    source=StringProperty()
    name=os.path.split(str(source))[1]
    root_screen=None
    image_screen=None
    
    def on_touch_down(self, touch):
        if self.image_screen is None:
            root = touch.grab_list[0].__call__()
            if root is None:
                pass # DO MDialog

            while not isinstance(root, BaseScreen):
                root = root.parent # !WARNING!
            
            self.root_screen=root
            self.image_screen=ZoomingImageScreen(self)
            MDApp.get_running_app().sm.add_widget(self.image_screen)

        MDApp.get_running_app().sm.current=self.image_screen.name

    def back_to_root_screen(self):
        MDApp.get_running_app().sm.current=self.root_screen.name