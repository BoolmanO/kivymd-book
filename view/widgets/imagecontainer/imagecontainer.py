from kivymd.uix.fitimage import FitImage
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout


class ScatterImage(Scatter):
    def __init__(self,  img_obj: Image):
        super().__init__()
        self.size_hint_y = None
        self.size = img_obj.size
        self.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.do_rotation = False
        self.add_widget(img_obj)
        

class ZoomingImage(Image):
    dialog = None
    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Image",
                type="custom",
                content_cls=ScatterImage(
                Image(
                        size=list(map(lambda x: x/2, self.size)), 
                        source=self.source, 
                        size_hint_y=None
                    )
                ),
                buttons=[],
                size=self.texture_size
            )

        self.dialog.open()