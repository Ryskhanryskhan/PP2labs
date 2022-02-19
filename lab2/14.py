hi=[]
s=input()


while s!= "0":
  hi.append(int(s))
  s=input()

for i in range(len(hi)//2):
    print(hi[i]+hi[-i-1], end=" ")
if len(hi)%2:
   print(hi[len(hi)//2])