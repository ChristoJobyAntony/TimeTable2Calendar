from datetime import datetime
from enums import Colors, Days
from timeTable import TimeTable
from course import Course
from datetime import date


# Create a timetabe to hold your course and porvied the date unite the events reccur
timeTable =  TimeTable(name='First Semester', until=date(year=2022, month=2, day=1))

'''
Course(
    '<Course Name>', 
    timeTable, # refer to the original timetable class
    description='BCHY101L Prof.Balamurali M.', #Add a description to all the classes in this course
    color=Colors.yellow #Select a tag color to recognize this course
).addSlots({Days.Monday : [1,4]) #Pass a dicitionary in the mannrer { Dat : [ <slot-no  starting from 1>]}

'''


Course(
    '🧪 Engineering Chemistry : Theory', 
    timeTable, 
    description='BCHY101L Prof.Balamurali M.',
    color=Colors.yellow
).addSlots({Days.Monday : [1], Days.Friday : [3]})

Course(
    ' 🧪 Engineering Chemistry : Lab',
    timeTable,
    description='BCHY101P Prof.Buthanapalli Ramakrishnan',
    lab=True,
    color=Colors.yellow
).addSlots({Days.Tuesday : [7, 8]})

Course (
    '💻 Computer Science Programming  : Theory',
    timeTable,
    description='BCSE101E Prof.Rajesh M. ',
    color=Colors.turquoise
).addSlots({Days.Wednesday: [4]})

Course (
    '💻 Computer Science Programming : Lab',
    timeTable,
    description='BCSE101E Prof.Rajesh M.',
    lab=True,
    color=Colors.turquoise
).addSlots({Days.Wednesday:[9,10], Days.Friday:[9,10]})

Course(
    '⚡ Basic Electrical Engineering : Theory',
    timeTable,
    description='BEEE101L Prof.Meenakshi J.',
    color=Colors.blue
).addSlots({Days.Wednesday:[1], Days.Friday:[2]})

Course(
    '⚡ Basic Electrical Engineering : Lab',
    timeTable,
    description='BEEE101P Prof.Meenakshi J.',
    lab=True,
    color=Colors.blue
).addSlots({Days.Monday:[7,8]})

Course(
    '🧮 Calculus : Theory',
    timeTable,
    description='BMAT101L Prof.Srutha Keerthi',
    color=Colors.red
).addSlots({Days.Tuesday:[3], Days.Thursday:[4]})

Course(
    '🧮 Calculus : Lab',
    timeTable,
    description='BMAT101P Prof.Muhunagai',
    lab=True,
    color=Colors.red
).addSlots({Days.Thursday : [9,10]})

Course(
    '🤹🏿 Qunatitative Skills Practice',
    timeTable,
    description="BSTS101P FACE(APT)",
    lab=True,
    color=Colors.purple
).addSlots({Days.Monday:[4], Days.Thursday:[2]})

print(timeTable.addToClaneder(dry_run=False))
