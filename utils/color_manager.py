class ColorManager:
    def change_theme(self, mode: bool):
        if mode:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def get_icon_color(self):
        raise NotImplementedError()

    def get_inactive_icon_color(self):
        if self.theme_cls.theme_style == "Light":
            return (0.8, 0.8, 0.8, 1)
        return (0.2, 0.2, 0.2, 1)

    def get_active_icon_color(self):
        if self.theme_cls.theme_style == "Dark":
            return (0.4, 0.4, 0.4, 1)
        return (0.2, 0.2, 0.2, 1)