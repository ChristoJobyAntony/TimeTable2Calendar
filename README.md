TIMETABLE2CALENDER 
 
An application to automate adding your School/College timetables to your google calendar using  google calendar API.
 
To use this application, you need to create a google cloud platform project and  the authorization credentials for a desktop application and save it in the root directory as "credentials.json"
 
This application is currently configured to my college time-table specifications :
    1. IST Timezone
    2. 2 variants of a course : Theory, Lab
    3. Theory classes : 55 minutes
    4. Practical Classes : 50 minutes
    3. 12 slots (classes) per day
 
Quick Setup 
    Refer to example.py for quick setup
        
 
 
The TimeTable Object : 
    This object holds the setting for the general structure of your time-table and also all the courses and events that have been added.
    It computes your class slots, based on the parameters provided and allows you to easily add slots with slot numbers.
    It is also responsible to connect to google calendars and insert your timetable       
 
The Course Object : 
    The course object acts like a collection for similar slots.
    It allows you to have similar titles and descriptions among various slots, allowing for more concise code. It is linked to the parent time-table since it uses the time-table configurations for creating the event.
 
The event Object : 
    This is just an object to enforce types on the calendar api's event object, to allow for easier handling of events.
 
 
 

