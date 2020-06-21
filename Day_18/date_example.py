from datetime import *

cdate = datetime.now()
print(cdate)

print(cdate.year)
print(cdate.month)
print(cdate.day)

print (cdate.strftime("weekday short: %a"))
print (cdate.strftime("weekday full: %A"))
print (cdate.strftime("weekday number: %w"))

print (cdate.strftime("day of month: %d"))
print (cdate.strftime("month short: %b"))
print (cdate.strftime("month full: %B"))
print (cdate.strftime("month number: %m"))

print (cdate.strftime("year short: %y"))
print (cdate.strftime("year full: %Y"))

print (cdate.strftime("hour 0-23: %H"))
print (cdate.strftime("hour 12: %I"))
print (cdate.strftime("AM/PM: %p"))
print (cdate.strftime("minute: %M"))
print (cdate.strftime("Second: %S"))

print (cdate.strftime("Date: %Y-%m-%d"))
print (cdate.strftime("Date: %B %d,%Y"))

print (cdate.strftime("Time: %H:%M:%S"))
print (cdate.strftime("Time: %I:%M:%S %p"))