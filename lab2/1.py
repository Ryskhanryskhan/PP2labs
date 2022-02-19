array=list(map(int, input().split()))
current=0
fin=True
for th, i in enumerate(array):
    current=max(current-1,i)
    if current<=0:
       if th != len(array)-1:
          fin=False
       break
if fin:
   print(1)
else:
   print(0)
