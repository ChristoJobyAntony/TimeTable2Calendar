from datetime import datetime, time, timedelta, date,timezone, tzinfo
from typing import Dict, List, TYPE_CHECKING
from slot import Slot
if TYPE_CHECKING : 
    from timeTable import TimeTable

class Course : 
    
    def __init__(self, name:str, timeTable:'TimeTable', description='', lab=False) -> None:
        self.name = name
        self.description = description
        self.lab = lab
        self.timeTable = timeTable
        self.slots : List[Slot]= []

    def getSlots(self) -> List[Slot]: 
        return self.slots

    def addSlot(self, weekDay:str, slot:int) -> None :
        assert weekDay.lower() in self.timeTable.WEEK_DAYS
        weekDayInt = self.timeTable.WEEK_DAYS.index(weekDay.lower())
        date = self.timeTable.dates[weekDayInt]
        
        assert slot > 0 and slot < (self.timeTable.MORNING_SLOTS + self.timeTable.EVENING_SLOTS)
        if slot < self.timeTable.MORNING_SLOTS : slot -= 1
        startTime = (self.timeTable.theorySlots[slot]) if not self.lab else self.timeTable.labSlots[slot]
        endTime = self.timeTable.theorySlots[slot+1] if not self.lab else self.timeTable.labSlots[slot+1]
        slot = Slot(date, startTime, endTime, self.timeTable, self)
        self.slots.append(slot)
        self.timeTable.events.append(slot)

    def addSlots(self, dictSlots:Dict[str, List[int]]) :
        for day, slots in dictSlots.items():
            for slot in slots :
                self.addSlot(day, slot)
        
    