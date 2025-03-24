next sat, mon, wed 905-1330
DTSTART:{ref + reldate(weekday=MO) + reldate(weekday=SA)}T090500
DTEND:{ref + reldate(weekday=MO) + reldate(weekday=SA)}T133000
DURATION:PT3H
RDATE:{ref + reldate(weekday=MO) + 0}T090500
RDATE:{ref + reldate(weekday=MO) + reldate(weekday=WE)}T090500
# we assume next week means the week commencing the next monday