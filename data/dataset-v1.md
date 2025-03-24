wed 9:20
---
DTSTART:{ref + relativedelta(weekday=WE)}T092000
RRULE:FREQ=WEEKLY;BYDAY=WE;

mon 3:45
---
DTSTART:{ref + relativedelta(weekday=MO)}T154500
RRULE:FREQ=WEEKLY;BYDAY=MO;

tue 11:30
---
DTSTART:{ref + relativedelta(weekday=TU)}T113000
RRULE:FREQ=WEEKLY;BYDAY=TU;

thu 2:15
---
DTSTART:{ref + relativedelta(weekday=TH)}T141500
RRULE:FREQ=WEEKLY;BYDAY=TH;

fri 7:00
---
DTSTART:{ref + relativedelta(weekday=FR)}T070000
RRULE:FREQ=WEEKLY;BYDAY=FR;

sat 10:45
---
DTSTART:{ref + relativedelta(weekday=SA)}T104500
RRULE:FREQ=WEEKLY;BYDAY=SA;

sun 8:30
---
DTSTART:{ref + relativedelta(weekday=SU)}T083000
RRULE:FREQ=WEEKLY;BYDAY=SU;

wed 6:15
---
DTSTART:{ref + relativedelta(weekday=WE)}T061500
RRULE:FREQ=WEEKLY;BYDAY=WE;

mon 12:00
---
DTSTART:{ref + relativedelta(weekday=MO)}T120000
RRULE:FREQ=WEEKLY;BYDAY=MO;

tue 530
---
DTSTART:{ref + relativedelta(weekday=TU)}T173000
RRULE:FREQ=WEEKLY;BYDAY=TU;

thu 9:45pm
---
DTSTART:{ref + relativedelta(weekday=TH)}T214500
RRULE:FREQ=WEEKLY;BYDAY=TH;

fri 4:20
---
DTSTART:{ref + relativedelta(weekday=FR)}T162000
RRULE:FREQ=WEEKLY;BYDAY=FR;

sat 1:10
---
DTSTART:{ref + relativedelta(weekday=SA)}T131000
RRULE:FREQ=WEEKLY;BYDAY=SA;

sun 7:25pm
---
DTSTART:{ref + relativedelta(weekday=SU)}T192500
RRULE:FREQ=WEEKLY;BYDAY=SU;

wed 10:05pm
---
DTSTART:{ref + relativedelta(weekday=WE)}T220500
RRULE:FREQ=WEEKLY;BYDAY=WE;

next mon 9am
---
DTSTART:{ref + relativedelta(days=1, weekday=MO)}T090000

next tue 10am
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}T100000

next wed 11am
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T110000

next thu 12pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH)}T120000

next fri 1pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T130000

next sat 2pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T140000

next sun 3pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T150000

next mon 4:30pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO)}T163000

next tue 5:45pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}T174500

next wed 6:15am
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T061500

next thu 7:30pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH)}T193000

next fri 8:45am
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T084500

next sat 9:15pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T211500

next sun 10:30am
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T103000

next mon 11:45pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO)}T234500

every mon 9am
---
DTSTART:{ref + relativedelta(weekday=MO)}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO;

every tue 3pm
---
DTSTART:{ref + relativedelta(weekday=TU)}T150000
RRULE:FREQ=WEEKLY;BYDAY=TU;

every thu 5pm
---
DTSTART:{ref + relativedelta(weekday=TH)}T170000
RRULE:FREQ=WEEKLY;BYDAY=TH;

every fri 2:30pm
---
DTSTART:{ref + relativedelta(weekday=FR)}T143000
RRULE:FREQ=WEEKLY;BYDAY=FR;

every sat 715am
---
DTSTART:{ref + relativedelta(weekday=SA)}T071500
RRULE:FREQ=WEEKLY;BYDAY=SA;

every sun 445pm
---
DTSTART:{ref + relativedelta(weekday=SU)}T164500
RRULE:FREQ=WEEKLY;BYDAY=SU;

every day 9:30pm
---
DTSTART:{ref + relativedelta(hour=21, minute=30)}T213000
RRULE:FREQ=DAILY;

every weekday 1pm
---
DTSTART:{ref + relativedelta(weekday=MO|TU|WE|TH|FR)}T130000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;

every weekend 4pm
---
DTSTART:{ref + relativedelta(weekday=SA|SU)}T160000
RRULE:FREQ=WEEKLY;BYDAY=SA,SU;

every mon wed fri 7am
---
DTSTART:{ref + relativedelta(weekday=MO|WE|FR)}T070000
RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR;

every tue thu 6pm
---
DTSTART:{ref + relativedelta(weekday=TU|TH)}T180000
RRULE:FREQ=WEEKLY;BYDAY=TU,TH;

every week 3pm
---
DTSTART:{ref + relativedelta(days=7)}T150000
RRULE:FREQ=WEEKLY;

every 2 weeks 4pm
---
DTSTART:{ref + relativedelta(days=14)}T160000
RRULE:FREQ=WEEKLY;INTERVAL=2;


every month 15th 10am
---
DTSTART:{ref + relativedelta(day=15)}T100000
RRULE:FREQ=MONTHLY;

every month 1st 9am
---
DTSTART:{ref + relativedelta(day=1)}T090000
RRULE:FREQ=MONTHLY;

every month 5th 2pm
---
DTSTART:{ref + relativedelta(day=5)}T140000
RRULE:FREQ=MONTHLY;

10th of every month 3:30pm
---
DTSTART:{ref + relativedelta(day=10)}T153000
RRULE:FREQ=MONTHLY;

8:37am on the 20th monthly
---
DTSTART:{ref + relativedelta(day=20)}T083700
RRULE:FREQ=MONTHLY;

7:23pm 25th each month
---
DTSTART:{ref + relativedelta(day=25)}T192300
RRULE:FREQ=MONTHLY;

1142 3rd monthly
---
DTSTART:{ref + relativedelta(day=3)}T114200
RRULE:FREQ=MONTHLY;

5:15pm on the 12th every month
---
DTSTART:{ref + relativedelta(day=12)}T171500
RRULE:FREQ=MONTHLY;

every month 18th 615am
---
DTSTART:{ref + relativedelta(day=18)}T061500
RRULE:FREQ=MONTHLY;

every month 22nd 1645
---
DTSTART:{ref + relativedelta(day=22)}T164500
RRULE:FREQ=MONTHLY;

every month 7th 12pm
---
DTSTART:{ref + relativedelta(day=7)}T120000
RRULE:FREQ=MONTHLY;

every month 28th 1:30pm
---
DTSTART:{ref + relativedelta(day=28)}T133000
RRULE:FREQ=MONTHLY;

monthly on 14th 9:30pm
---
DTSTART:{ref + relativedelta(day=14)}T213000
RRULE:FREQ=MONTHLY;

monthly 8th 6am
---
DTSTART:{ref + relativedelta(day=8)}T060000
RRULE:FREQ=MONTHLY;

every 30th 1030pm
---
DTSTART:{ref + relativedelta(day=30)}T223000
RRULE:FREQ=MONTHLY;

monday in 3 weeks
---
DTSTART:{ref + relativedelta(weeks=3, weekday=MO)}

friday in 1 week
---
DTSTART:{ref + relativedelta(weeks=1, weekday=FR)}

wednesday in 4 weeks
---
DTSTART:{ref + relativedelta(weeks=4, weekday=WE)}

tuesday in 5 weeks
---
DTSTART:{ref + relativedelta(weeks=5, weekday=TU)}

saturday in 2 weeks
---
DTSTART:{ref + relativedelta(weeks=2, weekday=SA)}

sunday in 3 weeks
---
DTSTART:{ref + relativedelta(weeks=3, weekday=SU)}

monday in 6 weeks
---
DTSTART:{ref + relativedelta(weeks=6, weekday=MO)}

thursday in 7 weeks
---
DTSTART:{ref + relativedelta(weeks=7, weekday=TH)}

wednesday in 10 weeks
---
DTSTART:{ref + relativedelta(weeks=10, weekday=WE)}

friday in 8 weeks
---
DTSTART:{ref + relativedelta(weeks=8, weekday=FR)}

tuesday in 9 weeks
---
DTSTART:{ref + relativedelta(weeks=9, weekday=TU)}

saturday in 4 weeks
---
DTSTART:{ref + relativedelta(weeks=4, weekday=SA)}

sunday in 5 weeks
---
DTSTART:{ref + relativedelta(weeks=5, weekday=SU)}

wednesday in 12 weeks
---
DTSTART:{ref + relativedelta(weeks=12, weekday=WE)}


in 2 wednesdays
---
DTSTART:{ref + relativedelta(weekday=WE(2))}

in 3 thursdays
---
DTSTART:{ref + relativedelta(weekday=TH(3))}

in 4 fridays
---
DTSTART:{ref + relativedelta(weekday=FR(4))}

18 mondays from today
---
DTSTART:{ref + relativedelta(weekday=MO(18))}

147th monday from today
---
DTSTART:{ref + relativedelta(weekday=MO(147))}

3rd monday from today
---
DTSTART:{ref + relativedelta(weekday=MO(3))}


monday 2nd
---
DTSTART:{ref + relativedelta(day=2, weekday=MO)}

thursday 5th
---
DTSTART:{ref + relativedelta(day=5, weekday=TH)}


mon 5th jan
---
DTSTART:{ref + relativedelta(day=5, month=1, weekday=MO)}

tue 15th feb
---
DTSTART:{ref + relativedelta(day=15, month=2, weekday=TU)}

thursday the 20th of march
---
DTSTART:{ref + relativedelta(day=20, month=3, weekday=TH)}

10th of april, friday
---
DTSTART:{ref + relativedelta(day=10, month=4, weekday=FR)}

may 25th (saturday)
---
DTSTART:{ref + relativedelta(day=25, month=5, weekday=SA)}

june 30 sunday
---
DTSTART:{ref + relativedelta(day=30, month=6, weekday=SU)}

july 12 (wednesday)
---
DTSTART:{ref + relativedelta(day=12, month=7, weekday=WE)}

august 8, monday
---
DTSTART:{ref + relativedelta(day=8, month=8, weekday=MO)}

tuesday september 17
---
DTSTART:{ref + relativedelta(day=17, month=9, weekday=TU)}

october 3rd, thursday
---
DTSTART:{ref + relativedelta(day=3, month=10, weekday=TH)}

fri 22nd nov
---
DTSTART:{ref + relativedelta(day=22, month=11, weekday=FR)}

sat 14th dec
---
DTSTART:{ref + relativedelta(day=14, month=12, weekday=SA)}

sun 7th jan
---
DTSTART:{ref + relativedelta(day=7, month=1, weekday=SU)}

wed 28th feb
---
DTSTART:{ref + relativedelta(day=28, month=2, weekday=WE)}






2-3:30pm last fri of month
---
DTSTART:{ref + relativedelta(day=31, weekday=FR(-1))}T140000
DTEND:{ref + relativedelta(day=31, weekday=FR(-1))}T153000

9am-10:30am last mon of month
---
DTSTART:{ref + relativedelta(day=31, weekday=MO(-1))}T090000
DTEND:{ref + relativedelta(day=31, weekday=MO(-1))}T103000

11:00-12:00 last tue of month
---
DTSTART:{ref + relativedelta(day=31, weekday=TU(-1))}T110000
DTEND:{ref + relativedelta(day=31, weekday=TU(-1))}T120000

1pm to 2:30pm 2nd last wed of month
---
DTSTART:{ref + relativedelta(day=31, weekday=WE(-2))}T130000
DTEND:{ref + relativedelta(day=31, weekday=WE(-2))}T143000

from 3 until 4:15pm last thu of month
---
DTSTART:{ref + relativedelta(day=31, weekday=TH(-1))}T150000
DTEND:{ref + relativedelta(day=31, weekday=TH(-1))}T161500

5-645 in the evening last sat of month
---
DTSTART:{ref + relativedelta(day=31, weekday=SA(-1))}T170000
DTEND:{ref + relativedelta(day=31, weekday=SA(-1))}T184500

7-830pm 2nd last sun of month
---
DTSTART:{ref + relativedelta(day=31, weekday=SU(-2))}T190000
DTEND:{ref + relativedelta(day=31, weekday=SU(-2))}T203000

10am till 11:15 first mon of month
---
DTSTART:{ref + relativedelta(day=1, weekday=MO(1))}T100000
DTEND:{ref + relativedelta(day=1, weekday=MO(1))}T111500

noon-1:30p first tue of month
---
DTSTART:{ref + relativedelta(day=1, weekday=TU(1))}T120000
DTEND:{ref + relativedelta(day=1, weekday=TU(1))}T133000

between 2 and 3:45 first wed of month
---
DTSTART:{ref + relativedelta(day=1, weekday=WE(1))}T140000
DTEND:{ref + relativedelta(day=1, weekday=WE(1))}T154500

16:00-17:30 first thu of month
---
DTSTART:{ref + relativedelta(day=1, weekday=TH(1))}T160000
DTEND:{ref + relativedelta(day=1, weekday=TH(1))}T173000

6pm to 7:15 first fri of month
---
DTSTART:{ref + relativedelta(day=1, weekday=FR(1))}T180000
DTEND:{ref + relativedelta(day=1, weekday=FR(1))}T191500

8 till 9:30 evening first sat of month
---
DTSTART:{ref + relativedelta(day=1, weekday=SA(1))}T200000
DTEND:{ref + relativedelta(day=1, weekday=SA(1))}T213000

1000-1145 first sun of month
---
DTSTART:{ref + relativedelta(day=1, weekday=SU(1))}T100000
DTEND:{ref + relativedelta(day=1, weekday=SU(1))}T114500

13:00-14:30 third wed of month
---
DTSTART:{ref + relativedelta(day=1, weekday=WE(3))}T130000
DTEND:{ref + relativedelta(day=1, weekday=WE(3))}T143000


5-6pm tuesday
---
DTSTART:{ref + relativedelta(weekday=TU)}T170000
DTEND:{ref + relativedelta(weekday=TU)}T180000

9-10am wednesday
---
DTSTART:{ref + relativedelta(weekday=WE)}T090000
DTEND:{ref + relativedelta(weekday=WE)}T100000

2-3:30pm thursday
---
DTSTART:{ref + relativedelta(weekday=TH)}T140000
DTEND:{ref + relativedelta(weekday=TH)}T153000

7-8:15pm friday
---
DTSTART:{ref + relativedelta(weekday=FR)}T190000
DTEND:{ref + relativedelta(weekday=FR)}T201500

11am-12pm saturday
---
DTSTART:{ref + relativedelta(weekday=SA)}T110000
DTEND:{ref + relativedelta(weekday=SA)}T120000

3-4:45pm sunday
---
DTSTART:{ref + relativedelta(weekday=SU)}T150000
DTEND:{ref + relativedelta(weekday=SU)}T164500

8:30-9:30am monday
---
DTSTART:{ref + relativedelta(weekday=MO)}T083000
DTEND:{ref + relativedelta(weekday=MO)}T093000

12-1:30pm tuesday
---
DTSTART:{ref + relativedelta(weekday=TU)}T120000
DTEND:{ref + relativedelta(weekday=TU)}T133000

4-5:15pm wednesday
---
DTSTART:{ref + relativedelta(weekday=WE)}T160000
DTEND:{ref + relativedelta(weekday=WE)}T171500

6:30-8pm thursday
---
DTSTART:{ref + relativedelta(weekday=TH)}T183000
DTEND:{ref + relativedelta(weekday=TH)}T200000

10-11:45am friday
---
DTSTART:{ref + relativedelta(weekday=FR)}T100000
DTEND:{ref + relativedelta(weekday=FR)}T114500

1-2:30pm saturday
---
DTSTART:{ref + relativedelta(weekday=SA)}T130000
DTEND:{ref + relativedelta(weekday=SA)}T143000

7-9pm sunday
---
DTSTART:{ref + relativedelta(weekday=SU)}T190000
DTEND:{ref + relativedelta(weekday=SU)}T210000

9:30-10:30am monday
---
DTSTART:{ref + relativedelta(weekday=MO)}T093000
DTEND:{ref + relativedelta(weekday=MO)}T103000

2:45-4:15pm tuesday
---
DTSTART:{ref + relativedelta(weekday=TU)}T144500
DTEND:{ref + relativedelta(weekday=TU)}T161500

tuesday 10am for 2h
---
DTSTART:{ref + relativedelta(weekday=TU)}T100000
DURATION:PT2H

for 1h on monday at 9am
---
DTSTART:{ref + relativedelta(weekday=MO)}T090000
DURATION:PT1H

wednesday 2pm, duration 3h
---
DTSTART:{ref + relativedelta(weekday=WE)}T140000
DURATION:PT3H

1.5h thursday at 4pm
---
DTSTART:{ref + relativedelta(weekday=TH)}T160000
DURATION:PT1H30M

friday evening 6pm for 2.5h
---
DTSTART:{ref + relativedelta(weekday=FR)}T180000
DURATION:PT2H30M

4h saturday 11am
---
DTSTART:{ref + relativedelta(weekday=SA)}T110000
DURATION:PT4H

2h on sunday at 3pm
---
DTSTART:{ref + relativedelta(weekday=SU)}T150000
DURATION:PT2H

7pm monday for 1h
---
DTSTART:{ref + relativedelta(weekday=MO)}T190000
DURATION:PT1H

45m on tuesday 8am
---
DTSTART:{ref + relativedelta(weekday=TU)}T080000
DURATION:PT45M

wednesday 12pm for 1h
---
DTSTART:{ref + relativedelta(weekday=WE)}T120000
DURATION:PT1H

for 2h starting thursday 5:30pm
---
DTSTART:{ref + relativedelta(weekday=TH)}T173000
DURATION:PT2H

friday morning 10:30am, 1.5h duration
---
DTSTART:{ref + relativedelta(weekday=FR)}T103000
DURATION:PT1H30M

saturday afternoon for 3h at 2pm
---
DTSTART:{ref + relativedelta(weekday=SA)}T140000
DURATION:PT3H

duration 2h sunday 9:30am
---
DTSTART:{ref + relativedelta(weekday=SU)}T093000
DURATION:PT2H

30m monday 1pm
---
DTSTART:{ref + relativedelta(weekday=MO)}T130000
DURATION:PT30M

45m next tuesday 2pm
---
DTSTART:{ref + next(weekday=TU)}T140000
DURATION:PT45M

1h wednesday 3pm
---
DTSTART:{ref + relativedelta(weekday=WE)}T150000
DURATION:PT1H

1.5h thursday 4pm
---
DTSTART:{ref + relativedelta(weekday=TH)}T160000
DURATION:PT1H30M

2h friday 5pm
---
DTSTART:{ref + relativedelta(weekday=FR)}T170000
DURATION:PT2H

2.5h next saturday 6pm
---
DTSTART:{ref + next(weekday=SA)}T180000
DURATION:PT2H30M

3h next sunday 7pm
---
DTSTART:{ref + next(weekday=SU)}T190000
DURATION:PT3H

15m monday 8am
---
DTSTART:{ref + relativedelta(weekday=MO)}T080000
DURATION:PT15M

20m tuesday 9am
---
DTSTART:{ref + relativedelta(weekday=TU)}T090000
DURATION:PT20M

25m wednesday 10am
---
DTSTART:{ref + relativedelta(weekday=WE)}T100000
DURATION:PT25M

35m thursday 11am
---
DTSTART:{ref + relativedelta(weekday=TH)}T110000
DURATION:PT35M

40m next friday 12pm
---
DTSTART:{ref + next(weekday=FR)}T120000
DURATION:PT40M

50m saturday 1pm
---
DTSTART:{ref + relativedelta(weekday=SA)}T130000
DURATION:PT50M

55m sunday in 2w 2pm
---
DTSTART:{ref + next(weekday=SU(2))}T140000
DURATION:PT55M

4h monday 3pm
---
DTSTART:{ref + relativedelta(weekday=MO)}T150000
DURATION:PT4H

every weekday 9am-10am
---
DTSTART:{ref + relativedelta(weekday=MO)}T090000
DTEND:{ref + relativedelta(weekday=MO)}T100000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR


0947 mon, wed & sat 3h
---
DTSTART:{ref + relativedelta(weekday=MO)}T094700
DURATION:PT3H
RDATE:{ref + relativedelta(weekday=MO) + relativedelta(weekday=WE)}T094700
RDATE:{ref + relativedelta(weekday=MO) + relativedelta(weekday=SA)}T094700

10:30am tuesday, thursday and sunday for 2 hours
---
DTSTART:{ref + relativedelta(weekday=TU)}T103000
DURATION:PT2H
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=TH)}T103000
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=SU)}T103000

11:23am tuesday, thursday and sunday for 2 hours
---
DTSTART:{ref + relativedelta(weekday=TU)}T112300
DURATION:PT2H
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=TH)}T112300
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=SU)}T112300

tue fri sun 10:30am 1.5hr duration
---
DTSTART:{ref + relativedelta(weekday=TU)}T103000
DURATION:PT1H30M
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=FR)}T103000
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=SU)}T103000

tue fri sun 08:17am 1.5hr duration
---
DTSTART:{ref + relativedelta(weekday=TU)}T081700
DURATION:PT1H30M
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=FR)}T081700
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=SU)}T081700

1030-1430 on wed, fri, sun
---
DTSTART:{ref + relativedelta(weekday=WE)}T103000
DTEND:{ref + relativedelta(weekday=WE)}T143000
RDATE:{ref + relativedelta(weekday=WE) + relativedelta(weekday=FR)}T103000
RDATE:{ref + relativedelta(weekday=WE) + relativedelta(weekday=SU)}T103000

1412-1837 on wed, fri, sun
---
DTSTART:{ref + relativedelta(weekday=WE)}T141200
DTEND:{ref + relativedelta(weekday=WE)}T183700
RDATE:{ref + relativedelta(weekday=WE) + relativedelta(weekday=FR)}T141200
RDATE:{ref + relativedelta(weekday=WE) + relativedelta(weekday=SU)}T141200

10:30 on thursday, saturday & monday for 45 minutes
---
DTSTART:{ref + relativedelta(weekday=TH)}T103000
DURATION:PT45M
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA)}T103000
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA) + relativedelta(weekday=MO)}T103000

15:42 on thursday, saturday & monday for 45 minutes
---
DTSTART:{ref + relativedelta(weekday=TH)}T154200
DURATION:PT45M
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA)}T154200
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA) + relativedelta(weekday=MO)}T154200

2.5 hour sessions at 1135 on fri, sun and tue
---
DTSTART:{ref + relativedelta(weekday=FR)}T113500
DURATION:PT2H30M
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU)}T113500
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU) + relativedelta(weekday=TU)}T113500

2.5 hour sessions at 723am on fri, sun and tue
---
DTSTART:{ref + relativedelta(weekday=FR)}T072300
DURATION:PT2H30M
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU)}T072300
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU) + relativedelta(weekday=TU)}T072300

sunday, tuesday, thursday 10:30am for 1h
---
DTSTART:{ref + relativedelta(weekday=SU)}T103000
DURATION:PT1H
RDATE:{ref + relativedelta(weekday=SU) + relativedelta(weekday=TU)}T103000
RDATE:{ref + relativedelta(weekday=SU) + relativedelta(weekday=TH)}T103000

sunday, tuesday, thursday 6:58am for 1h
---
DTSTART:{ref + relativedelta(weekday=SU)}T065800
DURATION:PT1H
RDATE:{ref + relativedelta(weekday=SU) + relativedelta(weekday=TU)}T065800
RDATE:{ref + relativedelta(weekday=SU) + relativedelta(weekday=TH)}T065800

5h starting 10:30am on thu, sat, mon
---
DTSTART:{ref + relativedelta(weekday=TH)}T103000
DURATION:PT5H
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA)}T103000
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA) + relativedelta(weekday=MO)}T103000

5h starting 13:27 on thu, sat, mon
---
DTSTART:{ref + relativedelta(weekday=TH)}T132700
DURATION:PT5H
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA)}T132700
RDATE:{ref + relativedelta(weekday=TH) + relativedelta(weekday=SA) + relativedelta(weekday=MO)}T132700

10:30-12:30 on friday, sunday and wednesday
---
DTSTART:{ref + relativedelta(weekday=FR)}T103000
DTEND:{ref + relativedelta(weekday=FR)}T123000
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU)}T103000
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU) + relativedelta(weekday=WE)}T103000

09:18-11:43 on friday, sunday and wednesday
---
DTSTART:{ref + relativedelta(weekday=FR)}T091800
DTEND:{ref + relativedelta(weekday=FR)}T114300
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU)}T091800
RDATE:{ref + relativedelta(weekday=FR) + relativedelta(weekday=SU) + relativedelta(weekday=WE)}T091800

tue, thu & sun at 730am lasting 90 minutes
---
DTSTART:{ref + relativedelta(weekday=TU)}T073000
DURATION:PT1H30M
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=TH)}T073000
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=SU)}T073000

tue, thu & sun at 405pm lasting 90 minutes
---
DTSTART:{ref + relativedelta(weekday=TU)}T160500
DURATION:PT1H30M
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=TH)}T160500
RDATE:{ref + relativedelta(weekday=TU) + relativedelta(weekday=SU)}T160500

next sat, mon, wed 905-1330
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T090500
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T133000
DURATION:PT3H
RDATE:{ref + relativedelta(days=1, weekday=MO)}T090500
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T090500

next tue, thu, sat 1000-1200
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}T100000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}T120000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH)}T100000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T100000

next wed, fri, sun 1400-1600
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T140000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T160000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T140000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T140000

next mon, thu, sat 0800-0930
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO)}T080000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO)}T093000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH)}T080000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T080000

next tue, fri, sun 1530-1700
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}T153000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}T170000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T153000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T153000

next wed, sat, mon 1100-1300
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T110000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE)}T130000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T110000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO(+1))}T110000

next thu, sun, tue 0730-0900
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH)}T073000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH)}T090000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T073000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU(+1))}T073000

next fri, mon, wed 1245-1415
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T124500
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T141500
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO(+1))}T124500
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE(+1))}T124500

next sat, tue, thu 1630-1800
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T163000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA)}T180000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU(+1))}T163000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH(+1))}T163000

next sun, wed, fri 0900-1030
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T090000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU)}T103000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE(+1))}T090000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR(+1))}T090000

next mon, thu, sat 1300-1500
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO(+1))}T130000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO(+1))}T150000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH(+1))}T130000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA(+1))}T130000

next tue, fri, sun 0830-1000
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU(+1))}T083000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU(+1))}T100000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR(+1))}T083000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU(+1))}T083000

next wed, sat, mon 1500-1700
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE(+1))}T150000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE(+1))}T170000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SA(+1))}T150000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO(+2))}T150000

next thu, sun, tue 1900-2030
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH(+1))}T190000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH(+1))}T203000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=SU(+1))}T190000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU(+2))}T190000

next fri, mon, wed 0700-0830
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR(+1))}T070000
DTEND:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR(+1))}T083000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=MO(+2))}T070000
RDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=WE(+2))}T070000



next week
---
DTSTART:{ref + relativedelta(days=1, weekday=MO)}

DTFORMAT: DDMMYYYY
16/08 1245-4pm
---
DTSTART:{ref + relativedelta(day=16, month=8)}T124500
DTEND:{ref + relativedelta(day=16, month=8)}T160000

context as a pretext to the input prompt

DTFORMAT: DDMMYYYY
05/09 0900-1130
---
DTSTART:{ref + relativedelta(day=5, month=9)}T090000
DTEND:{ref + relativedelta(day=5, month=9)}T113000

DTFORMAT: DDMMYYYY
23/11 1500-1700
---
DTSTART:{ref + relativedelta(day=23, month=11)}T150000
DTEND:{ref + relativedelta(day=23, month=11)}T170000

DTFORMAT: DDMMYYYY
14/02 0830-1000
---
DTSTART:{ref + relativedelta(day=14, month=2)}T083000
DTEND:{ref + relativedelta(day=14, month=2)}T100000

DTFORMAT: DDMMYYYY
30/06 1900-2130
---
DTSTART:{ref + relativedelta(day=30, month=6)}T190000
DTEND:{ref + relativedelta(day=30, month=6)}T213000

DTFORMAT: DDMMYYYY
19/04 1000-1200
---
DTSTART:{ref + relativedelta(day=19, month=4)}T100000
DTEND:{ref + relativedelta(day=19, month=4)}T120000

DTFORMAT: DDMMYYYY
07/12 1330-1530
---
DTSTART:{ref + relativedelta(day=7, month=12)}T133000
DTEND:{ref + relativedelta(day=7, month=12)}T153000

DTFORMAT: DDMMYYYY
25/03 0730-0900
---
DTSTART:{ref + relativedelta(day=25, month=3)}T073000
DTEND:{ref + relativedelta(day=25, month=3)}T090000

DTFORMAT: DDMMYYYY
11/10 1600-1800
---
DTSTART:{ref + relativedelta(day=11, month=10)}T160000
DTEND:{ref + relativedelta(day=11, month=10)}T180000

DTFORMAT: DDMMYYYY
02/01 1100-1400
---
DTSTART:{ref + relativedelta(day=2, month=1)}T110000
DTEND:{ref + relativedelta(day=2, month=1)}T140000

DTFORMAT: DDMMYYYY
28/07 1415-1545
---
DTSTART:{ref + relativedelta(day=28, month=7)}T141500
DTEND:{ref + relativedelta(day=28, month=7)}T154500

DTFORMAT: DDMMYYYY
09/05 0945-1115
---
DTSTART:{ref + relativedelta(day=9, month=5)}T094500
DTEND:{ref + relativedelta(day=9, month=5)}T111500

DTFORMAT: DDMMYYYY
17/09 1800-2000
---
DTSTART:{ref + relativedelta(day=17, month=9)}T180000
DTEND:{ref + relativedelta(day=17, month=9)}T200000

DTFORMAT: DDMMYYYY
21/11 1230-1400
---
DTSTART:{ref + relativedelta(day=21, month=11)}T123000
DTEND:{ref + relativedelta(day=21, month=11)}T140000

DTFORMAT: DDMMYYYY
03/06 1700-1830
---
DTSTART:{ref + relativedelta(day=3, month=6)}T170000
DTEND:{ref + relativedelta(day=3, month=6)}T183000

DTFORMAT: MMDDYYYY
12/25
---
DTSTART:{ref + relativedelta(month=12, day=25)}
DTEND:{ref + relativedelta(month=12, day=25+1)}


DTFORMAT: MMDDYYYY
03/06 1700-1830
---
DTSTART:{ref + relativedelta(month=3, day=6)}T170000
DTEND:{ref + relativedelta(month=3, day=6)}T183000

DTFORMAT: MMDDYYYY
01/15 0900-1030
---
DTSTART:{ref + relativedelta(month=1, day=15)}T090000
DTEND:{ref + relativedelta(month=1, day=15)}T103000

DTFORMAT: MMDDYYYY
05/22 1400-1600
---
DTSTART:{ref + relativedelta(month=5, day=22)}T140000
DTEND:{ref + relativedelta(month=5, day=22)}T160000

DTFORMAT: MMDDYYYY
07/04 1200-1500
---
DTSTART:{ref + relativedelta(month=7, day=4)}T120000
DTEND:{ref + relativedelta(month=7, day=4)}T150000

DTFORMAT: MMDDYYYY
09/10 0800-0930
---
DTSTART:{ref + relativedelta(month=9, day=10)}T080000
DTEND:{ref + relativedelta(month=9, day=10)}T093000

DTFORMAT: MMDDYYYY
11/23 1600-1800
---
DTSTART:{ref + relativedelta(month=11, day=23)}T160000
DTEND:{ref + relativedelta(month=11, day=23)}T180000

DTFORMAT: MMDDYYYY
02/14 1900-2100
---
DTSTART:{ref + relativedelta(month=2, day=14)}T190000
DTEND:{ref + relativedelta(month=2, day=14)}T210000

DTFORMAT: MMDDYYYY
04/30 1000-1200
---
DTSTART:{ref + relativedelta(month=4, day=30)}T100000
DTEND:{ref + relativedelta(month=4, day=30)}T120000

DTFORMAT: MMDDYYYY
06/15 1300-1430
---
DTSTART:{ref + relativedelta(month=6, day=15)}T130000
DTEND:{ref + relativedelta(month=6, day=15)}T143000

DTFORMAT: MMDDYYYY
08/21 1500-1700
---
DTSTART:{ref + relativedelta(month=8, day=21)}T150000
DTEND:{ref + relativedelta(month=8, day=21)}T170000

DTFORMAT: MMDDYYYY
10/31 1800-2000
---
DTSTART:{ref + relativedelta(month=10, day=31)}T180000
DTEND:{ref + relativedelta(month=10, day=31)}T200000

DTFORMAT: MMDDYYYY
12/24 1700-1900
---
DTSTART:{ref + relativedelta(month=12, day=24)}T170000
DTEND:{ref + relativedelta(month=12, day=24)}T190000

DTFORMAT: MMDDYYYY
02/29 0930-1130
---
DTSTART:{ref + relativedelta(month=2, day=29)}T093000
DTEND:{ref + relativedelta(month=2, day=29)}T113000

DTFORMAT: MMDDYYYY
05/01 1100-1300
---
DTSTART:{ref + relativedelta(month=5, day=1)}T110000
DTEND:{ref + relativedelta(month=5, day=1)}T130000

DTFORMAT: MMDDYYYY
09/05 1400-1630
---
DTSTART:{ref + relativedelta(month=9, day=5)}T140000
DTEND:{ref + relativedelta(month=9, day=5)}T163000



in 2 days
---
DTSTART:{ref + relativedelta(days=2)}

in 2 days at 10am
---
DTSTART:{ref + relativedelta(days=2)}T100000

in 3 days
---
DTSTART:{ref + relativedelta(days=3)}

in 5 days at 2pm
---
DTSTART:{ref + relativedelta(days=5)}T140000

in 1 week
---
DTSTART:{ref + relativedelta(days=7)}

in 10 days at 9am
---
DTSTART:{ref + relativedelta(days=10)}T090000

in 2 weeks
---
DTSTART:{ref + relativedelta(weeks=2)}

in 2 weeks at 3pm
---
DTSTART:{ref + relativedelta(weeks=2)}T150000

in 1 month
---
DTSTART:{ref + relativedelta(months=1)}

in 1 month at 11am
---
DTSTART:{ref + relativedelta(months=1)}T110000

in 3 months
---
DTSTART:{ref + relativedelta(months=3)}

in 3 months at 4:30pm
---
DTSTART:{ref + relativedelta(months=3)}T163000

in 1 year
---
DTSTART:{ref + relativedelta(years=1)}

in 1 year on the 1st of june
---
DTSTART:{ref + relativedelta(years=1, day=1, month=6)}

in 5 years
---
DTSTART:{ref + relativedelta(years=5)}

in 18 months
---
DTSTART:{ref + relativedelta(months=18)}

DTFORMAT: DDMMYYYY
in 2y 1/08
---
DTSTART:{ref + relativedelta(years=2, day=1, month=8)}

DTFORMAT: MMDDYYYY
2y from now 12/27
---
DTSTART:{ref + relativedelta(years=2, month=12, day=27)}

DTFORMAT: DDMMYYYY
next year 17.05
---
DTSTART:{ref + relativedelta(years=1, day=17, month=5)}

DTFORMAT: MMDDYYYY
in 5 years 12/08
---
DTSTART:{ref + relativedelta(years=5, month=12, day=8)}

next tuesday
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TU)}

first mon of feb
---
DTSTART:{ref + relativedelta(month=2, day=1, weekday=MO(1))}

2nd tue of mar
---
DTSTART:{ref + relativedelta(month=3, day=1, weekday=TU(2))}

first wed of apr
---
DTSTART:{ref + relativedelta(month=4, day=1, weekday=WE(1))}

4th thu of may
---
DTSTART:{ref + relativedelta(month=5, day=1, weekday=TH(4))}

2nd fri of jun
---
DTSTART:{ref + relativedelta(month=6, day=1, weekday=FR(2))}

first sat of jul
---
DTSTART:{ref + relativedelta(month=7, day=1, weekday=SA(1))}

first sun of aug
---
DTSTART:{ref + relativedelta(month=8, day=1, weekday=SU(1))}

first mon of sep
---
DTSTART:{ref + relativedelta(month=9, day=1, weekday=MO(1))}

1st tue of oct
---
DTSTART:{ref + relativedelta(month=10, day=1, weekday=TU(1))}

wed 2nd of nov
---
DTSTART:{ref + relativedelta(month=11, day=2, weekday=WE(1))}

thu 3rd of dec
---
DTSTART:{ref + relativedelta(month=12, day=3, weekday=TH(1))}

fri 4th of jan
---
DTSTART:{ref + relativedelta(month=1, day=1, weekday=FR(1))}

first sat of feb
---
DTSTART:{ref + relativedelta(month=2, day=1, weekday=SA(1))}

first sun of mar
---
DTSTART:{ref + relativedelta(month=3, day=1, weekday=SU(1))}

first mon of apr
---
DTSTART:{ref + relativedelta(month=4, day=1, weekday=MO(1))}

3rd june
---
DTSTART:{ref + relativedelta(day=3, month=6)}

5th january
---
DTSTART:{ref + relativedelta(day=5, month=1)}

12th february
---
DTSTART:{ref + relativedelta(day=12, month=2)}

21st march
---
DTSTART:{ref + relativedelta(day=21, month=3)}

7th april
---
DTSTART:{ref + relativedelta(day=7, month=4)}

19th may
---
DTSTART:{ref + relativedelta(day=19, month=5)}

28th june
---
DTSTART:{ref + relativedelta(day=28, month=6)}

14th july
---
DTSTART:{ref + relativedelta(day=14, month=7)}

2nd august
---
DTSTART:{ref + relativedelta(day=2, month=8)}

30th september
---
DTSTART:{ref + relativedelta(day=30, month=9)}

11th october
---
DTSTART:{ref + relativedelta(day=11, month=10)}

25th november
---
DTSTART:{ref + relativedelta(day=25, month=11)}

17th december
---
DTSTART:{ref + relativedelta(day=17, month=12)}

8th january
---
DTSTART:{ref + relativedelta(day=8, month=1)}

16th february
---
DTSTART:{ref + relativedelta(day=16, month=2)}

23rd march
---
DTSTART:{ref + relativedelta(day=23, month=3)}

9th april
---
DTSTART:{ref + relativedelta(day=9, month=4)}

27th may
---
DTSTART:{ref + relativedelta(day=27, month=5)}

4th june
---
DTSTART:{ref + relativedelta(day=4, month=6)}

20th july
---
DTSTART:{ref + relativedelta(day=20, month=7)}

13th august
---
DTSTART:{ref + relativedelta(day=13, month=8)}

1st september
---
DTSTART:{ref + relativedelta(day=1, month=9)}

29th october
---
DTSTART:{ref + relativedelta(day=29, month=10)}

6th november
---
DTSTART:{ref + relativedelta(day=6, month=11)}

24th december
---
DTSTART:{ref + relativedelta(day=24, month=12)}

10th january
---
DTSTART:{ref + relativedelta(day=10, month=1)}

18th february
---
DTSTART:{ref + relativedelta(day=18, month=2)}

3rd march
---
DTSTART:{ref + relativedelta(day=3, month=3)}

15th april
---
DTSTART:{ref + relativedelta(day=15, month=4)}

22nd may
---
DTSTART:{ref + relativedelta(day=22, month=5)}

7th june
---
DTSTART:{ref + relativedelta(day=7, month=6)}

31st july
---
DTSTART:{ref + relativedelta(day=31, month=7)}

9th august
---
DTSTART:{ref + relativedelta(day=9, month=8)}

26th september
---
DTSTART:{ref + relativedelta(day=26, month=9)}

14th october
---
DTSTART:{ref + relativedelta(day=14, month=10)}

2nd november
---
DTSTART:{ref + relativedelta(day=2, month=11)}

19th december
---
DTSTART:{ref + relativedelta(day=19, month=12)}

6th january
---
DTSTART:{ref + relativedelta(day=6, month=1)}

23rd february
---
DTSTART:{ref + relativedelta(day=23, month=2)}

11th march
---
DTSTART:{ref + relativedelta(day=11, month=3)}

28th april
---
DTSTART:{ref + relativedelta(day=28, month=4)}

5th may
---
DTSTART:{ref + relativedelta(day=5, month=5)}

17th june
---
DTSTART:{ref + relativedelta(day=17, month=6)}

24th july
---
DTSTART:{ref + relativedelta(day=24, month=7)}

8th august
---
DTSTART:{ref + relativedelta(day=8, month=8)}

20th september
---
DTSTART:{ref + relativedelta(day=20, month=9)}

3rd october
---
DTSTART:{ref + relativedelta(day=3, month=10)}

16th november
---
DTSTART:{ref + relativedelta(day=16, month=11)}

29th december
---
DTSTART:{ref + relativedelta(day=29, month=12)}

7th january
---
DTSTART:{ref + relativedelta(day=7, month=1)}

14th february
---
DTSTART:{ref + relativedelta(day=14, month=2)}

21st march
---
DTSTART:{ref + relativedelta(day=21, month=3)}

4th april
---
DTSTART:{ref + relativedelta(day=4, month=4)}

18th may
---
DTSTART:{ref + relativedelta(day=18, month=5)}

25th june
---
DTSTART:{ref + relativedelta(day=25, month=6)}

12th july
---
DTSTART:{ref + relativedelta(day=12, month=7)}

30th august
---
DTSTART:{ref + relativedelta(day=30, month=8)}

9th september
---
DTSTART:{ref + relativedelta(day=9, month=9)}

27th october
---
DTSTART:{ref + relativedelta(day=27, month=10)}

13th november
---
DTSTART:{ref + relativedelta(day=13, month=11)}

1st december
---
DTSTART:{ref + relativedelta(day=1, month=12)}

19th january
---
DTSTART:{ref + relativedelta(day=19, month=1)}

5th february
---
DTSTART:{ref + relativedelta(day=5, month=2)}

22nd march
---
DTSTART:{ref + relativedelta(day=22, month=3)}

10th april
---
DTSTART:{ref + relativedelta(day=10, month=4)}

28th may
---
DTSTART:{ref + relativedelta(day=28, month=5)}

15th june
---
DTSTART:{ref + relativedelta(day=15, month=6)}

3rd july
---
DTSTART:{ref + relativedelta(day=3, month=7)}

21st august
---
DTSTART:{ref + relativedelta(day=21, month=8)}

7th september
---
DTSTART:{ref + relativedelta(day=7, month=9)}

24th october
---
DTSTART:{ref + relativedelta(day=24, month=10)}

11th november
---
DTSTART:{ref + relativedelta(day=11, month=11)}

29th december
---
DTSTART:{ref + relativedelta(day=29, month=12)}

16th january
---
DTSTART:{ref + relativedelta(day=16, month=1)}

2nd february
---
DTSTART:{ref + relativedelta(day=2, month=2)}

20th march
---
DTSTART:{ref + relativedelta(day=20, month=3)}

8th april
---
DTSTART:{ref + relativedelta(day=8, month=4)}

25th may
---
DTSTART:{ref + relativedelta(day=25, month=5)}

13th june
---
DTSTART:{ref + relativedelta(day=13, month=6)}

30th july
---
DTSTART:{ref + relativedelta(day=30, month=7)}

17th august
---
DTSTART:{ref + relativedelta(day=17, month=8)}

4th september
---
DTSTART:{ref + relativedelta(day=4, month=9)}

22nd october
---
DTSTART:{ref + relativedelta(day=22, month=10)}

9th november
---
DTSTART:{ref + relativedelta(day=9, month=11)}

27th december
---
DTSTART:{ref + relativedelta(day=27, month=12)}

14th january
---
DTSTART:{ref + relativedelta(day=14, month=1)}

1st february
---
DTSTART:{ref + relativedelta(day=1, month=2)}

19th march
---
DTSTART:{ref + relativedelta(day=19, month=3)}

6th april
---
DTSTART:{ref + relativedelta(day=6, month=4)}

23rd may
---
DTSTART:{ref + relativedelta(day=23, month=5)}

10th june
---
DTSTART:{ref + relativedelta(day=10, month=6)}

28th july
---
DTSTART:{ref + relativedelta(day=28, month=7)}

15th august
---
DTSTART:{ref + relativedelta(day=15, month=8)}

2nd september
---
DTSTART:{ref + relativedelta(day=2, month=9)}

20th october
---
DTSTART:{ref + relativedelta(day=20, month=10)}

7th november
---
DTSTART:{ref + relativedelta(day=7, month=11)}

25th december
---
DTSTART:{ref + relativedelta(day=25, month=12)}

12th january
---
DTSTART:{ref + relativedelta(day=12, month=1)}

29th february
---
DTSTART:{ref + relativedelta(day=29, month=2)}

17th march
---
DTSTART:{ref + relativedelta(day=17, month=3)}

4th april
---
DTSTART:{ref + relativedelta(day=4, month=4)}

21st may
---
DTSTART:{ref + relativedelta(day=21, month=5)}

8th june
---
DTSTART:{ref + relativedelta(day=8, month=6)}

26th july
---
DTSTART:{ref + relativedelta(day=26, month=7)}

13th august
---
DTSTART:{ref + relativedelta(day=13, month=8)}

30th september
---
DTSTART:{ref + relativedelta(day=30, month=9)}

18th october
---
DTSTART:{ref + relativedelta(day=18, month=10)}

5th november
---
DTSTART:{ref + relativedelta(day=5, month=11)}

23rd december
---
DTSTART:{ref + relativedelta(day=23, month=12)}

june 3
---
DTSTART:{ref + relativedelta(day=3, month=6)}

15th july
---
DTSTART:{ref + relativedelta(day=15, month=7)}

july 15
---
DTSTART:{ref + relativedelta(day=15, month=7)}

22nd august
---
DTSTART:{ref + relativedelta(day=22, month=8)}

august 22
---
DTSTART:{ref + relativedelta(day=22, month=8)}

10th september
---
DTSTART:{ref + relativedelta(day=10, month=9)}

september 10
---
DTSTART:{ref + relativedelta(day=10, month=9)}

5th october
---
DTSTART:{ref + relativedelta(day=5, month=10)}

october 5
---
DTSTART:{ref + relativedelta(day=5, month=10)}

18th november
---
DTSTART:{ref + relativedelta(day=18, month=11)}

november 18
---
DTSTART:{ref + relativedelta(day=18, month=11)}

25th december
---
DTSTART:{ref + relativedelta(day=25, month=12)}

december 25
---
DTSTART:{ref + relativedelta(day=25, month=12)}

1st jan 1245-1415
---
DTSTART:{ref + relativedelta(day=1, month=1)}T124500
DTEND:{ref + relativedelta(day=1, month=1)}T141500

2 oct 10-12
---
DTSTART:{ref + relativedelta(day=2, month=10)}T100000
DTEND:{ref + relativedelta(day=2, month=10)}T120000




for 1hr
---
DTSTART:{ref}
DURATION:PT1H

for 1.5hrs
---
DTSTART:{ref}
DURATION:PT1H30M

for 3hrs
---
DTSTART:{ref}
DURATION:PT3H

for 2hrs
---
DTSTART:{ref}
DURATION:PT2H

for 45min
---
DTSTART:{ref}
DURATION:PT45M

for 30min
---
DTSTART:{ref}
DURATION:PT30M

for 2.5hrs
---
DTSTART:{ref}
DURATION:PT2H30M

for 4hrs
---
DTSTART:{ref}
DURATION:PT4H

for 90min
---
DTSTART:{ref}
DURATION:PT1H30M

for 15min
---
DTSTART:{ref}
DURATION:PT15M

for 5hrs
---
DTSTART:{ref}
DURATION:PT5H

for 75min
---
DTSTART:{ref}
DURATION:PT75M

for 3.5hrs
---
DTSTART:{ref}
DURATION:PT3H30M

for 20min
---
DTSTART:{ref}
DURATION:PT20M

for 6hrs
---
DTSTART:{ref}
DURATION:PT6H

every 10 minutes between 2 and 7pm
---
DTSTART:{ref + relativedelta(hour=14)}T140000
RRULE:FREQ=MINUTELY;INTERVAL=10;UNTIL:{ref + relativedelta(hour=19)}T190000

between 3 and 4
---
DTSTART:{ref + relativedelta(hour=3)}T030000
DTEND:{ref + relativedelta(hour=4)}T040000

10 tomorrow
---
DTSTART:{ref + relativedelta(days=1)}T100000

tues at 1
---
DTSTART:{ref + relativedelta(weekday=TU)}T010000

tues at 1am
---
DTSTART:{ref + relativedelta(weekday=TU)}T010000

from 6 til 8pm
---
DTSTART:{ref + relativedelta(hour=18)}T180000
DTEND:{ref + relativedelta(hour=20)}T200000

remind 30m before 10am
---
DTSTART:{ref + relativedelta(hour=10)}T100000
VALARM:TRIGGER:-PT30M

from new years day 9am repeat daily
---
DTSTART:{ref + relativedelta(month=1, day=1)}T090000
RRULE:FREQ=DAILY

next week friday 445pm
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}T164500

in 2 weeks 4 days
---
DTSTART:{ref + relativedelta(weeks=2, days=4)}

2 weeks today
---
DTSTART:{ref + relativedelta(weeks=2)}

monday next week
---
DTSTART:{ref + relativedelta(days=1, weekday=MO)}

thurs in 2 weeks
---
DTSTART:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=TH(2))}

next weekday
---
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}

weekdays 2-4pm
---
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T140000
DTEND:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T160000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR

every fri 2pm except next week
---
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T140000
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + relativedelta(days=1, weekday=MO) + relativedelta(weekday=FR)}

hourly from 9am to 5pm weekdays
---
DTSTART:{ref + relativedelta( (days=1) if ref.weekday == SA else (weekday=SA))}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={range(9, 17)}

weekends 10am-12pm
---
DTSTART:{ref + relativedelta((days=1) if ref.weekday == SA else (weekday=SA))}T100000
DTEND:{ref + relativedelta((days=1) if ref.weekday == SA else (weekday=SA))}T120000


1wk from now
---
DTSTART:{ref + relativedelta(weeks=1)}

2wk thursday 10am
---
DTSTART:{ref + relativedelta(weekday=TH, weeks=2)}T100000

tmrw 10am
---
DTSTART:{ref + relativedelta(days=1)}T100000

next week
---
DTSTART:{ref + relativedelta(days=1, weekday=MO)}


DTFORMAT: DDMMYYYY
14/06
---
DTSTART:{ref + relativedelta(day=14, month=6)}


noon
---
DTSTART:{ref + relativedelta(hour=12)}T120000

DTFORMAT: MMDDYYYY
12/30 noon
---
DTSTART:{ref + relativedelta(day=30, month=12)}T120000

noon fri
---
DTSTART:{ref + relativedelta(weekday=FR)}T120000

1230
---
DTSTART:{ref + relativedelta(hour=12, minute=30)}T123000

Q1 26
---
DTSTART:{datetime(2026, 1,1) + relativedelta(weekday=MO)}

Q4
---
DTSTART:{ref + relativedelta(month=10, weekday=MO)}

Q2 2029
---
DTSTART:{datetime(2029, 4,1) + relativedelta(weekday=MO)}

weekdays minus thursday
---
DTSTART:{ref + relativedelta(**(
    {'days': 2} if ref.weekday() == WEDNESDAY else
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO }
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,FR

thursdays, mondays and saturdays
---
DTSTART:{ref + relativedelta(**(
    {'weekday': TH} if ref.weekday() < THURSDAY else
    {'weekday': SA} if ref.weekday() < SATURDAY else
    {'weekday': MO}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO,TH,SA

weekends and wednesdays
---
DTSTART:{ref + relativedelta(**(
    {'weekday': WE} if ref.weekday() < WEDNESDAY else
    {'weekday': SA} if ref.weekday() < SATURDAY else
    {'weekday': SU} if ref.weekday() < SUNDAY else
    {'weekday': WE}
))}
RRULE:FREQ=WEEKLY;BYDAY=WE,SA,SU

every tues and every other mon
---
DTSTART:{ref + relativedelta(**(
    {'weekday': TU} if ref.weekday() < TUESDAY else
    {'weekday': MO} if ref.weekday() < MONDAY else
    {'weekday': TU}
))}
RRULE:FREQ=WEEKLY;BYDAY=MO;INTERVAL=2;BYDAY=TU;


nov 6,7,8 annually 10-12pm
---
DTSTART:{ref + relativedelta(month=11, day=6)}T100000
DTEND:{ref + relativedelta(month=11, day=6)}T120000
RRULE:FREQ=YEARLY;BYMONTH=11;BYMONTHDAY=6,7,8

july 10-14 annually 10-12pm
---
DTSTART:{ref + relativedelta(month=7, day=10)}T100000
DTEND:{ref + relativedelta(month=7, day=14)}T120000
RRULE:FREQ=YEARLY;BYMONTH=7;BYMONTHDAY=10,11,12,13,14


nov 6-8
---
DTSTART:{ref + relativedelta(month=11, day=6)}
DTEND:{ref + relativedelta(month=11, day=8)}T235959


every tues except last week of month
---
DTSTART:{ref + relativedelta(weekday=TU)}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + relativedelta(day=31,weekday=TU(-1))}


first mon of next quarter
---
DTSTART:{ref.replace(day=1) + relativedelta(months=4 - month % 3) + relativedelta(weekday=MO)}


friday on the last week of the quarter
---
DTSTART:{ref + relativedelta(months=3 - month % 3, day = 31, weekday=FR(-1))}


the beginning of Q1 Q3 1500
---
DTSTART:{ref + relativedelta(months=3- month % 3, day = 1)}T150000
RDATE:{ref + relativedelta(months=3 - month % 3, day = 1)}


the first mon of Q1-4 10:40
---
DTSTART:{ref.replace(month=1, day=1)}T104000
RDATE:{ref.replace(month=4, day=1)}
RDATE:{ref.replace(month=7, day=1)}
RDATE:{ref.replace(month=10, day=1)}

the second mon of Q1-4 8-9am every year
---
DTSTART:{ref.replace(month=1, day=1) + relativedelta(weekday=MO(2))}T080000
RRULE:FREQ=YEARLY;BYMONTH=1,4,7,10;BYDAY=MO;BYSETPOS=2

quarterly 9am mon on first week
---
DTSTART:{ref.replace(month=1, day=1) + relativedelta(weekday=MO)}T090000
RRULE:FREQ=YEARLY;BYMONTH=1,4,7,10;BYDAY=MO;BYSETPOS=1

Q2 w3 tuesday 10am
---
DTSTART:{ref + relativedelta(month=4, day=1) + relativedelta(weekday=TU(3))}T100000


last sunday of every month
---
DTSTART:{ref + relativedelta(day = 31, weekday=SU(-1))}
RRULE:FREQ=MONTHLY;BYDAY=-1SU

aug 9th 7pm rem 1hr
---
DTSTART:{ref + relativedelta(day=9, month=8)}T190000
VALARM:TRIGGER:-PT1H

last sun feb 0800 2hrs
---
DTSTART:{ref + relativedelta(month=2, day=31, weekday=SU(-1))}T080000
DURATION:PT2H

last fri of june 1pm
---
DTSTART:{ref + relativedelta(month=6, day=31, weekday=FR(-1))}T130000

in 4hrs
---
DTSTART:{ref + relativedelta(hours=4)}

GMT+1 1200
---
DTSTART:{ref + relativedelta(hour=12)}T120000
TZOFFSETFROM:+0000
TZOFFSETTO:+0100

EST+5
---
DTSTART:{ref + relativedelta(hour=5)}T050000
TZOFFSETFROM:-0500
TZOFFSETTO:-0400

2:38pm in hawaii
---
DTSTART;TZID=Pacific/Honolulu:{ref + relativedelta(hour=14, minute=38)}T143800


8pm EST
---
DTSTART;TZID=America/New_York:{ref + relativedelta(hour=20)}T200000

9:19am madrid time
---
DTSTART;TZID=Europe/Madrid:{ref + relativedelta(hour=9, minute=19)}

2pm chile time
---
DTSTART;TZID=America/Santiago:{ref + relativedelta(hour=14)}T140000

1745+0800
---
DTSTART:{ref + relativedelta(hour=17, minute=45)}T174500
TZOFFSETTO:+0800

3 jan 2pm 1hr
---
DTSTART:{ref + relativedelta(day=3, month=1)}T140000
DURATION:PT1H

every mon 0700 45mins
---
DTSTART:{ref + relativedelta(weekday=MO)}T070000
DURATION:PT45M

fri night 8pm till 10:30
---
DTSTART:{ref + relativedelta(weekday=FR)}T200000
DTEND:{ref + relativedelta(weekday=FR)}T223000

every tues unless 1st week of month
---
DTSTART:{ref + relativedelta(weekday=TU)}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + relativedelta(day=1,weekday=TU)}

every other sat 10-12pm
---
DTSTART:{ref + relativedelta(weekday=SA)}T100000
DTEND:{ref + relativedelta(weekday=SA)}T120000
RRULE:FREQ=WEEKLY;BYDAY=SA;INTERVAL=2

every 20 minutes from 3 to 4pm
---
DTSTART:{ref + relativedelta(hour=15)}T150000
RRULE:FREQ=MINUTELY;INTERVAL=20;UNTIL:{ref + relativedelta(hour=16)}


every 15 minutes from 1600-1800 on weekdays
---
DTSTART:{ref + relativedelta( weekday = MO|TU|WE|TH|FR)}T160000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYMINUTE=0,15,30,45

1033 then every 20m until 5pm weekdays
---
DTSTART:{ref + relativedelta( weekday = MO|TU|WE|TH|FR)}T103300
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR={range(10, 17)};BYMINUTE=13,33,53;


in 10m
---
DTSTART:{ref + relativedelta(minutes=10)}

wkly 7pm mon
---
DTSTART:{ref + relativedelta(weekday=MO)}T190000
RRULE:FREQ=WEEKLY;BYDAY=MO;

15 past the hour every hour from 9-5pm weekdays
---
DTSTART:{ref + relativedelta( weekday = MO|TU|WE|TH|FR)}T091500
RRULE:FREQ=HOURLY;BYMINUTE=15;COUNT={17-9};

every 5 days from now except last 2 weeks of feb
---
DTSTART:{ref + relativedelta(days=5)}
RRULE:FREQ=DAILY;INTERVAL=5;EXDATE:{ref + relativedelta(month=2, day=28, weekday=TU(-2))}

weekly from 9am today til 5pm in 2 fridays
---
DTSTART:{ref}T090000
RRULE:FREQ=WEEKLY;UNTIL:{ref + relativedelta(weekday=FR(2), hour=17)}

weekly on friday from 18 jun til 20 oct
---
DTSTART:{ref + relativedelta(weekday=FR, month=6, day=18)}
RRULE:FREQ=WEEKLY;BYDAY=FR;UNTIL:{ref + relativedelta(month=10, day=20)}

every 2 days for 10 weeks
---
DTSTART:{ref + relativedelta(days=2)}
RRULE:FREQ=DAILY;INTERVAL=2;UNTIL:{ref + relativedelta(weeks=10)}

3pm tuesdays for 2mo
---
DTSTART:{ref + relativedelta(weekday=TU)}T150000
RRULE:FREQ=WEEKLY;BYDAY=TU;UNTIL:{ref + relativedelta(months=2)}

every other weekend after jul 1st
---
DTSTART:{ref + relativedelta(month=7, day=1)}
RRULE:FREQ=WEEKLY;BYDAY=SA,SU;INTERVAL=2

every 2nd weekday
---
DTSTART:{ref + relativedelta(weekday=MO)}
RRULE:FREQ=WEEKLY;BYDAY=TU,WE,TH;INTERVAL=2

every 2nd weekend
---
DTSTART:{ref + relativedelta(weekday=SA)}
RRULE:FREQ=WEEKLY;BYDAY=SA,SU;INTERVAL=2

every tu for 10 times
---
DTSTART:{ref + relativedelta(weekday=TU)}
RRULE:FREQ=WEEKLY;BYDAY=TU;COUNT={10}

every other day for 19 times
---
DTSTART:{ref + relativedelta(days=2)}
RRULE:FREQ=DAILY;INTERVAL=2;COUNT={19}

daily 8am
---
DTSTART:{ref + relativedelta(hour=8)}
RRULE:FREQ=DAILY

halloween 9pm
---
DTSTART:{ref + relativedelta(month=10, day=31)}T210000

christmas eve 2pm
---
DTSTART:{ref + relativedelta(month=12, day=24)}T140000

every christmas eve
---
DTSTART:{ref + relativedelta(month=12, day=24)}
RRULE:FREQ=YEARLY;BYMONTH=12;BYMONTHDAY=24

sat 9am, sun 10am, tue 330pm remind 15m before
---
DTSTART:{ref + relativedelta(weekday=SA)}T090000
RDATE:{ref + relativedelta(weekday=SU)}T100000
RDATE:{ref + relativedelta(weekday=TU)}T153000
VALARM:TRIGGER:-PT15M

every 3rd sat of month 9am
---
DTSTART:{ref + relativedelta(day=1, weekday=SA(3))}T090000
RRULE:FREQ=MONTHLY;BYDAY=SA;BYSETPOS=3

the last weekend of the month 10am
---
DTSTART:{ref + relativedelta(day=31, weekday=SU(-1)|SA(-1))}T100000

last workday of every month 10am
---
DTSTART:{ref + relativedelta(day=31, weekday=FR(-1)|TH(-1)|TU(-1)|WE(-1)|MO(-1))}T100000
RRULE:FREQ=MONTHLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=-1

3rd sat of this month 1035
---
DTSTART:{ref.replace(day=1) + relativedelta(weekday=SA(3))}T103500

sem 1 start sept 15
sem 1 week 3 tues 1010
---
DTSTART:{ref.replace(month=9, day=15) + relativedelta(weekday=TU(3))}T101000

this is the 3rd week of sem 1
week 5 tues 1149-1300
---
DTSTART:{ref - relativedelta(weeks=2, weekday=MO(-1)) + relativedelta(weekday=TU(5))}T114900
DTEND:{ref - relativedelta(weeks=2, weekday=MO(-1)) + relativedelta(weekday=TU(5))}T130000

fiscal year starts apr 5
fiscal week 32 wed 1530
---
DTSTART:{ref.replace(month=4, day=5) + relativedelta(weekday=WE(32))}T153000


fiscal year start apr 1
first mon of FY28
---
DTSTART:{ref.replace(year=2028, month=4, day=1) + relativedelta(weekday=MO)}

fiscal year start jan 1
every second wed of this fiscal year
---
DTSTART:{ref.replace(month=1, day=1) + relativedelta(weekday=WE(2))}




