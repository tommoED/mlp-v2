daily 8am
DTSTART:{ref + reldate(hour=8)}
RRULE:FREQ=DAILY

every 2 days for 10d
DTSTART:{ref + reldate(days=2)}
RRULE:FREQ=DAILY;INTERVAL=2;UNTIL:{ref + reldate(days=10)}

weekly on monday for 10weeks
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;UNTIL:{ref + reldate(weeks=10)}

every 3 days for 15d
DTSTART:{ref + reldate(days=3)}
RRULE:FREQ=DAILY;INTERVAL=3;UNTIL:{ref + reldate(days=15)}
