every fri 2pm except next week
DTSTART:{ref + reldate( (days=1) if ref.weekday == SA else (weekday=SA))}T140000
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(days=1, weekday=MO) + reldate(weekday=FR)}