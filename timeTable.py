

from _typeshed import Self
from datetime import date, datetime, timedelta, time, timezone
from googleapiclient.discovery import Resource, build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from typing import List, Tuple, TYPE_CHECKING

import os
<<<<<<< HEAD

if TYPE_CHECKING : 
    from slot import Slot


class TimeTable () :

    """
    This object holds the setting for the genreal structure of you time-table and also all the courses and events that have been added.
    It computes your class slots, based on the parameters provided and alows you to easily add slots with slot numbers.
    It is also responsible to connect to google calendars and insert your timetable      
    """ 
    WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
=======


WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

MORNING_START_TIME = time(hour=8)
EVENING_START_TIME = time(hour=14)

THEORY_DELTA = timedelta(minutes=50)
THEORY_BREAK = timedelta(minutes=10)

LAB_DELTA = timedelta(minutes=50)
# Lab break is alternating 0, 10
LAB_BREAK = timedelta(minutes=0), timedelta(minutes=10)
MORNING_SLOTS = 6
EVENING_SLOTS = 6


class TimeTable: 
>>>>>>> 3f846bb48fd90dd31dc6a15cb50b8e0a8c32fb9f
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__ (self, name:str,  until : datetime, template :tuple[tuple[time, time]]= None, **config) :
        
        # Constants that can be manually edited
        """
        Set the timezone for all the times and date provided !
        """
        self.TZ_STR = "Asia/Kolkata"
        self.TZ = timezone(timedelta(hours=5, minutes=30))
<<<<<<< HEAD

        """
        Configs for auto-generating a time table with regular durations and a single break
        """
        self.MORNING_START_TIME = time(hour=8)
        self.EVENING_START_TIME = time(hour=14)
        self.CLASS_DELTA = timedelta(minutes=55)
        self.MORNING_SLOTS = 6
        self.EVENING_SLOTS = 6

        self.SLOTS = self.MORNING_SLOTS + self.EVENING_SLOTS

        self.name = name
        self.endDate = until
        self.events : List['Slot'] = []
        # Compute the time-table slots if none are provided 
        if not template : 
            self.timeSlots = self._buildSlots(self.MORNING_SLOTS, self.MORNING_START_TIME, self.CLASS_DELTA) + self._buildSlots(self.EVENING_SLOTS, self.EVENING_START_TIME, self.CLASS_DELTA)
        else : 
            self.timeSlots = template
            self.SLOTS = len(template)

=======

        self.name = name
        self.endDate = until
        self.events: List['Slot'] = []
>>>>>>> 3f846bb48fd90dd31dc6a15cb50b8e0a8c32fb9f
        self.dates = self._computeDates()
        self.theorySlots = self._buildTheorySlots()
        self.labSlots = self._buildLabSlots() 
        self.service = self._serviceBuilder()
<<<<<<< HEAD

    
        
        self.__dict__.update(config)

    def _buildSlots (self, slots, start : time, duration : timedelta) -> Tuple[Tuple[time,time]]:
        theorySlots = []
        pointer = start
        for i in range(slots+1) : 
            duration = (pointer, self._addToTime(pointer, self.CLASS_DELTA))
            theorySlots.append(duration) 
            pointer = duration[0]
        
        return tuple(theorySlots)

=======

    def _build_slots(self, total_slots: int, start_time: time, slot_time: timedelta, break_times):
        slots = []
        if not isinstance(break_times, (list, tuple)):
            break_times = (break_times,)

        for i in range(total_slots):
            end_time = self._addToTime(start_time, slot_time)
            slots.append((start_time, end_time))
            start_time = self._addToTime(end_time, break_times[i % len(break_times)])
        return slots

    def _buildTheorySlots(self):
        slots = self._build_slots(MORNING_SLOTS, MORNING_START_TIME, THEORY_DELTA, THEORY_BREAK)
        slots += self._build_slots(EVENING_SLOTS, EVENING_START_TIME, THEORY_DELTA, THEORY_BREAK)
        return slots
    
    def _buildLabSlots(self) : 
        slots = self._build_slots(MORNING_SLOTS, MORNING_START_TIME, LAB_DELTA, LAB_BREAK)
        slots += self._build_slots(EVENING_SLOTS, EVENING_START_TIME, LAB_DELTA, LAB_BREAK)
        return slots
    
>>>>>>> 3f846bb48fd90dd31dc6a15cb50b8e0a8c32fb9f
    def _computeDates (self) -> Tuple[date] :
        pointer = date.today()
        aDay = timedelta(days=1)
        dates = [None for i in range(7)]
        for i in range(7) : 
            dates[pointer.weekday()] = pointer
            pointer += aDay
        return tuple(dates)

    def _authenticate (self) -> Credentials :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
            return creds
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
            
            return creds
    
    def _serviceBuilder (self) -> Resource :
        return build('calendar', 'v3', credentials=self._authenticate())
    
    def _createcalendar (self) -> str :
        calendar = {
            'summary': self.name,
            'timeZone': self.TZ_STR
        }
        created_calendar = self.service.calendars().insert(body=calendar).execute()
        return created_calendar['id']

    def addToCalendar (self, dry_run=False) -> List[str] :
        if dry_run : 
            for event in self.events  :
                print(event.event)
            return []
        
        calendar = self._createcalendar()
        events : List[str] = []
        for event in self.events : 
            event = self.service.events().insert(calendarId=calendar, body=event.event).execute()
            events.append(event)
        return events

    def register(self, weekday, course_dict):
        assert weekday.lower() in WEEK_DAYS
        weekDayInt = WEEK_DAYS.index(weekday.lower())

        for slot_id, course in course_dict.items():
            assert slot_id > 0 and slot_id <= (MORNING_SLOTS + EVENING_SLOTS)
            course.addSlot(self, weekDayInt, slot_id)

    def _addToTime (self, t: time, d: timedelta) -> time :
        dt = datetime(100, 1, 1, t.hour, t.minute, t.second) + d
        return dt.time()
        


