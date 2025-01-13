import calendar

year = 2050

month = 1 #this means January

days_in_january = calendar.monthrange(year, month)[1]

seconds_in_january = days_in_january * 24 * 60 * 60

print(f"The number of seconds in January is{seconds_in_january}.")