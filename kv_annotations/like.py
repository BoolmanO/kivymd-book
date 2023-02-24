from typing import Callable, Type
from .functions import FunctionWrapper


path = Type[str]

string = Type[str]
    
screen_name = Type[str]
        
bool_function = Type[Callable]
        
function = Type[Callable]

wrapped_function = Type[FunctionWrapper] 

wrapped_bool_function = Type[FunctionWrapper]