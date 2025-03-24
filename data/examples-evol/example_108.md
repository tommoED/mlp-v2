last workday of every month 10am
DTSTART:{ref + reldate(day=31, weekday=FR(-1)|TH(-1)|TU(-1)|WE(-1)|MO(-1))}T100000
RRULE:FREQ=MONTHLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=-1