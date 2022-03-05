import datetime
a = datetime.datetime.now()
b = datetime.datetime.now().replace(microsecond = 0)
print(a)
print(b)
