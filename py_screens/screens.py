from kivymd.uix.screen import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import (SwapTransition, CardTransition, 
                    FadeTransition, WipeTransition, SlideTransition)
    
from kivymd.app import MDApp
from kivy.metrics import sp
from typing import Optional

class BaseScreen(Screen):
    name: Optional[str] = None # follow snake_case
    
    def __init__(self, *args, **kwargs):
        assert self.name != None, "Not implemented name" # FIXME: Production-build
        assert isinstance(self.name, str), "Name requires string" # FIXME: Production-build
        super().__init__(*args, **kwargs)
        

class FirstSteps(BaseScreen):
    name = "first_steps"

class MainScreen(BaseScreen):
    name = "main_screen"

class SettingsScreen(BaseScreen):
    name = "settings_screen"
    transitions = (SwapTransition, CardTransition, 
                    FadeTransition, WipeTransition, SlideTransition)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ self.transtion_backdrop_caller = self.ids["transition_backdrop"]
        self.transition_backdrop_menu = MDDropdownMenu(items=self.transition_backdrop_items,
                                                       caller=self.transition_backdrop_caller) """
    

    def open_transition_backdrop(self):
        self.transition_backdrop_caller = self.ids["transition_backdrop"]
        self.transition_backdrop_items = []
        self.transition_backdrop_items = \
                [
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Swap",
                        "on_release": self.change_to_swap,
                        "height": sp(56),
                    },
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Card",
                        "on_release": self.change_to_card,
                        "height": sp(56),
                    },
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Fade",
                        "on_release": self.change_to_fade,
                        "height": sp(56),
                    },
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Wipe",
                        "on_release": self.change_to_wipe,
                        "height": sp(56),
                    },
                    {
                        "viewclass": "OneLineListItem",
                        "text": "Slide",
                        "on_release": self.change_to_slide,
                        "height": sp(56),
                    },
                ]
        self.transition_backdrop_menu = MDDropdownMenu(items=self.transition_backdrop_items,
                                                       caller=self.transition_backdrop_caller,
                                                       width_mult=6,
                                                       elevation=0,
                                                       position="center",
                                                       #radius=[16, 16, 16, 16],
                                                       opening_time=0.4,
                                                       border_margin=sp(8),
                                                       max_height=sp(228)) # TODO
        self.transition_backdrop_menu.open()

    def change_to_swap(self):
        self.select_transition(SwapTransition)

    def change_to_card(self):
        self.select_transition(CardTransition)

    def change_to_fade(self):
        self.select_transition(FadeTransition)

    def change_to_wipe(self):
        self.select_transition(WipeTransition)
    
    def change_to_slide(self):
        self.select_transition(SlideTransition)

    def select_transition(self, transition):
        MDApp.get_running_app().set_transition(transition)
        self.transition_backdrop_caller.text = transition.__name__
        self.transition_backdrop_menu.dismiss()

all_screens = (MainScreen, SettingsScreen, FirstSteps,)