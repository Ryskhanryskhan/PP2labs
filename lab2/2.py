num=int(input())
el=list(map(int, input().split()))
el.sort()
print(el[len(el)-2]*el[len(el)-1])