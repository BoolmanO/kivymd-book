from kivymd.uix.fitimage import FitImage
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivy.uix.scatter import Scatter
from kivymd.uix.button import MDRaisedButton
from kivy.graphics import Color


class ScatterImage(Scatter):
    def __init__(self,  img_obj: Image):
        super().__init__()
        self.size_hint_y = None
        self.size = img_obj.size
        #self.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.do_rotation = False
        #self.do_translation = False
        self.add_widget(img_obj)
        # scale max and scale min TODO:
        

class ZoomingImage(Image):
    dialog = None

    def close_dialog(self, *args):
        print(args)
        if self.dialog:
            self.dialog.dismiss(force=True)

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                size=self.texture_size,
                auto_dismiss=False,
                buttons=[
                    MDRaisedButton(
                        text="Закрыть",
                        on_release=self.close_dialog
                        ),
                    ],
                content_cls=ScatterImage(
                    FitImage(
                            size=(500, 500),#list(map(lambda x: x/1.3, self.size)), 
                            source=self.source, 
                            size_hint_y=None,
                            pos_hint = {"center_x":0.5, "center_y": 0.5}
                        )
                    )
                )

        self.dialog.open()