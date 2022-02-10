hi=input()
d=0
for i in range(0, len(hi)):
    d+= int(hi[i]) * (2**(len(hi)-i))/2

print(int(d))