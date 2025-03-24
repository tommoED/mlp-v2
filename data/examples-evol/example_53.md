weekdays minus thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

weekdays except monday
DTSTART:{ref + reldate(weekday=TU|WE|TH|FR)}
RRULE:FREQ=WEEKLY;BYDAY=TU,WE,TH,FR

every monday and friday
DTSTART:{ref + reldate(**(
    {'weekday': MO} if ref.weekday() < WEDNESDAY else
    {'weekday': FR}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,FR

weekdays excluding thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

mon tue wed fri
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

every weekday but thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

all weekdays except thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

on mondays to fridays skipping thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

weekdays without thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

every mon-wed and fri
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

every day except thursday and weekends
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

monday tuesday wednesday and friday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

work days minus thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

business days except thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

weekdays omitting thursday
DTSTART:{ref + reldate(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR
