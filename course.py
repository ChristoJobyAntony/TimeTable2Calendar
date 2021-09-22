from datetime import datetime, time, timedelta, date,timezone, tzinfo
from typing import Dict, List, TYPE_CHECKING, Tuple
from enums import Colors, Days, Reminder
from slot import Slot

if TYPE_CHECKING : 
    from timeTable import TimeTable


class Course : 
            
    def __init__(self, name:str, **config) -> None:
        """
        The course object that acts like a collection for similar slots.
        It allows you to have similar titles and description among various slots, allowing for more concise code. 

        Args:
            name (str): Name/ Summary of Course
            description (str, optional): Optional description to add to all classes. Defaults to ''.
            color (Colors, optional): The color to identify the classes  Defaults to Colors.green.
        """        
        self.name = name
        self._buildSelf(config)

    def _buildSelf(self, config:dict) :
        self.description = config.get('description')
        self.color = config.get('color')
        self.events = config.get('events', []) 
        reminders = config.get('reminders')
        self.reminders = (reminders,) if reminders and type(reminders[0]) != tuple else  reminders
        
    def inherit(self, timeTable : 'TimeTable') : 
        config = {}
        for k, v in self.__dict__.items() :
            if k == None and timeTable.defaultCourseConfig.get(v): 
                config[k] = timeTable.defaultCourseConfig.get(v)
            else : 
                config[k] = self.__dict__.get(k)
        self._buildSelf(config)




    