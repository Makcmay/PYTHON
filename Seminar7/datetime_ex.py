# from datetime import datetime
import datetime
'''
Дельта между двумя датами
'''
#
# date_1 = datetime.datetime(year=2020, month=12, day=5)
# date_2 = datetime.datetime(year=2018, month=12, day=5)
# date_delta = date_1 - date_2
# print(date_delta.days)

'''
В секундах
'''

# datetime_1 = datetime.datetime(year=2020, month=12, day=5, hour=18, minute=57, second=30)
# datetime_2 = datetime.datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
# datetime_delta = datetime_1 - datetime_2
# print(datetime_delta.seconds)
#

'''
А если нужно сделать прибавить к моменту времени несколько дней или часов? 
Например, если нам нужно определить, валиден ли код активации:
'''

# from datetime import datetime, timedelta

# user_created = datetime(year=2022, month=12, day=4, hour=15, minute=25, second=32)

# activation_period = timedelta(days=1, hours=12)

# datetime_now = datetime.now()
# if datetime_now < user_created + activation_period:
#     print('еще можно активировать аккаунт: {time_before}'.format(
#         time_before=datetime_now - user_created
#     ))
# else:
#     print('не хватило {time_after}'.format(
#         time_after=datetime_now - (user_created + activation_period)
#     ))



# from datetime import datetime

# now = datetime.now()

# print(now.year)
# print(now.month)
# print(now.hour)
# print(now.second)