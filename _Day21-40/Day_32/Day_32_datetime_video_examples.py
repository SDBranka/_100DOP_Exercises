import datetime


now = datetime.datetime.now()
# print(f"now: {now}")
# print(type(now))      #datetime object
year = now.year
month = now.month
# print(f"year: {year}")
# print(type(year))     # int
# year, month, hour, minutes

print("#####")
# 0 == Monday
day_of_week = now.weekday()
print(f"day_of_week: {day_of_week}")

# a datetime object only requires year, month, and day, but more specific
# values may also be included
date_of_birth = datetime.datetime(year=1995, 
                                    month=12, 
                                    day=15, 
                                    hour=4
)
print(f"date_of_birth: {date_of_birth}")








