def selection(n):
    for i in range(0,n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
a = selection(50)
print(next(a))
print(next(a))
