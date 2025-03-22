# Taxonomy examples
## Structure:

*Extra context*
phrase
iCal fields
*# Note*

## Contents
### SIMPLE RELATIVE EXPRESSIONS
in 2 days
in 2 days at 10am
next mon
next week
in 4hrs
2 weeks today
1wk from now
tmrw 10am
noon
1230

### RECURRING RULES (RRULE)
every wed 2pm
every weekday 9am-10am
1030 mon, wed & sat 3h
every 10 minutes between 2 and 7pm
every christmas eve
every 3rd sat of month 9am
every other sat 10-12pm

### TIME RANGES
2-3:30pm last fri of month
5-6pm tuesday
from 6 til 8pm
nov 6-8
fri night 8pm till 10:30

### COMBINATION EXPRESSIONS
weekdays minus thursday
thursdays, mondays and saturdays
weekends and wednesdays
every tues except last week of month
last workday of every month 10am

### ABSOLUTE DATE EXPRESSIONS
wed 1st oct
3rd june
june 3
halloween 9pm
christmas eve 2pm

### DURATION-BASED
tuesday 10am for 2h
for 1hr
for 1.5hrs
last sun feb 0800 2hrs

### TIME ZONE EXPRESSIONS
2:38pm in hawaii
8pm EST
9:19am madrid time
GMT+1 1200
1745+0800

### ALARM/REMINDER EXPRESSIONS
remind 30m before 10am
aug 9th 7pm rem 1hr
sat 9am, sun 10am, tue 330pm remind 15m before

### SPECIAL CASES
first mon of next quarter
fiscal week 32 wed 1530
Q2 w3 tuesday 10am
sem 1 week 3 tues 1010

### COMPLEX CONDITIONAL LOGIC
next weekday
weekends 10am-12pm
every 15 minutes from 1600-1800 on weekdays
every 2nd weekday



## Examples
--------------------------------


every wed 2pm
DTSTART:{ref + relativedelta(weekday=WE(1))}T140000
RRULE:FREQ=WEEKLY;BYDAY=WE;

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
DTSTART:{ref + relativedelta(weekday=MO) + relativedelta(weekday=SA)}T090500
DTEND:{ref + relativedelta(weekday=MO) + relativedelta(weekday=SA)}T133000
DURATION:PT3H
RDATE:{ref + relativedelta(weekday=MO) + 0}T090500
RDATE:{ref + relativedelta(weekday=MO) + relativedelta(weekday=WE)}T090500
# we assume next week means the week commencing the next monday

next mon
DTSTART:{ref + relativedelta(days=1, weekday=MO)}
# 'next' mon implies monday starting next week, so we add 1 day to the reference time in the case we are already on a monday

next week
DTSTART:{ref + relativedelta(days=1, weekday=MO)}

DTFORMAT: en-UK
16/08 1245-4pm
DTSTART:{ref + relativedelta(day=16, month=8)}T124500
DTEND:{ref + relativedelta(day=16, month=8)}T160000
# extra context is necessary for absolute dates, I include extra context as a pretext to the input prompt

DTFORMAT: en-US
12/25
DTSTART:{ref + relativedelta(day=25, month=12)}
DTEND:{ref + relativedelta(day=25+1, month=12)}

in 2 days
DTSTART:{ref + relativedelta(days=2)}

in 2 days at 10am
DTSTART:{ref + relativedelta(days=2)}T100000

next tuesday
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}

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

every 10 minutes between 2 and 7pm
DTSTART:{ref + relativedelta(hour=14)}T140000
RRULE:FREQ=MINUTELY;INTERVAL=10;UNTIL:{ref + relativedelta(hour=19)}T190000

between 3 and 4
DTSTART:{ref + relativedelta(hour=3)}T030000
DTEND:{ref + relativedelta(hour=4)}T040000

10 tomorrow
DTSTART:{ref + relativedelta(days=1)}T100000

tues at 1
DTSTART:{ref + relativedelta(weekday=TU(1))}T010000

tues at 1am
DTSTART:{ref + relativedelta(weekday=TU(1))}T010000

from 6 til 8pm
DTSTART:{ref + relativedelta(hour=18)}T180000
DTEND:{ref + relativedelta(hour=20)}T200000

remind 30m before 10am
DTSTART:{ref + relativedelta(hour=10)}T100000
VALARM:TRIGGER:-PT30M

from new years day 9am repeat daily
DTSTART:{ref + relativedelta(month=1, day=1)}T090000
RRULE:FREQ=DAILY

next week friday 445pm
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T164500

in 2 weeks 4 days
DTSTART:{ref + relativedelta(weeks=2, days=4)}

2 weeks today
DTSTART:{ref + relativedelta(weeks=2)}

monday next week
DTSTART:{ref + relativedelta(days=1, weekday=MO)}

thurs in 2 weeks
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH(2))}

next weekday
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}

weekdays 2-4pm
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T140000
DTEND:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T160000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR

every fri 2pm except next week
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T140000
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}

hourly from 9am to 5pm weekdays
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={range(9, 17)}

weekends 10am-12pm
DTSTART:{ref + relativedelta((days=1) if ref.weekday == SA else (weekday=SA))}T100000
DTEND:{ref + relativedelta((days=1) if ref.weekday == SA else (weekday=SA))}T120000
# we can use != to exclude a day, otherwise add 1 day

1wk from now
DTSTART:{ref + relativedelta(weeks=1)}

2wk thursday 10am
DTSTART:{ref + relativedelta(weekday=TH(1), weeks=2)}T100000

tmrw 10am
DTSTART:{ref + relativedelta(days=1)}T100000

next week
DTSTART:{ref + relativedelta(days=1, weekday=MO)}


DTFORMAT: en-UK
14/06
DTSTART:{ref + relativedelta(day=14, month=6)}


noon
DTSTART:{ref + relativedelta(hour=12)}T120000

DTFORMAT: en-US
12/30 noon
DTSTART:{ref + relativedelta(day=30, month=12)}T120000

noon fri
DTSTART:{ref + relativedelta(weekday=FR(1))}T120000

1230
DTSTART:{ref + relativedelta(hour=12, minute=30)}T123000

Q1 26
DTSTART:{datetime(2026, 1,1) + relativedelta(weekday=MO)}

Q4
DTSTART:{ref + relativedelta(month=10, weekday=MO)}

Q2 2029
DTSTART:{datetime(2029, 4,1) + relativedelta(weekday=MO)}

weekdays minus thursday
DTSTART:{ref + relativedelta(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

thursdays, mondays and saturdays
DTSTART:{ref + relativedelta(**(
    {'weekday': TH} if ref.weekday() < THURSDAY else
    {'weekday': SA} if ref.weekday() < SATURDAY else
    {'weekday': MO}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TH,SA

weekends and wednesdays
DTSTART:{ref + relativedelta(**(
    {'weekday': WE} if ref.weekday() < WEDNESDAY else
    {'weekday': SA} if ref.weekday() < SATURDAY else
    {'weekday': SU} if ref.weekday() < SUNDAY else
    {'weekday': WE}
))}
RRULE:FREQ=WEEKLY;BYDAY=WE,SA,SU

every tues and every other mon
DTSTART:{ref + relativedelta(**(
    {'weekday': TU} if ref.weekday() < TUESDAY else
    {'weekday': MO} if ref.weekday() < MONDAY else
    {'weekday': TU}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO;INTERVAL=2;BYDAY=TU;


nov 6,7,8 annually 10-12pm
DTSTART:{ref + relativedelta(month=11, day=6)}T100000
DTEND:{ref + relativedelta(month=11, day=6)}T120000
RRULE:FREQ=YEARLY;BYMONTH=11;BYMONTHDAY=6,7,8

july 10-14 annually 10-12pm
DTSTART:{ref + relativedelta(month=7, day=10)}T100000
DTEND:{ref + relativedelta(month=7, day=14)}T120000
RRULE:FREQ=YEARLY;BYMONTH=7;BYMONTHDAY=10,11,12,13,14
# we expect that a date range includes the end date

nov 6-8
DTSTART:{ref + relativedelta(month=11, day=6)}
DTEND:{ref + relativedelta(month=11, day=8)}T235959
# we expect that a date range includes the end date, so we set the end time to midnight of the end date

every tues except last week of month
DTSTART:{ref + relativedelta(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + relativedelta(day=31,weekday=TU(-1))}


first mon of next quarter
DTSTART:{ref.replace(day=1) + relativedelta(months=4 - month % 3) + relativedelta(weekday=MO)}
# finding the next quarter is a bit tricky, we need to find the next quarter from the current month, we could create a custom parameter for relative quarters to improve accuracy

friday on the last week of the quarter
DTSTART:{ref + relativedelta(months=3 - month % 3, day = 31, weekday=FR(-1))}


<!-- the beginning of Q1 Q3 1500
DTSTART:{ref + relativedelta(months=3- month % 3, day = 1)}T150000
RDATE:{ref + relativedelta(months=3 - month % 3, day = 1)}
## should we bias the beginning of a business event to the first monday rather than the first date of the quarter? -->

the first mon of Q1-4 10:40
DTSTART:{ref.replace(month=1, day=1)}T104000
RDATE:{ref.replace(month=4, day=1)}
RDATE:{ref.replace(month=7, day=1)}
RDATE:{ref.replace(month=10, day=1)}

the second mon of Q1-4 8-9am every year
DTSTART:{ref.replace(month=1, day=1) + relativedelta(weekday=MO(2))}T080000
RRULE:FREQ=YEARLY;BYMONTH=1,4,7,10;BYDAY=MO;BYSETPOS=2

quarterly 9am mon on first week
DTSTART:{ref.replace(month=1, day=1) + relativedelta(weekday=MO(1))}T090000
RRULE:FREQ=YEARLY;BYMONTH=1,4,7,10;BYDAY=MO;BYSETPOS=1

Q2 w3 tuesday 10am
DTSTART:{ref + relativedelta(month=4, day=1) + relativedelta(weekday=TU(3))}T100000


last sunday of every month
DTSTART:{ref + relativedelta(day = 31, weekday=SU(-1))}
RRULE:FREQ=MONTHLY;BYDAY=-1SU

aug 9th 7pm rem 1hr
DTSTART:{ref + relativedelta(day=9, month=8)}T190000
VALARM:TRIGGER:-PT1H

last sun feb 0800 2hrs
DTSTART:{ref + relativedelta(month=2, day=31, weekday=SU(-1))}T080000
DURATION:PT2H

last fri of june 1pm
DTSTART:{ref + relativedelta(month=6, day=31, weekday=FR(-1))}T130000

in 4hrs
DTSTART:{ref + relativedelta(hours=4)}

GMT+1 1200
DTSTART:{ref + relativedelta(hour=12)}T120000
TZOFFSETFROM:+0000
TZOFFSETTO:+0100

EST+5
DTSTART:{ref + relativedelta(hour=5)}T050000
TZOFFSETFROM:-0500
TZOFFSETTO:-0400

2:38pm in hawaii
DTSTART;TZID=Pacific/Honolulu:{ref + relativedelta(hour=14, minute=38)}T143800
# in this case we calculate from *our* reference time, not the target time. This could cause confusion as it might not technically be past 14:38 in hawaii even if it is in the past for us.

8pm EST
DTSTART;TZID=America/New_York:{ref + relativedelta(hour=20)}T200000

9:19am madrid time
DTSTART;TZID=Europe/Madrid:{ref + relativedelta(hour=9, minute=19)}

2pm chile time
DTSTART;TZID=America/Santiago:{ref + relativedelta(hour=14)}T140000

1745+0800
DTSTART:{ref + relativedelta(hour=17, minute=45)}T174500
TZOFFSETTO:+0800

3 jan 2pm 1hr
DTSTART:{ref + relativedelta(day=3, month=1)}T140000
DURATION:PT1H

every mon 0700 45mins
DTSTART:{ref + relativedelta(weekday=MO(1))}T070000
DURATION:PT45M

fri night 8pm till 10:30
DTSTART:{ref + relativedelta(weekday=FR(1))}T200000
DTEND:{ref + relativedelta(weekday=FR(1))}T223000

every tues unless 1st week of month
DTSTART:{ref + relativedelta(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + relativedelta(day=1,weekday=TU(1))}

every other sat 10-12pm
DTSTART:{ref + relativedelta(weekday=SA(1))}T100000
DTEND:{ref + relativedelta(weekday=SA(1))}T120000
RRULE:FREQ=WEEKLY;BYDAY=SA;INTERVAL=2

every 20 minutes from 3 to 4pm
DTSTART:{ref + relativedelta(hour=15)}T150000
RRULE:FREQ=MINUTELY;INTERVAL=20;UNTIL:{ref + relativedelta(hour=16)}


every 15 minutes from 1600-1800 on weekdays
DTSTART:{ref + relativedelta( weekday = MO|TU|WE|TH|FR)}T160000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYMINUTE=0,15,30,45

1033 then every 20m until 5pm weekdays
DTSTART:{ref + relativedelta( weekday = MO|TU|WE|TH|FR)}T103300
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={range(10, 17)};BYMINUTE=13,33,53;
# the kings building bus schedule

in 10m
DTSTART:{ref + relativedelta(minutes=10)}

wkly 7pm mon
DTSTART:{ref + relativedelta(weekday=MO(1))}T190000
RRULE:FREQ=WEEKLY;BYDAY=MO;

15 past the hour every hour from 9-5pm weekdays
DTSTART:{ref + relativedelta( weekday = MO|TU|WE|TH|FR)}T091500
RRULE:FREQ=HOURLY;BYMINUTE=15;COUNT={17-9};

every 5 days from now except last 2 weeks of feb
DTSTART:{ref + relativedelta(days=5)}
RRULE:FREQ=DAILY;INTERVAL=5;EXDATE:{ref + relativedelta(month=2, day=28, weekday=TU(-2))}

weekly from 9am today til 5pm in 2 fridays
DTSTART:{ref}T090000
RRULE:FREQ=WEEKLY;UNTIL:{ref + relativedelta(weekday=FR(2), hour=17)}

weekly on friday from 18 jun til 20 oct
DTSTART:{ref + relativedelta(weekday=FR(1), month=6, day=18)}
RRULE:FREQ=WEEKLY;BYDAY=FR;UNTIL:{ref + relativedelta(month=10, day=20)}

every 2 days for 10 weeks
DTSTART:{ref + relativedelta(days=2)}
RRULE:FREQ=DAILY;INTERVAL=2;UNTIL:{ref + relativedelta(weeks=10)}

3pm tuesdays for 2mo
DTSTART:{ref + relativedelta(weekday=TU(1))}T150000
RRULE:FREQ=WEEKLY;BYDAY=TU;UNTIL:{ref + relativedelta(months=2)}

every other weekend after jul 1st
DTSTART:{ref + relativedelta(month=7, day=1)}
RRULE:FREQ=WEEKLY;BYDAY=SA,SU;INTERVAL=2

every 2nd weekday
DTSTART:{ref + relativedelta(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU,WE,TH;INTERVAL=2

every 2nd weekend
DTSTART:{ref + relativedelta(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA,SU;INTERVAL=2

every tu for 10 times
DTSTART:{ref + relativedelta(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;COUNT={10}

every other day for 19 times
DTSTART:{ref + relativedelta(days=2)}
RRULE:FREQ=DAILY;INTERVAL=2;COUNT={19}

daily 8am
DTSTART:{ref + relativedelta(hour=8)}
RRULE:FREQ=DAILY

halloween 9pm
DTSTART:{ref + relativedelta(month=10, day=31)}T210000

christmas eve 2pm
DTSTART:{ref + relativedelta(month=12, day=24)}T140000

every christmas eve
DTSTART:{ref + relativedelta(month=12, day=24)}
RRULE:FREQ=YEARLY;BYMONTH=12;BYMONTHDAY=24

sat 9am, sun 10am, tue 330pm remind 15m before
DTSTART:{ref + relativedelta(weekday=SA(1))}T090000
RDATE:{ref + relativedelta(weekday=SU(1))}T100000
RDATE:{ref + relativedelta(weekday=TU(1))}T153000
VALARM:TRIGGER:-PT15M

every 3rd sat of month 9am
DTSTART:{ref + relativedelta(day=1, weekday=SA(3))}T090000
RRULE:FREQ=MONTHLY;BYDAY=SA;BYSETPOS=3

the last weekend of the month 10am
DTSTART:{ref + relativedelta(day=31, weekday=SU(-1)|SA(-1))}T100000

last workday of every month 10am
DTSTART:{ref + relativedelta(day=31, weekday=FR(-1)|TH(-1)|TU(-1)|WE(-1)|MO(-1))}T100000
RRULE:FREQ=MONTHLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=-1

3rd sat of this month 1035
DTSTART:{ref.replace(day=1) + relativedelta(weekday=SA(3))}T103500

sem 1 start sept 15
sem 1 week 3 tues 1010
DTSTART:{ref.replace(month=9, day=15) + relativedelta(weekday=TU(3))}T101000

this is the 3rd week of sem 1
week 5 tues 1149-1300
DTSTART:{ref - relativedelta(weeks=2, weekday=MO(-1)) + relativedelta(weekday=TU(5))}T114900
DTEND:{ref - relativedelta(weeks=2, weekday=MO(-1)) + relativedelta(weekday=TU(5))}T130000

fiscal year starts apr 5
fiscal week 32 wed 1530
DTSTART:{ref.replace(month=4, day=5) + relativedelta(weekday=WE(32))}T153000


fiscal year start apr 1
first mon of FY28
DTSTART:{ref.replace(year=2028, month=4, day=1) + relativedelta(weekday=MO(1))}

fiscal year start jan 1
every second wed of this fiscal year
DTSTART:{ref.replace(month=1, day=1) + relativedelta(weekday=WE(2))}




