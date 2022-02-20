def unique(): 
    a = input().split() 
    un = [] 
    for x in a: 
        if x not in un: 
            un.append(x) 
    print(un) 
 
unique()