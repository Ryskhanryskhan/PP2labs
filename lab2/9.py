g = int(input())
a = []

for i in range(g):
    k = input().split()
    if (len(k) == 2): 
        a.append(k[1])
    else: 
        print(a[0], end =' ')
        a.pop(0)