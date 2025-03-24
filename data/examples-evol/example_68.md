last sunday of every month
DTSTART:{ref + reldate(day = 31, weekday=SU(-1))}
RRULE:FREQ=MONTHLY;BYDAY=-1SU

last monday of each month
DTSTART:{ref + reldate(day = 31, weekday=MO(-1))}
RRULE:FREQ=MONTHLY;BYDAY=-1MO

final tuesday of the month
DTSTART:{ref + reldate(day = 31, weekday=TU(-1))}
RRULE:FREQ=MONTHLY;BYDAY=-1TU

last thursday monthly
DTSTART:{ref + reldate(day = 31, weekday=TH(-1))}
RRULE:FREQ=MONTHLY;BYDAY=-1TH

last fri of every month 3pm
DTSTART:{ref + reldate(day = 31, weekday=FR(-1))}T150000
RRULE:FREQ=MONTHLY;BYDAY=-1FR

last saturday monthly 10:30am
DTSTART:{ref + reldate(day = 31, weekday=SA(-1))}T103000
RRULE:FREQ=MONTHLY;BYDAY=-1SA

last sun each month 2-4pm
DTSTART:{ref + reldate(day = 31, weekday=SU(-1))}T140000
DTEND:{ref + reldate(day = 31, weekday=SU(-1))}T160000
RRULE:FREQ=MONTHLY;BYDAY=-1SU

last monday monthly 0900
DTSTART:{ref + reldate(day = 31, weekday=MO(-1))}T090000
RRULE:FREQ=MONTHLY;BYDAY=-1MO

last wednesday monthly 5:45pm
DTSTART:{ref + reldate(day = 31, weekday=WE(-1))}T174500
RRULE:FREQ=MONTHLY;BYDAY=-1WE

last thu of each month 8am
DTSTART:{ref + reldate(day = 31, weekday=TH(-1))}T080000
RRULE:FREQ=MONTHLY;BYDAY=-1TH

last friday monthly 11-12
DTSTART:{ref + reldate(day = 31, weekday=FR(-1))}T110000
DTEND:{ref + reldate(day = 31, weekday=FR(-1))}T120000
RRULE:FREQ=MONTHLY;BYDAY=-1FR

last sunday monthly for 1h30m
DTSTART:{ref + reldate(day = 31, weekday=SU(-1))}T100000
DURATION:PT1H30M
RRULE:FREQ=MONTHLY;BYDAY=-1SU