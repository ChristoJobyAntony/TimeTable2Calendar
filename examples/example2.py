from timeTable import TimeTable
from course import Course
from datetime import date, time

# Create a timetabe to hold your courses
timeTable =  TimeTable(name='First Semester', until=date(year=2022, month=2, day=1))


# Add your courses here
BCHY101L = Course(
    '🧪 Engineering Chemistry - Theory', 
    description='[BCHY101L] Prof. Veera Venkata Ramesh E'
)

BCHY101P = Course(
    ' 🧪 Engineering Chemistry - Lab',
    description='[BCHY101P] Prof. Veera Venkata Ramesh E',
    lab=True
)

BCSE101E = Course (
    '💻 Computer Programming - Theory',
    description='[BCSE101E] Prof. Tamizharasi T'
)

BCSE101EP = Course (
    '💻 Computer Programming - Lab',
    description='[BCSE101E] Prof. Tamizharasi T',
    lab=True
)

BEEE101L = Course(
    '⚡ Basic Electrical Engineering - Theory',
    description='[BEEE101L] Prof. Tapan Prakash'
)

BEEE101P = Course(
    '⚡ Basic Electrical Engineering - Lab',
    description='[BEEE101P] Prof. Tapan Prakash',
    lab=True
)

BMAT101L = Course(
    '🧮 Calculus - Theory',
    description='[BMAT101L] Prof. Karthika K'
)

BMAT101P = Course(
    '🧮 Calculus - Lab',
    description='[BMAT101P] Prof. Karthika K',
    lab=True
)

BSTS101P = Course(
    '🤹🏿 Quantitative Skills Practice',
    description="[BSTS101P] SMART (APT)",
    lab=True
)


# Register your slots here
timeTable.register('monday', {
    1: BEEE101L,
    4: BMAT101L,
    11: BSTS101P
})

timeTable.register('tuesday', {
    1: BMAT101L,
    3: BCHY101L,
    8: BSTS101P,
    9: BMAT101P,
    10: BMAT101P
})

timeTable.register('wednesday', {
    2: BEEE101L,
    7: BCSE101EP,
    8: BCSE101EP,
    9: BCHY101P,
    10: BCHY101P
})

timeTable.register('thursday', {
    2: BMAT101L,
    4: BCHY101L,
    7: BEEE101P,
    8: BEEE101P,
    9: BSTS101P
})

timeTable.register('friday', {
    1: BCHY101L,
    5: BCSE101E,
    11: BCSE101EP,
    12: BCSE101EP
})

#print(timeTable.events)
print(timeTable.addToCalendar(dry_run=False))
