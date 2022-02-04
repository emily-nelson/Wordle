import datetime

a = datetime.datetime.today().date()
numdays = 10
date_list = [a + datetime.timedelta(days=x) for x in range(numdays)]
#print(date_list[1].strftime('%d, %m, %Y'))
dates = [date.strftime('%d, %m, %Y') for date in date_list]
print(dates)