n=int(input())

hi=[]
a="@gmail.com"
for i in range(0, n):
    s=input()
    if a in s:
        d=s.strip(a)
        hi.append(d)
        

print(*hi, sep = "\n")