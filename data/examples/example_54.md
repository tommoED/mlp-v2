thursdays, mondays and saturdays
DTSTART:{ref + reldate(**(
    {'weekday': TH} if ref.weekday() < THURSDAY else
    {'weekday': SA} if ref.weekday() < SATURDAY else
    {'weekday': MO}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TH,SA