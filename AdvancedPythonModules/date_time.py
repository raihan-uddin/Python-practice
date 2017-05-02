import datetime

t = datetime.time(5, 25, 10)
print(t)
print(type(t))
print(t.hour)
print(t.minute)

print(datetime.time.min)
print(datetime.time.max)
# 23:59:59.999999

print(datetime.time.resolution)
# 0:00:00.000001

today = datetime.date.today()
print(today)
# 2017-05-02

print(today.timetuple())
# time.struct_time(tm_year=2017, tm_mon=5, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=122, tm_isdst=-1)

print(today.day)
print(today.month)


print(datetime.date.min)
# 0001-01-01

print(datetime.date.max)
# 9999-12-31

print(datetime.date.resolution)
# 1 day, 0:00:00

d1 = datetime.date(2015,3,11)
print(d1)
# 2015-03-11

d2 = d1.replace(year=1990)
print(d2)
# 1990-03-11


print(d1-d2)
# 9131 days, 0:00:00


mybirtday = datetime.date(1995, 12, 2)
currentDay = datetime.date.today()
print(currentDay - mybirtday)