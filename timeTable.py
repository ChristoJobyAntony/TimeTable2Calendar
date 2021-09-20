from course import Course
from datetime import date, datetime, timedelta, time, timezone
from enums import Days
from googleapiclient.discovery import Resource, build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from typing import Dict, List, Tuple, TYPE_CHECKING
from slot import Slot

import os
<<<<<<< HEAD
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
=======

>>>>>>> Support-For-Custom-TimeTable-Structures


WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
SCOPES = ['https://www.googleapis.com/auth/calendar']

<<<<<<< HEAD
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
=======
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

        
>>>>>>> Support-For-Custom-TimeTable-Structures
        self.dates = self._computeDates()
        self.theorySlots = self._buildTheorySlots()
        self.labSlots = self._buildLabSlots() 
        self.service = self._serviceBuilder()
<<<<<<< HEAD
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
=======
        
    def _buildTimeSlots (self, slots:int, startTime:time, slotDelta:timedelta, breakDelta:Tuple[timedelta]) -> Tuple[Tuple[time,time]]:
        timeSlots = []
        pointer = startTime
        for i in range(slots+1) : 
            duration = (pointer, self._addToTime(pointer, slotDelta))
            timeSlots.append(duration) 
            pointer = self._addToTime(duration[1], breakDelta[i % len(breakDelta)])

        return tuple(timeSlots)   
>>>>>>> Support-For-Custom-TimeTable-Structures
    
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
    
<<<<<<< HEAD
    def _createcalendar (self) -> str :
=======
    def _createCalendar (self) -> str :
>>>>>>> Support-For-Custom-TimeTable-Structures
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
        
<<<<<<< HEAD
        calendar = self._createcalendar()
=======
        calendar = self._createCalendar()
>>>>>>> Support-For-Custom-TimeTable-Structures
        events : List[str] = []
        for event in self.events : 
            event = self.service.events().insert(calendarId=calendar, body=event.event).execute()
            events.append(event)
        return events

    def register(self, course_dict:Dict[Days, Dict[int, Course]]):
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
    
        


