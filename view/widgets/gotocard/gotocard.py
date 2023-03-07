from kivymd.uix.list import BaseListItem, TwoLineRightIconListItem
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class GoToLessonCard2(TwoLineRightIconListItem, MDCard):
    go_to = StringProperty() # screen name