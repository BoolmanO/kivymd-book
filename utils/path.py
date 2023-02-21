from os.path import join
from typing import Iterable, Type
from glob import glob
from kivy.lang.builder import Builder


FileExtension = Type[str]

def builder_load() -> None:
    "loads all files from view, use join for run this code on win and unix"
    for file in glob(join("view","widgets","*.kv")):
        Builder.load_file(file)

    for file in glob(join("view","*.kv")):
        Builder.load_file(file)

    for file in glob(join("view", "screens", "lessons", "*.kv")):
        Builder.load_file(file)

    for file in glob(join("view", "screens", "bottom_nav_screens", "*.kv")):
        Builder.load_file(file)


class PathObj:
    def __init__(self, path: Iterable):
        self.path=join(*path)
    
    def ext(self, ext: FileExtension) -> str:
        return str(self.path+ext)


class KvPathUtils:
    def path_to(self, *args) -> PathObj:
        return PathObj(args)