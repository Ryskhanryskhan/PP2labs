k = list(set(input().split()))

print(len(k))

k.sort()

for i in k:
    if '.' in i or ',' in i or '?' in i or '!' in i:
        print(i[:-1])
    else:
        print(i)