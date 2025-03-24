every christmas eve
DTSTART:{ref + reldate(month=12, day=24)}
RRULE:FREQ=YEARLY;BYMONTH=12;BYMONTHDAY=24

every new year's day
DTSTART:{ref + reldate(month=1, day=1)}
RRULE:FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1

every valentine's day
DTSTART:{ref + reldate(month=2, day=14)}
RRULE:FREQ=YEARLY;BYMONTH=2;BYMONTHDAY=14

every st. patrick's day
DTSTART:{ref + reldate(month=3, day=17)}
RRULE:FREQ=YEARLY;BYMONTH=3;BYMONTHDAY=17

every april fool's day
DTSTART:{ref + reldate(month=4, day=1)}
RRULE:FREQ=YEARLY;BYMONTH=4;BYMONTHDAY=1

every earth day
DTSTART:{ref + reldate(month=4, day=22)}
RRULE:FREQ=YEARLY;BYMONTH=4;BYMONTHDAY=22

every cinco de mayo
DTSTART:{ref + reldate(month=5, day=5)}
RRULE:FREQ=YEARLY;BYMONTH=5;BYMONTHDAY=5

every mother's day
DTSTART:{ref + reldate(month=5, weekday=SU(2))}
RRULE:FREQ=YEARLY;BYMONTH=5;BYDAY=SU;BYSETPOS=2

every father's day
DTSTART:{ref + reldate(month=6, weekday=SU(3))}
RRULE:FREQ=YEARLY;BYMONTH=6;BYDAY=SU;BYSETPOS=3

every independence day
DTSTART:{ref + reldate(month=7, day=4)}
RRULE:FREQ=YEARLY;BYMONTH=7;BYMONTHDAY=4

every labor day
DTSTART:{ref + reldate(month=9, weekday=MO(1))}
RRULE:FREQ=YEARLY;BYMONTH=9;BYDAY=MO;BYSETPOS=1

every columbus day
DTSTART:{ref + reldate(month=10, weekday=MO(2))}
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=MO;BYSETPOS=2

every halloween
DTSTART:{ref + reldate(month=10, day=31)}
RRULE:FREQ=YEARLY;BYMONTH=10;BYMONTHDAY=31

every veterans day
DTSTART:{ref + reldate(month=11, day=11)}
RRULE:FREQ=YEARLY;BYMONTH=11;BYMONTHDAY=11
