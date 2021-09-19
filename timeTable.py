

from _typeshed import Self
from datetime import date, datetime, timedelta, time, timezone
from googleapiclient.discovery import Resource, build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from typing import List, Tuple, TYPE_CHECKING

import os

if TYPE_CHECKING : 
    from slot import Slot


class TimeTable () :

    """
    This object holds the setting for the genreal structure of you time-table and also all the courses and events that have been added.
    It computes your class slots, based on the parameters provided and alows you to easily add slots with slot numbers.
    It is also responsible to connect to google calenders and insert your timetable      
    """ 
    WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def __init__ (self, name:str,  until : datetime, **config) :
        
        # Constants that can be manually edited
        self.TZ_STR = "Asia/Kolkata"
        self.TZ = timezone(timedelta(hours=5, minutes=30))
        self.MORNING_START_TIME = time(hour=8)
        self.EVENING_START_TIME = time(hour=14)
        self.THEORY_DELTA = timedelta(minutes=55)
        self.LAB_DELTA = timedelta(minutes=55)
        self.MORNING_SLOTS = 6
        self.EVENING_SLOTS = 6
        self.SLOTS = self.MORNING_SLOTS + self.EVENING_SLOTS

        self.name = name
        self.endDate = until
        self.events : List['Slot'] = []
        self.theorySlots = self._buildTheorySlots()
        self.labSlots = self._buildLabSlots()
        self.dates = self._computeDates()
        self.service = self._serviceBuilder()
        
        self.__dict__.update(config)

    def _buildTheorySlots (self) -> Tuple[time]:
        theorySlots = []
        pointer = self.MORNING_START_TIME
        for i in range(self.MORNING_SLOTS+1) : 
            theorySlots.append(pointer) 
            pointer = self._addToTime(pointer, self.THEORY_DELTA)
        pointer = self.EVENING_START_TIME
        for i in range(self.EVENING_SLOTS+1) :
            theorySlots.append(pointer)
            pointer = self._addToTime(pointer, self.THEORY_DELTA)
        return tuple(theorySlots)
    
    def _buildLabSlots (self) -> Tuple[time] : 
        labSlots = []
        pointer = self.MORNING_START_TIME
        for i in range(self.MORNING_SLOTS+1) : 
            labSlots.append(pointer) 
            pointer = self._addToTime(pointer, self.LAB_DELTA)

        pointer = self.EVENING_START_TIME
        for i in range(self.EVENING_SLOTS+1) :
            labSlots.append(pointer)
            pointer = self._addToTime(pointer, self.LAB_DELTA)
        return tuple(labSlots)
    
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
    
    def _createCalender (self) -> str :
        calendar = {
            'summary': self.name,
            'timeZone': self.TZ_STR
        }
        created_calendar = self.service.calendars().insert(body=calendar).execute()
        return created_calendar['id']

    def addToClaneder (self, dry_run=False) -> List[str] :
        if dry_run : 
            for event in self.events  :
                print(event.event)
            return []
        
        calender = self._createCalender()
        events : List[str] = []
        for event in self.events : 
            event = self.service.events().insert(calendarId=calender, body=event.event).execute()
            events.append(event)
        return events

    def _addToTime (self, t : time, d : timedelta) -> time :
        dt = datetime(100, 1, 1, t.hour, t.minute, t.second) + d
        return dt.time()
        


