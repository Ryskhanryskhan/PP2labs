def Vol(rad): 
    
    import math 
    print((4 / 3) * math.pi * rad**3) 

def palindrome(s):  
    s1 = "" 
    for i in range(len(s) - 1, -1, -1): 
        s1 += s[i] 
    if s1 == s: 
        return True 
    else: 
        return False

rad = float(input()) 
s=input()

if palindrome(s):
    Vol(rad)
else:
    print("it is not a palindrome")