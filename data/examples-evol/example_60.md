every tues except last week of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=31,weekday=TU(-1))}
every monday except first week of month
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(day=1,weekday=MO(1))}

wednesdays except last wed of month
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(day=31,weekday=WE(-1))}

thursdays except week 2 of month
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(day=8,weekday=TH(2))}

every fri except third week of month
DTSTART:{ref + reldate(weekday=FR(1))}
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(day=15,weekday=FR(3))}

sat recurring except week 4 of month
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(day=31,weekday=SA(-1))}

sundays except week one of month
DTSTART:{ref + reldate(weekday=SU(1))}
RRULE:FREQ=WEEKLY;BYDAY=SU;EXDATE:{ref + reldate(day=1,weekday=SU(1))}

every mon except week four of month
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(day=22,weekday=MO(4))}

tuesdays except week 1 of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=1,weekday=TU(1))}

every wed except week two of month
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(day=8,weekday=WE(2))}

thursdays except last week of month
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(day=31,weekday=TH(-1))}

every friday except week 3 of month
DTSTART:{ref + reldate(weekday=FR(1))}
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(day=15,weekday=FR(3))}

saturdays except second week of month
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(day=8,weekday=SA(2))}

every sun except week 4 of month
DTSTART:{ref + reldate(weekday=SU(1))}
RRULE:FREQ=WEEKLY;BYDAY=SU;EXDATE:{ref + reldate(day=22,weekday=SU(4))}

mondays except last mon of month
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(day=31,weekday=MO(-1))}

every tue except first tuesday of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=1,weekday=TU(1))}

wednesdays except 3rd wed of month
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(day=15,weekday=WE(3))}

every thur except second thursday of month
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(day=8,weekday=TH(2))}

fridays except fourth fri of month
DTSTART:{ref + reldate(weekday=FR(1))}
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(day=22,weekday=FR(4))}

every sat except last saturday of month
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(day=31,weekday=SA(-1))}

sundays except 1st sun of month
DTSTART:{ref + reldate(weekday=SU(1))}
RRULE:FREQ=WEEKLY;BYDAY=SU;EXDATE:{ref + reldate(day=1,weekday=SU(1))}

every monday except third mon of month
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(day=15,weekday=MO(3))}

tuesdays except 4th tue of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=22,weekday=TU(4))}

every wed except first wednesday of month
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(day=1,weekday=WE(1))}

thursdays except 3rd thurs of month
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(day=15,weekday=TH(3))}

every friday except last friday of month
DTSTART:{ref + reldate(weekday=FR(1))}
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(day=31,weekday=FR(-1))}

saturdays except first sat of month
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(day=1,weekday=SA(1))}

every sun except second sunday of month
DTSTART:{ref + reldate(weekday=SU(1))}
RRULE:FREQ=WEEKLY;BYDAY=SU;EXDATE:{ref + reldate(day=8,weekday=SU(2))}

mondays except 2nd mon of month
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(day=8,weekday=MO(2))}

every tue except fourth tuesday of month
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(day=22,weekday=TU(4))}

wednesdays except last wed of month
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(day=31,weekday=WE(-1))}

every thur except first thursday of month
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(day=1,weekday=TH(1))}

fridays except 3rd fri of month
DTSTART:{ref + reldate(weekday=FR(1))}
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(day=15,weekday=FR(3))}

every sat except second saturday of month
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(day=8,weekday=SA(2))}

every sat except second saturday of feb
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(month=2,day=8,weekday=SA(2))}

every mon except third monday of jan
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(month=1,day=15,weekday=MO(3))}

tuesdays except 1st tue of mar
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(month=3,day=1,weekday=TU(1))}

every wed except fourth wednesday of apr
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(month=4,day=22,weekday=WE(4))}

thursdays except last thurs of may
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(month=5,day=31,weekday=TH(-1))}

every friday except second friday of jun
DTSTART:{ref + reldate(weekday=FR(1))}
RRULE:FREQ=WEEKLY;BYDAY=FR;EXDATE:{ref + reldate(month=6,day=8,weekday=FR(2))}

saturdays except 3rd sat of jul
DTSTART:{ref + reldate(weekday=SA(1))}
RRULE:FREQ=WEEKLY;BYDAY=SA;EXDATE:{ref + reldate(month=7,day=15,weekday=SA(3))}

every sun except week 1 of aug
DTSTART:{ref + reldate(weekday=SU(1))}
RRULE:FREQ=WEEKLY;BYDAY=SU;EXDATE:{ref + reldate(month=8,day=1,weekday=SU(1))}

mondays except 4th mon of sep
DTSTART:{ref + reldate(weekday=MO(1))}
RRULE:FREQ=WEEKLY;BYDAY=MO;EXDATE:{ref + reldate(month=9,day=22,weekday=MO(4))}

every tue except last tuesday of oct
DTSTART:{ref + reldate(weekday=TU(1))}
RRULE:FREQ=WEEKLY;BYDAY=TU;EXDATE:{ref + reldate(month=10,day=31,weekday=TU(-1))}

wednesdays except 2nd wed of nov
DTSTART:{ref + reldate(weekday=WE(1))}
RRULE:FREQ=WEEKLY;BYDAY=WE;EXDATE:{ref + reldate(month=11,day=8,weekday=WE(2))}

every thur except 22nd of dec
DTSTART:{ref + reldate(weekday=TH(1))}
RRULE:FREQ=WEEKLY;BYDAY=TH;EXDATE:{ref + reldate(month=12,day=22)}
