from datetime import datetime, time, timedelta, date,timezone, tzinfo
from typing import Dict, List, TYPE_CHECKING, Tuple
from enums import Colors, Days, Reminder
from slot import Slot

if TYPE_CHECKING : 
    from timeTable import TimeTable


class Course : 
            
    def __init__(self, name:str, description=None, color:'Colors'=None, reminders:Tuple[Tuple[Reminder, time]]=None, **config) -> None:
        """
        The course object that acts like a collection for similar slots.
        It allows you to have similar titles and description among various slots, allowing for more concise code. 

        Args:
            name (str): Name/ Summary of Course
            description (str, optional): Optional description to add to all classes. Defaults to ''.
            color (Colors, optional): The color to identify the classes  Defaults to Colors.green.
        """
        self.__dict__.update(config)
        
        self.name = name
        self.description = description
        self.color = color
        self.events = []
        self.reminders = (reminders,) if reminders and type(reminders[0]) != tuple else  reminders

        


    