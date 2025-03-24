every tues unless 1st week of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=1,weekday=TU(1))}