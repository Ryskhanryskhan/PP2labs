h = input().split()
if(len(h) == 2):
    n = int(h[0])
    x = int(h[1])
if(len(h) == 1):
    n = int(h[0])
    x = int(input())
sum = 0
a = []
for i in range(n):
    a.append(x + 2*i)
for j in range(n):
    sum = sum ^ a[j]
print(sum)