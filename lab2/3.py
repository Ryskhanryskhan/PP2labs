size=int(input())
r=size
list=[0]*size
for i in range(size):
    list[i]=[0]*r
for i in range(size):
    for j in range(size):
        if(i==j):
            list[i][j]=i*j
        elif(i==0 or j==0):
            list[i][j]=i+j
for i in range(size):
    for j in range(size):
        print(list[i][j],end=' ')
    print()