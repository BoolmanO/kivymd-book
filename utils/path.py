from os.path import join
from typing import Type
from glob import glob
from kivy.lang.builder import Builder


FileExtension = Type[str]

def builder_load() -> None: # TODO refactoring
    "loads all files from view, use join for run this code on win and unix"
    for file in glob(join("view","widgets","*.kv")):
        Builder.load_file(file)

    Builder.load_file(join("view", "widgets", "listitem", "listitem.kv"))
    Builder.load_file(join("view", "widgets", "gotocard", "gotocard.kv"))
    Builder.load_file(join("view", "widgets", "imagecontainer", "imagecontainer.kv"))

    for file in glob(join("view","*.kv")):
        Builder.load_file(file)

    for file in glob(join("view", "screens", "lessons", "*.kv")):
        Builder.load_file(file)

    for file in glob(join("view", "screens", "bottom_nav_screens", "*.kv")):
        Builder.load_file(file)


def path_to(*args, ext: FileExtension) -> str:
    return str(join(*args)+ext)