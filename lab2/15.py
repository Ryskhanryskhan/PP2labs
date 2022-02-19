def conag(s):
    nu = {'0': 'ZER', '1': 'ONE', '2': 'TWO', '3': 'THR', '4': 'FOU', '5': 'FIV', '6': 'SIX', '7': 'SEV', '8': 'EIG', '9': 'NIN'}
    return nu[s]

def trip(n):
    s = ''
    for i in str(n):
        s = s + conag(i)
    return s

def number(s):
    d = {'ZER': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOU': 4, 'FIV': 5, 'SIX': 6, 'SEV': 7, 'EIG': 8, 'NIN': 9}
    return d[s]

def add(a, b):
    powa, powb = len(a) // 3, len(b) // 3
    k, l = 0, 0
    for i in range(powa - 1, -1, -1):
        k = k + number(a[:3]) * (10 ** i)
        a = a[3:]
    for i in range(powb - 1, -1, -1):
        l = l + number(b[:3]) * (10 ** i)
        b = b[3:]
    return k + l

a, b = input().split('+')
print(trip(add(a, b)))