from cmath import tan
import math
a = int(input())
b = int(input())
tg = math.tan((math.pi)/b)
s = 0.25 * a * a * b / tg
print(s)