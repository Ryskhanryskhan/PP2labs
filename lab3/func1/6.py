def reversed(s): 
    wo = "" 
    for i in range(len(s) - 1, - 1, -1): 
        wo = wo + " " + s[i] 
    print(wo.strip()) 
 
s = input().split() 
reversed(s)