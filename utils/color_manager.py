class ColorManager:
    def change_theme(self, mode: bool):
        if mode:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"