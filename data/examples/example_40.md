weekends 10am-12pm
DTSTART:{ref + reldate((days=1) if ref.weekday == SA else (weekday=SA))}T100000
DTEND:{ref + reldate((days=1) if ref.weekday == SA else (weekday=SA))}T120000
# we can use != to exclude a day, otherwise add 1 day