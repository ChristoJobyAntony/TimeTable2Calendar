
from enums import Colors
from typing import  List, TYPE_CHECKING

if TYPE_CHECKING :
    from slot import Slot

class Course : 

    def __init__(self, name:str, description='', color:Colors=Colors.green) -> None:
        """
        The course object that acts like a collection for similar slots.
        It allows you to have similar titles and description among various slots, allowing for more concise code. 

        Args:
            name (str): Name/ Summary of Course
            description (str, optional): Optional description to add to all classes. Defaults to ''.
            color (Colors, optional): The color to identify the classes  Defaults to Colors.green.
        """

        self.name = name
        self.description = description
        self.color = color
        self.events : List[Slot]= []


    