comp={}
for i in range(int(input())):
    s=input().split()
    if s[0] not in comp:
       comp[s[0]]=int(s[1])
    else:
       comp[s[0]]+=int(s[1])
m=max(comp.values())
for i in sorted(comp.keys()):
  print(i, end=" ")
  if comp[i]==m:
     print("is lucky!")
  else:
     print(f"has to receive {m - comp[i]} tenge")