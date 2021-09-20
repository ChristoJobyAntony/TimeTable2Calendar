from typing import Dict, TYPE_CHECKING
from datetime import datetime, time, timedelta, date,timezone, tzinfo
from timeTable import WEEK_DAYS

if TYPE_CHECKING : 
    from course import Course


class Slot:
    def __init__(self, date: date, startTime:time, endTime: time, timeTable: 'TimeTable', course: 'Course') -> None:
        self.eventDate = date
        self.timeTable = timeTable
        self.startTime = startTime
        self.endTime = endTime
        self.course = course
        self._createEvent()

    def _createEvent(self) ->  Dict[str,any]: 
        startDateTime = datetime.combine(self.eventDate, self.startTime, tzinfo=self.timeTable.TZ)
        endDateTime = datetime.combine(self.eventDate, self.endTime, tzinfo=self.timeTable.TZ)
        until = self.timeTable.endDate.strftime('%Y%m%dT%H%M%SZ')
        return {
        'summary': self.course.name,
        'description' : self.course.description,
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

    def __repr__(self):
        weekday = WEEK_DAYS[self.eventDate.weekday()]
        return f"{self.course.name} ({weekday} {self.startTime} - {self.endTime})"




        

        