import re
txt = input()
def camel_to_snake(txt):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
print(camel_to_snake(txt))