from sys import platform, version_info
from os import name, getcwd
from typing import Any
from kivymd._version import __version__
from kivy.config import version


def get_metadata() -> dict[str, Any]:
    "fetch metadata of process"
    return {
        "platform": platform,
        "python": f"{version_info[0]}.{version_info[1]}.{version_info[2]}",
        "osname": name,
        "directory": getcwd(),
        "kivy_version": version,
        "kivymd_version": __version__
    }
