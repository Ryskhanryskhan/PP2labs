ze=[]
def password(s):
    up = lo = num = False
    for i in s:
        if i.isdigit():
           num=True
        elif i.isupper():
           up=True
        elif i.islower():
           lo=True
    return num and lo and up
for i in range(int(input())):
    c=input()
    if password(c) and c not in ze:
       ze.append(c)
print(len(ze), *sorted(ze), sep="\n")