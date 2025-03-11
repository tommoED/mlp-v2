every wed 2pm
DTSTART:{ref + relativedelta(weekday=WE(1))}T140000
RRULE:FREQ=WEEKLY;BYDAY=WE;BYHOUR=14;BYMINUTE=00;BYSECOND=00

thursday in 2 weeks
DTSTART:{ref + relativedelta(weeks=2, weekday=TH(1))}

wed 1st oct
DTSTART:{ref + relativedelta(day=1, month=10, weekday=WE(1))}


2-3:30pm last fri of month
DTSTART:{ref + relativedelta(day=31, weekday=FR(-1))}T140000
DTEND:{ref + relativedelta(day=31, weekday=FR(-1))}T153000


5-6pm tuesday
DTSTART:{ref + relativedelta(weekday=TU(1))}T170000
DTEND:{ref + relativedelta(weekday=TU(1))}T180000

tuesday 10am for 2h
DTSTART:{ref + relativedelta(weekday=TU(1))}T100000
DURATION:PT2H

every weekday 9am-10am
DTSTART:{ref + relativedelta(weekday=MO(1))}T090000
DTEND:{ref + relativedelta(weekday=MO(1))}T100000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR


1030 mon, wed & sat 3h
DTSTART:{ref + relativedelta(weekday=MO(1))}T103000
DURATION:PT3H
RRULE:FREQ=WEEKLY;BYDAY=MO,WE,SA


next sat, mon, wed 905-1330
DTSTART:{ref + relativedelta(weekday=SA(1))}T090500
DTEND:{ref + relativedelta(weekday=SA(1))}T133000
DURATION:PT3H
RDATE:{ref + relativedelta(weekday=MO(1))}T090500
RDATE:{ref + relativedelta(weekday=WE(1))}T090500


16/08 1245-4pm
DTFORMAT: en-UK
DTSTART:{ref + relativedelta(day=16, month=8)}T124500
DTEND:{ref + relativedelta(day=16, month=8)}T160000


12/25
DTFORMAT: en-US
DTSTART:{ref + relativedelta(day=25, month=12)}
DTEND:{ref + relativedelta(day=25+1, month=12)}









































