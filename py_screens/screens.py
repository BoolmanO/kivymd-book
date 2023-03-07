from kivymd.uix.screen import Screen
from typing import Optional


class BaseScreen(Screen):
    name: Optional[str] = None # follow snake_case
        

class FirstSteps(BaseScreen):
    name = "first_steps"

class MainScreen(BaseScreen):
    name = "main_screen"

class LessonMenu(BaseScreen):
    name = "lesson_menu"

class SettingsScreen(BaseScreen):
    name = "settings_screen"

all_screens = (MainScreen, SettingsScreen, LessonMenu, FirstSteps,)