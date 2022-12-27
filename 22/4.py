import datetime as dt

timedelta = int(input())
now = dt.date(2019, 9, 1)

new_date = dt.timedelta(days=timedelta) + now
print(new_date.day, new_date.month)
