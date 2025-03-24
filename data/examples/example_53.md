weekdays minus thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR