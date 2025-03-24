sat 9am, sun 10am, tue 330pm remind 15m before
DTSTART:{ref + reldate(weekday=SA(1))}T090000
RDATE:{ref + reldate(weekday=SU(1))}T100000
RDATE:{ref + reldate(weekday=TU(1))}T153000
VALARM:TRIGGER:-PT15M

mon 8am, wed 2pm and fri 5pm r-10m
DTSTART:{ref + reldate(weekday=MO(1))}T080000
RDATE:{ref + reldate(weekday=WE(1))}T140000
RDATE:{ref + reldate(weekday=FR(1))}T170000
VALARM:TRIGGER:-PT10M

7am tue, 11am thu, 4pm sat r-30m
DTSTART:{ref + reldate(weekday=TU(1))}T070000
RDATE:{ref + reldate(weekday=TH(1))}T110000
RDATE:{ref + reldate(weekday=SA(1))}T160000
VALARM:TRIGGER:-PT30M

6am mon, 9am wed, 3pm fri r-15m
DTSTART:{ref + reldate(weekday=MO(1))}T060000
RDATE:{ref + reldate(weekday=WE(1))}T090000
RDATE:{ref + reldate(weekday=FR(1))}T150000
VALARM:TRIGGER:-PT15M

8am tue, 12pm thu, 5pm sun r-20m
DTSTART:{ref + reldate(weekday=TU(1))}T080000
RDATE:{ref + reldate(weekday=TH(1))}T120000
RDATE:{ref + reldate(weekday=SU(1))}T170000
VALARM:TRIGGER:-PT20M

5:30am wed, 10:30am fri, 2:30pm mon r-25m
DTSTART:{ref + reldate(weekday=WE(1))}T053000
RDATE:{ref + reldate(weekday=FR(1))}T103000
RDATE:{ref + reldate(weekday=MO(1))}T143000
VALARM:TRIGGER:-PT25M

9am thu, 1pm sat, 6pm tue r-10m
DTSTART:{ref + reldate(weekday=TH(1))}T090000
RDATE:{ref + reldate(weekday=SA(1))}T130000
RDATE:{ref + reldate(weekday=TU(1))}T180000
VALARM:TRIGGER:-PT10M

7:30am fri, 11:30am sun, 4:30pm wed r-5m
DTSTART:{ref + reldate(weekday=FR(1))}T073000
RDATE:{ref + reldate(weekday=SU(1))}T113000
RDATE:{ref + reldate(weekday=WE(1))}T163000
VALARM:TRIGGER:-PT5M
