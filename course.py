from datetime import datetime, time, timedelta, date,timezone, tzinfo
from typing import Dict, List, TYPE_CHECKING
from slot import Slot

from timeTable import TimeTable, MORNING_SLOTS, EVENING_SLOTS, WEEK_DAYS

class Course : 
    
    def __init__(self, name:str, timeTable:'TimeTable', description='', lab=False) -> None:
        self.name = name
        self.description = description
        self.lab = lab
        self.timeTable = timeTable
        self.slots : List[Slot]= []

    def getSlots(self) -> List[Slot]: 
        return self.slots

    def addSlot(self, weekDay: str, slot_id: int) -> None :
        assert weekDay.lower() in WEEK_DAYS
        weekDayInt = WEEK_DAYS.index(weekDay.lower())
        
        assert slot_id > 0 and slot_id <= (MORNING_SLOTS + EVENING_SLOTS)
        if slot_id < MORNING_SLOTS:
            slot_id -= 1

        slot_list = self.timeTable.labSlots if self.lab else self.timeTable.theorySlots
        slot = slot_list[weekDayInt][slot_id]
        slot.register_course(self)
        self.slots.append(slot)

    def addSlots(self, dictSlots:Dict[str, List[int]]) :
        for day, slots in dictSlots.items():
            for slot in slots :
                self.addSlot(day, slot)
        
    