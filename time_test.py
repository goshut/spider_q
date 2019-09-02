from datetime import datetime
from datetime import timedelta

t_now = datetime.now() - timedelta(days=1)
time = t_now.strftime('%Y-%m-%d')

s = datetime.now().strftime('%Y-%m-%d')
print(s)
# print(a)
# print(time)
# print(time2)
