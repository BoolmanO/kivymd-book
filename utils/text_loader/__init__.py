from .core import TextManager
from .first_steps import first_steps_node


#------------- node load
nodes = {
    "first_steps": first_steps_node
}
#-------------


text_manager = TextManager(nodes)