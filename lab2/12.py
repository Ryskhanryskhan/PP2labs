a = input()

def bra(sy):
    brackets = ['()', '{}', '[]']
    while any(r in sy for r in brackets):
        for i in brackets:
            sy = sy.replace(i, '')
    return not sy

if bra(a):
    print("Yes")
else:
    print("No")