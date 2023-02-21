from abc import ABC, abstractmethod
import dark
import light


class BaseHook(ABC):
    @abstractmethod
    def get_active_icon_color(self):
        pass

    @abstractmethod
    def get_inactive_icon_color(self):
        pass


class DarkHook(BaseHook):
    def get_active_icon_color(self):
        return dark.icon_active
    
    def get_inactive_icon_color(self):
        return dark.icon_inactive