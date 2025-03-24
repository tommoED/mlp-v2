hourly from 9am to 5pm weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9,10,11,12,13,14,15,16

every hour from 10am to 3pm on weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T100000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=10,11,12,13,14

hourly 8am-4pm monday to friday
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T080000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=8,9,10,11,12,13,14

each hour from 7am until 2pm on weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T070000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7,8,9,10,11,12,13

hourly 11am-6pm mon-fri
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T110000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=11,12,13,14,15,16,17

every 30m from 9am to 12pm weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYMINUTE=0,30

hourly 2pm-6pm work days
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T140000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=14,15,16,17

hourly from noon to 4pm mon thru fri
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T120000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=12,13,14,15

every hour 8:30am to 2:30pm weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T083000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=8,9,10,11,12,13

hourly 10-7pm business days
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T100000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=10,11,12,13,14,15,16,17,18

each hour between 1pm and 5pm weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T130000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=13,14,15,16

hourly 9am-3pm mon-fri
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T090000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=9,10,11,12,13,14

every 60 min from 7am to 7pm workdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T070000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7,8,9,10,11,12,13,14,15,16,17,18

hourly 10:30am-4:30pm weekdays
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T103000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=10,11,12,13,14,15

every hour on the hour 8am-6pm mon-fri
DTSTART:{ref + reldate(**
    {'days': 1} if ref.weekday() < SATURDAY else
    {'weekday': MO(1)}
)}T080000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=8,9,10,11,12,13,14,15,16,17,18