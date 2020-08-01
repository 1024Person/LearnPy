import datetime
import time

print(datetime.time.hour)  # 对象，
print(time.localtime().tm_hour)
print(datetime.date.month)
d = datetime.date(2020, 7, 24)
print(datetime.date.ctime(d))

print(datetime.date.today())

timede = datetime.timedelta(weeks=4, days=5, hours=5)  # 这是在创建对象
d = datetime.datetime.now()
print(d)
result = d - timede
print(result)
