s = input()
x = "".join(reversed(s))
if s == x:
    print("correct")
else:
    print("wrong")