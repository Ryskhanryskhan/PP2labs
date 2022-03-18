s = input()
uppercase = 0
lowercase = 0
for i in s:
    if i.islower():
        lowercase += 1
    if i.isupper():
        uppercase += 1
print(uppercase)
print(lowercase)