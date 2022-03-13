import re
txt = input()
x = re.sub(r"(\w)(\s)+([A-Z])", r"\1 \3",txt)
print(x)