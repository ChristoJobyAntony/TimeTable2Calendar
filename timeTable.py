from datetime import date, datetime, timedelta, time, timezone
from googleapiclient.discovery import Resource, build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from typing import Dict, List, Tuple, TYPE_CHECKING
from enums import Days
from slot import Slot
import os

if TYPE_CHECKING : 
    from course import Course



WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
SCOPES = ['https://www.googleapis.com/auth/calendar']


MORNING_START_TIME = time(hour=8)
EVENING_START_TIME = time(hour=14)

THEORY_DELTA = timedelta(minutes=50)
THEORY_BREAK = timedelta(minutes=10)

LAB_DELTA = timedelta(minutes=50)
# Lab break is alternating 0, 10
LAB_BREAK = timedelta(minutes=0), timedelta(minutes=10)
MORNING_SLOTS = 6
EVENING_SLOTS = 6



class TimeTable () :

    def __init__ (self, name:str,  until : datetime, template : Tuple[Tuple[time,time]] = None, **config) :
        """
        This object holds the setting for the general structure of you time-table. 
        You can provide a custom template or configure the  standard time slot generator      
        Args:
            name (str): [description]
            until (datetime): [description]
            template (tuple[tuple[time,time]]): [description]
            **config : use to configure the time zone and the default time slot builder       
        Defult Configuration of Time Slot Generator: 
            TZ_STR = "Asia/Kolkata"
            TZ = timezone(timedelta(hours=5, minutes=30))
            morningStartTime = time(hour=8) #Start before break
            eveningStartTime = time(hour=14) #Start after break
            classDelta = timedelta(minutes=50) The duration of each class
            breakDelta = (timedelta(minutes=5),) The break between classes
            morningSlots = 6
            eveningSlots = 6
        """
        
        self.TZ_STR = "Asia/Kolkata"
        self.TZ = timezone(timedelta(hours=5, minutes=30))
        self.morningStartTime = time(hour=8)
        self.eveningStartTime = time(hour=14)
        self.classDelta = timedelta(minutes=50)
        self.breakDelta = (timedelta(minutes=5), )
        self.morningSlots = 6
        self.eveningSlots = 6

        self.__dict__.update(config)

        self.name = name
        self.endDate = until
        self.events : List['Slot'] = []
        if  not template  : 
            self.timeSlots = self._buildTimeSlots(self.morningSlots, self.morningStartTime, self.classDelta, self.breakDelta) + self._buildTimeSlots(self.eveningSlots, self.eveningStartTime, self.classDelta, self.breakDelta)
            self.SLOTS = self.eveningSlots + self.morningSlots
        else : 
            self.timeSlots = template
            self.SLOTS = len(template)

        
        self.dates = self._computeDates()
        self.service = self._serviceBuilder() 
        
        self.__dict__.update(config)
    
    def _buildTimeSlots (self, slots:int, startTime:time, slotDelta:timedelta, breakDelta:Tuple[timedelta]) -> Tuple[Tuple[time,time]]:
        timeSlots = []
        pointer = startTime
        for i in range(slots+1) : 
            duration = (pointer, self._addToTime(pointer, slotDelta))
            timeSlots.append(duration) 
            pointer = self._addToTime(duration[1], breakDelta[i % len(breakDelta)])

        return tuple(timeSlots)   
    
    def _computeDates (self) -> Tuple[date] :
        pointer = date.today()
        aDay = timedelta(days=1)
        dates = [None for i in range(7)]
        for i in range(7) : 
            dates[pointer.weekday()] = pointer
            pointer += aDay
        return tuple(dates)

    def _authenticate (self) -> Credentials :
        credentials = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
            return credentials
        # If there are no (valid) credentials available, let the user log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(credentials.to_json())
            
            return credentials
    
    def _serviceBuilder (self) -> Resource :
        return build('calendar', 'v3', credentials=self._authenticate())
    
    def _createCalendar (self) -> str :
        calendar = {
            'summary': self.name,
            'timeZone': self.TZ_STR
        }
        created_calendar = self.service.calendars().insert(body=calendar).execute()
        return created_calendar['id']

    def _addToTime (self, t : time, d : timedelta) -> time :
        dt = datetime(100, 1, 1, t.hour, t.minute, t.second) + d
        return dt.time()

    def addToCalendar (self, dry_run=False) -> List[dict] :
        """Adds the registered course to your google calendar 

        Args:
            dry_run (bool, optional): Prints a verbose of all the events to be registered to the console. Defaults to False.

        Returns:
            List[dict]: Returns the google API response
        """
        if dry_run : 
            for event in self.events  :
                print(event.event)
            return []
        
        calendar = self._createcalendar()
        calendar = self._createCalendar()
        events : List[str] = []
        for event in self.events : 
            event = self.service.events().insert(calendarId=calendar, body=event.event).execute()
            events.append(event)
        return events

    def register(self, course_dict:Dict['Days', Dict[int, 'Course']]):
        """Register courses to the time table

        Args:
            course_dict (Dict[Days, Dict[int, Course]]): Pass a dictionary in format {Days : {<slot-id>, <course>} }
        """
        for day, courses in course_dict.items() :
            for slot_id, course in courses.items():
                assert slot_id > 0 and slot_id <= (self.SLOTS)
                if not course  :continue
                slot_id -= 1
                date = self.dates[day.value]
                # Check if block periods : 
                if  courses.get(slot_id+2) == course : 
                    startTime = self.timeSlots[slot_id][0]
                    endTime = self.timeSlots[slot_id + 1][1]
                    courses[slot_id+2] = None
                else : 
                    startTime, endTime = self.timeSlots[slot_id]
                slot = Slot(date, startTime, endTime, self, course)
                course.events.append(slot)
                self.events.append(slot)
    
        


