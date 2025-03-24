first mon of next quarter
DTSTART:{ref.replace(day=1) + reldate(months=4 - month % 3) + reldate(weekday=MO)}
# finding the next quarter is a bit tricky, we need to find the next quarter from the current month, we could create a custom parameter for relative quarters to improve accuracy