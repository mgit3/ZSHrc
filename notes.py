
from datetime import datetime

moment = datetime.now()
path = '/home/roberto/Documents/notes/'
text = input('text: ')
name = input('name: ').replace(' ', '_')
name = name + "{:_%y%m%d_%H%M%p}".format(moment)
with open(f'{path}{name}.txt', 'w') as f:
    f.writelines(text)




#%a: Returns the first three characters of the weekday, e.g. Wed.
#%A: Returns the full name of the weekday, e.g. Wednesday.
#%B: Returns the full name of the month, e.g. September.
#%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
#%m: Returns the month as a number, from 01 to 12.
#%p: Returns AM/PM for time.
#%y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
#%f: Returns microsecond from 000000 to 999999.
#%Z: Returns the timezone.
#%z: Returns UTC offset.
#%j: Returns the number of the day in the year, from 001 to 366.
#%W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
#%U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
#%c: Returns the local date and time version.
#%x: Returns the local version of date.
#%X: Returns the local version of time.







