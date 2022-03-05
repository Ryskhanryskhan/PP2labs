from datetime import date, timedelta
a = date.today()
b = date.today() - timedelta(1)
c = date.today() + timedelta(1)
print("Yesterday is",b, "and", b.strftime("%A"))
print("Today is", a, "and", a.strftime("%A"))
print("Tomorrow is", c, "and", c.strftime("%A"))