weekdays 2-4pm
DTSTART:{ref + reldate( (days=1) if ref.weekday == SA else (weekday=SA))}T140000
DTEND:{ref + reldate( (days=1) if ref.weekday == SA else (weekday=SA))}T160000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR