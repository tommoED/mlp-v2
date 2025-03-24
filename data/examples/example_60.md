every tues except last week of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=31,weekday=TU(-1))}