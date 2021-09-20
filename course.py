from datetime import datetime, time, timedelta, date,timezone, tzinfo
from typing import Dict, List, TYPE_CHECKING
from slot import Slot

from timeTable import TimeTable, MORNING_SLOTS

class Course : 
    def __init__(self, name:str, description='', lab=False) -> None:
        self.name = name
        self.description = description
        self.lab = lab
        self.slots : List[Slot]= []

    def getSlots(self) -> List[Slot]: 
        return self.slots

    def addSlot(self, timeTable: TimeTable, weekDayInt: int, slot_id: int) -> None :
        slot_list = timeTable.labSlots if self.lab else timeTable.theorySlots
        start_time, end_time = slot_list[slot_id - 1]

        slot = Slot(timeTable.dates[weekDayInt], start_time, end_time, timeTable, self)
        self.slots.append(slot)
        timeTable.events.append(slot)

    def addSlots(self, timeTable: TimeTable, dictSlots:Dict[str, List[int]]) :
        for day, slots in dictSlots.items():
            for slot in slots :
                self.addSlot(timeTable, day, slot)
        
    