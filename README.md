## TIMETABLE2CALENDER 
 
***A python program to automate adding your School/College timetables to your google calendar using  google calendar API.***


To use this application, you need to create a google cloud platform project and  the authorization credentials for a desktop application and save under the root directory as "credentials.json"
 

 
###Quick Setup 
    Refer to example.py for quick setup
        
 
 
### The TimeTable Object : 
This object holds the setting for the general structure of your time-table and also all the courses and events that have been added.
It computes your class slots, based on the configurations or you can provide your custom template for the time slots.
It is also responsible to connect to google calendars and insert your timetable
The default time-table configuration : 
```
{
TZ_STR = "Asia/Kolkata"
TZ = timezone(timedelta(hours=5, minutes=30))
'morningStartTime' = time(hour=8) #Start before break
'eveningStartTime' = time(hour=14) #Start after break
'classDelta' = timedelta(minutes=50) The duration of each class
'breakDelta' = (timedelta(minutes=5),) The break between classes
'morningSlots' = 6
'eveningSlots' = 6
}
```

- Defualt time-table construction : 
 ```
 theoryTimeTable =  TimeTable(name='First Semester - Theory ', until=date(2022,2, 1) )
 ```
- Custom configured time-table construction : 
```
theoryTimeTable =  TimeTable(name='First Semester - Theory ', until=date(2022,2, 1), **{"morningStartTime":time(10, 00)})
```
- Cutsom Template time-table construction : 
```
template = (
    (time(8,00), time(8,50)),
    (time(8,50), time(9,40)),
    (time(9,50), time(10,40)),
    (time(10,40), time(11,30)),
    (time(11,40), time(12,30)),
    (time(12,30), time(13,20)),
    (time(14,00), time(14,50)),
)
# Initiate the TimeTable class with the template parameter 
labTimeTable = TimeTable('First Semester : Lab', date(2022, 2, 1), template)
```
 
### The Course Object
The course object acts like a collection for similar slots.It allows you to have similar titles and descriptions among various slots, allowing for more concise code. 

A Standard course object creation : 
```
BMAT101L = Course(
    '🧮  Muggle Studies',
    description='Prof. Charity Burbage',
    color=Colors.red
)
```

### The event Object
This is just an object to enforce types on the calendar api's event object, to allow for easier handling.
 
 
 

