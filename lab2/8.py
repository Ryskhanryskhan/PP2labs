x, y = map(int, input().split()) 
ir = [] 
n = int(input()) 

for i in range(n): 
    ir.append(list(map(int, input().split()))) 
 
b = [] 
import math 
for i in range(n): 
    d = math.sqrt((x - ir[i][0])**2 + (y - ir[i][1])**2) 
    b.append (list((d, ir[i]))) 
 
b.sort() 
for t in b: 
    print(t[1][0], t[1][1])