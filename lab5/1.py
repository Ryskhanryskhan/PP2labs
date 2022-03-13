import re
txt = "abb and a0 and ab are given"
x = re.findall(r"ab", txt)
y = re.findall(r"a0", txt)
z = re.findall(r"abb", txt)
print(x)
print(y)
print(z)