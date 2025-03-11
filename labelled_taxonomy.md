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

in 2 days
DTSTART:{ref + relativedelta(days=2)}

in 2 days at 10am
DTSTART:{ref + relativedelta(days=2)}T100000

next tuesday
DTSTART:{ref + relativedelta(weekday=TU(2 if ref.weekday() < TUESDAY else 1))}


first mon of feb
DTSTART:{ref + relativedelta(month=2, weekday=MO(1))}


3rd june
DTSTART:{ref + relativedelta(day=3, month=6)}


june 3
DTSTART:{ref + relativedelta(day=3, month=6)}


for 1hr
DTSTART:{ref}
DURATION:PT1H

for 1.5hrs
DTSTART:{ref}
DURATION:PT1H30M

for 3hrs
DTSTART:{ref}
DURATION:PT3H

every 10 minutes between 3 and 4
RRULE:FREQ=MINUTELY;BYHOUR=15,16;BYMINUTE=0,10,20,30,40,50


# intervals

between 3 and 4
DTSTART:{ref + relativedelta(hour=3)}
DTEND:{ref + relativedelta(hour=4)}

10 tomorrow
DTSTART:{ref + relativedelta(days=1)}T100000

tues at 1
DTSTART:{ref + relativedelta(weekday=TU(1))}T010000

tues at 1am
DTSTART:{ref + relativedelta(weekday=TU(1))}T010000

from 6 til 8pm
DTSTART:{ref + relativedelta(hour=18)}
DTEND:{ref + relativedelta(hour=20)}

remind 30m before 10am
DTSTART:{ref + relativedelta(hour=10)}
VALARM:TRIGGER:-PT30M

from new years day 9am repeat daily
DTSTART:{ref + relativedelta(month=1, day=1)}T090000
RRULE:FREQ=DAILY

next week friday 445pm
DTSTART:{ref + relativedelta(weekday=FR(1))}T164500

in 2 weeks 4 days
DTSTART:{ref + relativedelta(weeks=2, days=4)}

2 weeks today
DTSTART:{ref + relativedelta(weeks=2)}

monday next week
DTSTART:{ref + relativedelta(weekday=MO(1))}

thurs in 2 weeks
DTSTART:{ref + relativedelta(weekday=TH(2))}






















































































