import re
txt = input()
x = re.findall(r"ab{2,3}", txt)
print(x)