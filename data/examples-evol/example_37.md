wknds 2-4pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T140000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T160000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

wknds 9-11am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T090000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T110000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

wknds 5-7pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T170000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T190000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

wknds 10am-12pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T100000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T120000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

wknds 3-5pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T150000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T170000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 8-10am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T080000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T100000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 6-8pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T180000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T200000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 11am-1pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T110000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T130000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 4-6pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T160000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T180000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 7-9am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T070000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T090000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 1-3pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T130000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T150000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 7-9pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T190000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T210000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 12-2pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T120000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T140000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

on weekends 5-7am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T050000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T070000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 8-10pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T200000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T220000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 6-8am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T060000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T080000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 9-11pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T210000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T230000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 10am-12:30pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T100000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T123000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 1:30-3:30pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T133000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T153000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 4:30-6:30pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T163000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T183000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 7:30-9:30am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T073000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T093000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 11:30am-1:30pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T113000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T133000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 2:30-4:30pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T143000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T163000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 5:30-7:30pm
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T173000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T193000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 8:30-10:30am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T083000
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T103000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU

weekends 9:15-11:15am
DTSTART:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T091500
DTEND:{ref + reldate(**(
    {'days': 1} if ref.weekday() == SATURDAY else
    {'weekday': SA}
))}T111500
RRULE:FREQ=WEEKLY;BYDAY=SA,SU
