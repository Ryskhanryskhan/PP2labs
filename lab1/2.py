a=input()
sum=0

for i in range(0, len(a)):
    sum += int(ord(a[i]))
    i+=1

if sum>300:
    print("It is tasty!")
else:
    print("Oh, no!")