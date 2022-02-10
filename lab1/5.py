n, f = [int(n) for n in input().split()] 

pri = False
for i in range(2, n):
    if n%i==0:
        pri = True
        break

if n<500 and not pri and f%2==0:
    print("Good job!")
else:
    print("Try next time!")