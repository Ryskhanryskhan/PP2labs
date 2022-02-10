word=str(input())

for i in word:
    if ord(i)>=65 and ord(i)<=90:
        l=chr(ord(i)+32)
        word=word.replace(i, l)
    

print(word)