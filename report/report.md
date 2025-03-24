# Finetuning a small language model to reason about dates and times

## Abstract

Language models are being increasingly integrated into normal life, and are increasingly expected to perform real world tasks. One task that people engage in daily is scheduling. State-of-the-art models are capable of reasoning about temporal relationships with high accuracy, but in this paper we explore the capability of much smaller locally run models to provide useful performance understanding scheduling phrases in the English language.

## Introduction

iCalendar (iCal) is an open plaintext format for describing calendar event information. It provides a platform to describe common temporal relationships in a flexible manner, and is widely supported in applications such as Outlook and Google Calendar.

Given the wide base of support for iCal, it is a robust domain specific language for describing many kinds of temporal relationships.
For example, a simple iCalendar event might look like this:

```
BEGIN:VEVENT
DTSTART:20240101T000000
DTEND:20240101T010000
SUMMARY:New Year's Day Celebrations
END:VEVENT
```

iCalendar can also describe very complex temporal relationships, such as:

```
BEGIN:VEVENT
DTSTART:20260301T120000
DTEND:20260301T130000
SUMMARY: Engineer Design Review
RRULE:FREQ=YEARLY;BYHOUR=12,16;BYMINUTE=0;BYDAY=1TU,3TU;BYMONTH=3,4,5;
EXDATE:20260308T120000,20260315T120000,20260322T120000
END:VEVENT
```

Where the event occurs at 12:00 and 16:00 on the first and third Tuesday of March, April and May, except for March 8th, 15th and 22nd of 2026.

Support for such complex expressions has varying support in commercial software, but as iCal is an open standard, we can ensure that our output will be correct and to the greatest extent compatible with existing software, without modification.


We foresee a few applications that a small model like this could be applied to:

- Message/email client calendar integrations
- NL calendar input
- Improving voice assistant scheduling capability and accuracy

LLMs are increasingly being used to assist with scheduling tasks, but they are not yet capable of interpreting the wide variety of scheduling phrases to the same standard as a human. Many LLMs have a propensity to use corporate, American, formal English due to their fine-tuning, and perform variably on understanding colloquial and shorthand phrases.


## Task and dataset

The task we propose is to convert a natural English phrase such as "wed 3pm 02/02" or "2 weeks from now" into a rigorous and machine readable format.

No dataset exists for the given task. We have researched similar datasets, but these are of limited use and quality. As such we created our own fine-tuning dataset using a LLM - assisted data generation strategy.

Building from a taxonomy

Use of intermediate syntax 

- We found in initial experiments that untrained first shot accuracy increased with the use of a basic intermediate syntax for relative date calculations due to the model not having encoded all of the irregularity in the Gregorian date system, we decided to take this forward in our data generation approach.

Because of the relatively restricted input space, we can effectively enumerate the majority of inputs

Because there are a limited number of common ways to express scheduling phrases, we began with a taxonomy of examples, by expressing every single phrasing we would like to support.

# Taxonomy of scheduling phrases
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

### SPECIAL CASES - CONTEXT DEPENDENT
first mon of next quarter
fiscal week 32 wed 1530
Q2 w3 tuesday 10am
sem 1 week 3 tues 1010

### COMPLEX CONDITIONAL LOGIC
next weekday
weekends 10am-12pm
every 15 minutes from 1600-1800 on weekdays
every 2nd weekday





## Method

### Dataset Iteration

Dataset development was a core feature of our project, the dataset had to meet the following criterion:



### Pre-training with iCalendar specification (RFC5545)

https://www.rfc-editor.org/rfc/rfc5545.txt





## Experiments

## Related work

## Conclusion
