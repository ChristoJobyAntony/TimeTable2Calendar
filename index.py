from datetime import datetime
from timeTable import TimeTable
from course import Course
from datetime import date, time

# Create a timetabe to hold your courses
timeTable =  TimeTable(name='First Semester', until=date(year=2022, month=2, day=1))
# print(timeTable.labSlots)
# print(timeTable.theorySlots)

Course(
    '🧪 Engineering Chemistry : Theory', 
    timeTable, 
    description='BCHY101L Prof.Balamurali M.'
    ).addSlots({'monday' : [1],'friday' : [3]})

Course(
    ' 🧪 Engineering Chemistry : Lab',
    timeTable,
    description='BCHY101P Prof.Buthanapalli Ramakrishnan',
    lab=True
    ).addSlots({'tuesday' : [7, 8]})

Course (
    '💻 Computer Science Programming  : Theory',
    timeTable,
    description='BCSE101E Prof.Rajesh M. '
).addSlots({'wednesday': [4]})

Course (
    '💻 Computer Science Programming : Lab',
    timeTable,
    description='BCSE101E Prof.Rajesh M.',
    lab=True
).addSlots({'wednesday':[9,10], 'friday':[9,10]})

Course(
    '⚡ Basic Electrical Engineering : Theory',
    timeTable,
    description='BEEE101L Prof.Meenakshi J.'
).addSlots({'wednesday':[1], 'friday':[2]})


Course(
    '⚡ Basic Electrical Engineering : Lab',
    timeTable,
    description='BEEE101P Prof.Meenakshi J.',
    lab=True
).addSlots({'monday':[7,8]})

Course(
    '🧮 Calculus : Theory',
    timeTable,
    description='BMAT101L Prof.Srutha Keerthi'
).addSlots({'tuesday':[3], 'thursday':[4]})

Course(
    '🧮 Calculus : Lab',
    timeTable,
    description='BMAT101P Prof.Muhunagai',
    lab=True
).addSlots({'thursday' : [9,10]})

Course(
    '🤹🏿 Qunatitative Skills Practice',
    timeTable,
    description="BSTS101P FACE(APT)"
).addSlots({'monday':[4], 'thursday':[2]})

print(timeTable.addToClaneder(dry_run=False))
