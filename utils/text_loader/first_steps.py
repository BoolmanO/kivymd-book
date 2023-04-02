from .core import create_node


first_steps_node = create_node(
    {
    "hello_text": 
"""Здраствуйте, это имплементация учебника %book_name% в виде мобильного приложения.
Глава 1. Правила оформления чертежа по ГОСТ'у.""",

    "start_integration": "text![]"*100

    }
)