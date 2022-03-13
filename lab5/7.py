import re
txt = input()
def snake_to_camel(txt):
    x = re.findall("[a-z]+",txt)
    y = ""
    for i in x:
        y+=i[0].upper()+i[1:len(i)]
    return y
print(snake_to_camel(txt))