import calendar
import datetime
import time
print()
print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 3))
print()

print(calendar.monthcalendar(2020, 3))
print()

print(calendar.calendar(2020))
print()

print()
day_of_the_week = calendar.weekday(2020, 3, 8)
print(day_of_the_week)

print()
is_leap = calendar.isleap(2020)
print(is_leap)

print()
how_many_leap_days = calendar.leapdays(2020, 2021)
print(how_many_leap_days)
