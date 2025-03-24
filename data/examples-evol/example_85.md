every 20 minutes from 3 to 4pm
DTSTART:{ref + reldate(hour=15)}T150000
RRULE:FREQ=MINUTELY;INTERVAL=20;UNTIL:{ref + reldate(hour=16)}

every 15 minutes from 9 to 10am
DTSTART:{ref + reldate(hour=9)}T090000
RRULE:FREQ=MINUTELY;INTERVAL=15;UNTIL:{ref + reldate(hour=10)}

every 30 minutes from 1 to 3pm
DTSTART:{ref + reldate(hour=13)}T130000
RRULE:FREQ=MINUTELY;INTERVAL=30;UNTIL:{ref + reldate(hour=15)}

every 10 minutes from 5 to 6pm
DTSTART:{ref + reldate(hour=17)}T170000
RRULE:FREQ=MINUTELY;INTERVAL=10;UNTIL:{ref + reldate(hour=18)}

every 45 minutes from 8 to 10am
DTSTART:{ref + reldate(hour=8)}T080000
RRULE:FREQ=MINUTELY;INTERVAL=45;UNTIL:{ref + reldate(hour=10)}

every 5 minutes from 2 to 2:30pm
DTSTART:{ref + reldate(hour=14)}T140000
RRULE:FREQ=MINUTELY;INTERVAL=5;UNTIL:{ref + reldate(hour=14, minute=30)}

every 25 minutes from 11am to 12pm
DTSTART:{ref + reldate(hour=11)}T110000
RRULE:FREQ=MINUTELY;INTERVAL=25;UNTIL:{ref + reldate(hour=12)}

every 40 minutes from 6 to 8pm
DTSTART:{ref + reldate(hour=18)}T180000
RRULE:FREQ=MINUTELY;INTERVAL=40;UNTIL:{ref + reldate(hour=20)}

every 12 minutes from 4 to 5pm
DTSTART:{ref + reldate(hour=16)}T160000
RRULE:FREQ=MINUTELY;INTERVAL=12;UNTIL:{ref + reldate(hour=17)}

every 60 minutes from 9am to 5pm
DTSTART:{ref + reldate(hour=9)}T090000
RRULE:FREQ=MINUTELY;INTERVAL=60;UNTIL:{ref + reldate(hour=17)}

every hr from 10am to 5pm
DTSTART:{ref + reldate(hour=10)}T100000
RRULE:FREQ=HOURLY;INTERVAL=1;UNTIL:{ref + reldate(hour=17)}


