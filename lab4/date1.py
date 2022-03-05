from datetime import date, timedelta 
a = date.today() - timedelta(5)
print("Current date is ", date.today())
print("Before 5 days ", a)