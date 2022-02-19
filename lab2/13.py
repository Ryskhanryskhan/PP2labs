k = [] 
while  True: 
    b = list(input().split()) 
    if b[0] == "0": 
        break 
    k.append(b) 
for i in range(len(k)): 
    k[i].reverse() 
k.sort() 
for i in range(len(k)): 
    k[i].reverse() 
for i in range(len(k)): 
    for j in range(3): 
        print(k[i][j], end = ' ') 
    print()