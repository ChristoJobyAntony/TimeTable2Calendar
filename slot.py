from typing import Dict, TYPE_CHECKING
from datetime import datetime, time, timedelta, date,timezone, tzinfo

if TYPE_CHECKING : 
    from course import Course


class Slot:
    def __init__(self, date: date, startTime:time, endTime: time, timeTable: 'TimeTable') -> None:
        self.eventDate = date
        self.timeTable = timeTable
        self.startTime = startTime
        self.endTime = endTime
        self.course = None

    def register_course(self, course: 'Course'):
        self.course = course
        self.event = self._createEvent()
        self.timeTable.events.append(self)

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
        name = self.course.name if self.course else 'Empty'
        return f"{self.course.name} ({self.eventDate.weekday()} {self.startTime} - {self.endTime})"




        

        