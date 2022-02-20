def filter_prime(k, m): 
    if m == 0: 
        return 
    if m == 1: 
        pri.append(k) 
    else: 
        if k % m != 0: 
            return filter_prime(k, m - 1) 
        else: 
            return 
 

hi = list(map(int, input().split())) 
pri = [] 
for i in range(len(hi)): 
    filter_prime(hi[i], hi[i] - 1) 
print(pri)