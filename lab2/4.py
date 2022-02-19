si=int(input()) 
list=['.']*si 
for i in range(si): 
    list[i]=['.']*si
if(si%2==0): 
    for i in range(si): 
        for j in range(si): 
            if(i>=j): 
                list[i][j]='#' 
elif(si%2==1): 
    for i in range(si): 
        for j in range(si): 
            if(i+j==si-1 or i+j>=si): 
                list[i][j]='#' 
for i in range(si): 
    for j in range(si): 
        print(list[i][j],end='')            
    print()