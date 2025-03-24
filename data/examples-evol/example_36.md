next weekday
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}

on weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR


every weekday
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR

on weekends
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
)}
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

every weekend
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
)}
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

next weekend
DTSTART:{ref + reldate(weeks=1, weekday=SA(0))}
DTEND:{ref + reldate(weeks=1, weekday=SU(0))}









