every tues and every other mon
DTSTART:{ref + reldate(**(
    {'weekday': TU} if ref.weekday() < TUESDAY else
    {'weekday': MO} if ref.weekday() < MONDAY else
    {'weekday': TU}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO;INTERVAL=2;BYDAY=TU;