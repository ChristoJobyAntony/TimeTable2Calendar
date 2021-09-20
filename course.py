from datetime import datetime, time, timedelta, date,timezone, tzinfo
from enums import Colors, Days
from typing import Dict, List, TYPE_CHECKING
from slot import Slot
if TYPE_CHECKING : 
    from timeTable import TimeTable

class Course : 
    """
    The course object that acts like a collection for similar slots.
    It allows you to have simialr titles and description among various slots, allowing for more concise code. 
    It inhertis the parent time-table configurations for creating an event
    """
        
    def __init__(self, name:str, timeTable:'TimeTable', description='', lab=False, color:Colors=Colors.green) -> None:
        """
        Args:
            name (str): Name/ Summary of Course
            timeTable (TimeTable): parent TimeTable to inherit
            description (str, optional): Optional desription to add to all classes. Defaults to ''.
            lab (bool, optional): Is this course a lab or theory ?. Defaults to Theory.
            color (Colors, optional): The color to identify the classes  Defaults to Colors.green.
        """
        self.name = name
        self.description = description
        self.lab = lab
        self.timeTable = timeTable
        self.color = color
        self.slots : List[Slot]= []

    def addSlot(self, weekDay:Days, slot:int) -> None :
        date = self.timeTable.dates[weekDay.value]
        
        assert slot > 0 and slot < (self.timeTable.SLOTS)
        if slot < self.timeTable.MORNING_SLOTS : slot -= 1
        startTime = (self.timeTable.timeSlots[slot]) if not self.lab else self.timeTable.labSlots[slot]
        endTime = self.timeTable.timeSlots[slot+1] if not self.lab else self.timeTable.labSlots[slot+1]
        slot = Slot(date, startTime, endTime, self.timeTable, self)
        self.slots.append(slot)
        self.timeTable.events.append(slot)

    def addSlots(self, dictSlots:Dict[Days, List[int]]) :
        """
        Add the slots at which this class is being conducted

        Args:
            dictSlots (Dict[Days, List[int]]): Pass the key as the day and the value as the slot number
        
        Example : 
            timeTable =  TimeTable(name='First Semester', until=date(year=2022, month=2, day=1))
            course = Course('🧪 Engineering Chemistry : Theory', timeTable)
            courses.addSlots( { Days.Monday : [1, 3], Days.Friday : [3] } )
        """
        for day, slots in dictSlots.items():
            for slot in slots :
                self.addSlot(day, slot)
        
    