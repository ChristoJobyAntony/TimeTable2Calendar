from typing import Dict, TYPE_CHECKING
from timeTable import TimeTable
from datetime import datetime, time, date

if TYPE_CHECKING : 
    from course import Course

class Slot : 
    """
    This is a simple python class wrapper for the the google events dictionary,
    """
    def __init__(self, date:date, startTime:time, endTime: time, timeTable:TimeTable, course:'Course') -> None:
        """
        Args:
            date (date): Date for class event
            startTime (time)
            endTime (time)
            timeTable (TimeTable) : Parent TimeTable to inherit
            course (Course): Parent Course to inherit
        """
        self.eventDate = date
        self.timeTable = timeTable
        self.course = course
        self.startTime = startTime
        self.endTime = endTime
        self.event = self._createEvent()

    def _createEvent(self) ->  Dict[str,any]: 
        startDateTime = datetime.combine(self.eventDate, self.startTime, tzinfo=self.timeTable.TZ)
        endDateTime = datetime.combine(self.eventDate, self.endTime, tzinfo=self.timeTable.TZ)
        until = self.timeTable.endDate.strftime('%Y%m%dT%H%M%SZ')
        event =  {
            'summary': self.course.name,
            'description' : self.course.description,
            'colorId' : self.course.color.value,  
            'start': {
                'dateTime': startDateTime.isoformat(),
                'timeZone': self.timeTable.TZ_STR
            },
            'end': {
                'dateTime': endDateTime.isoformat(),
                'timeZone': self.timeTable.TZ_STR
            },
            'recurrence': [
                'RRULE:FREQ=WEEKLY;UNTIL='+until,
            ],
        }
        return event





        

        