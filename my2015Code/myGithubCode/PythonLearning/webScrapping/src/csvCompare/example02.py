import datetime
# http://stackoverflow.com/questions/1622038/find-mondays-date-with-python
today = datetime.date.today()

print today

print today + datetime.timedelta(days=-today.weekday(), weeks=1)

print str(today), type(str(today))