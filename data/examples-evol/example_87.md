1033 then every 20m until 5pm weekdays
DTSTART:{ref + reldate( weekday = MO|TU|WE|TH|FR)}T103300
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={10,11,12,13,14,15,16};BYMINUTE=13,33,53;

1230 then every 15m until 5pm weekdays
DTSTART:{ref + reldate(weekday=MO(1))}T123000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={12,13,14,15,16};BYMINUTE=00,15,30,45;

