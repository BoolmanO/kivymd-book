from .functions import func_wrap
from . import like

"""
Don't do this in your projects, it's a very bad decision. 
This module is a product of my laziness regarding reading the documentation.

I implemented the idea of ​​callback functions with arguments with a separate class, 
instead use the standard functools library and the partial function (functools.partial).
https://docs.python.org/3/library/functools.html#functools.partial

Instead of pseudo annotations, I recommend you use properties from kivy.properties.
https://kivy.org/doc/stable/api-kivy.properties.html
"""