from kivy.metrics import sp
from kivymd.uix.menu import MDDropdownMenu

class TransitionBackDrop(MDDropdownMenu):
    items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": sp(56),
                "on_release": lambda x=f"Item {i}": x,
            } for i in range(5)
        ]