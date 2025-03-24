weekends and wednesdays
DTSTART:{ref + reldate(**(
    {'weekday': WE} if ref.weekday() < WEDNESDAY else
    {'weekday': SA} if ref.weekday() < SATURDAY else
    {'weekday': SU} if ref.weekday() < SUNDAY else
    {'weekday': WE}
))}
RRULE:FREQ=WEEKLY;BYDAY=WE,SA,SU