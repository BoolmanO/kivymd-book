from kivymd.uix.list import BaseListItem, IRightBodyTouch, OneLineRightIconListItem, TwoLineRightIconListItem
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.properties import BooleanProperty

class BaseListItemWithSwitch(BaseListItem):
    pass


class RightSwitchContainer(IRightBodyTouch, MDSwitch):
    pass

class OneLineItemWithSwitch(OneLineRightIconListItem, BaseListItemWithSwitch):
    pass


class TwoLineItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    pass