1033 then every 20m until 5pm weekdays
DTSTART:{ref + reldate( weekday = MO|TU|WE|TH|FR)}T103300
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={range(10, 17)};BYMINUTE=13,33,53;
# the kings building bus schedule