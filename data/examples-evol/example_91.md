every 5 days from now except last 2 weeks of feb
DTSTART:{ref + reldate(days=5)}
RRULE:FREQ=DAILY;INTERVAL=5;EXDATE:{ref + reldate(month=2, day=28, weekday=TU(-2))}