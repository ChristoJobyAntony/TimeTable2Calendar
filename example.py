from datetime import time
from enums import Colors, Days
from timeTable import TimeTable
from course import Course
from datetime import date

"""
This File will only run when under the root direcotry of this project
"""


"""
A Generic Example of timetable creation without custom templates the time table.
The default configurations of the time table class is used to genreate the time slots.
"""
# Create a timetable to hold your course and provide the date unite the events reccur
theoryTimeTable =  TimeTable(name='First Semester - Theory ', until=date(2022,2, 1), **{"MORNING_START_TIME":time(10, 00)})

'''
A Course object defines the common properties among the all the classes of your course
'''
BCHY101L = Course(
    '🧪 Engineering Chemistry : Theory',  
    description='BCHY101L Prof.Balamurali M.',
    color=Colors.yellow
)

BCSE101E = Course (
    '💻 Computer Science Programming  : Theory',
    description='BCSE101E Prof.Rajesh M. ',
    color=Colors.turquoise
)

BEEE101L = Course(
    '⚡ Basic Electrical Engineering : Theory',
    description='BEEE101L Prof.Meenakshi J.',
    color=Colors.blue
)

BMAT101L = Course(
    '🧮 Calculus : Theory',
    description='BMAT101L Prof.Srutha Keerthi',
    color=Colors.red
)

"""
Register the courses according to the format { WeekDay : {<Slot-No> : <Course-Names>} }
"""
theoryTimeTable.register({
    Days.Monday : {1:BCHY101L},
    Days.Tuesday : {3:BMAT101L},
    Days.Wednesday : {1:BEEE101L, 2:BCHY101L, 4:BCSE101E},
    Days.Thursday : {4:BMAT101L},
    Days.Friday : {1:BMAT101L, 2:BEEE101L, 3:BCHY101L}

})

"""
Now we add the registered courses to your google calender !
"""
theoryTimeTable.addToCalendar(dry_run=False)

#################################################################

"""
A Example of timetable creation with custom templates the time table.
"""
template = (
    (time(8,00), time(8,50)),
    (time(8,50), time(9,40)),
    (time(9,50), time(10,40)),
    (time(10,40), time(11,30)),
    (time(11,40), time(12,30)),
    (time(12,30), time(13,20)),
    (time(14,00), time(14,50)),
    (time(14,50), time(15,40)),
    (time(15,50), time(16,40)),
    (time(16,40), time(17,30)),
    (time(17,40), time(18,30)),
    (time(18,30), time(19,20)),
)
# Initiate the TimeTable class with the template parameter 
labTimeTable = TimeTable('First Semester : Lab', date(2022, 2, 1), template)


BCHY101P = Course(
    ' 🧪 Engineering Chemistry : Lab',
    description='BCHY101P Prof.Buthanapalli Ramakrishnan',
    color=Colors.yellow
)

BCSE101E = Course (
    '💻 Computer Science Programming : Lab',
    description='BCSE101E Prof.Rajesh M.',
    color=Colors.turquoise
)

BEEE101P = Course(
    '⚡ Basic Electrical Engineering : Lab',
    description=' Prof.Meenakshi J.',
    color=Colors.blue
)

BMAT101P = Course(
    '🧮 Calculus : Lab',
    description='BMAT101P Prof.Muhunagai',
    color=Colors.red
)

BSTS101P =Course(
    '🤹🏿 Quantitative Skills Practice',
    description="BSTS101P FACE(APT)",
    color=Colors.purple
)


labTimeTable.register({
    Days.Monday : {4:BSTS101P, 7:BEEE101P, 8:BEEE101P},
    Days.Tuesday : {1:BSTS101P, 7:BSTS101P, 8:BSTS101P},
    Days.Wednesday : {9 : BCSE101E, 10: BCSE101E},
    Days.Thursday : {2: BSTS101P, 9:BMAT101P},
    Days.Friday : {9: BCSE101E, 10:BCSE101E}
})

labTimeTable.addToCalendar(dry_run=False)