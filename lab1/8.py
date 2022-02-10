from gettext import find


word=input()
letter=input()
e=""

for i in range(len(word)):
    if letter in word[i]:
        e+=str(i)+" "
re=e.split()

if(len(re)>2):
    print(re[0]+" "+re[len(re)-1])
if(len(re)==1):
    print(re[0])
if(len(re)==2):
    print(re[0]+" "+re[1])



'''
f=word.find(letter)
if not f==-1:
    e+=str(f)

d=word.find(letter)
if d!=-1 and not d==f:
    e+=" "
    e+=str(d)
if len(e)!=0:
    print(e)
'''