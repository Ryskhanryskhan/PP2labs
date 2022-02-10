a=int(input())
z=str(input())
c=int(input())

if z=='k':
    res=a/1024
elif z=='b':
    res=a*1024
res=float(res)
res="{:.cf}".format(res)

print(res)

'''
if z=='k':
    print(round(a/1024, c))
elif z=='b':
    print(round(a*1024, c))
'''

