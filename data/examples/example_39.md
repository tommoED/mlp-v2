hourly from 9am to 5pm weekdays
DTSTART:{ref + reldate( (days=1) if ref.weekday == SA else (weekday=SA))}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={range(9, 17)}