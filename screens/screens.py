from kivymd.uix.screen import Screen
from typing import Optional

class BaseScreen(Screen):
    "Thats like ABC class, but I don't want to load an extra module into the app"
    name: Optional[str] = None # follow snake_case
    
    def __init__(self, *args, **kwargs):
        assert self.name != None, "Not implemented name"
        assert isinstance(self.name, str), "Name requires string"
        super().__init__(*args, **kwargs)
        

class FirstSteps(BaseScreen):
    name = "first_steps"

class MainScreen(BaseScreen):
    name = "main_screen"

all = (MainScreen, FirstSteps,)